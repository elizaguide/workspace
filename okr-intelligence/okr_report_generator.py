#!/usr/bin/env python3
"""
OKR Intelligence Report Generator
Generates comprehensive, readable reports from OKR analysis data
"""

import json
import sys
from datetime import datetime
from typing import Dict, Any

class OKRReportGenerator:
    def __init__(self):
        self.grade_mapping = {
            (9, 10): "🟢 EXCELLENT",
            (7, 8.9): "🟡 GOOD", 
            (5, 6.9): "🟠 NEEDS IMPROVEMENT",
            (1, 4.9): "🔴 POOR"
        }
        
    def get_grade(self, score: float) -> str:
        """Convert numeric score to grade"""
        for (min_score, max_score), grade in self.grade_mapping.items():
            if min_score <= score <= max_score:
                return grade
        return "🔴 POOR"
    
    def generate_executive_summary(self, analysis: Dict[str, Any]) -> str:
        """Generate executive summary section"""
        overall_score = analysis["overall_score"]
        overall_grade = self.get_grade(overall_score)
        
        summary = f"""
# OKR Intelligence Report
**Generated:** {datetime.now().strftime("%B %d, %Y at %I:%M %p")}
**Analysis Framework:** John Doerr's "Measure What Matters" Methodology

## 📊 Executive Summary

**Overall OKR Health Score:** {overall_score:.1f}/10 {overall_grade}

| Metric | Score | Grade |
|--------|-------|-------|
| Average Objective Quality | {analysis['summary']['avg_objective_score']:.1f}/10 | {self.get_grade(analysis['summary']['avg_objective_score'])} |
| Average Key Results Quality | {analysis['summary']['avg_key_results_score']:.1f}/10 | {self.get_grade(analysis['summary']['avg_key_results_score'])} |
| Strategic Alignment | {analysis['summary']['alignment_score']:.1f}/10 | {self.get_grade(analysis['summary']['alignment_score'])} |
| Total OKRs Analyzed | {analysis['summary']['total_okrs']} | - |

"""
        return summary
    
    def generate_detailed_analysis(self, analysis: Dict[str, Any]) -> str:
        """Generate detailed analysis for each OKR"""
        details = "\n## 📋 Detailed OKR Analysis\n\n"
        
        for i, okr_analysis in enumerate(analysis["analyses"], 1):
            okr = okr_analysis["okr"]
            analysis_data = okr_analysis["analysis"]
            total_score = okr_analysis["total_score"]
            
            # Truncate long objectives for readability
            display_objective = okr[:80] + "..." if len(okr) > 80 else okr
            
            avg_kr_score = sum(analysis_data["key_results_scores"])/len(analysis_data["key_results_scores"]) if analysis_data["key_results_scores"] else 0
            
            details += f"""
### OKR #{i}: {display_objective}
**Overall Score:** {total_score:.1f}/10 {self.get_grade(total_score)}

| Component | Score | Grade |
|-----------|-------|-------|
| Objective Quality | {analysis_data["objective_score"]:.1f}/10 | {self.get_grade(analysis_data["objective_score"])} |
| Key Results Quality | {avg_kr_score:.1f}/10 | {self.get_grade(avg_kr_score)} |
| Strategic Alignment | {analysis_data["alignment_score"]:.1f}/10 | {self.get_grade(analysis_data["alignment_score"])} |

"""
            
            # Key Results breakdown
            if analysis_data["key_results_scores"]:
                details += "**Key Results Scores:**\n"
                for j, kr_score in enumerate(analysis_data["key_results_scores"], 1):
                    details += f"- KR{j}: {kr_score:.1f}/10 {self.get_grade(kr_score)}\n"
                details += "\n"
                
            # Feedback and recommendations
            if analysis_data["recommendations"]:
                details += "**Key Feedback:**\n"
                for rec in analysis_data["recommendations"][:3]:  # Top 3 recommendations
                    details += f"- {rec}\n"
                details += "\n"
                
        return details
    
    def generate_recommendations(self, analysis: Dict[str, Any]) -> str:
        """Generate actionable recommendations section"""
        recommendations = "\n## 🎯 Priority Recommendations\n\n"
        
        top_recs = analysis["summary"]["top_recommendations"][:5]
        
        recommendations += "### Immediate Actions Required:\n"
        for i, rec in enumerate(top_recs, 1):
            recommendations += f"{i}. **{rec}**\n"
            
        recommendations += "\n### OKR Quality Improvement Matrix:\n\n"
        
        # Analyze patterns for systemic issues
        obj_scores = [a["analysis"]["objective_score"] for a in analysis["analyses"]]
        kr_scores = [sum(a["analysis"]["key_results_scores"])/len(a["analysis"]["key_results_scores"]) if a["analysis"]["key_results_scores"] else 0 for a in analysis["analyses"]]
        alignment_scores = [a["analysis"]["alignment_score"] for a in analysis["analyses"]]
        
        avg_obj = sum(obj_scores) / len(obj_scores) if obj_scores else 0
        avg_kr = sum(kr_scores) / len(kr_scores) if kr_scores else 0
        avg_align = sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0
        
        if avg_obj < 6.0:
            recommendations += """
**🔴 CRITICAL: Objective Quality Issues**
- Objectives lack inspiration and specificity
- Add action-oriented language (achieve, create, build, transform)
- Make objectives more concrete and meaningful
- Avoid business-as-usual language

"""
        
        if avg_kr < 6.0:
            recommendations += """
**🔴 CRITICAL: Key Results Quality Issues** 
- Key Results are not sufficiently measurable
- Add specific numeric targets with deadlines
- Focus on outcomes rather than activities
- Ensure results are verifiable (yes/no achievement)

"""
        
        if avg_align < 6.0:
            recommendations += """
**🟠 WARNING: Strategic Alignment Issues**
- OKRs don't sufficiently connect to strategic priorities
- Review meeting notes to ensure OKRs reflect actual focus areas
- Better integration needed with active projects
- Align with company mission and vision

"""
            
        return recommendations
    
    def generate_doerr_compliance(self, analysis: Dict[str, Any]) -> str:
        """Generate compliance check against Doerr's FACTS framework"""
        compliance = "\n## ✅ Doerr F.A.C.T.S. Framework Compliance\n\n"
        
        # Calculate compliance scores
        obj_scores = [a["analysis"]["objective_score"] for a in analysis["analyses"]]
        kr_scores = [sum(a["analysis"]["key_results_scores"])/len(a["analysis"]["key_results_scores"]) if a["analysis"]["key_results_scores"] else 0 for a in analysis["analyses"]]
        alignment_scores = [a["analysis"]["alignment_score"] for a in analysis["analyses"]]
        
        focus_score = sum(obj_scores) / len(obj_scores) if obj_scores else 0
        alignment_score = sum(alignment_scores) / len(alignment_scores) if alignment_scores else 0
        tracking_score = sum(kr_scores) / len(kr_scores) if kr_scores else 0
        
        # Simplified scoring for commitment and stretching
        commitment_score = (focus_score + alignment_score) / 2
        stretching_score = max(0, min(10, focus_score + 1))  # Rough estimate
        
        compliance += f"""
| F.A.C.T.S. Element | Score | Grade | Assessment |
|-------------------|-------|-------|------------|
| **Focus** | {focus_score:.1f}/10 | {self.get_grade(focus_score)} | {'Clear priorities' if focus_score >= 7 else 'Lacks focus'} |
| **Alignment** | {alignment_score:.1f}/10 | {self.get_grade(alignment_score)} | {'Well aligned' if alignment_score >= 7 else 'Poor alignment'} |
| **Commitment** | {commitment_score:.1f}/10 | {self.get_grade(commitment_score)} | {'Strong commitment' if commitment_score >= 7 else 'Weak commitment'} |
| **Tracking** | {tracking_score:.1f}/10 | {self.get_grade(tracking_score)} | {'Measurable' if tracking_score >= 7 else 'Hard to measure'} |
| **Stretching** | {stretching_score:.1f}/10 | {self.get_grade(stretching_score)} | {'Ambitious' if stretching_score >= 7 else 'Not ambitious enough'} |

"""
        
        # Overall FACTS compliance
        facts_score = (focus_score + alignment_score + commitment_score + tracking_score + stretching_score) / 5
        compliance += f"\n**Overall F.A.C.T.S. Compliance:** {facts_score:.1f}/10 {self.get_grade(facts_score)}\n"
        
        return compliance
    
    def generate_next_steps(self, analysis: Dict[str, Any]) -> str:
        """Generate next steps and action plan"""
        next_steps = "\n## 🚀 Next Steps & Action Plan\n\n"
        
        overall_score = analysis["overall_score"]
        
        if overall_score < 5.0:
            next_steps += """
### 🆘 IMMEDIATE INTERVENTION REQUIRED

**Week 1-2:**
1. **Emergency OKR Workshop** - Rewrite all OKRs using Doerr methodology
2. **Leadership Alignment** - Ensure leadership consensus on priorities
3. **Resource Assessment** - Evaluate if current OKRs are achievable

**Week 3-4:** 
1. **Team Training** - Educate teams on proper OKR writing
2. **Check-in Process** - Establish weekly OKR review meetings
3. **Tracking Setup** - Implement measurement systems

"""
        elif overall_score < 7.0:
            next_steps += """
### 🔧 STRUCTURED IMPROVEMENT PLAN

**Month 1:**
1. **OKR Refinement** - Address specific quality issues identified
2. **Alignment Workshop** - Improve strategic coherence
3. **Measurement Systems** - Enhance tracking capabilities

**Month 2:**
1. **Team Coaching** - Work with teams on OKR quality
2. **Cross-functional Alignment** - Improve project integration
3. **Progress Reviews** - Implement regular assessment cycles

"""
        else:
            next_steps += """
### 📈 OPTIMIZATION & SCALING

**Ongoing Improvements:**
1. **Advanced OKR Techniques** - Implement aspirational vs committed OKR balance
2. **Cross-team Alignment** - Enhance horizontal coordination  
3. **Cultural Integration** - Embed OKRs deeper into company culture
4. **Coaching Excellence** - Develop internal OKR coaching capabilities

"""
        
        next_steps += """
### 📅 Regular OKR Health Checks

- **Weekly:** Team-level OKR progress reviews
- **Monthly:** Cross-functional alignment assessment  
- **Quarterly:** Comprehensive OKR quality analysis
- **Annually:** OKR methodology and culture evaluation

### 📚 Recommended Reading

1. **"Measure What Matters"** by John Doerr - Foundation methodology
2. **"Radical Focus"** by Christina Wodtke - Practical OKR implementation
3. **"The 4 Disciplines of Execution"** - Execution excellence
"""
        
        return next_steps
    
    def generate_full_report(self, analysis: Dict[str, Any]) -> str:
        """Generate complete OKR intelligence report"""
        report = ""
        report += self.generate_executive_summary(analysis)
        report += self.generate_detailed_analysis(analysis)
        report += self.generate_doerr_compliance(analysis)
        report += self.generate_recommendations(analysis)
        report += self.generate_next_steps(analysis)
        
        report += "\n---\n*Report generated by OKR Intelligence System based on John Doerr's \"Measure What Matters\" methodology*\n"
        
        return report

def main():
    if len(sys.argv) < 2:
        print("Usage: python okr_report_generator.py <analysis_results.json> [output_file.md]")
        sys.exit(1)
    
    # Load analysis results
    with open(sys.argv[1], 'r') as f:
        analysis = json.load(f)
    
    # Generate report
    generator = OKRReportGenerator()
    report = generator.generate_full_report(analysis)
    
    # Output report
    if len(sys.argv) > 2:
        with open(sys.argv[2], 'w') as f:
            f.write(report)
        print(f"Report written to {sys.argv[2]}")
    else:
        print(report)

if __name__ == "__main__":
    main()