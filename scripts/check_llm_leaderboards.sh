#!/usr/bin/env bash
# check_llm_leaderboards.sh
#
# What: Checks LLM leaderboards for models best suited to a specific job type
# Why: Models improve rapidly; leaderboards show current best for each task
# Usage: ./scripts/check_llm_leaderboards.sh [job_type]

set -euo pipefail

JOB_TYPE="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

usage() {
    echo "Usage: $0 [job_type]"
    echo ""
    echo "Check LLM leaderboards for models best suited to specific jobs."
    echo ""
    echo "Job types:"
    echo "  technical_reasoning  - Deep multi-step technical analysis"
    echo "  product_strategy     - Strategic product decisions"
    echo "  code_generation      - Writing/debugging code"
    echo "  math_reasoning       - Mathematical problem solving"
    echo "  creative_writing     - Content generation"
    echo "  general              - General purpose tasks"
    echo ""
    echo "Examples:"
    echo "  $0 technical_reasoning"
    echo "  $0 product_strategy"
    exit 1
}

get_leaderboards_for_job() {
    local job="$1"
    
    echo -e "${BLUE}Recommended leaderboards for: $job${NC}"
    echo ""
    
    case "$job" in
        technical_reasoning)
            echo "Primary Leaderboards:"
            echo "  - Vellum LLM Leaderboard: GPQA Diamond benchmark"
            echo "    URL: https://www.vellum.ai/llm-leaderboard"
            echo "    Focus: Graduate-level expert reasoning"
            echo ""
            echo "  - Artificial Analysis: Quality + Speed"
            echo "    URL: https://artificialanalysis.ai/leaderboards/models"
            echo "    Focus: Performance vs cost tradeoffs"
            echo ""
            echo "Secondary:"
            echo "  - LM Arena: Technical conversation quality"
            echo "    URL: https://lmarena.ai"
            echo ""
            echo -e "${YELLOW}Check for models scoring >75% on GPQA Diamond${NC}"
            ;;
            
        product_strategy)
            echo "Primary Leaderboards:"
            echo "  - LM Arena (Chatbot Arena): User preference"
            echo "    URL: https://lmarena.ai"
            echo "    Focus: Multi-turn reasoning, strategic thinking"
            echo ""
            echo "  - Vellum LLM Leaderboard: Reasoning benchmarks"
            echo "    URL: https://www.vellum.ai/llm-leaderboard"
            echo ""
            echo "Secondary:"
            echo "  - Artificial Analysis: Context window + quality"
            echo "    URL: https://artificialanalysis.ai/leaderboards/models"
            echo ""
            echo -e "${YELLOW}Check for models strong in multi-turn dialogue${NC}"
            ;;
            
        code_generation)
            echo "Primary Leaderboards:"
            echo "  - Vellum LLM Leaderboard: SWE-Bench scores"
            echo "    URL: https://www.vellum.ai/llm-leaderboard"
            echo "    Focus: Real-world coding tasks"
            echo ""
            echo "  - Stack AI: HumanEval benchmark"
            echo "    URL: https://www.stack-ai.com/llm-leaderboard"
            echo "    Focus: Code generation quality"
            echo ""
            echo "Secondary:"
            echo "  - Artificial Analysis: Speed for code tasks"
            echo "    URL: https://artificialanalysis.ai/leaderboards/models"
            echo ""
            echo -e "${YELLOW}Check for models scoring >60% on SWE-Bench${NC}"
            ;;
            
        math_reasoning)
            echo "Primary Leaderboards:"
            echo "  - Vellum LLM Leaderboard: AIME 2024/2025"
            echo "    URL: https://www.vellum.ai/llm-leaderboard"
            echo "    Focus: High school competition math"
            echo ""
            echo "  - Stack AI: GSM8K, MATH benchmarks"
            echo "    URL: https://www.stack-ai.com/llm-leaderboard"
            echo "    Focus: Multi-step math reasoning"
            echo ""
            echo -e "${YELLOW}Check for models scoring >90% on AIME${NC}"
            ;;
            
        creative_writing)
            echo "Primary Leaderboards:"
            echo "  - LM Arena: Creative writing category"
            echo "    URL: https://lmarena.ai"
            echo "    Focus: Human preference for creative content"
            echo ""
            echo "  - Artificial Analysis: Quality scores"
            echo "    URL: https://artificialanalysis.ai/leaderboards/models"
            echo ""
            echo -e "${YELLOW}User preference matters more than benchmarks here${NC}"
            ;;
            
        general)
            echo "Primary Leaderboards:"
            echo "  - LM Arena: Overall rankings"
            echo "    URL: https://lmarena.ai"
            echo ""
            echo "  - Artificial Analysis: Quality + Speed + Cost"
            echo "    URL: https://artificialanalysis.ai/leaderboards/models"
            echo ""
            echo "  - Vellum LLM Leaderboard: Multi-benchmark"
            echo "    URL: https://www.vellum.ai/llm-leaderboard"
            echo ""
            echo -e "${YELLOW}Consider cost/speed tradeoffs for general tasks${NC}"
            ;;
            
        *)
            echo -e "${RED}Unknown job type: $job${NC}"
            echo ""
            usage
            ;;
    esac
    
    echo ""
    echo -e "${BLUE}How to use these leaderboards:${NC}"
    echo "1. Visit the URLs above"
    echo "2. Check current top models for relevant benchmarks"
    echo "3. Compare to your current model"
    echo "4. If >10% improvement available, test new model"
    echo "5. Update subagent if new model proves better"
    echo ""
    echo -e "${BLUE}Current date:${NC} $(date +%Y-%m-%d)"
    echo "Leaderboards update frequently - check every 3 months minimum"
}

main() {
    if [[ -z "$JOB_TYPE" ]]; then
        usage
    fi
    
    get_leaderboards_for_job "$JOB_TYPE"
}

main
