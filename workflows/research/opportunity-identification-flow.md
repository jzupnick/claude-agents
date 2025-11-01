# Opportunity Identification Flow
*Enhanced with Northwestern MPD2 & Roger Martin Frameworks*

## Overview
Systematic workflow for identifying and qualifying product/design opportunities using Northwestern MPD2 methodologies including Knowledge Funnel progression, Three Horizons framework, and structured opportunity assessment.

## Prerequisites
- Project scope and constraints defined
- Stakeholder alignment on objectives
- Access to market research resources

## Workflow Steps

### Phase 1: Mystery Exploration
**Objective**: Discover unknown opportunities through systematic observation and research

#### Step 1.1: Environmental Scanning
```bash
# Use existing tools to gather baseline data
python /Users/justinzupnick/Documents/claude-agents/design-system/primitives/generators/morphological-chart.py \
  --dimensions market_segments,user_needs,solution_approaches \
  --output environmental_scan.md
```

**Activities:**
- Conduct market trend analysis
- Interview lead users and edge cases  
- Analyze competitive white spaces
- Study adjacent industries for inspiration

**Deliverables:**
- Environmental scan report
- Lead user insights
- Trend analysis summary

#### Step 1.2: Problem Discovery
**Integration Point**: Use existing `problem_framing_workflow.md` 

**Activities:**
- Apply observational research methods
- Document "mysteries" - unexplained user behaviors
- Identify jobs-to-be-done not well served
- Map user journey pain points

**Deliverables:**
- Problem opportunity briefs
- User journey maps with pain points
- Jobs-to-be-done analysis

### Phase 2: Heuristic Development
**Objective**: Convert mysteries into structured opportunities with decision frameworks

#### Step 2.1: Opportunity Framing
```bash
# Apply Northwestern opportunity scoring
python /Users/justinzupnick/Documents/claude-agents/design-system/primitives/calculators/opportunity-score.py \
  market_data.yaml concept_draft.yaml \
  --output opportunity_assessment.md
```

**Activities:**
- Define opportunity scope and boundaries
- Apply Three Horizons classification
- Assess knowledge stage (Mystery/Heuristic/Algorithm)
- Determine exploration vs exploitation balance

**Deliverables:**
- Opportunity framing documents (using `project.yaml` schema)
- Three Horizons classification
- Knowledge stage assessment

#### Step 2.2: Market Validation Research
**Activities:**
- Size total addressable market (TAM/SAM/SOM)
- Analyze competitive landscape depth
- Conduct user need validation interviews
- Test willingness-to-pay assumptions

**Tools Integration:**
- Use existing `validate_design_feasibility.md` subagent
- Apply `product_concept_validator.py` for initial assessment

**Deliverables:**
- Market sizing analysis
- Competitive positioning map
- User validation findings

### Phase 3: Algorithm Crystallization  
**Objective**: Develop systematic approach for evaluating and prioritizing opportunities

#### Step 3.1: Opportunity Scoring
```bash
# Generate comprehensive trade-off analysis
python /Users/justinzupnick/Documents/claude-agents/design-system/primitives/generators/trade-off-matrix.py \
  opportunities.yaml criteria.yaml \
  --output opportunity_tradeoffs.md
```

**Activities:**
- Apply weighted scoring criteria (using `criteria.yaml` schema)
- Run trade-off analysis across dimensions
- Calculate risk-adjusted opportunity scores
- Perform sensitivity analysis on key assumptions

**Deliverables:**
- Scored opportunity matrix
- Trade-off analysis report  
- Risk-adjusted rankings

#### Step 3.2: Strategic Recommendation
**Activities:**
- Synthesize findings across all phases
- Apply Northwestern decision frameworks
- Generate strategic recommendations
- Define next phase requirements

**Deliverables:**
- Strategic opportunity brief
- Go/No-Go recommendation with rationale
- Next phase planning (if proceeding)

## Decision Gates

### Gate 1: Mystery → Heuristic
**Criteria:**
- Sufficient problem definition clarity
- User need validation achieved
- Market opportunity sized
- Initial feasibility confirmed

**Required Artifacts:**
- Problem framing document
- User research summary
- Market sizing analysis
- Initial concept sketches

### Gate 2: Heuristic → Algorithm  
**Criteria:**
- Systematic evaluation framework established
- Multiple opportunities scored and ranked
- Risk assessment completed
- Resource requirements estimated

**Required Artifacts:**
- Trade-off matrix analysis
- Risk assessment report
- Resource requirement estimates
- Strategic recommendation

## Integration with Existing Components

### Leverages Existing Agents:
- `product_design_strategist.md` - For systematic methodology application
- `lean_design_specialist.md` - For rapid validation approaches

### Leverages Existing Subagents:
- `validate_design_feasibility.md` - For technical/market feasibility
- `find_core_value.md` - For value proposition clarification

### Leverages Existing Tools:
- `product_concept_validator.py` - For structured concept assessment
- `design_review_checklist.sh` - For quality gates

## Northwestern MPD2 Enhancements

### Knowledge Funnel Application:
- **Mystery Stage**: Focus on observation, discovery, exploration
- **Heuristic Stage**: Develop frameworks, test patterns, build understanding  
- **Algorithm Stage**: Systematic execution, optimization, scaling

### Three Horizons Framework:
- **Horizon 1**: Core business optimization opportunities
- **Horizon 2**: Adjacent market/capability extension  
- **Horizon 3**: Transformational/exploratory opportunities

### Exploration vs Exploitation Balance:
- High uncertainty → Heavy exploration focus
- Medium uncertainty → Balanced approach
- Low uncertainty → Exploitation focus

## Success Metrics

### Process Metrics:
- Number of high-quality opportunities identified
- Conversion rate from mystery to validated opportunity
- Time from identification to decision

### Outcome Metrics:
- Percentage of pursued opportunities that meet success criteria
- Accuracy of opportunity scoring vs actual outcomes
- Resource efficiency in opportunity development

## Common Pitfalls & Mitigations

**Pitfall**: Jumping to solutions too quickly (skipping mystery stage)
**Mitigation**: Enforce gate criteria, require user research validation

**Pitfall**: Analysis paralysis in heuristic stage
**Mitigation**: Time-box research phases, use minimum viable insights

**Pitfall**: Over-optimistic opportunity scoring
**Mitigation**: Apply risk adjustment factors, use confidence intervals

## Example Usage

```bash
# 1. Start environmental scanning
./workflows/research/opportunity-identification-flow.md --phase=mystery

# 2. Apply Northwestern frameworks  
python design-system/primitives/calculators/opportunity-score.py \
  market_trends.yaml initial_concepts.yaml

# 3. Generate trade-off analysis
python design-system/primitives/generators/trade-off-matrix.py \
  validated_opportunities.yaml scoring_criteria.yaml

# 4. Make strategic decision
# Review all artifacts and apply gate criteria
```

## Related Workflows
- `problem_framing_workflow.md` (existing)
- `concept-scoring-flow.md` (Layer 2)
- `market-sizing-flow.md` (Layer 2)