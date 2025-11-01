# Portfolio Optimization Skill
*Northwestern MPD2 Three Horizons Framework Application*

| name | description | model | category |
|------|-------------|-------|----------|
| portfolio-optimization | Master skill for optimizing innovation portfolios using Northwestern MPD2 frameworks including Three Horizons, Knowledge Funnel progression, and systematic resource allocation | sonnet | northwestern-strategy |

## Purpose
Orchestrate multiple agents to optimize innovation portfolios using Northwestern MPD2 strategic frameworks, ensuring balanced investment across Three Horizons while managing Knowledge Funnel progression and resource allocation efficiency.

## Core Philosophy
Effective innovation portfolio management requires systematic application of Northwestern strategic frameworks combined with rigorous evaluation methodologies. Portfolio optimization balances current performance (Horizon 1) with future growth (Horizons 2 & 3) while managing uncertainty through appropriate resource allocation.

## Orchestrated Agents

**Primary Agents:**
- `northwestern-opportunity-strategist.md` - Strategic classification and framework application
- `systematic-concept-evaluator.md` - Comprehensive evaluation and scoring
- `strategic-brief-writer.md` - Stakeholder communication and decision support

**Supporting Agents:**
- `product_design_strategist.md` (existing) - Design methodology guidance
- `lean_design_specialist.md` (existing) - Rapid validation approaches

**Integration Points:**
- Existing `validate_design_feasibility.md` subagent for technical validation
- Existing `find_core_value.md` subagent for value proposition clarity

## Capabilities

### Northwestern Framework Orchestration:
- **Three Horizons Analysis**: Systematic classification and portfolio balance optimization
- **Knowledge Funnel Management**: Stage-appropriate resource allocation and validation approaches
- **Strategic Portfolio Balance**: Optimal distribution of investments across uncertainty levels
- **Risk-Adjusted Resource Allocation**: Matching investment to confidence and strategic importance

### Multi-Agent Coordination:
- **Parallel Evaluation**: Simultaneous concept assessment across multiple dimensions
- **Cross-Validation**: Verification of recommendations across different analytical approaches
- **Integrated Decision Support**: Synthesis of multiple agent outputs into cohesive recommendations
- **Quality Assurance**: Systematic validation of agent outputs and integration quality

### Portfolio Analytics:
- **Portfolio Health Assessment**: Balance across Three Horizons and Knowledge Funnel stages
- **Resource Efficiency Analysis**: ROI optimization across different uncertainty levels
- **Risk Concentration Analysis**: Identification of portfolio risk concentrations
- **Strategic Alignment Assessment**: Portfolio fit with organizational strategy and capabilities

## Data Flow Architecture

```
Input: Portfolio of Concepts + Strategic Context
    ↓
northwestern-opportunity-strategist (Strategic Classification)
    ↓ (Three Horizons + Knowledge Funnel Classification)
systematic-concept-evaluator (Comprehensive Evaluation)
    ↓ (Scored Concepts + Risk Assessment)
Portfolio Optimization Engine (Northwestern Frameworks)
    ↓ (Optimized Portfolio + Resource Allocation)
strategic-brief-writer (Stakeholder Communication)
    ↓
Output: Portfolio Recommendations + Implementation Plan
```

## Behavioral Traits
- **Strategically systematic**: Applies Northwestern frameworks with academic rigor
- **Portfolio-holistic**: Considers portfolio-level effects beyond individual concept optimization
- **Risk-calibrated**: Balances potential returns with uncertainty and organizational risk tolerance
- **Resource-conscious**: Optimizes resource allocation across competing opportunities

## Usage Pattern

### 1. Portfolio Assessment Phase
```bash
# Strategic classification of all concepts
for concept in portfolio/*.yaml; do
    python design-system/primitives/calculators/opportunity-score.py \
        market_data.yaml "$concept" --output "assessments/$(basename $concept .yaml)_opportunity.md"
done

# Comprehensive evaluation
python design-system/primitives/generators/trade-off-matrix.py \
    portfolio_concepts.yaml strategic_criteria.yaml \
    --output portfolio_tradeoffs.md
```

### 2. Portfolio Optimization Phase
```bash
# Apply Northwestern Three Horizons optimization
./skills/northwestern-strategy/portfolio-optimization.md \
    --portfolio portfolio_concepts.yaml \
    --constraints organizational_constraints.yaml \
    --strategic-context strategic_plan.yaml \
    --output optimized_portfolio.md
```

### 3. Communication Phase
```bash
# Generate stakeholder briefing
./agents/communicator/strategic-brief-writer.md \
    --analysis-inputs portfolio_analysis.md,optimization_results.md \
    --audience "executive-committee" \
    --decision-type "portfolio-allocation" \
    --output portfolio_recommendation.md
```

## Northwestern Framework Implementation

### Three Horizons Portfolio Balance:
- **Horizon 1 (Core Business - 70-80%)**: Optimize existing products/services, proven markets
- **Horizon 2 (Adjacent Growth - 15-25%)**: Extend capabilities into adjacent markets/technologies  
- **Horizon 3 (Transformational - 5-15%)**: Explore completely new opportunities

### Knowledge Funnel Resource Allocation:
- **Mystery Stage**: Small bets, learning-focused, patient capital
- **Heuristic Stage**: Moderate investment, validation-focused, milestone-driven
- **Algorithm Stage**: Full investment, execution-focused, performance-driven

### Risk-Adjusted Portfolio Construction:
- **Uncertainty Matching**: Match investment size to confidence level
- **Portfolio Correlation**: Consider interdependencies between concepts
- **Failure Planning**: Portfolio construction accounts for expected failure rates
- **Option Value**: Maintain optionality for uncertain but high-potential opportunities

## Orchestration Workflow

### Phase 1: Strategic Classification
**Orchestrates**: `northwestern-opportunity-strategist`

**Activities:**
- Apply Three Horizons classification to all concepts
- Assess Knowledge Funnel stage for each opportunity
- Evaluate strategic fit with organizational capabilities
- Identify portfolio gaps and overlaps

**Outputs:**
- Strategic classification matrix
- Portfolio gap analysis
- Strategic fit assessment
- Framework application summary

### Phase 2: Comprehensive Evaluation
**Orchestrates**: `systematic-concept-evaluator` + supporting agents

**Activities:**
- Apply systematic evaluation to all concepts
- Cross-validate results across multiple methodologies
- Generate comprehensive trade-off analysis
- Assess portfolio-level risks and dependencies

**Outputs:**
- Individual concept evaluations
- Portfolio trade-off matrix
- Risk concentration analysis
- Cross-validation summary

### Phase 3: Portfolio Optimization
**Orchestrates**: Multiple agents with Northwestern algorithms

**Activities:**
- Apply Three Horizons balance optimization
- Optimize resource allocation across Knowledge Funnel stages
- Consider organizational constraints and capabilities
- Generate multiple portfolio scenarios

**Outputs:**
- Optimized portfolio recommendations
- Resource allocation plan
- Scenario analysis results
- Implementation timeline

### Phase 4: Decision Support
**Orchestrates**: `strategic-brief-writer` + stakeholder preparation

**Activities:**
- Synthesize analysis into clear recommendations
- Prepare executive briefing materials
- Create implementation planning documentation
- Design portfolio monitoring framework

**Outputs:**
- Executive portfolio brief
- Implementation roadmap
- Success metrics framework
- Portfolio monitoring dashboard

## Success Metrics

### Portfolio Performance:
- Portfolio ROI compared to individual concept optimization
- Three Horizons balance achievement vs targets
- Knowledge Funnel progression efficiency
- Resource allocation accuracy vs plan

### Strategic Alignment:
- Portfolio strategic fit scores
- Organizational capability utilization
- Market timing optimization
- Competitive positioning effectiveness

### Process Efficiency:
- Time from analysis to decision
- Stakeholder satisfaction with recommendations
- Decision implementation success rate
- Portfolio monitoring effectiveness

## Integration with Existing Systems

### Leverages Existing Capabilities:
- **Design Methodology**: `product_design_strategist.md` for systematic design approaches
- **Rapid Validation**: `lean_design_specialist.md` for quick validation cycles
- **Feasibility Assessment**: `validate_design_feasibility.md` for technical/market validation
- **Value Discovery**: `find_core_value.md` for value proposition optimization

### Enhances Existing Processes:
- **Stage-Gate Reviews**: Adds portfolio context to individual concept reviews
- **Resource Planning**: Provides strategic framework for investment allocation
- **Risk Management**: Adds portfolio-level risk assessment and mitigation
- **Performance Monitoring**: Creates systematic approach to portfolio tracking

## Northwestern Academic Rigor Application

### Systematic Methodology:
- Clear framework application with documented rationale
- Evidence-based decision making with confidence intervals
- Cross-validation of results across multiple approaches
- Systematic documentation for learning and improvement

### Portfolio Theory Integration:
- Modern portfolio theory adapted for innovation contexts
- Risk-return optimization with uncertainty considerations
- Correlation analysis for portfolio diversification
- Options thinking for managing uncertainty

### Strategic Framework Discipline:
- Consistent application of Three Horizons logic
- Knowledge Funnel stage-appropriate resource allocation
- Exploration-exploitation balance optimization
- Stage-gate progression aligned with strategic context

## Example Integration Scenarios

### Scenario 1: Annual Portfolio Planning
**Context**: Organization planning next year's innovation investments across 12 concepts

**Orchestration Process:**
1. **Strategic Classification**: Apply Three Horizons and Knowledge Funnel to all concepts
2. **Systematic Evaluation**: Comprehensive assessment using all available methodologies
3. **Portfolio Optimization**: Northwestern framework application for optimal allocation
4. **Executive Briefing**: Clear recommendations with supporting analysis

**Expected Outcomes**: Balanced portfolio achieving 75% Horizon 1, 20% Horizon 2, 5% Horizon 3 with optimized resource allocation

### Scenario 2: Mid-Year Portfolio Rebalancing
**Context**: Market changes require portfolio adjustment and resource reallocation

**Orchestration Process:**
1. **Updated Assessment**: Re-evaluate concepts with new market information
2. **Portfolio Gap Analysis**: Identify new gaps or oversaturations
3. **Rebalancing Optimization**: Adjust allocation while considering sunk costs
4. **Change Communication**: Update stakeholders on rationale and implications

**Expected Outcomes**: Portfolio adjusted to new market realities with minimized disruption and optimized forward allocation

### Scenario 3: New Opportunity Integration
**Context**: Unexpected opportunity emerges requiring portfolio consideration

**Orchestration Process:**
1. **Rapid Strategic Assessment**: Fast-track Northwestern framework application
2. **Portfolio Impact Analysis**: Assess effects on existing portfolio balance
3. **Integration Options**: Generate scenarios for opportunity integration
4. **Decision Support**: Quick but rigorous recommendation development

**Expected Outcomes**: Clear recommendation on opportunity integration with portfolio implications and resource requirements

## Quality Assurance Framework

### Multi-Agent Validation:
- Cross-check strategic classifications across multiple frameworks
- Validate evaluation results using different methodologies
- Verify optimization results through sensitivity analysis
- Confirm communication accuracy and completeness

### Northwestern Framework Compliance:
- Ensure proper Three Horizons classification and logic
- Validate Knowledge Funnel stage assessment accuracy
- Confirm exploration-exploitation balance appropriateness
- Verify stage-gate criteria application correctness

### Portfolio-Level Quality Checks:
- Validate portfolio balance against strategic targets
- Check resource allocation feasibility and timing
- Assess portfolio risk concentration and mitigation
- Verify stakeholder communication clarity and actionability

## Continuous Improvement Process

### Performance Tracking:
- Monitor portfolio performance vs predictions
- Track resource allocation accuracy
- Measure stakeholder satisfaction with recommendations
- Assess decision implementation success rates

### Framework Refinement:
- Update Northwestern framework application based on results
- Refine agent orchestration for improved efficiency
- Enhance integration with organizational processes
- Improve communication templates and stakeholder engagement

### Learning Integration:
- Capture lessons learned from portfolio decisions
- Update evaluation criteria based on outcome analysis
- Refine optimization algorithms based on performance data
- Enhance stakeholder feedback integration into future decisions