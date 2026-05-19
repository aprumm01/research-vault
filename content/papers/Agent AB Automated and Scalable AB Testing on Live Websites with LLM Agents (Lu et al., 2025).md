---

source_file: "research_docs/P443.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Lu et al."
---

# Agent A/B: Automated and Scalable A/B Testing on Live Websites with LLM Agents (Lu et al., 2025)

## Summary
Lu et al. introduce Agent A/B, an end-to-end system that deploys LLM agents with structured personas to interact with live webpages and generate scalable behavioral evidence before product launch. A formative study with six industry practitioners revealed that traditional A/B testing is slowed by scarce user traffic, long runtimes, and high operational costs. Agent A/B addresses this by simulating A/B tests using 1,000 persona-conditioned LLM agents. In a case study on Amazon.com, the system compared filter panel designs and found results consistent with a parallel large-scale human experiment. The authors position Agent A/B as a complement to human testing: suitable for earlier prototyping, pre-deployment validation, and hypothesis-driven UX evaluation, while not replacing live human experiments for final decisions.

## Key Concepts
- LLM agent-based A/B testing at scale (1,000 simulated users)
- Structured persona conditioning for behavioral diversity
- Pre-deployment validation before human user traffic is available
- Behavioral evidence generation: purchase clicks, navigation patterns
- Subgroup analysis: detecting differential effects across demographic personas
- Complementary role of simulation alongside human A/B testing

## Theoretical Framework
Situated within HCI and UX research on agentic LLM evaluation; builds on prior work by Park et al. (generative agents) and WebVoyager; contextualizes simulation within A/B testing literature; uses behavioral evidence framework aligned with UX practitioner needs; published as an arXiv preprint (2026) and developed at Northeastern University in collaboration with Amazon.

## Methods
Formative interviews with six industry A/B testing practitioners to identify pain points; system design with three modules: persona generator, LLM agent interaction loop, and behavioral log analyzer; case study: 1,000 agents divided between two filter panel designs on Amazon.com, measuring simulated purchase rates and navigation; comparison against concurrent large-scale human A/B test on the same design variants; subgroup analysis by persona demographics.

## Main Arguments
- Current A/B testing bottlenecks (low traffic, slow runtimes, high cost) make pre-launch evaluation difficult; LLM agent simulation can fill this gap
- Agent A/B reproduced the directional outcome of a real human A/B test (reduced filter list generated more simulated purchases), validating simulation-to-human alignment at the directional level
- Simulated agents can detect interface-sensitive behavioral differences and surface subgroup patterns at fraction of the cost and time of human experiments
- Agent A/B should be framed as a complement rather than a replacement: useful for hypothesis generation and early screening, not final launch decisions

## Limitations & Critiques
Only one live case study on one platform (Amazon.com); directional alignment is validated but precise numerical alignment with human experiments is not established; persona conditioning may not capture the behavioral diversity of real user populations; the system cannot simulate emotional states, frustration, or accessibility needs; generalizability across design types and product domains is untested.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[UXAgent A System for Simulating Usability Testing of Web Design with LLM Agents (Lu et al., 2025)]] - related system by overlapping author team
