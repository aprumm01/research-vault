---
source_file: Generative AI Personas Considered Harmful - Amin et al - 2025.pdf
type: paper
authors: Danial Amin, Joni Salminen, Bernard J. Jansen, Joongi Shin, Dae Hyun Kim
year: 2024
builds_on:
- '[[frameworks/Human-Centered AI]]'
- '[[frameworks/Value Sensitive Design]]'
- '[[methods/Persona Development]]'
critiques:
- '[[concepts/Democratization of Design]]'
tensions_with:
- '[[concepts/AI Augmentation]]'
- '[[concepts/Cognitive Offloading]]'
supports:
- '[[concepts/AI Hallucinations]]'
- '[[concepts/De-skilling]]'
- '[[concepts/Fauxtomation]]'
- '[[concepts/Ironies of Automation]]'
- '[[concepts/Complacency Risk]]'
key_claims:
- All 20 identified GenAIP challenges were rated as problematic by experts (M > 4.0
  on 7-point scale), with hallucinations, over-sanitization, and lack of standardization
  rated as highest concerns
- 12 of 20 challenges are considered more problematic for GenAIPs than traditional
  data-driven personas, particularly bias amplification, validation challenges, and
  accessibility without expertise
- Target groups (users represented by personas) bear the most severe consequences
  when GenAIP systems fail, though persona developers face 17 of 20 operational challenges
  directly
- GenAIPs transform rather than eliminate traditional persona challenges, shifting
  persona development from human-interpretable processes to AI-driven generation requiring
  ethical oversight and human-AI collaboration rather than full automation
- The 'desk drawer effect' risk increases with GenAIPs as ease of creation may lead
  to personas being developed but never used in actual design decisions
methodology: '[[methods/Mixed Methods]]'
sample_size: 17
sample_type: persona researchers and subject matter experts
context: Analysis of four published GenAIP studies combined with expert survey on
  persona development challenges
study_type: mixed
---

# Generative AI Personas Considered Harmful? Twenty Challenges of Algorithmic User Representation in Human-Computer Interaction

## Summary
This paper systematically examines twenty challenges associated with Generative AI Personas (GenAIPs) using Human-Centered AI (HCAI) principles. Inspired by Dijkstra's classic essay on harmful programming constructs, the authors analyze how GenAIPs transform rather than eliminate traditional persona challenges, with the highest concerns being hallucinations, over-sanitization, and lack of standardization.

Through literature review and an expert survey of 17 persona researchers, the study finds that all 20 identified challenges were rated as problematic for GenAIPs (M > 4.0 on a 7-point scale). Critically, 12 of 20 challenges are considered more problematic for GenAIPs than traditional personas, particularly bias amplification, validation challenges, and accessibility without expertise. The authors categorize challenges across seven HCAI themes: transparency, fairness, reliability, control, privacy, safety, and user experience.

The paper provides empirical assessment through analysis of four published GenAIP studies (addiction-related personas, water access issues, survey-based personas, and data-driven approaches), demonstrating how challenges manifest across different contexts. The stakeholder impact analysis reveals that while persona developers face 17 of 20 operational challenges, target groups bear the most severe consequences when GenAIP systems fail.

## Key Concepts
- **Generative AI Personas (GenAIPs)**: User representations created using GenAI technologies like LLMs, TTIMs, and multi-modal models for persona development
- **Human-Centered AI (HCAI)**: Framework organizing GenAIP challenges around transparency, fairness, reliability, control, privacy, safety, and user experience
- **Hallucinations**: GenAIs generating convincing but factually incorrect persona details
- **Over-sanitization**: GenAI tendency to omit negative characteristics, creating unrealistically positive personas
- **Desk Drawer Effect**: Personas developed but never used in actual design decisions

## Theoretical Framework
The paper applies Shneiderman's HCAI principles to categorize and analyze GenAIP challenges. It draws on traditional persona literature (Cooper, Chapman and Milham) while extending analysis to AI-specific concerns like algorithmic bias, opacity, and accountability.

## Methods
Three-pronged approach: (1) snowball literature sampling identifying 20 challenges from foundational persona literature mapped to GenAIP contexts; (2) empirical case study analysis of four published GenAIP studies examining how challenges manifest; (3) expert survey with 17 SMEs rating challenge severity and comparing GenAIPs to traditional data-driven personas (DDPs).

## Main Arguments
- GenAIPs shift persona development from human-interpretable processes to AI-driven generation requiring ethical oversight
- Challenges are categorized thematically: transparency (understanding black-box AI), fairness (addressing algorithmic bias), reliability (managing hallucinations), control (balancing automation with oversight), privacy (protecting data), safety (preventing harmful personas), and user experience (ensuring practical utility)
- The shift to HCAI territory demands that challenges be connected to established AI ethics principles
- Target groups (users represented by personas) bear the most severe consequences when GenAIPs fail, though they face fewer direct challenges
- Effective GenAIP implementation requires human-AI collaboration rather than automation replacing human judgment
- HCAI-grounded guidelines are necessary for responsible GenAIP development including bias detection protocols and human-AI collaboration workflows

## Limitations & Critiques
- Primarily conceptual; challenges are mapped from literature rather than discovered through primary empirical investigation
- Expert survey sample (n=17) is relatively small
- The rapidly evolving nature of GenAI technologies means specific challenges may shift
- The framework focuses on identifying challenges rather than validated solutions
- Case studies are secondary analysis of published work rather than original data collection
- Does not address all potential GenAI applications (e.g., video-based personas)
