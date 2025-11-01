#!/usr/bin/env python3
"""
Trade-off Matrix Generator

Generates comprehensive trade-off analysis matrices showing concepts scored across multiple criteria.
Produces both markdown tables and visualizations for decision-making.

Input: concepts.yaml + criteria.yaml
Output: Markdown table + visualization + analysis
"""

import yaml
import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

@dataclass
class TradeOffAnalysis:
    """Complete trade-off analysis with scoring and insights"""
    scored_matrix: pd.DataFrame
    weighted_scores: pd.DataFrame
    rankings: List[Tuple[str, float]]
    sensitivity_analysis: Dict
    trade_off_insights: List[str]
    visualization_path: Optional[str] = None

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

def score_concept_against_criteria(concept: Dict, criteria: Dict) -> float:
    """Score a single concept against a single criteria"""
    criteria_name = criteria.get('name', '')
    scoring_method = criteria.get('scoring', {}).get('scoring_method', 'Qualitative')
    
    # Get concept data relevant to this criteria
    concept_data = extract_relevant_concept_data(concept, criteria)
    
    if scoring_method == 'Quantitative':
        return score_quantitative_criteria(concept_data, criteria)
    elif scoring_method == 'Qualitative':
        return score_qualitative_criteria(concept_data, criteria)
    else:
        return score_mixed_criteria(concept_data, criteria)

def extract_relevant_concept_data(concept: Dict, criteria: Dict) -> Dict:
    """Extract concept data relevant to the criteria being scored"""
    category = criteria.get('category', '').lower()
    criteria_name = criteria.get('name', '').lower()
    
    # Map criteria categories to concept data sections
    if category == 'market':
        return {
            'market_size': concept.get('positioning', {}).get('target_market', {}).get('segment_size'),
            'growth_rate': concept.get('positioning', {}).get('target_market', {}).get('growth_rate'),
            'competition': concept.get('positioning', {}).get('competitive_landscape', {}),
            'maturity': concept.get('positioning', {}).get('market_maturity')
        }
    elif category == 'technical':
        return {
            'complexity': concept.get('attributes', {}).get('complexity'),
            'trl': concept.get('technical', {}).get('technology_readiness_level'),
            'performance': concept.get('technical', {}).get('performance_requirements', []),
            'integrations': concept.get('technical', {}).get('integration_points', [])
        }
    elif category == 'business':
        return {
            'revenue_model': concept.get('business_model', {}),
            'cost_structure': concept.get('business_model', {}).get('cost_structure'),
            'pricing': concept.get('positioning', {}).get('pricing_strategy', {})
        }
    elif category == 'user':
        return {
            'value_proposition': concept.get('core_value_proposition', {}),
            'user_segment': concept.get('core_value_proposition', {}).get('target_user_segment'),
            'job_to_be_done': concept.get('core_value_proposition', {}).get('job_to_be_done')
        }
    elif category == 'risk':
        return {
            'risks': concept.get('risks', {}),
            'assumptions': concept.get('validation', {}).get('assumptions', [])
        }
    else:
        # Return full concept for flexible scoring
        return concept

def score_quantitative_criteria(concept_data: Dict, criteria: Dict) -> float:
    """Score concept using quantitative criteria"""
    scale_range = criteria.get('scoring', {}).get('scale_range', {})
    minimum = scale_range.get('minimum', 0)
    maximum = scale_range.get('maximum', 100)
    
    criteria_name = criteria.get('name', '').lower()
    
    # Market size scoring
    if 'market size' in criteria_name:
        market_size = concept_data.get('market_size', 0)
        if market_size == 0:
            return minimum
        
        # Log scale for market size
        log_size = np.log10(max(market_size, 1))
        # Assume 10K = 0, 10M = 100 scale
        normalized = (log_size - 4) / (7 - 4) * (maximum - minimum) + minimum
        return max(minimum, min(maximum, normalized))
    
    # Growth rate scoring
    elif 'growth' in criteria_name:
        growth_rate = concept_data.get('growth_rate', 0)
        # 0% = minimum, 20% = maximum
        normalized = (growth_rate / 0.20) * (maximum - minimum) + minimum
        return max(minimum, min(maximum, normalized))
    
    # Technology readiness scoring
    elif 'technology' in criteria_name or 'trl' in criteria_name:
        trl = concept_data.get('trl', 1)
        # TRL 1 = minimum, TRL 9 = maximum
        normalized = ((trl - 1) / 8) * (maximum - minimum) + minimum
        return max(minimum, min(maximum, normalized))
    
    # Default quantitative scoring
    else:
        return (minimum + maximum) / 2  # Middle score if can't determine

def score_qualitative_criteria(concept_data: Dict, criteria: Dict) -> float:
    """Score concept using qualitative criteria"""
    rating_levels = criteria.get('qualitative_scoring', {}).get('rating_levels', [])
    
    if not rating_levels:
        # Create default rating levels
        rating_levels = [
            {'level': 'Poor', 'score': 20},
            {'level': 'Fair', 'score': 40},
            {'level': 'Good', 'score': 60},
            {'level': 'Very Good', 'score': 80},
            {'level': 'Excellent', 'score': 100}
        ]
    
    criteria_name = criteria.get('name', '').lower()
    category = criteria.get('category', '').lower()
    
    # Market criteria scoring
    if category == 'market':
        if 'competitive advantage' in criteria_name:
            advantages = concept_data.get('competition', {}).get('competitive_advantages', [])
            strong_advantages = sum(1 for adv in advantages if adv.get('strength') == 'Strong')
            
            if strong_advantages >= 2:
                return 90  # Excellent
            elif strong_advantages == 1:
                return 70  # Very Good
            elif len(advantages) > 0:
                return 50  # Good
            else:
                return 25  # Poor
    
    # Technical criteria scoring
    elif category == 'technical':
        if 'complexity' in criteria_name:
            complexity = concept_data.get('complexity', 'Medium')
            complexity_scores = {'Low': 85, 'Medium': 60, 'High': 35}
            return complexity_scores.get(complexity, 60)
        
        elif 'integration' in criteria_name:
            integrations = concept_data.get('integrations', [])
            if len(integrations) == 0:
                return 90  # Excellent - no integration complexity
            elif len(integrations) <= 2:
                return 70  # Very Good
            elif len(integrations) <= 4:
                return 50  # Good
            else:
                return 30  # Poor - high integration complexity
    
    # User criteria scoring
    elif category == 'user':
        if 'value proposition' in criteria_name:
            value_prop = concept_data.get('value_proposition', {})
            completeness = sum(1 for key in ['primary_benefit', 'target_user_segment', 'job_to_be_done', 'differentiation']
                             if value_prop.get(key))
            
            if completeness == 4:
                return 90  # Excellent
            elif completeness == 3:
                return 70  # Very Good
            elif completeness == 2:
                return 50  # Good
            elif completeness == 1:
                return 30  # Fair
            else:
                return 15  # Poor
    
    # Default qualitative scoring - return middle value
    return sum(level['score'] for level in rating_levels) / len(rating_levels)

def score_mixed_criteria(concept_data: Dict, criteria: Dict) -> float:
    """Score concept using mixed quantitative and qualitative criteria"""
    # For mixed criteria, use a combination approach
    quant_score = score_quantitative_criteria(concept_data, criteria)
    qual_score = score_qualitative_criteria(concept_data, criteria)
    
    # Weight equally unless specified otherwise
    return (quant_score + qual_score) / 2

def calculate_weighted_scores(scored_matrix: pd.DataFrame, criteria_weights: Dict[str, float]) -> pd.DataFrame:
    """Calculate weighted scores for each concept"""
    weighted_matrix = scored_matrix.copy()
    
    for criteria_name, weight in criteria_weights.items():
        if criteria_name in weighted_matrix.columns:
            weighted_matrix[criteria_name] = weighted_matrix[criteria_name] * weight
    
    # Add total weighted score column
    weighted_matrix['Total Score'] = weighted_matrix.sum(axis=1)
    
    return weighted_matrix

def perform_sensitivity_analysis(scored_matrix: pd.DataFrame, criteria_weights: Dict[str, float]) -> Dict:
    """Perform sensitivity analysis on criteria weights"""
    sensitivity_results = {}
    base_weighted = calculate_weighted_scores(scored_matrix, criteria_weights)
    base_ranking = base_weighted['Total Score'].rank(ascending=False)
    
    # Test impact of changing each criteria weight by ±20%
    for criteria_name in criteria_weights.keys():
        if criteria_name not in scored_matrix.columns:
            continue
            
        # Increase weight by 20%
        modified_weights = criteria_weights.copy()
        modified_weights[criteria_name] *= 1.2
        
        # Normalize weights to maintain total
        total_weight = sum(modified_weights.values())
        modified_weights = {k: v/total_weight for k, v in modified_weights.items()}
        
        modified_weighted = calculate_weighted_scores(scored_matrix, modified_weights)
        modified_ranking = modified_weighted['Total Score'].rank(ascending=False)
        
        # Calculate ranking changes
        ranking_changes = abs(base_ranking - modified_ranking).sum()
        
        sensitivity_results[criteria_name] = {
            'ranking_sensitivity': ranking_changes,
            'weight_impact': 'High' if ranking_changes > 2 else 'Medium' if ranking_changes > 1 else 'Low'
        }
    
    return sensitivity_results

def identify_trade_off_insights(scored_matrix: pd.DataFrame, weighted_scores: pd.DataFrame) -> List[str]:
    """Identify key trade-offs and insights from the analysis"""
    insights = []
    
    # Find concepts that excel in different areas
    concepts = scored_matrix.index.tolist()
    criteria = scored_matrix.columns.tolist()
    
    # Identify top performer in each criteria
    for criteria_name in criteria:
        top_concept = scored_matrix[criteria_name].idxmax()
        top_score = scored_matrix[criteria_name].max()
        
        # Check if this top performer is also the overall winner
        overall_winner = weighted_scores['Total Score'].idxmax()
        
        if top_concept != overall_winner and top_score > 70:
            insights.append(f"{top_concept} excels in {criteria_name} ({top_score:.1f}) but ranks lower overall")
    
    # Identify balanced vs specialized concepts
    for concept in concepts:
        concept_scores = scored_matrix.loc[concept]
        score_std = concept_scores.std()
        score_mean = concept_scores.mean()
        
        if score_std < 15 and score_mean > 60:
            insights.append(f"{concept} shows balanced performance across all criteria")
        elif score_std > 25:
            high_areas = concept_scores[concept_scores > score_mean + score_std].index.tolist()
            if high_areas:
                insights.append(f"{concept} is specialized in {', '.join(high_areas)}")
    
    # Identify close competitions
    total_scores = weighted_scores['Total Score'].sort_values(ascending=False)
    for i in range(len(total_scores) - 1):
        score_diff = total_scores.iloc[i] - total_scores.iloc[i + 1]
        if score_diff < 5:  # Very close scores
            insights.append(f"Close competition between {total_scores.index[i]} and {total_scores.index[i + 1]} "
                          f"({score_diff:.1f} point difference)")
    
    return insights[:5]  # Return top 5 insights

def create_visualization(scored_matrix: pd.DataFrame, weighted_scores: pd.DataFrame, 
                        output_path: Path) -> str:
    """Create trade-off matrix visualization"""
    # Set up the plot
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Heatmap of raw scores
    sns.heatmap(scored_matrix, annot=True, fmt='.1f', cmap='RdYlGn', ax=ax1, cbar_kws={'label': 'Score'})
    ax1.set_title('Concept Scoring Matrix', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Criteria')
    ax1.set_ylabel('Concepts')
    
    # 2. Bar chart of total weighted scores
    total_scores = weighted_scores['Total Score'].sort_values(ascending=True)
    ax2.barh(range(len(total_scores)), total_scores.values, color='skyblue')
    ax2.set_yticks(range(len(total_scores)))
    ax2.set_yticklabels(total_scores.index)
    ax2.set_xlabel('Weighted Total Score')
    ax2.set_title('Overall Ranking', fontsize=14, fontweight='bold')
    
    # Add score labels on bars
    for i, v in enumerate(total_scores.values):
        ax2.text(v + 1, i, f'{v:.1f}', va='center')
    
    # 3. Radar chart for top 3 concepts
    top_3_concepts = weighted_scores['Total Score'].nlargest(3).index.tolist()
    criteria_names = scored_matrix.columns.tolist()
    
    # Set up radar chart
    angles = np.linspace(0, 2 * np.pi, len(criteria_names), endpoint=False).tolist()
    angles += angles[:1]  # Complete the circle
    
    ax3 = plt.subplot(2, 2, 3, projection='polar')
    
    colors = ['red', 'blue', 'green']
    for i, concept in enumerate(top_3_concepts):
        values = scored_matrix.loc[concept].tolist()
        values += values[:1]  # Complete the circle
        
        ax3.plot(angles, values, color=colors[i], linewidth=2, label=concept)
        ax3.fill(angles, values, color=colors[i], alpha=0.25)
    
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(criteria_names)
    ax3.set_ylim(0, 100)
    ax3.set_title('Top 3 Concepts Comparison', fontsize=14, fontweight='bold')
    ax3.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    # 4. Criteria importance vs discrimination chart
    criteria_weights = {col: 1/len(scored_matrix.columns) for col in scored_matrix.columns}  # Equal weights for visualization
    discrimination = scored_matrix.std()  # How much each criteria differentiates concepts
    importance = pd.Series(criteria_weights)
    
    ax4.scatter(importance, discrimination, s=100, alpha=0.7)
    for i, criteria in enumerate(criteria_names):
        ax4.annotate(criteria, (importance[criteria], discrimination[criteria]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    ax4.set_xlabel('Criteria Weight/Importance')
    ax4.set_ylabel('Score Discrimination (Std Dev)')
    ax4.set_title('Criteria Importance vs Discrimination', fontsize=14, fontweight='bold')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save the plot
    viz_path = output_path / 'trade_off_matrix.png'
    plt.savefig(viz_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return str(viz_path)

def generate_trade_off_matrix(concepts_file: Path, criteria_file: Path, 
                             output_dir: Optional[Path] = None) -> TradeOffAnalysis:
    """Generate comprehensive trade-off matrix analysis"""
    
    # Load data
    concepts_data = load_yaml_file(concepts_file)
    criteria_data = load_yaml_file(criteria_file)
    
    # Extract concepts and criteria lists
    concepts = concepts_data.get('concepts', [])
    criteria_list = criteria_data.get('criteria', [])
    
    if not concepts or not criteria_list:
        raise ValueError("No concepts or criteria found in input files")
    
    # Create scoring matrix
    concept_names = [c.get('name', f'Concept {i}') for i, c in enumerate(concepts)]
    criteria_names = [c.get('name', f'Criteria {i}') for i, c in enumerate(criteria_list)]
    
    # Score each concept against each criteria
    scoring_data = []
    for concept in concepts:
        concept_scores = []
        for criteria in criteria_list:
            score = score_concept_against_criteria(concept, criteria)
            concept_scores.append(score)
        scoring_data.append(concept_scores)
    
    # Create DataFrame
    scored_matrix = pd.DataFrame(scoring_data, 
                                index=concept_names,
                                columns=criteria_names)
    
    # Calculate criteria weights
    criteria_weights = {}
    for criteria in criteria_list:
        weight = criteria.get('weighting', {}).get('weight', 1.0)
        criteria_weights[criteria.get('name')] = weight
    
    # Normalize weights
    total_weight = sum(criteria_weights.values())
    criteria_weights = {k: v/total_weight for k, v in criteria_weights.items()}
    
    # Calculate weighted scores
    weighted_scores = calculate_weighted_scores(scored_matrix, criteria_weights)
    
    # Create rankings
    rankings = [(concept, score) for concept, score in 
               weighted_scores['Total Score'].sort_values(ascending=False).items()]
    
    # Perform sensitivity analysis
    sensitivity_analysis = perform_sensitivity_analysis(scored_matrix, criteria_weights)
    
    # Identify insights
    trade_off_insights = identify_trade_off_insights(scored_matrix, weighted_scores)
    
    # Create visualization if output directory provided
    visualization_path = None
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        visualization_path = create_visualization(scored_matrix, weighted_scores, output_dir)
    
    return TradeOffAnalysis(
        scored_matrix=scored_matrix,
        weighted_scores=weighted_scores,
        rankings=rankings,
        sensitivity_analysis=sensitivity_analysis,
        trade_off_insights=trade_off_insights,
        visualization_path=visualization_path
    )

def generate_trade_off_report(analysis: TradeOffAnalysis, output_format: str = 'markdown') -> str:
    """Generate trade-off analysis report"""
    
    if output_format.lower() == 'markdown':
        report = """# Trade-Off Matrix Analysis

## Executive Summary
"""
        
        # Add top ranking
        top_concept, top_score = analysis.rankings[0]
        report += f"**Winner**: {top_concept} ({top_score:.1f} points)\n\n"
        
        # Add key insights
        report += "## Key Trade-Off Insights\n"
        for i, insight in enumerate(analysis.trade_off_insights, 1):
            report += f"{i}. {insight}\n"
        
        report += "\n## Concept Rankings\n\n"
        report += "| Rank | Concept | Weighted Score |\n"
        report += "|------|---------|----------------|\n"
        
        for i, (concept, score) in enumerate(analysis.rankings, 1):
            report += f"| {i} | {concept} | {score:.1f} |\n"
        
        report += "\n## Detailed Scoring Matrix\n\n"
        
        # Convert DataFrame to markdown table
        matrix_md = analysis.scored_matrix.round(1).to_markdown()
        report += matrix_md
        
        report += "\n\n## Sensitivity Analysis\n\n"
        report += "| Criteria | Ranking Sensitivity | Impact Level |\n"
        report += "|----------|-------------------|-------------|\n"
        
        for criteria, data in analysis.sensitivity_analysis.items():
            report += f"| {criteria} | {data['ranking_sensitivity']:.1f} | {data['weight_impact']} |\n"
        
        if analysis.visualization_path:
            report += f"\n## Visualization\n\nSee detailed charts at: `{analysis.visualization_path}`\n"
        
        return report
    
    elif output_format.lower() == 'json':
        return json.dumps({
            'rankings': [{'concept': concept, 'score': score} for concept, score in analysis.rankings],
            'scoring_matrix': analysis.scored_matrix.to_dict(),
            'weighted_scores': analysis.weighted_scores.to_dict(),
            'trade_off_insights': analysis.trade_off_insights,
            'sensitivity_analysis': analysis.sensitivity_analysis,
            'visualization_path': analysis.visualization_path
        }, indent=2)
    
    else:
        # Summary format
        top_concept, top_score = analysis.rankings[0]
        return f"Winner: {top_concept} ({top_score:.1f} points)\nTop insights: {'; '.join(analysis.trade_off_insights[:3])}"

def main():
    parser = argparse.ArgumentParser(description='Generate trade-off matrix analysis for concepts')
    parser.add_argument('concepts_file', type=str, help='Path to concepts YAML file')
    parser.add_argument('criteria_file', type=str, help='Path to criteria YAML file')
    parser.add_argument('--output', type=str, help='Output directory for reports and visualizations')
    parser.add_argument('--format', choices=['markdown', 'json', 'summary'], default='markdown',
                       help='Output format')
    
    args = parser.parse_args()
    
    try:
        concepts_path = Path(args.concepts_file)
        criteria_path = Path(args.criteria_file)
        
        if not concepts_path.exists():
            print(f"❌ Error: Concepts file {concepts_path} not found")
            sys.exit(1)
        
        if not criteria_path.exists():
            print(f"❌ Error: Criteria file {criteria_path} not found")
            sys.exit(1)
        
        # Generate analysis
        output_dir = Path(args.output) if args.output else None
        analysis = generate_trade_off_matrix(concepts_path, criteria_path, output_dir)
        
        # Generate report
        report = generate_trade_off_report(analysis, args.format)
        
        # Output report
        if args.output:
            output_path = Path(args.output) / 'trade_off_analysis.md'
            with open(output_path, 'w') as f:
                f.write(report)
            print(f"✅ Trade-off analysis written to: {output_path}")
            if analysis.visualization_path:
                print(f"📊 Visualization saved to: {analysis.visualization_path}")
        else:
            print(report)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()