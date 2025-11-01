#!/bin/bash

# Design Review Checklist Tool
# Generates comprehensive design review checklists based on Northwestern MPD2 methodology

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Design review phase templates
CONCEPT_REVIEW_ITEMS=(
    "Problem definition clarity and scope"
    "Market opportunity validation"
    "User needs and requirements analysis"
    "Competitive landscape assessment"
    "Technology feasibility evaluation"
    "Resource requirements estimation"
    "Risk identification and mitigation strategies"
    "Success criteria definition"
)

DESIGN_DEVELOPMENT_ITEMS=(
    "Design concept alignment with requirements"
    "Materials selection rationale"
    "Manufacturing process compatibility"
    "Safety and regulatory compliance"
    "Cost targets and analysis"
    "Environmental impact assessment"
    "Quality standards and testing approach"
    "Intellectual property considerations"
    "Supplier and supply chain evaluation"
)

PROTOTYPE_REVIEW_ITEMS=(
    "Prototype functionality validation"
    "Performance against specifications"
    "User testing feedback integration"
    "Manufacturing trial results"
    "Quality control and testing outcomes"
    "Cost validation and optimization"
    "Timeline and milestone assessment"
    "Risk mitigation effectiveness"
    "Design for manufacturing optimization"
)

PRODUCTION_READINESS_ITEMS=(
    "Final design freeze and documentation"
    "Manufacturing process validation"
    "Quality assurance system implementation"
    "Supply chain readiness confirmation"
    "Regulatory approvals and certifications"
    "Launch planning and execution strategy"
    "Post-launch monitoring plan"
    "Customer support and service strategy"
)

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Generate design review checklists for MPD2-based product development"
    echo ""
    echo "Options:"
    echo "  -p, --phase PHASE        Design review phase (concept|development|prototype|production)"
    echo "  -o, --output FILE        Output checklist to file (default: stdout)"
    echo "  -f, --format FORMAT      Output format (markdown|text|json) (default: markdown)"
    echo "  -c, --custom FILE        Custom checklist items from file"
    echo "  -t, --template           Generate template file for custom checklist"
    echo "  -h, --help              Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 --phase concept --output concept_review.md"
    echo "  $0 --phase development --format json"
    echo "  $0 --template"
}

generate_template() {
    local template_file="custom_checklist_template.json"
    cat > "$template_file" << 'EOF'
{
  "phase": "custom",
  "description": "Custom design review phase",
  "checklist_items": [
    {
      "category": "Category 1",
      "items": [
        "Custom checklist item 1",
        "Custom checklist item 2"
      ]
    },
    {
      "category": "Category 2", 
      "items": [
        "Custom checklist item 3",
        "Custom checklist item 4"
      ]
    }
  ],
  "additional_notes": [
    "Important consideration 1",
    "Important consideration 2"
  ]
}
EOF
    echo -e "${GREEN}✅ Created template file: $template_file${NC}"
    echo "Edit this file and use with --custom option"
}

generate_checklist_markdown() {
    local phase="$1"
    local output_file="$2"
    
    {
        echo "# Design Review Checklist - $(echo $phase | tr '[:lower:]' '[:upper:]') Phase"
        echo ""
        echo "**Project**: _[Project Name]_"
        echo "**Date**: $(date '+%Y-%m-%d')"
        echo "**Reviewer(s)**: _[Reviewer Names]_"
        echo "**Phase**: $phase"
        echo ""
        echo "## Review Criteria"
        echo ""
        
        case $phase in
            "concept")
                items=("${CONCEPT_REVIEW_ITEMS[@]}")
                ;;
            "development")
                items=("${DESIGN_DEVELOPMENT_ITEMS[@]}")
                ;;
            "prototype")
                items=("${PROTOTYPE_REVIEW_ITEMS[@]}")
                ;;
            "production")
                items=("${PRODUCTION_READINESS_ITEMS[@]}")
                ;;
        esac
        
        for i in "${!items[@]}"; do
            echo "- [ ] **$(($i + 1)). ${items[$i]}**"
            echo "  - Status: _[Pass/Fail/Needs Work]_"
            echo "  - Notes: _[Comments and observations]_"
            echo "  - Action Items: _[Required actions if any]_"
            echo ""
        done
        
        echo "## Overall Assessment"
        echo ""
        echo "- [ ] **Ready to proceed to next phase**"
        echo "- [ ] **Conditional approval with action items**"
        echo "- [ ] **Requires significant rework**"
        echo ""
        echo "### Summary Comments"
        echo "_[Overall assessment and key findings]_"
        echo ""
        echo "### Action Items"
        echo "1. _[Action item 1]_ - Owner: _[Name]_ - Due: _[Date]_"
        echo "2. _[Action item 2]_ - Owner: _[Name]_ - Due: _[Date]_"
        echo ""
        echo "### Next Steps"
        echo "_[What happens next in the development process]_"
        echo ""
        echo "---"
        echo "*Generated by MPD2 Design Review Checklist Tool*"
        
    } > "$output_file"
}

generate_checklist_json() {
    local phase="$1"
    local output_file="$2"
    
    case $phase in
        "concept")
            items=("${CONCEPT_REVIEW_ITEMS[@]}")
            ;;
        "development")
            items=("${DESIGN_DEVELOPMENT_ITEMS[@]}")
            ;;
        "prototype")
            items=("${PROTOTYPE_REVIEW_ITEMS[@]}")
            ;;
        "production")
            items=("${PRODUCTION_READINESS_ITEMS[@]}")
            ;;
    esac
    
    {
        echo "{"
        echo "  \"phase\": \"$phase\","
        echo "  \"date\": \"$(date '+%Y-%m-%d')\","
        echo "  \"checklist_items\": ["
        
        for i in "${!items[@]}"; do
            echo "    {"
            echo "      \"id\": $(($i + 1)),"
            echo "      \"description\": \"${items[$i]}\","
            echo "      \"status\": \"pending\","
            echo "      \"notes\": \"\","
            echo "      \"action_items\": []"
            if [ $i -eq $((${#items[@]} - 1)) ]; then
                echo "    }"
            else
                echo "    },"
            fi
        done
        
        echo "  ],"
        echo "  \"overall_assessment\": \"\","
        echo "  \"decision\": \"\","
        echo "  \"next_steps\": \"\""
        echo "}"
        
    } > "$output_file"
}

load_custom_checklist() {
    local custom_file="$1"
    local output_file="$2"
    local format="$3"
    
    if [[ ! -f "$custom_file" ]]; then
        echo -e "${RED}❌ Error: Custom checklist file not found: $custom_file${NC}"
        exit 1
    fi
    
    # For now, just copy the custom file (assuming it's already in the desired format)
    cp "$custom_file" "$output_file"
    echo -e "${GREEN}✅ Generated custom checklist: $output_file${NC}"
}

main() {
    local phase=""
    local output_file=""
    local format="markdown"
    local custom_file=""
    local show_template=false
    
    # Parse command line arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
            -p|--phase)
                phase="$2"
                shift 2
                ;;
            -o|--output)
                output_file="$2"
                shift 2
                ;;
            -f|--format)
                format="$2"
                shift 2
                ;;
            -c|--custom)
                custom_file="$2"
                shift 2
                ;;
            -t|--template)
                show_template=true
                shift
                ;;
            -h|--help)
                usage
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Error: Unknown option $1${NC}"
                usage
                exit 1
                ;;
        esac
    done
    
    # Handle template generation
    if [[ "$show_template" == true ]]; then
        generate_template
        exit 0
    fi
    
    # Handle custom checklist
    if [[ -n "$custom_file" ]]; then
        if [[ -z "$output_file" ]]; then
            output_file="custom_checklist.$format"
        fi
        load_custom_checklist "$custom_file" "$output_file" "$format"
        exit 0
    fi
    
    # Validate required parameters
    if [[ -z "$phase" ]]; then
        echo -e "${RED}❌ Error: Phase is required${NC}"
        usage
        exit 1
    fi
    
    # Validate phase
    if [[ ! "$phase" =~ ^(concept|development|prototype|production)$ ]]; then
        echo -e "${RED}❌ Error: Invalid phase. Must be one of: concept, development, prototype, production${NC}"
        exit 1
    fi
    
    # Set default output file if not provided
    if [[ -z "$output_file" ]]; then
        if [[ "$format" == "markdown" ]]; then
            output_file="${phase}_review_checklist.md"
        elif [[ "$format" == "json" ]]; then
            output_file="${phase}_review_checklist.json"
        else
            output_file="${phase}_review_checklist.txt"
        fi
    fi
    
    # Generate checklist based on format
    case $format in
        "markdown")
            generate_checklist_markdown "$phase" "$output_file"
            ;;
        "json")
            generate_checklist_json "$phase" "$output_file"
            ;;
        "text")
            generate_checklist_markdown "$phase" "$output_file"
            # Convert markdown to plain text (simplified)
            sed -i '' 's/^# //' "$output_file"
            sed -i '' 's/^## //' "$output_file"
            sed -i '' 's/\*\*//g' "$output_file"
            sed -i '' 's/^- \[ \] /☐ /' "$output_file"
            ;;
        *)
            echo -e "${RED}❌ Error: Invalid format. Must be one of: markdown, text, json${NC}"
            exit 1
            ;;
    esac
    
    echo -e "${GREEN}✅ Generated ${phase} phase checklist: $output_file${NC}"
    echo -e "${BLUE}📋 Review the checklist and customize for your project needs${NC}"
}

main "$@"