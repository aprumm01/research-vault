---
source_file: synth users/SimAB Simulating A-B Tests with Persona-Conditioned AI Agents
  - Rieder et al - 2026.pdf
type: paper
authors: for Rapid Design Evaluation
community: Responsible AI and Ethics
tags: null
year: 2026
builds_on:
- '[[concepts/Synthetic Users]]'
- '[[frameworks/Human-Centered Design]]'
- '[[concepts/Interactive Virtual Personas]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Synthetic Users]]'
- '[[concepts/Interactive Virtual Personas]]'
- '[[concepts/AI Augmentation]]'
key_claims:
- SimAB achieves 67% overall accuracy against 47 historical A/B tests, increasing
  to 83% for high-confidence cases
- Traditional A/B testing requires months to reach statistical significance; SimAB
  reduces feedback latency from months to minutes through persona-conditioned AI agents
- 'Four critical pain points in traditional A/B testing: low-traffic pages, high volume
  of design variants, low-value changes, and instrumentation/sampling constraints'
- LLM-based synthetic users have systematic failures in capturing nuanced human preferences
  and reflect perspectives of specific demographic groups rather than universal behaviors
- SimAB enables rapid screening and validation during ideation when design changes
  are still inexpensive, particularly for low-traffic scenarios and privacy-sensitive
  contexts
methodology: '[[methods/Mixed Methods]]'
sample_size: 61
sample_type: 14 practitioners from four enterprise organizations (formative study)
  and 47 historical A/B tests (validation)
context: Enterprise design evaluation across multiple organizations with historical
  A/B test data
study_type: empirical
---

# SimAB Simulating A-B Tests with Persona-Conditioned AI Agents - Rieder et al - 2026

## Summary
SimAB: Simulating A/B Tests with Persona-Conditioned AI Agents for Rapid Design Evaluation Tim Rieder∗† ETH Zurich Zurich, Switzerland timrieder@ethz ch Marian Schneider∗† ETH Zurich Zurich, Switzerland smarian@ethz HC] 1 Mar 2026 Sinem Dere Mario Truss Vitaly Tsaplin.

## Key Concepts
- Synthetic A/B testing using persona-conditioned AI agents
- Rapid design evaluation without real user traffic
- Persona-driven agents that interact with design variants
- Counterbalancing and neutral naming to mitigate LLM biases
- Privacy-preserving simulation approach

## Theoretical Framework
Generative agents with persona conditioning; User modeling through LLM-based synthetic audiences; Multi-agent systems for design evaluation

## Methods
Formative study with 14 practitioners across four enterprise organizations (participatory design engagements); Empirical validation using 47 historical A/B tests with known outcomes; SimAB system: (1) Input Processing (design variants, conversion goals, target audience, context documents), (2) Persona Generation (diverse synthetic users), (3) Persona Simulation (agent interactions with designs), (4) Summary Generation (aggregated verdicts and rationales)

## Main Arguments
- Traditional A/B testing has significant bottleneck requiring large user traffic and months to reach statistical significance
- Four pain points: low-traffic pages, high volume of design variants, low-value changes, instrumentation/sampling constraints
- SimAB reduces feedback latency from months to minutes through persona-conditioned AI agents
- System achieves 67% overall accuracy against historical tests, increasing to 83% for high-confidence cases
- Enables fast evaluation cycles and rapid screening of designs difficult to assess with traditional A/B tests
- Allows validation during ideation and early iteration when changes are still inexpensive
- Supports testing in privacy-sensitive contexts and low-traffic scenarios

## Limitations & Critiques
- Significant concerns about validity of synthetic data for understanding human preferences
- LLM outputs reflect perspectives of specific demographic groups (not universal)
- Systematic failures in capturing nuanced preferences identified in prior work
- Behavioral gaps between humans and AI agents
- Limitations in GenAI-based usability testing documented in literature
- Challenges in validating simulated behaviors
- Validity and reproducibility concerns about LLM use in HCI research
- Risk that LLMs replacing human participants can harmfully misportray and flatten identity groups
- Performance not perfect - 67% accuracy overall means 33% failure rate
- Systematic biases in LLMs (naming bias, positional bias) require mitigation strategies

## Connections
- [[communities/Responsible AI and Ethics]] - Research community
