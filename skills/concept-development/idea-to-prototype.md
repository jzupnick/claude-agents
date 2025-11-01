# Idea-to-Prototype Skill
*Northwestern MPD2 Knowledge Funnel Application*

| name | description | model | category |
|------|-------------|-------|----------|
| idea-to-prototype | Master skill for systematic progression from initial ideas to validated prototypes using Northwestern MPD2 Knowledge Funnel methodology and multi-agent orchestration | sonnet | concept-development |

## Purpose
Orchestrate multiple agents to systematically progress ideas through the Knowledge Funnel (Mystery → Heuristic → Algorithm) stages, ensuring appropriate validation and resource allocation at each phase while maintaining momentum toward prototype development.

## Core Philosophy
Effective idea development requires systematic progression through uncertainty reduction using Northwestern MPD2 Knowledge Funnel methodology. Each stage demands different approaches, validation techniques, and resource allocation strategies. Success depends on matching methodology to uncertainty level while maintaining systematic progression.

## Orchestrated Agents

**Primary Agents:**
- `northwestern-opportunity-strategist.md` - Knowledge Funnel stage classification and progression planning
- `systematic-concept-evaluator.md` - Stage-appropriate evaluation and validation
- `strategic-brief-writer.md` - Stakeholder communication and decision support

**Supporting Agents:**
- `product_design_strategist.md` (existing) - Design methodology guidance
- `lean_design_specialist.md` (existing) - Rapid validation approaches

**Integration Points:**
- Existing `validate_design_feasibility.md` subagent for technical validation
- Existing `find_core_value.md` subagent for value proposition clarity

## Capabilities

### Knowledge Funnel Orchestration:
- **Mystery Stage Management**: Exploration-focused approaches with assumption identification
- **Heuristic Stage Development**: Pattern recognition and framework building
- **Algorithm Stage Optimization**: Systematic execution and performance optimization
- **Stage Transition Planning**: Appropriate criteria and validation for progression

### Multi-Agent Coordination:
- **Stage-Appropriate Agent Selection**: Match agent capabilities to uncertainty levels
- **Progressive Validation**: Increasing rigor as investment and confidence grow
- **Cross-Stage Learning**: Capture insights for future idea development
- **Quality Assurance**: Systematic validation of progression decisions

### Prototype Development:
- **Systematic Progression**: Clear path from concept to working prototype
- **Risk-Adjusted Investment**: Resource allocation matching confidence levels
- **Assumption Validation**: Systematic testing of critical assumptions
- **Decision Gate Management**: Clear criteria for stage progression

## Data Flow Architecture

```
Input: Initial Idea + Development Context
    ↓
northwestern-opportunity-strategist (Knowledge Funnel Classification)
    ↓ (Stage Assessment + Progression Plan)
systematic-concept-evaluator (Stage-Appropriate Evaluation)
    ↓ (Validated Concept + Risk Assessment)
Prototype Development Engine (Northwestern Methodology)
    ↓ (Working Prototype + Validation Evidence)
strategic-brief-writer (Stakeholder Communication)
    ↓
Output: Validated Prototype + Development Plan
```

## Behavioral Traits
- **Systematically progressive**: Applies Knowledge Funnel logic with discipline
- **Stage-appropriate**: Matches methodology to uncertainty level
- **Learning-focused**: Captures insights for systematic improvement
- **Prototype-oriented**: Maintains focus on tangible deliverable

## Usage Pattern

### 1. Mystery Stage (Initial Exploration)
```bash
# Strategic classification and exploration planning
python design-system/primitives/calculators/opportunity-score.py \
    initial_market.yaml rough_idea.yaml --stage mystery \
    --output exploration_plan.md

# Risk assessment for exploration approach
python design-system/primitives/calculators/risk-score.py \
    rough_idea.yaml --assumptions initial_assumptions.yaml \
    --output exploration_risks.md
```

### 2. Heuristic Stage (Pattern Development)
```bash
# Enhanced concept development and validation
python design-system/primitives/calculators/feasibility-score.py \
    developed_concept.yaml --constraints heuristic_constraints.yaml \
    --output concept_validation.md

# Trade-off analysis for concept refinement
python design-system/primitives/generators/trade-off-matrix.py \
    concept_variants.yaml development_criteria.yaml \
    --output concept_tradeoffs.md
```

### 3. Algorithm Stage (Prototype Development)
```bash
# Systematic prototype development planning
./skills/concept-development/idea-to-prototype.md \
    --concept validated_concept.yaml \
    --stage algorithm \
    --output prototype_plan.md
```

## Northwestern Framework Implementation

### Knowledge Funnel Stage Management:

**Mystery Stage (Exploration - 10-20% of resources):**
- Focus on understanding problem and opportunity space
- Assumption identification and initial validation
- Multiple concept variants exploration
- Learning-oriented experimentation

**Heuristic Stage (Development - 30-50% of resources):**
- Pattern recognition and framework development
- Systematic concept refinement
- Structured validation experiments
- Trade-off analysis and optimization

**Algorithm Stage (Execution - 50-70% of resources):**
- Systematic prototype development
- Performance optimization
- Scalability planning
- Market preparation

### Stage Transition Criteria:

**Mystery → Heuristic Transition:**
- Problem clearly defined and validated
- Initial market opportunity confirmed
- Core assumptions identified
- Technical feasibility demonstrated

**Heuristic → Algorithm Transition:**
- Solution approach validated
- Business model confirmed
- Technical solution proven
- Market acceptance demonstrated

## Orchestration Workflow

### Phase 1: Mystery Stage Exploration
**Orchestrates**: `northwestern-opportunity-strategist` + exploration agents

**Activities:**
- Apply Knowledge Funnel classification (Mystery stage)
- Identify critical assumptions requiring validation
- Design exploration experiments and learning plan
- Assess initial feasibility and opportunity potential

**Outputs:**
- Knowledge Funnel stage classification
- Critical assumption register
- Exploration plan with experiments
- Initial opportunity assessment

### Phase 2: Heuristic Stage Development
**Orchestrates**: `systematic-concept-evaluator` + development agents

**Activities:**
- Develop systematic concept framework
- Execute structured validation experiments
- Apply trade-off analysis across concept variants
- Build systematic understanding of solution space

**Outputs:**
- Validated concept framework
- Systematic evaluation results
- Trade-off analysis matrix
- Refined business model

### Phase 3: Algorithm Stage Prototyping
**Orchestrates**: Multiple agents with Northwestern execution methodology

**Activities:**
- Systematic prototype development planning
- Execute development with performance monitoring
- Validate prototype against success criteria
- Prepare for market testing and scaling

**Outputs:**
- Working prototype
- Performance validation results
- Market readiness assessment
- Scaling preparation plan

### Phase 4: Communication and Next Steps
**Orchestrates**: `strategic-brief-writer` + stakeholder preparation

**Activities:**
- Synthesize development journey and learnings
- Prepare stakeholder briefing on prototype
- Plan next phase development strategy
- Document systematic methodology for replication

**Outputs:**
- Prototype briefing package
- Development lessons learned
- Next phase strategic plan
- Methodology documentation

## Success Metrics

### Knowledge Funnel Progression:
- Stage transition accuracy (appropriate timing and criteria)
- Resource allocation efficiency by stage
- Learning velocity (assumption validation rate)
- Prototype quality vs development investment

### Prototype Development:
- Time from idea to working prototype
- Prototype performance vs success criteria
- Market validation results
- Technical feasibility confirmation

### Process Efficiency:
- Agent coordination effectiveness
- Decision quality at stage transitions
- Stakeholder satisfaction with progression
- Methodology replication success

## Integration with Existing Systems

### Leverages Existing Capabilities:
- **Design Methodology**: `product_design_strategist.md` for systematic design approaches
- **Rapid Validation**: `lean_design_specialist.md` for quick validation cycles
- **Feasibility Assessment**: `validate_design_feasibility.md` for technical/market validation
- **Value Discovery**: `find_core_value.md` for value proposition optimization

### Enhances Existing Processes:
- **Idea Management**: Adds systematic progression methodology
- **Prototype Planning**: Provides strategic framework for development
- **Resource Allocation**: Stage-appropriate investment strategies
- **Risk Management**: Systematic assumption validation and risk mitigation

## Northwestern Academic Rigor Application

### Systematic Methodology:
- Clear Knowledge Funnel stage classification with evidence
- Stage-appropriate validation methodology selection
- Progressive resource commitment aligned with confidence
- Systematic documentation for learning and improvement

### Knowledge Funnel Discipline:
- Mystery stage: Maximum exploration, minimum premature optimization
- Heuristic stage: Systematic pattern development and validation
- Algorithm stage: Execution optimization with performance focus
- Stage transitions: Clear criteria and evidence-based decisions

### Academic Framework Integration:
- Research-based approach to concept development
- Systematic literature review for relevant patterns
- Structured experimentation with hypothesis testing
- Documentation standards enabling replication and learning

## Example Integration Scenarios

### Scenario 1: Software Product Idea
**Context**: Team has initial idea for productivity software

**Orchestration Process:**
1. **Mystery Stage**: Northwestern classification (likely Horizon 2), user research design, technical feasibility exploration
2. **Heuristic Stage**: Systematic feature framework development, user validation experiments, technical architecture validation
3. **Algorithm Stage**: MVP development with performance monitoring, market validation testing
4. **Communication**: Stakeholder briefing with next phase planning

**Expected Outcomes**: Working MVP with validated user need, technical feasibility, and market potential

### Scenario 2: Hardware Innovation Concept
**Context**: Engineering team identifies potential hardware optimization opportunity

**Orchestration Process:**
1. **Mystery Stage**: Market opportunity assessment, technical constraint identification, competitive analysis
2. **Heuristic Stage**: Systematic engineering approach development, performance requirement validation, manufacturing feasibility
3. **Algorithm Stage**: Functional prototype development, performance testing, manufacturing pilot
4. **Communication**: Executive briefing with commercialization planning

**Expected Outcomes**: Functional prototype with validated performance, manufacturing feasibility, and market opportunity

### Scenario 3: Service Design Innovation
**Context**: Service delivery problem identified requiring systematic solution

**Orchestration Process:**
1. **Mystery Stage**: Service delivery analysis, stakeholder need identification, solution space exploration
2. **Heuristic Stage**: Service framework development, delivery model validation, stakeholder acceptance testing
3. **Algorithm Stage**: Service prototype implementation, delivery optimization, stakeholder feedback integration
4. **Communication**: Implementation briefing with scaling strategy

**Expected Outcomes**: Validated service prototype with stakeholder acceptance and delivery optimization

## Quality Assurance Framework

### Knowledge Funnel Compliance:
- Verify appropriate stage classification and methodology
- Validate stage transition criteria and evidence
- Confirm resource allocation matches uncertainty level
- Ensure systematic documentation and learning capture

### Multi-Agent Coordination Quality:
- Cross-validate agent outputs and recommendations
- Verify integration quality across different analytical approaches
- Confirm stakeholder communication accuracy and completeness
- Assess coordination efficiency and agent utilization

### Prototype Development Quality:
- Validate prototype performance against success criteria
- Confirm technical feasibility and market validation
- Assess development efficiency and resource utilization
- Verify stakeholder satisfaction with development process

## Continuous Improvement Process

### Performance Tracking:
- Monitor prototype success rates vs predictions
- Track Knowledge Funnel stage transition accuracy
- Measure resource allocation efficiency by stage
- Assess stakeholder satisfaction with development process

### Methodology Refinement:
- Update Knowledge Funnel stage criteria based on outcomes
- Refine agent orchestration for improved efficiency
- Enhance integration with organizational development processes
- Improve communication templates and stakeholder engagement

### Learning Integration:
- Capture lessons learned from prototype development
- Update evaluation criteria based on prototype performance
- Refine progression algorithms based on success patterns
- Enhance stakeholder feedback integration into future developments