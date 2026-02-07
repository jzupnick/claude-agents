---
name: refactor-plan
description: Create a safe, incremental engineering refactor roadmap. Use when planning codebase improvements, decomposing tech debt, or designing safe migration paths for architecture changes.
---

# Engineering Refactor Plan

Apply best practices from Refactoring and Understanding Variation to produce a safe, incremental refactor roadmap.

## Process

### Step 1: Gather Inputs
- Current architecture overview
- Pain points (what's hard to change?)
- Recent incidents related to this code
- Delivery goals (what needs to ship?)
- Current test coverage

### Step 2: Analysis
- **Software Engineer**: Code analysis, dependency mapping, change impact
- **Senior Engineer**: Signal vs noise, systemic patterns, safe change boundaries

### Step 3: Root Cause Analysis
For each problem area:
- Root cause (not just symptoms)
- Blast radius of changes
- Dependencies (what else touches this?)
- Test coverage gaps

### Step 4: Create Safe Slices
Break refactor into independently deployable slices:
- Each slice: small, testable, reversible
- Order by: risk (lowest first) + value (highest first)
- Define rollback plan for each

### Step 5: Red-Team
- What could go wrong?
- Hidden dependencies we missed?
- Is this the right time for this refactor?
- Opportunity cost vs shipping features?

### Step 6: Output Format

```
# Refactor Plan: [Area]

## Problem Statement
[What's broken and why it matters]

## Root Cause Analysis
[Not symptoms — actual causes]

## Refactor Roadmap
### Slice 1: [Name] — Risk: Low
- Changes: ...
- Tests needed: ...
- Rollback: ...
- Definition of Done: ...

### Slice 2: [Name] — Risk: Medium
...

## Risk Register
| Risk | Likelihood | Impact | Mitigation |

## Dependencies
- Blocked by: ...
- Blocks: ...

## Success Metrics
- Before: [current state metric]
- After: [target metric]

## Next Action
[First concrete step, ≤15 min]
```

## Operating Principles
- Favor clarity over cleverness
- Small safe changes > big bang rewrites
- Every change must be testable
- Separate signal from noise
