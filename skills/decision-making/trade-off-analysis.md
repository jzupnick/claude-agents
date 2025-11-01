# Trade-off Analysis Skill
*Northwestern MPD2 Systematic Decision Support*

| name | description | model | category |
|------|-------------|-------|----------|
| trade-off-analysis | Master skill for systematic trade-off analysis and decision support using Northwestern MPD2 methodologies with multi-agent orchestration for complex decision scenarios | sonnet | decision-making |

## Purpose
Orchestrate multiple agents to provide comprehensive trade-off analysis for complex design and business decisions, ensuring systematic evaluation across multiple dimensions while maintaining Northwestern academic rigor and practical applicability.

## Core Philosophy
Effective decision-making requires systematic evaluation of trade-offs across multiple dimensions with appropriate weighting based on strategic context. Northwestern MPD2 emphasizes evidence-based decision making with clear documentation of rationale and assumptions. Success depends on balancing analytical rigor with practical decision support.

## Orchestrated Agents

**Primary Agents:**
- `systematic-concept-evaluator.md` - Multi-dimensional evaluation and scoring
- `northwestern-opportunity-strategist.md` - Strategic context and framework application
- `strategic-brief-writer.md` - Decision package preparation and stakeholder communication

**Supporting Agents:**
- `product_design_strategist.md` (existing) - Design methodology perspective
- `lean_design_specialist.md` (existing) - Rapid validation insights

**Integration Points:**
- Existing `validate_design_feasibility.md` subagent for technical trade-offs
- Existing `find_core_value.md` subagent for value proposition analysis

## Capabilities

### Systematic Trade-off Analysis:
- **Multi-Dimensional Evaluation**: Assessment across technical, market, financial, and strategic dimensions
- **Weighted Scoring**: Context-appropriate weighting based on strategic priorities
- **Sensitivity Analysis**: Understanding decision robustness under different assumptions
- **Risk-Adjusted Assessment**: Trade-off evaluation considering uncertainty levels

### Northwestern Framework Application:
- **Knowledge Funnel Context**: Trade-off criteria appropriate to uncertainty level
- **Three Horizons Weighting**: Strategic context influences evaluation criteria
- **Stage-Gate Integration**: Decision support aligned with development stage
- **Exploration-Exploitation Balance**: Trade-offs between learning and execution

### Decision Support:
- **Clear Recommendations**: Systematic ranking with detailed rationale
- **Confidence Intervals**: Uncertainty assessment for each trade-off dimension
- **Assumption Tracking**: Critical assumptions underlying trade-off analysis
- **Scenario Planning**: Trade-off implications under different future scenarios

## Data Flow Architecture

```
Input: Decision Options + Evaluation Criteria + Strategic Context
    ↓
northwestern-opportunity-strategist (Strategic Framework Application)
    ↓ (Strategic Context + Weighting Guidance)
systematic-concept-evaluator (Multi-Dimensional Analysis)
    ↓ (Scored Options + Trade-off Matrix)
Trade-off Analysis Engine (Northwestern Methodology)
    ↓ (Systematic Trade-off Assessment + Sensitivity Analysis)
strategic-brief-writer (Decision Package)
    ↓
Output: Decision Recommendation + Supporting Analysis
```

## Behavioral Traits
- **Systematically comprehensive**: Evaluates all relevant dimensions with appropriate depth
- **Evidence-based**: Grounds all trade-off assessments in available data and analysis
- **Context-sensitive**: Adapts evaluation criteria to strategic and developmental context
- **Decision-oriented**: Provides clear recommendations with actionable next steps

## Usage Pattern

### 1. Trade-off Setup Phase
```bash
# Strategic context assessment for weighting
python design-system/primitives/calculators/opportunity-score.py \
    strategic_context.yaml decision_options.yaml \
    --output strategic_weighting.md

# Multi-dimensional evaluation setup
python design-system/primitives/generators/trade-off-matrix.py \
    decision_options.yaml evaluation_criteria.yaml \
    --setup-phase --output evaluation_framework.md
```

### 2. Comprehensive Analysis Phase
```bash
# Systematic evaluation across all options
python design-system/primitives/calculators/feasibility-score.py \
    option1.yaml option2.yaml option3.yaml \
    --constraints decision_constraints.yaml \
    --output comparative_feasibility.md

# Risk assessment for each option
python design-system/primitives/calculators/risk-score.py \
    decision_options.yaml --comparative-mode \
    --output risk_comparison.md
```

### 3. Decision Support Phase
```bash
# Complete trade-off analysis with recommendations
./skills/decision-making/trade-off-analysis.md \
    --options decision_options.yaml \
    --criteria evaluation_criteria.yaml \
    --context strategic_context.yaml \
    --output decision_package.md
```

## Northwestern Framework Implementation

### Knowledge Funnel-Appropriate Analysis:

**Mystery Stage Decisions:**
- Emphasize learning potential and option value
- Weight exploration capability heavily
- Accept higher uncertainty in projections
- Focus on assumption identification and validation

**Heuristic Stage Decisions:**
- Balance learning with performance criteria
- Apply systematic evaluation frameworks
- Moderate confidence in projections
- Focus on pattern validation and framework building

**Algorithm Stage Decisions:**
- Emphasize execution efficiency and performance
- Apply proven evaluation methodologies
- High confidence in analytical projections
- Focus on optimization and scaling potential

### Three Horizons Decision Weighting:

**Horizon 1 Decisions (Core Business):**
- Weight proven performance heavily
- Emphasize efficiency and optimization
- Apply conservative risk assessment
- Focus on immediate ROI and execution

**Horizon 2 Decisions (Adjacent Growth):**
- Balance proven capability with growth potential
- Moderate risk tolerance
- Apply systematic validation requirements
- Focus on strategic positioning and market expansion

**Horizon 3 Decisions (Transformational):**
- Weight transformational potential heavily
- Accept higher risk and uncertainty
- Apply exploration-focused evaluation
- Focus on long-term option value and learning

## Orchestration Workflow

### Phase 1: Strategic Context Assessment
**Orchestrates**: `northwestern-opportunity-strategist`

**Activities:**
- Apply Northwestern frameworks to establish decision context
- Classify decision type using Knowledge Funnel and Three Horizons
- Establish appropriate evaluation criteria and weighting
- Identify critical assumptions and uncertainty factors

**Outputs:**
- Strategic context classification
- Evaluation criteria with weights
- Critical assumption register
- Uncertainty assessment framework

### Phase 2: Multi-Dimensional Evaluation
**Orchestrates**: `systematic-concept-evaluator` + supporting agents

**Activities:**
- Apply comprehensive evaluation across all dimensions
- Generate trade-off matrix with quantitative and qualitative assessments
- Conduct sensitivity analysis on key variables
- Cross-validate results across multiple methodologies

**Outputs:**
- Complete trade-off matrix
- Sensitivity analysis results
- Cross-validation summary
- Uncertainty confidence intervals

### Phase 3: Decision Analysis
**Orchestrates**: Multiple agents with Northwestern decision methodology

**Activities:**
- Apply weighted scoring based on strategic context
- Generate scenario analysis under different assumptions
- Assess decision robustness and sensitivity
- Identify critical decision factors and break-even points

**Outputs:**
- Weighted decision matrix
- Scenario analysis results
- Sensitivity assessment
- Critical factor identification

### Phase 4: Decision Package Preparation
**Orchestrates**: `strategic-brief-writer`

**Activities:**
- Synthesize analysis into clear decision recommendation
- Prepare comprehensive decision package for stakeholders
- Document rationale and supporting evidence
- Provide implementation guidance and next steps

**Outputs:**
- Decision recommendation with rationale
- Executive decision package
- Implementation planning guidance
- Monitoring and review framework

## Success Metrics

### Decision Quality:
- Decision outcome correlation with predicted trade-offs
- Stakeholder satisfaction with decision process and outcomes
- Decision implementation success rate
- Post-decision performance vs projections

### Analysis Quality:
- Trade-off assessment accuracy vs actual outcomes
- Sensitivity analysis predictive value
- Assumption validation accuracy
- Cross-validation consistency

### Process Efficiency:
- Time from decision request to recommendation
- Stakeholder confidence in decision process
- Analysis thoroughness vs decision complexity
- Resource utilization efficiency

## Integration with Existing Systems

### Leverages Existing Capabilities:
- **Design Methodology**: `product_design_strategist.md` for design-focused trade-offs
- **Rapid Validation**: `lean_design_specialist.md` for quick validation of trade-off assumptions
- **Feasibility Assessment**: `validate_design_feasibility.md` for technical trade-off analysis
- **Value Discovery**: `find_core_value.md` for value proposition trade-offs

### Enhances Existing Processes:
- **Strategic Planning**: Adds systematic trade-off methodology to planning processes
- **Resource Allocation**: Provides evidence-based framework for investment decisions
- **Risk Management**: Integrates trade-off thinking into risk assessment
- **Performance Review**: Creates systematic framework for retrospective analysis

## Northwestern Academic Rigor Application

### Systematic Methodology:
- Clear evaluation criteria with documented rationale
- Multi-dimensional assessment with appropriate weighting
- Sensitivity analysis and scenario planning
- Systematic documentation enabling audit and learning

### Evidence-Based Decision Making:
- Quantitative analysis where data is available
- Qualitative assessment with clear evaluation criteria
- Cross-validation across multiple methodologies
- Confidence interval assessment and uncertainty management

### Strategic Framework Integration:
- Knowledge Funnel stage-appropriate evaluation criteria
- Three Horizons context influencing trade-off weighting
- Exploration-exploitation balance in decision recommendations
- Stage-gate integration with development process

## Example Integration Scenarios

### Scenario 1: Product Feature Prioritization
**Context**: Development team must choose between 3 major features for next release

**Orchestration Process:**
1. **Strategic Assessment**: Northwestern framework application (likely Horizon 1), Knowledge Funnel stage assessment
2. **Multi-Dimensional Evaluation**: Technical complexity, user value, market impact, resource requirements
3. **Trade-off Analysis**: Weighted scoring with sensitivity analysis, scenario planning
4. **Decision Package**: Clear recommendation with implementation timeline and success metrics

**Expected Outcomes**: Evidence-based feature priority with clear rationale and implementation plan

### Scenario 2: Technology Platform Decision
**Context**: Organization must choose between building custom vs buying existing platform

**Orchestration Process:**
1. **Strategic Classification**: Three Horizons positioning, Knowledge Funnel stage assessment
2. **Comprehensive Analysis**: Build vs buy trade-offs across technical, financial, strategic dimensions
3. **Risk-Adjusted Assessment**: Uncertainty analysis, scenario planning, option value calculation
4. **Executive Briefing**: Decision recommendation with risk mitigation and implementation planning

**Expected Outcomes**: Strategic platform decision with comprehensive risk assessment and implementation roadmap

### Scenario 3: Market Entry Strategy
**Context**: Company evaluating different approaches to enter new market segment

**Orchestration Process:**
1. **Strategic Context**: Northwestern methodology for market entry evaluation
2. **Market Analysis**: Entry strategy trade-offs across speed, investment, risk, competitive positioning
3. **Scenario Planning**: Market evolution scenarios and strategy robustness assessment
4. **Strategic Briefing**: Market entry recommendation with phased approach and success metrics

**Expected Outcomes**: Market entry strategy with clear trade-off rationale and execution planning

## Quality Assurance Framework

### Northwestern Framework Compliance:
- Verify appropriate Knowledge Funnel and Three Horizons application
- Validate evaluation criteria alignment with strategic context
- Confirm trade-off weighting reflects organizational priorities
- Ensure systematic methodology application consistency

### Trade-off Analysis Quality:
- Cross-validate quantitative assessments with qualitative insights
- Verify sensitivity analysis completeness and relevance
- Confirm scenario planning covers relevant uncertainty ranges
- Assess recommendation robustness under different assumptions

### Decision Support Quality:
- Validate decision package clarity and actionability
- Confirm stakeholder communication appropriateness
- Assess implementation guidance completeness
- Verify monitoring framework adequacy

## Continuous Improvement Process

### Performance Tracking:
- Monitor decision outcome correlation with trade-off predictions
- Track stakeholder satisfaction with decision process
- Measure implementation success rates
- Assess trade-off analysis accuracy over time

### Methodology Refinement:
- Update evaluation criteria based on decision outcomes
- Refine weighting methodologies for different decision contexts
- Enhance sensitivity analysis techniques
- Improve stakeholder communication approaches

### Learning Integration:
- Capture lessons learned from trade-off decisions
- Update decision frameworks based on outcome analysis
- Refine Northwestern methodology application
- Enhance cross-agent coordination for improved analysis quality