# Journals

Work journals for retrospective subagent improvement.

## Why Journals Matter

**Without journals:**
- Repeat same mistakes
- Forget what worked
- No performance tracking
- Can't improve systematically

**With journals:**
- Learn from each cycle
- Compound improvements
- Track what's working
- Make evidence-based changes

## Structure

```
journals/
  subagent_name/
    2025-10.md    # October 2025 entries
    2025-11.md    # November 2025 entries
    README.md     # Subagent-specific notes
```

## Journal Template

Copy this for each new entry:

```markdown
## YYYY-MM Week N

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
Metrics vs targets:
- Metric 1: Target X - Actual Y (trend: ↑/↓/→)
- Metric 2: Target X - Actual Y (trend: ↑/↓/→)

### Insights
- Non-obvious discoveries
- Second-order effects observed
- What surprised us

### Improvement Areas
- What to change next cycle
- Tools to add/remove/upgrade
- LLM performance issues
- Process inefficiencies

### Self-Reflection
Answer these questions:
- Is this subagent still solving the right problem?
- Is the job-to-be-done still relevant?
- Are we using the right LLM?
- Are the tools still optimal?
- Should this merge with another subagent?
- Should this be split into multiple subagents?
- What would make this 10x better?

### Action Items
- [ ] Specific change to implement
- [ ] Benchmark to update
- [ ] Tool to evaluate
- [ ] Documentation to improve
```

## Update Frequency

**Weekly:** After major uses
- Quick entry: achievements, challenges, learnings
- 5-10 minutes

**Monthly:** Full review
- Review all weekly entries
- Update subagent based on patterns
- Check if fundamentals still right
- 30-60 minutes

**Quarterly:** Deep review
- Consider major changes
- Check LLM is still optimal
- Review tool stack
- Consider merge/split decisions
- 2-4 hours

## What to Track

### Quantitative
- Performance metrics (accuracy, speed, cost)
- Usage frequency
- Success/failure rates
- Time to completion

### Qualitative
- What felt easy vs hard
- What surprised you
- What patterns emerged
- What you'd do differently

### Meta
- Is the job still relevant?
- Are metrics still right?
- Should this evolve?

## Example: Real Journal Entry

```markdown
## 2025-11 Week 1

### Achievements
- Analyzed 15 PRs this week
- Caught 3 critical race conditions
- Zero false positives
- Average analysis time: 2.3 minutes (down from 3.1)

### Challenges
- Failed on one PR with 800+ lines (timeout)
- Missed a subtle SQL injection in sanitized input
- Model hallucinated a security issue that didn't exist (false positive, but caught by human review)

### Learnings
- Large PRs need chunking strategy
- SQL injection patterns need more explicit prompting
- Model confidence scores unreliable for edge cases

### Progress Tracking
- Detection rate: Target 95% - Actual 93% (↓ from 94% last week)
- False positive rate: Target <10% - Actual 6.7% (↑ from 4%)
- Speed: Target <3min - Actual 2.3min (↑ improved)

### Insights
- The hallucinated issue came from over-aggressive security prompting
- Chunking improves accuracy but increases cost
- Human review caught the false positive in 30 seconds

### Improvement Areas
- Need better chunking strategy for large PRs
- SQL injection patterns should be explicit checklist
- Model confidence thresholds need tuning
- Consider adding human-in-loop for borderline cases

### Self-Reflection
- Job still relevant? YES - catching real issues
- Right LLM? MAYBE - check if newer models better at SQL patterns
- Right tools? YES - but need better PR chunking tool
- Merge/split? NO - scope is right
- 10x better? Human-in-loop for low-confidence cases

### Action Items
- [ ] Implement PR chunking (max 200 lines per chunk)
- [ ] Add SQL injection checklist to prompt
- [ ] Test claude-sonnet-4-5 vs current model on SQL patterns
- [ ] Design confidence threshold for human escalation
- [ ] Update benchmarks with this week's data
```

## Journal-Driven Improvements

### Pattern 1: Metrics Trending Wrong
**Journal shows:** Detection rate dropping over time
**Action:** Review recent failures, update prompts or model

### Pattern 2: Consistent Surprises
**Journal shows:** Keep being surprised by same thing
**Action:** Update mental models, add to documentation

### Pattern 3: Tool Inefficiency
**Journal shows:** Spending too much time on X
**Action:** Add/upgrade tool, automate bottleneck

### Pattern 4: Scope Drift
**Journal shows:** Solving different problems than original job
**Action:** Either refocus or acknowledge job changed

### Pattern 5: Model Degradation
**Journal shows:** Same inputs getting worse outputs
**Action:** Check leaderboards, test newer models

## Red Flags

**Stop and investigate if you see:**
- Same problem appears 3+ weeks in a row
- Metrics consistently miss targets
- You're not sure what the job is anymore
- Journal entries getting vaguer over time
- You skip updating the journal repeatedly

## Integration with Subagent Lifecycle

### After Each Use
Quick journal entry (5 min):
- What happened?
- What worked/didn't?
- One learning

### Weekly Review
Review week's entries (15 min):
- Patterns emerging?
- Action items needed?

### Monthly Update
Update subagent file (30 min):
- Improve prompts based on learnings
- Update tools if needed
- Refresh benchmarks

### Quarterly Deep Dive
Major review (2 hours):
- Should LLM change?
- Should job change?
- Should subagent evolve?

## Tips for Good Journaling

### Be Specific
Bad: "It worked well"
Good: "Caught race condition in async handler that 3 humans missed"

### Be Honest
Bad: "Everything perfect"
Good: "Missed SQL injection because pattern wasn't in prompt"

### Be Actionable
Bad: "Need to improve"
Good: "Add SQL injection patterns checklist to prompt by next week"

### Be Quantitative
Bad: "Faster than before"
Good: "2.3 min avg vs 3.1 min last week (26% improvement)"

### Be Reflective
Bad: Just list facts
Good: "Surprised model hallucinated this - suggests over-aggressive security prompting"

## Your Challenge

For each subagent you build:

1. **Create journal:** `journals/[subagent_name]/2025-11.md`
2. **After first use:** Quick entry (5 min)
3. **After 3 uses:** Review patterns
4. **After 1 month:** Update subagent based on learnings

If you're not journaling, you're not improving systematically.

What subagent will you journal first?
