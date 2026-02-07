---
name: linear-project-management
description: Master Linear project management with MCP integration. Use when auditing backlogs, syncing issue status with codebase reality, creating well-structured issues, or generating evidence-based sprint plans.
---

# Linear Project Management Skill

Combine Linear MCP server operations with codebase auditing to maintain perfect sync between project tracking and implementation reality.

## Core Principles

### 1. Evidence-Based Updates

Never update Linear status without codebase verification:

```bash
# Before marking AB-32 as Done, verify:
git log --all --grep="AB-32"                    # Find merge commits
find . -name "*Audio*" -type f                  # Locate implementation files
wc -l Services/Audio/*.swift                    # Count lines of code
gh pr list --search "AB-32" --state merged      # Confirm PR merge
```

Update Linear with evidence:
```
✅ MERGED - PR #192 (Nov 19, 2025)
Evidence:
- Git commit: ab0fd17
- Files: AudioManager.swift (22KB), EmergencyAudioManager.swift (15KB)
- Tests: 31 total tests
```

### 2. Structured Issue Creation

```markdown
Title: [Clear, specific - 50 chars max]

## Overview
[2-3 sentence summary at 5th grade reading level]

## Scope
- Specific deliverable 1
- Acceptance criteria

## Implementation Notes
FILES TO CREATE:
- ServiceName.swift

DEPENDENCIES:
- Blocked by: AB-X
```

Estimate with reference class forecasting — search similar past issues, calculate average effort, provide range estimates (e.g., 12-15 hours, not 13.5 hours).

### 3. Backlog Reconciliation Workflow

1. **List all Linear issues** via MCP (in_progress, backlog, done states)
2. **Search codebase** for each issue reference
3. **Compare Linear vs Reality** — check files, git log, PR merges
4. **Generate reconciliation report:**
   - Issues to close (code says done, Linear says not)
   - Issues to update progress
   - Missing issues (code exists, not tracked)
5. **Execute updates** via Linear MCP
6. **Sync TODO.md** to match

### 4. Sprint Planning

1. Gather backlog + in-progress issues via MCP
2. Audit actual completion for each in-progress issue
3. Calculate remaining effort from verified progress
4. Sequence work by dependencies
5. Generate sprint plan with revised estimates

## Linear MCP Operations Reference

```javascript
// List issues by state
mcp__linear-server__list_issues({ filter: { state: { type: "in_progress" } } })

// Create issue
mcp__linear-server__create_issue({
  title: "Feature Name",
  description: "[structured spec]",
  priority: "high",
  estimate: 15,
  labels: ["label1"]
})

// Update issue with evidence
mcp__linear-server__update_issue({
  issueId: "AB-32",
  status: "Done",
  comment: "✅ MERGED - PR #192\nEvidence: [details]"
})

// Search issues
mcp__linear-server__search_issues({ query: "feature name" })
```

## Codebase Verification Techniques

```bash
# Find implementation files
grep -r "AB-32" . --include="*.swift"
find . -iname "*feature*"

# Check git history
git log --all --grep="AB-32" --oneline
gh pr list --state merged --search "AB-32"

# Calculate completion percentage
# Planned: 4 files | Implemented: 3 files → 75%
```

## Status Decision Tree

```
Does code exist for this issue?
  ├─ No → Status: Backlog (Not Started)
  ├─ Partial implementation
  │   ├─ PR open → Status: In Progress (X%)
  │   └─ PR merged → Status: Done
  └─ Full implementation
      ├─ PR merged to main → Status: Done
      └─ PR not merged → Status: In Progress (95%+)
```

## Best Practices

- **Evidence beats intuition**: Always verify in codebase before updating
- **Automate everything**: Use Linear MCP for all operations
- **Maintain bidirectional sync**: Linear ↔ TODO.md ↔ Codebase
- **Reference class forecasting**: Estimate from similar past work
- **Consistent formatting**: Use status indicators (✅ 🟡 ❌ 🔄)

## Error Prevention

- Never mark done without verification (git log + find + wc)
- Always search before creating (avoid duplicate issues)
- Calculate completion from scope items, don't guess percentages
