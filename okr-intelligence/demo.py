#!/usr/bin/env python3
"""
OKR Intelligence Demo
Demonstrates the complete OKR analysis workflow
"""

import subprocess
import json
import os

def run_demo():
    print("🧠 OKR Intelligence System Demo")
    print("Based on John Doerr's 'Measure What Matters' methodology")
    print("=" * 60)
    
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Step 1: Analyze OKRs
    print("\n📊 Step 1: Analyzing OKRs...")
    analysis_cmd = [
        "python3", "okr_analyzer.py",
        "--okr-file", "examples/sample_okrs.json", 
        "--context-file", "examples/context_data.json",
        "--output", "analysis_results.json"
    ]
    
    result = subprocess.run(analysis_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running analysis: {result.stderr}")
        return
        
    print("✅ Analysis complete!")
    
    # Step 2: Generate report
    print("\n📋 Step 2: Generating comprehensive report...")
    report_cmd = [
        "python3", "okr_report_generator.py",
        "analysis_results.json",
        "okr_intelligence_report.md"
    ]
    
    result = subprocess.run(report_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error generating report: {result.stderr}")
        return
        
    print("✅ Report generated!")
    
    # Step 3: Show summary results
    print("\n📈 Step 3: Summary Results...")
    with open('analysis_results.json', 'r') as f:
        analysis = json.load(f)
    
    print(f"Overall OKR Health Score: {analysis['overall_score']:.1f}/10")
    print(f"Average Objective Quality: {analysis['summary']['avg_objective_score']:.1f}/10")
    print(f"Average Key Results Quality: {analysis['summary']['avg_key_results_score']:.1f}/10") 
    print(f"Strategic Alignment Score: {analysis['summary']['alignment_score']:.1f}/10")
    
    print("\nTop Recommendations:")
    for i, rec in enumerate(analysis['summary']['top_recommendations'][:3], 1):
        print(f"{i}. {rec}")
    
    # Step 4: Show specific OKR examples
    print("\n🔍 Step 4: Example OKR Analysis...")
    
    print("\nEXAMPLE - Good OKR:")
    print("Objective: Transform Mindvalley's AI education platform...")
    print(f"Score: {analysis['analyses'][0]['total_score']:.1f}/10")
    
    print("\nEXAMPLE - Poor OKR (Business-as-usual):")
    print("Objective: Maintain current email marketing performance...")
    print(f"Score: {analysis['analyses'][3]['total_score']:.1f}/10")
    
    print(f"\n📄 Full detailed report saved to: okr_intelligence_report.md")
    print("🎯 Next: Review the report and implement recommendations!")
    
    # Clean up demo files
    cleanup = input("\nClean up demo files? (y/n): ")
    if cleanup.lower() == 'y':
        os.remove('analysis_results.json')
        os.remove('okr_intelligence_report.md')
        print("✅ Demo files cleaned up!")

if __name__ == "__main__":
    run_demo()