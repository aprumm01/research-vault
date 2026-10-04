---
source_file: 2026/i609-sustainability/Xia25.pdf
type: paper
authors: Tianqi Xiao, Francesco Fuso Nerini, H. Damon Matthews, Massimo Tavoni, Fengqi
  You
community: Sustainable Computing
tags:
- sustainability
- i609
- artificial-intelligence
- net-zero
- water-footprint
- carbon-emissions
- energy-policy
year: 2025
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with:
- '[[concepts/Technological Determinism]]'
supports:
- '[[concepts/Wicked Problems]]'
key_claims:
- AI servers in the United States could generate an annual water footprint ranging
  from 731 to 1,125 million m³ and additional annual carbon emissions from 24 to 44
  Mt CO2-equivalent between 2024 and 2030
- Indirect water footprint contributes 71% of total water use, with direct cooling
  use at only 29%, highlighting that grid electricity generation dominates water consumption
- The AI server industry is unlikely to meet its net-zero aspirations by 2030 without
  substantial reliance on highly uncertain carbon offset and water restoration mechanisms
- Combined best practices cut residual emissions and water footprints by 73% and 86%,
  respectively, but achieving net-zero requires 28 GW of wind or 43 GW of solar additions
  beyond current plans
- Texas, Montana, Nebraska, and South Dakota emerge as optimal candidates for AI server
  installation, considering both water scarcity concerns and future decarbonization
  efforts
methodology: '[[methods/Scenario Building]]'
sample_size: null
sample_type: null
context: United States AI server deployment projections 2024-2030
study_type: theoretical
---

# Environmental Impact and Net-Zero Pathways for Sustainable Artificial Intelligence Servers in the USA

## Summary

Tianqi Xiao (Cornell University) and colleagues from an international team spanning Sweden, UK, Italy, and Canada present the most comprehensive analysis to date of AI's compound environmental impacts across energy, water, and carbon emissions in this Nature Sustainability paper (December 2025). The work is groundbreaking for several reasons: it projects AI server deployment through 2030, analyzes the interconnected energy-water-climate nexus rather than examining dimensions in isolation, and provides actionable pathways toward net-zero emissions. The findings are sobering: AI servers in the United States could generate "an annual water footprint ranging from 731 to 1,125 million m3 and additional annual carbon emissions from 24 to 44 Mt CO2-equivalent between 2024 and 2030" (Xiao et al., 2025, p. 1541). The paper demonstrates that achieving net-zero requires not just efficiency improvements but strategic spatial distribution of data centers to regions with favorable renewable energy potential and water availability, particularly identifying Midwestern states (Texas, Montana, Nebraska, South Dakota) as optimal locations. Most critically, the research reveals that "the AI server industry is unlikely to meet its net-zero aspirations by 2030 without substantial reliance on highly uncertain carbon offset and water restoration mechanisms" (p. 1541), challenging industry sustainability claims.

## Research Overview

The central research question asks: What are the magnitude and spatiotemporal distributions of energy consumption, water footprint, and climate impact from AI server deployment in the United States between 2024 and 2030, and what pathways could achieve net-zero goals?

The methodology employs scenario-based modeling with comprehensive uncertainty analysis:

**Scenario Design**: Five scenarios are modeled: "low demand, low power, mid-case, high application and high demand" (Xiao et al., 2025, p. 1542). The mid-case serves as baseline while low/high scenarios bound projections.

**Spatial Analysis**: State-level allocation of AI servers using "power usage effectiveness (PUE), and projected grid water usage effectiveness (WUE) and projected grid carbon intensity" for each state (p. 1542).

**Key Projections** (mid-case scenario):
- Annual energy consumption: 174.1 TWh by 2030
- Annual water footprint: 860.1 million m3 by 2030
- Annual carbon emissions: 26.8 Mt by 2030

**Manufacturing Bottleneck Analysis**: The study uniquely examines "the forecast of the AI chip manufacture capacity" using CoWoS (Chip-on-Wafer-on-Substrate) technology as a constraint on AI server expansion.

## Theoretical Framework

The paper operates within several theoretical and methodological frameworks:

**Energy-Water-Climate Nexus**: Rather than analyzing environmental dimensions separately, the authors integrate "energy, water, and carbon impacts, incorporating dynamic interactions with local energy systems" (Xiao et al., 2025, p. 1542). This recognizes that water is needed for both electricity generation and data center cooling, creating compound effects.

**Life Cycle Assessment Perspective**: Following standard LCA approaches, the study divides impacts into scopes: "Scope 1 encompasses the on-site water footprint, calculated on the basis of on-site WUE... Scope 2 includes off-site water footprint and carbon emissions, which are contingent on the local grid power supply portfolio" (p. 1551).

**Regional Energy Deployment System (ReEDS)**: Grid carbon and water factors are derived from the NREL ReEDS model, which projects future grid development patterns under different decarbonization scenarios.

**Power Usage Effectiveness (PUE) and Water Usage Effectiveness (WUE)**: Standard data center efficiency metrics where PUE measures total facility energy divided by IT equipment energy, and WUE measures water use per unit of energy.

**Utilization-Based Energy Model**: AI server electricity usage follows the model "P_server = (P_max - P_idle)u + P_idle" where utilization u incorporates "average processor utilization of active GPUs and the ratio of active GPUs to total GPUs" (p. 1550).

## Central Arguments

**Argument 1: AI's Environmental Impact is Substantial and Growing**

The projections reveal massive scale: "The projected accumulative capacity of AI servers in the United States from 2024 to 2030 under different scenarios" ranges from approximately 17.6 GW (lowest scenario) to 33.7 GW (highest scenario) (Xiao et al., 2025, p. 1543).

The water footprint is particularly significant: "indirect water footprint contributes 71% of total, with direct use at 29%" (p. 1542), highlighting that grid electricity generation dominates water consumption.

**Argument 2: Efficiency Improvements Alone are Insufficient**

Even with best practices: "The best-practice scenario approaches the physical limits of AI data centres... our best-case scenario for industry efficiency approaches the physical limits of AI data centres. Moreover, projections from the US Energy Information Administration offer limited support for additional grid decarbonization compared with the considered best case. These constraints suggest that, without additional interventions, AI data centres are likely to generate substantial environmental impacts in the coming years" (p. 1547).

Specific efficiency potentials:
- PUE reduction yields ~7% reduction in energy, emissions, and water footprint
- WUE reduction yields ~85% reduction in total water footprint
- Advanced Liquid Cooling (ALC) can reduce 1.7% of energy, 2.4% of water, 1.6% of carbon by 2030
- Server Utilization Optimization (SUO) can reduce 5.5% in all footprint values

**Argument 3: Spatial Distribution is Critical**

Location choices dramatically affect environmental outcomes: "States such as Georgia, Nevada, North Carolina and Tennessee showed marked sensitivity to renewable cost scenarios. In addition, the Pacific states, including California, Oregon and Washington, which achieved a low grid carbon factor, slow their hydropower adoption pace under the LRC scenario, avoiding exacerbating their water scarcity issues with additional AI server installations" (p. 1545).

Optimal locations identified: "Texas, Montana, Nebraska and South Dakota emerge as optimal candidates for AI server installation, considering both water scarcity concerns and future decarbonization efforts" (p. 1548).

**Argument 4: Net-Zero Requires Combined Strategies**

The pathways analysis shows: "Notably, combined best practices cut residual emissions and water footprints by 73% and 86%, respectively, indicating a feasible pathway to net zero. Under the mid-case, best industry, spatial and grid scenarios each reduces over 21 Mt, 25 Mt and 92 Mt of carbon from a base of 186 Mt due to AI server installation" (p. 1547).

However, best-case achievement requires 28 GW of wind or 43 GW of solar to offset carbon emissions by 2030.

## Evidence

**Scenario Projections**:
- Energy consumption (2024-2030): Lowest 147.3 TWh, Mid-case 174.1 TWh, Highest 244.9 TWh
- Water footprint (2024-2030): Lowest 730.8 million m3, Mid-case 860.1 million m3, Highest 1124.5 million m3
- Carbon emissions (2024-2030): Lowest 24.0 Mt, Mid-case 26.8 Mt, Highest 44.1 Mt

**State-Level Variation**:
The paper includes detailed radar charts showing PUE, WUE, grid carbon factor, and grid water factor for all 50 states plus DC, revealing that "southern states such as Florida exhibit higher PUE and WUE than northern states such as Washington, reflecting climate impacts" (p. 1542).

**Sensitivity Analysis**:
Figure 6 provides sensitivity analysis across multiple parameters including server lifetime (3, 4, 5 years), US allocation ratio (30%, 53%, 70%), server maximum power (70%, 88%, 100%), and training/inference ratio (10:30:50). Results show uncertainties of -43.4% to +32.1% for energy consumption and -43.4% to +32.1% for carbon emissions.

**Limitations**:
- Model and algorithm innovations could "fundamentally alter computing requirements" (p. 1551)
- Supply-chain uncertainties for CoWoS technology
- Hardware and data-centre efficiency evolution uncertain
- Geopolitical and market forces not fully modeled
- Confidential commercial data limits reproducibility in some areas

## Conclusion

This paper provides the most rigorous assessment to date of AI's compound environmental footprint and pathways to sustainability. The integration of energy, water, and carbon analysis reveals interdependencies that single-dimension studies miss, particularly the dominance of indirect water use from grid electricity.

For future recall: (1) AI servers in the US could generate 731-1,125 million m3 annual water footprint and 24-44 Mt CO2 annually by 2030; (2) Indirect water (from electricity generation) is 71% of total, direct cooling only 29%; (3) Best-practice efficiency improvements can achieve up to 73% emissions reduction and 86% water footprint reduction; (4) Texas, Montana, Nebraska, and South Dakota are optimal locations balancing renewable potential and water availability; (5) Net-zero by 2030 requires 28 GW wind or 43 GW solar additions beyond current plans; (6) Current industry claims of net-zero are "unlikely to be met without substantial reliance on highly uncertain carbon offset and water restoration mechanisms."

The policy implications are significant: AI expansion must be strategically located, efficiency improvements must be pursued across PUE, WUE, and utilization dimensions simultaneously, and honest accounting of offset reliance is needed for credible sustainability claims.

## APA Citation

Xiao, T., Fuso Nerini, F., Matthews, H. D., Tavoni, M., & You, F. (2025). Environmental impact and net-zero pathways for sustainable artificial intelligence servers in the USA. *Nature Sustainability, 8*(12), 1541-1553. https://doi.org/10.1038/s41893-025-01681-y

## Discussion Questions

1. The paper identifies Midwestern states as optimal for AI server deployment due to renewable energy potential and water availability. What social, economic, and infrastructure challenges might arise from concentrating AI infrastructure in these regions, and how might local communities be affected?

2. The findings suggest that industry net-zero claims depend heavily on "uncertain carbon offset and water restoration mechanisms." How should regulators and investors evaluate corporate sustainability claims in the AI sector given these findings?

3. The water footprint analysis reveals that indirect water consumption (from electricity generation) dominates direct cooling needs. How might this finding change the conversation about data center water use and the relative priority of cooling efficiency versus grid decarbonization?

4. The paper models scenarios to 2030, but AI capabilities are evolving rapidly with innovations like DeepSeek potentially changing energy requirements. How should environmental projections account for fundamental technological discontinuities that could either increase or decrease environmental impact?

## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Artificial Intelligence]]
- [[topics/Net-Zero Emissions]]
- [[topics/Water Footprint]]
- [[topics/Energy Policy]]
- [[topics/Data Centers]]
- [[topics/Climate Change]]
