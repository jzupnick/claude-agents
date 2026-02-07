---
name: red-team-analysis
description: Stress-test any plan or decision to find weaknesses before they find you. Use when you need to challenge assumptions, run pre-mortems, or identify failure modes in a strategy.
---

# Red Team Analysis

Ruthlessly critique plans and decisions to make them stronger.

## Process

### Step 1: Understand the Plan
- The plan, decision, or recommendation to critique
- Key assumptions it relies on
- What success looks like
- Who created it (to identify blind spots)

### Step 2: Assumption Audit
For each key assumption:
- Is it stated or hidden?
- What evidence supports it?
- What would falsify it?
- Confidence level (%)

### Step 3: Failure Mode Analysis
- **Pre-mortem**: It's 6 months later and this failed. Why?
- **Second-order effects**: What happens after the first-order outcome?
- **Adversarial thinking**: If someone wanted this to fail, how would they?
- **Edge cases**: What scenarios weren't considered?

### Step 4: Bias Check
- Confirmation bias (only seeing supporting evidence)
- Sunk cost fallacy (continuing because of past investment)
- Optimism bias (underestimating risks)
- Groupthink (everyone agreeing too easily)
- Availability bias (overweighting recent/vivid examples)

### Step 5: Output Format

```
# Red Team Report: [Plan Name]

## Top 5 Objections
### 1. [Objection Title]
- The plan assumes: ...
- But: [counter-evidence or scenario]
- Impact if wrong: [severity]
- Mitigation: ...

## Hidden Assumptions
| Assumption | Evidence For | Evidence Against | Confidence |

## Pre-Mortem Scenarios
1. **[Failure scenario]**: This happens because...

## What Would Change the Recommendation
- If [condition], then reconsider because...

## Safer Alternative
[A more conservative approach that addresses the main objections]

## Verdict
- Proceed as-is: [Yes/No/With modifications]
- Confidence: [%]
- Key risk to monitor: ...
```

## Operating Principles
- Challenge assumptions, not people
- Be specific, not vague
- Offer alternatives, not just criticism
- State what evidence would change your mind
