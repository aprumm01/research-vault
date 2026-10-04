---
title: "The environmental footprint of data centers in the United States"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/The environmental footprint of data centers in the United States.pdf"
type: paper
authors:
  - Md Abu Bakar Siddik
  - Arman Shehabi
  - Landon Marston
year: 2021
venue: Environmental Research Letters
doi: "10.1088/1748-9326/abfba1"
builds_on:
  - "[[Data center growth in the United States - decoupling the demand for services from electricity use]]"
  - "[[Recalibrating global data center energy-use estimates]]"
supports:
  - "[[Water-Energy Nexus]]"
  - "[[Sustainable Computing]]"
critiques: []
tensions_with: []
key_claims:
  - Data centers account for approximately 1.8% of US electricity consumption
  - Data centers are responsible for approximately 0.5% of total US GHG emissions
  - One-fifth of data center servers draw water from moderately to highly water-stressed watersheds
  - Nearly half of servers are powered by power plants located in water-stressed regions
  - Strategic data center placement could reduce water and carbon footprints by up to 90%
methodology: Spatially-detailed bottom-up analysis linking data centers to specific power plants, water utilities, and wastewater treatment plants
study_type: Quantitative empirical analysis
context: United States data center industry in 2018
---

# The environmental footprint of data centers in the United States

## Summary

This study provides the first spatially-detailed assessment of water and carbon footprints of data centers operating in the United States. The authors develop a bottom-up methodology that connects individual data centers to their specific power plants, water utilities, and wastewater treatment plants. The research quantifies both direct impacts (on-site water consumption for cooling) and indirect impacts (water and carbon embedded in electricity generation). Key findings reveal that data centers account for 1.8% of US electricity use and 0.5% of total US greenhouse gas emissions, with significant geographic variation in environmental footprints depending on location. The study demonstrates that strategic placement of future data centers could substantially reduce the industry's environmental impact.

## Key Concepts

- **Water Footprint (WF)**: Consumptive blue water use (surface water and groundwater) associated with data center operations, including direct cooling and indirect electricity generation
- **Water Scarcity Footprint (WSF)**: Water consumption weighted by local water scarcity using the AWARE methodology (ISO 14046)
- **Carbon Footprint (CF)**: GHG emissions expressed as equivalent CO2, attributed to data centers based on their electricity consumption and the local generation mix
- **Power Usage Effectiveness (PUE)**: Ratio of total data center energy to IT equipment energy; lower values indicate better efficiency (ideal = 1.0)
- **Virtual Water**: Water consumed indirectly through electricity generation at power plants
- **Virtual Carbon**: GHG emissions from electricity generation and wastewater treatment attributed to data centers

## Key Findings

### Water Footprint
- Total annual operational water footprint of US data centers in 2018: **5.13 x 10^8 m³**
- Approximately three-fourths of the water footprint comes from indirect sources (electricity generation)
- Direct water consumption: 1.30 x 10^8 m³
- 1 MWh of data center energy requires approximately 7.1 m³ of water nationally

### Water Scarcity
- Water scarcity footprint: **1.29 x 10^9 m³** US-equivalent (more than twice volumetric footprint)
- 70% of overall WSF occurs in Western and Southwestern US (which host only 20% of servers)
- Direct water consumption is disproportionately skewed toward water-stressed subbasins

### Carbon Footprint
- Total GHG emissions attributed to data centers in 2018: **3.15 x 10^7 tons CO2-eq**
- This represents approximately **0.5%** of total US GHG emissions
- Over half (52%) of emissions are from the Northeast, Southeast, and Central US
- Central US accounts for 30% of emissions due to reliance on coal and natural gas

### Geographic Variation
- Water intensity ranges from 1.8 to 106 m³/MWh depending on location
- Water scarcity intensity ranges from 0.5 to 305 m³ US-eq/MWh
- Carbon intensity ranges from 0.02 to 1 ton CO2-eq/MWh

### Data Center Types (per MWh of electricity)
| Type | Water Intensity | Carbon Intensity |
|------|-----------------|------------------|
| Internal | 12.15 m³ | 0.75 ton CO2-eq |
| Colocation | 3.85 m³ | 0.25 ton CO2-eq |
| Hyperscale | 2.10 m³ | 0.15 ton CO2-eq |

### Strategic Placement Potential
- Placing new data centers in optimal locations could reduce:
  - WSF by 153 x 10^6 m³ US-eq (90% less than business-as-usual)
  - Carbon footprint by 2.34 x 10^6 tons CO2-eq (55% reduction)
- Less than 5% of US subbasins are optimal for both low water scarcity and low carbon footprint
- 40% of subbasins require trade-offs between water and carbon optimization

## Relevance to Sustainable Computing

This paper is foundational for understanding the environmental externalities of digital infrastructure. Key implications for sustainable computing include:

1. **Location Matters**: The environmental footprint of computing is highly dependent on where data centers are located, not just their operational efficiency
2. **Water-Energy Nexus**: Data centers create complex interdependencies between water and energy systems that must be considered holistically
3. **Hidden Impacts**: Most of a data center's water footprint is indirect (via electricity generation), highlighting the importance of renewable energy sourcing
4. **Trade-offs**: Optimizing for one environmental metric (e.g., carbon) may not optimize another (e.g., water scarcity)
5. **Policy Implications**: Environmental considerations should factor into data center siting decisions alongside traditional factors like tax incentives and connectivity

The findings support arguments for:
- Renewable energy procurement by data center operators
- Geographic distribution strategies that account for environmental factors
- Transparency in reporting data center environmental impacts
- Integration of water scarcity into sustainability assessments (not just carbon)

## Citation

Siddik, M. A. B., Shehabi, A., & Marston, L. (2021). The environmental footprint of data centers in the United States. *Environmental Research Letters*, *16*(6), 064017. https://doi.org/10.1088/1748-9326/abfba1
