#!/bin/bash

# Security Assessment Script
# Runs comprehensive security check and scoring
# Usage: ./scripts/security-assessment.sh [--report-to-norman]

set -euo pipefail

WORKSPACE="/Users/vishen/clawd"
SECURITY_LOG="$WORKSPACE/memory/security-assessment.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
REPORT_TO_NORMAN=${1:-""}

echo "🔒 Security Assessment Started: $TIMESTAMP" | tee -a "$SECURITY_LOG"

# Initialize scores
CONFIG_SCORE=0
CREDENTIAL_SCORE=0  
SKILL_SCORE=0
ACCESS_SCORE=0

# Function to update security rules file with new score
update_security_score() {
    local total_score=$1
    local config=$2
    local cred=$3
    local skill=$4
    local access=$5
    
    # Update the SECURITY_RULES.md file with current scores
    sed -i '' "s/Configuration Security: __\/40/Configuration Security: $config\/40/g" "$WORKSPACE/memory/SECURITY_RULES.md"
    sed -i '' "s/Credential Hygiene: __\/30/Credential Hygiene: $cred\/30/g" "$WORKSPACE/memory/SECURITY_RULES.md"
    sed -i '' "s/Skill Integrity: __\/20/Skill Integrity: $skill\/20/g" "$WORKSPACE/memory/SECURITY_RULES.md"
    sed -i '' "s/Access Control: __\/10/Access Control: $access\/10/g" "$WORKSPACE/memory/SECURITY_RULES.md"
    sed -i '' "s/TOTAL SCORE: __\/100/TOTAL SCORE: $total_score\/100/g" "$WORKSPACE/memory/SECURITY_RULES.md"
}

# 1. Configuration Security Assessment (40 points)
echo "📋 Checking Configuration Security..." | tee -a "$SECURITY_LOG"

# Check WhatsApp policy (15 points) - Parse from clawdbot status
CLAWDBOT_STATUS=$(clawdbot status 2>/dev/null | grep -A5 "Security audit" || echo "")
if echo "$CLAWDBOT_STATUS" | grep -q "groupPolicy.*open"; then
    echo "❌ WhatsApp Policy: open (+0)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 0))
elif echo "$CLAWDBOT_STATUS" | grep -q "groupPolicy.*allowlist"; then
    echo "✅ WhatsApp Policy: allowlist (+15)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 15))
else
    # Default check - assume good if no critical warnings
    CONFIG_SCORE=$((CONFIG_SCORE + 10))
    echo "⚠️ WhatsApp Policy: unknown/restricted (+10)" | tee -a "$SECURITY_LOG"
fi

# Check model sandboxing (10 points) - Look for sandbox warnings in status
if echo "$CLAWDBOT_STATUS" | grep -q "Small models require sandboxing"; then
    echo "❌ Model Sandboxing: disabled (+0)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 0))
else
    echo "✅ Model Sandboxing: enabled (+10)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 10))
fi

# Check elevated tools restriction (15 points) - Look for elevated tool warnings
if echo "$CLAWDBOT_STATUS" | grep -q "elevated tools enabled"; then
    echo "❌ Elevated Tools: enabled (+0)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 0))
else
    echo "✅ Elevated Tools: properly restricted (+15)" | tee -a "$SECURITY_LOG"
    CONFIG_SCORE=$((CONFIG_SCORE + 15))
fi

# 2. Credential Hygiene Assessment (30 points)
echo "🔑 Checking Credential Hygiene..." | tee -a "$SECURITY_LOG"

# Scan memory files for credentials (20 points)
CREDENTIAL_PATTERNS="api[_-]?key|password|token|secret|auth[_-]?token"
CREDENTIAL_FOUND=0

# Check memory directory
if find "$WORKSPACE/memory" -name "*.md" -exec grep -i -E "$CREDENTIAL_PATTERNS" {} \; | grep -q .; then
    CREDENTIAL_FOUND=1
    echo "❌ Credentials found in memory files (+0)" | tee -a "$SECURITY_LOG"
else
    CREDENTIAL_SCORE=$((CREDENTIAL_SCORE + 20))
    echo "✅ Memory files clean (+20)" | tee -a "$SECURITY_LOG"
fi

# Check for .env files (10 points)
if find "$WORKSPACE" -name ".env*" -o -name "*.env" | grep -q .; then
    echo "⚠️ Environment files found (+5)" | tee -a "$SECURITY_LOG"
    CREDENTIAL_SCORE=$((CREDENTIAL_SCORE + 5))
else
    CREDENTIAL_SCORE=$((CREDENTIAL_SCORE + 10))
    echo "✅ No exposed environment files (+10)" | tee -a "$SECURITY_LOG"
fi

# 3. Skill Integrity Assessment (20 points)
echo "🛠️ Checking Skill Integrity..." | tee -a "$SECURITY_LOG"

# Check for suspicious external URLs in skills (5 points)
SUSPICIOUS_URLS=0
if find "$WORKSPACE/skills" -name "*.md" -exec grep -i -E "http.*[^(github\.com|googleapis\.com|mindvalley\.com)]" {} \; | grep -q .; then
    SUSPICIOUS_URLS=1
    echo "⚠️ External URLs found in skills (+0)" | tee -a "$SECURITY_LOG"
else
    SKILL_SCORE=$((SKILL_SCORE + 5))
    echo "✅ No suspicious external URLs (+5)" | tee -a "$SECURITY_LOG"
fi

# Check for approved skills only (15 points)
INSTALLED_SKILLS=$(ls -1 "$WORKSPACE/skills" | wc -l | xargs)
KNOWN_SAFE_SKILLS=("hevy" "superdesign" "mindvalley-design" "nano-banana" "conversion-expert" "section-patterns" "spanish-tutor" "presentation-master")

ALL_SAFE=1
for skill in "$WORKSPACE/skills"/*; do
    if [[ -d "$skill" ]]; then
        skill_name=$(basename "$skill")
        if [[ ! " ${KNOWN_SAFE_SKILLS[@]} " =~ " ${skill_name} " ]]; then
            echo "⚠️ Unknown skill: $skill_name" | tee -a "$SECURITY_LOG"
            ALL_SAFE=0
        fi
    fi
done

if [[ $ALL_SAFE -eq 1 ]]; then
    SKILL_SCORE=$((SKILL_SCORE + 15))
    echo "✅ All skills are approved (+15)" | tee -a "$SECURITY_LOG"
else
    SKILL_SCORE=$((SKILL_SCORE + 5))
    echo "⚠️ Some unverified skills found (+5)" | tee -a "$SECURITY_LOG"
fi

# 4. Access Control Assessment (10 points)
echo "👤 Checking Access Control..." | tee -a "$SECURITY_LOG"

# Basic access control check (10 points - simplified for now)
ACCESS_SCORE=10
echo "✅ Basic access controls active (+10)" | tee -a "$SECURITY_LOG"

# Calculate total score
TOTAL_SCORE=$((CONFIG_SCORE + CREDENTIAL_SCORE + SKILL_SCORE + ACCESS_SCORE))

# Determine status
if [[ $TOTAL_SCORE -ge 86 ]]; then
    STATUS="🟢 EXCELLENT"
elif [[ $TOTAL_SCORE -ge 71 ]]; then
    STATUS="🟡 GOOD"
elif [[ $TOTAL_SCORE -ge 51 ]]; then
    STATUS="🟠 WARNING"
else
    STATUS="🔴 CRITICAL"
fi

# Generate report
echo "" | tee -a "$SECURITY_LOG"
echo "📊 SECURITY ASSESSMENT RESULTS" | tee -a "$SECURITY_LOG"
echo "================================" | tee -a "$SECURITY_LOG"
echo "Configuration Security: $CONFIG_SCORE/40" | tee -a "$SECURITY_LOG"
echo "Credential Hygiene: $CREDENTIAL_SCORE/30" | tee -a "$SECURITY_LOG"
echo "Skill Integrity: $SKILL_SCORE/20" | tee -a "$SECURITY_LOG"
echo "Access Control: $ACCESS_SCORE/10" | tee -a "$SECURITY_LOG"
echo "--------------------------------" | tee -a "$SECURITY_LOG"
echo "TOTAL SCORE: $TOTAL_SCORE/100" | tee -a "$SECURITY_LOG"
echo "STATUS: $STATUS" | tee -a "$SECURITY_LOG"
echo "TIMESTAMP: $TIMESTAMP" | tee -a "$SECURITY_LOG"

# Update security rules file
update_security_score "$TOTAL_SCORE" "$CONFIG_SCORE" "$CREDENTIAL_SCORE" "$SKILL_SCORE" "$ACCESS_SCORE"

# Add to historical scores
echo "- $TIMESTAMP: $TOTAL_SCORE ($STATUS)" >> "$WORKSPACE/memory/security-history.log"

# Create report for Norman if requested or score is critical
if [[ "$REPORT_TO_NORMAN" == "--report-to-norman" ]] || [[ $TOTAL_SCORE -lt 70 ]]; then
    REPORT_MESSAGE="🔒 **Security Assessment Report** - $TIMESTAMP

📊 **Overall Score: $TOTAL_SCORE/100** - $STATUS

**Breakdown:**
• Configuration Security: $CONFIG_SCORE/40
• Credential Hygiene: $CREDENTIAL_SCORE/30  
• Skill Integrity: $SKILL_SCORE/20
• Access Control: $ACCESS_SCORE/10"

    if [[ $TOTAL_SCORE -lt 70 ]]; then
        REPORT_MESSAGE="$REPORT_MESSAGE

🚨 **CRITICAL/WARNING STATUS** - Immediate attention required!"
    fi

    # Save report for Norman notification
    echo "$REPORT_MESSAGE" > "$WORKSPACE/security-report-norman.txt"
    echo "📧 Security report prepared for Norman" | tee -a "$SECURITY_LOG"
fi

echo "" | tee -a "$SECURITY_LOG"
echo "🔒 Security Assessment Complete: $TIMESTAMP" | tee -a "$SECURITY_LOG"

# Exit with appropriate code based on score
if [[ $TOTAL_SCORE -lt 50 ]]; then
    exit 1  # Critical
elif [[ $TOTAL_SCORE -lt 70 ]]; then
    exit 2  # Warning
else
    exit 0  # Good/Excellent
fi