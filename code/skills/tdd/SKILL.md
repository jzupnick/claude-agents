---
name: test-driven-development
description: Enforce TDD practices for implementing features and fixes. Use when implementing any feature or bugfix - write the test first, watch it fail, write minimal code to pass.
---

# Test-Driven Development

## The Iron Law

**No production code exists without a failing test first.**

Code written before tests must be deleted entirely - not kept as reference.

## Red-Green-Refactor Cycle

### 1. RED
Write one minimal test demonstrating required behavior.

### 2. VERIFY RED (Never Skip!)
Confirm test fails for the expected reason.
- Wrong failure reason = wrong test
- No failure = test doesn't verify anything

### 3. GREEN
Write the **simplest code possible** to pass the test.
- No extra features
- No premature optimization
- Just make it pass

### 4. VERIFY GREEN
Confirm all tests pass with clean output.

### 5. REFACTOR
Clean up code while maintaining green status.

### 6. REPEAT
Next feature, next test.

## Common Rationalizations (All Wrong)

- "I'll write tests after" - You won't, or they'll be weak
- "Manual testing is enough" - It's not reproducible
- "The code already works" - How do you know?
- "TDD is slower" - It's faster including debug time
- "Just this once" - Slippery slope

## Completion Checklist

- [ ] Every new function has a failing test that was watched
- [ ] Implementation is minimal
- [ ] All tests pass
- [ ] Edge cases covered
