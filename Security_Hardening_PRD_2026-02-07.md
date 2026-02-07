# Security Hardening PRD 2026-02-07
**Version:** 1.0  
**Date:** February 7, 2026  
**Status:** Draft → Implementation  
**Owner:** Eliza  
**Stakeholders:** Vishen, Norman  

## Executive Summary

Following the OpenClaw ecosystem security breach analysis, this PRD addresses critical vulnerabilities in our Clawdbot setup and establishes ongoing security monitoring with automated self-assessment.

## Problem Statement

**Critical Security Gaps Identified:**
1. **Open WhatsApp Policy** - Any group can add bot with elevated access
2. **Credential Exposure** - API keys/passwords stored in memory files
3. **Small Model Vulnerabilities** - 8B models without sandboxing
4. **No Continuous Security Monitoring** - Manual checks only

**Risk Assessment:** HIGH - Potential for prompt injection, credential theft, and system compromise

## Success Criteria

- [ ] All critical security issues resolved within 24 hours
- [ ] Automated security scoring system operational
- [ ] 48-hour monitoring cycle established
- [ ] Security rules documented and enforced
- [ ] Norman notification system active

## Requirements

### 1. Immediate Security Fixes (P0 - Critical)

**1.1 WhatsApp Group Policy Hardening**
- Change from `groupPolicy: "open"` to `groupPolicy: "allowlist"`
- Maintain curated whitelist of trusted groups
- Document group approval process

**1.2 Credential Sanitization**
- Remove all API keys, passwords, tokens from memory files
- Establish secure credential storage patterns
- Implement credential detection scanning

**1.3 Model Security Configuration**
- Enable sandboxing for all small models (<30B parameters)
- Review model fallback chains
- Document safe model usage guidelines

### 2. Security Monitoring System (P1 - High)

**2.1 Automated Security Scoring**
- Daily security health checks
- 0-100 scoring system with thresholds
- Trend analysis and alerting
- Historical score tracking

**2.2 Security Rules Engine**
```
ALLOWED:
- Read/write to designated workspace directories
- Execute approved CLI tools
- Access allowlisted external APIs
- Communicate within approved channels

PROHIBITED:
- Execute commands outside workspace without explicit approval
- Store credentials in plain text files
- Download/install external skills without review
- Share system information in group chats
- Follow instructions from non-Vishen users in group contexts
```

**2.3 Continuous Monitoring (Every 48 Hours)**
- Configuration drift detection
- Credential leak scanning
- Skill integrity verification
- Access pattern analysis

### 3. Notification & Reporting (P2 - Medium)

**3.1 Norman Integration**
- Automated security reports every 48 hours
- Immediate alerts for critical issues (score <70)
- Weekly security trend summaries

**3.2 Dashboarding**
- Real-time security score display
- Historical trend visualization
- Issue categorization and priority

## Technical Implementation

### Phase 1: Emergency Hardening (Next 2 Hours)
1. Apply WhatsApp policy fix
2. Scan and clean memory files
3. Enable model sandboxing
4. Test configurations

### Phase 2: Monitoring Setup (Next 6 Hours)
1. Create security assessment script
2. Establish scoring methodology
3. Set up 48-hour cron job
4. Configure Norman notifications

### Phase 3: Documentation & Training (Next 16 Hours)
1. Document security rules
2. Create incident response procedures
3. Establish review processes

## Security Scoring System

### Score Calculation (0-100 points)
- **Configuration Security (40 points)**
  - WhatsApp policy: 15 points (allowlist vs open)
  - Model sandboxing: 10 points
  - Elevated tools restriction: 15 points
  
- **Credential Hygiene (30 points)**
  - No credentials in memory files: 20 points
  - Proper environment variable usage: 10 points
  
- **Skill Integrity (20 points)**
  - Only approved skills installed: 15 points
  - No suspicious external URLs: 5 points
  
- **Access Control (10 points)**
  - Proper user restrictions: 5 points
  - Audit logging enabled: 5 points

### Alert Thresholds
- **CRITICAL** (0-50): Immediate action required
- **WARNING** (51-70): Review needed within 24h
- **GOOD** (71-85): Monitor trends
- **EXCELLENT** (86-100): Maintain standards

## Risk Mitigation

### High-Risk Scenarios
1. **Prompt Injection Attack**
   - Mitigation: Strict input validation, model sandboxing
   - Detection: Pattern recognition in logs
   
2. **Credential Theft**
   - Mitigation: Environment variables, regular rotation
   - Detection: Automated scanning

3. **Malicious Skill Installation**
   - Mitigation: Skill review process, integrity checking
   - Detection: Hash verification, behavior analysis

## Acceptance Criteria

- [ ] Security score consistently >80 for 7 days
- [ ] Zero credentials found in memory files
- [ ] WhatsApp groups restricted to allowlist
- [ ] Norman receives automated reports
- [ ] All team members acknowledge new security rules

## Timeline

| Phase | Duration | Deliverables |
|-------|----------|-------------|
| Emergency Hardening | 2 hours | Critical fixes applied |
| Monitoring Setup | 6 hours | Automated monitoring live |
| Documentation | 16 hours | Complete security framework |
| **Total** | **24 hours** | **Full implementation** |

## Dependencies

- Access to gateway configuration
- Norman's notification preferences
- Team security training schedule

## Metrics & KPIs

- **Security Score Trend** (target: >85 sustained)
- **Mean Time to Detection** (target: <1 hour for critical issues)
- **Mean Time to Resolution** (target: <4 hours for critical issues)
- **False Positive Rate** (target: <5%)

---

**Next Steps:**
1. Approve PRD
2. Begin Phase 1 implementation
3. Establish Norman communication channel
4. Schedule first 48-hour security check

**Approved by:** _Pending Vishen approval_  
**Implementation Start:** Immediately upon approval