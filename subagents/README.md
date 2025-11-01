# Subagents

Reusable components. Building blocks you mix and match.

## What Goes Here

Subagents organized by the job they're hired to do (Clayton Christensen style):
- "Help me understand if this is risky"
- "Help me ship faster without breaking things"
- "Help me make technical decisions under uncertainty"
- "Help me find what's slowing us down"

## Naming Convention

Name by the job to be done:
- `reduce_deployment_risk.md` (not "deployment_validator")
- `accelerate_code_reviews.md` (not "code_reviewer")
- `clarify_architectural_tradeoffs.md` (not "architecture_analyzer")
- `surface_hidden_costs.md` (not "cost_estimator")

Ask: "When would I hire this?" That's your name.

## Template

```markdown
# Job To Be Done: [Clear statement of the job]

| name | description | model | category |
|------|-------------|-------|----------|
| [subagent_name] | [One-line description of what this does] | [sonnet/haiku/etc] | [technical/product/ops] |

## The Hiring Moment
When do you reach for this? What's the specific frustration or need?

## Core Philosophy
What principles guide this subagent's approach?

## Input
What does it need to work?

## Artifacts vs Deliverables

**Artifacts** (internal, for other subagents):
- Data structures, intermediate analysis, working documents
- What gets passed between subagents in a workflow
- Usually machine-readable or semi-structured

**Deliverables** (external, for humans):
- What you actually ship to stakeholders
- Decisions made, recommendations, final reports
- Human-readable, actionable

Example:
- Artifact: Risk assessment matrix with scores
- Deliverable: "Don't do X because Y; do Z instead"

## Stakeholders
Who consumes the deliverables?
- Primary: [Who needs this to make decisions?]
- Secondary: [Who should be informed?]
- Excluded: [Who explicitly should NOT see this?]

## Capabilities
Core areas of expertise:

**[Capability Area 1]:**
- [Specific skill 1]
- [Specific skill 2]

**[Capability Area 2]:**
- [Specific skill 1]
- [Specific skill 2]

## How It Works
Key approach and reasoning model.

## Behavioral Traits
How this subagent operates:
- [Trait 1]: [Description]
- [Trait 2]: [Description]

## Tools & Software
Preferred tools this subagent uses:
- Tool 1 (why this over alternatives)
- Tool 2 (specific capabilities needed)

## Mental Models
Core frameworks this subagent applies:
- Model 1 (when to use it)
- Model 2 (what it reveals)

## Knowledge Base
- Books: [Key texts that inform this approach]
- Influences: [People/ideas that shaped this]
- Channels: [Where to learn more]
- Frameworks: [Specific methodologies applied]

## Jargon Glossary
Define terms this subagent uses that aren't obvious:
- **Term 1**: [Plain English definition, why it matters]
- **Term 2**: [What it actually means in practice]
- **Term 3**: [Common misunderstanding vs. real meaning]

Keep it practical. Define what you'd need to Google.

## Online Communities
Where would this subagent "hang out" to discuss issues?

**Primary haunts** (active participation):
- [Community name] - [Why here? What questions get answered?]
- [Forum/Discord/Slack] - [What expertise lives here?]

**Occasional visits** (specific deep dives):
- [Specialized forum] - [When you need this specific knowledge]
- [Subreddit/Stack] - [For what edge cases?]

**Reddit communities** (curated by signal/noise):
- r/[subreddit] - [What discussions? Quality level?]
- r/[subreddit] - [When to search here?]

**Avoid** (poor signal/noise):
- [Community name] - [Why it's not useful for this job]

Include:
- Specific URLs/server names
- What expertise is concentrated there
- What questions you'd ask there
- Quality of answers (fast vs. thoughtful)

**Reddit-specific guidance:**
- Search before asking (most questions already answered)
- Sort by "top" for best discussions
- Check subreddit wiki first
- Look for "[X] professionals" threads
- AMAs from practitioners > general discussions

## Educational Background
What domain expertise does this assume?
- Required: [Must-have knowledge]
- Helpful: [Nice-to-have context]

## Hardware Requirements
Any specific compute/storage/network needs?

## CLI Tools for Autonomous Delivery

**IMPORTANT**: All tools must be validated as real, available packages. Use web search to verify existence before including.

**Required tools** (subagent cannot run without these):
- `tool_name` - What it does, why required (verified: package manager/source)
- `tool_name` - What it does, why required (verified: package manager/source)

**Optional tools** (enhance but not required):
- `tool_name` - What it enables, tradeoff if missing (verified: package manager/source)

**Installation:**
```bash
# Required - all commands verified
install_command_1
install_command_2

# Optional - all commands verified
install_command_3
```

**Health check:**
```bash
# Test all required tools are available and working
./scripts/check_subagent_tools.sh [subagent_name]
```

**Autonomous usage pattern:**
```bash
# How this subagent uses tools without human intervention
tool_name [inputs] | tool_name [process] > artifact.json
```

## LLM Configuration

**Ideal model:** `model-name` (as of YYYY-MM-DD)

**Why this model:**
- [Specific capability 1] - Why it matters for this job
- [Specific capability 2] - Performance requirement
- [Specific capability 3] - Cost/speed tradeoff

**Leaderboard validation:**
Before selecting a model, check current leaderboards for this job:
```bash
# Check reasoning leaderboards
# - Vellum LLM Leaderboard (reasoning, GPQA Diamond)
# - Artificial Analysis (speed + quality)
# - LM Arena (user preference for this task type)

# For technical reasoning jobs:
# Primary: GPQA Diamond, AIME benchmarks
# Secondary: HumanEval for code-heavy reasoning

# For product strategy jobs:
# Primary: LM Arena multi-turn scores
# Secondary: Real-world user preference data

# Update model choice if leaderboards show >10% improvement
```

**Minimum requirements:**
- Context window: [size needed]
- Reasoning capability: [what level]
- Speed: [response time needed]
- Cost: [$/1M tokens budget]

**Model fallbacks:**
1. Primary: `model-name-1` - Best for this job
2. Secondary: `model-name-2` - If primary unavailable
3. Minimum: `model-name-3` - Acceptable but degraded performance

**Model check script:**
```bash
# Check if assigned model is still relevant
./scripts/check_model_currency.sh [subagent_name]

# Also check leaderboards for this job type
./scripts/check_llm_leaderboards.sh [job_type]

# Returns:
# - Current model vs. leaderboard leaders
# - Benchmark scores for this task
# - Newer alternatives if available
# - Cost/performance tradeoffs
```

**Review schedule:**
- Check model currency: Every 3 months
- Check leaderboards: Every 3 months (same review)
- Last reviewed: YYYY-MM-DD
- Next review: YYYY-MM-DD

**Performance benchmarks:**
Track these metrics to know if model needs updating:
- Metric 1: [target value] - [actual value]
- Metric 2: [target value] - [actual value]
- Metric 3: [target value] - [actual value]

If actual < target, trigger model review + leaderboard check.

**Leaderboard tracking:**
For this job type, monitor these leaderboards:
- Primary: [Specific leaderboard + benchmark]
- Secondary: [Backup leaderboard]
- Reasoning: [Why these benchmarks matter for this job]

Example:
- Primary: Vellum GPQA Diamond (measures deep technical reasoning)
- Secondary: Artificial Analysis speed/quality (cost-effectiveness)
- Reasoning: This subagent needs deep multi-step reasoning, not just speed

## When NOT to Use
What jobs is this NOT hired to do?

## Collaborates With

**Upstream** (depends on these subagents):
- [Subagent name] - Provides: [what you need from it]
- [Subagent name] - Provides: [what you need from it]

**Downstream** (feeds into these subagents):
- [Subagent name] - Consumes: [what artifacts you produce]
- [Subagent name] - Consumes: [what artifacts you produce]

**Parallel** (runs alongside, shares context):
- [Subagent name] - Coordinates: [what you sync on]

**Conflicts With** (don't run together):
- [Subagent name] - Because: [why they clash]

## Example Integration
Show it composed with other subagents.

## Success Metrics
How do you know it did the job well?

## Work Journal

Every subagent maintains a recurring journal to improve retrospectively.

**Journal location:** `journals/[subagent_name]/YYYY-MM.md`

**Update frequency:** After each significant use (or weekly minimum)

**Journal entries include:**

### Achievements
- What worked well this cycle
- Problems solved effectively
- Unexpected successes

### Challenges
- What didn't work as expected
- Blockers encountered
- Failure modes discovered

### Learnings
- Key insights from this cycle
- Patterns recognized
- Mental models updated

### Progress Tracking
- Metrics vs targets
- Performance trends
- Quality improvements

### Insights
- Non-obvious discoveries
- Second-order effects observed
- What surprised us

### Improvement Areas
- What to change next cycle
- Tools to add/remove/upgrade
- LLM performance issues
- Process inefficiencies

### Self-Reflection Questions
- Is this subagent still solving the right problem?
- Is the job-to-be-done still relevant?
- Are we using the right LLM?
- Are the tools still optimal?
- Should this merge with another subagent?
- Should this be split into multiple subagents?
- What would make this 10x better?

### Action Items
- [ ] Specific changes to implement
- [ ] Benchmarks to update
- [ ] Tools to evaluate
- [ ] Documentation to improve

**Review schedule:**
- Weekly: Update journal after major uses
- Monthly: Review full month, update subagent
- Quarterly: Deep review, consider major changes

**Example journal entry:**
```markdown
## 2025-11 Week 1

### Achievements
- Successfully analyzed 15 PRs, caught 3 critical issues
- Zero false positives this week

### Challenges  
- Slow on large PRs (>500 lines)
- Missed a subtle race condition

### Learnings
- Race conditions need specific prompting
- Breaking large PRs into chunks improves accuracy

### Action Items
- [ ] Add race condition patterns to prompt
- [ ] Implement chunking for large PRs
- [ ] Benchmark new approach
```
```

## Examples

Good: `prevent_scope_creep.md`
- Job: Help me say no to features that don't serve the core value prop
- Hired when: Feature requests pile up and you're losing focus

Bad: `feature_analyzer.md`
- Too generic. What's the actual job?

Good: `recover_from_production_incidents.md`
- Job: Help me debug fast and communicate clearly when things break
- Hired when: Pager goes off

Bad: `incident_handler.md`
- Doesn't capture the real job (speed + communication under pressure)

## Catalog

*Your subagents*
