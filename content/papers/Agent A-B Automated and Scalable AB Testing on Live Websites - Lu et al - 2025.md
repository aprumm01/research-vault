---
source_file: "synth users/Agent A-B Automated and Scalable AB Testing on Live Websites - Lu et al - 2025.pdf"
type: paper
authors: "with Interactive LLM Agents"
community: "GenAI in UX and Design Practice"
tags:
---

# Agent A-B Automated and Scalable AB Testing on Live Websites - Lu et al - 2025

## Summary
A/B testing is central to UI/UX design, yet our formative study with six industry practitioners revealed that it is slowed by scarce user traffic, long runtimes, and high operational costs To address these challenges, we introduce Agent A/B, an end-to-end system that deploys large language model (LLM) agents with structured personas to interact with live webpages and generate scalable behavioral evidence before launch In a case study on Amazon.

## Key Concepts
- LLM-agent-based A/B testing for UI/UX evaluation
- Persona-driven agent simulation in live web environments
- Automated behavioral analysis at scale
- DOM-based web interaction by AI agents
- Lightweight prototyping and pre-deployment validation
- Synthetic user behavior generation
- Between-subjects experimental design with agents
- Complement to human testing rather than replacement

## Theoretical Framework
- A/B testing and online controlled experimentation methodology
- User behavior simulation frameworks
- Persona-driven interaction modeling

## Methods
- Formative study with six industry practitioners (semi-structured interviews, grounded theory analysis)
- Case study on Amazon.com filter panel design
- Between-subjects simulation with 1,000 LLM agents (500 per condition)
- Comparison with parallel large-scale human A/B experiment
- Behavioral monitoring and automated analysis of agent interactions

## Main Arguments
- Traditional A/B testing faces three critical bottlenecks: limited lightweight piloting, scarce/contested user traffic, and slow feedback cycles
- LLM agents with structured personas can interact with live webpages to generate scalable behavioral evidence before human traffic allocation
- Agent A/B simulation can detect interface-sensitive behavioral differences and reproduce directional outcomes observed in human experiments
- Agent-based testing complements human testing by enabling earlier prototyping, faster iteration, and hypothesis-driven exploration
- System enables thousands of distributed sessions without manual intervention, addressing traffic scarcity and collaboration overhead
- Agent simulations can surface subgroup patterns and meaningful behavioral signals aligned with real user outcomes
- End-to-end system (agent specification, testing configuration, live interaction, monitoring, automated analysis) integrates into existing agent stacks

## Limitations & Critiques
- LLM-agent-based A/B testing is not a replacement for real user testing; should be viewed as complementary tool
- Agents may not fully capture complex human motivations, emotions, and contextual factors in decision-making
- Generalizability beyond e-commerce domains remains to be validated
- Potential for agent behaviors to diverge from actual human patterns in subtle or unexpected ways
- Limited exploration of how persona design quality affects simulation validity
- Reliance on existing agent technology limitations (e.g., error rates in DOM interpretation)
- Need for validation across diverse interface types and interaction patterns
- Ethical considerations around synthetic data use in product decision-making
- Costs of running large-scale LLM agent simulations versus human testing not fully characterized
- Long-term effects and behavioral dynamics not captured in single-session agent interactions

## Connections
- [[methods/Case Study]] - Research methodology
- [[communities/GenAI in UX and Design Practice]] - Research community
