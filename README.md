# Wealth Management FP&A & Financial Forecasting

### Crescent Gulf Bank | Independent Financial Analysis Project

An end-to-end financial planning and analysis project for a fictional Dubai-oriented wealth management division with AED 571.21 million in assets under management.

The project examines historical financial performance, wealth management revenue economics, client asset gathering, operating costs, budgeting, scenario forecasting and forecast validation using Microsoft Excel.

## Management Dashboard

<img width="1233" height="1565" alt="image" src="https://github.com/user-attachments/assets/ddc43a49-6207-4b8c-9ac7-6da20f5951a3" />


## Project Objectives

- Understand the financial and commercial economics of a wealth management business.
- Analyze AUM growth, distinguishing organic client flows from market appreciation.
- Evaluate fee revenue, operating expenses, profitability and budget performance.
- Construct quarterly driver-based financial forecasts under multiple scenarios.
- Evaluate forecasts against previously concealed synthetic outcomes and a historical benchmark.
- Communicate findings through an executive management dashboard.

## FY2025 Financial Performance

| Financial Metric | FY2025 |
|---|---:|
| Opening AUM | AED 500.00M |
| Closing AUM | AED 571.21M |
| AUM Growth | 14.24% |
| Net New Money | AED 22.74M |
| Market Appreciation | AED 48.47M |
| Operating Revenue | AED 4.12M |
| Operating Expenses | AED 3.20M |
| Operating Profit | AED 924.93K |
| Operating Margin | 22.44% |
| Cost-to-Income Ratio | 77.56% |

Market appreciation contributed approximately 68% of total AUM growth, while net new money contributed approximately 32%.

Revenue exceeded budget by 3.01%, but operating expenses exceeded budget by 3.88%, limiting operating profit outperformance.

## Analytical Framework

### Historical Financial Analysis

- Monthly AUM reconciliation
- Net new money and market performance decomposition
- Product-level fee revenue analysis
- Operating expense analysis
- Management profit and loss statement
- Budget versus actual variance analysis
- Client segmentation: Mass Affluent, HNW and UHNW
- Relationship manager book analysis

### Driver-Based Forecasting

Quarterly FY2026 forecasts were constructed using assumptions for net new money, market returns, management fee yields, transaction and advisory fee yields, and operating expense growth.

| Forecast Assumption | Bear | Base | Bull |
|---|---:|---:|---:|
| Annual NNM Rate | 2.00% | 4.50% | 6.00% |
| Annual Market Return | -5.00% | 4.00% | 9.00% |
| Management Fee Yield | 0.64% | 0.679% | 0.70% |
| Transaction Fee Yield | 0.07% | 0.09% | 0.11% |
| Operating Expense Growth | 9.00% | 5.00% | 3.00% |

## FY2026 Scenario Analysis

| Metric | Bear | Base | Bull | Simulated Actual |
|---|---:|---:|---:|---:|
| Closing AUM | 553.72M | 620.97M | 659.99M | 618.82M |
| Revenue | 3.99M | 4.58M | 4.98M | 4.28M |
| Operating Expenses | 3.48M | 3.36M | 3.29M | 3.38M |
| Operating Profit | 509.35K | 1,225.43K | 1,686.15K | 899.48K |

All monetary amounts are in AED.

## Forecast Validation

Forecasts were recorded in a separate workbook before the concealed FY2026 synthetic outcomes were revealed.

The finalized driver-based forecast was compared with a simple historical benchmark that repeated the absolute FY2025 AUM increase and historical annual revenue and expense levels.

Absolute percentage error was calculated as:

Absolute Error % = ABS(Actual - Forecast) / ABS(Actual)

| Metric | Driver-Based Forecast Error | Historical Benchmark Error |
|---|---:|---:|
| Closing AUM | 0.35% | 3.81% |
| Revenue | 6.95% | 3.79% |
| Operating Expenses | 0.83% | 5.56% |
| Operating Profit | 36.24% | 2.83% |

The driver-based forecast was more accurate for year-end AUM and expenses, while the historical benchmark was more accurate for revenue and operating profit in this simulation.

The model overestimated AUM during the earlier quarters despite closely predicting the year-end balance. This illustrates why year-end AUM accuracy alone does not guarantee accurate annual fee revenue or profitability forecasts.

All four annual simulated financial outcomes fell within their respective Bear–Bull scenario ranges.

## Management Recommendations

1. Strengthen organic asset gathering and client retention to reduce dependence on market appreciation.
2. Improve revenue forecasts by monitoring quarterly average AUM, realized fee yields and product mix.
3. Improve employee and compliance expense monitoring to strengthen operating efficiency.
4. Retain simple historical benchmarks as independent checks on driver-based financial forecasts.

## Tools and Skills

- Microsoft Excel
- Power Query
- PivotTables
- Financial planning and analysis
- Management accounting
- Budget variance analysis
- AUM reconciliation
- Driver-based financial forecasting
- Scenario analysis
- Forecast benchmarking and validation
- Financial dashboard development

## Repository Guide

| File | Description |
|---|---|
| Crescent_Gulf_Bank_Wealth_FP&A.xlsx | Complete financial model and executive dashboard |
| Crescent_Gulf_Bank_Wealth_FP&A Frozen.xlsx | Preserved forecast workbook and values-only prediction snapshot |
| management dashboard.png | Executive dashboard preview |
| Monthly_AUM_2025.csv | Monthly AUM, client flows and client counts |
| Product_Revenue_2025.csv | Product-level AUM and fee revenue |
| Expenses_2025.csv | Monthly operating expenses |
| Budget_2025.csv | Monthly financial budget |
| RM_Performance_2025.csv | Simulated relationship manager books |
| Assumptions_2025.csv | Historical simulation parameters |
| Quarterly_Actuals_2026.csv | Revealed synthetic quarterly outcomes |
| regenerate_2025_only.py | Historical synthetic data regeneration script |
| unlock_2026_after_forecast.py | Original simulation reveal utility |

## How to Explore the Project

1. View the management dashboard above for an executive overview.
2. Download the final Excel workbook to explore the underlying financial analysis and forecasting formulas.
3. Review Scenario_Comparison for the forecast validation results.
4. Examine the Forecast_Snapshot worksheet in the frozen workbook for the preserved predictions.
5. Use the CSV datasets to inspect the underlying financial information.

The final workbook contains saved financial data. Power Query connections may require local source paths to be updated before refreshing.

## Data Reproducibility

The historical data regeneration script reproduces the five core FY2025 financial datasets and generates a validation report.

Run the script with:

`python regenerate_2025_only.py`

The FY2026 simulated outcomes are provided separately.

## Limitations and Disclaimer

Crescent Gulf Bank is fictional. All financial, client and relationship manager information is synthetic and was generated for educational purposes with AI assistance.

The project is intended to demonstrate financial analysis, Excel modeling and analytical reasoning rather than actual banking performance.

The simulation covers a limited historical period and one set of future outcomes. Forecast accuracy within this exercise does not establish predictive reliability in live financial markets.

Relationship manager records are proportionally allocated within client segments, limiting conclusions about individual manager effectiveness.

The Bear, Base and Bull scenarios are assumption-driven financial scenarios rather than probability forecasts or statistical confidence intervals.

This project does not constitute investment advice or represent work undertaken for an actual financial institution.
