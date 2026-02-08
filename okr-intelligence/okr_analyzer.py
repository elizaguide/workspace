#!/usr/bin/env python3
"""
OKR Intelligence Analyzer
Based on John Doerr's "Measure What Matters" methodology

Analyzes OKRs against meeting notes, project data, and strategic goals
to provide comprehensive quality assessment and alignment scoring.
"""

import json
import re
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass
from datetime import datetime
import argparse

@dataclass
class Objective:
    text: str
    key_results: List[str]
    type: str = "committed"  # committed, aspirational, learning
    owner: str = ""
    quarter: str = ""
    
@dataclass
class OKRAnalysis:
    objective_score: float
    key_results_scores: List[float]
    alignment_score: float
    feasibility_score: float
    recommendations: List[str]
    flags: List[str]

class OKRIntelligence:
    def __init__(self):
        self.doerr_principles = {
            "focus": ["priority", "important", "critical", "key", "primary"],
            "alignment": ["align", "support", "connect", "contribute", "enable"],
            "commitment": ["commit", "deliver", "achieve", "complete", "ensure"],
            "tracking": ["measure", "track", "monitor", "assess", "evaluate"],
            "stretching": ["grow", "improve", "increase", "transform", "breakthrough"]
        }
        
        self.anti_patterns = {
            "bau": ["maintain", "continue", "sustain", "keep", "routine", "ongoing"],
            "vague": ["better", "more", "improve", "enhance", "optimize"],
            "sandbagging": ["ensure", "guarantee", "maintain", "keep stable"],
            "vanity": ["views", "clicks", "likes", "followers", "downloads"]
        }

    def analyze_objective(self, objective: str) -> Tuple[float, List[str]]:
        """Analyze objective quality based on Doerr principles"""
        score = 5.0  # baseline
        feedback = []
        
        # Check for inspiration and clarity
        if len(objective) < 20:
            score -= 1.5
            feedback.append("Objective too brief - lacks inspirational detail")
        elif len(objective) > 100:
            score -= 1.0
            feedback.append("Objective too verbose - should be concise and memorable")
            
        # Check for action orientation
        action_words = ["achieve", "create", "build", "launch", "establish", "deliver"]
        if any(word in objective.lower() for word in action_words):
            score += 1.0
            feedback.append("Good action orientation")
        else:
            score -= 1.0
            feedback.append("Lacks action-oriented language")
            
        # Check for inspiration
        inspiring_words = ["transform", "revolutionize", "breakthrough", "exceptional", "world-class"]
        if any(word in objective.lower() for word in inspiring_words):
            score += 1.5
            feedback.append("Contains inspirational language")
            
        # Check for business-as-usual anti-pattern
        bau_score = sum(1 for word in self.anti_patterns["bau"] if word in objective.lower())
        if bau_score > 0:
            score -= bau_score * 0.5
            feedback.append("WARNING: Contains business-as-usual language")
            
        # Check for vagueness
        vague_score = sum(1 for word in self.anti_patterns["vague"] if word in objective.lower())
        if vague_score > 1:
            score -= 1.0
            feedback.append("WARNING: Contains vague language - be more specific")
            
        return min(10.0, max(1.0, score)), feedback

    def analyze_key_result(self, key_result: str) -> Tuple[float, List[str]]:
        """Analyze key result quality"""
        score = 5.0
        feedback = []
        
        # Check for measurability
        number_pattern = r'\d+([.,]\d+)?(%|k|M|B|$|€|£)?'
        if re.search(number_pattern, key_result):
            score += 2.0
            feedback.append("Contains measurable metrics")
        else:
            score -= 2.0
            feedback.append("CRITICAL: Lacks measurable metrics")
            
        # Check for time bounds
        time_words = ["by", "within", "until", "before", "q1", "q2", "q3", "q4", "january", 
                     "february", "march", "april", "may", "june", "july", "august", 
                     "september", "october", "november", "december"]
        if any(word in key_result.lower() for word in time_words):
            score += 1.0
            feedback.append("Time-bound")
        else:
            score -= 1.5
            feedback.append("Missing time boundary")
            
        # Check for outcome vs output focus
        outcome_words = ["impact", "result", "outcome", "effect", "value", "benefit"]
        output_words = ["feature", "meeting", "document", "report", "presentation"]
        
        outcome_count = sum(1 for word in outcome_words if word in key_result.lower())
        output_count = sum(1 for word in output_words if word in key_result.lower())
        
        if outcome_count > output_count:
            score += 1.0
            feedback.append("Outcome-focused")
        elif output_count > 0:
            score -= 0.5
            feedback.append("Consider focusing on outcomes rather than outputs")
            
        # Check for vanity metrics
        vanity_count = sum(1 for word in self.anti_patterns["vanity"] if word in key_result.lower())
        if vanity_count > 0:
            score -= 1.0
            feedback.append("WARNING: May contain vanity metrics")
            
        return min(10.0, max(1.0, score)), feedback

    def analyze_alignment(self, okrs: List[Objective], context_data: Dict) -> Tuple[float, List[str]]:
        """Analyze OKR alignment with strategic context"""
        score = 5.0
        feedback = []
        
        # Check against meeting notes
        if 'meeting_notes' in context_data:
            meeting_alignment = self._check_meeting_alignment(okrs, context_data['meeting_notes'])
            score += (meeting_alignment - 5.0) * 0.3
            if meeting_alignment < 6.0:
                feedback.append("Low alignment with meeting discussions")
            else:
                feedback.append("Good alignment with meeting priorities")
                
        # Check against project data
        if 'projects' in context_data:
            project_alignment = self._check_project_alignment(okrs, context_data['projects'])
            score += (project_alignment - 5.0) * 0.4
            if project_alignment < 6.0:
                feedback.append("Poor integration with active projects")
            else:
                feedback.append("Well integrated with project roadmap")
                
        # Check strategic coherence
        if 'strategy' in context_data:
            strategic_alignment = self._check_strategic_coherence(okrs, context_data['strategy'])
            score += (strategic_alignment - 5.0) * 0.3
            if strategic_alignment < 6.0:
                feedback.append("Weak connection to strategic goals")
            else:
                feedback.append("Strong strategic alignment")
                
        return min(10.0, max(1.0, score)), feedback

    def _check_meeting_alignment(self, okrs: List[Objective], meeting_notes: str) -> float:
        """Check how well OKRs align with meeting discussions"""
        score = 5.0
        
        # Extract key topics from meetings
        meeting_text = meeting_notes.lower()
        okr_text = " ".join([obj.text.lower() for obj in okrs])
        
        # Simple keyword overlap analysis
        meeting_keywords = set(re.findall(r'\b\w+\b', meeting_text))
        okr_keywords = set(re.findall(r'\b\w+\b', okr_text))
        
        overlap = len(meeting_keywords.intersection(okr_keywords))
        total_unique = len(meeting_keywords.union(okr_keywords))
        
        if total_unique > 0:
            overlap_ratio = overlap / len(okr_keywords) if len(okr_keywords) > 0 else 0
            score = 1.0 + (overlap_ratio * 9.0)
            
        return min(10.0, max(1.0, score))

    def _check_project_alignment(self, okrs: List[Objective], projects: List[Dict]) -> float:
        """Check alignment between OKRs and active projects"""
        score = 5.0
        
        if not projects:
            return score
            
        # Check if projects support OKR key results
        project_names = [p.get('name', '').lower() for p in projects]
        project_text = " ".join(project_names)
        
        alignment_count = 0
        total_krs = sum(len(obj.key_results) for obj in okrs)
        
        for obj in okrs:
            for kr in obj.key_results:
                kr_keywords = set(re.findall(r'\b\w+\b', kr.lower()))
                project_keywords = set(re.findall(r'\b\w+\b', project_text))
                
                if kr_keywords.intersection(project_keywords):
                    alignment_count += 1
                    
        if total_krs > 0:
            alignment_ratio = alignment_count / total_krs
            score = 1.0 + (alignment_ratio * 9.0)
            
        return min(10.0, max(1.0, score))

    def _check_strategic_coherence(self, okrs: List[Objective], strategy: Dict) -> float:
        """Check OKR coherence with strategic direction"""
        score = 5.0
        
        # Extract strategic keywords
        strategic_text = ""
        if isinstance(strategy, dict):
            strategic_text = " ".join([
                strategy.get('mission', ''),
                strategy.get('vision', ''),
                " ".join(strategy.get('goals', []))
            ]).lower()
        else:
            strategic_text = str(strategy).lower()
            
        okr_text = " ".join([obj.text.lower() for obj in okrs])
        
        # Check keyword alignment
        strategy_keywords = set(re.findall(r'\b\w+\b', strategic_text))
        okr_keywords = set(re.findall(r'\b\w+\b', okr_text))
        
        if len(okr_keywords) > 0:
            overlap_ratio = len(strategy_keywords.intersection(okr_keywords)) / len(okr_keywords)
            score = 1.0 + (overlap_ratio * 9.0)
            
        return min(10.0, max(1.0, score))

    def generate_recommendations(self, analysis: OKRAnalysis, okr: Objective) -> List[str]:
        """Generate specific recommendations for OKR improvement"""
        recommendations = []
        
        if analysis.objective_score < 6.0:
            recommendations.append("Rewrite objective to be more specific and inspirational")
            recommendations.append("Add concrete action language (achieve, create, build)")
            
        avg_kr_score = sum(analysis.key_results_scores) / len(analysis.key_results_scores) if analysis.key_results_scores else 0
        if avg_kr_score < 6.0:
            recommendations.append("Add specific, measurable metrics to key results")
            recommendations.append("Include clear deadlines for each key result")
            recommendations.append("Focus on outcomes rather than activities")
            
        if analysis.alignment_score < 6.0:
            recommendations.append("Better align with meeting discussions and project priorities")
            recommendations.append("Review strategic goals to ensure coherent direction")
            
        if analysis.feasibility_score < 6.0:
            recommendations.append("Assess resource requirements and availability")
            recommendations.append("Consider breaking down into smaller, achievable milestones")
            
        return recommendations

    def analyze_okr_set(self, okrs: List[Objective], context_data: Dict = None) -> Dict[str, Any]:
        """Comprehensive analysis of an OKR set"""
        if context_data is None:
            context_data = {}
            
        results = {
            "overall_score": 0.0,
            "analyses": [],
            "summary": {
                "total_okrs": len(okrs),
                "avg_objective_score": 0.0,
                "avg_key_results_score": 0.0,
                "alignment_score": 0.0,
                "top_recommendations": []
            }
        }
        
        total_scores = []
        all_recommendations = []
        
        for okr in okrs:
            # Analyze objective
            obj_score, obj_feedback = self.analyze_objective(okr.text)
            
            # Analyze key results
            kr_scores = []
            kr_feedback = []
            for kr in okr.key_results:
                kr_score, kr_fb = self.analyze_key_result(kr)
                kr_scores.append(kr_score)
                kr_feedback.extend(kr_fb)
                
            # Analyze alignment
            alignment_score, alignment_feedback = self.analyze_alignment([okr], context_data)
            
            # Create analysis
            analysis = OKRAnalysis(
                objective_score=obj_score,
                key_results_scores=kr_scores,
                alignment_score=alignment_score,
                feasibility_score=7.0,  # Default - would need more context to assess
                recommendations=obj_feedback + kr_feedback + alignment_feedback,
                flags=[]
            )
            
            # Generate specific recommendations
            specific_recs = self.generate_recommendations(analysis, okr)
            all_recommendations.extend(specific_recs)
            
            okr_total_score = (obj_score + (sum(kr_scores)/len(kr_scores) if kr_scores else 0) + alignment_score) / 3
            total_scores.append(okr_total_score)
            
            results["analyses"].append({
                "okr": okr.text,
                "analysis": {
                    "objective_score": analysis.objective_score,
                    "key_results_scores": analysis.key_results_scores,
                    "alignment_score": analysis.alignment_score,
                    "feasibility_score": analysis.feasibility_score,
                    "recommendations": analysis.recommendations,
                    "flags": analysis.flags
                },
                "total_score": okr_total_score
            })
            
        # Calculate summary
        results["overall_score"] = sum(total_scores) / len(total_scores) if total_scores else 0
        results["summary"]["avg_objective_score"] = sum(a["analysis"]["objective_score"] for a in results["analyses"]) / len(results["analyses"]) if results["analyses"] else 0
        results["summary"]["avg_key_results_score"] = sum(sum(a["analysis"]["key_results_scores"])/len(a["analysis"]["key_results_scores"]) if a["analysis"]["key_results_scores"] else 0 for a in results["analyses"]) / len(results["analyses"]) if results["analyses"] else 0
        results["summary"]["alignment_score"] = sum(a["analysis"]["alignment_score"] for a in results["analyses"]) / len(results["analyses"]) if results["analyses"] else 0
        
        # Top recommendations (deduplicated)
        rec_counts = {}
        for rec in all_recommendations:
            rec_counts[rec] = rec_counts.get(rec, 0) + 1
        results["summary"]["top_recommendations"] = sorted(rec_counts.keys(), key=rec_counts.get, reverse=True)[:5]
        
        return results

def main():
    parser = argparse.ArgumentParser(description="OKR Intelligence Analyzer")
    parser.add_argument("--okr-file", required=True, help="JSON file containing OKRs")
    parser.add_argument("--context-file", help="JSON file containing context data")
    parser.add_argument("--output", help="Output file for analysis results")
    
    args = parser.parse_args()
    
    # Load OKRs
    with open(args.okr_file, 'r') as f:
        okr_data = json.load(f)
        
    okrs = []
    for okr_dict in okr_data:
        okr = Objective(
            text=okr_dict["objective"],
            key_results=okr_dict["key_results"],
            type=okr_dict.get("type", "committed"),
            owner=okr_dict.get("owner", ""),
            quarter=okr_dict.get("quarter", "")
        )
        okrs.append(okr)
    
    # Load context data if provided
    context_data = {}
    if args.context_file:
        with open(args.context_file, 'r') as f:
            context_data = json.load(f)
    
    # Analyze OKRs
    analyzer = OKRIntelligence()
    results = analyzer.analyze_okr_set(okrs, context_data)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
    else:
        print(json.dumps(results, indent=2, default=str))

if __name__ == "__main__":
    main()