---

source_file: "research_docs/P458.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2026"
authors: "Rieder et al"
---

# SimAB: Simulating A/B Tests with Persona-Conditioned AI Agents for Rapid Design Evaluation (Rieder et al., 2026)

## Summary
Rieder, Schneider, Truss, Tsaplin, Rublea, Dere, Chicharro Sanz, Reiss, and Dogan (ETH Zurich and Adobe Research) present SimAB, a system for simulating A/B tests using persona-conditioned AI agents. Given a control and challenger design, a conversion goal, and target audience description, SimAB generates diverse personas (e.g., Teacher, Marketer, Developer), simulates agent interactions with each design variant, and produces behavioral data for comparison. The system is designed for rapid early-stage design evaluation before real user testing is feasible. The paper demonstrates SimAB in practical design evaluation contexts and discusses the validity, limitations, and ethical implications of agent-simulated A/B testing for UX research workflows.

## Key Concepts
- Persona-conditioned AI agents: agents role-playing diverse user types to simulate A/B test participants
- Three inputs: control vs. challenger design, conversion goal, target audience description
- Persona Generator creates diverse representative personas from audience description
- Behavioral evidence generation: simulated agent interactions with design variants
- Pre-deployment design validation: rapid feedback before real user traffic
- Complementary tool: SimAB as early screening, not replacement for live A/B tests

## Theoretical Framework
A/B testing literature and UX experimentation methods; builds on Agent A/B (Lu et al.) and generative agent work (Park et al.); situated within a design research context at ETH Zurich and Adobe Research; examines tension between simulation efficiency and ecological validity; published as arXiv preprint (March 2026).

## Methods
System design with four components: audience description input, persona generator, agent simulation engine, results analysis; case demonstrations of SimAB applied to real design comparison scenarios; evaluation discussion around persona diversity, behavioral fidelity, and systematic biases; comparison of outputs across different persona types and design variants; qualitative analysis of agent-generated behavioral traces.

## Main Arguments
- Persona-conditioned A/B simulation can surface directional design insights faster and cheaper than traditional A/B testing during early prototype phases, before access to real user traffic
- Persona diversity is a key design consideration: SimAB's explicit persona generation from audience descriptions produces more intentional demographic coverage than ad hoc LLM prompting
- The fundamental limitation of SimAB and similar systems is that AI agents lack the authentic motivational and emotional states that drive real user behavior -- simulated purchase decisions are driven by token probabilities, not genuine desire
- SimAB is most trustworthy for evaluating information architecture, navigation clarity, and content comprehension, and least trustworthy for evaluating emotional resonance, trust, or motivation

## Limitations & Critiques
No systematic validation against real A/B test outcomes; the persona generator itself relies on LLM output, which may perpetuate demographic biases; conversion goals defined by users may not map cleanly to behavioral signals an LLM agent can reliably simulate; the system's ecological validity is not formally tested; overlap with Agent A/B in scope and motivation creates questions about differentiation.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[A/B Testing]] - `` [EXTRACTED]
- [[Agent AB Automated and Scalable AB Testing on Live Websites with LLM Agents (Lu et al., 2025)]] - parallel system for LLM-based A/B simulation
- [[PersonaCite VoC-Grounded Interviewable Agentic Synthetic AI Personas (Truss, 2026)]] - companion paper from same Adobe research team
