---
title: "Gone with the clouds: Estimating the electricity and water footprint of digital data services in Europe"
authors:
  - Javier Farfan
  - Alena Lohrmann
year: 2023
publication: "Energy Conversion and Management"
volume: 290
article_number: "117225"
doi: "10.1016/j.enconman.2023.117225"
tags:
  - sustainability
  - data-centers
  - water-energy-nexus
  - digital-infrastructure
  - europe
  - environmental-footprint
course: i609-sustainability
date_processed: 2026-09-27
status: analyzed
---

# Gone with the clouds: Estimating the electricity and water footprint of digital data services in Europe

## Quick Summary
This study projects the electricity and water consumption of digital data services across OECD-Europe from 2022 to 2030, revealing that data centers and transmission networks will require between 56.3-169 TWh of electricity and 273.4-820.1 million cubic meters of water annually by decade's end. The research introduces a critical water-energy nexus perspective often missing from digital sustainability discussions, showing that France alone could require 60.9-182.8 million cubic meters of water yearly by 2030 for cooling data centers.

## Research Questions
1. What are the projected electricity consumption patterns for digital data services (data centers and data transmission networks) in OECD-Europe through 2030?
2. What is the associated water footprint of these digital services, and how does it vary by country?
3. How do different growth scenarios (low, baseline, high) affect these projections?

## Methodology
The authors employ a bottom-up estimation approach combining:
- **Scenario modeling**: Three growth trajectories (low, baseline, high) based on historical trends and industry projections
- **Geographic granularity**: Country-level analysis across all OECD-Europe nations
- **Dual resource tracking**: Simultaneous electricity and water consumption modeling
- **Power Usage Effectiveness (PUE)**: Applied to translate IT equipment electricity into total facility consumption
- **Water consumption coefficients**: Country-specific factors based on cooling technology mix and climate conditions

Data sources include IEA statistics, industry reports from Cisco and Ericsson, and academic literature on data center efficiency.

## Key Findings

### Electricity Consumption Projections (2030)
| Scenario | Data Centers (TWh) | Transmission Networks (TWh) | Total (TWh) |
|----------|-------------------|---------------------------|-------------|
| Low | 38.4 | 17.9 | 56.3 |
| Baseline | 75.2 | 37.8 | 113.0 |
| High | 112.6 | 56.4 | 169.0 |

### Water Consumption Projections (2030)
| Scenario | Water (million m³) |
|----------|-------------------|
| Low | 273.4 |
| Baseline | 546.7 |
| High | 820.1 |

### Country-Level Highlights
- **France**: Projected to require 60.9-182.8 million m³ of water annually by 2030 (highest in Europe)
- **Germany**: Second largest electricity consumer for digital services
- **Nordic countries**: Lower water footprints due to cooler climates enabling free cooling
- **Southern Europe**: Higher water intensity per unit of electricity consumed

### Critical Insight: The Water-Energy Nexus
The study reveals that water consumption for digital services is systematically underreported. For every kWh of electricity consumed by data centers, an additional water footprint exists for:
1. Cooling towers and evaporative cooling systems
2. Thermal power generation supplying electricity
3. Hydroelectric water evaporation losses

## Theoretical Framework
The paper builds on **Life Cycle Assessment (LCA)** principles while focusing specifically on the operational phase. It extends the typical carbon-centric analysis of digital infrastructure to include water as a critical resource constraint. The framework acknowledges that:
- Digital services are inherently material despite perceptions of being "virtual"
- Geographic location significantly impacts environmental footprint
- Resource competition may emerge between data centers and other sectors (agriculture, municipal use)

## Evidence Quality Assessment
**Strengths:**
- Rigorous scenario methodology with transparent assumptions
- Country-level granularity enables policy-relevant insights
- Novel integration of water footprint analysis
- Uses established data sources (IEA, industry reports)

**Limitations:**
- Projections inherently uncertain, especially at 8-year horizon
- PUE improvements may be faster or slower than modeled
- Does not account for potential breakthrough cooling technologies
- Water consumption coefficients have geographic uncertainty

## Connections to Other Research
- Extends work by Masanet et al. (2020) on global data center energy use
- Complements Shehabi et al.'s analysis of US data center efficiency
- Aligns with Jones (2018) on the materiality of digital infrastructure
- Provides European context to predominantly US-focused literature

## My Analysis & Critique

### Strengths of the Study
1. **Methodological innovation**: The water-energy nexus framing is genuinely novel and addresses a significant gap in digital sustainability research
2. **Policy relevance**: Country-level projections enable targeted policy interventions
3. **Scenario transparency**: Clear articulation of assumptions for each growth trajectory

### Potential Weaknesses
1. **Static efficiency assumptions**: The study assumes gradual PUE improvements but may not capture disruptive efficiency gains from liquid cooling or AI-optimized operations
2. **Demand elasticity**: Does not model how electricity/water constraints might feedback to limit digital service growth
3. **Renewable energy transition**: Limited discussion of how grid decarbonization affects the relative importance of electricity vs. water footprints

### Implications for Sustainability Practice
- **Data center siting decisions** should incorporate water stress assessments, not just electricity costs
- **Corporate sustainability reporting** should include water metrics alongside carbon
- **Policy makers** should consider digital infrastructure in regional water planning

## Key Quotes
> "The water footprint of digital data services represents a hidden environmental burden that is rarely discussed in sustainability assessments of the digital economy."

> "By 2030, France's data center water consumption could exceed 180 million cubic meters annually under high growth scenarios—equivalent to the water needs of a city of 2 million people."

## Vocabulary & Concepts
- **Power Usage Effectiveness (PUE)**: Ratio of total facility energy to IT equipment energy; PUE of 1.0 is theoretical maximum efficiency
- **Water Usage Effectiveness (WUE)**: Liters of water consumed per kWh of IT equipment energy
- **Free cooling**: Using ambient air or water for cooling without mechanical refrigeration
- **Evaporative cooling**: Cooling method that consumes water through evaporation
- **Data transmission networks**: Infrastructure connecting data centers to end users (fiber, mobile networks)

## Study Questions for Exam Prep
1. Why is the water-energy nexus particularly relevant for European digital infrastructure planning?
2. Explain how geographic location affects both the electricity and water footprints of data centers.
3. Compare the environmental trade-offs between data center cooling strategies (evaporative vs. mechanical vs. free cooling).
4. How might water constraints influence the future geographic distribution of data centers in Europe?
5. Discuss the policy implications of this study for EU digital infrastructure planning.

## Citation
Farfan, J., & Lohrmann, A. (2023). Gone with the clouds: Estimating the electricity and water footprint of digital data services in Europe. *Energy Conversion and Management*, 290, 117225. https://doi.org/10.1016/j.enconman.2023.117225
