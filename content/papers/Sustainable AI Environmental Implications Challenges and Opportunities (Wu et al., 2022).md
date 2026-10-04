---
source_file: 2026/i609-sustainability/Wu21.pdf
type: paper
authors: Carole-Jean Wu, Ramya Raghavendra, Udit Gupta, Bilge Acun, Newsha Ardalani,
  Kiwan Maeng, Gloria Chang, Fiona Aga Behram, James Huang, Charles Bai, Michael Gschwind,
  Anurag Gupta, Myle Ott, Anastasia Melnikov, Salvatore Candido, David Brooks, Geeta
  Chauhan, Benjamin Lee, Hsien-Hsin S. Lee, Bugra Akyildiz, Maximilian Balandat, Joe
  Spisak, Ravi Jain, Mike Rabbat, Kim Hazelwood
community: Sustainable Computing
tags:
- sustainability
- i609
- artificial-intelligence
- machine-learning
- carbon-footprint
- data-centers
year: 2022
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with: []
supports: []
key_claims:
- For production systems at Facebook, inference dominates resource allocation with
  a 10:20:70 power capacity breakdown across Experimentation:Training:Inference phases,
  challenging the research community's focus on training-only carbon estimates
- Embodied carbon from hardware manufacturing accounts for roughly 50% of location-based
  operational carbon footprint for large-scale ML tasks, and becomes the dominant
  source when accounting for renewable energy adoption
- 'Jevon''s Paradox manifests in AI systems: despite 20% efficiency improvements every
  6 months, the net operational power footprint reduction was only 28.5% over two
  years because AI infrastructure continued to scale out'
- Cross-stack optimization achieved 800x operational footprint reduction for language
  translation through combined platform-level caching (6.7x), GPU acceleration (10.1x),
  and algorithmic optimization (12x)
- GPU utilization in experimentation phase is only 30-50%, representing a major optimization
  opportunity that could reduce carbon footprint without sacrificing model quality
methodology: '[[methods/Case Study]]'
sample_size: null
sample_type: Production ML systems at Facebook and open-source large language models
  (GPT-3, Meena, BERT-NAS, T5, Switch Transformer)
context: Large-scale AI infrastructure deployment at Facebook/Meta spanning recommendation
  systems and language models
study_type: empirical
---

# Sustainable AI: Environmental Implications, Challenges and Opportunities

## Summary

This landmark paper from Facebook AI (now Meta), authored by a team of 24 researchers led by Carole-Jean Wu, provides the first comprehensive industry analysis of AI's environmental footprint from a holistic perspective spanning data, algorithms, and system hardware. Published in Proceedings of Machine Learning and Systems (2022), the work is groundbreaking because it moves beyond the commonly cited training-only carbon estimates (such as the widely publicized GPT-3 and Meena figures) to examine the complete machine learning development cycle including data processing, experimentation, training, and inference. The authors reveal that for production recommendation systems at Facebook, inference can dominate carbon footprint, while training dominates for language models, demonstrating that there is no single pattern across AI applications. Most significantly, the paper quantifies the growing importance of embodied carbon from manufacturing AI hardware, noting that "more than 50% of Facebook's emissions owe to its value chain - Scope 3 of Facebook's GHG emission" (Wu et al., 2022, p. 3). This finding challenges the common focus on operational energy efficiency alone. The paper provides a sustainability roadmap spanning data efficiency, algorithm optimization, and hardware co-design, making it essential reading for understanding AI's environmental trajectory.

## Research Overview

The central research question asks: What is the true environmental footprint of AI computing when examined holistically across the machine learning development lifecycle and system hardware, and what are the opportunities for reducing this footprint?

The methodology combines empirical analysis of production ML systems at Facebook with comparative analysis of open-source large models (GPT-3, Meena, BERT-NAS, T5, Switch Transformer). The research scope covers:

**ML Development Phases**: The paper identifies four major phases: "Data Processing, Experimentation, Training, and Inference" (Wu et al., 2022, p. 3). This decomposes the ML lifecycle more granularly than prior work.

**Life Cycle Analysis Framework**: Following industrial ecology principles, the authors assess carbon from "manufacturing, transport, product use, and recycling" with focus on "manufacturing" (embodied carbon footprint) and "product use" (operational carbon footprint) (p. 3).

**Key Finding on Phase Distribution**: "At Facebook, we observe a rough power capacity breakdown of 10:20:70 for AI infrastructures devoted to the three key phases - Experimentation, Training, and Inference" (p. 3). This demonstrates that inference demands the majority of compute resources.

**Carbon Intensity Methodology**: The authors "measure the total energy consumed, assume location-based carbon intensities, and use a data center Power Usage Effectiveness (PUE) of 1.1" (p. 4) for emissions calculations.

## Theoretical Framework

The paper operates within several theoretical frameworks:

**Life Cycle Assessment (LCA)**: A standard environmental assessment methodology adapted for AI systems. The authors emphasize that "from the perspective of AI's carbon footprint analysis, manufacturing and product use are the focus" (Wu et al., 2022, p. 3).

**Embodied vs. Operational Carbon**: Following hardware sustainability literature, embodied carbon refers to "carbon emissions from building infrastructures specifically for AI" while operational carbon comes from "the use of AI" (p. 3). The key insight is that "embodied carbon cost becomes the dominating source of AI's overall environmental impact" as operational efficiency improves and renewable energy adoption increases (p. 7).

**Jevon's Paradox**: A critical concept explaining why efficiency gains may not reduce total impact: "The net effect, with Jevon's Paradox, is a 28.5% operational power footprint reduction over two years" despite 20% efficiency improvements every six months, because "AI infrastructure continued to scale out" (p. 5). This explains how efficiency improvements coexist with growing total footprint.

**Sustainability Mindset**: The authors advocate for moving beyond accuracy-only metrics: "we must achieve competitive model accuracy at a fixed or even reduced computational and environmental cost" (p. 7).

## Central Arguments

**Argument 1: Holistic Assessment Requires Looking Beyond Training**

The paper challenges the focus on training-only emissions popularized by prior research: "Although recent work shows the carbon footprint of training one large ML model, such as Meena, is equivalent to 242,231 miles driven by an average passenger vehicle, this is only one aspect; to fully understand the real environmental impact we must consider the AI ecosystem holistically going forward" (Wu et al., 2022, p. 2).

For production systems at Facebook: "For recommendation use cases, we find the carbon footprint is split evenly between training and inference. On the other hand, the carbon footprint of LM is dominated by the inference phase, using much higher inference resources (65%) as compared to training (35%)" (p. 4).

**Argument 2: Embodied Carbon is Becoming Dominant**

As operational carbon is reduced through renewable energy and efficiency: "When considering the overall life cycle of ML models and systems in this analysis, manufacturing carbon cost is roughly 50% of the (location-based) operational carbon footprint of large-scale ML tasks. Taking into account carbon-free energy, such as solar, the operational energy consumption can be significantly reduced, leaving the manufacturing carbon cost as the dominating source of AI's carbon footprint" (p. 4-5).

Figure 5 shows that for large-scale ML tasks, projected embodied carbon approaches or exceeds operational carbon even before accounting for renewable energy offsets.

**Argument 3: Cross-Stack Optimization is Essential**

Efficiency must span the entire stack: "Optimization is an iterative process - we reduce the power footprint across the machine learning hardware-software stack by 20% every 6 months. But at the same time, AI infrastructure continued to scale out" (p. 5).

The paper demonstrates 800x operational footprint reduction for language translation through combined optimizations:
- Platform-level caching: 6.7x improvement
- GPU acceleration: 10.1x additional improvement
- Algorithmic optimization (precision reduction, custom operators): 12x additional improvement

**Argument 4: A Sustainability Mindset Must Become Standard**

The call to action: "We must take a deliberate approach when developing AI research and technologies, considering the environmental impact of innovations and taking a responsible approach to technology development" (p. 10).

## Evidence

**Operational Carbon Analysis**:
- "The average carbon footprint for ML training tasks at Facebook is 1.8 times larger than that of the open-source Meena model and one-third of GPT-3's carbon footprint" (Wu et al., 2022, p. 4)
- Training recommendation models requires "2.96 GPU days" at p50, with p99 reaching "125 GPU days" (p. 3)
- Inference produces "trillions of daily predictions to serve billions of users worldwide" (p. 3)

**Infrastructure Scale**:
- Data growth: "2.4x and 1.9x in the last two years, reaching exabyte scale" for recommendation use cases (p. 1)
- Model growth: "20x" increase in recommendation model sizes between 2019-2021 (p. 2)
- Infrastructure growth: "2.9x and 2.5x capacity increases for AI training and inference" over 18 months (p. 2)

**Efficiency Improvements**:
- "28.5% operational power footprint reduction over the two-year time period" (p. 5)
- PUE of 1.1 compared to industry average of 1.58 (p. 4)
- GPU utilization in experimentation is only "30-50%" leaving significant room for improvement (p. 8)

**Limitations**:
- Analysis is specific to Facebook's infrastructure and workloads
- Embodied carbon estimates rely on assumptions about hardware utilization (30-60%) and server lifetime (3-5 years)
- Network and storage carbon not fully quantified
- Focus on large-scale systems may not generalize to smaller deployments

## Conclusion

This paper establishes the definitive framework for understanding AI's environmental footprint. The key insight is that single-metric assessments (e.g., training carbon for one model) dramatically underestimate the true impact, which spans the entire ML lifecycle and includes substantial embodied carbon from hardware manufacturing.

For future recall: (1) The 10:20:70 ratio of Experimentation:Training:Inference power allocation at scale; (2) Embodied carbon approaches 50% of operational and becomes dominant with renewable energy; (3) Jevon's Paradox explains why efficiency gains don't reduce total footprint; (4) Cross-stack optimization (800x for LM) is achievable through platform, hardware, and algorithmic improvements combined; (5) GPU utilization in experimentation is only 30-50%, representing major optimization opportunity.

The paper's call for a "sustainability mindset" that includes carbon footprint alongside accuracy as a research evaluation criterion is particularly important. The proposed metrics - reporting total runtime, hardware platforms, and number of machines - provide a minimum standard for research transparency.

## APA Citation

Wu, C.-J., Raghavendra, R., Gupta, U., Acun, B., Ardalani, N., Maeng, K., Chang, G., Aga Behram, F., Huang, J., Bai, C., Gschwind, M., Gupta, A., Ott, M., Melnikov, A., Candido, S., Brooks, D., Chauhan, G., Lee, B., Lee, H.-H. S., Akyildiz, B., Balandat, M., Spisak, J., Jain, R., Rabbat, M., & Hazelwood, K. (2022). Sustainable AI: Environmental implications, challenges and opportunities. *Proceedings of Machine Learning and Systems, 4*, 795-813.

## Discussion Questions

1. The paper reveals that inference can dominate carbon footprint for production systems, yet most research focuses on training efficiency. How should the ML research community shift its priorities, and what publication incentives would encourage inference optimization?

2. Jevon's Paradox suggests that efficiency improvements enable more AI deployment rather than reducing total emissions. What policy or technical mechanisms could decouple AI capability growth from environmental impact?

3. The authors argue that embodied carbon from hardware manufacturing is becoming dominant. How should this insight change hardware procurement and lifecycle decisions at technology companies?

4. The paper calls for reporting carbon footprint alongside accuracy metrics. What standardized methodology would enable fair comparisons across research papers, given variations in hardware, geography, and measurement approaches?

## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Artificial Intelligence]]
- [[topics/Machine Learning]]
- [[topics/Data Centers]]
- [[topics/Green Computing]]
- [[topics/Life Cycle Assessment]]
