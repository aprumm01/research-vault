---
title: "Environmental Burden of United States Data Centers in the Artificial Intelligence Era"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Guidi24.pdf"
type: paper
authors:
  - Gianluca Guidi
  - Francesca Dominici
  - Jonathan Gilmour
  - Kevin Butler
  - Eric Bell
  - Scott Delaney
  - Falco J. Bargagli-Stoffi
year: 2024
venue: "arXiv preprint (arXiv:2411.09786)"
builds_on:
  - "[[The environmental footprint of data centers in the united states (Siddik, 2021)]]"
  - "[[Recalibrating global data center energy-use estimates (Masanet, 2020)]]"
  - "[[Energy and Policy Considerations for Deep Learning in NLP (Strubell, 2019)]]"
supports:
  - "[[Carbon Emissions and Large Neural Network Training (Patterson, 2021)]]"
  - "[[Measuring the carbon intensity of AI in cloud instances (Dodge, 2022)]]"
critiques:
  - "[[The environmental footprint of data centers in the united states (Siddik, 2021)]]"
tensions_with:
  - "[[Corporate sustainability pledges]]"
key_claims:
  - "US data centers account for more than 4% of total US electricity consumption"
  - "56% of data center electricity is derived from fossil fuels"
  - "Data centers generated more than 105 million tons of CO2e (2.18% of US emissions in 2023)"
  - "Data center carbon intensity exceeds the US national average by 48%"
  - "Data center emissions have tripled since 2018 (from 0.5% to 2.18%)"
  - "95% of data centers are located in areas with higher carbon intensity than the national average"
methodology: "Quantitative analysis using data pipeline integrating publicly available data with proprietary data from Baxtel.com; gradient-boosted regression tree model for imputation; generation-weighted average (attributional) approach for CO2e accounting; validated using satellite imagery and Open Street Map"
study_type: empirical
context: "United States, September 2023 to August 2024, 2,132 data centers (78% of all US data centers), 52 balancing authority regions"
---

## Summary

This study introduces a comprehensive data pipeline to estimate the environmental impact of US data centers in the era of artificial intelligence. The authors compiled detailed information on 2,132 US data centers operating between September 2023 and August 2024, determining their electricity consumption, electricity sources, and attributable CO2 equivalent emissions. The research addresses a critical data gap: while data centers are proliferating rapidly due to AI adoption, industry emissions data has been largely unavailable, making effective policymaking difficult.

The key finding is alarming: US data centers now account for over 4% of total US electricity consumption (192.64 TWh annually), with 56% of this electricity derived from fossil fuels. This translates to 105.59 million metric tons of CO2e emissions, representing 2.18% of all US carbon emissions from energy consumption. Most critically, this represents a three-fold increase from the 0.5% estimated for 2018.

## Key Concepts

- **Balancing Authority Region**: A specific geographic region within the US electric grid managed by a single entity responsible for maintaining balance between electricity generation and consumption. The study analyzed 52 such regions.

- **Carbon Intensity**: The amount of CO2e emitted per unit of electricity consumed, measured in grams of CO2e per kilowatt hour (gCO2e/kWh). US data centers averaged 548 gCO2e/kWh, 48% higher than the national average of 369 gCO2e/kWh.

- **Attributional vs. Consequential Approaches**: Attributional methods allocate emissions proportionally to users (used in this study for comprehensive inventory), while consequential methods identify which power plants respond to new energy demand (useful for siting decisions).

- **Capacity Utilization Rate (Uptime)**: The percentage of time a data center operates at maximum capacity. The study assumed a conservative 0.75 (75%) for all data centers.

- **Power Capacity**: The maximum amount of electricity a data center can draw, measured in megawatts (MW). Data centers in the sample ranged from 0.04 to 325 MW, with a mean of 13.75 MW and median of 4.5 MW.

## Key Findings

### Geographic Distribution and Energy Consumption
- Virginia leads with 301 data centers and highest electricity consumption (52.21 TWh, 27% of total)
- Texas ranks second (221 data centers, 18.86 TWh, 13%)
- Oregon third (86 data centers, 15.25 TWh, 8%)
- California fourth (248 data centers, 11.54 TWh, 6%)
- These four states account for over 50% of total data center energy consumption

### Carbon Emissions by State
| State | CO2e (Million Tons) | Rank |
|-------|---------------------|------|
| Virginia | 30.08 | 1 |
| Texas | 9.63 | 2 |
| Oregon | 8.92 | 3 |
| Illinois | 6.23 | 4 |
| Ohio | 5.55 | 5 |
| Iowa | 5.15 | 6 |
| California | 4.37 | 7 |

### Energy Source Mix (All US Data Centers)
- Natural Gas: 40.8%
- Nuclear: 20.6%
- Coal: 15.8%
- Hydro: 8.4%
- Wind: 7.1%
- Solar: 4.2%
- Geothermal: 0.5%
- Oil: 0.2%
- Biomass: 1.8%

### Carbon Intensity Comparisons
- US data centers average: 548 gCO2e/kWh
- US national average: 369 gCO2e/kWh
- Central regions (Colorado, Kansas, Missouri, Wyoming): ~1000 gCO2e/kWh (coal-dependent)
- California (CISO): 373 gCO2e/kWh (cleaner grid)
- France: 58 gCO2e/kWh
- Brazil: 98 gCO2e/kWh

### Industry Context
- Google's 2023 greenhouse gas emissions increased 13% year-over-year
- Microsoft's emissions increased 29% since 2020 baseline
- Both companies cited data centers as the main driver

## Relevance to Sustainable Computing

This paper is highly relevant to sustainable computing research for several reasons:

1. **Quantifies the AI Carbon Problem**: Provides the first comprehensive, data-driven estimate of US data center emissions in the AI era, establishing a critical baseline for policy and research.

2. **Exposes Geographic Disparities**: Demonstrates that data center siting decisions have major carbon implications, with 95% of facilities located in areas with above-average carbon intensity despite tech companies' renewable energy pledges.

3. **Reveals Policy Gaps**: Shows that policy has lagged behind data center growth, though regulatory attention is increasing at state and federal levels.

4. **Provides Tools for Intervention**: The authors developed a public web platform (https://tinyurl.com/4k8fbhka) for tracking data center carbon footprints at multiple geographic levels.

5. **Highlights Attributional vs. Consequential Tension**: Notes that different emission accounting methods are appropriate for different decisions (inventory vs. siting), a key consideration for sustainable computing policy.

6. **Documents Three-Fold Increase**: The jump from 0.5% (2018) to 2.18% (2023) of US emissions in just five years demonstrates the urgency of addressing computing's environmental footprint.

## Citation

Guidi, G., Dominici, F., Gilmour, J., Butler, K., Bell, E., Delaney, S., & Bargagli-Stoffi, F. J. (2024). Environmental burden of United States data centers in the artificial intelligence era. *arXiv preprint arXiv:2411.09786*. https://arxiv.org/abs/2411.09786
