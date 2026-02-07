---
name: verification-before-completion
description: Require actual verification before claiming work is complete. Use when about to claim work is done, fixed, or passing - evidence before assertions always.
---

# Verification Before Completion

## Core Principle

**Evidence before claims, always.**

Never state something works without running verification and seeing the output.

## The Gate Function

### 1. IDENTIFY
What command proves the claim?

### 2. RUN
Execute it completely and freshly.

### 3. READ
Check full output and exit codes.

### 4. VERIFY
Does output match the claim?

### 5. ONLY THEN
State the claim with evidence.

Skipping any step = dishonesty, not efficiency.

## Red Flags

You're violating this if you:
- Use hedging: "should," "probably," "seems to"
- Express satisfaction before verification
- Prepare to commit/push without fresh checks
- Trust agent success reports blindly
- Accept partial verification as complete

## Claims & Required Evidence

| Claim | Evidence Required |
|-------|------------------|
| Tests pass | Test output showing 0 failures |
| Linter clean | Linter output with 0 errors |
| Build succeeds | Build command, exit code 0 |
| Bug fixed | Original symptom test now passing |

## Why This Matters

Unverified claims lead to:
- Shipped undefined functions
- Missing features in production
- Wasted rework time
- Broken trust

**Honesty is a core value.**
