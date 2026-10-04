---
source_file: 2026/i609-sustainability/She26.pdf
type: paper
authors: Yu Sheng, Chenxuan Zhang, Zixuan Zhu, Hongyi Xu, Junqi Wen, Ruoheng Wang,
  Jianjun Yang, Qin Wang, Siqi Bu
community: Sustainable Computing
tags:
- sustainability
- i609
- AI-data-centers
- grid-impacts
- energy-demand
- power-systems
- renewable-energy
year: 2026
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with:
- '[[concepts/Technological Determinism]]'
supports:
- '[[concepts/Wicked Problems]]'
key_claims:
- AI data centers consume approximately 460 TWh of electricity in 2022 (about 2% of
  global electricity demand), projected to double by 2026 to roughly 1000 TWh—approximately
  the entire electricity consumption of Japan
- AI data centers operate at ultra-high power densities of 30-100+ kW per rack versus
  5-15 kW for traditional data centers, with near-100% sustained utilization during
  training versus <40% for traditional centers
- A pronounced timing mismatch exists between rapid AI hardware deployment (2 years)
  and slower grid modernization (5-10 years for major transmission upgrades), creating
  systemic integration challenges
- Inference may account for up to 90% of AI lifecycle energy consumption as deployment
  horizons extend, with complex prompts consuming 29.078 ± 9.725 Wh versus 0.3 Wh
  for keyword searches
- AI data centers introduce novel grid stability threats including sympathetic tripping,
  subsynchronous oscillations at 14.7 Hz from power electronics interactions, and
  extreme transient spikes that existing grid codes were not designed to handle
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: null
context: Global AI data center energy infrastructure across multiple geographic regions
  including Ireland, Northern Virginia, and UK
study_type: review
---

# Power for AI Data Centers: Energy Demand, Grid Impacts, Challenges and Perspectives

## Summary

This comprehensive review article examines the rapidly evolving energy landscape of AI data centers and their unprecedented impacts on power systems. Published in the journal *Energies* in January 2026, the authors from Hong Kong Polytechnic University (Yu Sheng, Chenxuan Zhang, Zixuan Zhu, Hongyi Xu, Junqi Wen, Ruoheng Wang, Qin Wang, and Siqi Bu) and Shenzhen Research Institute (Jianjun Yang) provide a systematic analysis of how AI computing is fundamentally transforming data center energy characteristics. The paper is particularly timely: "At the global level, data centers, cryptocurrencies, and AI consumed approximately 460 TWh of electricity in 2022 (about 2% of global electricity demand), and this consumption could rise sharply by 2026 to roughly the entire electricity consumption of Germany" (Sheng et al., 2026, p. 2). The research distinguishes AI data centers from traditional cloud facilities, demonstrating that AI workloads create qualitatively different grid challenges through ultra-high power densities (30-100+ kW per rack versus 5-15 kW for traditional), near-100% utilization rates during training, and extreme transient load characteristics. This review is essential for sustainable computing because it maps the collision course between AI industry growth and global decarbonization goals, while cataloging emerging solutions across grid, data center, and user-side domains.

## Research Overview

The paper addresses a central question: How do AI data centers impact power systems, and what solutions can enable their sustainable integration? The review methodology employed "a comprehensive search across major academic databases, including IEEE Xplore, ScienceDirect, MDPI, and Google Scholar" (Sheng et al., 2026, p. 4), supplemented by industry technical reports from EPRI, IEA, and major cloud providers. The literature search focused on the intersection of "AI data center," "Large Language Model (LLM) energy consumption," "grid impact of AI," and "data center demand response" primarily covering 2018-2026. The research framework connects four dimensions: (1) energy profiles of AI workloads across preparation, training, fine-tuning, and inference stages; (2) grid impacts on stability, reliability, markets, and infrastructure planning; (3) technological, operational, and sustainability challenges; and (4) emerging solutions at grid-side, data-center-side, and user-side levels. Key concepts defined include Power Usage Effectiveness (PUE = Total energy consumption of data center / Energy consumption of IT equipment), Water Usage Effectiveness (WUE = Total Site Water Usage / IT Equipment Energy), and Carbon Usage Effectiveness (CUE = Total CO2 Emissions / IT Equipment Energy).

## Theoretical Framework

The paper employs a multi-dimensional framework distinguishing AI data centers from traditional cloud infrastructure across several parameters. Table 1 presents a systematic comparison: traditional centers operate at "Low to Medium Density (5-15 kW/rack)" while AI centers require "Ultra-High Density (30-100+ kW/rack)"; traditional centers show "Bursty, variable traffic; Average utilization often low (<40%)" while AI centers exhibit "Sustained peak load (~100% for training tasks); Continuous operation" (Sheng et al., 2026, p. 7).

The theoretical framework for grid impacts encompasses four functional dimensions: "(i) physical grid stability and reliability constraints, (ii) electricity markets and price, (iii) economic dispatch and operating reserve scheduling, and (iv) infrastructure planning and coordination" (Sheng et al., 2026, p. 11). The concept of energy proportionality is implicitly critiqued through observations that AI workloads operate at sustained high utilization rather than scaling with demand.

Key theoretical constructs include the distinction between training energy consumption (characterized by "sustained near-peak utilization of computational hardware over long horizons--often weeks to months") and inference energy consumption (characterized by "highly stochastic bursty consumption with abrupt spikes and drops") (Sheng et al., 2026, p. 9-10). The framework also incorporates the concept of "sympathetic tripping" where "the loss of one facility increases the likelihood of cascading disconnections of neighboring loads" (Sheng et al., 2026, p. 11).

## Central Arguments

The paper's central thesis is that AI data centers represent a qualitatively new category of electricity consumer that requires fundamentally different grid integration strategies than traditional data centers. The main argument is articulated as: "The rapid scaling and expansion of AI data centers are posing unprecedented challenges to the planning, operation, and resilience of power systems" (Sheng et al., 2026, p. 2).

**Sub-claim 1 - Distinct load characteristics**: "Unlike traditional data centers for cloud storage, web hosting, and standard enterprise applications typically operate at power densities of 5 to 10 kilowatts (kW) per rack... In contrast, AI data centers are purpose-built AI factories to support high-performance clusters where thousands of GPUs operate together with distinct characteristics" (Sheng et al., 2026, p. 2). These include rack power densities exceeding 40-100 kW, near-100% utilization for weeks/months during training, and requirement for liquid cooling.

**Sub-claim 2 - Grid stability threats**: "On short time scales, loads of large AI data centers can significantly influence power-system stability and reliability... AI clusters generate extreme transient spikes and high di/dt (rate of change of current) events during computational synchronization, imposing severe stress on electrical infrastructure" (Sheng et al., 2026, p. 6, 11).

**Sub-claim 3 - Infrastructure timing mismatch**: "A pronounced timing mismatch exists between rapid AI hardware deployment and slower grid modernization. Data centers can often be constructed within two years, whereas major high-voltage transmission upgrades typically require 5-10 years for planning, permitting, and construction" (Sheng et al., 2026, p. 13).

**Sub-claim 4 - Multi-layer solutions required**: "Emerging solutions across three coordinated layers are identified and categorized: grid-side measures (e.g., enhanced forecasting), data-center-side strategies (e.g., flexible scheduling), and user-side mechanisms (e.g., delay-tolerant inference)" (Sheng et al., 2026, p. 3).

## Evidence

The paper marshals extensive quantitative evidence from academic literature and industry reports.

**Energy scale**: "The IEA projects that electricity consumption from data centers, AI, and the cryptocurrency sector could double by 2026, exceeding 1000 TWh--approximately the annual electricity consumption of Japan" (Sheng et al., 2026, p. 5). "In regions with high concentrations of data centers, such as Northern Virginia in the United States or Ireland, data centers already consume a substantial portion of the available grid capacity, reaching approximately 16% of total electricity demand in Ireland as of 2022" (Sheng et al., 2026, p. 2).

**Training energy**: "Training BLOOM (176B parameters) consumed approximately 433 MWh and required continuous execution on 384 GPUs for more than three months" (Sheng et al., 2026, p. 8). "Google's PaLM (540B parameters) required an estimated 2.56 x 10^24 floating-point operations" (Sheng et al., 2026, p. 8).

**Inference energy dominance**: "Measurements in hyperscale settings suggest that inference accounts for roughly 60% of total AI energy consumption, largely due to the request volume in billion-user services... More recent projections indicate that inference may exceed 90% of lifecycle energy as deployment horizons extend" (Sheng et al., 2026, p. 9).

**Per-query energy**: "A keyword search may consume about 0.3 Wh, whereas a long, complex prompt processed by a large generative model (e.g., DeepSeekR1) is estimated at 29.078 +/- 9.725 Wh" (Sheng et al., 2026, p. 9).

**Grid case studies**: 
- Ireland: "EirGrid, the transmission system operator, reported that data centers have introduced significant risks to system inertia and stability... EirGrid imposed a moratorium on new data center connections in the Dublin area" (Sheng et al., 2026, p. 14).
- Virginia: "In the Dominion Energy service territory (Northern Virginia), known as 'Data Center Alley,' field measurements revealed a novel stability threat involving inverter-based resources. High-frequency switching dynamics of server power supply units were found to interact with the grid impedance, exciting a subsynchronous oscillation mode at approximately 14.7 Hz" (Sheng et al., 2026, p. 14-15).
- UK: "In 2022, the Greater London Authority noted that new housing developments in West London faced delays of over a decade for electricity connections. This bottleneck was driven by the rapid proliferation of hyperscale data centers along the M4 corridor, which consumed all available transmission headroom" (Sheng et al., 2026, p. 15).

**Table 3** provides a comparative analysis of key challenges including renewable energy integration (cause: temporal/spatial mismatch; key indicators: renewable penetration rate <20%, wind curtailment rate up to 28%), waste heat utilization (cause: low-grade heat 40-60 degrees C; key indicators: heat recovery efficiency <40%, retrofit cost >200 USD/kW), carbon neutrality (cause: indirect emissions, embodied carbon; key indicators: CUE >0.5 kgCO2/kWh for grid-dependent DCs), and water-energy nexus (cause: evaporative/liquid cooling feedback loop; key indicators: WUE 1.8-2.5 L/kWh for evaporative cooling).

**Limitations**: The authors acknowledge focusing on "public GitHub repositories with at least 100 stars" and note that "articles focusing solely on internal computer architecture optimization without addressing energy or grid implications... were excluded" (Sheng et al., 2026, p. 5).

## Conclusion

This comprehensive review establishes that AI data centers represent a fundamental shift in the relationship between computing infrastructure and electrical grids. The key insight for long-term recall is the temporal mismatch between AI infrastructure deployment (2 years) and grid infrastructure modernization (5-10 years), creating a structural problem that cannot be solved by either side acting alone. The paper demonstrates that AI workloads differ qualitatively from traditional computing: sustained high utilization, extreme power density, and novel transient characteristics that existing grid codes and interconnection standards were not designed to handle. The case studies from Ireland, Virginia, and London serve as early warning indicators of systemic risks that will intensify as AI deployment accelerates.

For practitioners, the multi-layer solution framework provides a roadmap: grid-side solutions include AI-enhanced load forecasting and updated grid codes; data-center-side solutions include flexible workload scheduling, on-site storage, and energy-efficient algorithms; user-side solutions include delay-tolerant inference and carbon-aware prompting. The review emphasizes that "isolated interventions are insufficient, and that coordinated actions across grid operation, data center infrastructure, AI service design, and policy frameworks are required" (Sheng et al., 2026, p. 18). Future research priorities include developing dynamic load models for AI clusters, creating enhanced grid codes for power quality and ramp-rate limits, and designing mechanisms to value and compensate demand flexibility from data center operators.

## APA Citation

Sheng, Y., Zhang, C., Zhu, Z., Xu, H., Wen, J., Wang, R., Yang, J., Wang, Q., & Bu, S. (2026). Power for AI data centers: Energy demand, grid impacts, challenges and perspectives. *Energies*, *19*(3), 722. https://doi.org/10.3390/en19030722

## Discussion Questions

1. The paper documents a "timing mismatch" between AI deployment (2 years) and grid infrastructure (5-10 years). What policy mechanisms could help align these timelines, and what are the trade-offs between different approaches (moratoriums, co-location requirements, demand charges)?

2. Ireland's EirGrid imposed a moratorium on new data center connections in Dublin due to stability risks. Under what conditions might such moratoriums be justified, and what are their implications for global AI development and equity?

3. The case of subsynchronous oscillations in Northern Virginia reveals unexpected interactions between power electronics and grid impedance. How should interconnection standards evolve to anticipate and prevent such novel stability threats from large AI facilities?

4. The paper suggests that inference may account for 90% of AI lifecycle energy as deployment extends. How does this shift from training-dominated to inference-dominated energy consumption change the sustainability strategies that should be prioritized?

## Connections

- [[topics/Sustainable Computing]]
- [[topics/Data Center Energy Efficiency]]
- [[topics/Power Grid Stability]]
- [[topics/AI Infrastructure]]
- [[topics/Renewable Energy Integration]]
- [[communities/Sustainable Computing]]
- [[topics/Demand Response]]
