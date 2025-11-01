# Subagent Collaboration Patterns

How subagents work together to get complex jobs done.

## Why This Matters

Single subagent = one perspective.
Composed subagents = system that catches blind spots.

## Four Collaboration Types

### 1. Upstream/Downstream (Sequential)
One subagent's deliverable becomes another's input.

**Example:**
```
challenge_technical_assumptions
  ↓ (passes: top 3 risky assumptions)
accelerate_prototyping
  ↓ (passes: prototype results)
estimate_true_costs
  ↓ (passes: quantified risks)
communicate_technical_risk
```

**When to use:** Clear workflow, each step depends on previous.

### 2. Parallel (Simultaneous)
Multiple subagents run on same input, compare results.

**Example:**
```
evaluate_vendor_claims + challenge_technical_assumptions
Both question: "Is this actually true?"
Sync on: Where marketing diverges from technical reality
```

**When to use:** Need multiple perspectives, cross-validation.

### 3. Conflicts (Mutually Exclusive)
Subagents that shouldn't run together.

**Example:**
```
find_core_value ⚡ add_feature_parity
One kills features, one adds them.
```

**When to use:** Force yourself to choose a strategy.

### 4. Recursive (Self-Referential)
Subagent calls itself with refined input.

**Example:**
```
challenge_assumptions → finds new assumption → challenge_assumptions again
```

**When to use:** Iterative refinement, drilling down.

## Artifacts vs Deliverables Pattern

**Rule:** Subagents exchange artifacts. Humans get deliverables.

```
Subagent A → Artifact (structured data) → Subagent B
Subagent B → Deliverable (decision-ready) → Human
```

**Why:**
- Artifacts can be messy, machine-readable, comprehensive
- Deliverables must be clear, actionable, concise
- Humans don't want to see your work, they want decisions

**Example:**
```
Artifact: 47-row risk matrix with probabilistic scores
Deliverable: "Don't do X. If you must, mitigate Y first."
```

## Stakeholder Rules

### Primary Stakeholders
- Have decision authority
- Must act on deliverable
- Get full context, not summary

### Secondary Stakeholders  
- Need to know for coordination
- Don't make final decision
- Get summary, not full context

### Excluded Stakeholders
- Too early for them
- Would derail with premature input
- Explicitly leave them out

**Example:**
Don't send executives a technical risk assessment while you're still exploring. They'll make a premature decision. Send them the recommendation after you've done the work.

## Common Mistakes

**Mistake 1: Linear thinking**
Bad: Always run subagents in sequence
Good: Some should run parallel for cross-checking

**Mistake 2: Over-communication**
Bad: Share all artifacts with all stakeholders
Good: Filter artifacts into appropriate deliverables

**Mistake 3: No conflicts defined**
Bad: Run contradictory subagents simultaneously, get confused
Good: Force yourself to choose one strategy

**Mistake 4: Forgetting exclusions**
Bad: CC everyone on everything
Good: Explicitly exclude people who would derail at this stage

## Design Questions

When creating a subagent, ask:

1. **What artifacts does this produce for other subagents?**
   - Structured data? Scored lists? Dependency graphs?

2. **What deliverables does this produce for humans?**
   - Decisions? Recommendations? One-pagers?

3. **Who must this integrate with?**
   - What comes before? What comes after?

4. **Who should this conflict with?**
   - What strategies are mutually exclusive?

5. **Who sees what?**
   - Which stakeholders get which deliverables?

## Your Challenge

Pick two subagents you're building. Define:
- What artifacts they exchange
- What deliverables they produce
- Whether they run sequential, parallel, or conflict
- Who's excluded from seeing what

If you can't answer these, you don't understand how they fit together yet.
