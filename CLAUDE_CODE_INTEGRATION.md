# Claude Code Native Integration

How to use these subagents within Claude Code's `.claude/` structure.

## Quick Overview

**This repo:** Building blocks (agents, subagents, skills)
**Claude Code:** Runtime environment with `.claude/` conventions

**Bridge:** Export your subagents as Claude Code slash commands.

## Claude Code Directory Structure

```
your-project/
├── .claude/
│   ├── commands/         # Custom slash commands
│   │   ├── project/      # Project-specific commands
│   │   └── personal/     # Your personal commands
│   ├── hooks/           # Pre/post execution automation
│   └── CLAUDE.md        # Project context
├── .mcp.json           # MCP server configurations
└── [your code]
```

## Exporting Subagents as Slash Commands

### Pattern 1: Simple Subagent → Single Command

**Subagent:** `challenge_technical_assumptions.md`
**Export as:** `.claude/commands/project/challenge-assumptions.md`

```bash
# In your project directory
mkdir -p .claude/commands/project

# Create command file
cat > .claude/commands/project/challenge-assumptions.md << 'EOF'
You are a technical risk assessment subagent following the jobs-to-be-done framework.

## Job To Be Done
Challenge technical assumptions before they become technical debt.

## The Hiring Moment
I'm about to commit to a technical direction that "feels right" but hasn't been pressure-tested.

## How to Proceed

1. **Gather Context**
   - Ask for the proposed technical approach
   - Understand current constraints (time, team, budget)
   - Identify known requirements and unknowns

2. **Pre-mortem Analysis**
   - Assume the approach failed in 6 months
   - Work backwards to find what caused it
   - Identify assumptions that, if wrong, cause failure

3. **Risk Assessment**
   - Rank by: likelihood of being wrong × cost if wrong
   - Focus on top 3 riskiest assumptions

4. **Experiment Design**
   - Design cheapest test for each risky assumption
   - Specific, executable experiments

5. **Deliverables**
   - Executive summary: "Do/Don't do X because Y"
   - Risk-ranked list with recommendations
   - Alternatives considered

## Tools to Use
- Use `jq` to analyze JSON configs/dependencies
- Use `git` to examine codebase history
- Use `curl` to test API assumptions
- Use `grep/ripgrep` to search for assumption patterns

## Mental Models to Apply
- Pre-mortem: Assume failure, work backwards
- Inversion: What would make this fail?
- Occam's Razor: Favor simpler solutions
- Lindy Effect: Older tech often less risky

## Output Format
Provide:
1. **Artifacts** (for other tools):
   - Risk matrix with scores
   - Failure scenarios with probabilities
   - Experiment designs

2. **Deliverables** (for humans):
   - Clear recommendation with reasoning
   - One-pager: approach, risks, mitigations

## When NOT to Use
- Actual crisis (do the obvious thing fast)
- Decision is easily reversible (just try it)
- Cost of being wrong is negligible
- Bikeshedding (don't use this to delay)

$ARGUMENTS
EOF

chmod 644 .claude/commands/project/challenge-assumptions.md
```

**Usage in Claude Code:**
```
/project:challenge-assumptions

We're considering using microservices architecture for our new feature.
Time constraint: 3 months to launch.
Team: 5 engineers, mixed experience.
Unknowns: How many services? What splits make sense?
```

### Pattern 2: Complex Subagent → Multiple Commands

**Subagent:** Large workflow with multiple steps
**Export as:** Multiple related commands

```
.claude/commands/project/
├── review-start.md       # Initialize code review
├── review-analyze.md     # Deep analysis
└── review-complete.md    # Finalize and report
```

Each command references the others in workflow.

### Pattern 3: Workflow → Hook

**Workflow:** `code_review_workflow.md`
**Export as:** `.claude/hooks/pre-commit`

```bash
# In your project
mkdir -p .claude/hooks

cat > .claude/hooks/pre-commit << 'EOF'
#!/usr/bin/env bash
# Pre-commit code review hook

echo "Running automated code review..."

# Get staged files
staged_files=$(git diff --cached --name-only --diff-filter=ACM)

if [ -z "$staged_files" ]; then
    echo "No files to review"
    exit 0
fi

# Run review subagent
claude << PROMPT
Review these staged files for:
- Security vulnerabilities
- Performance issues  
- Code quality concerns
- Breaking changes

Files:
$staged_files

Provide:
- Critical issues (block commit)
- Warnings (proceed with caution)
- Suggestions (nice to have)

PROMPT

# Could parse output and block on critical issues
exit 0
EOF

chmod +x .claude/hooks/pre-commit
```

## CLAUDE.md Template

Create context for your project that subagents can use:

```markdown
# Project: [Name]

## Overview
[What this project does]

## Architecture
[Key architectural decisions]

## Tech Stack
[Technologies used]

## Conventions
[Coding standards, patterns]

## Known Issues
[Current pain points]

## Areas Needing Attention
[Where AI assistance is most valuable]

## Custom Subagents
This project uses custom subagents from claude-agents repo:
- `/project:challenge-assumptions` - Technical risk assessment
- `/project:review-security` - Security-focused code review
- `/project:optimize-performance` - Performance analysis

## Context for Subagents

### Technical Constraints
- [List constraints]

### Business Constraints
- [List constraints]

### Team Context
- [Team size, expertise]

### Decision History
- [Major technical decisions and why]
```

## MCP Integration

MCPs (Model Context Protocols) extend Claude Code with external integrations.

### Example: GitHub MCP for Code Review Subagent

**.mcp.json:**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Updated command (.claude/commands/project/review-pr.md):**
```markdown
You are a code review subagent with GitHub access via MCP.

## Tools Available
- GitHub MCP: Access PRs, issues, code, comments
- Standard tools: git, jq, etc.

## Process
1. Use GitHub MCP to fetch PR details
2. Analyze changes for issues
3. Post review comments via GitHub MCP
4. Generate summary deliverable

$ARGUMENTS should be PR number.

Example: /project:review-pr 123
```

### Useful MCPs for Subagents

**Development:**
- `@modelcontextprotocol/server-github` - GitHub integration
- `@modelcontextprotocol/server-postgres` - Database queries
- `@modelcontextprotocol/server-filesystem` - File operations

**Monitoring:**
- Sentry MCP - Error tracking
- Datadog MCP - Metrics access

**Business:**
- Stripe MCP - Payment data
- Notion MCP - Documentation access

## Best Practices

### 1. Keep Commands Focused
One command = one job
Don't: `/project:do-everything`
Do: `/project:challenge-assumptions`, `/project:review-security`

### 2. Make Commands Composable
Commands should work standalone or in sequence.

### 3. Use $ARGUMENTS
Allow parameters:
```markdown
Analyze the deployment plan: $ARGUMENTS
```

Usage: `/project:challenge-assumptions deployment-plan.md`

### 4. Document Prerequisites
In command file:
```markdown
## Prerequisites
- Tools: jq, gh
- MCPs: github
- Environment: GITHUB_TOKEN set
```

### 5. Provide Examples
In command file:
```markdown
## Examples
/project:review-pr 123
/project:review-pr 456 --focus security
```

### 6. Set Expectations
Tell users what to expect:
```markdown
## Output
Analysis takes ~30 seconds.
Produces:
- Risk assessment JSON
- Human-readable summary
```

## Migration Checklist

Exporting a subagent to Claude Code:

- [ ] Choose export type (command/hook/both)
- [ ] Create appropriate `.claude/` file
- [ ] Adapt template to command format
- [ ] Add $ARGUMENTS handling
- [ ] Document prerequisites
- [ ] Add examples
- [ ] Test in Claude Code
- [ ] Update project CLAUDE.md

## Example: Complete Integration

**Subagent:** `challenge_technical_assumptions.md`

**Files created:**
```
your-project/
├── .claude/
│   ├── commands/
│   │   └── project/
│   │       └── challenge-assumptions.md    # Slash command
│   ├── hooks/
│   │   └── pre-commit                      # Auto-run on commit
│   └── CLAUDE.md                           # Project context
├── .mcp.json                               # GitHub MCP config
└── journals/
    └── challenge_assumptions/
        └── 2025-11.md                      # Work journal
```

**Usage patterns:**
```bash
# Manual invocation
/project:challenge-assumptions our-microservices-plan.md

# Auto-run via hook
git commit -m "Add new service"
# Hook runs challenge-assumptions automatically

# With MCP integration
/project:challenge-assumptions
# Has access to GitHub, can analyze PRs directly
```

## Your Challenge

Pick one subagent. Export it:

1. **Create command file** in `.claude/commands/project/`
2. **Test it** with `/project:command-name`
3. **Add to CLAUDE.md** with description
4. **Journal results** after first use

If export worked, you've bridged the gap between building blocks and runtime.

What subagent are you exporting first?
