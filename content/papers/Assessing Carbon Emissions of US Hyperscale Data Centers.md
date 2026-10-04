---
title: Assessing Carbon Emissions of US Hyperscale Data Centers
authors:
- Gianluca Guidi
- Francesca Dominici
- Tiziano Squartini
- Callaway Sprinkle
- Jonathan Gilmour
- Kevin Butler
- Eric Bell
- Scott Delaney
- Falco J. Bargagli-Stoffi
year: 2026
publication: arXiv preprint
arxiv: 2606.05420v1
doi: ''
tags:
- sustainability
- hyperscale-data-centers
- carbon-emissions
- united-states
- AI-infrastructure
- electricity-consumption
course: i609-sustainability
date_processed: 2026-09-27
status: analyzed
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with:
- '[[concepts/Technological Determinism]]'
supports:
- '[[concepts/AI Hallucinations]]'
- '[[concepts/Fauxtomation]]'
key_claims:
- US hyperscale data centers consumed 68-99 TWh of electricity and emitted 37-54 million
  metric tons of CO2 over a 12-month period (May 2024 - April 2025)
- The carbon intensity of electricity consumed by hyperscale data centers is 545 gCO2/kWh,
  which is 48% higher than the US national average of 368 gCO2/kWh
- Virginia hosts 142 hyperscale data centers (35% of US capacity) consuming 21 TWh
  annually, with carbon intensity of 520-580 gCO2/kWh despite corporate renewable
  energy claims
- Location-based emissions accounting reveals that corporate market-based renewable
  energy claims obscure actual grid-level carbon emissions, exposing a transparency
  gap between sustainability reporting and environmental impact
- Balancing authority region attribution provides more accurate carbon accounting
  than national or regional averages by matching each facility's consumption to its
  specific grid's hourly carbon intensity
methodology: '[[methods/Mixed Methods]]'
sample_size: 403
sample_type: US hyperscale data centers operated by major cloud providers and tech
  companies
context: United States electrical grid infrastructure and data center operations over
  12-month period (May 2024 - April 2025)
study_type: empirical
---

# Assessing Carbon Emissions of US Hyperscale Data Centers

## Quick Summary
This groundbreaking study provides the first comprehensive carbon emissions assessment specifically for US hyperscale data centers (HDCs), analyzing 403 facilities over a 12-month period from May 2024 to April 2025. The research reveals that HDCs consumed 68-99 TWh of electricity and emitted 37-54 million metric tons of CO2, with a carbon intensity of 545 gCO2/kWh—48% higher than the US national average. Virginia emerges as the dominant hub with 142 HDCs consuming 21 TWh, while the study exposes significant disparities between corporate renewable energy claims and actual grid emissions.

## Research Questions
1. What is the actual electricity consumption and carbon footprint of US hyperscale data centers?
2. How does the carbon intensity of HDC electricity supply compare to national averages?
3. What are the geographic patterns of HDC deployment and their environmental implications?
4. How do corporate renewable energy claims compare to actual grid-level emissions?

## Methodology
The authors employ a novel **balancing authority region attribution method**:

- **Data collection**: Identified 403 hyperscale data centers across the US using multiple data sources (FCC filings, SEC disclosures, satellite imagery, industry databases)
- **Geographic mapping**: Linked each HDC to its corresponding balancing authority region (electrical grid operator)
- **Electricity estimation**: Combined building footprint analysis, industry benchmarks, and reported capacity data
- **Carbon calculation**: Applied hourly marginal emissions rates from balancing authorities to estimate real-time carbon intensity
- **Temporal scope**: 12-month study period (May 2024 - April 2025)

### Key Methodological Innovation
Unlike studies using national or regional averages, this research matches each facility's electricity consumption to its specific grid's hourly carbon intensity, providing more accurate location-based emissions accounting.

## Key Findings

### Aggregate Electricity and Emissions
| Metric | Low Estimate | High Estimate |
|--------|--------------|---------------|
| Electricity Consumption | 68 TWh | 99 TWh |
| CO2 Emissions | 37 million MT | 54 million MT |
| Carbon Intensity | 545 gCO2/kWh | 545 gCO2/kWh |

### Geographic Distribution
| State | Number of HDCs | Electricity (TWh) | Key Operators |
|-------|----------------|-------------------|---------------|
| Virginia | 142 | 21 | Amazon, Microsoft, Google |
| Texas | 58 | 14 | Meta, Google, Oracle |
| California | 41 | 9 | Google, Apple, Meta |
| Oregon | 28 | 7 | Google, Amazon, Facebook |

### Carbon Intensity Comparison
- **HDC average**: 545 gCO2/kWh
- **US national average**: 368 gCO2/kWh
- **Difference**: 48% higher carbon intensity for HDCs

### Critical Finding: Virginia's Carbon Problem
Virginia hosts 35% of US hyperscale capacity but relies heavily on fossil fuel generation:
- Carbon intensity: 520-580 gCO2/kWh (depending on time of year)
- Primary fuel mix: Natural gas (45%), nuclear (30%), coal (15%)
- Despite corporate renewable energy purchases, actual grid supply remains carbon-intensive

## Theoretical Framework
The study operationalizes the **GHG Protocol Scope 2 guidance** for electricity accounting, distinguishing between:

1. **Market-based accounting**: Credits renewable energy certificates (RECs) regardless of grid connection
2. **Location-based accounting**: Reflects actual grid emissions where consumption occurs

The authors argue location-based accounting provides more accurate environmental impact assessment, revealing that market-based claims can obscure actual carbon footprints.

### Carbon Attribution Philosophy
The framework recognizes that:
- Electricity is fungible within balancing authority regions
- Time-matching matters (24/7 carbon-free energy vs. annual matching)
- Physical electron delivery differs from contractual renewable energy claims

## Evidence Quality Assessment
**Strengths:**
- First study specifically targeting hyperscale facilities (distinct from general data centers)
- Granular geographic and temporal resolution
- Novel balancing authority attribution methodology
- Large sample size (403 facilities)
- Transparent methodological documentation

**Limitations:**
- Electricity consumption estimates have significant uncertainty (31% range)
- Facility identification may miss recently constructed or planned HDCs
- Cannot access actual metered consumption data (proprietary)
- PUE assumptions may not reflect actual facility efficiency

## Connections to Other Research
- Extends Guidi et al. (2024) analysis of all US data centers to hyperscale subset
- Challenges IEA (2024) estimates suggesting data center growth is decoupling from emissions
- Complements Masanet et al. (2020) efficiency analysis with emissions focus
- Provides empirical ground truth for Patterson et al.'s theoretical carbon accounting frameworks

## My Analysis & Critique

### Strengths of the Study
1. **Methodological rigor**: The balancing authority approach represents a significant advancement over national average attribution
2. **Policy relevance**: Geographic granularity enables state-level policy interventions
3. **Transparency gap exposure**: Reveals disconnect between corporate sustainability claims and actual emissions
4. **Timeliness**: Addresses urgent questions about AI infrastructure expansion

### Potential Weaknesses
1. **Proprietary data access**: Without actual metered data, estimates remain uncertain
2. **Dynamic landscape**: HDC capacity is expanding rapidly; study may be outdated quickly
3. **Limited Scope 3 analysis**: Does not address embodied carbon in hardware/construction
4. **Renewable energy complexity**: May oversimplify corporate PPA arrangements

### Critical Implications
- **Corporate greenwashing risk**: Companies claiming "100% renewable" may still draw carbon-intensive grid power
- **Grid planning urgency**: Concentrating HDCs in fossil-heavy regions compounds environmental impact
- **Policy intervention points**: State-level renewable portfolio standards could drive HDC siting decisions

## Key Quotes
> "The carbon intensity of electricity consumed by US hyperscale data centers is 48% higher than the national average, challenging narratives about tech industry leadership on climate."

> "Virginia's dominance in hyperscale hosting creates a concentrated carbon liability that corporate renewable energy purchases do little to address at the grid level."

> "Location-based emissions accounting reveals the true environmental burden of digital infrastructure that market-based accounting obscures."

## Vocabulary & Concepts
- **Hyperscale data center (HDC)**: Facilities with >5,000 servers or >10,000 square feet, operated by cloud providers (AWS, Azure, GCP) or large tech companies
- **Balancing authority**: Grid operator responsible for maintaining electricity supply-demand balance in a region
- **Carbon intensity**: Grams of CO2 emitted per kilowatt-hour of electricity generated
- **Marginal emissions rate**: Carbon intensity of the last generating unit dispatched to meet demand
- **Market-based vs. location-based accounting**: GHG Protocol distinction between contractual and physical emissions attribution

## Study Questions for Exam Prep
1. Why does the carbon intensity of hyperscale data centers exceed the US national average, and what geographic factors contribute to this?
2. Explain the difference between market-based and location-based emissions accounting. Why does this distinction matter for assessing corporate climate claims?
3. Discuss the implications of Virginia's dominance in hyperscale data center hosting for regional grid decarbonization.
4. How might 24/7 carbon-free energy procurement differ from annual renewable energy matching in environmental impact?
5. What policy interventions could reduce the carbon intensity of hyperscale data center electricity consumption?

## Citation
Guidi, G., Dominici, F., Squartini, T., Sprinkle, C., Gilmour, J., Butler, K., Bell, E., Delaney, S., & Bargagli-Stoffi, F. J. (2026). Assessing Carbon Emissions of US Hyperscale Data Centers. *arXiv preprint arXiv:2606.05420v1*.
