#!/usr/bin/env python3
"""
Enhanced Feasibility Score Calculator

Extends the existing product_concept_validator.py with enhanced feasibility assessment.
Provides detailed breakdown by feasibility dimensions with confidence intervals.

Input: concept.yaml + constraints.yaml
Output: 0-100 feasibility score with breakdown by technical, resource, timeline, market readiness
"""

import yaml
import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import importlib.util

@dataclass
class FeasibilityScore:
    """Complete feasibility assessment with category breakdown"""
    overall_score: float
    technical_feasibility: float
    resource_availability: float
    timeline_realistic: float
    market_ready: float
    confidence_interval: Tuple[float, float]
    feasibility_level: str
    key_enablers: List[str]
    critical_barriers: List[str]
    recommendation: str

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

def get_existing_validator_score(concept: Dict) -> Optional[Dict]:
    """Get score from existing product concept validator for comparison"""
    try:
        # Try to import and use existing validator
        validator_path = Path(__file__).parent.parent.parent.parent / "tools" / "product_concept_validator.py"
        if validator_path.exists():
            spec = importlib.util.spec_from_file_location("validator", validator_path)
            validator = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(validator)
            
            # Convert concept to ProductConcept format expected by existing tool
            try:
                product_concept = validator.ProductConcept(
                    name=concept.get('name', 'Unknown'),
                    description=concept.get('description', ''),
                    market=validator.MarketCriteria(
                        target_market_size=concept.get('positioning', {}).get('target_market', {}).get('segment_size'),
                        market_growth_rate=concept.get('positioning', {}).get('target_market', {}).get('growth_rate'),
                        competitive_landscape=str(concept.get('positioning', {}).get('competitive_landscape', {})),
                        value_proposition_clarity=8 if concept.get('core_value_proposition') else 5
                    ),
                    technical=validator.TechnicalCriteria(
                        technology_readiness_level=concept.get('technical', {}).get('technology_readiness_level'),
                        development_complexity=concept.get('attributes', {}).get('complexity'),
                        integration_requirements=concept.get('technical', {}).get('integration_points', []),
                        performance_requirements=concept.get('technical', {}).get('performance_requirements', {})
                    ),
                    manufacturing=validator.ManufacturingCriteria(
                        manufacturing_process=concept.get('technical', {}).get('system_type'),
                        material_availability="High",  # Default assumption
                        tooling_requirements="Medium",  # Default assumption
                        scalability_assessment=concept.get('technical', {}).get('scalability', {}).get('scaling_strategy', "Medium")
                    ),
                    resources=validator.ResourceCriteria(
                        development_timeline_weeks=concept.get('development', {}).get('timeline', {}).get('full_development_weeks'),
                        team_size_required=concept.get('development', {}).get('resources', {}).get('team_size'),
                        budget_estimate_usd=concept.get('development', {}).get('resources', {}).get('budget_estimate'),
                        expertise_required=concept.get('development', {}).get('resources', {}).get('key_skills', [])
                    )
                )
                return product_concept.calculate_feasibility_score()
            except Exception as e:
                print(f"Warning: Could not use existing validator: {e}")
                return None
    except Exception:
        return None

def calculate_technical_feasibility(concept: Dict, constraints: Dict) -> float:
    """Calculate technical implementation feasibility"""
    technical_score = 0.0
    factors = 0
    
    # Technology Readiness Level (TRL)
    trl = concept.get('technical', {}).get('technology_readiness_level')
    if trl:
        factors += 1
        # TRL 1-3: Research, TRL 4-6: Development, TRL 7-9: Deployment
        if trl >= 7:
            technical_score += 90  # High feasibility
        elif trl >= 4:
            technical_score += 60  # Medium feasibility
        else:
            technical_score += 30  # Low feasibility - research needed
    
    # Development Complexity
    complexity = concept.get('attributes', {}).get('complexity', 'Medium')
    factors += 1
    complexity_scores = {'Low': 85, 'Medium': 60, 'High': 35}
    technical_score += complexity_scores.get(complexity, 60)
    
    # Technology Stack Maturity
    tech_stack = concept.get('technical', {}).get('architecture', {}).get('technology_stack', [])
    if tech_stack:
        factors += 1
        # Assume modern, well-supported technologies score higher
        stack_maturity = 70  # Base assumption for typical stacks
        technical_score += stack_maturity
    
    # Integration Complexity
    integrations = concept.get('technical', {}).get('integration_points', [])
    factors += 1
    if len(integrations) == 0:
        technical_score += 80  # No integration complexity
    elif len(integrations) <= 2:
        technical_score += 60  # Low integration complexity
    elif len(integrations) <= 5:
        technical_score += 40  # Medium integration complexity
    else:
        technical_score += 20  # High integration complexity
    
    # Performance Requirements Feasibility
    perf_reqs = concept.get('technical', {}).get('performance_requirements', [])
    if perf_reqs:
        factors += 1
        # Assess if performance requirements are reasonable
        # This is simplified - in practice would need domain-specific analysis
        technical_score += 65  # Assume moderate feasibility for now
    
    # Technical Constraints Impact
    tech_constraints = [c for c in constraints.get('constraints', []) 
                       if c.get('category') == 'Technical']
    if tech_constraints:
        factors += 1
        # More flexible constraints = higher feasibility
        flexibility_scores = []
        for constraint in tech_constraints:
            flexibility = constraint.get('constraint_definition', {}).get('flexibility', 'Medium')
            flex_score = {'High': 80, 'Medium': 60, 'Low': 40, 'None': 20}.get(flexibility, 60)
            flexibility_scores.append(flex_score)
        
        avg_flexibility = sum(flexibility_scores) / len(flexibility_scores) if flexibility_scores else 60
        technical_score += avg_flexibility
    
    return technical_score / max(factors, 1) if factors > 0 else 50.0

def calculate_resource_availability(concept: Dict, constraints: Dict) -> float:
    """Calculate resource availability and adequacy"""
    resource_score = 0.0
    factors = 0
    
    # Team Size Adequacy
    team_size = concept.get('development', {}).get('resources', {}).get('team_size')
    if team_size:
        factors += 1
        # Assess team size adequacy based on project complexity and timeline
        complexity = concept.get('attributes', {}).get('complexity', 'Medium')
        timeline_weeks = concept.get('development', {}).get('timeline', {}).get('full_development_weeks', 26)
        
        # Simple heuristic: Low complexity = 2-4 people, Medium = 4-8, High = 8-15
        complexity_needs = {'Low': (2, 4), 'Medium': (4, 8), 'High': (8, 15)}
        min_team, max_team = complexity_needs.get(complexity, (4, 8))
        
        if min_team <= team_size <= max_team:
            resource_score += 80  # Right-sized team
        elif team_size < min_team:
            resource_score += 40  # Under-resourced
        else:
            resource_score += 60  # Over-resourced (coordination overhead)
    
    # Budget Adequacy
    budget = concept.get('development', {}).get('resources', {}).get('budget_estimate')
    timeline_weeks = concept.get('development', {}).get('timeline', {}).get('full_development_weeks', 26)
    team_size = concept.get('development', {}).get('resources', {}).get('team_size', 5)
    
    if budget and timeline_weeks and team_size:
        factors += 1
        # Rough budget check: $100k per person per year as baseline
        estimated_cost = team_size * (timeline_weeks / 52) * 100000
        budget_ratio = budget / estimated_cost
        
        if budget_ratio >= 1.2:
            resource_score += 85  # Well-funded
        elif budget_ratio >= 1.0:
            resource_score += 70  # Adequately funded
        elif budget_ratio >= 0.8:
            resource_score += 50  # Tight but feasible
        else:
            resource_score += 25  # Under-funded
    
    # Skills Availability
    required_skills = concept.get('development', {}).get('resources', {}).get('key_skills', [])
    if required_skills:
        factors += 1
        # Assess skill rarity/availability (simplified)
        common_skills = ['project management', 'design', 'development', 'testing']
        rare_skills = ['ai/ml', 'blockchain', 'hardware', 'regulatory expertise']
        
        rare_skill_count = sum(1 for skill in required_skills 
                              if any(rare in skill.lower() for rare in rare_skills))
        total_skills = len(required_skills)
        
        if rare_skill_count == 0:
            resource_score += 80  # Common skills
        elif rare_skill_count / total_skills <= 0.3:
            resource_score += 60  # Some rare skills
        else:
            resource_score += 35  # Many rare skills
    
    # Resource Constraints Impact
    resource_constraints = [c for c in constraints.get('constraints', []) 
                           if c.get('category') == 'Resource']
    if resource_constraints:
        factors += 1
        # Assess severity of resource constraints
        severity_scores = []
        for constraint in resource_constraints:
            severity = constraint.get('impact', {}).get('severity', 'Medium')
            sev_score = {'Low': 70, 'Medium': 50, 'High': 30, 'Critical': 10}.get(severity, 50)
            severity_scores.append(sev_score)
        
        avg_constraint_impact = sum(severity_scores) / len(severity_scores) if severity_scores else 60
        resource_score += avg_constraint_impact
    
    return resource_score / max(factors, 1) if factors > 0 else 50.0

def calculate_timeline_realistic(concept: Dict, constraints: Dict) -> float:
    """Calculate timeline realism and achievability"""
    timeline_score = 0.0
    factors = 0
    
    # Overall Timeline Assessment
    timeline_weeks = concept.get('development', {}).get('timeline', {}).get('full_development_weeks')
    if timeline_weeks:
        factors += 1
        complexity = concept.get('attributes', {}).get('complexity', 'Medium')
        
        # Baseline timeline expectations by complexity
        baseline_weeks = {'Low': 12, 'Medium': 26, 'High': 52}
        expected_weeks = baseline_weeks.get(complexity, 26)
        
        timeline_ratio = timeline_weeks / expected_weeks
        
        if 0.8 <= timeline_ratio <= 1.5:
            timeline_score += 80  # Realistic timeline
        elif 0.6 <= timeline_ratio < 0.8 or 1.5 < timeline_ratio <= 2.0:
            timeline_score += 50  # Challenging but possible
        else:
            timeline_score += 25  # Unrealistic timeline
    
    # Phase Structure Assessment
    phases = concept.get('development', {}).get('timeline', {}).get('phases', [])
    if phases:
        factors += 1
        # More phases generally indicate better planning
        phase_count = len(phases)
        if 3 <= phase_count <= 6:
            timeline_score += 75  # Well-structured
        elif phase_count < 3:
            timeline_score += 50  # Simple but may lack detail
        else:
            timeline_score += 60  # Very detailed but may be over-planned
    
    # Dependencies Assessment
    external_deps = concept.get('development', {}).get('dependencies', {}).get('external_dependencies', [])
    internal_deps = concept.get('development', {}).get('dependencies', {}).get('internal_dependencies', [])
    
    factors += 1
    total_deps = len(external_deps) + len(internal_deps)
    external_ratio = len(external_deps) / max(total_deps, 1)
    
    # External dependencies are riskier for timeline
    if external_ratio <= 0.2:
        timeline_score += 80  # Low external dependency
    elif external_ratio <= 0.4:
        timeline_score += 60  # Moderate external dependency
    else:
        timeline_score += 35  # High external dependency
    
    # Time Constraints Impact
    time_constraints = [c for c in constraints.get('constraints', []) 
                       if c.get('category') == 'Time']
    if time_constraints:
        factors += 1
        # Hard time constraints reduce timeline feasibility
        hard_constraints = sum(1 for c in time_constraints 
                              if c.get('type') == 'Hard')
        total_time_constraints = len(time_constraints)
        
        if hard_constraints == 0:
            timeline_score += 70  # No hard deadlines
        elif hard_constraints / total_time_constraints <= 0.5:
            timeline_score += 50  # Some hard deadlines
        else:
            timeline_score += 30  # Many hard deadlines
    
    return timeline_score / max(factors, 1) if factors > 0 else 50.0

def calculate_market_ready(concept: Dict) -> float:
    """Calculate market readiness and timing"""
    market_score = 0.0
    factors = 0
    
    # Market Maturity
    maturity = concept.get('positioning', {}).get('market_maturity', 'Growing')
    factors += 1
    maturity_scores = {
        'Emerging': 45,  # High potential but risky
        'Growing': 80,   # Best timing
        'Mature': 60,    # Stable but competitive
        'Declining': 25  # Poor timing
    }
    market_score += maturity_scores.get(maturity, 60)
    
    # Competitive Landscape Readiness
    competitors = concept.get('positioning', {}).get('competitive_landscape', {})
    direct_competitors = competitors.get('direct_competitors', [])
    advantages = competitors.get('competitive_advantages', [])
    
    factors += 1
    if len(direct_competitors) == 0 and len(advantages) == 0:
        market_score += 40  # No market or no advantage
    elif len(direct_competitors) == 0:
        market_score += 60  # Blue ocean but validate market exists
    elif len(advantages) >= len(direct_competitors):
        market_score += 85  # Good competitive position
    else:
        market_score += 50  # Competitive but challenging
    
    # Value Proposition Clarity
    value_prop = concept.get('core_value_proposition', {})
    factors += 1
    
    vp_score = 0
    if value_prop.get('primary_benefit'):
        vp_score += 25
    if value_prop.get('target_user_segment'):
        vp_score += 25
    if value_prop.get('job_to_be_done'):
        vp_score += 25
    if value_prop.get('differentiation'):
        vp_score += 25
    
    market_score += vp_score
    
    # Business Model Clarity
    business_model = concept.get('business_model', {})
    if business_model:
        factors += 1
        bm_score = 0
        if business_model.get('revenue_streams'):
            bm_score += 35
        if business_model.get('cost_structure'):
            bm_score += 35
        if business_model.get('key_partnerships'):
            bm_score += 30
        
        market_score += bm_score
    
    return market_score / max(factors, 1) if factors > 0 else 50.0

def calculate_confidence_interval(scores: Dict[str, float]) -> Tuple[float, float]:
    """Calculate confidence interval for overall feasibility score"""
    # Simple approach: use variance in category scores as uncertainty measure
    score_values = list(scores.values())
    mean_score = sum(score_values) / len(score_values)
    
    # Calculate standard deviation
    variance = sum((score - mean_score) ** 2 for score in score_values) / len(score_values)
    std_dev = variance ** 0.5
    
    # 90% confidence interval (approximately ±1.65 standard deviations)
    margin = 1.65 * std_dev
    
    lower_bound = max(0, mean_score - margin)
    upper_bound = min(100, mean_score + margin)
    
    return (round(lower_bound, 1), round(upper_bound, 1))

def determine_feasibility_level(overall_score: float) -> str:
    """Determine feasibility level from overall score"""
    if overall_score >= 80:
        return "Highly Feasible"
    elif overall_score >= 65:
        return "Feasible"
    elif overall_score >= 50:
        return "Moderately Feasible"
    elif overall_score >= 35:
        return "Challenging Feasibility"
    else:
        return "Low Feasibility"

def identify_key_enablers(scores: Dict[str, float], concept: Dict) -> List[str]:
    """Identify key factors that enable feasibility"""
    enablers = []
    
    if scores['technical_feasibility'] >= 70:
        trl = concept.get('technical', {}).get('technology_readiness_level')
        if trl and trl >= 7:
            enablers.append(f"Mature technology (TRL {trl})")
        
        complexity = concept.get('attributes', {}).get('complexity')
        if complexity == 'Low':
            enablers.append("Low development complexity")
    
    if scores['resource_availability'] >= 70:
        enablers.append("Adequate resources and budget")
    
    if scores['timeline_realistic'] >= 70:
        enablers.append("Realistic development timeline")
    
    if scores['market_ready'] >= 70:
        maturity = concept.get('positioning', {}).get('market_maturity')
        if maturity == 'Growing':
            enablers.append("Growing market opportunity")
        
        value_prop = concept.get('core_value_proposition', {})
        if all(value_prop.get(key) for key in ['primary_benefit', 'target_user_segment', 'differentiation']):
            enablers.append("Clear value proposition")
    
    return enablers

def identify_critical_barriers(scores: Dict[str, float], concept: Dict, constraints: Dict) -> List[str]:
    """Identify critical barriers to feasibility"""
    barriers = []
    
    if scores['technical_feasibility'] < 50:
        trl = concept.get('technical', {}).get('technology_readiness_level')
        if trl and trl < 4:
            barriers.append(f"Immature technology (TRL {trl})")
        
        complexity = concept.get('attributes', {}).get('complexity')
        if complexity == 'High':
            barriers.append("High development complexity")
    
    if scores['resource_availability'] < 50:
        barriers.append("Insufficient resources or budget")
    
    if scores['timeline_realistic'] < 50:
        barriers.append("Unrealistic timeline expectations")
    
    if scores['market_ready'] < 50:
        barriers.append("Market timing or competitive challenges")
    
    # Add constraint-based barriers
    critical_constraints = [c for c in constraints.get('constraints', [])
                          if c.get('impact', {}).get('severity') in ['Critical', 'High']]
    for constraint in critical_constraints[:2]:  # Top 2 critical constraints
        barriers.append(f"Critical constraint: {constraint.get('name', 'Unknown')}")
    
    return barriers

def generate_recommendation(overall_score: float, feasibility_level: str, 
                          enablers: List[str], barriers: List[str]) -> str:
    """Generate recommendation based on feasibility assessment"""
    if overall_score >= 75:
        return "✅ **PROCEED**: High feasibility with strong enablers. Recommended for development."
    elif overall_score >= 60:
        return "🟡 **PROCEED WITH CAUTION**: Good feasibility but address identified barriers before full commitment."
    elif overall_score >= 45:
        return "⚠️ **CONDITIONAL PROCEED**: Moderate feasibility. Address critical barriers and validate key assumptions."
    elif overall_score >= 30:
        return "🔴 **DO NOT PROCEED**: Low feasibility. Significant changes needed or consider alternative approaches."
    else:
        return "🛑 **STOP**: Very low feasibility. Fundamental changes required or abandon concept."

def calculate_enhanced_feasibility(concept_file: Path, constraints_file: Optional[Path] = None) -> FeasibilityScore:
    """Calculate enhanced feasibility score with detailed analysis"""
    
    # Load data files
    concept = load_yaml_file(concept_file)
    constraints = load_yaml_file(constraints_file) if constraints_file else {}
    
    # Get existing validator score for comparison
    existing_scores = get_existing_validator_score(concept)
    
    # Calculate enhanced category scores
    technical_feasibility = calculate_technical_feasibility(concept, constraints)
    resource_availability = calculate_resource_availability(concept, constraints)
    timeline_realistic = calculate_timeline_realistic(concept, constraints)
    market_ready = calculate_market_ready(concept)
    
    # Calculate weighted overall score
    weights = {
        'technical_feasibility': 0.30,
        'resource_availability': 0.25,
        'timeline_realistic': 0.25,
        'market_ready': 0.20
    }
    
    category_scores = {
        'technical_feasibility': technical_feasibility,
        'resource_availability': resource_availability,
        'timeline_realistic': timeline_realistic,
        'market_ready': market_ready
    }
    
    overall_score = sum(score * weights[category] for category, score in category_scores.items())
    
    # Calculate confidence interval
    confidence_interval = calculate_confidence_interval(category_scores)
    
    # Generate insights
    feasibility_level = determine_feasibility_level(overall_score)
    key_enablers = identify_key_enablers(category_scores, concept)
    critical_barriers = identify_critical_barriers(category_scores, concept, constraints)
    recommendation = generate_recommendation(overall_score, feasibility_level, key_enablers, critical_barriers)
    
    return FeasibilityScore(
        overall_score=round(overall_score, 1),
        technical_feasibility=round(technical_feasibility, 1),
        resource_availability=round(resource_availability, 1),
        timeline_realistic=round(timeline_realistic, 1),
        market_ready=round(market_ready, 1),
        confidence_interval=confidence_interval,
        feasibility_level=feasibility_level,
        key_enablers=key_enablers,
        critical_barriers=critical_barriers,
        recommendation=recommendation
    )

def generate_feasibility_report(feasibility: FeasibilityScore, output_format: str = 'markdown') -> str:
    """Generate feasibility assessment report"""
    
    if output_format.lower() == 'markdown':
        report = f"""# Feasibility Assessment Report

## Overall Feasibility: {feasibility.overall_score}/100
**Level**: {feasibility.feasibility_level}  
**Confidence Interval**: {feasibility.confidence_interval[0]}-{feasibility.confidence_interval[1]}

## Recommendation
{feasibility.recommendation}

## Feasibility Breakdown by Category

| Category | Score | Assessment |
|----------|-------|------------|
| Technical Feasibility | {feasibility.technical_feasibility}/100 | {'🟢 Strong' if feasibility.technical_feasibility >= 70 else '🟡 Moderate' if feasibility.technical_feasibility >= 50 else '🔴 Weak'} |
| Resource Availability | {feasibility.resource_availability}/100 | {'🟢 Strong' if feasibility.resource_availability >= 70 else '🟡 Moderate' if feasibility.resource_availability >= 50 else '🔴 Weak'} |
| Timeline Realistic | {feasibility.timeline_realistic}/100 | {'🟢 Strong' if feasibility.timeline_realistic >= 70 else '🟡 Moderate' if feasibility.timeline_realistic >= 50 else '🔴 Weak'} |
| Market Ready | {feasibility.market_ready}/100 | {'🟢 Strong' if feasibility.market_ready >= 70 else '🟡 Moderate' if feasibility.market_ready >= 50 else '🔴 Weak'} |

## Key Enablers
"""
        for i, enabler in enumerate(feasibility.key_enablers, 1):
            report += f"{i}. {enabler}\n"
        
        if not feasibility.key_enablers:
            report += "No significant enablers identified.\n"
        
        report += "\n## Critical Barriers\n"
        for i, barrier in enumerate(feasibility.critical_barriers, 1):
            report += f"{i}. {barrier}\n"
        
        if not feasibility.critical_barriers:
            report += "No critical barriers identified.\n"
        
        return report
    
    elif output_format.lower() == 'json':
        return json.dumps({
            'overall_score': feasibility.overall_score,
            'feasibility_level': feasibility.feasibility_level,
            'confidence_interval': {
                'lower': feasibility.confidence_interval[0],
                'upper': feasibility.confidence_interval[1]
            },
            'category_scores': {
                'technical_feasibility': feasibility.technical_feasibility,
                'resource_availability': feasibility.resource_availability,
                'timeline_realistic': feasibility.timeline_realistic,
                'market_ready': feasibility.market_ready
            },
            'key_enablers': feasibility.key_enablers,
            'critical_barriers': feasibility.critical_barriers,
            'recommendation': feasibility.recommendation
        }, indent=2)
    
    else:
        return f"Feasibility: {feasibility.overall_score}/100 ({feasibility.feasibility_level})"

def main():
    parser = argparse.ArgumentParser(description='Calculate enhanced feasibility scores for design concepts')
    parser.add_argument('concept_file', type=str, help='Path to concept YAML file')
    parser.add_argument('--constraints', type=str, help='Path to constraints YAML file')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--format', choices=['markdown', 'json', 'summary'], default='markdown',
                       help='Output format')
    
    args = parser.parse_args()
    
    try:
        concept_path = Path(args.concept_file)
        constraints_path = Path(args.constraints) if args.constraints else None
        
        if not concept_path.exists():
            print(f"❌ Error: Concept file {concept_path} not found")
            sys.exit(1)
        
        # Calculate feasibility score
        feasibility = calculate_enhanced_feasibility(concept_path, constraints_path)
        
        # Generate report
        report = generate_feasibility_report(feasibility, args.format)
        
        # Output report
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"✅ Feasibility assessment written to: {args.output}")
        else:
            print(report)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()