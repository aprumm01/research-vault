---
title: "Chasing Carbon: The Elusive Environmental Footprint of Computing"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Gup20.pdf"
type: paper
authors:
  - Udit Gupta
  - Young Geun Kim
  - Sylvia Lee
  - Jordan Tse
  - Hsien-Hsin S. Lee
  - Gu-Yeon Wei
  - David Brooks
  - Carole-Jean Wu
year: 2020
venue: IEEE Micro
doi: 10.1109/MM.2022.3163226
builds_on:
  - "[[Life Cycle Assessment]]"
  - "[[GHG Protocol]]"
  - "[[Dark Silicon]]"
supports:
  - "[[Sustainable Computing]]"
  - "[[Hardware Carbon Footprint]]"
  - "[[Embodied Carbon]]"
critiques:
  - "[[Energy Efficiency as Sole Metric]]"
tensions_with:
  - "[[Moore's Law Benefits]]"
  - "[[Renewable Energy as Panacea]]"
key_claims:
  - Hardware manufacturing (embodied carbon) now dominates computing's carbon footprint over operational energy use
  - For battery-powered devices, manufacturing accounts for roughly 75% of emissions
  - Renewable energy alone cannot solve computing's environmental impact due to capex-related emissions
  - Amortizing manufacturing carbon requires operating mobile devices beyond their typical 3-year lifetime
  - Efficiency gains are overshadowed by Jevon's paradox and rising application-level demands
methodology: Data-driven analysis using publicly available industry sustainability reports and GHG Protocol data from Apple, Facebook, Google, Huawei, Intel, Microsoft, and TSMC
study_type: Empirical analysis / Industry data synthesis
context: Computing industry environmental impact assessment using Greenhouse Gas Protocol framework
---

## Summary

This paper presents a comprehensive data-driven analysis of the environmental impact of computing, arguing that the primary source of carbon emissions has shifted from operational energy consumption (opex) to hardware manufacturing and infrastructure (capex). Using publicly available sustainability reports from major technology companies (Apple, Facebook, Google, Intel, TSMC, Microsoft), the authors demonstrate that as energy efficiency improves and renewable energy adoption increases, the dominant carbon footprint now comes from embodied emissions in hardware manufacturing, facility construction, and supply chain activities.

The paper introduces the distinction between **operational footprint** (emissions from energy use during device operation) and **embodied footprint** (emissions from manufacturing, materials, fabrication, packaging, and assembly). For consumer devices like iPhones, the shift has been dramatic: manufacturing accounted for 49% of emissions in iPhone 3GS but 86% in iPhone 11. Similarly, at Facebook, capex- and supply-chain activities accounted for 23x more emissions than opex-related activities in 2019.

## Key Concepts

- **Operational vs. Embodied Carbon**: The paper distinguishes between emissions from device use (operational) and emissions from manufacturing processes (embodied)
- **GHG Protocol Scopes**: 
  - Scope 1: Direct emissions (fuel combustion, refrigerants)
  - Scope 2: Purchased energy for fabs, offices, data centers
  - Scope 3: Full upstream and downstream supply chain
- **Carbon Amortization**: The concept that devices must operate long enough for operational efficiency gains to offset manufacturing carbon
- **Dark Silicon Problem**: Underutilized transistors that contribute embodied emissions without proportional use benefits
- **Life Cycle Analysis (LCA)**: Framework for quantifying emissions across production, transport, use, and end-of-life

## Key Findings

1. **Consumer Devices**: Manufacturing dominates emissions for battery-powered devices (phones, wearables, tablets) at ~75%, while operational consumption dominates for always-connected devices (desktops, game consoles)

2. **Generational Trends**: From iPhone 3GS to iPhone XR, while manufacturing accounted for 40% initially, it rose to 75% despite energy efficiency improvements

3. **Data Centers**: Between 2010-2018, operational energy increased only 6% while infrastructure capacity increased 6x, indicating rising infrastructure overhead dominance

4. **Carbon Breakeven**: For MobileNet v3 running AI inference on a CPU, it takes 5 billion images (350 days continuous operation) to equal manufacturing footprint; DSPs extend this to 1,200 days

5. **Renewable Energy Limitations**: Even with 64x improvement in renewable energy at TSMC, overall emissions only drop 2.7x due to persistent manufacturing-related emissions

6. **Company-Level Data**: 
   - Apple: Hardware manufacturing accounts for 74% of total emissions; operational only 19%
   - Google: Scope 3 emissions 21x higher than Scope 2 (14M vs 684K metric tons CO2)
   - Facebook: Scope 3 emissions 23x higher than Scope 2 (5.8M vs 252K metric tons CO2)

## Relevance to Sustainable Computing

This paper is foundational for sustainable computing research because it reframes the optimization target. While the past two decades focused heavily on energy efficiency, this analysis demonstrates that:

1. **Holistic Assessment Required**: Sustainability research must consider full life-cycle carbon, not just operational energy
2. **Longevity Over Efficiency**: Extending device lifetimes may be more impactful than incremental efficiency gains
3. **Hardware Design Implications**: Circuit designers should consider embodied carbon alongside performance and power
4. **Renewable Energy is Necessary but Insufficient**: Even 100% renewable-powered operations leave significant manufacturing emissions
5. **Cross-Stack Optimization Needed**: Solutions require collaboration across algorithms, systems, hardware, and circuits

The paper serves as a call-to-action for computer systems researchers to tackle computing's environmental crisis by fundamentally rethinking design approaches to include carbon as a first-order optimization metric alongside performance and efficiency.

## Citation (APA)

Gupta, U., Kim, Y. G., Lee, S., Tse, J., Lee, H.-H. S., Wei, G.-Y., Brooks, D., & Wu, C.-J. (2020). Chasing carbon: The elusive environmental footprint of computing. *IEEE Micro*. https://doi.org/10.1109/MM.2022.3163226
