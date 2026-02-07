---
name: product-prototype-plan
description: "Use when planning prototypes, designing validation experiments, creating MVPs, or running user testing"
---

# Product Prototype Planning

Own the Prototyping and Testing track. Build, test, and validate. Provide the reality check that separates assumptions from evidence.

## Testing Philosophy

### Validation Hierarchy
1. Does it work? (Technical validation)
2. Can users use it? (Usability validation)
3. Do users want it? (Desirability validation)
4. Will users pay for it? (Value validation)
5. Does it survive real-world use? (Reliability validation)

### Test Design Principles
- Test to fail, not to pass (find the weaknesses)
- Test with real users, not proxies
- Test in real environments, not just lab
- Test edge cases, not just happy path
- Document everything -- failures are data

### Sample Size Guidance
- Usability testing: 5 users catches 85% of issues
- Customer validation: 10-20 for qualitative signal
- Reliability testing: Depends on failure modes
- Beta program: 10-50 depending on use case diversity

## Prototype Progression

| Stage | Purpose | Fidelity | Validates |
|-------|---------|----------|-----------|
| Visual Models | Form, scale, aesthetics | Low (foam, 3D prints) | Form factor, ergonomics |
| Engineering Breadboard | Technical feasibility | Functional but rough | Core technical assumptions |
| Alpha Prototype | Concept validation | Functional, rough finish | Problem-solution fit, usability |
| Working Prototype | Design refinement | Near-production | Full feature set, performance |
| Beta Units | Production validation | Production-representative | Reliability, manufacturability |
| Lab/Field/Site Testing | Comprehensive validation | Production units | All specs, real-world performance |

## Prototype Planning Process

### Step 1: Gather Inputs
Collect from the user:
- User jobs-to-be-done (what are they trying to accomplish?)
- Constraints (time, tech, team)
- Existing patterns to leverage
- Accessibility requirements
- What question does this prototype need to answer?

### Step 2: Decompose into Tasks
Assign to worker perspectives:
- **UX Designer**: Interaction patterns, component selection, flow design
- **Facilitator**: Test planning, participant recruitment, session structure

### Step 3: Scope the Prototype
Determine fidelity level:
- **Paper/Lo-fi**: Test concepts, flows, mental models
- **Clickable**: Test interactions, navigation, task completion
- **Hi-fi**: Test visual design, micro-interactions, emotional response

Rule: Use the lowest fidelity that answers the question.

### Step 4: Define Key Flows
For each critical user task:
- Entry point
- Steps (numbered)
- Decision points
- Success state
- Error states

### Step 5: Red-Team (Challenger)
Switch to UX Researcher perspective:
- What biases might this prototype introduce?
- Are we testing the right thing?
- What will we NOT learn from this?
- Accessibility blind spots?

### Step 6: Deliver Prototype Plan
Include:
- Research question ("Will users [behavior] when [condition]?")
- Prototype scope (fidelity, screens/states, out of scope)
- Key flows with detailed steps
- Usability risks with likelihood and testing approach
- Test script outline (intro, background questions, tasks, debrief)
- What we will learn / will not learn / follow-up needed
- Next action (first build step, completable in 15 minutes or less)

## Validation Methods (Match Fidelity to Stage)

### Problem Validation
- Customer interviews (5-10 minimum)
- Problem surveys
- Existing behavior analysis
- Competitor review analysis

### Solution Validation
- Concept tests (descriptions, mockups)
- Smoke tests / fake door tests
- Landing page + signup
- Wizard of Oz / Concierge MVP
- Crowdfunding / pre-orders

### Product Validation
- Usability testing (5 users catches 85% of issues)
- Beta programs
- Cohort analysis
- NPS / CSAT
- Retention curves

## Anti-Patterns to Avoid
- Do NOT skip fidelity levels to save time -- you will waste more later
- Do NOT test with friends and family -- biased signal
- Do NOT hide negative results -- they are the most valuable
- Do NOT over-test before design freeze -- things will change
- Do NOT under-test after design freeze -- this is the last chance
- Do NOT confuse prototype success with product success

## Operating Principles
- Prototype early, before you are ready
- Externalize thinking -- make it visible
- Meaning before polish
- Test with real users, not assumptions
- Be evidence-based and unflinching
- Lead with the finding (pass/fail/inconclusive), then the data, then the implications
- Distinguish between critical failures and minor issues
- When tests fail, diagnose root cause and recommend action

## Reference Frameworks
- Wizard of Oz MVP
- Concierge MVP
- Fake Door / Smoke Tests
- 5-User Usability Testing (Nielsen)
- A/B Testing
- Cohort Analysis
