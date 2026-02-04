#!/usr/bin/env python3
"""
Portfolio Analysis Tool
Analyzes daily portfolio changes and identifies new purchases vs market gains
"""
import json
import csv
from datetime import datetime
from typing import Dict, List, Tuple

def load_snapshots(file_path: str) -> Dict:
    """Load portfolio snapshots from JSON file"""
    with open(file_path, 'r') as f:
        return json.load(f)

def identify_new_purchases(prev_holdings: Dict, curr_holdings: Dict, threshold: float = 0.15) -> List[str]:
    """
    Identify positions that likely had new share purchases
    Based on unrealistic single-day price movements
    """
    new_purchases = []
    
    for symbol in curr_holdings:
        if symbol not in prev_holdings:
            new_purchases.append(f"{symbol} (NEW)")
            continue
            
        prev_value = prev_holdings[symbol]['value']
        curr_value = curr_holdings[symbol]['value']
        change_pct = (curr_value - prev_value) / prev_value
        
        # If increase is >15% in one day, likely a purchase
        if change_pct > threshold:
            new_purchases.append(f"{symbol} (+{change_pct:.1%})")
    
    return new_purchases

def calculate_true_market_gain(prev_snap: Dict, curr_snap: Dict) -> Tuple[float, float, List[str]]:
    """Calculate actual market gain excluding new purchases"""
    total_change = curr_snap['totalValue'] - prev_snap['totalValue']
    
    # Identify positions with likely new purchases
    purchases = identify_new_purchases(prev_snap['holdings'], curr_snap['holdings'])
    
    # Calculate purchase amounts (improved with share data when available)
    purchase_amount = 0
    for symbol in curr_snap['holdings']:
        if symbol not in prev_snap['holdings']:
            # New position - entire value is purchase
            purchase_amount += curr_snap['holdings'][symbol]['value']
        else:
            prev_val = prev_snap['holdings'][symbol]['value']
            curr_val = curr_snap['holdings'][symbol]['value']
            
            # Check if we have share count data
            if 'shares' in curr_snap['holdings'][symbol] and 'shares' in prev_snap['holdings'][symbol]:
                prev_shares = prev_snap['holdings'][symbol]['shares']
                curr_shares = curr_snap['holdings'][symbol]['shares']
                
                if curr_shares > prev_shares:
                    # Calculate purchase based on share increase and current price
                    share_increase = curr_shares - prev_shares
                    current_price = curr_val / curr_shares
                    purchase_amount += share_increase * current_price
            else:
                # Fallback to price change analysis
                change_pct = (curr_val - prev_val) / prev_val
                if change_pct > 0.15:  # Likely purchase
                    estimated_purchase = curr_val - prev_val * 1.05
                    purchase_amount += max(0, estimated_purchase)
    
    market_gain = total_change - purchase_amount
    
    return market_gain, purchase_amount, purchases

def main():
    data = load_snapshots('snapshots.json')
    snapshots = data['snapshots']
    
    print("Portfolio Analysis Summary")
    print("=" * 40)
    
    for i in range(1, len(snapshots)):
        prev_snap = snapshots[i-1]
        curr_snap = snapshots[i]
        
        market_gain, purchases, purchase_list = calculate_true_market_gain(prev_snap, curr_snap)
        
        print(f"\n{prev_snap['date']} → {curr_snap['date']}")
        print(f"Total Change: ${curr_snap['totalValue'] - prev_snap['totalValue']:,.0f}")
        print(f"Market Gain: ${market_gain:,.0f}")
        print(f"New Purchases: ${purchases:,.0f}")
        if purchase_list:
            print(f"Positions with purchases: {', '.join(purchase_list)}")

if __name__ == "__main__":
    main()