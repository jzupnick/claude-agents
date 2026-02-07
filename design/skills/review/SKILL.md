---
name: design-review
description: Translate opportunity into product architecture and specifications. Use when creating design summaries, concept development, system architecture, requirements specs, or preliminary BOMs for product development.
---

# Design Review

Translate market opportunity into product architecture, specifications, and validated concepts. Bridge strategy and execution.

## Process

### Step 1: Gather Context
- What opportunity/problem are we designing for?
- Existing discovery outputs (opportunity_map, customer_segments, jobs_to_be_done)?
- Constraints (time, budget, technical skills)?
- Hardware or software (or both)?
- Any existing prototypes or concepts?

### Step 2: Concept Development
Generate 2-3 concept options, each with:
- **Core approach** — How it solves the job-to-be-done
- **Technical feasibility** — Can a solo founder build this?
- **Manufacturing feasibility** — (If hardware) Can this be made?
- **Key tradeoffs** — What you give up for what you gain
- **Risk profile** — What could go wrong

### Step 3: Architecture Design
For the selected concept, produce:
- **System architecture** (use Mermaid diagrams)
- **Component breakdown** — Major subsystems
- **Interface definitions** — How parts connect
- **Technology choices** — With rationale

### Step 4: Requirements & Specs
Create:
- **PRD outline** — Key requirements prioritized (Must/Should/Could)
- **Functional specifications** — What it does
- **Preliminary BOM** — (If hardware) Initial bill of materials
- **DFM/DFA considerations**

### Step 5: Risk Assessment
| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|

### Step 6: Red-Team
- What's the weakest technical assumption?
- What will be hardest to change later?
- Where might we over-engineer?
- What's the simplest version that validates the concept?

## Output Format

```markdown
# Design Summary: [Project Name]

## Selected Concept
[1-2 sentence description]

## System Architecture
[Mermaid diagram]

## Key Requirements (MoSCoW)
### Must Have / Should Have / Could Have

## Preliminary BOM (if hardware)
| Component | Purpose | Est. Cost | Source |

## Technical Risks
| Risk | Likelihood | Impact | Mitigation |

## Design Decisions Made
1. [Decision] — Rationale: [why]

## Next Action
[Single concrete step, ≤30 min]
```

## Architecture Principles

- Prefer modular over monolithic (easier to iterate)
- Prefer standard interfaces over custom (cheaper, faster)
- Prefer proven technology over cutting-edge (lower risk)
- Design for testability and serviceability
