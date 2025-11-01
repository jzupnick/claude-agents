# Problem Framing Workflow

| name | description | model | category |
|------|-------------|-------|----------|
| problem-framing-workflow | Early-stage innovation pipeline linking strategy, user insight, and technical feasibility before development | sonnet | product strategy |

## Purpose
Systematically frame problems worth solving by integrating trends analysis, user insights, and technical architecture assessment before committing to development resources.

## Core Philosophy
Problem framing is the foundation of successful innovation. By connecting market opportunities with user needs and technical feasibility, we ensure development efforts focus on problems that are both important and solvable.

## Workflow Overview

### Phase 1: Opportunity Recognition
**Duration**: 1-2 weeks
**Key Activities**:
- Market scanning and trend identification
- Competitive landscape analysis
- Technology advancement monitoring
- User pain point discovery

**Deliverables**:
- Opportunity landscape map
- Trend analysis report
- Initial problem hypotheses

### Phase 2: Problem Framing Circle
**Duration**: 2-3 weeks
**Parallel Investigation Tracks**:

#### Track A: Trends & Inspiration
- **Input Sources**: Market research, analog industries, emerging technologies
- **Activities**: Pattern recognition, trend synthesis, inspiration gathering
- **Output**: Trend-driven opportunity areas

#### Track B: Insights Discovery
- **Input Sources**: User research, behavioral observations, need analysis
- **Activities**: User interviews, ethnographic research, need prioritization
- **Output**: Distilled user insights and behavioral patterns

#### Track C: Technical Architecture
- **Input Sources**: Technology assessment, feasibility analysis, capability mapping
- **Activities**: Technical spike exploration, architecture options, constraint identification
- **Output**: Feasibility framework and technical constraints

### Phase 3: Integration & Synthesis
**Duration**: 1 week
**Key Activities**:
- Overlay analysis of all three tracks
- Problem statement refinement
- Solution space definition
- Go/no-go decision preparation

**Deliverables**:
- Integrated problem framework
- Solution opportunity assessment
- Technical feasibility validation

## Iterative Process Flow

```
Research → Visioning → Concepts → Review → Research → Develop
    ↑                                            ↓
    ←←← Feedback Loop ←←← Validation ←←←←←←←←←←←←
```

### Research Phase
- User research and market analysis
- Technical feasibility exploration
- Competitive intelligence gathering

### Visioning Phase
- Problem statement synthesis
- Solution vision articulation
- Success criteria definition

### Concepts Phase
- Solution concept generation
- Rapid prototyping and testing
- Concept evaluation and selection

### Review Phase
- Stakeholder alignment checkpoint
- Technical architecture review
- Market opportunity validation

## Quality Gates

### Gate 1: Opportunity Recognition Review
**Criteria**:
- Market opportunity size validated (>$100M addressable market)
- User pain point severity confirmed (high urgency/frequency)
- Competitive landscape understood (clear differentiation path)

### Gate 2: Problem Framing Complete
**Criteria**:
- All three investigation tracks completed
- Problem statement clearly articulated
- Solution space well-defined
- Technical feasibility confirmed

### Gate 3: Development Readiness
**Criteria**:
- Solution concepts validated with users
- Technical architecture approved
- Resource requirements defined
- Success metrics established

## Tools Integration

### Research Tools
- `user_research_coordinator` - User interview planning and execution
- `market_analysis_specialist` - Competitive and market research
- `technical_feasibility_validator` - Technology assessment

### Analysis Tools
- `trend_pattern_analyzer` - Pattern recognition across data sources
- `insight_synthesizer` - User insight distillation
- `technical_architecture_evaluator` - Feasibility assessment

### Documentation Tools
- `problem_statement_generator` - Structured problem articulation
- `opportunity_mapper` - Visual opportunity mapping
- `workflow_tracker` - Progress and milestone tracking

## Success Metrics

### Process Metrics
- Time to problem validation: <6 weeks
- Stakeholder alignment score: >80%
- Technical feasibility confidence: >70%

### Outcome Metrics
- Problems proceeding to development: >60% success rate
- User need validation accuracy: >85%
- Technical estimate accuracy: ±20% variance

## Risk Management

### Common Pitfalls
- Rushing to solutions before understanding problems
- Ignoring technical constraints early
- Insufficient user validation
- Inadequate market opportunity assessment

### Mitigation Strategies
- Enforce gate criteria strictly
- Maintain parallel investigation tracks
- Regular cross-track synchronization
- Early technical spike validation

## When NOT to Use
- For well-understood problems with established solutions
- When speed-to-market is more critical than problem validation
- For incremental feature additions to existing products
- When technical architecture is predetermined

## Integration with Other Workflows
- **Upstream**: Strategic planning and innovation pipeline
- **Downstream**: `stage_gate_development` for systematic development
- **Parallel**: User research and technical architecture workflows

## Example Application
Applied to emergency alert system development: identified user confusion during high-stress scenarios (insights), leveraged CAP protocol standardization trend (trends), and confirmed iOS notification framework capabilities (technical architecture) to frame the problem of "reliable emergency communication under stress."