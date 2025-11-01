#!/usr/bin/env bash
# agent_performance_monitor.sh
#
# What: Monitor agent performance and effectiveness across projects
# Why: Track agent ROI and identify optimization opportunities
# Usage: ./agent_performance_monitor.sh [--report] [--agent agent_name]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="$(dirname "$SCRIPT_DIR")"
METRICS_FILE="$SCRIPT_DIR/agent_metrics.json"
REPORT_FILE="$SCRIPT_DIR/agent_performance_report.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Parse command line arguments
GENERATE_REPORT=false
SPECIFIC_AGENT=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --report)
            GENERATE_REPORT=true
            shift
            ;;
        --agent)
            SPECIFIC_AGENT="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Function to initialize metrics file if it doesn't exist
initialize_metrics() {
    if [ ! -f "$METRICS_FILE" ]; then
        cat > "$METRICS_FILE" << 'EOF'
{
  "last_updated": "",
  "agents": {}
}
EOF
    fi
}

# Function to record agent usage
record_agent_usage() {
    local agent_name="$1"
    local project="$2"
    local task_type="$3"
    local duration_minutes="$4"
    local success_rating="$5"
    local notes="$6"
    
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    
    # Update metrics file
    jq --arg agent "$agent_name" \
       --arg project "$project" \
       --arg task "$task_type" \
       --arg duration "$duration_minutes" \
       --arg rating "$success_rating" \
       --arg notes "$notes" \
       --arg timestamp "$timestamp" '
       .last_updated = $timestamp |
       .agents[$agent] = (.agents[$agent] // {
         "total_uses": 0,
         "total_duration_minutes": 0,
         "average_rating": 0,
         "usage_history": []
       }) |
       .agents[$agent].total_uses += 1 |
       .agents[$agent].total_duration_minutes += ($duration | tonumber) |
       .agents[$agent].usage_history += [{
         "timestamp": $timestamp,
         "project": $project,
         "task_type": $task,
         "duration_minutes": ($duration | tonumber),
         "success_rating": ($rating | tonumber),
         "notes": $notes
       }] |
       .agents[$agent].average_rating = (
         .agents[$agent].usage_history | 
         map(.success_rating) | 
         add / length
       )
    ' "$METRICS_FILE" > "$METRICS_FILE.tmp" && mv "$METRICS_FILE.tmp" "$METRICS_FILE"
    
    echo -e "${GREEN}✓ Recorded usage for agent: $agent_name${NC}"
}

# Function to get agent performance metrics
get_agent_metrics() {
    local agent_name="$1"
    
    if [ ! -f "$METRICS_FILE" ]; then
        echo "No metrics data available"
        return 1
    fi
    
    jq -r --arg agent "$agent_name" '
    if .agents[$agent] then
        .agents[$agent] | 
        "Total Uses: \(.total_uses)\n" +
        "Total Duration: \(.total_duration_minutes) minutes\n" +
        "Average Rating: \(.average_rating | . * 100 | round / 100)/5\n" +
        "Average Duration: \((.total_duration_minutes / .total_uses) | round) minutes per use"
    else
        "No data available for agent: " + $agent
    end
    ' "$METRICS_FILE"
}

# Function to generate performance report
generate_performance_report() {
    local current_date=$(date +"%Y-%m-%d")
    
    cat > "$REPORT_FILE" << EOF
# Agent Performance Report
Generated: $current_date

## Executive Summary

EOF
    
    if [ ! -f "$METRICS_FILE" ] || [ "$(jq '.agents | length' "$METRICS_FILE")" = "0" ]; then
        cat >> "$REPORT_FILE" << EOF
No agent usage data available yet. Start using agents and recording metrics to see performance insights.

## Getting Started

To record agent usage:
\`\`\`bash
./agent_performance_monitor.sh --record \\
  --agent "ios-emergency-systems-architect" \\
  --project "ab-demo" \\
  --task "emergency alert architecture" \\
  --duration 240 \\
  --rating 5 \\
  --notes "Excellent compliance specification"
\`\`\`

EOF
        return
    fi
    
    # Generate summary statistics
    local total_agents=$(jq '.agents | length' "$METRICS_FILE")
    local total_uses=$(jq '.agents | [.[].total_uses] | add // 0' "$METRICS_FILE")
    local total_duration=$(jq '.agents | [.[].total_duration_minutes] | add // 0' "$METRICS_FILE")
    local avg_rating=$(jq '.agents | [.[].average_rating] | add / length' "$METRICS_FILE")
    
    cat >> "$REPORT_FILE" << EOF
**Key Metrics:**
- Active Agents: $total_agents
- Total Agent Uses: $total_uses
- Total Time Invested: $total_duration minutes ($(echo "$total_duration / 60" | bc -l | xargs printf "%.1f") hours)
- Average Success Rating: $(echo "$avg_rating * 100" | bc -l | xargs printf "%.1f")/100

## Agent Performance Analysis

EOF
    
    # Generate per-agent analysis
    jq -r '
    .agents | to_entries | sort_by(-.value.average_rating) | .[] |
    "### " + .key + "\n\n" +
    "**Performance Metrics:**\n" +
    "- Total Uses: " + (.value.total_uses | tostring) + "\n" +
    "- Average Rating: " + ((.value.average_rating * 100 | round) / 100 | tostring) + "/5\n" +
    "- Total Duration: " + (.value.total_duration_minutes | tostring) + " minutes\n" +
    "- Avg Duration per Use: " + ((.value.total_duration_minutes / .value.total_uses | round) | tostring) + " minutes\n\n" +
    "**Recent Usage:**\n" +
    (
      .value.usage_history[-3:] | reverse | .[] |
      "- " + .timestamp[:10] + ": " + .task_type + " (" + (.success_rating | tostring) + "/5) - " + .notes
    ) + "\n\n"
    ' "$METRICS_FILE" >> "$REPORT_FILE"
    
    # Add recommendations
    cat >> "$REPORT_FILE" << EOF
## Recommendations

### High-Performing Agents
EOF
    
    jq -r '
    .agents | to_entries | 
    map(select(.value.average_rating >= 4.5 and .value.total_uses >= 2)) |
    sort_by(-.value.average_rating) | .[] |
    "- **" + .key + "**: " + ((.value.average_rating * 100 | round) / 100 | tostring) + "/5 rating with " + (.value.total_uses | tostring) + " uses - Consider expanding scope"
    ' "$METRICS_FILE" >> "$REPORT_FILE"
    
    cat >> "$REPORT_FILE" << EOF

### Agents Needing Attention
EOF
    
    jq -r '
    .agents | to_entries | 
    map(select(.value.average_rating < 3.5 or (.value.total_uses >= 3 and (.value.total_duration_minutes / .value.total_uses) > 120))) |
    sort_by(.value.average_rating) | .[] |
    "- **" + .key + "**: " + ((.value.average_rating * 100 | round) / 100 | tostring) + "/5 rating - Review capabilities and optimization opportunities"
    ' "$METRICS_FILE" >> "$REPORT_FILE"
    
    cat >> "$REPORT_FILE" << EOF

### Optimization Opportunities
- **High Duration Tasks**: Review agents with >120 minutes average duration for optimization potential
- **Low Usage Agents**: Consider whether rarely-used agents should be merged or deprecated
- **Success Patterns**: Replicate success patterns from high-performing agents in similar domains

## Next Steps

1. **For High Performers**: Expand scope or create specialized variants
2. **For Underperformers**: Analyze failure modes and improve capabilities
3. **For All Agents**: Continue tracking and monthly performance reviews

---
*Report generated by agent_performance_monitor.sh*
EOF
    
    echo -e "${GREEN}✓ Performance report generated: $REPORT_FILE${NC}"
}

# Function to display current metrics
display_metrics() {
    echo -e "${BLUE}=== Agent Performance Overview ===${NC}"
    echo ""
    
    if [ ! -f "$METRICS_FILE" ] || [ "$(jq '.agents | length' "$METRICS_FILE")" = "0" ]; then
        echo "No metrics data available yet."
        echo ""
        echo "To start tracking agent performance:"
        echo "1. Use agents in your projects"
        echo "2. Record usage with: ./agent_performance_monitor.sh --record [options]"
        echo "3. Generate reports with: ./agent_performance_monitor.sh --report"
        return
    fi
    
    if [ -n "$SPECIFIC_AGENT" ]; then
        echo "Metrics for agent: $SPECIFIC_AGENT"
        echo ""
        get_agent_metrics "$SPECIFIC_AGENT"
    else
        echo "All Agent Performance Summary:"
        echo ""
        
        jq -r '
        .agents | to_entries | sort_by(-.value.average_rating) | .[] |
        (.key | ascii_upcase) + ":\n" +
        "  Uses: " + (.value.total_uses | tostring) + 
        " | Rating: " + ((.value.average_rating * 100 | round) / 100 | tostring) + "/5" +
        " | Avg Duration: " + ((.value.total_duration_minutes / .value.total_uses | round) | tostring) + "min\n"
        ' "$METRICS_FILE"
    fi
}

# Interactive usage recording
interactive_record() {
    echo -e "${BLUE}=== Record Agent Usage ===${NC}"
    echo ""
    
    read -p "Agent name: " agent_name
    read -p "Project name: " project_name
    read -p "Task type: " task_type
    read -p "Duration (minutes): " duration
    read -p "Success rating (1-5): " rating
    read -p "Notes: " notes
    
    record_agent_usage "$agent_name" "$project_name" "$task_type" "$duration" "$rating" "$notes"
}

# Main execution
initialize_metrics

if [ "$GENERATE_REPORT" = true ]; then
    generate_performance_report
elif [ $# -eq 0 ]; then
    # Interactive mode
    echo -e "${BLUE}Agent Performance Monitor${NC}"
    echo ""
    echo "1. Display current metrics"
    echo "2. Record agent usage"
    echo "3. Generate performance report"
    echo ""
    read -p "Choose option (1-3): " choice
    
    case $choice in
        1)
            display_metrics
            ;;
        2)
            interactive_record
            ;;
        3)
            generate_performance_report
            ;;
        *)
            echo "Invalid choice"
            exit 1
            ;;
    esac
else
    display_metrics
fi