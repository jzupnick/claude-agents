#!/usr/bin/env bash
# setup_and_push_github.sh
#
# What: Creates GitHub repo and pushes this project
# Why: One command to get everything on GitHub
# Usage: ./setup_and_push_github.sh [repo-name] [visibility]

set -euo pipefail

REPO_NAME="${1:-claude-agents}"
VISIBILITY="${2:-public}"  # public or private

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Claude Agents GitHub Setup ===${NC}"
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}GitHub CLI (gh) not found${NC}"
    echo ""
    echo "Install it:"
    echo "  macOS:   brew install gh"
    echo "  Linux:   See https://github.com/cli/cli/blob/trunk/docs/install_linux.md"
    echo "  Windows: winget install --id GitHub.cli"
    echo ""
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo -e "${YELLOW}Not authenticated with GitHub${NC}"
    echo "Authenticating now..."
    gh auth login
fi

echo -e "${GREEN}✓${NC} GitHub CLI authenticated"
echo ""

# Get GitHub username
GH_USERNAME=$(gh api user -q .login)
echo -e "${BLUE}GitHub username:${NC} $GH_USERNAME"
echo -e "${BLUE}Repository name:${NC} $REPO_NAME"
echo -e "${BLUE}Visibility:${NC} $VISIBILITY"
echo ""

# Check if repo already exists
if gh repo view "$GH_USERNAME/$REPO_NAME" &> /dev/null; then
    echo -e "${YELLOW}Repository $REPO_NAME already exists${NC}"
    read -p "Delete and recreate? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Deleting existing repo..."
        gh repo delete "$GH_USERNAME/$REPO_NAME" --yes
    else
        echo "Aborting."
        exit 1
    fi
fi

# Create repository
echo -e "${BLUE}Creating repository...${NC}"
gh repo create "$REPO_NAME" \
    --${VISIBILITY} \
    --description "Framework for building Claude Code agents with jobs-to-be-done methodology, work journals, and LLM leaderboard integration" \
    --source=. \
    --remote=origin \
    --push

echo ""
echo -e "${GREEN}✓${NC} Repository created and pushed!"
echo ""

# Add topics
echo -e "${BLUE}Adding topics...${NC}"
gh repo edit "$GH_USERNAME/$REPO_NAME" \
    --add-topic claude-code \
    --add-topic agents \
    --add-topic subagents \
    --add-topic llm \
    --add-topic ai-tools \
    --add-topic jobs-to-be-done \
    --add-topic autonomous-agents \
    --add-topic developer-tools

echo -e "${GREEN}✓${NC} Topics added"
echo ""

# Show repository URL
REPO_URL="https://github.com/$GH_USERNAME/$REPO_NAME"
echo -e "${GREEN}=== Success! ===${NC}"
echo ""
echo -e "${BLUE}Repository URL:${NC}"
echo "$REPO_URL"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo "1. Visit $REPO_URL"
echo "2. Star your repo (why not?)"
echo "3. Create your first subagent"
echo "4. Export to .claude/commands/"
echo "5. Journal after using it"
echo ""
echo -e "${BLUE}Clone elsewhere:${NC}"
echo "git clone $REPO_URL"
echo ""
