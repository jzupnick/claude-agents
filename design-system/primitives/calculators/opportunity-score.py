#!/usr/bin/env python3
"""
Northwestern MPD2 Opportunity Score Calculator

Based on Roger Martin's frameworks from "The Design of Business" and Northwestern
MPD2 methodologies including:
- Knowledge Funnel (Mystery → Heuristic → Algorithm)
- Three Horizons opportunity framework
- Exploration vs Exploitation balance
- Tournament structure for opportunity identification

Input: market data + concept + competitive landscape
Output: opportunity score, horizon classification, knowledge stage assessment
"""

import yaml
import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np

@dataclass
class OpportunityAssessment:
    """Complete opportunity assessment with Northwestern MPD2 frameworks"""
    overall_score: float
    horizon_classification: str
    knowledge_stage: str
    market_size_score: float
    growth_rate_score: float
    competitive_intensity_score: float
    addressable_segment_score: float
    certainty_level: str
    exploration_exploitation_balance: str
    recommended_approach: str
    risk_adjusted_score: float
    confidence_interval: Tuple[float, float]
    key_insights: List[str]
    next_steps: List[str]

def load_yaml_file(file_path: Path) -> Dict:
    """Load YAML file with error handling"""
    try:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Warning: {file_path} not found, using empty data")
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing {file_path}: {e}")
        return {}

def classify_knowledge_stage(concept: Dict, market_data: Dict) -> str:
    """
    Classify opportunity using Roger Martin's Knowledge Funnel:
    Mystery → Heuristic → Algorithm
    """
    
    # Assess level of understanding and structure
    understanding_indicators = 0
    total_indicators = 0
    
    # Market understanding
    if market_data.get('market_size') and market_data.get('growth_rate'):
        understanding_indicators += 1
    total_indicators += 1
    
    # User understanding
    value_prop = concept.get('core_value_proposition', {})
    if all(value_prop.get(key) for key in ['target_user_segment', 'job_to_be_done']):
        understanding_indicators += 1
    total_indicators += 1
    
    # Competitive understanding
    competition = concept.get('positioning', {}).get('competitive_landscape', {})
    if competition.get('direct_competitors') and competition.get('competitive_advantages'):
        understanding_indicators += 1
    total_indicators += 1
    
    # Technical understanding
    technical = concept.get('technical', {})
    if technical.get('technology_readiness_level', 0) >= 6:
        understanding_indicators += 1
    total_indicators += 1
    
    # Business model understanding
    business_model = concept.get('business_model', {})
    if business_model.get('revenue_streams') and business_model.get('cost_structure'):
        understanding_indicators += 1
    total_indicators += 1
    
    understanding_ratio = understanding_indicators / total_indicators
    
    if understanding_ratio >= 0.8:
        return "Algorithm"  # Well-understood, can be systematized
    elif understanding_ratio >= 0.4:
        return "Heuristic"  # Partially understood, rules of thumb available
    else:
        return "Mystery"    # High uncertainty, requires exploration

def classify_horizon(concept: Dict, market_data: Dict) -> str:
    """
    Classify opportunity using Three Horizons framework:
    Horizon 1: Core business improvements/extensions
    Horizon 2: Adjacent growth opportunities
    Horizon 3: Transformational/exploratory opportunities
    """
    
    # Assess market and solution newness
    market_maturity = concept.get('positioning', {}).get('market_maturity', 'Growing')
    innovation_level = concept.get('attributes', {}).get('innovation_level', 'Incremental')
    target_market = concept.get('positioning', {}).get('target_market', {})
    
    # Market newness
    if market_maturity in ['Emerging']:
        market_newness = 3  # New market
    elif market_maturity in ['Growing']:
        market_newness = 2  # Adjacent market
    else:
        market_newness = 1  # Existing market
    
    # Solution newness
    if innovation_level == 'Disruptive':
        solution_newness = 3  # New solution
    elif innovation_level == 'Radical':
        solution_newness = 2  # Adjacent solution
    else:
        solution_newness = 1  # Existing solution type
    
    # Technology readiness
    trl = concept.get('technical', {}).get('technology_readiness_level', 5)
    if trl <= 3:
        tech_newness = 3  # New technology
    elif trl <= 6:
        tech_newness = 2  # Adjacent technology
    else:
        tech_newness = 1  # Existing technology
    
    # Calculate weighted horizon score
    horizon_score = (market_newness * 0.4 + solution_newness * 0.4 + tech_newness * 0.2)
    
    if horizon_score >= 2.5:
        return "Horizon 3"  # Exploration into new markets/solutions
    elif horizon_score >= 1.8:
        return "Horizon 2"  # Adjacent growth
    else:
        return "Horizon 1"  # Core business improvements

def calculate_market_size_score(market_data: Dict) -> float:
    """Calculate market size opportunity score (0-100)"""
    market_size = market_data.get('market_size', 0)
    
    if market_size == 0:
        return 20  # No market data is risky
    
    # Log scale scoring for market size
    # $1M = 30, $10M = 50, $100M = 70, $1B+ = 90+
    if market_size >= 1000000000:  # $1B+
        return 95
    elif market_size >= 100000000:  # $100M+
        return 80
    elif market_size >= 10000000:   # $10M+
        return 65
    elif market_size >= 1000000:    # $1M+
        return 45
    elif market_size >= 100000:     # $100K+
        return 30
    else:
        return 15

def calculate_growth_rate_score(market_data: Dict) -> float:
    """Calculate market growth opportunity score (0-100)"""
    growth_rate = market_data.get('growth_rate', 0)
    
    # Annual growth rate scoring
    if growth_rate >= 0.25:      # 25%+ growth
        return 95
    elif growth_rate >= 0.15:    # 15%+ growth
        return 85
    elif growth_rate >= 0.10:    # 10%+ growth
        return 75
    elif growth_rate >= 0.05:    # 5%+ growth
        return 60
    elif growth_rate >= 0.0:     # Positive growth
        return 45
    elif growth_rate >= -0.05:   # Slight decline
        return 25
    else:                        # Declining market
        return 10

def calculate_competitive_intensity_score(concept: Dict) -> float:
    """Calculate competitive intensity score (higher = less competition)"""
    competition = concept.get('positioning', {}).get('competitive_landscape', {})
    direct_competitors = competition.get('direct_competitors', [])
    competitive_advantages = competition.get('competitive_advantages', [])
    
    # Base score from number of competitors
    if len(direct_competitors) == 0:
        base_score = 95  # No direct competition (blue ocean or no market)
    elif len(direct_competitors) <= 2:
        base_score = 80  # Low competition
    elif len(direct_competitors) <= 5:
        base_score = 60  # Moderate competition
    elif len(direct_competitors) <= 10:
        base_score = 40  # High competition
    else:
        base_score = 20  # Very high competition
    
    # Adjust for competitive advantages
    strong_advantages = sum(1 for adv in competitive_advantages 
                           if adv.get('strength') == 'Strong')
    
    if strong_advantages >= 2:
        advantage_bonus = 20
    elif strong_advantages == 1:
        advantage_bonus = 10
    elif len(competitive_advantages) > 0:
        advantage_bonus = 5
    else:
        advantage_bonus = -10  # No clear advantages
    
    return min(100, max(0, base_score + advantage_bonus))

def calculate_addressable_segment_score(concept: Dict, market_data: Dict) -> float:
    """Calculate addressable segment opportunity score"""
    total_market = market_data.get('market_size', 0)
    target_segment = concept.get('positioning', {}).get('target_market', {})
    segment_size = target_segment.get('segment_size', 0)
    
    if total_market == 0 or segment_size == 0:
        return 30  # Unknown addressable segment
    
    # Calculate what percentage of market is addressable
    addressable_ratio = segment_size / total_market
    
    # Score based on absolute size and percentage
    if segment_size >= 10000000 and addressable_ratio >= 0.1:  # $10M+ and 10%+
        return 90
    elif segment_size >= 1000000 and addressable_ratio >= 0.05:  # $1M+ and 5%+
        return 75
    elif segment_size >= 100000 and addressable_ratio >= 0.02:   # $100K+ and 2%+
        return 60
    elif segment_size >= 50000:                                  # $50K+
        return 45
    else:
        return 25

def assess_certainty_level(knowledge_stage: str, market_data: Dict, concept: Dict) -> str:
    """Assess level of certainty about the opportunity"""
    uncertainty_factors = 0
    
    # Knowledge stage uncertainty
    if knowledge_stage == "Mystery":
        uncertainty_factors += 3
    elif knowledge_stage == "Heuristic":
        uncertainty_factors += 1
    
    # Market data uncertainty
    if not market_data.get('market_size') or not market_data.get('growth_rate'):
        uncertainty_factors += 2
    
    # Competitive uncertainty
    competition = concept.get('positioning', {}).get('competitive_landscape', {})
    if not competition.get('direct_competitors'):
        uncertainty_factors += 1
    
    # Technical uncertainty
    trl = concept.get('technical', {}).get('technology_readiness_level', 1)
    if trl <= 3:
        uncertainty_factors += 2
    elif trl <= 6:
        uncertainty_factors += 1
    
    # User validation uncertainty
    validation = concept.get('validation', {})
    if not validation.get('user_research'):
        uncertainty_factors += 1
    
    if uncertainty_factors >= 6:
        return "High Uncertainty"
    elif uncertainty_factors >= 3:
        return "Medium Uncertainty"
    else:
        return "Low Uncertainty"

def determine_exploration_exploitation_balance(horizon: str, knowledge_stage: str, 
                                             certainty: str) -> str:
    """
    Determine exploration vs exploitation approach based on Roger Martin framework
    """
    
    if horizon == "Horizon 3" or knowledge_stage == "Mystery":
        return "Heavy Exploration"
    elif horizon == "Horizon 2" or knowledge_stage == "Heuristic":
        if certainty == "High Uncertainty":
            return "Exploration Focus"
        else:
            return "Balanced Exploration-Exploitation"
    else:  # Horizon 1 or Algorithm
        if certainty == "Low Uncertainty":
            return "Exploitation Focus"
        else:
            return "Cautious Exploitation"

def generate_recommended_approach(horizon: str, knowledge_stage: str, 
                                certainty: str, overall_score: float) -> str:
    """Generate recommended approach based on Northwestern MPD2 methodology"""
    
    if overall_score < 40:
        return "🔴 **DO NOT PURSUE**: Low opportunity score suggests significant risks outweigh potential."
    
    if knowledge_stage == "Mystery":
        return "🔬 **EXPLORE & LEARN**: Focus on understanding user needs, market dynamics, and technical feasibility before major investment."
    
    elif knowledge_stage == "Heuristic":
        if horizon == "Horizon 3":
            return "🧪 **EXPERIMENT & VALIDATE**: Run small experiments to test key assumptions while building understanding."
        elif horizon == "Horizon 2":
            return "📈 **PILOT & SCALE**: Develop pilot programs to validate business model before full market entry."
        else:
            return "⚡ **OPTIMIZE & EXECUTE**: Apply existing capabilities with proven approaches for quick wins."
    
    else:  # Algorithm stage
        if overall_score >= 75:
            return "🚀 **FULL SPEED AHEAD**: High-confidence opportunity with systematic approach to capture value."
        elif overall_score >= 60:
            return "✅ **MEASURED ADVANCE**: Good opportunity but monitor key metrics and be ready to adjust."
        else:
            return "⚠️ **CAREFUL PROGRESS**: Moderate opportunity requiring risk management and milestone gates."

def calculate_risk_adjusted_score(overall_score: float, certainty: str, 
                                knowledge_stage: str) -> float:
    """Calculate risk-adjusted opportunity score"""
    
    # Risk adjustment factors
    certainty_adjustments = {
        "Low Uncertainty": 1.0,
        "Medium Uncertainty": 0.85,
        "High Uncertainty": 0.7
    }
    
    knowledge_adjustments = {
        "Algorithm": 1.0,
        "Heuristic": 0.9,
        "Mystery": 0.75
    }
    
    certainty_factor = certainty_adjustments.get(certainty, 0.85)
    knowledge_factor = knowledge_adjustments.get(knowledge_stage, 0.9)
    
    # Combined risk adjustment
    risk_factor = (certainty_factor + knowledge_factor) / 2
    
    return overall_score * risk_factor

def calculate_confidence_interval(overall_score: float, certainty: str) -> Tuple[float, float]:
    """Calculate confidence interval based on uncertainty level"""
    
    uncertainty_ranges = {
        "Low Uncertainty": 5,     # ±5 points
        "Medium Uncertainty": 15, # ±15 points
        "High Uncertainty": 25    # ±25 points
    }
    
    range_size = uncertainty_ranges.get(certainty, 15)
    
    lower = max(0, overall_score - range_size)
    upper = min(100, overall_score + range_size)
    
    return (round(lower, 1), round(upper, 1))

def identify_key_insights(assessment_data: Dict) -> List[str]:
    """Identify key insights from the opportunity assessment"""
    insights = []
    
    horizon = assessment_data['horizon']
    knowledge_stage = assessment_data['knowledge_stage']
    certainty = assessment_data['certainty']
    scores = assessment_data['scores']
    
    # Market insights
    if scores['market_size'] >= 80:
        insights.append("Large addressable market provides significant revenue potential")
    elif scores['market_size'] <= 30:
        insights.append("Small market size may limit growth potential")
    
    if scores['growth_rate'] >= 80:
        insights.append("High market growth rate suggests strong momentum and timing")
    elif scores['growth_rate'] <= 30:
        insights.append("Slow/declining market growth presents timing challenges")
    
    # Competitive insights
    if scores['competitive_intensity'] >= 80:
        insights.append("Low competitive intensity offers first-mover advantage potential")
    elif scores['competitive_intensity'] <= 40:
        insights.append("High competition requires strong differentiation strategy")
    
    # Strategic insights
    if horizon == "Horizon 3" and knowledge_stage == "Mystery":
        insights.append("High-uncertainty exploration opportunity requires patient capital and learning approach")
    elif horizon == "Horizon 1" and knowledge_stage == "Algorithm":
        insights.append("Low-risk optimization opportunity suitable for systematic execution")
    
    # Risk insights
    if certainty == "High Uncertainty":
        insights.append("High uncertainty suggests need for assumption validation before major investment")
    
    return insights[:5]  # Return top 5 insights

def identify_next_steps(horizon: str, knowledge_stage: str, certainty: str, 
                       overall_score: float) -> List[str]:
    """Identify next steps based on Northwestern MPD2 methodology"""
    steps = []
    
    if knowledge_stage == "Mystery":
        steps.append("Conduct user research to understand core needs and jobs-to-be-done")
        steps.append("Analyze competitive landscape and market dynamics")
        steps.append("Develop and test key assumptions about value proposition")
        
    elif knowledge_stage == "Heuristic":
        steps.append("Create minimum viable product or prototype for validation")
        steps.append("Test business model assumptions with pilot customers")
        steps.append("Refine positioning and go-to-market strategy")
        
    else:  # Algorithm
        steps.append("Develop detailed business plan and financial projections")
        steps.append("Build operational capabilities for market entry")
        steps.append("Execute systematic rollout with performance monitoring")
    
    # Add horizon-specific steps
    if horizon == "Horizon 3":
        steps.append("Establish learning metrics and experimentation framework")
    elif horizon == "Horizon 2":
        steps.append("Define partnership strategy and ecosystem development")
    else:  # Horizon 1
        steps.append("Integrate with existing operations and capabilities")
    
    return steps[:5]  # Return top 5 steps

def calculate_opportunity_score(market_file: Path, concept_file: Path) -> OpportunityAssessment:
    """Calculate comprehensive opportunity score using Northwestern MPD2 frameworks"""
    
    # Load data
    market_data = load_yaml_file(market_file)
    concept = load_yaml_file(concept_file)
    
    # Apply Northwestern frameworks
    knowledge_stage = classify_knowledge_stage(concept, market_data)
    horizon = classify_horizon(concept, market_data)
    
    # Calculate component scores
    market_size_score = calculate_market_size_score(market_data)
    growth_rate_score = calculate_growth_rate_score(market_data)
    competitive_intensity_score = calculate_competitive_intensity_score(concept)
    addressable_segment_score = calculate_addressable_segment_score(concept, market_data)
    
    # Calculate weighted overall score
    weights = {
        'market_size': 0.30,
        'growth_rate': 0.25,
        'competitive_intensity': 0.25,
        'addressable_segment': 0.20
    }
    
    overall_score = (
        market_size_score * weights['market_size'] +
        growth_rate_score * weights['growth_rate'] +
        competitive_intensity_score * weights['competitive_intensity'] +
        addressable_segment_score * weights['addressable_segment']
    )
    
    # Assess uncertainty and risk
    certainty = assess_certainty_level(knowledge_stage, market_data, concept)
    exploration_exploitation = determine_exploration_exploitation_balance(horizon, knowledge_stage, certainty)
    recommended_approach = generate_recommended_approach(horizon, knowledge_stage, certainty, overall_score)
    risk_adjusted_score = calculate_risk_adjusted_score(overall_score, certainty, knowledge_stage)
    confidence_interval = calculate_confidence_interval(overall_score, certainty)
    
    # Generate insights and next steps
    assessment_data = {
        'horizon': horizon,
        'knowledge_stage': knowledge_stage,
        'certainty': certainty,
        'scores': {
            'market_size': market_size_score,
            'growth_rate': growth_rate_score,
            'competitive_intensity': competitive_intensity_score,
            'addressable_segment': addressable_segment_score
        }
    }
    
    key_insights = identify_key_insights(assessment_data)
    next_steps = identify_next_steps(horizon, knowledge_stage, certainty, overall_score)
    
    return OpportunityAssessment(
        overall_score=round(overall_score, 1),
        horizon_classification=horizon,
        knowledge_stage=knowledge_stage,
        market_size_score=round(market_size_score, 1),
        growth_rate_score=round(growth_rate_score, 1),
        competitive_intensity_score=round(competitive_intensity_score, 1),
        addressable_segment_score=round(addressable_segment_score, 1),
        certainty_level=certainty,
        exploration_exploitation_balance=exploration_exploitation,
        recommended_approach=recommended_approach,
        risk_adjusted_score=round(risk_adjusted_score, 1),
        confidence_interval=confidence_interval,
        key_insights=key_insights,
        next_steps=next_steps
    )

def generate_opportunity_report(assessment: OpportunityAssessment, output_format: str = 'markdown') -> str:
    """Generate opportunity assessment report"""
    
    if output_format.lower() == 'markdown':
        report = f"""# Opportunity Assessment Report
*Based on Northwestern MPD2 & Roger Martin Frameworks*

## Executive Summary
**Overall Opportunity Score**: {assessment.overall_score}/100  
**Risk-Adjusted Score**: {assessment.risk_adjusted_score}/100  
**Confidence Range**: {assessment.confidence_interval[0]}-{assessment.confidence_interval[1]}

## Strategic Classification

| Framework | Classification |
|-----------|---------------|
| **Three Horizons** | {assessment.horizon_classification} |
| **Knowledge Funnel** | {assessment.knowledge_stage} |
| **Certainty Level** | {assessment.certainty_level} |
| **Approach Balance** | {assessment.exploration_exploitation_balance} |

## Opportunity Breakdown

| Component | Score | Assessment |
|-----------|-------|------------|
| Market Size | {assessment.market_size_score}/100 | {'🟢 Large' if assessment.market_size_score >= 70 else '🟡 Medium' if assessment.market_size_score >= 40 else '🔴 Small'} |
| Growth Rate | {assessment.growth_rate_score}/100 | {'🟢 High' if assessment.growth_rate_score >= 70 else '🟡 Medium' if assessment.growth_rate_score >= 40 else '🔴 Low'} |
| Competitive Position | {assessment.competitive_intensity_score}/100 | {'🟢 Favorable' if assessment.competitive_intensity_score >= 70 else '🟡 Moderate' if assessment.competitive_intensity_score >= 40 else '🔴 Challenging'} |
| Addressable Segment | {assessment.addressable_segment_score}/100 | {'🟢 Strong' if assessment.addressable_segment_score >= 70 else '🟡 Moderate' if assessment.addressable_segment_score >= 40 else '🔴 Limited'} |

## Strategic Recommendation
{assessment.recommended_approach}

## Key Insights
"""
        for i, insight in enumerate(assessment.key_insights, 1):
            report += f"{i}. {insight}\n"
        
        report += "\n## Recommended Next Steps\n"
        for i, step in enumerate(assessment.next_steps, 1):
            report += f"{i}. {step}\n"
        
        report += f"""
## Framework Applications

**Knowledge Funnel Stage**: {assessment.knowledge_stage}
- Focus on {"systematic execution" if assessment.knowledge_stage == "Algorithm" else "developing heuristics" if assessment.knowledge_stage == "Heuristic" else "exploration and understanding"}

**Three Horizons Position**: {assessment.horizon_classification}
- {"Core business optimization with proven approaches" if assessment.horizon_classification == "Horizon 1" else "Adjacent growth requiring new capabilities" if assessment.horizon_classification == "Horizon 2" else "Transformational opportunity requiring exploration"}

**Exploration-Exploitation**: {assessment.exploration_exploitation_balance}
- Emphasize {"exploitation of known patterns" if "Exploitation" in assessment.exploration_exploitation_balance else "exploration of new possibilities" if "Exploration" in assessment.exploration_exploitation_balance else "balanced approach"}
"""
        
        return report
    
    elif output_format.lower() == 'json':
        return json.dumps({
            'overall_score': assessment.overall_score,
            'risk_adjusted_score': assessment.risk_adjusted_score,
            'confidence_interval': {
                'lower': assessment.confidence_interval[0],
                'upper': assessment.confidence_interval[1]
            },
            'strategic_classification': {
                'horizon': assessment.horizon_classification,
                'knowledge_stage': assessment.knowledge_stage,
                'certainty_level': assessment.certainty_level,
                'exploration_exploitation': assessment.exploration_exploitation_balance
            },
            'component_scores': {
                'market_size': assessment.market_size_score,
                'growth_rate': assessment.growth_rate_score,
                'competitive_intensity': assessment.competitive_intensity_score,
                'addressable_segment': assessment.addressable_segment_score
            },
            'recommended_approach': assessment.recommended_approach,
            'key_insights': assessment.key_insights,
            'next_steps': assessment.next_steps
        }, indent=2)
    
    else:
        return f"Opportunity Score: {assessment.overall_score}/100 ({assessment.horizon_classification}, {assessment.knowledge_stage})"

def main():
    parser = argparse.ArgumentParser(description='Northwestern MPD2 Opportunity Assessment')
    parser.add_argument('market_file', type=str, help='Path to market data YAML file')
    parser.add_argument('concept_file', type=str, help='Path to concept YAML file')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--format', choices=['markdown', 'json', 'summary'], default='markdown',
                       help='Output format')
    
    args = parser.parse_args()
    
    try:
        market_path = Path(args.market_file)
        concept_path = Path(args.concept_file)
        
        if not market_path.exists():
            print(f"❌ Error: Market file {market_path} not found")
            sys.exit(1)
        
        if not concept_path.exists():
            print(f"❌ Error: Concept file {concept_path} not found")
            sys.exit(1)
        
        # Calculate opportunity assessment
        assessment = calculate_opportunity_score(market_path, concept_path)
        
        # Generate report
        report = generate_opportunity_report(assessment, args.format)
        
        # Output report
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"✅ Opportunity assessment written to: {args.output}")
        else:
            print(report)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()