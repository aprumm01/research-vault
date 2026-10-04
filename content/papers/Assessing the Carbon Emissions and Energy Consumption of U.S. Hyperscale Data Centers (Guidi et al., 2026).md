---
title: "Assessing the Carbon Emissions and Energy Consumption of U.S. Hyperscale Data Centers"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Gui26.pdf"
type: paper
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
venue: "arXiv preprint (arXiv:2606.05420)"
builds_on:
  - "[[Siddik et al. 2018]]"
  - "[[Shehabi et al.]]"
  - "[[IEA Energy and AI Report]]"
supports:
  - "[[Data Center Sustainability]]"
  - "[[Carbon Footprint Assessment]]"
  - "[[Grid Carbon Intensity Analysis]]"
critiques:
  - "[[Corporate Renewable Energy Claims]]"
tensions_with:
  - "[[Location-Based vs Market-Based Accounting]]"
key_claims:
  - US hyperscale data centers consumed 68-99 TWh of electricity (May 2024-April 2025)
  - HDCs were associated with 37-54 million metric tons of CO2 emissions
  - HDC electricity-weighted carbon intensity was 545 gCO2/kWh (48% above US national average of 370 gCO2/kWh)
  - 54% of HDC electricity came from fossil fuels, 21% nuclear, 25% renewables
  - 90% of HDC electricity demand is in balancing authorities with above-average carbon intensity
  - Virginia alone accounts for ~25% of total HDC electricity consumption
methodology: "Attributional analysis using EPA eGRID2023 plant-level generation and emissions data; facility-level power capacity estimates validated through satellite imagery; bottom-up power-flow modeling"
study_type: "Quantitative empirical analysis"
context: "Environmental assessment of hyperscale data center industry driven by AI proliferation"
tags:
  - data-centers
  - carbon-footprint
  - energy-consumption
  - environmental-impact
  - green-computing
  - hyperscale
  - AI-infrastructure
---

# Assessing the Carbon Emissions and Energy Consumption of U.S. Hyperscale Data Centers

## Summary

This paper presents a comprehensive facility-level analysis of 403 U.S. hyperscale data centers (HDCs) operating between May 2024 and April 2025. The authors developed a data pipeline that integrates heterogeneous data sources and validates facility information through satellite imagery. Using EPA eGRID2023 plant-level data, they estimate electricity consumption, identify supplying power plants, characterize fuel mixes, and calculate attributable CO2 emissions at the state and balancing authority levels.

The central finding is that HDCs consumed approximately 82 TWh of electricity (range: 68-99 TWh depending on facility-load assumptions), corresponding to roughly 1.8% of total U.S. electricity consumption. These facilities were associated with approximately 45 million metric tons of CO2 emissions (range: 37-54 Mt). Critically, the HDC electricity-weighted average carbon intensity was 545 gCO2/kWh—about 48% higher than the U.S. national grid average of 370 gCO2/kWh—indicating that hyperscale facilities are disproportionately concentrated in regions with carbon-intensive electricity supplies.

## Key Concepts

- **Hyperscale Data Centers (HDCs)**: The largest and most powerful class of data centers, typically operated by cloud/content providers, with electrical capacity in the tens of megawatts and modular architecture verified through imagery analysis

- **Carbon Intensity**: Amount of CO2 produced per unit of electricity consumed, expressed as gCO2/kWh; used to compare environmental impact across regions

- **Attributional Method**: A generation-weighted average emission model that assigns each data center the power plants that supplied its electricity based on proportional contribution within balancing authorities

- **Balancing Authority**: Entity responsible for maintaining grid reliability by matching generation and demand within a defined territory; determines the power plant mix supplying each HDC

- **Power Use Effectiveness (PUE)**: Ratio of total facility energy to IT equipment energy; used to estimate operational electricity demand from nameplate capacity

## Key Findings

### Electricity Consumption
- 403 HDCs identified across the contiguous U.S.
- Total consumption: 68-99 TWh (central estimate: 82 TWh)
- Represents approximately 1.5-2.2% of total U.S. electricity consumption
- Consumption is 3.5-4x higher than the 22.85 TWh reported for HDCs in 2018

### Geographic Distribution
- Virginia hosts the most HDCs (142), accounting for ~25% of total HDC electricity (~21 TWh)
- Oregon (56 HDCs, ~11 TWh), Ohio (38 HDCs, ~9 TWh), and Iowa (26 HDCs, ~7 TWh) follow
- These four states account for >50% of total HDC electricity consumption

### Carbon Emissions
- Total attributable CO2: 37-54 million metric tons (central: 45 Mt)
- This is 3.5-5x the 10.5 Mt reported for HDCs in 2018
- Virginia: 11.5 Mt; Oregon: 4.9 Mt; Ohio: 4.7 Mt; Iowa: 4.6 Mt

### Carbon Intensity Analysis
- HDC electricity-weighted average: 545 gCO2/kWh
- U.S. national average: 370 gCO2/kWh
- 90% of HDC electricity demand is in balancing authorities with above-average carbon intensity
- PJM (Virginia's dominant balancing authority): 535 gCO2/kWh with 60% fossil fuel generation

### Fuel Mix Attribution
- **Fossil fuels**: 53.9% (natural gas 38.2%, coal 15.2%)
- **Nuclear**: 20.9%
- **Renewables**: 25.3% (hydro, wind, solar, biomass, geothermal combined)

## Relevance to Sustainable Computing

This study provides critical empirical evidence for understanding the environmental footprint of hyperscale computing infrastructure, with several implications for sustainable computing research and practice:

1. **Quantifying the AI Boom's Impact**: The paper documents a 3.5-5x increase in HDC emissions since 2018, directly attributable to cloud computing and AI workload growth, providing baseline data for tracking the industry's trajectory.

2. **Location Matters More Than Claimed**: Despite many HDC operators being major purchasers of renewable energy, the attributional analysis shows that 54% of electricity actually comes from fossil sources, highlighting the gap between market-based claims and physical grid reality.

3. **Policy Implications**: The concentration of HDCs in high-carbon-intensity regions (particularly Virginia/PJM) suggests that siting decisions prioritize factors other than grid carbon intensity, indicating opportunity for policy intervention.

4. **Transparency Gap**: The study highlights the absence of comprehensive, publicly available datasets on data center infrastructure—a barrier to research and accountability that the authors address through their open web platform.

5. **Scalability of Assessment Methods**: The automated, reproducible pipeline demonstrates how facility-level environmental assessment can scale, providing a model for ongoing monitoring of the data center industry.

6. **Future Research Needs**: The paper identifies the need for consequential (marginal) emissions analysis to inform decisions about where to locate new data centers to minimize total grid emissions.

## Citation

Guidi, G., Dominici, F., Squartini, T., Sprinkle, C., Gilmour, J., Butler, K., Bell, E., Delaney, S., & Bargagli-Stoffi, F. J. (2026). Assessing the carbon emissions and energy consumption of U.S. hyperscale data centers. *arXiv preprint arXiv:2606.05420*. https://arxiv.org/abs/2606.05420
