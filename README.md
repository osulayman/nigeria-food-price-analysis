# Nigeria Food Price Analysis (2002–2023)

## Overview
A comprehensive analysis of food price dynamics in Nigeria using 
World Food Programme (WFP) VAM monitoring data covering 51,106 price 
records across 14 states, 42 commodities and 21 years (2002–2023).

## Key Questions Answered
- How have food prices changed over 21 years?
- Which states face the highest food costs and why?
- How much of the price increase is Naira depreciation vs real inflation?
- When during the year are households most vulnerable?
- Which commodities have become unaffordable since 2020?
- How large is the retail markup over wholesale prices?

## Key Findings
| Finding | Detail |
|---|---|
| Price increase since 2020 | 54–89% across all major staples |
| Naira depreciation | ₦120/$ in 2002 → ₦598/$ in 2023 |
| Conflict premium | Borno and Adamawa 50–60% above national average |
| Retail markup | 40–100% above wholesale consistently |
| Lean season premium | 12–15% above harvest season lows |
| Most affected foods | Sorghum +89%, Gari +88%, Groundnuts +83% |

## Tools Used
- Python 3
- Pandas — data cleaning and analysis
- Matplotlib — data visualisation
- Seaborn — heatmap
- Jupyter Notebook

## Data Source
World Food Programme — VAM Food Security Analysis  
Available at: data.humdata.org

## How to Run
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Open `nigeria_food_price_analysis.ipynb` in Jupyter
4. Run all cells from top to bottom

## Charts Generated
| Chart | Description |
|---|---|
| Price Trends | 8 staple commodities 2002–2023 |
| Regional Comparison | State-level price gap vs national average |
| Naira Depreciation | NGN vs USD and implied exchange rate |
| Seasonality | Monthly price patterns and lean season |
| Category Analysis | 6 food categories trend and ranking |
| Retail vs Wholesale | Markup percentage and absolute gap |
| Affordability Ranking | Before vs after 2020 comparison |
| State × Commodity Heatmap | Operational price reference matrix |
