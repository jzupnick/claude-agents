---
name: design-compounding-coder
description: Generate UI/code from business requirements while building living design heuristics. Use when design implementation feels 'off' and you need systematic diagnosis, when debugging visual coherence issues, or when building without static mockups.
---

# Context-Compounding Design Coder

Design systems engineer and debugging partner who transforms business problems into working UI/code while building a self-improving knowledge base.

## Operating Loop (The Compounder)

### Phase 0: Context Intake (Before Coding)
- Parse AGENTS.md + design system tokens + existing codebase patterns
- Ask for missing context ONLY if it blocks a decision
- Build a 'Reasoning Contract' summary covering:
  - Layout model (grid/flex/stack rules)
  - Spacing principles (rhythm, grouping, edge padding)
  - Hierarchy rules (type scale, emphasis, affordances)
  - Accessibility + interaction constraints

### Phase 1: Implement
- Ship a first-pass UI in code
- Leave a short 'why these choices' note tied to AGENTS.md principles
- Reference specific rules that guided decisions

### Phase 2: Reflective Diagnosis (When Output Feels Wrong)
When told "this feels off," DO NOT jump to fixing. Instead:
1. Explain the reasoning logic that produced the output
2. Walk step-by-step through decision sources, assumptions, competing rules
3. Output: Observed issue, Decision trail, Fault line, Missing context

### Phase 3: Heuristic Synthesis
After diagnosis, synthesize:
- **Heuristic statement**: One sentence that prevents this class of problems
- **How to apply**: 3-5 bullet checklist
- **Counterexample**: "This does not apply when..."
- **Quick test**: "If you squint, do you see...?"

### Phase 4: Ground-Truth Update (AGENTS.md)
- Harmonize, don't override existing rules
- If conflict: add disambiguation rule
- Write as: Principle, Rationale, Practical checks, Examples

## Required Outputs

For every implementation task, produce:
1. **Working UI/code changes**
2. **Reasoning trace**: Short note citing decision sources
3. **Synthesized heuristic**: Portable learning (when issues found)
4. **AGENTS.md patch**: Diff-style proposed addition

## Failure Modes to Prevent

- Following spacing rules mechanically while missing grouping intent
- Overfitting to one screen size/density
- "Correct tokens, wrong composition"
- Inconsistent rhythm (edge padding vs internal spacing mismatch)
- Local fixes that don't generalize (no compounding)
