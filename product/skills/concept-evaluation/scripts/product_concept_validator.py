#!/usr/bin/env python3
"""
Product Concept Validator Tool

Validates product concepts against Northwestern MPD2 criteria including:
- Market opportunity assessment
- Technical feasibility analysis
- Manufacturing considerations
- Resource requirements evaluation
"""

import json
import sys
import argparse
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
from pathlib import Path

@dataclass
class MarketCriteria:
    """Market opportunity assessment criteria"""
    target_market_size: Optional[int] = None
    market_growth_rate: Optional[float] = None
    competitive_landscape: Optional[str] = None
    value_proposition_clarity: Optional[int] = None  # 1-10 scale

@dataclass 
class TechnicalCriteria:
    """Technical feasibility assessment criteria"""
    technology_readiness_level: Optional[int] = None  # 1-9 TRL scale
    development_complexity: Optional[str] = None  # Low/Medium/High
    integration_requirements: Optional[List[str]] = None
    performance_requirements: Optional[Dict[str, str]] = None

@dataclass
class ManufacturingCriteria:
    """Manufacturing feasibility criteria"""
    manufacturing_process: Optional[str] = None
    material_availability: Optional[str] = None
    tooling_requirements: Optional[str] = None
    scalability_assessment: Optional[str] = None

@dataclass
class ResourceCriteria:
    """Resource requirements assessment"""
    development_timeline_weeks: Optional[int] = None
    team_size_required: Optional[int] = None
    budget_estimate_usd: Optional[int] = None
    expertise_required: Optional[List[str]] = None

@dataclass
class ProductConcept:
    """Complete product concept with validation criteria"""
    name: str
    description: str
    market: MarketCriteria
    technical: TechnicalCriteria
    manufacturing: ManufacturingCriteria
    resources: ResourceCriteria
    
    def calculate_feasibility_score(self) -> Dict[str, float]:
        """Calculate feasibility scores across dimensions"""
        scores = {}
        
        # Market feasibility (0-100)
        market_score = 0
        if self.market.target_market_size:
            market_score += min(self.market.target_market_size / 1000000, 25)  # Up to 25 points for 1M+ market
        if self.market.market_growth_rate:
            market_score += min(self.market.market_growth_rate * 10, 25)  # Up to 25 points for 2.5%+ growth
        if self.market.value_proposition_clarity:
            market_score += self.market.value_proposition_clarity * 5  # Up to 50 points for clarity
        scores['market'] = min(market_score, 100)
        
        # Technical feasibility (0-100)
        technical_score = 0
        if self.technical.technology_readiness_level:
            technical_score += self.technical.technology_readiness_level * 10  # Up to 90 points for TRL 9
        if self.technical.development_complexity == "Low":
            technical_score += 10
        elif self.technical.development_complexity == "Medium":
            technical_score += 5
        scores['technical'] = min(technical_score, 100)
        
        # Manufacturing feasibility (0-100) 
        manufacturing_score = 50  # Base score
        if self.manufacturing.material_availability == "High":
            manufacturing_score += 25
        elif self.manufacturing.material_availability == "Medium":
            manufacturing_score += 10
        if self.manufacturing.scalability_assessment == "High":
            manufacturing_score += 25
        elif self.manufacturing.scalability_assessment == "Medium":
            manufacturing_score += 10
        scores['manufacturing'] = min(manufacturing_score, 100)
        
        # Resource feasibility (0-100)
        resource_score = 50  # Base score
        if self.resources.development_timeline_weeks and self.resources.development_timeline_weeks <= 12:
            resource_score += 25
        elif self.resources.development_timeline_weeks and self.resources.development_timeline_weeks <= 24:
            resource_score += 15
        if self.resources.team_size_required and self.resources.team_size_required <= 5:
            resource_score += 25
        elif self.resources.team_size_required and self.resources.team_size_required <= 10:
            resource_score += 15
        scores['resources'] = min(resource_score, 100)
        
        # Overall feasibility
        scores['overall'] = sum(scores.values()) / len(scores)
        
        return scores

def load_concept_from_file(file_path: Path) -> ProductConcept:
    """Load product concept from JSON file"""
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    return ProductConcept(
        name=data['name'],
        description=data['description'],
        market=MarketCriteria(**data.get('market', {})),
        technical=TechnicalCriteria(**data.get('technical', {})),
        manufacturing=ManufacturingCriteria(**data.get('manufacturing', {})),
        resources=ResourceCriteria(**data.get('resources', {}))
    )

def generate_validation_report(concept: ProductConcept) -> str:
    """Generate detailed validation report"""
    scores = concept.calculate_feasibility_score()
    
    report = f"""
# Product Concept Validation Report

## Concept Overview
**Name**: {concept.name}
**Description**: {concept.description}

## Feasibility Assessment

### Overall Feasibility Score: {scores['overall']:.1f}/100

| Dimension | Score | Status |
|-----------|-------|---------|
| Market | {scores['market']:.1f}/100 | {'✅ Strong' if scores['market'] >= 70 else '⚠️ Moderate' if scores['market'] >= 50 else '❌ Weak'} |
| Technical | {scores['technical']:.1f}/100 | {'✅ Strong' if scores['technical'] >= 70 else '⚠️ Moderate' if scores['technical'] >= 50 else '❌ Weak'} |
| Manufacturing | {scores['manufacturing']:.1f}/100 | {'✅ Strong' if scores['manufacturing'] >= 70 else '⚠️ Moderate' if scores['manufacturing'] >= 50 else '❌ Weak'} |
| Resources | {scores['resources']:.1f}/100 | {'✅ Strong' if scores['resources'] >= 70 else '⚠️ Moderate' if scores['resources'] >= 50 else '❌ Weak'} |

## Recommendations

"""
    
    if scores['overall'] >= 70:
        report += "**🟢 GO Decision**: Strong feasibility across dimensions. Recommended for development.\n\n"
    elif scores['overall'] >= 50:
        report += "**🟡 CONDITIONAL GO**: Moderate feasibility. Address weak areas before proceeding.\n\n"
    else:
        report += "**🔴 NO-GO**: Weak feasibility. Significant changes needed or consider alternative concepts.\n\n"
    
    # Specific recommendations
    if scores['market'] < 50:
        report += "- **Market Risk**: Clarify value proposition and validate market opportunity\n"
    if scores['technical'] < 50:
        report += "- **Technical Risk**: Reduce complexity or advance technology readiness\n"
    if scores['manufacturing'] < 50:
        report += "- **Manufacturing Risk**: Assess material availability and production scalability\n"
    if scores['resources'] < 50:
        report += "- **Resource Risk**: Optimize timeline and team requirements\n"
    
    return report

def create_example_concept() -> ProductConcept:
    """Create example product concept for demonstration"""
    return ProductConcept(
        name="Smart Emergency Safety Device",
        description="Wearable device for emergency alert and location tracking",
        market=MarketCriteria(
            target_market_size=2000000,
            market_growth_rate=0.15,
            competitive_landscape="Moderate competition with opportunity for differentiation",
            value_proposition_clarity=8
        ),
        technical=TechnicalCriteria(
            technology_readiness_level=7,
            development_complexity="Medium",
            integration_requirements=["iOS SDK", "GPS", "Cellular connectivity"],
            performance_requirements={"battery_life": "7 days", "alert_time": "< 2 seconds"}
        ),
        manufacturing=ManufacturingCriteria(
            manufacturing_process="Electronics assembly",
            material_availability="High",
            tooling_requirements="Moderate",
            scalability_assessment="High"
        ),
        resources=ResourceCriteria(
            development_timeline_weeks=16,
            team_size_required=6,
            budget_estimate_usd=750000,
            expertise_required=["iOS development", "hardware design", "compliance"]
        )
    )

def main():
    parser = argparse.ArgumentParser(description='Validate product concepts using MPD2 criteria')
    parser.add_argument('--concept-file', type=str, help='JSON file containing product concept')
    parser.add_argument('--create-example', action='store_true', help='Create example concept file')
    parser.add_argument('--output', type=str, help='Output file for validation report')
    
    args = parser.parse_args()
    
    if args.create_example:
        example = create_example_concept()
        example_file = Path('example_concept.json')
        with open(example_file, 'w') as f:
            json.dump(asdict(example), f, indent=2)
        print(f"✅ Created example concept file: {example_file}")
        return
    
    if not args.concept_file:
        print("❌ Error: Must provide --concept-file or use --create-example")
        sys.exit(1)
    
    try:
        concept = load_concept_from_file(Path(args.concept_file))
        report = generate_validation_report(concept)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"✅ Validation report written to: {args.output}")
        else:
            print(report)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()