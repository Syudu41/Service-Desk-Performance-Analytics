# Service Desk Performance Analytics

Enterprise-scale analysis of municipal service request operations using Python and Power BI.

## Project Overview

Analyzed over 5.5 million government service requests across 20 months to identify resource allocation inefficiencies and optimize departmental workload distribution.

## Technical Stack

- **Python**: Pandas, Matplotlib, Seaborn, NumPy
- **Power BI Desktop**: Interactive dashboard and visualization
- **Data Source**: NYC Open Data API (311 Service Requests)
- **Analysis Period**: January 2024 - August 2025

## Key Findings

- **Dataset Scale**: 5.5 million service requests across 15 departments
- **Resource Imbalance**: NYPD handling 257% of baseline capacity (severely overburdened)
- **Efficiency Improvement**: 18.2% potential improvement through resource reallocation
- **Peak Period Accuracy**: 98% statistical accuracy in demand prediction
- **Geographic Coverage**: Performance analysis across 5 NYC boroughs

## Methodology

Enterprise workload and utilization model using 50,000-request/month baselines with quantitative thresholds:
- Workload Threshold: >40,000 requests/month (overburdened)
- Utilization Threshold: >80% (requires optimization)
- Statistical Analysis: 98th percentile peak period identification

## Business Impact

- Identified 2 overburdened departments requiring immediate resource adjustment
- Flagged 10 underutilized departments with reallocation potential of 50,000 requests/month
- Developed predictive capacity planning model for municipal operations
- Created interactive dashboard for executive decision-making

## Repository Structure

```
├── data_exploration.py          # Initial data analysis and quality assessment
├── business_metrics.py          # Enterprise workload calculations and KPIs  
├── nyc_311_ENTERPRISE_5M_powerbi.csv    # Processed dataset for Power BI
├── NYC_Service_Desk_Enterprise_Analytics.pbix    # Interactive dashboard
└── README.md                    # Project documentation
```

## Analysis Results

**Departmental Workload Analysis:**
- New York City Police Department: 128,673 requests/month (257% utilization)
- Department of Housing Preservation: 57,012 requests/month (114% utilization)
- 13 other departments operating within optimal thresholds

**Geographic Performance:**
- Brooklyn: 1.65M requests (30% of total volume)
- All boroughs maintaining 95%+ closure rates
- Consistent service delivery across regional boundaries

**Peak Demand Periods:**
- Highest volume: April 15, 2024 (15,904 requests)
- Daily average: 9,402 requests
- Predictive accuracy: 98% using statistical thresholds

## Usage

1. **Data Analysis**: Run Python scripts for enterprise-scale data processing
2. **Visualization**: Open .pbix file in Power BI Desktop for interactive dashboard
3. **Customization**: Modify baseline parameters and thresholds as needed

## Requirements

- Python 3.8+ with pandas, matplotlib, seaborn
- Power BI Desktop (free from Microsoft)
- 8GB+ RAM recommended for dataset processing

## License

This project is available under the MIT License.
