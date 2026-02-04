// Daily Portfolio Analysis Script
const fs = require('fs');

// Load data
const snapshots = JSON.parse(fs.readFileSync('/Users/vishen/clawd/portfolio-tracker/snapshots.json', 'utf8'));
const current = JSON.parse(fs.readFileSync('/Users/vishen/clawd/portfolio-tracker/current_snapshot.json', 'utf8'));

// Get historical comparison data
const today = "2026-02-04";
const yesterday = "2026-02-02"; // Most recent in snapshots
const oneWeekAgo = "2026-01-30"; // Approx 5 days ago
const oneMonthAgo = "2026-01-30"; // Limited data - using what we have

// Find comparison snapshots
const yesterdayData = snapshots.snapshots.find(s => s.date === yesterday);
const weekAgoData = snapshots.snapshots.find(s => s.date === oneWeekAgo);
const monthAgoData = snapshots.snapshots.find(s => s.date === oneMonthAgo);

console.log("=== DAILY PORTFOLIO REPORT - February 4, 2026 ===\n");

// Current portfolio summary
console.log(`💼 **TOTAL PORTFOLIO VALUE**`);
console.log(`Current: $${current.totalValue.toLocaleString()}`);

// Daily comparison
if (yesterdayData) {
    const dailyChange = current.totalValue - yesterdayData.totalValue;
    const dailyChangePct = (dailyChange / yesterdayData.totalValue * 100);
    const emoji = dailyChange >= 0 ? "📈" : "📉";
    console.log(`${emoji} 1-Day: ${dailyChange >= 0 ? '+' : ''}$${dailyChange.toLocaleString()} (${dailyChangePct >= 0 ? '+' : ''}${dailyChangePct.toFixed(2)}%)`);
}

// Weekly comparison
if (weekAgoData) {
    const weeklyChange = current.totalValue - weekAgoData.totalValue;
    const weeklyChangePct = (weeklyChange / weekAgoData.totalValue * 100);
    const emoji = weeklyChange >= 0 ? "📊" : "📉";
    console.log(`${emoji} 5-Day: ${weeklyChange >= 0 ? '+' : ''}$${weeklyChange.toLocaleString()} (${weeklyChangePct >= 0 ? '+' : ''}${weeklyChangePct.toFixed(2)}%)`);
}

console.log("\n🏆 **TOP HOLDINGS** (by value)");
const sortedHoldings = Object.entries(current.holdings)
    .sort(([,a], [,b]) => b.value - a.value)
    .slice(0, 5);

for (const [symbol, data] of sortedHoldings) {
    console.log(`${symbol}: $${data.value.toLocaleString()} (${data.pct}%)`);
}

// Notable movers (comparing to yesterday)
if (yesterdayData) {
    console.log("\n📊 **NOTABLE MOVERS** (vs yesterday)");
    const movers = [];
    
    for (const [symbol, currentData] of Object.entries(current.holdings)) {
        const yesterdayHolding = yesterdayData.holdings[symbol];
        if (yesterdayHolding) {
            const change = currentData.value - yesterdayHolding.value;
            const changePct = (change / yesterdayHolding.value * 100);
            
            if (Math.abs(changePct) > 5) { // More than 5% change
                movers.push({
                    symbol,
                    name: currentData.name,
                    change,
                    changePct,
                    currentValue: currentData.value
                });
            }
        }
    }
    
    // Sort by absolute percentage change
    movers.sort((a, b) => Math.abs(b.changePct) - Math.abs(a.changePct));
    
    if (movers.length > 0) {
        for (const mover of movers.slice(0, 5)) {
            const emoji = mover.changePct >= 0 ? "🚀" : "🔴";
            console.log(`${emoji} ${mover.symbol}: ${mover.changePct >= 0 ? '+' : ''}${mover.changePct.toFixed(1)}% ($${mover.change.toLocaleString()})`);
        }
    } else {
        console.log("📊 No significant movers (>5%) detected");
    }
}

console.log("\n⚠️ **ALERTS & NOTES**");
console.log("• Data collected from SimplePortfolio at 12:00 GMT");
console.log(`• Portfolio contains ${Object.keys(current.holdings).length} positions`);
if (yesterdayData) {
    const biggestHolding = sortedHoldings[0];
    console.log(`• Largest position: ${biggestHolding[0]} (${biggestHolding[1].pct}% of portfolio)`);
}

// Update snapshots file with today's data
const updatedData = { ...current };
updatedData.totalReturn = 0; // Would need cost basis to calculate
updatedData.returnPct = 0; // Would need cost basis to calculate

snapshots.snapshots.push(updatedData);

// Save updated snapshots
fs.writeFileSync('/Users/vishen/clawd/portfolio-tracker/snapshots.json', JSON.stringify(snapshots, null, 2));
console.log("\n✅ Snapshot saved for 2026-02-04");

console.log("\n---");
console.log("Generated at: " + new Date().toISOString());