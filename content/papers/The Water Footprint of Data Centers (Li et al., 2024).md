---
source_file: 2026/i609-sustainability/Ris15.pdf
type: paper
authors: Bora Ristic, Kaveh Madani, Zen Makuch
community: Sustainable Computing
tags:
- sustainability
- i609
- data-centers
- water-footprint
- water-energy-nexus
- environmental-impact
- cooling-systems
year: 2015
builds_on: []
critiques: []
tensions_with: []
supports: []
key_claims:
- Data center water footprint ranges from 1,047 to 151,061 cubic meters per terajoule
  of energy consumed, or equivalently 1-205 liters per gigabyte of outbound data traffic
- Energy consumption constitutes by far the greatest share of DC WF, but the level
  of uncertainty associated with the WF of different energy sources used by DCs makes
  a comprehensive assessment of DCs' water use efficiency very challenging
- The uncertainty range involved in determining the WFsource hinders a definitive
  recommendation on which HVAC technology has the lowest total WF
- While air-cooled condensers with no evaporation have no direct water consumption,
  the WF of generating the additional electricity required more than neutralizes the
  gains of not having a direct footprint
- Annual global data center water footprint ranges from 767-147,082 million cubic
  meters based on 2010 consumption levels
methodology: '[[methods/Case Study]]'
sample_size: null
sample_type: Global data centers and Apple facility data
context: Global data center industry with specific analysis of Phoenix cooling systems
  and Apple facilities
study_type: empirical
---

# The Water Footprint of Data Centers

## Summary

This pioneering article conducts the first systematic water footprint (WF) accounting for data centers, addressing a critical blind spot in ICT sustainability research. Published in the journal *Sustainability* in August 2015, the authors Bora Ristic, Kaveh Madani, and Zen Makuch from the Center for Environmental Policy at Imperial College London present preliminary calculations estimating that data center water footprint ranges from 1,047 to 151,061 cubic meters per terajoule of energy consumed, or equivalently 1-205 liters per gigabyte of outbound data traffic. To contextualize this magnitude, the authors note this is "roughly equal to the WF of 1 kg of tomatoes at the higher end" (Ristic et al., 2015, p. 11260). While extensive research has examined data center energy efficiency, this paper demonstrates that water impacts have received virtually no attention despite data centers accounting for 1.1-1.5% of global electricity consumption as of 2010. The research is foundational for sustainable computing because it establishes the water-energy nexus as a critical consideration for data center design, siting, and operation, revealing that energy consumption typically constitutes the greatest share of data center water footprint but with substantial uncertainty that complicates technology choice recommendations.

## Research Overview

The central research question asks: What is the water footprint of data centers, and what are the key factors driving uncertainty in its assessment? The authors frame this as addressing "a gap in the literature" since "WF has not yet been used for measuring the water impacts of DCs" (Ristic et al., 2015, p. 11263). The methodology applies the Water Footprint (WF) framework, which "measures the quantity of freshwater consumed and polluted and is divided into blue, green, and grey water footprint" (Ristic et al., 2015, p. 11263). Blue WF covers freshwater consumption from surface or groundwater; green WF covers rainwater consumed; grey WF measures water required to assimilate pollutants. The study synthesizes data from multiple sources including Koomey's estimates of global DC energy use (732,240-978,480 TJ/year in 2010), energy source WF values from Mekonnen et al., HVAC water consumption data from Vokoun, and Apple's environmental reports. Key concepts include Water Use Effectiveness (WUE), defined as "Total Facility Water Use / IT Equipment Energy" (Ristic et al., 2015, p. 11264), and the distinction between direct WF (on-site water consumption for cooling) and indirect WF (water consumed in electricity generation).

## Theoretical Framework

The study employs the Water Footprint methodology as its primary theoretical framework, which "offers the most comprehensive scoping of the measurement of impacts on water resources out of the metrics considered" (Ristic et al., 2015, p. 11263). The framework distinguishes between: (1) water withdrawal, measuring "the total freshwater input into a process"; (2) water consumption, measuring "the volume of total water input that has become unavailable for reuse due to evaporative losses, incorporation into a product, or transfer to another catchment"; and (3) grey water footprint, defined as "the volume of freshwater that is required to assimilate the load of pollutants given natural background concentrations and existing ambient water quality standards" (Ristic et al., 2015, p. 11263).

The authors also engage with the Green Grid's Water Use Effectiveness (WUE) metric, noting it "does not take into account the full lifecycle" (Ristic et al., 2015, p. 11264) and therefore misses indirect water consumption from energy sources. The theoretical framework incorporates concepts of energy proportionality and the water-energy nexus, recognizing that "using more energy increases the use of water, which in turn increases energy use even further" (Ristic et al., 2015, p. 11261). The study also draws on ASHRAE guidelines for psychrometric conditions in data centers, specifying "a temperature range of 18-27 degrees C (64-81 degrees F), a dew point range of 5-15 degrees C (41-59 degrees F), and a maximum relative humidity of 60%" (Ristic et al., 2015, p. 11267).

## Central Arguments

The paper's central argument is that water footprint must become a primary consideration in data center sustainability assessment, alongside and integrated with energy efficiency metrics. The main thesis is articulated as: "Given the rising use of DCs coupled with rising environmental stress, substantially more attention should be paid to the WF of DCs" (Ristic et al., 2015, p. 11278).

**Sub-claim 1 - Energy dominates WF**: "Typically, energy consumption constitutes by far the greatest share of DC WF, but the level of uncertainty associated with the WF of different energy sources used by DCs makes a comprehensive assessment of DCs' water use efficiency very challenging" (Ristic et al., 2015, p. 11260).

**Sub-claim 2 - Uncertainty limits decision-making**: "The uncertainty range involved in determining the WFsource hinders a definitive recommendation on which HVAC technology has the lowest total WF, hence which technologies can provide environmental innovations most readily" (Ristic et al., 2015, p. 11274). The authors demonstrate this through Phoenix, Arizona case study where optimal cooling technology depends on which end of the energy source WF range is assumed.

**Sub-claim 3 - Focus should remain on energy efficiency**: "The first focus for reducing DC WF should be on air-side economization and energy efficiency" (Ristic et al., 2015, p. 11276), since reducing energy consumption reduces both direct and indirect water footprint.

**Sub-claim 4 - Policy response needed**: "It is fundamental that firms collaborate in the development of leading industry standards such as the WUE. As a parallel activity, standardization, monitoring, and reporting templates for DC WF should be created" (Ristic et al., 2015, p. 11277).

## Evidence

The authors provide extensive quantitative calculations supporting their water footprint estimates.

**Global DC water footprint calculation**: Using Koomey's DC energy values (732,240-978,480 TJ/year) multiplied by the global average energy portfolio WF (1,047-150,317 cubic meters per TJ), the study calculates annual DC water footprint of "767-147,082 million cubic meters (mcm) for the annual WF of energy consumed by DCs" (Ristic et al., 2015, p. 11276).

**Per-gigabyte water footprint**: "Dividing the above calculated values for annual DC WF by the outbound data traffic... DC WF gives us the range: 1-205 mcm/EB or liters per gigabyte of data sent out of DCs" (Ristic et al., 2015, p. 11276).

**Energy source WF variability**: Figure 3 shows consumptive WF per unit of electricity output varying dramatically by source: wind has the lowest (approximately 1 cubic meter per TJ), while firewood has the highest (approaching 1,000,000 cubic meters per TJ). Solar, nuclear, coal, and natural gas cluster between 100-10,000 cubic meters per TJ.

**Cooling technology trade-offs**: Figure 6 demonstrates the direct vs. indirect WF trade-off for four cooling options in Phoenix: "Direct Evaporation or Air-Cooled" uses 7,748 cubic meters for energy but only 192 for cooling; "No Evaporation or Air-Cooled" uses 8,980 cubic meters for energy and 1,691 for cooling. The counterintuitive finding is that "while the 'air cooled condensers/no evaporation' option has no direct water consumption, but because of greater electricity demand, The WF of generating this additional electricity more than neutralizes the gains of not having a direct footprint" (Ristic et al., 2015, p. 11274).

**Apple case study**: Table 1 presents Apple DC energy sources: Maiden, NC (576 TJ/year, 47% biogas, 53% solar); Newark, CA (443 TJ/year, 100% grid renewable); Prineville, OR (65 TJ/year, 100% wind); Reno, NV (11 TJ/year, 100% geothermal). Figure 5 shows resulting WFsource varies from near-zero for Maiden to approximately 200 cubic meters per TJ for Reno.

**Limitations**: The authors acknowledge significant data constraints: "This study has been limited to one simple dataset on different HVAC systems operating in Phoenix, because very little data can be found for the WF of DCs, or even HVAC systems, generally" (Ristic et al., 2015, p. 11278). Additionally, "the above data do not include the grey water footprint that is associated with water cooling" (Ristic et al., 2015, p. 11275).

## Conclusion

This foundational paper establishes water footprint as an essential but previously neglected dimension of data center sustainability. The key insight for long-term recall is the dominance of indirect water consumption through energy generation, which means that energy efficiency improvements simultaneously address both carbon and water sustainability goals. However, the massive uncertainty ranges in energy source WF values (spanning multiple orders of magnitude) currently prevent definitive technology recommendations for HVAC systems. The Phoenix case study vividly demonstrates this challenge: depending on which end of the energy source WF range is assumed, different cooling technologies emerge as optimal. For practitioners, the implication is that DC location decisions must consider not just climate conditions and energy costs but also the regional energy mix's water intensity. The study provides a critical warning against narrow optimization: "if an energy technology has a low carbon footprint, it cannot be considered 'green' or 'sustainable' unless its other footprints (i.e., water and land use footprints), together with cost, compare favourably to other energy technologies" (Ristic et al., 2015, p. 11262). Future research priorities include reducing uncertainty in energy source WF values, developing standardized DC WF reporting frameworks, and examining grey water footprint from cooling system chemical discharges.

## APA Citation

Ristic, B., Madani, K., & Makuch, Z. (2015). The water footprint of data centers. *Sustainability*, *7*(8), 11260-11284. https://doi.org/10.3390/su70811260

## Discussion Questions

1. The study finds that cooling technology choice may matter less than energy source choice for total water footprint. How should this insight influence data center siting decisions in water-stressed regions that may have abundant renewable energy?

2. Given the enormous uncertainty ranges in energy source water footprints (spanning multiple orders of magnitude), what research and measurement infrastructure would be needed to enable confident sustainability assessments for data center operations?

3. The authors note that large DC operators like Facebook and Google are building new facilities in cold climates where free cooling is effective. What are the trade-offs between water footprint reduction and other sustainability considerations (transmission losses, land use, community impacts) in such location decisions?

4. How might the water-energy nexus constraints identified in this paper affect the feasibility of data center growth in regions already experiencing water stress, such as the southwestern United States or parts of India and China?

## Connections

- [[topics/Sustainable Computing]]
- [[topics/Data Center Energy Efficiency]]
- [[topics/Water-Energy Nexus]]
- [[topics/Environmental Impact Assessment]]
- [[communities/Sustainable Computing]]
- [[topics/Cooling Systems]]
