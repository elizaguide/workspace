# Daily Mindvalley Monitoring System

## **How It Works:**

### 1. **Daily Report (8:45 AM GMT)**
- Automated cron job checks multiple sources
- Generates structured report using template
- Sends to WhatsApp group with summary
- Saves full report to `memory/mindvalley-monitoring/YYYY-MM-DD.md`

### 2. **Critical Alert System**
- Immediate alerts for:
  - New 1-star Trustpilot reviews
  - Viral negative Reddit posts (>50 upvotes)
  - Negative media coverage
  - Trending negative hashtags

### 3. **Sources Monitored:**
- **Trustpilot**: New reviews, rating changes
- **Reddit**: r/scams, r/entrepreneur, r/selfimprovement mentions
- **Social Media**: Twitter, Facebook mentions (when accessible)
- **Google Search**: Recent news, discussions
- **YouTube**: Video comments on Mindvalley content
- **App Store/Play Store**: New app reviews

### 4. **Report Sections:**
- **Executive Summary**: Quick overview for busy executives
- **Critical Alerts**: Immediate action items
- **Daily Metrics**: Quantified data
- **Ad Team Insights**: Specific recommendations
- **Competitive Intelligence**: What competitors are doing

## **Manual Override:**
- Type "Check Mindvalley NOW" for immediate report
- Type "Critical Alert Search" for urgent threat assessment
- All reports archived in memory folder for trend analysis

## **Escalation Protocol:**
1. **Low Priority**: Include in daily report
2. **Medium Priority**: Bold highlight in daily report  
3. **High Priority**: Immediate dedicated message to group
4. **Critical**: Immediate message + phone notification if available

This system runs automatically but can be triggered manually anytime for urgent situations.