---
name: brainstorming
description: Guide for collaborative design work before implementation. Use when creating or developing ideas, before writing code or implementation plans. Refines rough ideas into detailed specifications through structured dialogue.
---

# Brainstorming

Transform ideas into detailed specifications through structured dialogue.

## Process

### 1. Understand the Idea
- Examine project context
- Ask targeted questions **one at a time**
- Offer multiple-choice options when possible

### 2. Explore Approaches
- Propose 2-3 options with trade-offs
- Apply YAGNI ruthlessly (remove unnecessary features)
- Consider alternatives before settling

### 3. Present Design
- Break into 200-300 word sections
- Cover: architecture, components, data flow, error handling, testing
- Validate understanding after each section
- Get explicit approval before proceeding

## Key Principles

- **One question at a time** - Don't overwhelm
- **Offer choices** - Multiple-choice beats open-ended
- **Remove unnecessary features** - Ruthless YAGNI
- **Be flexible** - Revisit and clarify when needed
- **Validate often** - Check understanding at each step

## After Validation

1. Document design in `docs/plans/YYYY-MM-DD-<topic>-design.md`
2. Use clear, concise writing
3. Commit to git
4. Offer to establish implementation workspace (git worktrees)
