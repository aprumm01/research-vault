---
title: "Sustainable AI: Environmental Implications, Challenges and Opportunities"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Wu21.pdf"
type: paper
authors:
  - Carole-Jean Wu
  - Ramya Raghavendra
  - Udit Gupta
  - Bilge Acun
  - Newsha Ardalani
  - Kiwan Maeng
  - Gloria Chang
  - Fiona Aga Behram
  - James Huang
  - Charles Bai
  - Michael Gschwind
  - Anurag Gupta
  - Myle Ott
  - Anastasia Melnikov
  - Salvatore Candido
  - David Brooks
  - Geeta Chauhan
  - Benjamin Lee
  - Hsien-Hsin S. Lee
  - Bugra Akyildiz
  - Maximilian Balandat
  - Joe Spisak
  - Ravi Jain
  - Mike Rabbat
  - Kim Hazelwood
year: 2021
venue: arXiv preprint (arXiv:2111.00364)
builds_on:
  - "[[Carbon Emissions and Large Neural Network Training (Patterson, 2021)]]"
  - "[[Energy and Policy Considerations for Deep Learning in NLP (Strubell, 2019)]]"
supports:
  - "[[Green AI (Schwartz, 2019)]]"
  - "[[Tackling Climate Change with Machine Learning (Rolnick, 2019)]]"
critiques:
  - "[[focus on operational carbon alone]]"
tensions_with:
  - "[[AI scaling laws prioritizing accuracy over efficiency]]"
key_claims:
  - AI's carbon footprint must be considered holistically, including both operational and embodied carbon
  - Hardware-software co-design can reduce operational carbon footprint by over 800x for Transformer models
  - Manufacturing carbon cost is roughly 50% of overall ML lifecycle carbon footprint when using carbon-free operational energy
  - Inference can dominate the carbon footprint of deployed ML models (65% vs 35% for training in some cases)
  - GPUs are typically utilized at only 30-50% capacity during ML experimentation, leaving room for efficiency improvements
  - A sustainability mindset across data, algorithms, systems, and hardware is essential for environmentally responsible AI
methodology: Industry case study analysis with quantitative carbon footprint assessment across Facebook's ML infrastructure
study_type: empirical
context: Facebook AI production systems, datacenter-scale ML workloads
---

# Sustainable AI: Environmental Implications, Challenges and Opportunities

## Summary

This landmark paper from Facebook AI presents the first holistic analysis of AI's environmental impact, examining the complete machine learning lifecycle including data processing, experimentation, training, and inference. The authors characterize the carbon footprint of AI computing by examining industry-scale ML use cases at Facebook while also considering the life cycle of system hardware (manufacturing, transport, product use, recycling).

The paper introduces a critical distinction between **operational carbon footprint** (energy consumption during AI use) and **embodied carbon footprint** (emissions from manufacturing AI hardware). A key finding is that when accounting for carbon-free energy sources like solar, manufacturing carbon cost becomes the dominating source of AI's carbon footprint—roughly 50% of the overall lifecycle carbon.

Through detailed analysis of six representative ML models at Facebook (language translation and five recommendation models), the authors demonstrate that hardware-software co-design optimization can reduce operational energy footprint by more than 800x for Transformer-based language models through platform-level caching (6.7x), GPU acceleration (10.1x), and algorithmic optimization (12x).

## Key Concepts

### ML Development Lifecycle Phases
- **Data Processing**: Feature extraction and data ingestion (optimized for storage efficiency)
- **Experimentation**: Model architecture search and hyperparameter tuning (computationally intensive)
- **Training**: Production model training with rich features and hyperparameter tuning
- **Inference**: Serving billions of predictions daily, often exceeding training compute cycles

### Carbon Footprint Components
- **Operational Carbon**: Emissions from energy consumption during AI training and inference
- **Embodied Carbon**: Manufacturing emissions from building AI hardware infrastructure
- **Value Chain Emissions (Scope 3)**: More than 50% of Facebook's emissions come from the value chain

### Jevon's Paradox in AI
Despite achieving 28.5% operational power footprint reduction over two years through optimization, overall electricity demand for AI continues to increase because efficiency improvements stimulate additional novel AI use cases.

### System Life Cycle Analysis (LCA)
Four phases: manufacturing, transport, product use, and recycling. For AI's carbon footprint, manufacturing and product use are the focus areas.

## Key Findings

1. **Training vs. Inference Breakdown**: For recommendation models, carbon footprint is split evenly between training and inference; for language models, inference dominates (65% inference vs 35% training)

2. **Model Size vs. Carbon Footprint**: The operational carbon footprint of AI does not correlate directly with model parameters—the 1.5 trillion parameter Switch Transformer produces less carbon than GPT-3 (750B parameters) due to architectural efficiency

3. **GPU Utilization Gap**: A vast majority of model experimentation utilizes GPUs at only 30-50% capacity, presenting significant opportunity for efficiency improvements through virtualization and workload consolidation

4. **Infrastructure Breakdown**: At Facebook, AI infrastructure capacity is divided roughly 10:20:70 for Experimentation:Training:Inference

5. **Optimization Potential**: Cross-stack hardware-software co-design can reduce power footprint by 20% every 6 months across Facebook's AI fleet

6. **Federated Learning Carbon**: On-device learning emits non-negligible carbon comparable to training orders-of-magnitude larger Transformer models in centralized settings due to communication overhead

7. **Data Perishability**: Natural language data sets can lose half their predictive value in less than 7 years (the "half-life" of data), affecting long-term carbon efficiency of models

## Relevance to Sustainable Computing

This paper is foundational for sustainable computing research in several ways:

1. **Holistic Framework**: Establishes the need to consider both operational and embodied carbon, challenging the common focus on training energy alone

2. **Industry-Scale Evidence**: Provides rare empirical data from production ML systems at hyperscale, validating theoretical concerns about AI's environmental impact

3. **Actionable Recommendations**: Offers concrete optimization strategies across data, algorithms, systems, metrics, standards, and best practices

4. **Call for Telemetry**: Advocates for carbon accounting methodologies and easy-to-adopt telemetry to measure AI's environmental footprint

5. **Sustainability Mindset**: Argues that the ML research community must shift from purely accuracy-focused optimization to include efficiency and carbon footprint as evaluation criteria

6. **Hardware-Software Co-Design**: Demonstrates that cross-stack optimization can achieve dramatic efficiency improvements without sacrificing model quality

7. **Carbon Impact Statements**: Recommends that all published research papers disclose operational and embodied carbon footprint of proposed designs

The paper's key message is that to bend the exponential growth curve of AI's environmental footprint, the community must adopt a sustainability mindset that prioritizes achieving competitive model accuracy at fixed or reduced computational and environmental cost.

## Citation

Wu, C.-J., Raghavendra, R., Gupta, U., Acun, B., Ardalani, N., Maeng, K., Chang, G., Aga Behram, F., Huang, J., Bai, C., Gschwind, M., Gupta, A., Ott, M., Melnikov, A., Candido, S., Brooks, D., Chauhan, G., Lee, B., Lee, H.-H. S., Akyildiz, B., Balandat, M., Spisak, J., Jain, R., Rabbat, M., & Hazelwood, K. (2021). Sustainable AI: Environmental implications, challenges and opportunities. *arXiv preprint arXiv:2111.00364*. https://arxiv.org/abs/2111.00364
