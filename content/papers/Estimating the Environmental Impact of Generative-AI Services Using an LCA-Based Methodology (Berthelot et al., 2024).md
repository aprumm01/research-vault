---
title: "Estimating the Environmental Impact of Generative-AI Services Using an LCA-Based Methodology"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/EstimatingtheenvironmentalimpactofGenerative-AIservices.pdf"
type: paper
authors:
  - Adrien Berthelot
  - Eddy Caron
  - Mathilde Jay
  - Laurent Lefevre
year: 2024
venue: "31st CIRP Conference on Life Cycle Engineering (LCE 2024), Procedia CIRP 122"
doi: "10.1016/j.procir.2024.01.098"
builds_on:
  - "[[concepts/Life Cycle Assessment]]"
  - "[[concepts/ICT Environmental Impact]]"
  - "[[papers/Energy and Policy Considerations for Deep Learning in NLP (Strubell et al., 2019)]]"
  - "[[papers/Estimating the Carbon Footprint of BLOOM (Luccioni et al., 2023)]]"
supports:
  - "[[concepts/AI Environmental Impact]]"
  - "[[concepts/Sustainable Computing]]"
  - "[[concepts/Carbon Footprint]]"
critiques:
  - "[[concepts/Carbon Tunnel Vision]]"
tensions_with:
  - "[[concepts/AI Productivity Gains]]"
  - "[[concepts/Digital Rebound Effect]]"
key_claims:
  - "Gen-AI services have significant environmental impacts beyond just carbon emissions, including metal scarcity and energy consumption"
  - "One year of Stable Diffusion service generates 360 tons of CO2 equivalent emissions"
  - "End-user terminals represent over 90% of impact on Abiotic Depletion Potential (metal scarcity)"
  - "Inference costs dominate GWP and energy footprint, while training costs are often underestimated"
  - "Network and end-user impacts are non-negligible and must be included in environmental assessments"
methodology: "Life Cycle Assessment (LCA) with experimental measurements"
study_type: "Empirical methodology development with case study"
context: "Growing deployment of generative AI services (ChatGPT, Stable Diffusion) with limited understanding of full environmental costs"
tags:
  - generative-ai
  - life-cycle-assessment
  - carbon-footprint
  - energy-consumption
  - stable-diffusion
  - environmental-impact
  - sustainable-ai
---

# Estimating the Environmental Impact of Generative-AI Services Using an LCA-Based Methodology

## Summary

This paper proposes a comprehensive Life Cycle Assessment (LCA) methodology for evaluating the environmental impact of generative AI services. Unlike previous studies that focus primarily on training energy and carbon emissions, this work takes a holistic "AI as a Service" perspective that includes: end-user terminals, networks, web hosting infrastructure, model inference, model training, and data management (acquisition, processing, storage).

The methodology is validated through a case study of Stable Diffusion, an open-source text-to-image generative model. The authors conducted experimental measurements on the Grid'5000 platform using Nvidia DGX A100 servers to measure actual training and inference energy consumption. They evaluate impact across three categories: Abiotic Depletion Potential (ADP) for mineral/metal scarcity, Global Warming Potential (GWP) for climate impact, and Primary Energy (PE) for total energy footprint.

Key finding: One year of Stable Diffusion service generates approximately 360 tons of CO2 equivalent, impacts metal scarcity equivalent to producing 5,659 smartphones, and consumes 2.48 gigawatt-hours of energy. The authors argue this demonstrates Gen-AI's environmental impact extends far beyond carbon concerns alone.

## Key Concepts

### AI as a Service Framework
The paper conceptualizes Gen-AI not as isolated model training, but as a complete digital service ecosystem with six components:
1. **End-user terminals** - Smartphones, computers used to access the service
2. **Networks** - Fixed-line and mobile network infrastructure
3. **Web hosting** - Data center servers providing the user interface
4. **Model inference** - GPU-based computation for generating outputs
5. **Model training** - Initial and ongoing training costs
6. **Data management** - Acquisition, processing, and storage of training data

### Functional Units (FUs)
Two assessment perspectives:
- **FU1 (Client view)**: Single use impact - one user visiting and generating 4 images
- **FU2 (Host view)**: Service-level impact - one year of operating the service for all users

### Impact Categories
- **Abiotic Depletion Potential (ADP)**: Measures depletion of mineral and metal resources (kg Sb equivalent)
- **Global Warming Potential (GWP)**: Climate change contribution (kg CO2 equivalent)  
- **Primary Energy (PE)**: Total energy footprint (MJ)

### Active Utilization Rate (AUR)
Critical parameter affecting impact allocation - the percentage of equipment lifespan during which it is actively used vs. idle. The authors set training and inference GPUs at 80% and 40% AUR respectively, noting sensitivity analysis shows significant impact below 20% utilization.

## Key Findings

### Quantitative Results for Stable Diffusion (FU2 - One Year)

| Impact Category | Value |
|-----------------|-------|
| Global Warming Potential | 360 tons CO2 equivalent |
| Abiotic Depletion Potential | Equivalent to 5,659 smartphones |
| Primary Energy | 2.48 GWh |

### Energy Consumption Measurements
- Training Stable Diffusion v1-4 and v1-5: 1.28 x 10^4 kWh and 3.39 x 10^4 kWh respectively
- Single inference: 1.38 x 10^-3 kWh

### Impact Distribution Analysis
1. **For ADP (metal scarcity)**: End-user terminals dominate (>90% of impact) due to manufacturing costs of devices with batteries and screens
2. **For GWP and PE**: Data center inference costs dominate, consistent with industry reports
3. **Networks and end-user terminals**: Non-negligible contribution, validating the need to include them in assessments

### Training Cost Allocation
- Training costs decrease from FU1 to FU2 perspective since FU2 includes costs for two model versions (v1-4 and v1-5)
- Legacy training scenario (including v1-0 through v1-3) shows training impact is often underestimated
- Warning: Neglecting training costs in Gen-AI assessment can miss significant environmental burden

### Sensitivity Analysis Findings
- Below 20% AUR, impact increases significantly for both training and inference
- Current industry AUR estimates range 12-18%, suggesting real-world impacts may be higher
- Migration to cleaner electricity grids and improved PUE can reduce but not eliminate impacts

## Relevance to Sustainable Computing

### Methodological Contributions
1. **Multi-criteria assessment**: Moves beyond "carbon tunnel vision" to include metal scarcity and full energy footprint
2. **Service-level scope**: Demonstrates importance of including all infrastructure (networks, terminals) not just AI-specific components
3. **Reproducible framework**: Provides equations and methodology adaptable to other Gen-AI services

### Policy Implications
- End-user terminals represent 30%+ of environmental impact - not a lever AI providers can control
- Transparency needed from cloud providers on GPU utilization rates and PUE values
- Potential for rebound effects: productivity gains from Gen-AI could increase overall ICT footprint

### Limitations Acknowledged
- Data center utilization rates not publicly available (estimated based on limited studies)
- Methodology requires LCI data that may not exist for newest hardware
- GPU mutualizing difficulties reduce effective utilization rates

### Future Research Directions
- Application to text-to-text models (LLMs like ChatGPT)
- Consequentialist assessment of transition from traditional to Gen-AI services
- Better characterization of actual industry utilization rates

## Citation

Berthelot, A., Caron, E., Jay, M., & Lefevre, L. (2024). Estimating the environmental impact of Generative-AI services using an LCA-based methodology. *Procedia CIRP*, 122, 707-712. https://doi.org/10.1016/j.procir.2024.01.098
