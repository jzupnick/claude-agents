#!/usr/bin/env bash
# check_agent_tools.sh
#
# What: Verify required CLI tools for specific agents are installed and working
# Why: Ensure agents can run autonomously without missing dependencies
# Usage: ./check_agent_tools.sh [agent_name]

set -euo pipefail

AGENT_NAME="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENTS_DIR="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Tool definitions for each agent
declare -A IOS_EMERGENCY_SYSTEMS_ARCHITECT_REQUIRED=(
    ["xcodebuild"]="Xcode command-line tools for iOS project builds"
    ["security"]="macOS security framework for certificate management"
    ["plutil"]="Property list utility for iOS configuration"
)

declare -A IOS_EMERGENCY_SYSTEMS_ARCHITECT_OPTIONAL=(
    ["xcpretty"]="Xcode build output formatting"
    ["ios-sim"]="iOS Simulator command-line control"
)

declare -A SWIFTUI_PERFORMANCE_OPTIMIZER_REQUIRED=(
    ["xcodebuild"]="Xcode command-line tools for performance builds"
    ["instruments"]="Xcode Instruments for performance profiling"
    ["swiftlint"]="Swift code quality enforcement"
)

declare -A SWIFTUI_PERFORMANCE_OPTIMIZER_OPTIONAL=(
    ["periphery"]="Dead code detection"
    ["sourcery"]="Code generation for performance optimization"
)

declare -A MULTI_AGENT_ORCHESTRATOR_REQUIRED=(
    ["jq"]="JSON processing for agent coordination"
    ["curl"]="HTTP requests for agent communication"
)

declare -A MULTI_AGENT_ORCHESTRATOR_OPTIONAL=(
    ["httpie"]="User-friendly HTTP client"
    ["parallel"]="Parallel execution of agent tasks"
)

declare -A PRODUCT_PRIORITIZATION_STRATEGIST_REQUIRED=(
    ["python3"]="Python for data analysis and RICE calculations"
    ["jq"]="JSON data processing"
)

declare -A PRODUCT_PRIORITIZATION_STRATEGIST_OPTIONAL=(
    ["R"]="Statistical analysis for prioritization modeling"
    ["sqlite3"]="Local database for metrics tracking"
)

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check tool and provide installation guidance
check_tool() {
    local tool="$1"
    local description="$2"
    local is_required="$3"
    
    if command_exists "$tool"; then
        echo -e "${GREEN}✓${NC} $tool - $description"
        return 0
    else
        if [ "$is_required" = "true" ]; then
            echo -e "${RED}✗${NC} $tool - $description (REQUIRED)"
            return 1
        else
            echo -e "${YELLOW}?${NC} $tool - $description (optional)"
            return 0
        fi
    fi
}

# Function to provide installation instructions
provide_installation_instructions() {
    local agent="$1"
    
    echo ""
    echo -e "${BLUE}Installation Instructions for $agent:${NC}"
    echo ""
    
    case "$agent" in
        "ios-emergency-systems-architect")
            echo "Required tools:"
            echo "  xcodebuild: Install Xcode from App Store, then run 'xcode-select --install'"
            echo "  security: Built into macOS"
            echo "  plutil: Built into macOS"
            echo ""
            echo "Optional tools:"
            echo "  xcpretty: gem install xcpretty"
            echo "  ios-sim: npm install -g ios-sim"
            ;;
        "swiftui-performance-optimizer")
            echo "Required tools:"
            echo "  xcodebuild: Install Xcode from App Store, then run 'xcode-select --install'"
            echo "  instruments: Included with Xcode installation"
            echo "  swiftlint: brew install swiftlint"
            echo ""
            echo "Optional tools:"
            echo "  periphery: brew install periphery"
            echo "  sourcery: brew install sourcery"
            ;;
        "multi-agent-orchestrator")
            echo "Required tools:"
            echo "  jq: brew install jq"
            echo "  curl: Built into macOS/Linux"
            echo ""
            echo "Optional tools:"
            echo "  httpie: brew install httpie"
            echo "  parallel: brew install parallel"
            ;;
        "product-prioritization-strategist")
            echo "Required tools:"
            echo "  python3: brew install python3 (or use system Python)"
            echo "  jq: brew install jq"
            echo ""
            echo "Optional tools:"
            echo "  R: brew install r"
            echo "  sqlite3: Built into macOS/Linux"
            ;;
        *)
            echo "No specific installation instructions available for: $agent"
            ;;
    esac
}

# Function to check specific agent tools
check_agent_tools() {
    local agent="$1"
    local missing_required=0
    local missing_optional=0
    
    echo -e "${BLUE}Checking tools for agent: $agent${NC}"
    echo ""
    
    # Convert agent name to variable-safe format
    local var_prefix="${agent^^}"
    var_prefix="${var_prefix//-/_}"
    
    # Check required tools
    local required_var="${var_prefix}_REQUIRED[@]"
    local optional_var="${var_prefix}_OPTIONAL[@]"
    
    echo "Required tools:"
    if declare -p "${var_prefix}_REQUIRED" >/dev/null 2>&1; then
        local -n required_tools="${var_prefix}_REQUIRED"
        for tool in "${!required_tools[@]}"; do
            if ! check_tool "$tool" "${required_tools[$tool]}" "true"; then
                ((missing_required++))
            fi
        done
    else
        echo "  No required tools defined for this agent"
    fi
    
    echo ""
    echo "Optional tools:"
    if declare -p "${var_prefix}_OPTIONAL" >/dev/null 2>&1; then
        local -n optional_tools="${var_prefix}_OPTIONAL"
        for tool in "${!optional_tools[@]}"; do
            if ! check_tool "$tool" "${optional_tools[$tool]}" "false"; then
                ((missing_optional++))
            fi
        done
    else
        echo "  No optional tools defined for this agent"
    fi
    
    echo ""
    echo "Summary:"
    if [ $missing_required -eq 0 ]; then
        echo -e "${GREEN}✓ All required tools available${NC}"
    else
        echo -e "${RED}✗ $missing_required required tools missing${NC}"
    fi
    
    if [ $missing_optional -gt 0 ]; then
        echo -e "${YELLOW}? $missing_optional optional tools missing${NC}"
    else
        echo -e "${GREEN}✓ All optional tools available${NC}"
    fi
    
    if [ $missing_required -gt 0 ]; then
        provide_installation_instructions "$agent"
        return 1
    fi
    
    return 0
}

# Function to list available agents
list_available_agents() {
    echo "Available agents for tool checking:"
    echo "  - ios-emergency-systems-architect"
    echo "  - swiftui-performance-optimizer"
    echo "  - multi-agent-orchestrator"
    echo "  - product-prioritization-strategist"
    echo ""
    echo "Usage: $0 <agent-name>"
}

# Main execution
if [ -z "$AGENT_NAME" ]; then
    echo -e "${YELLOW}No agent specified${NC}"
    echo ""
    list_available_agents
    exit 1
fi

case "$AGENT_NAME" in
    "ios-emergency-systems-architect"|"swiftui-performance-optimizer"|"multi-agent-orchestrator"|"product-prioritization-strategist")
        if check_agent_tools "$AGENT_NAME"; then
            echo ""
            echo -e "${GREEN}✓ Agent $AGENT_NAME is ready to run autonomously${NC}"
            exit 0
        else
            echo ""
            echo -e "${RED}✗ Agent $AGENT_NAME has missing required tools${NC}"
            exit 1
        fi
        ;;
    *)
        echo -e "${RED}Unknown agent: $AGENT_NAME${NC}"
        echo ""
        list_available_agents
        exit 1
        ;;
esac