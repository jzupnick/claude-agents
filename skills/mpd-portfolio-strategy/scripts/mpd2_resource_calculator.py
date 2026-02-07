#!/usr/bin/env python3
"""
MPD2 Resource Calculator Tool

Calculates resource requirements for product development projects based on 
Northwestern MPD2 methodologies including timeline, team, and budget estimation.
"""

import json
import argparse
import sys
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
from pathlib import Path
import math

@dataclass
class ProjectScope:
    """Project scope and complexity assessment"""
    complexity_level: str  # Low, Medium, High
    technology_novelty: str  # Incremental, Moderate, Breakthrough
    market_uncertainty: str  # Low, Medium, High
    regulatory_requirements: bool
    manufacturing_complexity: str  # Low, Medium, High
    team_distribution: str  # Co-located, Distributed, Global

@dataclass
class ResourceEstimate:
    """Resource estimation results"""
    development_weeks: int
    team_size: int
    budget_usd: int
    risk_buffer_percent: int
    confidence_level: str

class MPD2ResourceCalculator:
    """Northwestern MPD2-based resource calculation engine"""
    
    # Base estimates for different complexity levels (person-weeks)
    BASE_EFFORT = {
        "Low": 40,
        "Medium": 80, 
        "High": 160
    }
    
    # Multipliers for various factors
    TECHNOLOGY_MULTIPLIERS = {
        "Incremental": 1.0,
        "Moderate": 1.5,
        "Breakthrough": 2.5
    }
    
    MARKET_MULTIPLIERS = {
        "Low": 1.0,
        "Medium": 1.2,
        "High": 1.5
    }
    
    MANUFACTURING_MULTIPLIERS = {
        "Low": 1.0,
        "Medium": 1.3,
        "High": 1.8
    }
    
    DISTRIBUTION_MULTIPLIERS = {
        "Co-located": 1.0,
        "Distributed": 1.2,
        "Global": 1.5
    }
    
    # Cost per person-week by role (USD)
    ROLE_COSTS = {
        "product_manager": 3000,
        "designer": 2500,
        "engineer": 2800,
        "researcher": 2200,
        "manufacturing": 2400,
        "quality": 2300
    }
    
    def calculate_effort(self, scope: ProjectScope) -> int:
        """Calculate total effort in person-weeks"""
        base_effort = self.BASE_EFFORT[scope.complexity_level]
        
        # Apply multipliers
        effort = base_effort
        effort *= self.TECHNOLOGY_MULTIPLIERS[scope.technology_novelty]
        effort *= self.MARKET_MULTIPLIERS[scope.market_uncertainty]
        effort *= self.MANUFACTURING_MULTIPLIERS[scope.manufacturing_complexity]
        effort *= self.DISTRIBUTION_MULTIPLIERS[scope.team_distribution]
        
        # Add regulatory overhead
        if scope.regulatory_requirements:
            effort *= 1.4
            
        return int(math.ceil(effort))
    
    def calculate_team_composition(self, scope: ProjectScope, total_effort: int) -> Dict[str, int]:
        """Calculate team composition based on project scope"""
        team = {}
        
        # Base team composition percentages
        if scope.complexity_level == "Low":
            team["product_manager"] = 0.15
            team["designer"] = 0.25
            team["engineer"] = 0.45
            team["researcher"] = 0.05
            team["manufacturing"] = 0.05
            team["quality"] = 0.05
        elif scope.complexity_level == "Medium":
            team["product_manager"] = 0.12
            team["designer"] = 0.20
            team["engineer"] = 0.45
            team["researcher"] = 0.08
            team["manufacturing"] = 0.10
            team["quality"] = 0.05
        else:  # High complexity
            team["product_manager"] = 0.10
            team["designer"] = 0.15
            team["engineer"] = 0.50
            team["researcher"] = 0.10
            team["manufacturing"] = 0.10
            team["quality"] = 0.05
            
        # Adjust for technology novelty
        if scope.technology_novelty == "Breakthrough":
            team["researcher"] += 0.05
            team["engineer"] -= 0.05
            
        # Adjust for regulatory requirements
        if scope.regulatory_requirements:
            team["quality"] += 0.05
            team["engineer"] -= 0.05
            
        # Convert to person counts
        for role in team:
            team[role] = max(1, int(math.ceil(team[role] * total_effort / 12)))  # Assuming 12 weeks average
            
        return team
    
    def calculate_budget(self, team_composition: Dict[str, int], duration_weeks: int) -> int:
        """Calculate project budget based on team and duration"""
        total_cost = 0
        
        for role, count in team_composition.items():
            role_cost = self.ROLE_COSTS.get(role, 2500)  # Default cost
            total_cost += count * duration_weeks * role_cost
            
        return int(total_cost)
    
    def calculate_risk_buffer(self, scope: ProjectScope) -> int:
        """Calculate risk buffer percentage"""
        buffer = 10  # Base buffer
        
        if scope.technology_novelty == "Breakthrough":
            buffer += 20
        elif scope.technology_novelty == "Moderate":
            buffer += 10
            
        if scope.market_uncertainty == "High":
            buffer += 15
        elif scope.market_uncertainty == "Medium":
            buffer += 8
            
        if scope.manufacturing_complexity == "High":
            buffer += 12
        elif scope.manufacturing_complexity == "Medium":
            buffer += 6
            
        if scope.team_distribution == "Global":
            buffer += 10
        elif scope.team_distribution == "Distributed":
            buffer += 5
            
        if scope.regulatory_requirements:
            buffer += 15
            
        return min(buffer, 60)  # Cap at 60%
    
    def estimate_resources(self, scope: ProjectScope) -> ResourceEstimate:
        """Main estimation function"""
        # Calculate effort
        total_effort = self.calculate_effort(scope)
        
        # Calculate team composition
        team_comp = self.calculate_team_composition(scope, total_effort)
        team_size = sum(team_comp.values())
        
        # Calculate duration (assuming parallel work)
        duration_weeks = int(math.ceil(total_effort / team_size))
        
        # Calculate budget
        budget = self.calculate_budget(team_comp, duration_weeks)
        
        # Calculate risk buffer
        risk_buffer = self.calculate_risk_buffer(scope)
        
        # Apply risk buffer to timeline and budget
        duration_with_buffer = int(math.ceil(duration_weeks * (1 + risk_buffer / 100)))
        budget_with_buffer = int(budget * (1 + risk_buffer / 100))
        
        # Determine confidence level
        if risk_buffer <= 20:
            confidence = "High"
        elif risk_buffer <= 35:
            confidence = "Medium"
        else:
            confidence = "Low"
        
        return ResourceEstimate(
            development_weeks=duration_with_buffer,
            team_size=team_size,
            budget_usd=budget_with_buffer,
            risk_buffer_percent=risk_buffer,
            confidence_level=confidence
        )

def generate_report(scope: ProjectScope, estimate: ResourceEstimate, team_comp: Dict[str, int]) -> str:
    """Generate detailed resource estimation report"""
    
    report = f"""# MPD2 Resource Estimation Report

## Project Scope Assessment
- **Complexity Level**: {scope.complexity_level}
- **Technology Novelty**: {scope.technology_novelty}
- **Market Uncertainty**: {scope.market_uncertainty}
- **Regulatory Requirements**: {'Yes' if scope.regulatory_requirements else 'No'}
- **Manufacturing Complexity**: {scope.manufacturing_complexity}
- **Team Distribution**: {scope.team_distribution}

## Resource Estimates

### Timeline
- **Development Duration**: {estimate.development_weeks} weeks
- **Risk Buffer Applied**: {estimate.risk_buffer_percent}%
- **Estimation Confidence**: {estimate.confidence_level}

### Team Requirements
- **Total Team Size**: {estimate.team_size} people

#### Team Composition:
"""
    
    for role, count in team_comp.items():
        role_display = role.replace('_', ' ').title()
        report += f"- **{role_display}**: {count} person(s)\n"
    
    report += f"""
### Budget
- **Total Project Cost**: ${estimate.budget_usd:,} USD
- **Weekly Burn Rate**: ${estimate.budget_usd // estimate.development_weeks:,} USD/week

## Risk Assessment
Risk Buffer: {estimate.risk_buffer_percent}% - {estimate.confidence_level} Confidence

### Key Risk Factors:
"""
    
    if scope.technology_novelty == "Breakthrough":
        report += "- High technology risk due to breakthrough innovation\n"
    if scope.market_uncertainty == "High":
        report += "- Significant market uncertainty affecting requirements\n"
    if scope.manufacturing_complexity == "High":
        report += "- Complex manufacturing requirements\n"
    if scope.team_distribution == "Global":
        report += "- Global team coordination challenges\n"
    if scope.regulatory_requirements:
        report += "- Regulatory compliance requirements\n"
    
    report += """
## Recommendations
1. **Phase Gate Reviews**: Implement stage-gate process with regular checkpoints
2. **Risk Mitigation**: Focus on highest risk factors identified above
3. **Resource Planning**: Secure team members early, especially specialized roles
4. **Timeline Management**: Build in flexibility for high-uncertainty phases

---
*Generated by MPD2 Resource Calculator*
"""
    
    return report

def main():
    parser = argparse.ArgumentParser(description='Calculate MPD2-based resource estimates')
    parser.add_argument('--complexity', choices=['Low', 'Medium', 'High'], required=True,
                      help='Project complexity level')
    parser.add_argument('--technology', choices=['Incremental', 'Moderate', 'Breakthrough'], 
                      required=True, help='Technology novelty level')
    parser.add_argument('--market', choices=['Low', 'Medium', 'High'], required=True,
                      help='Market uncertainty level')
    parser.add_argument('--manufacturing', choices=['Low', 'Medium', 'High'], required=True,
                      help='Manufacturing complexity level')
    parser.add_argument('--distribution', choices=['Co-located', 'Distributed', 'Global'], 
                      required=True, help='Team distribution')
    parser.add_argument('--regulatory', action='store_true', 
                      help='Project has regulatory requirements')
    parser.add_argument('--output', type=str, help='Output file for report')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    
    args = parser.parse_args()
    
    # Create project scope
    scope = ProjectScope(
        complexity_level=args.complexity,
        technology_novelty=args.technology,
        market_uncertainty=args.market,
        regulatory_requirements=args.regulatory,
        manufacturing_complexity=args.manufacturing,
        team_distribution=args.distribution
    )
    
    # Calculate estimates
    calculator = MPD2ResourceCalculator()
    estimate = calculator.estimate_resources(scope)
    team_comp = calculator.calculate_team_composition(scope, calculator.calculate_effort(scope))
    
    if args.json:
        # Output JSON format
        result = {
            "scope": asdict(scope),
            "estimate": asdict(estimate),
            "team_composition": team_comp
        }
        output = json.dumps(result, indent=2)
    else:
        # Output markdown report
        output = generate_report(scope, estimate, team_comp)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Resource estimation report written to: {args.output}")
    else:
        print(output)

if __name__ == "__main__":
    main()