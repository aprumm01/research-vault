---
source_file: "synth users/UXAgent A System for Simulating Usability Testing - Lu et al - 2025.pdf"
type: paper
authors: "Yuxuan Lu, Bingsheng Yao, Hansu Gu, Jing Huang, Zheshen Wang, Yang Li, Jiri Gesi, Qi He, Toby Jia-Jun Li, Dakuo Wang"
community: "GenAI in UX and Design Practice"
tags:
  - synthetic-users
  - usability-testing
  - LLM-agents
  - persona-simulation
  - dual-process-theory
---

# UXAgent A System for Simulating Usability Testing - Lu et al - 2025

## Summary
Full system paper (extended from CHI EA framework paper) describing UXAgent open-source system for simulating usability testing with LLM agents. Addresses study design evaluation challenge: pilot studies are time-consuming/costly, empathy-based methods introduce bias, study design flaws surface only during execution with limited-resource populations. New dual-loop architecture inspired by Kahneman’s Dual Process Theory: Fast Loop (System 1: real-time interaction, perception, planning, action) and Slow Loop (System 2: Wonder module for "mind drifting," Reflect module for strategic insights). Universal Browser Connector parses real-world web pages dynamically. Result Viewer Interface enables reviewing action/reasoning traces, post-study surveys, and agent interviews. User study with 16 UX researchers showed participants could identify study design flaws, revise study protocols, and generate feature improvement ideas by analyzing agent data. Position: agents complement, not replace, humans—provide early feedback on study design before human-subject studies.

## Key Concepts
- [[concepts/Simulated User Agents]]
- [[concepts/LLM Agents]]
- [[concepts/Usability Testing]]
- [[concepts/Persona-Based Testing]]
- [[concepts/Dual Process Theory]]
- [[concepts/System 1 and System 2 Reasoning]]
- [[concepts/Universal Browser Connector]]
- [[concepts/Pilot Studies]]

## Theoretical Framework
Dual Process Theory (Kahneman): System 1 (fast, intuitive, emotional, automatic responses) vs. System 2 (slow, deliberate, logical analysis). Park et al.’s "believable" agents: autonomous human-like interactions. Memory Stream with importance, relevance, recency-based retrieval (weights tailored: Fast Loop prioritizes recency, Slow Loop prioritizes relevance). Human-AI collaboration: agents as simulated pilot study providing early feedback on study design and feature design.

## Methods
- User study with 16 UX researchers
- Scenario: design usability test for shopping website feature (product filter menu)
- Task: analyze 20 LLM agents’ data (action trace, reasoning trace, qualitative interview), identify study design flaws, propose feature improvements
- Evaluation: satisfaction with revised study designs, ability to identify issues
- System tested on WebArena, Google Flights, real-world shopping platforms

## Main Arguments
- Study design stage underaddressed: pilot studies costly/time-consuming, empathy methods introduce bias, flaws surface only during execution with limited-resource populations
- LLM agents should provide early feedback on study design itself (not just feature design) before human-subject studies
- Dual-loop architecture balances reasoning depth with real-time responsiveness: existing systems either too simple (single-prompt agents like Operator/Claude Computer-use) or too slow (complex reasoning architectures hindering real-time interaction)
- Universal Browser Connector enables dynamic real-world web interaction without predefined action spaces
- Position: "LLM agents are not meant to replace human participants in UX studies, but rather to help UX researchers to iteratively revise the study design, thus to be more responsible to human participants"
- UX researchers successfully revised study designs and generated feature improvements after analyzing agent data despite some criticism that agent actions "not what real users would do"

## Limitations & Critiques
- Some participants criticized agent behaviors as unrealistic compared to real users
- User study limited to shopping website domain (product filter menu scenario)
- 16 participants (single evaluation study); generalizability across domains/contexts unclear
- Persona diversity generation method (LLM prompting with demographic distributions) not empirically validated for representativeness
- No longitudinal evaluation: whether revised study designs actually perform better with real human participants not tested
- Computational cost and latency trade-offs of dual-loop architecture not quantified
- Ethical concerns about agent replacing humans acknowledged but not deeply explored
- Agents may still lack affective/emotional dimensions of real human behavior

## Related Papers
- [[papers/UXAgent An LLM-Agent-Based Usability Testing Framework - Lu et al - 2025]]
- [[papers/UXCascade Scalable Usability Testing with Simulated User Agents - Holter et al -]]
- [[papers/Evaluating LLMs in Generating Synthetic HCI Research Data]]

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
- [[concepts/Simulated User Agents]] - Core method
- [[concepts/Dual Process Theory]] - Theoretical foundation
- [[methods/Survey]] - System supports post-study surveys
- [[methods/Interview]] - System supports agent interviews
