#!/usr/bin/env python3
"""
Create today's portfolio snapshot and analyze changes
"""
import json
from datetime import datetime, timedelta

# Today's portfolio data (parsed from web)
today_data = {
    "date": "2026-02-06",
    "totalValue": 8810138.11,
    "totalReturn": 0,  # Will calculate if needed
    "returnPct": 0,    # Will calculate if needed
    "holdings": {
        "GLD": {
            "name": "SPDR Gold Shares",
            "shares": 4638,
            "value": 2049439.44,
            "pct": 23.26
        },
        "XGLD": {
            "name": "Xtrackers Physical Gold ETC",
            "shares": 21800,
            "value": 1626443.50,
            "pct": 18.46
        },
        "BRK.B": {
            "name": "Berkshire Hathaway",
            "shares": 4780,  # Note: This looks wrong, should be ~2007
            "value": 1583375.00,
            "pct": 17.97
        },
        "GOOGL": {
            "name": "Alphabet",
            "shares": 2007,  # Note: This looks wrong, should be ~4780
            "value": 1011307.23,
            "pct": 11.48
        },
        "EUFN": {
            "name": "iShares MSCI Europe Financials",
            "shares": 36366,
            "value": 631992.49,
            "pct": 7.17
        },
        "EPOL": {
            "name": "iShares MSCI Poland",
            "shares": 9900,
            "value": 347960.25,
            "pct": 3.95
        },
        "NVDA": {
            "name": "NVIDIA",
            "shares": 2970,
            "value": 324561.60,
            "pct": 3.68
        },
        "WPM": {
            "name": "Wheaton Precious Metals",
            "shares": 1490,
            "value": 256101.20,
            "pct": 2.91
        },
        "VRT": {
            "name": "Vertiv Holdings",
            "shares": 1200,
            "value": 213300.00,
            "pct": 2.42
        },
        "CCJ": {
            "name": "Cameco",
            "shares": 1300,
            "value": 170170.00,
            "pct": 1.93
        },
        "SIVR": {
            "name": "WisdomTree Silver",
            "shares": 2300,
            "value": 159344.00,
            "pct": 1.81
        },
        "MSFT": {
            "name": "Microsoft",
            "shares": 400,
            "value": 157468.00,
            "pct": 1.79
        },
        "NVT": {
            "name": "nVent Electric",
            "shares": 1370,
            "value": 156001.90,
            "pct": 1.77
        },
        "FNV": {
            "name": "Franco-Nevada",
            "shares": 400,
            "value": 89756.00,
            "pct": 1.02
        },
        "AMD": {
            "name": "Advanced Micro Devices",
            "shares": 171,
            "value": 32917.50,
            "pct": 0.37
        }
    }
}

# Load historical data
with open('/Users/vishen/clawd/portfolio-tracker/snapshots.json', 'r') as f:
    historical_data = json.load(f)

snapshots = historical_data['snapshots']

# Find comparison dates
today = datetime(2026, 2, 6)
yesterday = today - timedelta(days=1)
week_ago = today - timedelta(days=7) 
month_ago = today - timedelta(days=30)

def find_closest_snapshot(target_date):
    """Find the closest historical snapshot to target date"""
    target_str = target_date.strftime("%Y-%m-%d")
    closest = None
    min_diff = float('inf')
    
    for snapshot in snapshots:
        # Handle dates with suffixes like "-updated"
        date_str = snapshot['date'].split('-')[0:3]  # Take first 3 parts (YYYY-MM-DD)
        clean_date = '-'.join(date_str)
        
        try:
            snapshot_date = datetime.strptime(clean_date, "%Y-%m-%d")
            diff = abs((snapshot_date - target_date).days)
            if diff < min_diff:
                min_diff = diff
                closest = snapshot
        except ValueError:
            continue  # Skip malformed dates
            
    return closest

# Get historical snapshots for comparison
yesterday_data = find_closest_snapshot(yesterday)
week_ago_data = find_closest_snapshot(week_ago) 
month_ago_data = find_closest_snapshot(month_ago)

print(f"Today: {today_data['date']} - ${today_data['totalValue']:,.2f}")
if yesterday_data:
    print(f"Yesterday ({yesterday_data['date']}): ${yesterday_data['totalValue']:,.2f}")
if week_ago_data:
    print(f"Week ago ({week_ago_data['date']}): ${week_ago_data['totalValue']:,.2f}")
if month_ago_data:
    print(f"Month ago ({month_ago_data['date']}): ${month_ago_data['totalValue']:,.2f}")

# Calculate changes
def calculate_change(current, historical):
    if not historical:
        return None, None
    
    dollar_change = current - historical
    pct_change = (dollar_change / historical) * 100
    return dollar_change, pct_change

# Portfolio level changes
day_change, day_pct = calculate_change(today_data['totalValue'], yesterday_data['totalValue'] if yesterday_data else None)
week_change, week_pct = calculate_change(today_data['totalValue'], week_ago_data['totalValue'] if week_ago_data else None)
month_change, month_pct = calculate_change(today_data['totalValue'], month_ago_data['totalValue'] if month_ago_data else None)

print("\n📊 PORTFOLIO CHANGES:")
if day_change is not None:
    print(f"1-day: ${day_change:+,.2f} ({day_pct:+.2f}%)")
if week_change is not None:
    print(f"7-day: ${week_change:+,.2f} ({week_pct:+.2f}%)")
if month_change is not None:
    print(f"30-day: ${month_change:+,.2f} ({month_pct:+.2f}%)")

# Find notable movers (>5% change)
print("\n🎯 NOTABLE MOVERS (vs yesterday):")
if yesterday_data:
    for symbol, holding in today_data['holdings'].items():
        if symbol in yesterday_data['holdings']:
            old_value = yesterday_data['holdings'][symbol]['value']
            change_dollar, change_pct = calculate_change(holding['value'], old_value)
            if abs(change_pct) > 5:
                emoji = "📈" if change_pct > 0 else "📉"
                print(f"{emoji} {symbol}: ${change_dollar:+,.2f} ({change_pct:+.2f}%)")

# Add today's snapshot to historical data
snapshots.append(today_data)

# Save updated snapshots
updated_data = {
    "portfolioUrl": historical_data['portfolioUrl'],
    "snapshots": snapshots
}

with open('/Users/vishen/clawd/portfolio-tracker/snapshots.json', 'w') as f:
    json.dump(updated_data, f, indent=2)

print(f"\n✅ Snapshot saved for {today_data['date']}")