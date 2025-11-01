#!/usr/bin/env python3
"""
Risk Score Calculator

Calculates comprehensive risk scores for concepts using constraint and assumption data.
Integrates with existing product_concept_validator.py scoring methodology.

Input: concept.yaml + constraints.yaml + assumptions.yaml
Output: 0-100 risk score with breakdown by category
"""

import yaml
import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional
import importlib.util

# Import existing product concept validator for consistency
def import_existing_validator():
    """Import the existing product concept validator for scoring consistency"""
    validator_path = Path(__file__).parent.parent.parent.parent / "tools" / "product_concept_validator.py"
    if validator_path.exists():
        spec = importlib.util.spec_from_file_location("validator", validator_path)
        validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(validator)
        return validator
    return None

@dataclass
class RiskCategory:
    """Risk category with individual risk items"""
    name: str
    risks: List[Dict]
    weight: float = 0.25  # Default equal weighting
    
@dataclass
class RiskScore:
    """Complete risk assessment with category breakdown"""
    overall_score: float
    technical_risk: float
    market_risk: float
    resource_risk: float
    timeline_risk: float
    competitive_risk: float
    category_details: Dict
    risk_level: str
    top_risks: List[str]
    mitigation_priorities: List[str]

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

def calculate_constraint_risk(constraints: Dict) -> float:
    """Calculate risk from project constraints"""
    if not constraints:
        return 50.0  # Medium risk if no constraints defined
    
    risk_score = 0.0
    constraint_count = 0
    
    # Analyze constraint severity and flexibility
    for constraint in constraints.get('constraints', []):
        constraint_count += 1
        severity = constraint.get('impact', {}).get('severity', 'Medium')
        flexibility = constraint.get('constraint_definition', {}).get('flexibility', 'Medium')
        
        # Higher risk for high severity, low flexibility constraints
        if severity == 'Critical':
            risk_score += 90
        elif severity == 'High':
            risk_score += 70
        elif severity == 'Medium':
            risk_score += 40
        else:  # Low
            risk_score += 20
            
        # Adjust for flexibility
        if flexibility == 'None':
            risk_score += 20
        elif flexibility == 'Low':
            risk_score += 10
        elif flexibility == 'Medium':
            risk_score += 5
        # High flexibility adds no additional risk
    
    return min(risk_score / max(constraint_count, 1), 100.0) if constraint_count > 0 else 30.0

def calculate_assumption_risk(assumptions: Dict) -> float:
    """Calculate risk from project assumptions"""
    if not assumptions:
        return 60.0  # Higher risk if assumptions not identified
    
    risk_score = 0.0
    assumption_count = 0
    
    # Analyze assumption confidence and impact
    for assumption in assumptions.get('assumptions', []):
        assumption_count += 1
        confidence = assumption.get('confidence', {}).get('confidence_level', 'Medium')
        impact = assumption.get('risk', {}).get('impact_severity', 'Medium')
        critical = assumption.get('assumption_definition', {}).get('critical_path', False)
        
        # Calculate base risk from confidence and impact
        confidence_risk = {'High': 10, 'Medium': 40, 'Low': 80}.get(confidence, 40)
        impact_multiplier = {'Critical': 2.0, 'High': 1.5, 'Medium': 1.0, 'Low': 0.5}.get(impact, 1.0)
        
        assumption_risk = confidence_risk * impact_multiplier
        
        # Critical path assumptions are riskier
        if critical:
            assumption_risk *= 1.3
            
        risk_score += assumption_risk
    
    return min(risk_score / max(assumption_count, 1), 100.0) if assumption_count > 0 else 50.0

def calculate_technical_risk(concept: Dict, constraints: Dict) -> float:
    """Calculate technical implementation risk"""
    technical_score = 0.0
    factors = 0
    
    # Technology readiness level
    trl = concept.get('technical', {}).get('technology_readiness_level')
    if trl:
        factors += 1
        # Lower TRL = higher risk
        technical_score += max(0, (9 - trl) * 10)
    
    # Development complexity
    complexity = concept.get('technical', {}).get('development_complexity', 'Medium')
    factors += 1
    complexity_risk = {'Low': 20, 'Medium': 50, 'High': 80}.get(complexity, 50)
    technical_score += complexity_risk
    
    # Integration requirements risk
    integrations = concept.get('technical', {}).get('integration_requirements', [])
    if integrations:
        factors += 1
        # More integrations = higher risk
        integration_risk = min(len(integrations) * 15, 60)
        technical_score += integration_risk
    
    # Technical constraints
    tech_constraints = [c for c in constraints.get('constraints', []) 
                       if c.get('category') == 'Technical']
    if tech_constraints:
        factors += 1
        constraint_risk = calculate_constraint_risk({'constraints': tech_constraints})
        technical_score += constraint_risk * 0.8
    
    return technical_score / max(factors, 1) if factors > 0 else 50.0

def calculate_market_risk(concept: Dict) -> float:
    """Calculate market-related risk"""
    market_score = 0.0
    factors = 0
    
    # Market maturity
    maturity = concept.get('positioning', {}).get('market_maturity', 'Growing')
    factors += 1
    maturity_risk = {'Emerging': 70, 'Growing': 40, 'Mature': 60, 'Declining': 90}.get(maturity, 50)
    market_score += maturity_risk
    
    # Competitive landscape
    competitors = concept.get('positioning', {}).get('competitive_landscape', {})
    direct_competitors = competitors.get('direct_competitors', [])
    factors += 1
    
    if len(direct_competitors) == 0:
        market_score += 80  # High risk - might indicate no market
    elif len(direct_competitors) <= 2:
        market_score += 30  # Low competition risk
    elif len(direct_competitors) <= 5:
        market_score += 50  # Medium competition
    else:
        market_score += 75  # High competition
    
    # Market size risk
    market_size = concept.get('positioning', {}).get('target_market', {}).get('segment_size')
    if market_size:
        factors += 1
        if market_size < 100000:
            market_score += 80  # Small market risk
        elif market_size < 1000000:
            market_score += 50  # Medium market
        else:
            market_score += 20  # Large market
    
    return market_score / max(factors, 1) if factors > 0 else 50.0

def calculate_resource_risk(concept: Dict, constraints: Dict) -> float:
    """Calculate resource-related risk"""
    resource_score = 0.0
    factors = 0
    
    # Development timeline risk
    timeline = concept.get('development', {}).get('timeline', {}).get('full_development_weeks')
    if timeline:
        factors += 1
        if timeline > 52:  # > 1 year
            resource_score += 70
        elif timeline > 26:  # > 6 months
            resource_score += 40
        else:
            resource_score += 20
    
    # Team size risk
    team_size = concept.get('development', {}).get('resources', {}).get('team_size')
    if team_size:
        factors += 1
        if team_size > 10:
            resource_score += 60  # Large team coordination risk
        elif team_size > 5:
            resource_score += 30
        else:
            resource_score += 15
    
    # Budget risk
    budget = concept.get('development', {}).get('resources', {}).get('budget_estimate')
    if budget:
        factors += 1
        if budget > 1000000:
            resource_score += 70  # High budget risk
        elif budget > 500000:
            resource_score += 40
        else:
            resource_score += 20
    
    # Resource constraints
    resource_constraints = [c for c in constraints.get('constraints', []) 
                           if c.get('category') == 'Resource']
    if resource_constraints:
        factors += 1
        constraint_risk = calculate_constraint_risk({'constraints': resource_constraints})
        resource_score += constraint_risk * 0.9
    
    return resource_score / max(factors, 1) if factors > 0 else 50.0

def calculate_timeline_risk(concept: Dict, constraints: Dict) -> float:
    """Calculate timeline and schedule risk"""
    timeline_score = 0.0
    factors = 0
    
    # Development phases
    phases = concept.get('development', {}).get('timeline', {}).get('phases', [])
    if phases:
        factors += 1
        # More phases = more coordination risk
        phase_risk = min(len(phases) * 12, 60)
        timeline_score += phase_risk
    
    # Dependencies
    external_deps = concept.get('development', {}).get('dependencies', {}).get('external_dependencies', [])
    if external_deps:
        factors += 1
        # External dependencies increase timeline risk
        dep_risk = min(len(external_deps) * 15, 70)
        timeline_score += dep_risk
    
    # Time constraints
    time_constraints = [c for c in constraints.get('constraints', []) 
                       if c.get('category') == 'Time']
    if time_constraints:
        factors += 1
        constraint_risk = calculate_constraint_risk({'constraints': time_constraints})
        timeline_score += constraint_risk
    
    return timeline_score / max(factors, 1) if factors > 0 else 40.0

def calculate_competitive_risk(concept: Dict) -> float:
    """Calculate competitive threats and market dynamics risk"""
    competitive_score = 0.0
    factors = 0
    
    # Competitive advantages
    advantages = concept.get('positioning', {}).get('competitive_landscape', {}).get('competitive_advantages', [])
    factors += 1
    
    if not advantages:
        competitive_score += 80  # No clear advantages
    else:
        strong_advantages = sum(1 for adv in advantages if adv.get('strength') == 'Strong')
        if strong_advantages == 0:
            competitive_score += 60
        elif strong_advantages == 1:
            competitive_score += 40
        else:
            competitive_score += 20
    
    # Innovation level
    innovation = concept.get('attributes', {}).get('innovation_level', 'Incremental')
    factors += 1
    innovation_risk = {'Incremental': 30, 'Radical': 50, 'Disruptive': 70}.get(innovation, 40)
    competitive_score += innovation_risk
    
    return competitive_score / max(factors, 1) if factors > 0 else 50.0

def determine_risk_level(overall_score: float) -> str:
    """Determine risk level from overall score"""
    if overall_score >= 75:
        return "High Risk"
    elif overall_score >= 50:
        return "Medium Risk"
    elif overall_score >= 25:
        return "Low Risk"
    else:
        return "Very Low Risk"

def identify_top_risks(risk_scores: Dict, concept: Dict, assumptions: Dict, constraints: Dict) -> List[str]:
    """Identify the top risk areas"""
    risks = []
    
    # Check each category
    if risk_scores['technical_risk'] >= 70:
        risks.append("Technical implementation complexity")
    if risk_scores['market_risk'] >= 70:
        risks.append("Market uncertainty and competition")
    if risk_scores['resource_risk'] >= 70:
        risks.append("Resource constraints and availability")
    if risk_scores['timeline_risk'] >= 70:
        risks.append("Schedule and timeline pressure")
    if risk_scores['competitive_risk'] >= 70:
        risks.append("Competitive threats and differentiation")
    
    # Add assumption-based risks
    for assumption in assumptions.get('assumptions', []):
        if (assumption.get('risk', {}).get('impact_severity') in ['High', 'Critical'] and
            assumption.get('confidence', {}).get('confidence_level') == 'Low'):
            risks.append(f"Low confidence assumption: {assumption.get('statement', 'Unknown')[:50]}...")
    
    return risks[:5]  # Return top 5 risks

def identify_mitigation_priorities(risk_scores: Dict, top_risks: List[str]) -> List[str]:
    """Identify mitigation priorities based on risk analysis"""
    priorities = []
    
    if risk_scores['technical_risk'] >= 60:
        priorities.append("Conduct technical proof of concept")
        priorities.append("Validate core technology assumptions early")
    
    if risk_scores['market_risk'] >= 60:
        priorities.append("Conduct user research and market validation")
        priorities.append("Analyze competitive positioning")
    
    if risk_scores['resource_risk'] >= 60:
        priorities.append("Secure adequate resources and budget")
        priorities.append("Plan resource allocation carefully")
    
    if risk_scores['timeline_risk'] >= 60:
        priorities.append("Build buffer time into schedule")
        priorities.append("Identify and manage critical dependencies")
    
    if risk_scores['competitive_risk'] >= 60:
        priorities.append("Strengthen competitive differentiation")
        priorities.append("Monitor competitive landscape actively")
    
    return priorities[:5]  # Return top 5 priorities

def calculate_risk_score(concept_file: Path, constraints_file: Optional[Path] = None, 
                        assumptions_file: Optional[Path] = None) -> RiskScore:
    """Calculate comprehensive risk score"""
    
    # Load data files
    concept = load_yaml_file(concept_file)
    constraints = load_yaml_file(constraints_file) if constraints_file else {}
    assumptions = load_yaml_file(assumptions_file) if assumptions_file else {}
    
    # Calculate category risks
    technical_risk = calculate_technical_risk(concept, constraints)
    market_risk = calculate_market_risk(concept)
    resource_risk = calculate_resource_risk(concept, constraints)
    timeline_risk = calculate_timeline_risk(concept, constraints)
    competitive_risk = calculate_competitive_risk(concept)
    
    # Calculate overall risk (weighted average)
    weights = {
        'technical': 0.25,
        'market': 0.25,
        'resource': 0.20,
        'timeline': 0.15,
        'competitive': 0.15
    }
    
    overall_score = (
        technical_risk * weights['technical'] +
        market_risk * weights['market'] +
        resource_risk * weights['resource'] +
        timeline_risk * weights['timeline'] +
        competitive_risk * weights['competitive']
    )
    
    # Add assumption and constraint risk
    assumption_risk = calculate_assumption_risk(assumptions)
    constraint_risk = calculate_constraint_risk(constraints)
    
    # Adjust overall score based on assumptions and constraints
    overall_score = (overall_score * 0.8 + assumption_risk * 0.1 + constraint_risk * 0.1)
    
    risk_scores = {
        'technical_risk': technical_risk,
        'market_risk': market_risk,
        'resource_risk': resource_risk,
        'timeline_risk': timeline_risk,
        'competitive_risk': competitive_risk
    }
    
    # Prepare detailed breakdown
    category_details = {
        'technical': {
            'score': technical_risk,
            'factors': ['Technology readiness', 'Development complexity', 'Integration requirements']
        },
        'market': {
            'score': market_risk,
            'factors': ['Market maturity', 'Competition', 'Market size']
        },
        'resource': {
            'score': resource_risk,
            'factors': ['Timeline', 'Team size', 'Budget', 'Resource constraints']
        },
        'timeline': {
            'score': timeline_risk,
            'factors': ['Development phases', 'Dependencies', 'Time constraints']
        },
        'competitive': {
            'score': competitive_risk,
            'factors': ['Competitive advantages', 'Innovation level']
        }
    }
    
    risk_level = determine_risk_level(overall_score)
    top_risks = identify_top_risks(risk_scores, concept, assumptions, constraints)
    mitigation_priorities = identify_mitigation_priorities(risk_scores, top_risks)
    
    return RiskScore(
        overall_score=round(overall_score, 1),
        technical_risk=round(technical_risk, 1),
        market_risk=round(market_risk, 1),
        resource_risk=round(resource_risk, 1),
        timeline_risk=round(timeline_risk, 1),
        competitive_risk=round(competitive_risk, 1),
        category_details=category_details,
        risk_level=risk_level,
        top_risks=top_risks,
        mitigation_priorities=mitigation_priorities
    )

def generate_risk_report(risk_score: RiskScore, output_format: str = 'markdown') -> str:
    """Generate risk assessment report"""
    
    if output_format.lower() == 'markdown':
        report = f"""# Risk Assessment Report

## Overall Risk Score: {risk_score.overall_score}/100
**Risk Level**: {risk_score.risk_level}

## Risk Breakdown by Category

| Category | Score | Risk Level |
|----------|-------|------------|
| Technical | {risk_score.technical_risk}/100 | {'🔴 High' if risk_score.technical_risk >= 70 else '🟡 Medium' if risk_score.technical_risk >= 40 else '🟢 Low'} |
| Market | {risk_score.market_risk}/100 | {'🔴 High' if risk_score.market_risk >= 70 else '🟡 Medium' if risk_score.market_risk >= 40 else '🟢 Low'} |
| Resource | {risk_score.resource_risk}/100 | {'🔴 High' if risk_score.resource_risk >= 70 else '🟡 Medium' if risk_score.resource_risk >= 40 else '🟢 Low'} |
| Timeline | {risk_score.timeline_risk}/100 | {'🔴 High' if risk_score.timeline_risk >= 70 else '🟡 Medium' if risk_score.timeline_risk >= 40 else '🟢 Low'} |
| Competitive | {risk_score.competitive_risk}/100 | {'🔴 High' if risk_score.competitive_risk >= 70 else '🟡 Medium' if risk_score.competitive_risk >= 40 else '🟢 Low'} |

## Top Risk Areas
"""
        for i, risk in enumerate(risk_score.top_risks, 1):
            report += f"{i}. {risk}\n"
        
        report += "\n## Recommended Mitigation Priorities\n"
        for i, priority in enumerate(risk_score.mitigation_priorities, 1):
            report += f"{i}. {priority}\n"
        
        report += f"\n## Risk Assessment Details\n"
        for category, details in risk_score.category_details.items():
            report += f"\n### {category.title()} Risk ({details['score']}/100)\n"
            report += f"**Factors assessed**: {', '.join(details['factors'])}\n"
        
        return report
    
    elif output_format.lower() == 'json':
        return json.dumps({
            'overall_score': risk_score.overall_score,
            'risk_level': risk_score.risk_level,
            'category_scores': {
                'technical': risk_score.technical_risk,
                'market': risk_score.market_risk,
                'resource': risk_score.resource_risk,
                'timeline': risk_score.timeline_risk,
                'competitive': risk_score.competitive_risk
            },
            'top_risks': risk_score.top_risks,
            'mitigation_priorities': risk_score.mitigation_priorities,
            'category_details': risk_score.category_details
        }, indent=2)
    
    else:
        return f"Risk Score: {risk_score.overall_score}/100 ({risk_score.risk_level})"

def main():
    parser = argparse.ArgumentParser(description='Calculate comprehensive risk scores for design concepts')
    parser.add_argument('concept_file', type=str, help='Path to concept YAML file')
    parser.add_argument('--constraints', type=str, help='Path to constraints YAML file')
    parser.add_argument('--assumptions', type=str, help='Path to assumptions YAML file')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--format', choices=['markdown', 'json', 'summary'], default='markdown',
                       help='Output format')
    
    args = parser.parse_args()
    
    try:
        concept_path = Path(args.concept_file)
        constraints_path = Path(args.constraints) if args.constraints else None
        assumptions_path = Path(args.assumptions) if args.assumptions else None
        
        if not concept_path.exists():
            print(f"❌ Error: Concept file {concept_path} not found")
            sys.exit(1)
        
        # Calculate risk score
        risk_score = calculate_risk_score(concept_path, constraints_path, assumptions_path)
        
        # Generate report
        report = generate_risk_report(risk_score, args.format)
        
        # Output report
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"✅ Risk assessment written to: {args.output}")
        else:
            print(report)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()