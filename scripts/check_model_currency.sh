#!/usr/bin/env bash
# check_model_currency.sh
#
# What: Checks if the LLM assigned to a subagent is still relevant and up-to-date
# Why: Models improve rapidly; outdated assignments hurt performance
# Usage: ./scripts/check_model_currency.sh [subagent_name]

set -euo pipefail

SUBAGENT_NAME="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MODEL_REGISTRY="$SCRIPT_DIR/model_registry.json"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    echo "Usage: $0 [subagent_name]"
    echo ""
    echo "Check if the assigned LLM is still current and relevant."
    echo ""
    echo "Examples:"
    echo "  $0 challenge_technical_assumptions"
    echo "  $0 find_core_value"
    exit 1
}

# Get current date as YYYY-MM-DD
current_date() {
    date +%Y-%m-%d
}

# Calculate days between two dates
days_between() {
    local date1="$1"
    local date2="$2"
    
    local d1_sec=$(date -d "$date1" +%s 2>/dev/null || date -j -f "%Y-%m-%d" "$date1" +%s)
    local d2_sec=$(date -d "$date2" +%s 2>/dev/null || date -j -f "%Y-%m-%d" "$date2" +%s)
    
    echo $(( (d2_sec - d1_sec) / 86400 ))
}

extract_model_info() {
    local subagent="$1"
    local subagent_file="$REPO_ROOT/subagents/${subagent}.md"
    
    if [[ ! -f "$subagent_file" ]]; then
        subagent_file="$REPO_ROOT/subagents/examples/${subagent}.md"
        if [[ ! -f "$subagent_file" ]]; then
            echo -e "${RED}Error: Subagent file not found: $subagent${NC}"
            exit 1
        fi
    fi
    
    # Extract model configuration section
    # Look for "Ideal model:" and "Last reviewed:" lines
    local ideal_model=$(grep "^\*\*Ideal model:\*\*" "$subagent_file" | sed 's/.*`\(.*\)`.*/\1/' | head -1)
    local last_reviewed=$(grep "^- Last reviewed:" "$subagent_file" | sed 's/.*: //' | head -1)
    
    echo "$ideal_model|$last_reviewed"
}

check_model_registry() {
    local model="$1"
    
    # If registry doesn't exist, create a minimal one
    if [[ ! -f "$MODEL_REGISTRY" ]]; then
        cat > "$MODEL_REGISTRY" <<EOF
{
  "models": {
    "claude-sonnet-4-5-20250929": {
      "released": "2025-09-29",
      "context_window": 200000,
      "notes": "Current best for complex reasoning"
    },
    "claude-sonnet-4-20250514": {
      "released": "2025-05-14",
      "context_window": 200000,
      "notes": "Good for most tasks"
    },
    "gpt-4-turbo-2024-04-09": {
      "released": "2024-04-09",
      "context_window": 128000,
      "notes": "Solid but aging"
    },
    "gpt-4o-2024-08-06": {
      "released": "2024-08-06",
      "context_window": 128000,
      "notes": "Fast, capable"
    }
  },
  "recommendations": {
    "technical_reasoning": "claude-sonnet-4-5-20250929",
    "product_strategy": "claude-sonnet-4-5-20250929",
    "code_generation": "claude-sonnet-4-5-20250929",
    "general": "claude-sonnet-4-20250514"
  }
}
EOF
    fi
    
    # Query registry (requires jq)
    if command -v jq &> /dev/null; then
        jq -r ".models[\"$model\"] // \"not_found\"" "$MODEL_REGISTRY"
    else
        echo "jq not installed - cannot query model registry"
    fi
}

main() {
    if [[ -z "$SUBAGENT_NAME" ]]; then
        usage
    fi
    
    echo "Checking model currency for: $SUBAGENT_NAME"
    echo ""
    
    # Extract model info from subagent file
    local info=$(extract_model_info "$SUBAGENT_NAME")
    local assigned_model=$(echo "$info" | cut -d'|' -f1)
    local last_reviewed=$(echo "$info" | cut -d'|' -f2)
    
    if [[ -z "$assigned_model" ]]; then
        echo -e "${RED}✗ No model assigned${NC}"
        echo "Add LLM Configuration section to subagent file"
        exit 1
    fi
    
    echo -e "${BLUE}Current assignment:${NC}"
    echo "  Model: $assigned_model"
    echo "  Last reviewed: ${last_reviewed:-never}"
    echo ""
    
    # Check if review is overdue (>90 days)
    if [[ -n "$last_reviewed" ]] && [[ "$last_reviewed" != "never" ]] && [[ "$last_reviewed" != "YYYY-MM-DD" ]]; then
        local days_since=$(days_between "$last_reviewed" "$(current_date)")
        
        if [[ $days_since -gt 90 ]]; then
            echo -e "${YELLOW}⚠ Review overdue${NC} (${days_since} days since last review)"
            echo "  Recommendation: Review model assignment"
        else
            echo -e "${GREEN}✓ Recently reviewed${NC} (${days_since} days ago)"
        fi
    else
        echo -e "${YELLOW}⚠ No review date found${NC}"
        echo "  Add 'Last reviewed: $(current_date)' to subagent file"
    fi
    echo ""
    
    # Check model registry
    echo -e "${BLUE}Model information:${NC}"
    local model_info=$(check_model_registry "$assigned_model")
    
    if [[ "$model_info" != "not_found" ]] && [[ "$model_info" != "jq not installed"* ]]; then
        echo "$model_info" | jq '.' 2>/dev/null || echo "$model_info"
    else
        echo "  Model not in registry or jq not available"
    fi
    echo ""
    
    # Recommendations
    echo -e "${BLUE}Recommendations:${NC}"
    echo "1. Review model assignment every 3 months"
    echo "2. Benchmark performance metrics regularly"
    echo "3. Test newer models when available"
    echo "4. Update 'Last reviewed' date after checks"
    echo ""
    echo "To update model assignment:"
    echo "  1. Edit subagents/${SUBAGENT_NAME}.md"
    echo "  2. Update 'Ideal model' field"
    echo "  3. Update 'Last reviewed' date"
    echo "  4. Document why change was made"
}

main
