#!/bin/bash

# Northwestern MPD2 Design Decision System Health Check
# Validates system integrity and component integration

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
HEALTH_REPORT="$PROJECT_ROOT/system_health_report.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNING_CHECKS=0

# Health check functions
log() {
    echo -e "$1" | tee -a "$HEALTH_REPORT"
}

check_start() {
    local check_name="$1"
    ((TOTAL_CHECKS++))
    echo -n "Checking $check_name... "
}

check_pass() {
    ((PASSED_CHECKS++))
    echo -e "${GREEN}PASS${NC}"
    log "✅ $1"
}

check_fail() {
    ((FAILED_CHECKS++))
    echo -e "${RED}FAIL${NC}"
    log "❌ $1"
}

check_warning() {
    ((WARNING_CHECKS++))
    echo -e "${YELLOW}WARNING${NC}"
    log "⚠️ $1"
}

# Initialize health report
init_report() {
    cat > "$HEALTH_REPORT" << EOF
# Northwestern MPD2 Design Decision System Health Report
Generated: $TIMESTAMP

## System Overview
This report validates the integrity and integration of the Northwestern MPD2 enhanced design decision system.

## Health Check Results

EOF
}

# Layer 1: Core Primitives Health Check
check_layer1_primitives() {
    log "### Layer 1: Core Primitives"
    log ""
    
    # Check schemas
    check_start "Schema files"
    local schema_dir="$PROJECT_ROOT/design-system/primitives/schemas"
    if [[ -d "$schema_dir" ]]; then
        local schema_count=$(find "$schema_dir" -name "*.yaml" | wc -l)
        if [[ $schema_count -ge 6 ]]; then
            check_pass "Found $schema_count schema files"
        else
            check_warning "Only found $schema_count schema files (expected 6+)"
        fi
    else
        check_fail "Schema directory not found"
    fi
    
    # Check calculators
    check_start "Calculator implementations"
    local calc_dir="$PROJECT_ROOT/design-system/primitives/calculators"
    if [[ -d "$calc_dir" ]]; then
        local calc_count=$(find "$calc_dir" -name "*.py" | wc -l)
        if [[ $calc_count -ge 3 ]]; then
            check_pass "Found $calc_count calculator implementations"
        else
            check_warning "Only found $calc_count calculators (expected 3+)"
        fi
    else
        check_fail "Calculator directory not found"
    fi
    
    # Check generators
    check_start "Generator implementations"
    local gen_dir="$PROJECT_ROOT/design-system/primitives/generators"
    if [[ -d "$gen_dir" ]]; then
        local gen_count=$(find "$gen_dir" -name "*.py" | wc -l)
        if [[ $gen_count -ge 1 ]]; then
            check_pass "Found $gen_count generator implementations"
        else
            check_warning "Only found $gen_count generators (expected 1+)"
        fi
    else
        check_fail "Generator directory not found"
    fi
    
    # Validate Python syntax
    check_start "Python file syntax"
    local python_errors=0
    for py_file in "$PROJECT_ROOT"/design-system/primitives/*/*.py; do
        if [[ -f "$py_file" ]]; then
            if ! python3 -m py_compile "$py_file" 2>/dev/null; then
                ((python_errors++))
            fi
        fi
    done
    
    if [[ $python_errors -eq 0 ]]; then
        check_pass "All Python files have valid syntax"
    else
        check_fail "$python_errors Python files have syntax errors"
    fi
    
    log ""
}

# Layer 2: Workflows Health Check
check_layer2_workflows() {
    log "### Layer 2: Workflows"
    log ""
    
    check_start "Northwestern enhanced workflows"
    local workflow_dir="$PROJECT_ROOT/workflows"
    if [[ -d "$workflow_dir" ]]; then
        local northwestern_workflows=0
        if [[ -f "$workflow_dir/evaluation/enhanced-concept-scoring-flow.md" ]]; then
            ((northwestern_workflows++))
        fi
        if [[ -f "$workflow_dir/evaluation/stage-gate-validation-flow.md" ]]; then
            ((northwestern_workflows++))
        fi
        if [[ -f "$workflow_dir/research/opportunity-identification-flow.md" ]]; then
            ((northwestern_workflows++))
        fi
        
        if [[ $northwestern_workflows -ge 3 ]]; then
            check_pass "Found $northwestern_workflows Northwestern enhanced workflows"
        else
            check_warning "Only found $northwestern_workflows Northwestern workflows (expected 3+)"
        fi
    else
        check_fail "Workflow directory not found"
    fi
    
    check_start "Workflow markdown validation"
    local md_errors=0
    for md_file in "$PROJECT_ROOT"/workflows/*/*.md; do
        if [[ -f "$md_file" ]] && ! grep -q "Northwestern" "$md_file"; then
            ((md_errors++))
        fi
    done
    
    if [[ $md_errors -eq 0 ]]; then
        check_pass "All enhanced workflows reference Northwestern methodologies"
    else
        check_warning "$md_errors workflow files may not be Northwestern enhanced"
    fi
    
    log ""
}

# Layer 3: Agents Health Check
check_layer3_agents() {
    log "### Layer 3: Agents"
    log ""
    
    check_start "Northwestern strategic agents"
    local agent_dir="$PROJECT_ROOT/agents"
    local required_agents=("northwestern-opportunity-strategist.md" "systematic-concept-evaluator.md" "strategic-brief-writer.md")
    local found_agents=0
    
    for agent in "${required_agents[@]}"; do
        if find "$agent_dir" -name "$agent" -type f | grep -q .; then
            ((found_agents++))
        fi
    done
    
    if [[ $found_agents -eq ${#required_agents[@]} ]]; then
        check_pass "Found all $found_agents required Northwestern agents"
    else
        check_fail "Only found $found_agents of ${#required_agents[@]} required Northwestern agents"
    fi
    
    check_start "Agent metadata tables"
    local agents_with_metadata=0
    for agent_file in "$PROJECT_ROOT"/agents/*/*.md; do
        if [[ -f "$agent_file" ]] && grep -q "| name | description | model | category |" "$agent_file"; then
            ((agents_with_metadata++))
        fi
    done
    
    if [[ $agents_with_metadata -ge 3 ]]; then
        check_pass "Found $agents_with_metadata agents with proper metadata tables"
    else
        check_warning "Only $agents_with_metadata agents have metadata tables"
    fi
    
    log ""
}

# Layer 4: Skills Health Check
check_layer4_skills() {
    log "### Layer 4: Skills"
    log ""
    
    check_start "Northwestern orchestration skills"
    local skill_dir="$PROJECT_ROOT/skills"
    local orchestration_skills=0
    
    if [[ -f "$skill_dir/northwestern-strategy/portfolio-optimization.md" ]]; then
        ((orchestration_skills++))
    fi
    if [[ -f "$skill_dir/concept-development/idea-to-prototype.md" ]]; then
        ((orchestration_skills++))
    fi
    if [[ -f "$skill_dir/decision-making/trade-off-analysis.md" ]]; then
        ((orchestration_skills++))
    fi
    
    if [[ $orchestration_skills -eq 3 ]]; then
        check_pass "Found all 3 Northwestern orchestration skills"
    else
        check_fail "Only found $orchestration_skills of 3 required orchestration skills"
    fi
    
    check_start "Skill orchestration documentation"
    local skills_with_orchestration=0
    for skill_file in "$skill_dir"/*/*.md; do
        if [[ -f "$skill_file" ]] && grep -q "Orchestrated Agents" "$skill_file"; then
            ((skills_with_orchestration++))
        fi
    done
    
    if [[ $skills_with_orchestration -ge 3 ]]; then
        check_pass "Found $skills_with_orchestration skills with orchestration documentation"
    else
        check_warning "Only $skills_with_orchestration skills have orchestration documentation"
    fi
    
    log ""
}

# Layer 5: Project Orchestration Health Check
check_layer5_orchestration() {
    log "### Layer 5: Project Orchestration"
    log ""
    
    check_start "Project orchestration components"
    local orch_dir="$PROJECT_ROOT/orchestration"
    if [[ -d "$orch_dir" ]]; then
        local orchestrators=0
        if [[ -f "$orch_dir/innovation-projects/mpd2-innovation-portfolio.md" ]]; then
            ((orchestrators++))
        fi
        if [[ -f "$orch_dir/product-development/systematic-development-program.md" ]]; then
            ((orchestrators++))
        fi
        
        if [[ $orchestrators -eq 2 ]]; then
            check_pass "Found all 2 project orchestration components"
        else
            check_warning "Only found $orchestrators of 2 project orchestration components"
        fi
    else
        check_fail "Orchestration directory not found"
    fi
    
    check_start "Northwestern framework integration"
    local framework_integration=0
    for orch_file in "$PROJECT_ROOT"/orchestration/*/*.md; do
        if [[ -f "$orch_file" ]]; then
            if grep -q "Knowledge Funnel" "$orch_file" && grep -q "Three Horizons" "$orch_file"; then
                ((framework_integration++))
            fi
        fi
    done
    
    if [[ $framework_integration -ge 2 ]]; then
        check_pass "Found $framework_integration orchestrators with Northwestern framework integration"
    else
        check_warning "Only $framework_integration orchestrators have Northwestern framework integration"
    fi
    
    log ""
}

# Supporting Infrastructure Health Check
check_supporting_infrastructure() {
    log "### Supporting Infrastructure"
    log ""
    
    check_start "Examples and templates"
    local examples_count=0
    local templates_count=0
    
    if [[ -d "$PROJECT_ROOT/examples/northwestern-mpd2" ]]; then
        examples_count=$(find "$PROJECT_ROOT/examples/northwestern-mpd2" -name "*.md" | wc -l)
    fi
    
    if [[ -d "$PROJECT_ROOT/templates" ]]; then
        templates_count=$(find "$PROJECT_ROOT/templates" -name "*.yaml" | wc -l)
    fi
    
    if [[ $examples_count -gt 0 && $templates_count -gt 0 ]]; then
        check_pass "Found $examples_count example files and $templates_count template files"
    elif [[ $examples_count -gt 0 || $templates_count -gt 0 ]]; then
        check_warning "Found $examples_count examples and $templates_count templates (both expected)"
    else
        check_fail "No examples or templates found"
    fi
    
    check_start "Integration documentation"
    local integration_docs=0
    if [[ -f "$PROJECT_ROOT/INTEGRATION_MAP.md" ]]; then
        ((integration_docs++))
    fi
    if [[ -f "$PROJECT_ROOT/MPD2_LARGE_PDFS_FOR_LATER_ANALYSIS.md" ]]; then
        ((integration_docs++))
    fi
    
    if [[ $integration_docs -eq 2 ]]; then
        check_pass "Found all integration documentation files"
    else
        check_warning "Only found $integration_docs of 2 integration documentation files"
    fi
    
    log ""
}

# System Integration Health Check
check_system_integration() {
    log "### System Integration"
    log ""
    
    check_start "Cross-layer references"
    local cross_references=0
    
    # Check if skills reference agents
    if grep -r "northwestern-opportunity-strategist" "$PROJECT_ROOT/skills/" >/dev/null 2>&1; then
        ((cross_references++))
    fi
    
    # Check if orchestration references skills
    if grep -r "portfolio-optimization" "$PROJECT_ROOT/orchestration/" >/dev/null 2>&1; then
        ((cross_references++))
    fi
    
    # Check if workflows reference calculators
    if grep -r "opportunity-score.py" "$PROJECT_ROOT/workflows/" >/dev/null 2>&1; then
        ((cross_references++))
    fi
    
    if [[ $cross_references -eq 3 ]]; then
        check_pass "Found all expected cross-layer references"
    else
        check_warning "Only found $cross_references of 3 expected cross-layer references"
    fi
    
    check_start "Northwestern framework consistency"
    local framework_consistency=0
    local knowledge_funnel_refs=$(grep -r "Knowledge Funnel" "$PROJECT_ROOT" --include="*.md" 2>/dev/null | wc -l)
    local three_horizons_refs=$(grep -r "Three Horizons" "$PROJECT_ROOT" --include="*.md" 2>/dev/null | wc -l)
    
    if [[ $knowledge_funnel_refs -ge 10 && $three_horizons_refs -ge 10 ]]; then
        check_pass "Northwestern frameworks consistently referenced ($knowledge_funnel_refs Knowledge Funnel, $three_horizons_refs Three Horizons)"
    else
        check_warning "Northwestern framework references may be inconsistent ($knowledge_funnel_refs Knowledge Funnel, $three_horizons_refs Three Horizons)"
    fi
    
    log ""
}

# Generate summary
generate_summary() {
    log "## Summary"
    log ""
    log "**Total Checks:** $TOTAL_CHECKS"
    log "**Passed:** $PASSED_CHECKS"
    log "**Failed:** $FAILED_CHECKS"
    log "**Warnings:** $WARNING_CHECKS"
    log ""
    
    local health_percentage=$((PASSED_CHECKS * 100 / TOTAL_CHECKS))
    
    if [[ $FAILED_CHECKS -eq 0 && $WARNING_CHECKS -eq 0 ]]; then
        log "🎉 **System Health: EXCELLENT** (100% pass rate)"
        log "All components are properly implemented and integrated."
    elif [[ $FAILED_CHECKS -eq 0 ]]; then
        log "✅ **System Health: GOOD** ($health_percentage% pass rate, $WARNING_CHECKS warnings)"
        log "Core functionality is working with minor issues to address."
    elif [[ $health_percentage -ge 70 ]]; then
        log "⚠️ **System Health: FAIR** ($health_percentage% pass rate, $FAILED_CHECKS failures)"
        log "System is functional but needs attention to failed components."
    else
        log "❌ **System Health: POOR** ($health_percentage% pass rate, $FAILED_CHECKS failures)"
        log "Significant issues need to be addressed for proper system operation."
    fi
    
    log ""
    log "## Recommendations"
    log ""
    
    if [[ $FAILED_CHECKS -gt 0 ]]; then
        log "1. **Address Failed Checks:** Focus on resolving the $FAILED_CHECKS failed components"
        log "2. **Verify Integration:** Ensure all layers are properly connected"
        log "3. **Test Functionality:** Run component-specific tests after fixes"
    fi
    
    if [[ $WARNING_CHECKS -gt 0 ]]; then
        log "1. **Review Warnings:** Investigate the $WARNING_CHECKS warning conditions"
        log "2. **Complete Implementation:** Finish any partially implemented components"
        log "3. **Enhance Documentation:** Ensure all components have proper documentation"
    fi
    
    log ""
    log "---"
    log "*Health check completed at $TIMESTAMP*"
}

# Main execution
main() {
    echo "Northwestern MPD2 Design Decision System Health Check"
    echo "======================================================"
    echo ""
    
    init_report
    
    echo "Checking system health across all layers..."
    echo ""
    
    check_layer1_primitives
    check_layer2_workflows
    check_layer3_agents
    check_layer4_skills
    check_layer5_orchestration
    check_supporting_infrastructure
    check_system_integration
    
    generate_summary
    
    echo ""
    echo "Health check complete! Report saved to: $HEALTH_REPORT"
    echo ""
    
    # Return appropriate exit code
    if [[ $FAILED_CHECKS -gt 0 ]]; then
        exit 1
    elif [[ $WARNING_CHECKS -gt 0 ]]; then
        exit 2
    else
        exit 0
    fi
}

# Execute main function
main "$@"