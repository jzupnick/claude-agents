#!/usr/bin/env bash
# ios_project_health_check.sh
#
# What: Comprehensive health check for iOS Xcode projects
# Why: Catch common iOS development issues before they impact development velocity
# Usage: ./ios_project_health_check.sh [project_path]

set -euo pipefail

PROJECT_PATH="${1:-.}"
REPORT_FILE="ios_health_report.md"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== iOS Project Health Check ===${NC}"
echo "Analyzing project at: $PROJECT_PATH"
echo ""

# Initialize report
cat > "$REPORT_FILE" << EOF
# iOS Project Health Report
Generated: $(date)
Project: $PROJECT_PATH

## Summary

EOF

# Function to add section to report
add_section() {
    local title="$1"
    local content="$2"
    echo -e "\n## $title\n\n$content" >> "$REPORT_FILE"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for required tools
echo -e "${BLUE}Checking development tools...${NC}"
MISSING_TOOLS=()

if ! command_exists xcodebuild; then
    MISSING_TOOLS+=("xcodebuild")
fi

if ! command_exists swiftlint; then
    MISSING_TOOLS+=("swiftlint")
fi

if [ ${#MISSING_TOOLS[@]} -gt 0 ]; then
    echo -e "${RED}Missing tools: ${MISSING_TOOLS[*]}${NC}"
    add_section "Missing Tools" "$(printf '- %s\n' "${MISSING_TOOLS[@]}")"
else
    echo -e "${GREEN}✓ All required tools available${NC}"
    add_section "Development Tools" "✅ All required tools available"
fi

# Find Xcode project/workspace
echo -e "${BLUE}Locating Xcode project...${NC}"
PROJECT_FILE=""
WORKSPACE_FILE=""

if [ -f "$PROJECT_PATH"/*.xcworkspace ]; then
    WORKSPACE_FILE=$(find "$PROJECT_PATH" -name "*.xcworkspace" | head -1)
    echo -e "${GREEN}✓ Found workspace: $(basename "$WORKSPACE_FILE")${NC}"
elif [ -f "$PROJECT_PATH"/*.xcodeproj ]; then
    PROJECT_FILE=$(find "$PROJECT_PATH" -name "*.xcodeproj" | head -1)
    echo -e "${GREEN}✓ Found project: $(basename "$PROJECT_FILE")${NC}"
else
    echo -e "${RED}✗ No Xcode project or workspace found${NC}"
    add_section "Project Structure" "❌ No Xcode project or workspace found"
    exit 1
fi

# Build configuration check
echo -e "${BLUE}Checking build configuration...${NC}"
BUILD_ISSUES=()

if [ -n "$WORKSPACE_FILE" ]; then
    BUILD_TARGET="$WORKSPACE_FILE"
    BUILD_FLAG="-workspace"
else
    BUILD_TARGET="$PROJECT_FILE"
    BUILD_FLAG="-project"
fi

# Try to build (dry run)
echo "Testing build configuration..."
if xcodebuild "$BUILD_FLAG" "$BUILD_TARGET" -scheme "$(xcodebuild -list | grep -A 1 "Schemes:" | tail -1 | xargs)" -dry-run >/dev/null 2>&1; then
    echo -e "${GREEN}✓ Build configuration valid${NC}"
    add_section "Build Configuration" "✅ Build configuration is valid"
else
    echo -e "${YELLOW}⚠ Build configuration may have issues${NC}"
    BUILD_ISSUES+=("Build configuration validation failed")
fi

# Swift/SwiftUI code quality check
echo -e "${BLUE}Checking code quality...${NC}"
SWIFT_FILES=$(find "$PROJECT_PATH" -name "*.swift" -not -path "*/Pods/*" -not -path "*/build/*" | wc -l | xargs)
echo "Found $SWIFT_FILES Swift files"

QUALITY_ISSUES=()

if command_exists swiftlint; then
    echo "Running SwiftLint analysis..."
    LINT_OUTPUT=$(cd "$PROJECT_PATH" && swiftlint --quiet 2>/dev/null || true)
    LINT_WARNINGS=$(echo "$LINT_OUTPUT" | grep -c "warning:" || true)
    LINT_ERRORS=$(echo "$LINT_OUTPUT" | grep -c "error:" || true)
    
    if [ "$LINT_ERRORS" -gt 0 ]; then
        echo -e "${RED}✗ SwiftLint found $LINT_ERRORS errors${NC}"
        QUALITY_ISSUES+=("$LINT_ERRORS SwiftLint errors")
    elif [ "$LINT_WARNINGS" -gt 0 ]; then
        echo -e "${YELLOW}⚠ SwiftLint found $LINT_WARNINGS warnings${NC}"
        QUALITY_ISSUES+=("$LINT_WARNINGS SwiftLint warnings")
    else
        echo -e "${GREEN}✓ No SwiftLint issues${NC}"
    fi
else
    echo -e "${YELLOW}⚠ SwiftLint not available for code quality check${NC}"
    QUALITY_ISSUES+=("SwiftLint not installed")
fi

# Check for common performance issues in SwiftUI
echo -e "${BLUE}Checking for SwiftUI performance patterns...${NC}"
PERFORMANCE_ISSUES=()

# Check for expensive view body computations
EXPENSIVE_BODY_COUNT=$(grep -r "body.*{" "$PROJECT_PATH" --include="*.swift" | grep -E "(\.sorted|\.filter|\.map)" | wc -l | xargs)
if [ "$EXPENSIVE_BODY_COUNT" -gt 0 ]; then
    PERFORMANCE_ISSUES+=("$EXPENSIVE_BODY_COUNT potential expensive computations in view body")
fi

# Check for proper @StateObject vs @ObservedObject usage
STATEOBJECT_COUNT=$(grep -r "@StateObject" "$PROJECT_PATH" --include="*.swift" | wc -l | xargs)
OBSERVEDOBJECT_COUNT=$(grep -r "@ObservedObject" "$PROJECT_PATH" --include="*.swift" | wc -l | xargs)

if [ "$OBSERVEDOBJECT_COUNT" -gt "$STATEOBJECT_COUNT" ]; then
    PERFORMANCE_ISSUES+=("Consider reviewing @ObservedObject vs @StateObject usage")
fi

# Check project structure and organization
echo -e "${BLUE}Analyzing project structure...${NC}"
STRUCTURE_ISSUES=()

# Check for deep nesting
MAX_DEPTH=$(find "$PROJECT_PATH" -name "*.swift" -not -path "*/Pods/*" | sed 's|[^/]||g' | awk '{print length}' | sort -n | tail -1)
if [ "$MAX_DEPTH" -gt 8 ]; then
    STRUCTURE_ISSUES+=("Deep directory nesting detected (depth: $MAX_DEPTH)")
fi

# Check for large files
LARGE_FILES=$(find "$PROJECT_PATH" -name "*.swift" -not -path "*/Pods/*" -exec wc -l {} + | awk '$1 > 500 {print $2 " (" $1 " lines)"}' | wc -l | xargs)
if [ "$LARGE_FILES" -gt 0 ]; then
    STRUCTURE_ISSUES+=("$LARGE_FILES files over 500 lines - consider refactoring")
fi

# Generate final report
echo -e "${BLUE}Generating health report...${NC}"

# Build summary
TOTAL_ISSUES=$((${#BUILD_ISSUES[@]} + ${#QUALITY_ISSUES[@]} + ${#PERFORMANCE_ISSUES[@]} + ${#STRUCTURE_ISSUES[@]}))

if [ "$TOTAL_ISSUES" -eq 0 ]; then
    HEALTH_STATUS="🟢 **Excellent** - No issues detected"
    echo -e "${GREEN}✓ Project health: Excellent${NC}"
elif [ "$TOTAL_ISSUES" -le 3 ]; then
    HEALTH_STATUS="🟡 **Good** - Minor issues detected"
    echo -e "${YELLOW}⚠ Project health: Good with minor issues${NC}"
else
    HEALTH_STATUS="🔴 **Needs Attention** - Multiple issues detected"
    echo -e "${RED}⚠ Project health: Needs attention${NC}"
fi

# Update report summary
sed -i '' "s/## Summary/## Summary\n\n$HEALTH_STATUS\n\n**Files Analyzed:** $SWIFT_FILES Swift files\n**Total Issues:** $TOTAL_ISSUES/" "$REPORT_FILE"

# Add detailed sections
if [ ${#BUILD_ISSUES[@]} -gt 0 ]; then
    add_section "Build Issues" "$(printf '- %s\n' "${BUILD_ISSUES[@]}")"
fi

if [ ${#QUALITY_ISSUES[@]} -gt 0 ]; then
    add_section "Code Quality Issues" "$(printf '- %s\n' "${QUALITY_ISSUES[@]}")"
fi

if [ ${#PERFORMANCE_ISSUES[@]} -gt 0 ]; then
    add_section "Performance Considerations" "$(printf '- %s\n' "${PERFORMANCE_ISSUES[@]}")"
fi

if [ ${#STRUCTURE_ISSUES[@]} -gt 0 ]; then
    add_section "Project Structure Issues" "$(printf '- %s\n' "${STRUCTURE_ISSUES[@]}")"
fi

# Add recommendations
cat >> "$REPORT_FILE" << EOF

## Recommendations

### Immediate Actions
- Review and fix any build configuration issues
- Address SwiftLint errors and critical warnings
- Consider refactoring files over 500 lines

### Performance Optimization
- Move expensive computations out of SwiftUI view body
- Review @StateObject vs @ObservedObject usage patterns
- Implement lazy loading for large lists

### Long-term Improvements
- Establish code review process with SwiftLint integration
- Set up automated health checks in CI/CD pipeline
- Consider modularizing large files and deep directory structures

## Next Steps
1. Address critical issues first (build errors, major SwiftLint violations)
2. Plan performance optimization in next sprint
3. Schedule technical debt reduction session for structural improvements

---
*Report generated by ios_project_health_check.sh*
EOF

echo ""
echo -e "${GREEN}✓ Health check complete!${NC}"
echo -e "${BLUE}Report saved to: $REPORT_FILE${NC}"
echo ""
echo "Summary:"
echo "- Swift files analyzed: $SWIFT_FILES"
echo "- Total issues found: $TOTAL_ISSUES"
echo "- Health status: $HEALTH_STATUS"