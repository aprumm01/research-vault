---
source_file: synth users/Generative AI Personas Considered Harmful - Amin et al -
  2025.pdf
type: paper
authors: Qatar Computing Research Institute, Hamad Bin Khalifa University, Doha, Qatar
community: AI and Future of Work
tags: null
year: 2025
builds_on:
- '[[frameworks/Human-Centered AI]]'
- '[[frameworks/Human-Centered Design]]'
- '[[methods/Persona Development]]'
critiques:
- '[[concepts/AI Augmentation]]'
- '[[concepts/Democratization of Design]]'
tensions_with:
- '[[concepts/Fauxtomation]]'
- '[[concepts/Ironies of Automation]]'
supports:
- '[[concepts/AI Hallucinations]]'
- '[[concepts/Human-in-the-Loop Pedagogy]]'
- '[[concepts/Hybrid Intelligence]]'
- '[[concepts/De-skilling]]'
- '[[concepts/Complacency Risk]]'
key_claims:
- All 20 GenAIP challenges were rated problematic (M>4.0), with highest concerns for
  hallucinations (M=5.94), over-sanitization (M=5.82), and lack of standardization
  (M=5.59)
- Twelve of 20 challenges are more problematic for GenAIPs than conventional personas,
  particularly bias amplification, validation difficulties, and accessibility without
  expertise
- 52% of GenAI personas provided fabricated answers to unanswerable questions, demonstrating
  the severity of hallucination challenges
- 86% of GenAI-generated addiction personas were US-based despite no geographical
  constraints in prompts, revealing systematic geographical bias
- Effective GenAIP implementation requires human-AI collaboration with substantial
  human oversight rather than automation, prioritizing user welfare over technical
  efficiency
methodology: '[[methods/Mixed Methods]]'
sample_size: 17
sample_type: persona subject matter experts
context: GenAI persona development and evaluation across HCI research
study_type: empirical
---

# Generative AI Personas Considered Harmful - Amin et al - 2025

## Summary
Inspired by Dijkstra's "Go To Statement Considered Harmful" (1968), this study systematically analyzes 20 challenges of Generative AI personas (GenAIPs) through Human-Centered AI principles. Using literature review and expert survey (n=17), the research finds GenAIPs transform rather than eliminate traditional persona challenges. All challenges were rated problematic (M>4.0), with highest concerns for hallucinations (M=5.94), over-sanitization (M=5.82), and lack of standardization (M=5.59). Twelve of 20 challenges are more problematic for GenAIPs than conventional personas, particularly bias amplification, validation difficulties, and accessibility without expertise. The study demonstrates effective GenAIP implementation requires human-AI collaboration rather than automation, prioritizing user welfare over technical efficiency.

## Key Concepts
- **Generative AI Personas (GenAIPs)**: User archetypes created using LLMs, Text-to-Image Models (TTIMs), and multimodal AI to represent target user groups, extending beyond data-driven personas through automated narrative and visual generation
- **Harmfulness Definition**: Potential negative impacts on HCI/UCD stakeholders including user group misrepresentation, bias propagation, erosion of authentic research practices, and misinformed design decisions
- **Persona Evolution**: Progression from Manual Personas (MPs) → Automated Personas (APs) → Data-Driven Personas (DDPs) → GenAIPs, with each transformation addressing limitations while introducing new challenges
- **HCAI Principles Framework**: Seven categories organizing GenAIP challenges - Transparency (2), Fairness (4), Reliability (3), Control (2), Privacy (2), Safety (1), User Experience (3) - revealing human-AI collaboration requirements
- **Three Stakeholder Groups**: (1) Persona developers (create personas from data collection to application), (2) Persona users (use personas for decision-making), (3) Target groups (represented by personas)

## Theoretical Framework
**Human-Centered AI (HCAI)** (Shneiderman, 2022)
Seven organizing principles applied to GenAIP challenges:
- **Transparency**: Explainability and auditability (TC01: lack of validation, TC02: hallucinations)
- **Fairness**: Bias and discrimination prevention (FC01: misrepresentation, FC02: persona-driven discrimination, FC03: over-sanitization, FC04: complications of average)
- **Reliability**: Consistency and dependability (RC01: superficiality, RC02: inconsistency dilemma, RC03: emergent toxicity)
- **Control**: Human oversight and automation balance (CC01: accessibility without capability, CC02: overreliance on GenAI)
- **Privacy**: Data protection and consent (PC01: privacy invasion, PC02: consent dilemma)
- **Safety**: Harm prevention (SC01: misleading deepfakes)
- **User Experience**: Practical utility (UC01: over-expectations, UC02: validating impact, UC03: desk drawer effect)

**Double Diamond Design Process** - Applied to persona development lifecycle:
- Discover → Define → Develop → Deliver phases where GenAIP challenges manifest differently across stakeholders

## Methods
**Three-Pronged Methodology**

1. **Snowball Literature Sampling**
   - Started from foundational persona literature (Cooper 1999, Chapman & Milham 2006, Ronkkö 2005, Salminen et al. 2021)
   - Forward/backward citation tracking through Google Scholar
   - Search terms combining challenges with GenAI terminology ("bias personas LLM", "hallucination AI-generated personas")
   - Prioritized HCI venues (CHI, DIS, UIST, IUI, CSCW) plus recent arXiv preprints
   - Systematically mapped 20 challenges from traditional personas to GenAIP manifestations

2. **Empirical Case Study Analysis** (4 published GenAIP studies)
   - Salminen et al. (2024): 450 addiction personas via GPT-4 (large-scale automated generation)
   - Sattele & Ortiz (2024): Water access personas for Iztapalapa (context-specific application)
   - Shin et al. (2024): Conversational persona interfaces (human-AI collaborative workflows)
   - Schuller et al. (2024): Comparative evaluation methods
   - Analyzed challenge manifestations across different stakeholders

3. **Expert Survey** (n=17 persona SMEs)
   - 20 challenges presented as statements rated on 7-point Likert scale (1=strongly disagree, 7=strongly agree)
   - Comparative evaluation: GenAIPs vs DDPs (more/equal/less problematic)
   - Quantitative validation of theoretical framework

## Main Arguments
1. **GenAIPs Transform Rather Than Eliminate Challenges**: Traditional persona problems persist but manifest differently—bias becomes algorithmic bias at scale, validation difficulties become opacity problems, inconsistency becomes AI hallucination with convincing fabrications

2. **Twelve Challenges Worsened by GenAI**: Over half (12/20) challenges are more problematic for GenAIPs than conventional personas, particularly bias amplification (FC02), validation opacity (TC01), hallucinations (TC02), and accessibility without expertise (CC01)

3. **Top Three Critical Challenges**:
   - Hallucinations (M=5.94): GenAI generates fluent, convincing but factually incorrect details (52% provided fabricated answers to unanswerable questions)
   - Over-sanitization (M=5.82): AI safety guardrails create unrealistically positive personas, missing genuine user struggles and pain points
   - Lack of standardization (M=5.59): No established protocols for GenAIP validation, evaluation, or quality assessment

4. **Human-AI Collaboration Required, Not Automation**: Effective GenAIP implementation demands substantial human oversight including domain expertise verification, bias detection protocols, and continuous validation—automation alone produces harmful outcomes

5. **HCI Methodology Becomes HCAI Challenge**: Integration of GenAI as active agent (not passive analytical tool) fundamentally transforms persona development, requiring examination through responsible AI frameworks addressing algorithmic transparency, fairness, and human control

6. **Stakeholder-Specific Harms**: Different challenges disproportionately affect different groups—developers face validation difficulties, users encounter over-reliance risks, target groups suffer misrepresentation and discrimination

## Limitations & Critiques
**Research Limitations**:
- Snowball sampling from traditional persona literature might miss GenAI-native challenges not rooted in previous methods
- Small expert sample (n=17) limits statistical power and generalizability of comparative assessments
- Primarily conceptual analysis focused on potential harms that may not yet be prominent in practice
- Illustrative scenarios were LLM-generated and intentionally exaggerated to demonstrate challenge types
- Limited longitudinal data on how GenAIP challenges evolve as technology matures

**GenAIP Practical Limitations Identified**:
- **Geographical Bias**: 86% of addiction personas US-based despite no geographical constraints in prompts (Salminen et al. 2024)
- **Systematic Misrepresentation**: Election simulation GenAIPs predicted Democratic victories in all states including Republican strongholds; 86% reflected urban, college-educated perspectives (Li et al. 2025)
- **Validation Gaps**: Major gaps in persona evaluation across 52 GenAIP research articles from 2022-2024 (Amin et al. 2025)
- **Superficiality**: Participants described GenAIPs as having "no soul" with "empty rhetoric" lacking authentic depth (Kaate et al. 2025)
- **Technical Inconsistency**: Same dataset produces drastically different personas with slight prompt modifications, creating design uncertainty
- **Over-Sanitization Example**: Learning platform GenAIPs claimed 100% course completion and found forums "instrumental" while real data showed frequent abandonment and forums perceived as "overwhelming"

**Methodological Challenges Documented**:
- Replication difficulty due to non-deterministic LLM outputs, temperature settings, and prompt sensitivity
- No standardized protocols for GenAIP creation, validation, or quality assessment
- Difficulty measuring intersectional bias, demographic parity, or representation rates in GenAI contexts
- Black-box nature prevents tracing persona attributes to source data or reasoning processes


## Related Papers
- [[papers/Reflecting on the Integration of Generative AI in Design Education]]
- [[papers/UI UX for Generative AI Taxonomy Trend and Challenge]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/Generative AI and the Automating of Academia]]
- [[papers/Experimenting with Generative AI Tools and their Implications Insights from High]]
## Connections
- [[methods/Survey]] - Research methodology: Expert survey validated theoretical framework
- [[frameworks/Human-Centered AI]] - HCAI principles organize and categorize GenAIP challenges
- [[methods/Persona Development]] - Evolution from manual to generative approaches with transformed challenges
- [[theories/Responsible AI]] - Ethical frameworks for algorithmic transparency, fairness, and human control
- [[papers/Data-Driven Personas]] - Foundation for understanding how GenAI transforms quantitative persona methods
- [[concepts/Algorithmic Bias]] - Generative bias and contextualization bias specific to GenAIPs
- [[tools/Large Language Models]] - LLMs as active agents in persona narrative generation
- [[tools/Text-to-Image Models]] - TTIMs for persona profile image generation with representation challenges
- [[communities/AI and Future of Work]] - Research community
- [[topics/AI collaboration rather]] - Key concept
- [[topics/Centered AI principles]] - Key concept
- [[topics/Contents lists available]] - Key concept
- [[topics/GenAIPs than conventional]] - Key concept
- [[topics/GenAIPs transform rather]] - Key concept