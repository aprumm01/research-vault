---
title: "Gone with the clouds: Estimating the electricity and water footprint of digital data services in Europe"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Gone with the clouds- Estimating the electricity and water footprint of digital data services in Europe.pdf"
type: paper
authors:
  - Javier Farfan
  - Alena Lohrmann
year: 2023
venue: "Energy Conversion and Management"
doi: "10.1016/j.enconman.2023.117225"
builds_on:
  - "[[Water-Energy Nexus]]"
  - "[[Data Center Energy Consumption]]"
  - "[[Life Cycle Assessment]]"
supports:
  - "[[Digital Sustainability]]"
  - "[[Environmental Impact of IT]]"
  - "[[Sustainable Computing]]"
critiques:
  - "[[Transparency in Data Center Reporting]]"
tensions_with:
  - "[[Digital Transformation Benefits]]"
key_claims:
  - European data usage will grow from 86 EB to 225 EB by 2030
  - Electricity consumption for data services will increase from 29.8 TWh (2020) to 112.7 TWh (2030)
  - Water consumption will rise from 145.2 million cubic meters (2020) to 546.7 million cubic meters (2030)
  - Per capita water consumption for data usage will reach 1.1 cubic meters per year by 2030
  - Lack of transparency from major cloud providers hinders accurate environmental assessment
methodology: "Quantitative projection model combining OECD subscription data, World Bank population projections, and energy intensity factors from literature to estimate electricity and water consumption across 26 European countries"
study_type: "Empirical projection study"
context: "OECD-Europe region (26 countries including EU27 minus Bulgaria, Croatia, Cyprus, Malta, Romania plus Iceland, Norway, Switzerland, UK)"
tags:
  - digital-sustainability
  - data-centers
  - energy-consumption
  - water-footprint
  - water-energy-nexus
  - environmental-impact
  - europe
  - cloud-computing
---

# Gone with the Clouds: Estimating the Electricity and Water Footprint of Digital Data Services in Europe

## Summary

This study provides the first comprehensive projection of both electricity and water consumption for digital data services across 26 OECD-Europe countries from 2022 to 2030. The authors develop a methodological framework that accounts for data center operations, data transmission networks, and the water-energy nexus. Using publicly available OECD data on broadband subscriptions, World Bank population projections, and energy intensity factors from literature (0.1-0.3 kWh/GB), they estimate current and future resource demands.

The research addresses a critical gap in sustainability assessment: while individual data center studies exist, no prior work had estimated the combined electricity and water footprint at a regional European level. The study highlights the "double water impact" of data centers—direct water use for cooling plus indirect water consumption embedded in electricity generation.

## Key Concepts

### Water-Energy Nexus in Data Centers
Data centers require water both directly (for cooling) and indirectly (through electricity production). The study calculates both components:
- **Direct water consumption**: Cooling at data center sites (2.94 m³/MWh average)
- **Indirect water consumption**: Water used in electricity generation, varying by country's energy mix (0.55-15.47 m³/MWh)

### Energy Intensity of Data
The study assumes 0.1-0.3 kWh per GB of data processed, based on literature values. This range accounts for efficiency improvements since 2012 (when values were 4.5-5.1 kWh) while acknowledging a floor of ~0.1 kWh/GB for minimum energy consumption.

### Data Transmission Network Ratio
Data transmission networks consume 30-36% more electricity than data centers alone. The study uses a transmission network ratio (DtT) of 1.33 to account for this additional load.

## Key Findings

### Electricity Consumption Projections
| Year | Total Energy (TWh) | Per Capita (kWh) |
|------|-------------------|------------------|
| 2020 | 29.8 | 54.9 |
| 2022 | ~56.3-169 | ~113-339 |
| 2030 | 104.5-313.6 | 226 (average) |

### Water Consumption Projections
| Year | Total Water (million m³) | Per Capita (m³) |
|------|-------------------------|-----------------|
| 2020 | 145.2 | 0.29 |
| 2022 | ~273.4 | ~0.55 |
| 2030 | 273.4-820.1 | 0.55-1.65 |

### Country-Specific Insights
- **France**: Highest projected water demand (60.9-182.8 million m³ by 2030) due to large population and high data usage
- **Austria**: Second highest water demand despite smaller population, due to hydropower-dominated energy mix
- **Italy**: High water stress region facing additional pressure from data center water demands
- **Denmark**: Unique case where most water use is direct (cooling) rather than indirect (energy-related)
- **Nordic countries**: Higher per capita data usage (Finland projected highest per subscription by 2030)

### Data Usage Growth
- Total OECD-Europe data usage: 86 EB (2022) → 225 EB (2030)
- Average European citizen used 187.3 GB/year in 2020 (286% increase from 5 years prior)
- Six countries exceed 20 million inhabitants and dominate total consumption: Germany, UK, France, Italy, Spain, Poland

## Relevance to Sustainable Computing

### Policy Implications
1. **Transparency legislation needed**: Major providers (Google, Meta, Microsoft, Amazon) lack detailed public reporting on water and electricity consumption
2. **Site selection**: Future data centers should consider water stress alongside energy availability
3. **Regional planning**: Governments need data to manage electricity grids and water resources where data centers operate

### Environmental Trade-offs
- Transitioning to renewables reduces water footprint (solar PV and wind have lowest water intensity)
- Hydropower, while renewable, has highest water footprint among renewables
- Coal and nuclear have high water requirements for thermal cooling

### Comparison to Other Sectors
- 226 kWh per capita for data usage by 2030 is small compared to EU28 average of 6,400 kWh total electricity consumption per capita (2016)
- However, 1.1 m³ water per person for data represents ~3L per day—approaching the amount needed for drinking

### Limitations Acknowledged
- Model relies on energy intensity assumptions (0.1-0.3 kWh/GB) that may not capture all efficiency improvements
- Lack of provider transparency means estimates carry uncertainty
- Does not account for edge computing growth or AI workload increases

## Citation (APA)

Farfan, J., & Lohrmann, A. (2023). Gone with the clouds: Estimating the electricity and water footprint of digital data services in Europe. *Energy Conversion and Management*, 290, 117225. https://doi.org/10.1016/j.enconman.2023.117225
