---
source_file: 2026/i609-sustainability/The environmental footprint of data centers
  in the United States.pdf
type: paper
authors: Md Abu Bakar Siddik, Arman Shehabi, Landon Marston
community: Sustainable Computing
tags:
- sustainability
- i609
- data-centers
- carbon-footprint
- water-footprint
- environmental-impact
- electricity
year: 2021
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with: []
supports: []
key_claims:
- Data centers consumed 73 TWh of electricity in 2016, representing 1.8% of total
  US electricity consumption and contributing 0.5% of US greenhouse gas emissions
  (34.7 Mt CO2e)
- Strategic placement of data centers could reduce their combined environmental footprint
  by 89-91% through optimization of location relative to regional electricity sources
  and water stress levels
- 23% of data center water footprint occurs in moderately-to-highly water-stressed
  regions, with indirect water consumption from electricity generation often exceeding
  direct water use for cooling
- Regional variations in electricity mix create dramatically different impact profiles
  for identical facilities, with coal-heavy grids producing ~900 g CO2/kWh versus
  <100 g CO2/kWh in hydro-dominated regions
- Data center workloads increased 550% from 2010-2018 while energy use grew only 6%
  due to efficiency improvements (PUE reduction from ~2.0 to ~1.6), but future growth
  may outpace efficiency gains
methodology: '[[methods/Mixed Methods]]'
sample_size: 2657
sample_type: data centers across 3,082 US counties
context: United States data center infrastructure analysis using 2016 data
study_type: empirical
---

# The Environmental Footprint of Data Centers in the United States

## Summary

This study provides the first spatially-detailed analysis of the water and carbon footprint of US data centers, examining 2016 data across 3,000+ counties. The research finds that data centers consumed approximately 1.8% of US electricity (73 TWh), contributing to 0.5% of US greenhouse gas emissions. Critically, the study reveals that strategic placement of data centers could reduce their combined environmental footprint by up to 90%, as regional variations in electricity sources and water stress create dramatically different impact profiles for identical facilities.

## Research Overview

**Research Questions:**
1. What is the spatially-explicit water and carbon footprint of US data centers?
2. How do regional factors (electricity mix, water stress, climate) affect environmental impact?
3. What reduction potential exists through strategic data center placement?

**Method:** 
- Combined multiple data sources: Hypelocations data center database, EIA electricity data, AWARE water stress characterization, EPA eGRID emissions factors
- Analyzed 2,657 data centers across 3,082 counties
- Calculated direct and indirect (electricity-driven) water consumption
- Computed operational GHG emissions based on regional electricity mix
- Developed spatial optimization model for footprint reduction

**Key Findings:**
- Data centers consumed 73 TWh electricity (1.8% of US total) in 2016
- Water footprint: 5.13 x 10^8 m^3 (comparable to 10 million American households)
- Carbon footprint: 34.7 Mt CO2e (0.5% of US emissions)
- 23% of data center water footprint is in moderately-to-highly water-stressed regions
- Optimal placement could reduce combined footprint by 89-91%

## Theoretical Framework

The study employs **life cycle assessment (LCA) methodology** adapted for spatial analysis:

1. **Scope Definition**: Focuses on operational phase (excludes embodied energy in construction)
   - Direct water: Cooling systems
   - Indirect water: Water consumed in electricity generation
   - GHG emissions: From electricity consumption based on regional fuel mix

2. **Water Stress Integration**: Uses AWARE (Available WAter REmaining) framework
   - Accounts for regional water scarcity
   - Weights water consumption by local stress levels
   - Enables comparison across regions with different water availability

3. **Electricity Fuel Mix Analysis**: 
   - Different generation sources have vastly different water and carbon intensities
   - Regional grids vary from coal-heavy to renewable-dominated
   - Power purchase agreements can modify effective fuel mix

4. **Spatial Optimization Framework**:
   - Multi-objective optimization considering water, carbon, and water stress
   - Trade-off analysis between different environmental objectives

## Central Arguments

### 1. Data Center Impacts Are Significant and Growing

- 1.8% of US electricity is substantial - equivalent to multiple states' total consumption
- Growth trajectory: Data center workloads increased 550% from 2010-2018 while energy use grew only 6% due to efficiency gains
- Future growth may outpace efficiency improvements, particularly with AI/ML workloads

### 2. Location Matters Enormously

The same data center can have vastly different environmental impacts based on location:
- **Virginia (data center hub)**: Coal-heavy grid, high carbon intensity
- **California**: Lower carbon but high water stress
- **Pacific Northwest**: Hydroelectric-dominant, low carbon, abundant water
- Moving workloads to optimal locations could reduce footprint by up to 90%

### 3. Water Stress Amplifies Impact

Raw water consumption is misleading without stress context:
- 23% of data center water footprint occurs in moderately-to-highly stressed basins
- Indirect water (electricity generation) often exceeds direct water (cooling)
- Water-stressed regions may face competing demands from agriculture and municipalities

### 4. Trade-offs Exist Between Objectives

Optimizing for one environmental metric may worsen others:
- Low-carbon regions aren't always low-water
- Cold climates reduce cooling needs but may have carbon-intensive heating
- Single-objective optimization misses synergies and conflicts

### 5. Policy Implications Are Substantial

- Renewable energy procurement significantly affects footprint
- Building codes and efficiency standards matter
- Water pricing rarely reflects true scarcity
- Carbon pricing would incentivize cleaner locations

## Evidence

**National-Level Statistics (2016):**
- Total data center electricity: 73 TWh
- Share of US electricity: 1.8%
- Water footprint: 5.13 x 10^8 m^3
- GHG emissions: 34.7 Mt CO2e
- Share of US emissions: 0.5%

**Regional Variations:**

*Top States by Data Center Concentration:*
1. Virginia (Northern Virginia corridor)
2. Texas
3. California
4. Illinois
5. New Jersey

*Carbon Intensity Variations:*
- Coal-heavy regions (e.g., West Virginia): ~900 g CO2/kWh
- National average: ~450 g CO2/kWh
- Hydro-dominated (e.g., Pacific Northwest): <100 g CO2/kWh

*Water Intensity Variations:*
- Thermoelectric-heavy regions: High indirect water consumption
- Wind/solar regions: Near-zero indirect water
- Direct cooling water: Highly variable by technology (air vs. evaporative)

**Optimization Potential:**
- 89% reduction possible optimizing for water + carbon
- 91% reduction with 3-objective optimization (water, carbon, water stress)
- Even modest redistribution yields significant improvements

**Efficiency Trends:**
- PUE (Power Usage Effectiveness) improved from ~2.0 to ~1.6 industry-wide
- Hyperscale facilities achieve PUE of 1.1-1.2
- Efficiency gains partially offset demand growth

## Conclusion

Data centers have a significant and growing environmental footprint, but their impact is highly dependent on location decisions. The 90% reduction potential through strategic placement represents an enormous opportunity for the industry and policymakers.

Key recommendations:
1. **For industry**: Consider environmental metrics alongside cost in siting decisions
2. **For policymakers**: Develop incentives for sustainable data center placement
3. **For researchers**: Continue developing spatially-explicit assessments as the industry evolves
4. **For users**: Recognize that "the cloud" has physical infrastructure with real environmental costs

The authors note that AI/ML workloads and cryptocurrency mining may significantly increase future data center demand, making sustainable siting increasingly urgent.

## APA Citation

Siddik, M. A. B., Shehabi, A., & Marston, L. (2021). The environmental footprint of data centers in the United States. *Environmental Research Letters, 16*(6), 064017. https://doi.org/10.1088/1748-9326/abfba1

## Discussion Questions

1. How should the industry balance economic factors (land cost, network latency, tax incentives) against environmental considerations in siting decisions?

2. The study shows 90% reduction potential through optimal placement. What policy mechanisms could drive this transition?

3. How do hyperscale data centers (Google, Microsoft, Amazon) compare to smaller facilities in environmental efficiency?

4. The study focuses on operational emissions. How significant is embodied carbon in data center construction, and how does facility lifespan affect total footprint?

5. As AI/ML workloads grow, how might the environmental footprint trajectory change, and what interventions are most promising?

## Connections

- **Digital hoarding and personal data**: Individual data accumulation contributes to aggregate data center demand - the 73 TWh includes storing users' digital hoards
- **Dark data**: The 80-90% of enterprise data that is never analyzed still requires storage infrastructure and energy
- **User understanding of deletion**: "Deleted" data that persists in backends continues consuming data center resources
- **Sustainability and HCI**: Motivates research on designing systems that reduce data storage demand
- **Cloud computing policy**: Informs debates about data localization, data sovereignty, and environmental regulation of tech infrastructure
