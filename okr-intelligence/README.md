# OKR Intelligence System

A comprehensive OKR analysis and evaluation system based on **John Doerr's "Measure What Matters"** methodology. Analyzes team OKRs against meeting notes, project data, and organizational goals to ensure alignment, quality, and effectiveness.

## 🎯 Overview

This system implements Doerr's **F.A.C.T.S. framework**:
- **Focus:** Rally behind carefully chosen priorities
- **Alignment:** Connect goals at every organizational layer  
- **Commitment:** Collective commitment to agreed-upon priorities
- **Tracking:** Monitor progress and know when to change tactics
- **Stretching:** Set goals beyond business-as-usual

## 🚀 Quick Start

### 1. Run the Demo
```bash
python3 demo.py
```

This will analyze sample OKRs and generate a comprehensive intelligence report.

### 2. Analyze Your Own OKRs

**Step 1: Prepare your OKR file** (`okrs.json`):
```json
[
  {
    "objective": "Transform our customer success platform into industry-leading solution",
    "key_results": [
      "Increase customer retention from 85% to 95% by Q2 end",
      "Reduce average resolution time from 24hrs to 4hrs by March 31st",
      "Achieve 4.8+ NPS score across all customer segments",
      "Launch predictive analytics for 100% of enterprise clients"
    ],
    "type": "aspirational",
    "owner": "Customer Success Team", 
    "quarter": "Q1 2026"
  }
]
```

**Step 2: Create context file** (`context.json`):
```json
{
  "meeting_notes": "Latest team meeting discussions and decisions...",
  "projects": [
    {
      "name": "Customer Platform Redesign",
      "status": "in_progress", 
      "priority": "high",
      "team": "Engineering"
    }
  ],
  "strategy": {
    "mission": "Your company mission",
    "goals": ["Strategic goal 1", "Strategic goal 2"]
  }
}
```

**Step 3: Run analysis:**
```bash
python3 okr_analyzer.py --okr-file okrs.json --context-file context.json --output results.json
```

**Step 4: Generate report:**
```bash
python3 okr_report_generator.py results.json report.md
```

## 📊 Analysis Framework

### OKR Quality Assessment

**Objectives evaluated on:**
- Clarity and specificity
- Inspirational quality
- Action orientation  
- Strategic alignment
- Avoidance of business-as-usual

**Key Results evaluated on:**
- Measurability and specificity
- Time-bound nature
- Outcome vs output focus
- Realistic stretch level
- Verifiability

### Cross-Reference Analysis

**Meeting Alignment:** Checks if OKRs reflect actual team priorities and discussions

**Project Integration:** Ensures active projects support OKR achievement

**Strategic Coherence:** Validates alignment with company mission, vision, and goals

## 📈 Scoring System

- **9-10:** 🟢 EXCELLENT - Best-in-class OKR quality
- **7-8:** 🟡 GOOD - Solid OKRs with minor improvements needed  
- **5-6:** 🟠 NEEDS IMPROVEMENT - Significant quality issues
- **1-4:** 🔴 POOR - Major rewrite required

## 🎯 Barry Consulting Project Integration

For consulting projects, use this OKR template:

```json
{
  "objective": "Transform [client] capability in [specific domain]",
  "key_results": [
    "[Measurable business impact - revenue/cost/efficiency]",
    "[Capability development metric - skills/processes/systems]", 
    "[Stakeholder adoption/satisfaction metric]",
    "[Knowledge transfer/sustainability metric]"
  ],
  "type": "committed",
  "quarter": "Q1 2026"
}
```

## 📋 Common OKR Issues Detected

### ❌ Anti-Patterns Flagged:
- **Business-as-usual:** Maintaining status quo instead of driving change
- **Sandbagging:** Targets set too low for easy achievement
- **Vanity metrics:** Focusing on impressive but meaningless numbers
- **Vague language:** Using unclear, non-specific terms
- **Poor alignment:** OKRs disconnected from strategic priorities

### ✅ Best Practices Enforced:
- Specific, measurable key results
- Outcome-focused rather than activity-focused
- Appropriate stretch level (70% confidence)
- Clear time boundaries
- Inspirational objectives that motivate teams

## 🛠 System Components

- **`okr_analyzer.py`** - Core analysis engine implementing Doerr methodology
- **`okr_report_generator.py`** - Generates comprehensive readable reports
- **`demo.py`** - Interactive demonstration of complete workflow
- **`examples/`** - Sample OKRs and context data for testing

## 📚 Methodology References

Based on principles from John Doerr's **"Measure What Matters"**:
- Objectives and Key Results framework
- F.A.C.T.S. implementation guidance  
- Google's OKR practices and grading systems
- Intel's original OKR methodology (Andy Grove)
- Committed vs Aspirational OKR distinctions

## 🔄 Regular Usage

### Weekly Health Checks
```bash
python3 okr_analyzer.py --okr-file current_okrs.json --context-file weekly_context.json
```

### Quarterly Comprehensive Review
```bash
# Generate full intelligence report for quarterly review
python3 okr_analyzer.py --okr-file q1_okrs.json --context-file quarter_context.json --output q1_analysis.json
python3 okr_report_generator.py q1_analysis.json Q1_OKR_Intelligence_Report.md
```

## 📊 Integration with Team Tools

The system can integrate with:
- **Meeting notes** from any text source
- **Project management** data (JSON format)
- **Strategic planning** documents
- **Performance metrics** and historical data

## 🎓 Training Your Team

Use this system to:
1. **Assess current OKR quality** and identify improvement areas
2. **Train teams** on proper OKR writing using Doerr methodology  
3. **Monitor alignment** between OKRs and actual work
4. **Track improvement** in OKR quality over time
5. **Coach individuals** on better goal setting

---

*Built on John Doerr's "Measure What Matters" methodology - helping teams achieve audacious goals through better OKRs.*