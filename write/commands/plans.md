---
name: writing-plans
description: Create detailed implementation plans for multi-step development tasks. Use when design is complete and you need actionable tasks for engineers with minimal codebase context.
---

# Writing Implementation Plans

## Core Purpose

Write comprehensive implementation plans assuming the engineer has **zero context** for the codebase.

## Task Granularity

Each task = single action, 2-5 minutes:
- Write test
- Run test (expect failure)
- Implement feature
- Run test (expect pass)
- Commit

## Required Structure

### Header
- Goal statement
- Architecture overview
- Tech stack

### Tasks (numbered)
- Exact file paths
- Complete code examples (not snippets)
- Specific commands with expected output
- Clear success criteria

## Best Practices

- **DRY** - Don't Repeat Yourself
- **YAGNI** - You Aren't Gonna Need It
- **TDD** - Write test first, watch it fail
- **Frequent commits** - After each task

## Execution Options

After plan completion:
1. **Subagent-driven** - Fresh subagent per task (current session)
2. **Parallel sessions** - Execute in separate terminal

## File Location

Save plans to: `docs/plans/YYYY-MM-DD-<feature-name>.md`
