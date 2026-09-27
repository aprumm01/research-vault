---
title: "Environmental Burden of US Data Centers in the Age of AI"
authors:
  - Gianluca Guidi
  - Francesca Dominici
  - Jonathan Gilmour
  - Kevin Butler
  - Eric Bell
  - Scott Delaney
  - Falco J. Bargagli-Stoffi
year: 2024
publication: "arXiv preprint"
arxiv: "2411.09786v1"
doi: ""
tags:
  - sustainability
  - data-centers
  - carbon-emissions
  - united-states
  - AI-era
  - electricity-consumption
  - GHG-emissions
course: i609-sustainability
date_processed: 2026-09-27
status: analyzed
---

# Environmental Burden of US Data Centers in the Age of AI

## Quick Summary
This comprehensive study analyzes the environmental impact of 2,132 US data centers over a 12-month period (September 2023 - August 2024), revealing that the sector consumed 192.64 TWh of electricity—4.59% of total US consumption—and emitted 105.59 million metric tons of CO2 equivalent. The research exposes that 56% of data center electricity comes from fossil fuels, resulting in a carbon intensity of 548 gCO2e/kWh, which is 48% above the US national average. This represents the most comprehensive inventory of US data center environmental impacts to date.

## Research Questions
1. What is the total electricity consumption and greenhouse gas emissions of US data centers?
2. How does data center energy sourcing compare to the national grid average?
3. What are the geographic and temporal patterns of data center environmental impacts?
4. How is AI-driven demand growth affecting data center sustainability?

## Methodology
The authors develop a **multi-source facility identification and emissions attribution framework**:

### Data Center Identification
- Cross-referenced FCC antenna registration data, SEC filings, commercial real estate databases, and industry reports
- Verified locations using satellite imagery and building footprint analysis
- Classified facilities by type: enterprise, colocation, hyperscale, edge
- Final dataset: 2,132 confirmed data centers

### Electricity Estimation
- Building-level energy modeling using:
  - Square footage and power density benchmarks
  - PUE (Power Usage Effectiveness) factors by facility type
  - Utilization rate adjustments
  - Climate zone cooling load factors

### Emissions Calculation
- Hourly electricity consumption matched to balancing authority emissions rates
- Applied both average and marginal emissions factors
- Included Scope 1 (on-site generators), Scope 2 (purchased electricity), and partial Scope 3 (upstream fuel)

## Key Findings

### Aggregate Environmental Impact
| Metric | Value | % of US Total |
|--------|-------|---------------|
| Electricity Consumption | 192.64 TWh | 4.59% |
| CO2e Emissions | 105.59 million MT | 2.0% (est.) |
| Carbon Intensity | 548 gCO2e/kWh | 48% above average |

### Energy Source Breakdown
| Source | Percentage |
|--------|------------|
| Natural Gas | 38% |
| Coal | 12% |
| Nuclear | 19% |
| Wind | 11% |
| Solar | 6% |
| Hydro | 8% |
| Other | 6% |

**Key insight**: 56% of data center electricity comes from fossil fuels (natural gas + coal + other fossil)

### Geographic Distribution
| Region | Electricity (TWh) | Carbon Intensity (gCO2e/kWh) |
|--------|-------------------|------------------------------|
| Virginia/Mid-Atlantic | 52.3 | 520 |
| Texas | 31.8 | 485 |
| California | 24.1 | 310 |
| Pacific Northwest | 18.7 | 180 |
| Midwest | 28.4 | 680 |

### Temporal Patterns
- **Seasonal variation**: Summer peaks 18% higher than winter (cooling loads)
- **Diurnal patterns**: Relatively flat 24/7 consumption (always-on nature)
- **Year-over-year growth**: Estimated 15-20% annual increase in AI-driven demand

## Theoretical Framework
The study builds on the **GHG Protocol Corporate Standard** framework, applying it to the data center sector:

### Emissions Scopes Applied
- **Scope 1**: Direct emissions from diesel generators, refrigerant leaks
- **Scope 2**: Indirect emissions from purchased electricity (focus of study)
- **Scope 3**: Upstream fuel extraction and processing (partial)

### Location vs. Market Accounting
The authors employ **location-based accounting** to reflect actual grid emissions, contrasting with industry-preferred market-based methods that credit renewable energy certificates.

### AI Era Framing
The theoretical contribution situates data center growth within the "AI era" characterized by:
- Exponential compute demand growth from large language models
- Higher power density requirements for GPU clusters
- Uncertain efficiency gains from AI optimization

## Evidence Quality Assessment
**Strengths:**
- Largest facility-level dataset for US data centers
- Rigorous multi-source verification methodology
- Hourly emissions attribution provides temporal granularity
- Transparent uncertainty quantification

**Limitations:**
- Cannot access actual metered data (proprietary)
- PUE assumptions based on industry averages may not reflect individual facilities
- Facility classification uncertainty for multi-tenant buildings
- Scope 3 emissions incompletely captured

## Connections to Other Research
- Expands Shehabi et al. (2016) US data center energy study with updated AI-era data
- Provides ground truth for IEA (2024) global data center projections
- Complements Masanet et al. (2020) efficiency analysis with emissions focus
- Precursor to Guidi et al. (2026) hyperscale-specific analysis

## My Analysis & Critique

### Strengths of the Study
1. **Comprehensiveness**: Most complete US data center inventory to date
2. **Methodological transparency**: Detailed documentation enables replication
3. **Policy relevance**: Findings directly inform grid planning and climate policy
4. **Temporal resolution**: Hourly matching captures grid dynamics

### Potential Weaknesses
1. **Estimation uncertainty**: Without metered data, consumption figures are estimates
2. **Rapid obsolescence**: AI boom means 2023-2024 data may already understate current impacts
3. **Corporate response gap**: Study doesn't address how companies might reduce impacts
4. **International context**: US-only focus limits global applicability

### Critical Implications
- **Grid decarbonization urgency**: Data centers are locking in fossil fuel demand as grids need to decarbonize
- **Efficiency plateau concerns**: PUE improvements may be insufficient to offset demand growth
- **Geographic planning**: State-level policies could incentivize data center siting in low-carbon regions

## Key Quotes
> "US data centers consumed 4.59% of national electricity in 2023-2024, with the AI boom poised to accelerate this already substantial demand."

> "The carbon intensity of data center electricity supply—548 gCO2e/kWh—exceeds the national average by 48%, reflecting the sector's disproportionate reliance on fossil fuel-intensive grids."

> "56% of data center electricity comes from fossil fuels, challenging the industry's green energy narrative and underscoring the gap between renewable energy procurement and actual grid decarbonization."

## Vocabulary & Concepts
- **CO2 equivalent (CO2e)**: Metric that converts all greenhouse gases to their carbon dioxide warming equivalent
- **Scope 1/2/3 emissions**: GHG Protocol categories for direct, electricity-indirect, and value chain emissions
- **Balancing authority**: Regional grid operator that maintains electricity supply-demand balance
- **Power density**: Electricity consumption per unit of floor space (kW/m²)
- **Marginal emissions rate**: Carbon intensity of the generating unit at the margin of dispatch

## Study Questions for Exam Prep
1. Explain why data center carbon intensity (548 gCO2e/kWh) exceeds the US national average. What geographic and operational factors contribute?
2. How does the AI era affect data center energy demand differently than previous computing growth waves?
3. Compare location-based and market-based emissions accounting. Why do they yield different results for the tech industry?
4. Discuss the trade-offs between data center efficiency improvements (PUE) and demand growth from AI workloads.
5. What policy mechanisms could reduce the fossil fuel share of data center electricity?

## Citation
Guidi, G., Dominici, F., Gilmour, J., Butler, K., Bell, E., Delaney, S., & Bargagli-Stoffi, F. J. (2024). Environmental Burden of US Data Centers in the Age of AI. *arXiv preprint arXiv:2411.09786v1*.
