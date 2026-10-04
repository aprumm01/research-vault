---
source_file: Mapping value sensitive design onto AI for social good principles.pdf
type: paper
authors: ORIGINAL RESEARCH
community: Responsible AI and Ethics
tags: null
year: 2020
builds_on:
- '[[frameworks/Value Sensitive Design]]'
- '[[frameworks/Human-Centered Design]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Human-in-the-Loop Pedagogy]]'
- '[[concepts/Explainable AI]]'
key_claims:
- Traditional VSD is insufficient for AI because machine learning creates unique challenges
  of opacity and emergent properties where systems may develop unintended features
  or disembody embedded values originally designed into them
- 'AI requires a two-tiered value approach: first tier commits to social good through
  SDGs (beneficence), second tier avoids harm through AI4SG principles (non-maleficence)
  - both tiers required to prevent ethical whitewashing'
- VSD must extend to full life cycle of AI technologies due to self-learning capabilities
  that may produce unintended value consequences after deployment, requiring continuous
  monitoring and redesign
- 'Seven AI4SG principles function as normative bridge between abstract values and
  technical design requirements: falsifiability/incremental deployment, safeguards
  against manipulation, receiver-contextualized intervention, explanation transparency,
  privacy/consent, situational fairness, human-friendly semanticization'
- Context-specific stakeholder values remain essential even with universal principles,
  as they determine how abstract values translate into concrete design requirements
  in AI systems
methodology: '[[methods/Case Analysis]]'
sample_size: null
sample_type: null
context: Conceptual analysis with illustrative case of SARS-CoV-2 contact tracing
  app
study_type: theoretical
---

# Mapping value sensitive design onto AI for social good principles

## Summary
Value sensitive design (VSD) is an established method for integrating values into technical design It has been applied to different technologies and, more recently, to artificial intelligence (AI) We argue that AI poses a number of challenges specific to VSD that require a somewhat modified VSD approach.

## Key Concepts
- **Value Sensitive Design (VSD)** - Tripartite methodology of empirical, conceptual, and technical investigations for integrating ethical values into technology design
- **AI4SG (AI for Social Good) Principles** - Seven factors for ethical AI: falsifiability/incremental deployment, safeguards against manipulation, receiver-contextualized intervention, explanation transparency, privacy/consent, situational fairness, human-friendly semanticization
- **Machine Learning Opacity** - Self-learning AI systems may develop features neither foreseen nor intended by designers, creating emergent and potentially opaque biases
- **Emergent Value Disembodiment** - AI systems may adapt in ways that unintentionally 'disembody' values originally embedded in their design
- **Promoted vs. Respected Values** - Distinction between values promoted by design (contributing to social good via SDGs) and values respected by design (avoiding harm through ethical constraints)
- **Life Cycle VSD Extension** - Extending VSD beyond initial design to encompass monitoring and redesign throughout the technology's full operational life
- **Value Hierarchy Translation** - Framework for translating abstract values into norms and concrete design requirements through AI4SG principles
- **Supervised vs. Unsupervised Learning Bias** - Bias in AI can emerge from biased training data in supervised learning or from feedback mechanisms in reinforcement learning
- **Sustainable Development Goals (SDGs) Integration** - UN SDGs as approximation of collectively valuable societal ends for orienting AI toward beneficence
- **Contextual Value Analysis** - Importance of context-specific stakeholder values beyond universal ethical principles

## Theoretical Framework
**Modified VSD Framework for AI**: Extends traditional Value Sensitive Design with three key modifications: (1) integrating AI4SG principles as design norms, (2) distinguishing promoted vs. respected values to ensure beneficence not just non-maleficence, (3) extending VSD process to entire AI technology life cycle with continuous monitoring. Four iterative phases: context analysis, value identification, formulating design requirements, and prototyping with ongoing monitoring.

## Methods
Conceptual/theoretical paper proposing modified VSD methodology. Uses illustrative case analysis (SARS-CoV-2 contact tracing app Corona Datenspende) to demonstrate four-phase iterative process. Integrates EU High-Level Expert Group on AI values (autonomy, prevention of harm, fairness, explicability) with AI4SG principles and UN SDGs through value hierarchy framework.

## Main Arguments
- Traditional VSD insufficient for AI because machine learning creates unique challenges: opacity (humans may not understand how AI learns) and emergent properties (systems may develop unintended features or disembody embedded values)
- AI requires specific design principles beyond conventional VSD value lists, particularly the seven AI4SG principles that address AI-specific ethical concerns
- Two-tiered value approach necessary: first tier commits to social good through SDGs (beneficence), second tier avoids harm through AI4SG principles (non-maleficence) - both tiers required to prevent ethical whitewashing
- VSD must extend to full life cycle of AI technologies due to self-learning capabilities that may produce unintended value consequences after deployment
- Context-specific stakeholder values remain essential even with universal principles, as they determine how abstract values translate into concrete design requirements
- AI4SG principles function as normative bridge between abstract values and technical design requirements in the value hierarchy framework
- Incremental deployment with falsifiable testing critical for identifying emergent biases and unintended value consequences before full-scale implementation
- Without orientation toward positive social good (SDGs), AI systems may avoid obvious harms while still failing to contribute meaningfully to societal benefit

## Limitations & Critiques
- Illustrative case (Corona Datenspende) applied ex post facto rather than during actual design process, limiting validation of proposed framework's practical efficacy
- Value hierarchy framework shown through limited examples; unclear how to systematically handle value conflicts or trade-offs between multiple AI4SG principles
- Reliance on UN SDGs as proxy for "social good" may not adequately capture diverse cultural perspectives on desirable societal outcomes or address critiques of SDG framework itself
- Paper does not specify concrete metrics or methods for monitoring emergent value consequences during AI system operation beyond general principle of incremental deployment
- Limited guidance on how to determine when redesign is warranted versus acceptable adaptation, particularly for systems already deployed at scale
- Stakeholder identification and value elicitation methods not fully specified; unclear how to ensure representation of indirect stakeholders or those lacking power to articulate values
- Does not address potential conflicts between promoted values (SDGs) and respected values (AI4SG principles) or provide prioritization framework
- Assumes falsifiability and interpretability are always achievable; may not account for fundamental technical limitations in explaining some ML systems
- Context analysis phase lacks structured methodology; unclear how designers determine scope of relevant contexts or weight competing contextual factors
- Limited discussion of institutional or economic constraints that may prevent full life-cycle monitoring and redesign in practice

## Connections
- [[frameworks/Value Sensitive Design]] - Theoretical framework
- [[communities/Responsible AI and Ethics]] - Research community
