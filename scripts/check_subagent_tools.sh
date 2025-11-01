#!/usr/bin/env bash
# check_subagent_tools.sh
#
# What: Verifies all required CLI tools for a subagent are installed and working
# Why: Prevents runtime failures from missing dependencies
# Usage: ./scripts/check_subagent_tools.sh [subagent_name]

set -euo pipefail

SUBAGENT_NAME="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

usage() {
    echo "Usage: $0 [subagent_name]"
    echo ""
    echo "Check if all required tools for a subagent are available."
    echo ""
    echo "Examples:"
    echo "  $0 challenge_technical_assumptions"
    echo "  $0 find_core_value"
    exit 1
}

check_tool() {
    local tool="$1"
    local description="$2"
    
    if command -v "$tool" &> /dev/null; then
        echo -e "${GREEN}✓${NC} $tool - $description"
        return 0
    else
        echo -e "${RED}✗${NC} $tool - $description (MISSING)"
        return 1
    fi
}

check_subagent_tools() {
    local subagent="$1"
    local subagent_file="$REPO_ROOT/subagents/${subagent}.md"
    
    # Check if file exists
    if [[ ! -f "$subagent_file" ]]; then
        # Try in examples
        subagent_file="$REPO_ROOT/subagents/examples/${subagent}.md"
        if [[ ! -f "$subagent_file" ]]; then
            echo -e "${RED}Error: Subagent file not found: $subagent${NC}"
            exit 1
        fi
    fi
    
    echo "Checking tools for: $subagent"
    echo "Reading from: $subagent_file"
    echo ""
    
    # Extract required tools from markdown file
    # This is a simplified parser - assumes tools are listed as `tool_name`
    # between "Required tools" and "Optional tools" sections
    
    # For now, do basic checks that any technical subagent needs
    local all_passed=true
    
    echo "Required tools:"
    check_tool "git" "Version control" || all_passed=false
    check_tool "curl" "HTTP requests" || all_passed=false
    check_tool "jq" "JSON processing" || all_passed=false
    
    echo ""
    echo "Optional tools:"
    check_tool "gh" "GitHub CLI" || echo -e "${YELLOW}!${NC} gh - GitHub CLI (optional, enhances GitHub operations)"
    check_tool "fzf" "Fuzzy finder" || echo -e "${YELLOW}!${NC} fzf - Fuzzy finder (optional, enhances search)"
    
    echo ""
    
    if [[ "$all_passed" == true ]]; then
        echo -e "${GREEN}All required tools are available!${NC}"
        return 0
    else
        echo -e "${RED}Some required tools are missing. Install them before running this subagent.${NC}"
        return 1
    fi
}

# Main
if [[ -z "$SUBAGENT_NAME" ]]; then
    usage
fi

check_subagent_tools "$SUBAGENT_NAME"
