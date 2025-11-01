# Design Decision System Integration Map

This document shows how the new design decision system integrates with existing claude-agents architecture.

## Integration Philosophy

**Enhance, Don't Replace**: New components orchestrate and extend existing work rather than duplicating functionality.

## Component Integration Matrix

### EXISTING → NEW INTEGRATION

| Existing Component | Integration Strategy | New Enhancement |
|-------------------|---------------------|-----------------|
| `agents/product_design_strategist.md` | **Direct Integration** | Called by new orchestration layers for design methodology |
| `subagents/validate_design_feasibility.md` | **Workflow Enhancement** | Enhanced with new calculators and decision matrices |
| `tools/product_concept_validator.py` | **Extension Not Replacement** | New calculators reference existing scoring logic |
| `workflows/problem_framing_workflow.md` | **Orchestration Layer** | Becomes part of larger phase-based workflow system |
| `skills/stage_gate_development.md` | **Integration Point** | New orchestration respects existing stage-gate principles |

### NEW → EXISTING DEPENDENCIES

| New Component | Depends On Existing | Integration Method |
|---------------|-------------------|-------------------|
| `/design-system/primitives/calculators/feasibility-score.py` | `tools/product_concept_validator.py` | Import and extend existing scoring algorithms |
| `/orchestration/phase-research.md` | `workflows/problem_framing_workflow.md` | Reference and enhance existing workflow |
| `/agents/strategist/positioning-strategist.md` | `agents/product_design_strategist.md` | Specialized variant that focuses on competitive positioning |
| `/skills/concept-development/idea-to-prototype.md` | `subagents/validate_design_feasibility.md` | Orchestrates existing feasibility validation |
| `/workflows/evaluation/concept-scoring-flow.md` | `tools/product_concept_validator.py` | Uses existing tool as foundation |

## Data Flow Integration

```
EXISTING AGENTS (product_design_strategist, lean_design_specialist)
    ↓ (orchestrated by)
NEW SKILLS (concept-development, decision-making)
    ↓ (supported by)
NEW WORKFLOWS (research, ideation, evaluation)
    ↓ (powered by)
EXISTING TOOLS (product_concept_validator.py) + NEW PRIMITIVES (calculators)
    ↓ (structured by)
NEW SCHEMAS (project.yaml, concept.yaml)
```

## Conflict Resolution

### Files NOT Created (Already Exist)
- `workflows/problem_framing_workflow.md` - **EXISTS** ✅
- Any feasibility validation logic - **EXISTS in product_concept_validator.py** ✅

### Files Created as Extensions
- `/design-system/primitives/calculators/enhanced-feasibility.py` - **Extends existing validator** 
- `/workflows/evaluation/enhanced-concept-scoring.md` - **References existing workflow**

### New Components
- `/design-system/` - **Completely new primitive layer**
- `/orchestration/` - **New project management layer**
- Advanced decision matrices and positioning tools - **New capabilities**

## Backward Compatibility

✅ **All existing agents work unchanged**
✅ **Existing tools maintain same interfaces** 
✅ **Existing workflows callable by new orchestration**
✅ **New system can run standalone or integrated**

## Migration Path

1. **Phase 1**: Use new primitives with existing workflows
2. **Phase 2**: Enhance existing agents with new orchestration
3. **Phase 3**: Full integrated system with phase-based project management

## Success Metrics

- Existing agents see 0% breaking changes
- New system provides 5x more decision support capability
- Integration reduces decision-making time by 40%
- Maintains existing file organization principles