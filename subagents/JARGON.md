# Jargon: When to Define It

Not all terminology needs explanation. But some does.

## The Test

If someone smart but outside your domain would have to Google it, define it.

## What to Define

### 1. Domain-Specific Terms
Terms that mean something different in context.

**Example:**
- "CAP theorem" in distributed systems
- "Jobs To Be Done" in product
- "Pre-mortem" in risk analysis

Not: "API" or "database" (too basic)

### 2. Overloaded Words
Common words with specific meanings in your domain.

**Example:**
- "Artifact" (you mean internal outputs, not ancient relics)
- "Deliverable" (you mean decision-ready docs, not pizza)
- "Stakeholder" (you mean specific roles, not vague "interested parties")

### 3. Acronyms That Aren't Universal
If it's not universally known, spell it out once.

**Example:**
- First use: "Architecture Decision Records (ADRs)"
- After: "ADRs"

Not: "HTTP" or "CEO" (universally known)

### 4. Framework-Specific Concepts
Terms from specific methodologies.

**Example:**
- "Lindy effect" (from Taleb)
- "Kano model" (from product management)
- "Cost of delay" (from lean)

### 5. Terms You're Using Differently
If you're using a term in a non-standard way, call it out.

**Example:**
"By 'prototype' I mean production-quality code for the hard part, not a throwaway mockup."

## What NOT to Define

### 1. Basic Technical Terms
Don't define things anyone in tech knows.

**Skip:**
- "Git", "commit", "branch"
- "Function", "variable", "loop"
- "User", "product", "feature"

### 2. Common Business Terms
Standard business vocabulary doesn't need explanation.

**Skip:**
- "ROI", "revenue", "customer"
- "Meeting", "deadline", "budget"
- "Team", "project", "milestone"

### 3. Terms You Just Defined
Don't repeat definitions. Define once, use freely after.

## How to Define

### Pattern 1: Plain English + Why It Matters
```
**Pre-mortem**: Assume failure happened, work backwards to causes. 
Not "what could go wrong" but "we failed, why?"
```

What it is + why it's different from related concepts.

### Pattern 2: Contrast with Misunderstanding
```
**Outcome vs. output**: Output = features shipped. Outcome = behavior 
changed, value delivered. Stop measuring output.
```

Show the common confusion, then clarify.

### Pattern 3: Practical Example
```
**Second-order effects**: Not the immediate result, but what that 
result causes. Example: "Making deploys faster" (first-order) → 
"Team deploys more often" (second-order) → "More surface area for 
bugs" (third-order)
```

Abstract concept → concrete example.

### Pattern 4: The "Actually Means" Formula
```
**Product/Market Fit (PMF)**: When you've found a job worth solving 
for people willing to pay. Sean Ellis's test: "Would you be very 
disappointed if this product disappeared?"
```

What people say + what it actually means + how to measure.

## Organization

### In Subagent Template
Keep definitions in one "Jargon Glossary" section.
- Alphabetical if many terms
- Order of appearance if few terms

### In Workflow Docs
Define inline on first use, then link back to glossary.

```markdown
When doing a pre-mortem (see [Jargon Glossary](#jargon-glossary))...
```

## Common Mistakes

### Mistake 1: Defining Everything
Makes docs unreadable. Define what needs defining.

### Mistake 2: Academic Definitions
Bad: "Pre-mortem: A prospective hindsight technique..."
Good: "Pre-mortem: Assume failure happened, work backwards to causes."

### Mistake 3: No Examples
Abstract definitions don't stick. Show, don't just tell.

### Mistake 4: Circular Definitions
Bad: "Feature bloat is when you have bloated features"
Good: "Feature bloat: Adding features feels like progress but creates maintenance debt, UI complexity, and confusion about what you actually do."

## Your Test

For each term in your subagent:

1. **Would a smart engineer from a different domain know this?**
   - Yes → Don't define
   - No → Define

2. **Is this term doing real work in understanding the subagent?**
   - Yes → Define it well
   - No → Maybe don't use it

3. **Can you define it in one sentence with an example?**
   - Yes → Good definition
   - No → Either you don't understand it or it's too complex (simplify)

## Examples from Real Subagents

**Good:**
```
**Yak shaving**: Solving problem A requires solving B, which requires 
C... and you end up literally shaving a yak. The chain of dependencies 
that keeps you from the real work.
```
- Plain English
- Memorable image
- Why it matters (blocks real work)

**Bad:**
```
**Optimization**: Making things better
```
- Too vague
- No specificity
- Doesn't actually help

**Good:**
```
**The "when" statement**: "When [situation], I use [product] to [outcome]" 
- Clayton Christensen. If you can't fill this in, you don't know your job.
```
- Format given
- Source cited
- Test for understanding

## Your Assignment

Take one subagent you're building. List every term that might need defining. Cut the list in half (too many definitions = none of them stick). Define the survivors using the patterns above.

If you can't define a term clearly, you might not understand it well enough to use it.
