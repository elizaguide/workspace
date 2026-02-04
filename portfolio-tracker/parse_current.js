// Parse current portfolio data from SimplePortfolio
const rawData = `4,638
 78 days
 $1,808,818.76
 $390.00/share
 $1,981,028.94
 $427.13/share
 $172,210.18
 11.81%
 -
 -
 $172,210.18
 11.81%
 22.46%
 4,780
 2688 days
 $989,516.44
 $207.01/share
 $1,642,838.20
 $343.69/share
 $653,321.76
 26.87%/year
 $3,756.00
 0.11%/year
 -
 $657,077.76
 26.98%/year
 18.63%
 21,800
 13 days
 $1,677,522.52
 $76.95/share
 $1,561,752.00
 $71.64/share
 -$115,770.52
 -8.39%
 -
 -
 -$115,770.52
 -8.39%
 17.71%
 2,007
 303 days
 $997,489.00
 $497.00/share
 $977,991.03
 $487.29/share
 -$19,497.97
 -5.46%
 -
 -
 -$19,497.97
 -5.46%
 11.09%
 36,366
 13 days
 $630,118.69
 $17.33/share
 $648,595.21
 $17.84/share
 $18,476.51
 3.06%
 -
 -
 $18,476.51
 3.06%
 7.35%
 2,970
 91 days
 $273,350.00
 $92.04/share
 $357,023.70
 $120.21/share
 $83,673.70
 46.99%
 $132.44
 0.31%
 -
 $83,806.14
 47.09%
 4.05%
 9,900
 9 days
 $353,110.33
 $35.67/share
 $347,391.00
 $35.09/share
 -$5,719.33
 -1.62%
 -
 -
 -$5,719.33
 -1.62%
 3.94%
 1,490
 394 days
 $199,260.00
 $133.73/share
 $276,558.90
 $185.61/share
 $77,298.90
 36.61%/year
 $59.60
 0.03%/year
 -
 $77,358.50
 36.64%/year
 3.14%
 1,200
 91 days
 $202,652.80
 $168.88/share
 $228,012.00
 $190.01/share
 $25,359.20
 17.5%
 $25.20
 0.03%
 -
 $25,384.40
 17.52%
 2.59%
 1,300
 9 days
 $192,400.00
 $148.00/share
 $171,873.00
 $132.21/share
 -$20,527.00
 -10.67%
 -
 -
 -$20,527.00
 -10.67%
 1.95%
 400
 1555 days
 $130,920.00
 $327.30/share
 $169,348.00
 $423.37/share
 $38,428.00
 6.23%/year
 $4,972.00
 0.83%/year
 -
 $43,400.00
 7.06%/year
 1.92%
 2,300
 9 days
 $233,376.57
 $101.47/share
 $163,116.00
 $70.92/share
 -$70,260.57
 -30.11%
 -
 -
 -$70,260.57
 -30.11%
 1.85%
 1,370
 91 days
 $145,100.00
 $105.91/share
 $158,632.30
 $115.79/share
 $13,532.30
 12.01%
 -
 -
 $13,532.30
 12.01%
 1.8%
 400
 14 days
 $100,960.00
 $252.40/share
 $93,196.00
 $232.99/share
 -$7,764.00
 -7.69%
 -
 -
 -$7,764.00
 -7.69%
 1.06%
 171
 1497 days
 $25,007.04
 $146.24/share
 $42,112.17
 $246.27/share
 $17,105.13
 13.55%/year
 -
 -
 $17,105.13
 13.55%/year
 0.48%`;

// Define holdings based on known symbols and structure
const holdings = [
  { symbol: "GLD", name: "SPDR Gold Shares" },
  { symbol: "GOOGL", name: "Alphabet" },
  { symbol: "XGLD", name: "Xtrackers Physical Gold ETC" },
  { symbol: "BRK.B", name: "Berkshire Hathaway" },
  { symbol: "EUFN", name: "iShares MSCI Europe Financials" },
  { symbol: "NVDA", name: "NVIDIA" },
  { symbol: "EPOL", name: "iShares MSCI Poland" },
  { symbol: "WPM", name: "Wheaton Precious Metals" },
  { symbol: "VRT", name: "Vertiv Holdings" },
  { symbol: "CCJ", name: "Cameco" },
  { symbol: "MSFT", name: "Microsoft" },
  { symbol: "SIVR", name: "WisdomTree Silver" },
  { symbol: "NVT", name: "nVent Electric" },
  { symbol: "FNV", name: "Franco-Nevada" },
  { symbol: "AMD", name: "Advanced Micro Devices" }
];

// Parse the raw data
const lines = rawData.trim().split('\n').map(l => l.trim()).filter(l => l);
const parsed = {};
let totalValue = 0;

let i = 0;
for (const holding of holdings) {
  if (i >= lines.length) break;
  
  // Extract pattern: shares, days, cost_value, cost_per_share, current_value, current_per_share, gain_loss, return_pct, ...
  const shares = parseInt(lines[i].replace(/,/g, ''));
  const currentValue = parseFloat(lines[i + 4].replace(/\$|,/g, ''));
  const returnPct = parseFloat(lines[i + 10].replace(/%/g, ''));
  const portfolioPct = parseFloat(lines[i + 12].replace(/%/g, ''));
  
  parsed[holding.symbol] = {
    name: holding.name,
    shares: shares,
    value: currentValue,
    return: returnPct,
    pct: portfolioPct
  };
  
  totalValue += currentValue;
  
  // Move to next holding (13 lines per holding based on pattern)
  i += 13;
}

const snapshot = {
  date: "2026-02-04",
  totalValue: totalValue,
  totalReturn: 0, // Will calculate after comparison
  returnPct: 0,
  holdings: parsed
};

console.log(JSON.stringify(snapshot, null, 2));