---
source_file: 2026/i609-sustainability/EstimatingtheenvironmentalimpactofGenerative-AIservices.pdf
type: paper
authors: Adrien Berthelot, Eddy Caron, Mathilde Jay, Laurent Lefevre
community: Sustainable Computing
tags:
- sustainability
- i609
- generative-AI
- LCA
- environmental-impact
- carbon-footprint
- energy-consumption
year: 2024
builds_on:
- '[[frameworks/Actor-Network Theory]]'
critiques: []
tensions_with: []
supports: []
key_claims:
- One year of Stable Diffusion service generates approximately 360 tons of CO2 equivalent
  emissions, metal resource depletion equivalent to manufacturing 5,659 smartphones,
  and 2.48 Gigawatt hours of primary energy consumption
- End-user terminals represent approximately 90% of Abiotic Depletion Potential (ADP)
  impact, while data-center inference represents approximately 75% of Global Warming
  Potential (GWP) impact
- Networks and end-user terminals are not negligible—prior studies focusing only on
  data centers miss significant portions of total environmental impact
- Below 20% Active Utilization Rate (AUR), environmental impacts increase significantly
  for training servers, with real data centers operating between 12-18% average utilization
- The majority of AI environmental studies are limited to measuring electricity consumption
  and carbon emissions, neglecting the conditions and resources required for deploying
  AI applications and missing a significant part of environmental impact
methodology: '[[methods/Case Study]]'
sample_size: null
sample_type: Stable Diffusion v1-4 and v1-5 models
context: Generative AI service (text-to-image) with full lifecycle infrastructure
  assessment
study_type: empirical
---

# Estimating the Environmental Impact of Generative-AI Services Using an LCA-Based Methodology

## Summary

Berthelot, Caron, Jay, and Lefevre authored this 2024 paper presented at the 31st CIRP Conference on Life Cycle Engineering (LCE 2024), representing collaboration between Univ. Lyon 1, OCTO Technology, CNRS, Inria, and Univ. Grenoble Alpes in France. The paper proposes and validates a comprehensive Life Cycle Assessment (LCA) methodology for evaluating the environmental impact of Generative AI (Gen-AI) services, considering not just training and inference but the full service infrastructure including end-user terminals, networks, web hosting, and data management. Using Stable Diffusion as a case study, the researchers found that one year of service operation generates approximately 360 tons of CO2 equivalent emissions, with significant impacts on metal resource depletion equivalent to manufacturing 5,659 smartphones. The paper's significance lies in providing a reproducible, multi-criteria assessment framework that goes beyond the "carbon tunnel vision" common in AI environmental studies, incorporating Abiotic Depletion Potential (minerals/metals), Global Warming Potential, and Primary Energy consumption across the entire service lifecycle.

## Research Overview

The paper addresses the gap that "the majority of studies are limited to measuring the electricity consumed by creating these AI, and possibly deducing their contribution to global warming via the carbon intensity of the electricity mix used" while "neglecting the conditions and resources required for deploying AI applications, such approaches miss out on a significant part of the environmental impact" (Berthelot et al., 2024, p. 707).

The methodology is based on **Life Cycle Assessment (LCA)**, "a methodology based on LCA and a reproducible experimental observation of training and inference electricity consumption" (Berthelot et al., 2024, p. 707). The system boundary encompasses the complete Gen-AI service: "end-user terminals, networking, web hosting, model inference, model training, and data management" (Berthelot et al., 2024, p. 708).

Key concepts include **Functional Units (FU)**, defined as standardized service outputs: "FU1, represents the average impact of a person visiting the website and submitting a prompt, generating 4 images" and "FU2, considers the cost of the service for one year, covering the activity periods of the v1-4 and v1-5 versions of the model" (Berthelot et al., 2024, p. 710).

Three impact categories were assessed: **Abiotic Depletion Potential (ADP)** "for minerals and metals... represents the decrease in available resources that have limited reserves"; **Global Warming Potential (GWP)** "evaluates the contribution to climate change"; and **Primary Energy (PE)** "expresses the total energy footprint" (Berthelot et al., 2024, p. 708).

## Theoretical Framework

The paper grounds its methodology in **Life Cycle Assessment** standards, specifically "following the IUT's recommendation for ICT services" (ITU I1410, cited in Berthelot et al., 2024, p. 710). LCA provides a comprehensive "cradle-to-grave" assessment framework considering manufacturing, use, and end-of-life phases.

The concept of **AI as a Service** frames the analysis: "The work focuses on AI as a service, which means that not only the specific costs of AI, i.e. training and inference phases, are integrated but also the infrastructure required to use it online, as a service, assuming that the AI is accessible through a website interface" (Berthelot et al., 2024, p. 708).

The paper critiques the prevalent **carbon tunnel vision** in AI environmental assessment: "this tendency towards carbon tunnel vision does not take into account impact categories, such as metal scarcity, which may be prevalent in ICT" (Berthelot et al., 2024, p. 707). This aligns with broader LCA literature emphasizing multi-criteria assessment.

**Allocation methods** are theoretically important: the paper employs time-based allocation for equipment impacts, where "the allocation is proportional to the total lifespan multiplied by its active utilization rate. It represents the fact that on-demand devices provided by data centers are not always used" (Berthelot et al., 2024, p. 709).

The concept of **Active Utilization Rate (AUR)** is central: "The AUR is the percentage of time in the equipment lifespan during which it is actively used, as opposed to when it is either idle or on standby" (Berthelot et al., 2024, p. 709).

## Central Arguments

The paper's central argument is that existing approaches to AI environmental assessment are inadequate because they focus narrowly on training energy and carbon emissions while ignoring the broader service infrastructure and multiple impact categories. The authors contend that "none of the previous work integrates the whole life cycle cost of the involved ICT equipment on a multi-criteria assessment. To fill these gaps, this work proposes an evaluation of AI as a service" (Berthelot et al., 2024, p. 708).

Supporting sub-claims include:

1. **End-user terminals dominate metal depletion impacts**: "The end-user terminals represent most of the impact in ADP, which was expected since such devices usually contain battery and screen which has a significant cost in manufacturing" (Berthelot et al., 2024, p. 710).

2. **Inference dominates energy and carbon impacts**: "The two other impact categories (GWP and PE) are dominated by the inference cost, which is coherent with reports from AI companies" (Berthelot et al., 2024, p. 710).

3. **Networks and terminals are non-negligible**: "Another interesting observation is that the impacts of networks and end-user terminals are not negligible, which validates the need to include them in such evaluations" (Berthelot et al., 2024, p. 710).

4. **Training impacts scale with model versions**: "The share of the training cost is decreasing from FU1 to FU2 since FU1 used the v1-5 model version and FU2 includes the training cost of two model versions (v1-4 and v1-5)" where earlier versions "required more than their training for their development" (Berthelot et al., 2024, p. 710).

5. **Utilization rates critically affect impacts**: "Below 20%, the impact is more significant for the average utilization rate of training servers... Unfortunately, the rare studies available on the subject are not that optimistic, pointing between 12% and 18% of the average utilization rate" (Berthelot et al., 2024, p. 711).

## Evidence

The paper provides quantitative environmental impact data from Stable Diffusion service assessment.

**Single inference (FU1)**: Abiotic Depletion Potential of 6.72e-08 kg Sb eq; Global Warming Potential of 7.84e-03 kg CO2 eq; Primary Energy of 2.02e-01 MJ (Berthelot et al., 2024, Table 2).

**One year of service (FU2)**: Abiotic Depletion Potential of 4.64e+00 kg Sb eq (equivalent to 5,659 smartphones); Global Warming Potential of 3.60e+05 kg CO2 eq (360 tons); Primary Energy of 8.93e+06 MJ (2.48 Gigawatt hours) (Berthelot et al., 2024, Table 2).

**Training energy measurements**: "we estimated that the v1-4 and v1-5 models consumed 1.28e+04 kWh and 3.39e+04 kWh to train, respectively. We measured that one inference consumed 1.38e-03 kWh" (Berthelot et al., 2024, p. 710).

**Impact distribution** (Figure 2): For FU2, end-user terminals represent approximately 90% of ADP impact; data-center inference represents approximately 75% of GWP impact; training represents a smaller but non-negligible share that varies by functional unit definition.

**Sensitivity analysis** findings: "Below 20%, the impact is more significant for the average utilization rate of training servers, which was expected since training requires 32 nodes with 8 GPUs" (Berthelot et al., 2024, p. 711).

**Limitations** acknowledged: "Improvements can be made to this use case to consolidate the results. This applies in particular to GPU footprints, web server sizing, and server utilization rates, for which better transparency from both the equipment manufacturing industries and the hosting providers offering these services can be expected" (Berthelot et al., 2024, p. 712).

## Conclusion

For recall six months from now, this paper establishes a comprehensive LCA methodology for assessing Gen-AI environmental impacts beyond the common "carbon tunnel vision." Key findings from Stable Diffusion case study: One year of service generates ~360 tons CO2 equivalent (GWP), metal depletion equivalent to 5,659 smartphones (ADP), and 2.48 GWh energy consumption (PE). Critical insight: end-user terminals dominate metal depletion impacts (~90% of ADP) while inference dominates carbon/energy impacts (~75% of GWP). Networks and end-user terminals are NOT negligible—prior studies focusing only on data centers miss significant portions of total impact. Training costs matter but allocation depends on functional unit definition and model versioning history. Sensitivity analysis reveals Active Utilization Rate (AUR) is critical—at utilization rates below 20% (where real data centers often operate), impacts increase significantly. The methodology's value is its reproducibility and extensibility to other Gen-AI services (authors plan to apply to text-to-text models). For sustainability policy, the paper suggests: (1) don't overlook manufacturing impacts of user devices that access AI services; (2) improving data center utilization rates has major potential for impact reduction; (3) multi-criteria assessment (ADP, GWP, PE) provides fuller picture than carbon-only metrics; (4) the transition to ubiquitous AI services could "severely increase the footprint of the ICT sector" due to rebound effects where productivity gains increase rather than decrease usage.

## APA Citation

Berthelot, A., Caron, E., Jay, M., & Lefevre, L. (2024). Estimating the environmental impact of Generative-AI services using an LCA-based methodology. *Procedia CIRP*, *122*, 707-712. https://doi.org/10.1016/j.procir.2024.01.098

## Discussion Questions

1. The paper finds end-user terminals dominate metal depletion impacts while inference dominates carbon impacts. How should this inform policy interventions—should we focus on device longevity or data center efficiency?

2. The methodology reveals that data center utilization rates below 20% significantly increase per-inference impacts. What market or regulatory mechanisms might improve utilization rates across the AI industry?

3. The paper explicitly critiques "carbon tunnel vision" in AI assessment. What other impact categories beyond ADP, GWP, and PE should be included in comprehensive Gen-AI environmental assessment (e.g., water consumption, land use)?

4. Given that one year of Stable Diffusion service generates impacts equivalent to manufacturing 5,659 smartphones, how should these AI-specific impacts be communicated to users to promote more sustainable usage patterns?


## Related Papers
- [[papers/UI UX for Generative AI Taxonomy Trend and Challenge]]
- [[papers/Generative AI and the Automating of Academia]]
- [[papers/Experimenting with Generative AI Tools and their Implications Insights from High]]
- [[papers/Generative AI Personas Considered Harmful - Amin et al - 2025]]
- [[papers/Integrating user experience in user interface design education a problem-based l]]
## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Life Cycle Assessment]]
- [[topics/AI Ethics]]
- [[topics/Carbon Footprint]]
- [[topics/Data Center Sustainability]]
