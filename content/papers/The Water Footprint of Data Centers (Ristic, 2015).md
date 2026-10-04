---
title: "The Water Footprint of Data Centers"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Ris15.pdf"
type: paper
authors:
  - Bora Ristic
  - Kaveh Madani
  - Zen Makuch
year: 2015
venue: "Sustainability"
doi: "10.3390/su70811260"
builds_on:
  - "[[Water Use Effectiveness (WUE) - Green Grid]]"
  - "[[Koomey DC Energy Efficiency Studies]]"
  - "[[Water Footprint Assessment Methodology]]"
supports:
  - "[[Water-Energy Nexus in ICT]]"
  - "[[Sustainable Data Center Design]]"
  - "[[Environmental Impact Assessment of ICT]]"
critiques:
  - "[[Energy-Only DC Sustainability Metrics]]"
  - "[[Carbon-Centric ICT Environmental Assessment]]"
tensions_with:
  - "[[Renewable Energy as Complete Sustainability Solution]]"
  - "[[PUE as Sole DC Efficiency Metric]]"
key_claims:
  - Data center water footprint ranges from 1047 to 151,061 cubic meters per terajoule of energy
  - Outbound DC data traffic generates 1-205 liters of water per gigabyte (comparable to 1 kg of tomatoes at high end)
  - Energy consumption constitutes the largest share of DC water footprint (indirect WF)
  - Direct water use in HVAC cooling is relatively small compared to indirect WF from electricity generation
  - WF of different energy sources varies enormously, making DC location and energy mix critical factors
methodology: "Water footprint accounting combining direct (HVAC cooling) and indirect (energy source) water consumption; case study analysis of Apple data centers and Phoenix DC cooling technologies"
study_type: "Quantitative analysis / Environmental accounting"
context: "First systematic application of water footprint methodology to data centers, addressing gap in DC environmental assessment that previously focused only on energy and carbon"
---

## Summary

This paper presents the first comprehensive water footprint (WF) analysis of data centers (DCs), addressing a critical gap in understanding the environmental impacts of ICT infrastructure. While DC energy efficiency has received extensive attention, water consumption has been largely overlooked. The authors develop a methodology that accounts for both direct water use (primarily in HVAC cooling systems) and indirect water use (embedded in electricity generation).

The key innovation is applying the established Water Footprint methodology to DCs, integrating it with the Green Grid's Water Use Effectiveness (WUE) metric. The analysis reveals that indirect WF from energy sources typically dominates total DC water consumption, meaning that the choice of electricity source and geographic location may be more important for water sustainability than on-site cooling technology choices.

## Key Concepts

### Water Footprint Components
- **Blue WF**: Volume of freshwater (surface or groundwater) consumed
- **Green WF**: Volume of rainwater consumed (minimal for DCs)
- **Grey WF**: Volume of freshwater required to assimilate pollutants (from thermal pollution, cooling system discharges)

### Key Metrics
- **WUE (Water Use Effectiveness)**: Total Facility Water Use / IT Equipment Energy
- **WUE_source**: Includes water use of energy sources in addition to facility water use
- **DCWF (Data Center Water Footprint)**: Volume of Water / Outbound Bits

### DC Water Consumption Drivers
1. **HVAC Systems**: Evaporative cooling, condensers, humidification
2. **Energy Source Portfolio**: Indirect WF varies dramatically by generation technology
3. **Psychrometrics**: Local temperature and humidity conditions affect cooling requirements

## Key Findings

1. **WF Magnitude**: Global DC WF estimated at 767-147,082 million cubic meters annually (comparable to Italy's total water use at high end)

2. **Energy Source Dominance**: Wind has lowest WF (~0.1 m³/TJ), while hydropower and firewood have highest (up to 1,000,000 m³/TJ). Most technologies fall between 100-10,000 m³/TJ.

3. **Geographic Variation**: Arizona WF_source ranges from 70 m³/TJ (fossil fuel dominated) to 540,544 m³/TJ (high hydro scenarios). France's nuclear reliance gives different WF profile than US.

4. **HVAC Trade-offs**: In Phoenix case study:
   - Direct evaporation/air-cooled: 7,748 m³ cooling + 192 m³ energy WF
   - No evaporation/air-cooled: 0 m³ cooling but 9,499 m³ energy WF (highest total)
   - Water-cooled condensers use less energy but more direct water

5. **Apple DC Case Study**: Facilities using renewable energy (Maiden NC with biogas/solar, Prineville OR with wind) achieve dramatically lower WF_source than grid-dependent facilities (Newark CA)

6. **Per-Gigabyte WF**: 1-205 liters per GB of outbound traffic, with high end comparable to producing 1 kg of tomatoes (214 liters)

## Relevance to Sustainable Computing

This paper is foundational for understanding the full environmental footprint of digital infrastructure. Key implications:

1. **Beyond Carbon**: Demonstrates that carbon-neutral computing (via renewable energy) does not equal water-neutral computing. Hydropower and bioenergy can have massive water footprints despite low carbon.

2. **Holistic Metrics**: Argues for multi-criteria assessment including water alongside energy, carbon, and land use. PUE alone is insufficient.

3. **Location Decisions**: DC siting involves complex trade-offs between:
   - Grid carbon intensity
   - Grid water intensity
   - Local psychrometric conditions (affecting HVAC needs)
   - Cooling technology options appropriate to climate

4. **Policy Implications**: Recommends:
   - Standardized WF reporting alongside WUE
   - Integration of water metrics into sustainability frameworks (GRI)
   - Best Available Techniques (BAT) reference documents for DC water management

5. **Future Research Needs**: Grey WF from thermal pollution, supply chain WF of IT equipment, and climate change impacts on DC water requirements remain under-studied.

## Citation (APA)

Ristic, B., Madani, K., & Makuch, Z. (2015). The water footprint of data centers. *Sustainability*, *7*(8), 11260-11284. https://doi.org/10.3390/su70811260
