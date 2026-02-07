---
name: systematic-debugging
description: Framework for debugging errors, test failures, and unexpected behavior. Use when encountering bugs, issues, or problems that need investigation. Enforces root cause analysis before attempting fixes.
---

# Systematic Debugging

## Core Principle

**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.**

This is non-negotiable. Skipping to fixes wastes time and creates new bugs.

## Four-Phase Framework

### Phase 1: Root Cause Investigation

1. **Read errors carefully** - What does it actually say?
2. **Reproduce consistently** - Can you trigger it reliably?
3. **Check recent changes** - What changed before this broke?
4. **Gather multi-component evidence** - Logs, state, network, etc.
5. **Trace data flow backward** - Where did bad data originate?

### Phase 2: Pattern Analysis

1. Find working examples of similar functionality
2. Compare against references
3. Identify differences systematically
4. Map dependencies

### Phase 3: Hypothesis and Testing

1. Form specific hypotheses
2. Test minimally - one variable at a time
3. Verify results before proceeding
4. Document findings

### Phase 4: Implementation

1. Create failing test case first
2. Implement single fix addressing root cause
3. Verify the solution works
4. Run full test suite

## Critical Safeguard

**If 3+ fix attempts have failed:** Stop. Question the underlying architecture. You may be chasing symptoms of a deeper design flaw.

## Red Flags (You're Violating the Process)

- Proposing "quick fixes"
- Changing multiple variables at once
- Proceeding without full understanding
- Saying "let's just try..."
- Guessing at causes
