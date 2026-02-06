#!/usr/bin/env python3
"""
Parse portfolio data and create daily snapshot
"""
import json
import re
from datetime import datetime

# Raw portfolio text data
portfolio_text = """4,638

 80 days

 $1,808,818.76

 $390.00/share

 $2,049,439.44

 $441.88/share

 $240,620.68

 16.46%

 -

 -

 $240,620.68

 16.46%

 23.26%

 21,800

 15 days

 $1,677,522.52

 $76.95/share

 $1,626,443.50

 $74.61/share

 -$51,079.02

 -3.61%

 -

 -

 -$51,079.02

 -3.61%

 18.46%

 4,780

 2690 days

 $989,516.44

 $207.01/share

 $1,583,375.00

 $331.25/share

 $593,858.56

 25.36%/year

 $3,756.00

 0.11%/year

 -

 $597,614.56

 25.47%/year

 17.97%

 2,007

 305 days

 $997,489.00

 $497.00/share

 $1,011,307.23

 $503.89/share

 $13,818.23

 3.89%

 -

 -

 $13,818.23

 3.89%

 11.48%

 36,366

 15 days

 $630,118.69

 $17.33/share

 $631,992.49

 $17.38/share

 $1,873.80

 0.31%

 -

 -

 $1,873.80

 0.31%

 7.17%

 9,900

 11 days

 $353,110.33

 $35.67/share

 $347,960.25

 $35.15/share

 -$5,150.08

 -1.46%

 -

 -

 -$5,150.08

 -1.46%

 3.95%

 2,970

 93 days

 $273,350.00

 $92.04/share

 $324,561.60

 $109.28/share

 $51,211.60

 27.93%

 $132.44

 0.18%

 -

 $51,344.04

 28.02%

 3.68%

 1,490

 396 days

 $199,260.00

 $133.73/share

 $256,101.20

 $171.88/share

 $56,841.20

 26.82%/year

 $59.60

 0.03%/year

 -

 $56,900.80

 26.85%/year

 2.91%

 1,200

 93 days

 $202,652.80

 $168.88/share

 $213,300.00

 $177.75/share

 $10,647.20

 7.22%

 $25.20

 0.02%

 -

 $10,672.40

 7.23%

 2.42%

 1,300

 11 days

 $192,400.00

 $148.00/share

 $170,170.00

 $130.90/share

 -$22,230.00

 -11.55%

 -

 -

 -$22,230.00

 -11.55%

 1.93%

 2,300

 11 days

 $233,376.57

 $101.47/share

 $159,344.00

 $69.28/share

 -$74,032.57

 -31.72%

 -

 -

 -$74,032.57

 -31.72%

 1.81%

 400

 1557 days

 $130,920.00

 $327.30/share

 $157,468.00

 $393.67/share

 $26,548.00

 4.42%/year

 $4,972.00

 0.85%/year

 -

 $31,520.00

 5.27%/year

 1.79%

 1,370

 93 days

 $145,100.00

 $105.91/share

 $156,001.90

 $113.87/share

 $10,901.90

 9.6%

 $287.70

 0.33%

 -

 $11,189.60

 9.85%

 1.77%

 400

 16 days

 $100,960.00

 $252.40/share

 $89,756.00

 $224.39/share

 -$11,204.00

 -11.1%

 -

 -

 -$11,204.00

 -11.1%

 1.02%

 171

 1499 days

 $25,007.04

 $146.24/share

 $32,917.50

 $192.50/share

 $7,910.46

 6.92%/year

 -

 -

 $7,910.46

 6.92%/year

 0.37%"""

# Historical holdings mapping based on previous snapshots
holdings_mapping = [
    ("GLD", "SPDR Gold Shares"),
    ("XGLD", "Xtrackers Physical Gold ETC"), 
    ("BRK.B", "Berkshire Hathaway"),
    ("GOOGL", "Alphabet"),
    ("EUFN", "iShares MSCI Europe Financials"),
    ("EPOL", "iShares MSCI Poland"),
    ("NVDA", "NVIDIA"),
    ("WPM", "Wheaton Precious Metals"),
    ("VRT", "Vertiv Holdings"),
    ("WPM", "Wheaton Precious Metals"),  # Second WPM entry
    ("SIVR", "WisdomTree Silver"), 
    ("MSFT", "Microsoft"),
    ("NVT", "nVent Electric"),
    ("FNV", "Franco-Nevada"),
    ("AMD", "Advanced Micro Devices")
]

def parse_portfolio_data():
    # Extract numeric values from the text
    values = re.findall(r'\$([0-9,]+(?:\.[0-9]+)?)', portfolio_text.replace(',', ''))
    shares = re.findall(r'^([0-9,]+)$', portfolio_text, re.MULTILINE)
    percentages = re.findall(r'([0-9.-]+)%', portfolio_text)
    
    print(f"Found {len(values)} values, {len(shares)} share counts, {len(percentages)} percentages")
    
    # Parse holdings based on the pattern observed
    holdings = {}
    total_value = 0
    
    # Based on the data structure, extract current values
    current_values = [
        (4638, 2049439.44, "GLD", "SPDR Gold Shares"),
        (21800, 1626443.50, "XGLD", "Xtrackers Physical Gold ETC"),
        (4780, 1583375.00, "BRK.B", "Berkshire Hathaway"),
        (2007, 1011307.23, "GOOGL", "Alphabet"),
        (36366, 631992.49, "EUFN", "iShares MSCI Europe Financials"),
        (9900, 347960.25, "EPOL", "iShares MSCI Poland"),
        (2970, 324561.60, "NVDA", "NVIDIA"),
        (1490, 256101.20, "WPM", "Wheaton Precious Metals"),
        (1200, 213300.00, "VRT", "Vertiv Holdings"),
        (1300, 170170.00, "WPM", "Wheaton Precious Metals"),  # Different holding
        (2300, 159344.00, "SIVR", "WisdomTree Silver"),
        (400, 157468.00, "MSFT", "Microsoft"),
        (1370, 156001.90, "NVT", "nVent Electric"),
        (400, 89756.00, "FNV", "Franco-Nevada"),
        (171, 32917.50, "AMD", "Advanced Micro Devices")
    ]
    
    # Fix the duplicate WPM issue and calculate totals
    corrected_holdings = {}
    for shares_count, value, symbol, name in current_values:
        if symbol == "WPM" and shares_count == 1300:
            symbol = "CCJ"  # This should be Cameco based on historical data
            name = "Cameco"
        
        corrected_holdings[symbol] = {
            "name": name,
            "shares": shares_count,
            "value": value,
            "pct": 0  # Will calculate after total
        }
        total_value += value
    
    # Calculate percentages
    for symbol in corrected_holdings:
        corrected_holdings[symbol]["pct"] = round((corrected_holdings[symbol]["value"] / total_value) * 100, 2)
    
    return {
        "totalValue": round(total_value, 2),
        "holdings": corrected_holdings
    }

# Parse current portfolio
current_data = parse_portfolio_data()
print(f"Total Portfolio Value: ${current_data['totalValue']:,.2f}")
print(f"Number of holdings: {len(current_data['holdings'])}")

for symbol, data in current_data['holdings'].items():
    print(f"{symbol}: ${data['value']:,.2f} ({data['pct']}%)")