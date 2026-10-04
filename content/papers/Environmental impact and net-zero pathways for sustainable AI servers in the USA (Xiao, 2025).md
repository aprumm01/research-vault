---
title: "Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the USA"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Xia25.pdf"
type: paper
authors:
  - Tianqi Xiao
  - Francesco Fuso Nerini
  - H. Damon Matthews
  - Massimo Tavoni
  - Fengqi You
year: 2025
venue: "Nature Sustainability"
doi: "10.1038/s41893-025-01681-y"
builds_on:
  - "[[Data center sustainability]]"
  - "[[AI environmental impact]]"
  - "[[Energy-water-climate nexus]]"
  - "[[Grid decarbonization]]"
supports:
  - "[[Sustainable AI]]"
  - "[[Net-zero computing]]"
  - "[[Regional energy planning]]"
critiques:
  - "[[AI industry net-zero claims]]"
  - "[[Carbon offset mechanisms]]"
tensions_with:
  - "[[AI expansion projections]]"
  - "[[Data center growth assumptions]]"
key_claims:
  - AI server deployment in the US could generate annual water footprint of 731-1125 million cubic meters by 2030
  - Additional annual carbon emissions of 24-44 Mt CO2-equivalent between 2024-2030
  - Best practices may reduce emissions and water footprints by up to 73% and 86% respectively
  - AI industry unlikely to meet net-zero aspirations by 2030 without substantial reliance on uncertain carbon offsets
  - Midwestern states (Texas, Montana, Nebraska, South Dakota) offer optimal combination of renewable energy and low water scarcity
methodology: "Bottleneck-based modeling approach with comprehensive uncertainty analysis; scenario-based projections using ReEDS model for grid factors; state-level allocation based on PUE, WUE, and grid carbon intensity"
study_type: "Quantitative modeling and scenario analysis"
context: "US AI data center expansion 2024-2030"
---

## Summary

This study provides the first comprehensive analysis of the combined energy-water-climate impacts of AI server deployment in the United States from 2024 to 2030. Using an open-source, bottleneck-based modeling approach, the researchers quantify the environmental footprint of AI servers across five deployment scenarios (low demand, low power, mid-case, high application, high demand) and assess pathways to achieve net-zero carbon and water goals.

The analysis reveals that AI server energy consumption could range from 147 to 245 TWh annually by 2030, with corresponding water footprints of 731-1125 million cubic meters and carbon emissions of 24-44 Mt CO2-equivalent. The study emphasizes the deep uncertainties in these projections driven by industry efficiency initiatives, grid decarbonization rates, and spatial distribution of server locations.

## Key Concepts

**Power Usage Effectiveness (PUE)**: Ratio of total facility energy to IT equipment energy; best-practice scenarios achieve over 7% reduction from current averages

**Water Usage Effectiveness (WUE)**: Measure of water consumed per unit of electricity; WUE reduction efforts can yield over 85% water footprint reduction

**CoWoS (Chip-on-Wafer-on-Substrate)**: Critical manufacturing bottleneck for AI server production controlled by Taiwan Semiconductor Manufacturing Company

**Advanced Liquid Cooling (ALC)**: Technology that can reduce energy consumption by 1.7%, water footprint by 2.4%, and carbon emissions by 1.6%

**Server Utilization Optimization (SUO)**: Best-case adoption can result in 5.5% reduction across all footprint metrics

**Scope 1, 2, and 3 Emissions**: Direct operations (Scope 1), indirect energy purchases (Scope 2), and supply chain activities (Scope 3)

## Key Findings

### Environmental Impact Projections
- **Energy consumption**: Mid-case scenario projects 174 TWh annual consumption by 2030
- **Water footprint**: 860 million cubic meters annually under mid-case scenario
- **Carbon emissions**: 26.8 Mt CO2-equivalent annually under mid-case scenario
- Server energy represents 89% of total energy consumption; infrastructure accounts for 11%
- Direct water usage accounts for 29% of total water footprint; indirect (electricity generation) accounts for 71%

### Spatial Distribution Analysis
- Southern states (Florida) exhibit higher PUE and WUE than northern states (Washington)
- Texas plays vital role with top 25% locations having 50% and 75% combined water and carbon factors
- West Coast states (California, Oregon, Washington) suitable for carbon reduction but lead to higher water footprints due to hydropower
- **Optimal locations**: Texas, Montana, Nebraska, and South Dakota emerge as best candidates considering both water scarcity and decarbonization

### Industry Efficiency Assessment
- Best-practice PUE improvements: 7.4% reduction in total energy and carbon emissions
- Best-practice WUE improvements: 29% reduction in total water footprint, 9.3% reduction in direct water
- Combined best practices could reduce residual emissions and water footprints by 73% and 86% respectively
- Worst-case scenarios (frozen adoption) lead to 7.3% increase in impacts by 2030

### Net-Zero Pathway Analysis
- Best-case scenario requires 28 GW of wind or 43 GW of solar to fully offset carbon emissions by 2030
- With 13 GW of AI company renewables already claimed, residual emissions could remain manageable
- Achieving best-case scenario extremely challenging due to facility constraints and optimal location difficulties
- Worst practices pose risk of unachievable net-zero pathways with 71 Mt annual residual carbon emissions

### Grid Decarbonization Impact
- Low renewable energy cost (LRC) scenario: 13% reduction in carbon, 2.0% increase in water footprint
- High renewable energy cost (HRC) scenario: 15% reduction in carbon, 2.5% reduction in water footprint
- States like Georgia, Nevada, North Carolina, and Tennessee show marked sensitivity to renewable cost scenarios
- Pacific states (California, Oregon, Washington) achieve low grid carbon factor but risk exacerbating water scarcity

## Relevance to Sustainable Computing

This paper is highly relevant to sustainable computing research as it:

1. **Quantifies the compound environmental costs** of AI infrastructure beyond just energy/carbon, incorporating water as a critical and often overlooked resource

2. **Demonstrates the energy-water-climate nexus** showing how optimization for one metric (e.g., carbon via hydropower) can worsen another (water consumption)

3. **Provides actionable spatial guidance** for sustainable AI server deployment, identifying Midwestern states as optimal locations

4. **Challenges net-zero claims** showing that industry aspirations require unprecedented investment in renewables and efficiency improvements

5. **Establishes methodology** for comprehensive environmental assessment of computing infrastructure using open-source, reproducible approaches

6. **Highlights policy implications** including the need for public-private partnerships, tax incentives for green infrastructure, and transparent accountability mechanisms

## Citation

Xiao, T., Fuso Nerini, F., Matthews, H. D., Tavoni, M., & You, F. (2025). Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the USA. *Nature Sustainability*, *8*, 1541-1553. https://doi.org/10.1038/s41893-025-01681-y
