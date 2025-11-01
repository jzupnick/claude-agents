# Stage-Gate Validation Flow
*Northwestern MPD2 Methodology Integration*

## Overview
Systematic stage-gate validation workflow based on Northwestern MPD2 course methodology, integrating with existing design decision system components while following structured development process with decision gates.

## Northwestern Stage-Gate Principles

### Core Philosophy (from MPD2 Syllabus):
1. **Structured Process**: Systematic approach to reduce uncertainty progressively
2. **Gate Criteria**: Clear decision points with specific deliverables
3. **Phase Gates**: Multiple evaluation checkpoints before advancing
4. **Risk Reduction**: Early identification and mitigation of potential failures
5. **Resource Optimization**: Increase investment only as confidence grows

### Integration with Knowledge Funnel:
- **Mystery → Heuristic**: Discovery gates focused on understanding
- **Heuristic → Algorithm**: Validation gates focused on proof  
- **Algorithm Execution**: Optimization gates focused on efficiency

## Stage-Gate Structure

### Stage 0: Ideation & Initial Screening
**Objective**: Generate and filter concepts for deeper investigation

#### Activities:
- Apply opportunity identification flow
- Conduct initial feasibility screening
- Generate multiple concept variants

#### Tools Used:
```bash
# Quick feasibility check using existing validator
python tools/product_concept_validator.py --concept-file initial_concept.json

# Strategic classification  
python design-system/primitives/calculators/opportunity-score.py \
  market_rough.yaml concept_draft.yaml --format summary
```

#### Gate 0 Criteria:
- [ ] Problem clearly defined and validated
- [ ] Initial market opportunity identified (>$1M TAM)
- [ ] No obvious technical/regulatory blockers
- [ ] Strategic fit with organizational capability
- [ ] Initial stakeholder support obtained

**Deliverables:**
- Problem statement (using `project.yaml` schema)
- Initial concept definition (using `concept.yaml` schema)
- Rough market sizing
- Strategic classification (Horizon 1/2/3)

---

### Stage 1: Concept Development & Preliminary Investigation
**Objective**: Develop concept details and validate core assumptions

#### Activities:
- Detailed concept development
- User research and needs validation
- Preliminary technical investigation
- Initial competitive analysis

#### Tools Used:
```bash
# Enhanced feasibility assessment
python design-system/primitives/calculators/feasibility-score.py \
  detailed_concept.yaml --constraints initial_constraints.yaml

# Risk assessment for major assumptions
python design-system/primitives/calculators/risk-score.py \
  detailed_concept.yaml --assumptions core_assumptions.yaml
```

#### Integration Points:
- **Existing Subagent**: `validate_design_feasibility.md`
- **Existing Agent**: `product_design_strategist.md`

#### Gate 1 Criteria:
- [ ] User needs validated through research
- [ ] Technical feasibility confirmed (TRL ≥ 3)
- [ ] Market size validated (≥$10M TAM)
- [ ] Competitive positioning defined
- [ ] Core assumptions identified and confidence assessed
- [ ] Business model hypothesis articulated

**Deliverables:**
- Detailed concept specification
- User research findings
- Technical feasibility report
- Competitive analysis
- Assumption register with confidence levels
- Business model canvas

---

### Stage 2: Business Case Development
**Objective**: Build comprehensive business case and validate key assumptions

#### Activities:
- Financial modeling and projections
- Detailed market analysis
- Technology/process development planning
- Resource requirement assessment

#### Tools Used:
```bash
# Comprehensive trade-off analysis
python design-system/primitives/generators/trade-off-matrix.py \
  concept_variants.yaml evaluation_criteria.yaml \
  --output business_case_analysis.md

# NPV calculation (integrate with existing financial tools if available)
# Risk-adjusted scoring
python design-system/primitives/calculators/risk-score.py \
  business_case_concept.yaml \
  --constraints detailed_constraints.yaml \
  --assumptions validated_assumptions.yaml
```

#### Integration Points:
- **Northwestern Framework**: Apply Three Horizons investment criteria
- **Knowledge Stage**: Transition from Heuristic to Algorithm requires systematic validation

#### Gate 2 Criteria:
- [ ] Positive business case (NPV > 0, ROI > hurdle rate)
- [ ] Market acceptance validated (customer interviews, pilots)
- [ ] Technical solution proven (TRL ≥ 6)
- [ ] Resource requirements realistic and available
- [ ] Risk profile acceptable for concept type
- [ ] Regulatory/compliance pathway clear

**Deliverables:**
- Business case with financial projections
- Market validation evidence
- Technical solution documentation
- Resource allocation plan
- Risk mitigation strategy
- Regulatory compliance plan

---

### Stage 3: Development & Testing
**Objective**: Develop solution and validate through testing

#### Activities:
- Prototype/solution development
- User testing and validation
- Technical performance validation
- Market testing (pilot programs)

#### Tools Used:
```bash
# Monitor assumption validation progress
# Track against success metrics defined in earlier stages
# Apply iterative risk assessment as new data emerges
```

#### Integration Points:
- **Existing Workflows**: Connect to development processes
- **Continuous Validation**: Regular application of feasibility scoring

#### Gate 3 Criteria:
- [ ] Solution meets performance requirements
- [ ] User acceptance demonstrated
- [ ] Manufacturing/delivery capability proven
- [ ] Market pilot results positive
- [ ] Financial projections validated
- [ ] Scalability path confirmed

**Deliverables:**
- Working prototype/solution
- User testing results
- Performance validation report
- Pilot program results
- Updated financial projections
- Scale-up plan

---

### Stage 4: Market Launch Preparation
**Objective**: Prepare for full market launch

#### Activities:
- Production/delivery system setup
- Marketing and sales preparation
- Launch planning and execution
- Performance monitoring system setup

#### Gate 4 Criteria:
- [ ] Production/delivery system operational
- [ ] Marketing materials and channels ready
- [ ] Sales team trained and equipped
- [ ] Success metrics and monitoring in place
- [ ] Risk mitigation systems operational

**Deliverables:**
- Launch plan
- Production/delivery capability
- Marketing assets
- Performance monitoring dashboard

---

## Decision Framework Integration

### Knowledge Funnel Alignment:
- **Stages 0-1**: Mystery → Heuristic transition
- **Stages 1-2**: Heuristic development and refinement  
- **Stages 2-3**: Heuristic → Algorithm transition
- **Stages 3-4**: Algorithm execution and optimization

### Three Horizons Investment Logic:
- **Horizon 1**: Lower gate criteria, faster progression (proven markets/technologies)
- **Horizon 2**: Moderate gate criteria, balanced validation (adjacent opportunities)
- **Horizon 3**: Higher gate criteria, extensive validation (exploratory opportunities)

### Exploration-Exploitation Balance:
- **Early Stages (0-1)**: Heavy exploration, learning-focused
- **Middle Stages (1-2)**: Balanced approach, systematic validation
- **Late Stages (2-4)**: Exploitation focus, execution-oriented

## Gate Review Process

### Gate Review Team:
- **Decision Authority**: Senior stakeholders with budget authority
- **Technical Expertise**: Subject matter experts for validation
- **Market Expertise**: Customer-facing teams for market validation
- **Financial Expertise**: Finance team for business case validation

### Gate Review Methodology:
1. **Pre-Review Package**: All deliverables distributed 48 hours in advance
2. **Structured Review**: Systematic evaluation against criteria
3. **Decision Options**:
   - **GO**: Proceed to next stage with allocated resources
   - **CONDITIONAL GO**: Proceed with specific conditions/modifications  
   - **RECYCLE**: Return to current stage with specific improvements
   - **HOLD**: Pause pending external factors
   - **KILL**: Terminate project

### Decision Documentation:
- Decision rationale and voting record
- Conditions/modifications if conditional go
- Resource allocation for next stage
- Success metrics and review timeline

## Integration with Existing Components

### Leverages Existing Tools:
- `product_concept_validator.py` - Baseline feasibility scoring
- `design_review_checklist.sh` - Quality gate validation
- All new calculators and generators

### Leverages Existing Agents/Subagents:
- `product_design_strategist.md` - Strategic methodology guidance
- `validate_design_feasibility.md` - Technical/market feasibility
- `lean_design_specialist.md` - Rapid validation approaches

### Enhances Existing Workflows:
- `problem_framing_workflow.md` - Feeds into Stage 0
- Connects to development workflows - Stages 3-4

## Northwestern MPD2 Enhancements

### Structured Process Benefits:
- Reduced development risk through systematic validation
- Clear decision points with specific criteria
- Progressive resource commitment aligned with confidence
- Early identification of fatal flaws

### Academic Rigor Applied:
- Systematic evaluation methodology
- Clear documentation requirements
- Structured decision-making process
- Learning capture and process improvement

## Success Metrics

### Process Metrics:
- Gate passage rates by stage
- Time spent in each stage
- Quality of gate deliverables
- Decision accuracy (vs later outcomes)

### Outcome Metrics:
- Project success rate (meet objectives)
- Time to market vs estimates
- Budget vs actual costs
- Post-launch performance vs projections

## Example Usage

```bash
# Stage 0: Initial screening
python design-system/primitives/calculators/opportunity-score.py \
  initial_market.yaml rough_concept.yaml --format summary

# Stage 1: Detailed assessment
python design-system/primitives/calculators/feasibility-score.py \
  detailed_concept.yaml --constraints stage1_constraints.yaml

# Stage 2: Business case validation
python design-system/primitives/generators/trade-off-matrix.py \
  concept_options.yaml business_criteria.yaml

# Stage 3: Development monitoring
# Apply iterative assessment as development progresses

# Stage 4: Launch readiness
# Final validation before market launch
```

## Adaptation Guidelines

### For Different Project Types:
- **Horizon 1 Projects**: Accelerated gates, proven criteria
- **Horizon 2 Projects**: Standard process with market validation emphasis
- **Horizon 3 Projects**: Extended early stages, higher validation requirements

### For Different Industries:
- **Software**: Emphasis on user validation, agile integration
- **Hardware**: Emphasis on technical validation, manufacturing readiness
- **Services**: Emphasis on delivery capability, service design validation

## Common Pitfalls & Northwestern Solutions

**Pitfall**: Rushing through early gates due to excitement
**Solution**: Enforce gate criteria discipline, require objective validation

**Pitfall**: Over-engineering gate process (analysis paralysis)
**Solution**: Time-box gate reviews, focus on critical assumptions

**Pitfall**: Treating all projects the same regardless of uncertainty
**Solution**: Apply Three Horizons logic, adjust criteria by project type

**Pitfall**: Poor gate decision documentation
**Solution**: Structured decision templates, clear rationale requirements