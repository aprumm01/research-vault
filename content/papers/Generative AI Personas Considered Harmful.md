---
source_file: "Generative AI Personas Considered Harmful - Amin et al - 2025.pdf"
type: paper
authors: "Danial Amin, Joni Salminen, Bernard J. Jansen, Joongi Shin, Dae Hyun Kim"
year: 2025
---
# Generative AI Personas Considered Harmful? Putting Forth Twenty Challenges of Algorithmic User Representation in Human-Computer Interaction

## Summary
This comprehensive analysis examines the potential harms of using Generative AI (GenAI) to create user personas for design and user research. Inspired by Dijkstra's classic essay on harmful programming constructs, the authors identify 20 challenges specific to GenAI-generated personas (GenAIPs), organized according to Shneiderman's Human-Centered AI (HCAI) principles across seven themes: transparency, fairness, reliability, control, privacy, safety, and user experience. Through literature review and expert survey (n=17), they find that GenAIPs transform rather than eliminate traditional persona challenges, with 12 of 20 challenges rated as more problematic for GenAIPs than conventional data-driven personas.

## Key Concepts
- **GenAIPs (Generative AI Personas)**: User personas created using LLMs, text-to-image models, and other generative AI technologies
- **Data-Driven Personas (DDPs)**: Personas created using statistical/algorithmic methods on actual user data
- **Manual Personas (MPs)**: Traditionally crafted personas based on qualitative research
- **Human-Centered AI (HCAI)**: Shneiderman's framework emphasizing transparency, fairness, and human control
- **Hallucinations**: AI-generated content that is factually incorrect or fabricated
- **Over-sanitization**: AI tendency to generate unrealistically positive portrayals

## Theoretical Framework
The authors apply Shneiderman's HCAI principles to systematically categorize GenAIP challenges, positioning persona development as a Human-Centered AI concern requiring ethical oversight. They draw on Dijkstra's "considered harmful" rhetorical framework to critically examine seemingly beneficial technological practices.

## Methods
- Snowball literature sampling from foundational persona research
- Systematic mapping of 20 challenges with evidence from prior literature
- Empirical case study analysis of four recent GenAIP implementations
- Expert survey with 17 persona researchers/practitioners
- 7-point Likert scale assessment of challenge severity
- Comparative analysis of GenAIPs vs. traditional DDPs

## Main Arguments
**Transparency Challenges (TC):**
- TC01: Lack of validation - cannot verify persona accuracy
- TC02: Hallucinations - fabricated details appear credible

**Fairness Challenges (FC):**
- FC01: Misrepresentation of minority user groups
- FC02: Persona-driven discrimination from training data biases
- FC03: Over-sanitization - unrealistically positive portrayals
- FC04: Complications of average - obscuring edge cases

**Reliability Challenges (RC):**
- RC01: Superficiality - polished but shallow personas
- RC02: Inconsistency - different outputs from same data
- RC03: Limited generalizability across contexts
- RC04: Aggregation artifacts - meaningless statistical patterns

**Control Challenges (CC):**
- CC01: Persona quality risk without human expertise
- CC02: Manual resource intensiveness persists
- CC03: Lack of standardization
- CC04: Over-reliance on GenAI

**Privacy Challenges (PC):**
- PC01: Reliance on third-party services

**Safety Challenges (SC):**
- SC01: Adversarial users can manipulate outputs
- SC02: Computational resource intensity (environmental impact)

**User Experience Challenges (UC):**
- UC01: Over-expectations about AI capabilities
- UC02: Validating impact is difficult
- UC03: Desk drawer effect - personas created but unused

## Limitations & Critiques
- Expert survey sample limited to 17 participants
- Challenges identified through literature may not capture all real-world issues
- Rapid evolution of GenAI may date findings quickly
- Framework assumes human-AI collaboration is desirable; may understate cases where GenAIPs should not be used at all
- Limited attention to organizational/structural factors influencing GenAIP adoption
- Does not provide empirical validation that proposed guidelines mitigate harms
