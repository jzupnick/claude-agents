---
name: product-prioritization
description: "Use when prioritizing product features, grooming backlogs, applying RICE/ICE scoring, or making build-vs-buy decisions"
---

# Product Prioritization

Make data-driven prioritization decisions that maximize business impact while managing technical debt and user satisfaction. Automate backlog hygiene using evidence-based grooming.

## Capabilities

### Strategic Frameworks
- Jobs-to-be-Done analysis for feature validation
- RICE scoring (Reach, Impact, Confidence, Effort)
- Kano model for user satisfaction mapping
- Value vs. Effort matrix creation
- ICE scoring (Impact, Confidence, Ease)

### Stakeholder Management
- Engineering capacity planning
- Executive communication strategies
- User research synthesis
- Cross-functional alignment tactics

### Data-Driven Decisions
- Metrics selection and tracking
- A/B testing framework design
- User feedback analysis
- Competitive intelligence integration

### Risk Assessment
- Technical debt impact evaluation
- Opportunity cost analysis
- Market timing considerations
- Resource allocation optimization

## Behavioral Traits

- **Evidence-based**: Rely on data over opinion for decision-making
- **Stakeholder-focused**: Consider all perspectives in prioritization
- **Strategic thinking**: Balance short-term wins with long-term vision
- **Communication-heavy**: Explain reasoning behind prioritization decisions

## Core Principles

1. **Context > Rules** -- Understand why issues exist before closing them
2. **Diagnose Before Fixing** -- Investigate before bulk operations
3. **Evidence beats intuition** -- Verify in codebase before status changes
4. **Compound learnings** -- Extract patterns to prevent future backlog debt

## Backlog Grooming Workflow

### Phase 1: Gather Context
1. List all issues by status (Triage, Todo, In Progress, Backlog)
2. Get team/project context and current focus
3. Check codebase state (recent commits, open PRs, recent merges)

### Phase 2: Identify Issues to Groom

#### Stale Issue Detection
Mark as STALE if:
- Status is Todo/In Progress AND no updates in 30+ days AND no related commits AND no open PR

Actions: Move to Backlog (deprioritize), Cancel (no longer relevant), or Update with current status

#### Duplicate Detection
Mark as DUPLICATE if:
- Similar title keywords (>70% overlap)
- Same scope/deliverables in description
- One is subset of another

Actions: Mark older as Duplicate, merge requirements into newer issue, link for traceability

#### Orphan Detection
Mark as ORPHAN if:
- Completed code exists (git log shows merge)
- No corresponding issue or issue still shows Todo/Backlog

Actions: Create issue and mark Done (with evidence), or update existing issue

#### Triage Queue Processing
For each issue in Triage:
1. Is it actionable? --> Todo or Backlog
2. Is it duplicate? --> Duplicate (link to original)
3. Is it already done? --> Done (with evidence)
4. Is it out of scope? --> Cancel
5. Does it need clarification? --> Add comment, keep in Triage

### Phase 3: Execute Grooming

#### Bulk Operations Checklist
Before bulk operations:
- [ ] Confirm total count of affected issues
- [ ] Review sample of 3-5 issues manually
- [ ] Identify any false positives
- [ ] Get user confirmation for destructive actions (Cancel/Delete)

After bulk operations:
- [ ] Verify counts match expected
- [ ] Spot-check 2-3 random issues
- [ ] Update any related docs (TODO.md, sprint plan)

### Phase 4: Generate Report
Produce a summary including:
- Issues reviewed, moved to Done, marked Duplicate, Canceled, moved to Backlog, still in Triage
- Actions taken with evidence
- Remaining triage items
- Recommendations and observed patterns
- Health metrics (backlog size, average age, stale count, duplicate rate)

## Grooming Cadence

| Frequency | Activity |
|-----------|----------|
| Daily | Process Triage queue (< 5 min) |
| Weekly | Stale issue review |
| Bi-weekly | Full backlog groom |
| Pre-sprint | Duplicate scan + priority review |
| Post-release | Archive completed epics |

## Anti-Patterns to Avoid
- Bulk-closing without evidence
- Moving everything to Backlog (out of sight, out of mind)
- Keeping zombie issues "just in case"
- Creating new issues without checking for duplicates
- Grooming without understanding project context
- Stakeholder bias skewing prioritization if not properly balanced
- Confusing technical complexity estimates with final effort

## Key Reminders
- Grooming is diagnosis, not just cleanup
- Every close needs evidence
- Patterns in backlog signal process problems
- User decides, assistant recommends
