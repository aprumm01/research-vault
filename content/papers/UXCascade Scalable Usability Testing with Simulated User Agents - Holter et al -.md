---
source_file: "synth users/UXCascade Scalable Usability Testing with Simulated User Agents - Holter et al - 2026.pdf"
type: paper
authors: "Steffen Holter, Eunyee Koh, Mustafa Doga Dogan, Gromit Yeuk-Yin Chan"
community: "GenAI in UX and Design Practice"
tags:
  - synthetic-users
  - usability-testing
  - LLM-agents
  - persona-simulation
  - iterative-design
---

# UXCascade Scalable Usability Testing with Simulated User Agents - Holter et al - 2026

## Summary
ETH Zurich and Adobe Research system for scalable usability testing using LLM-based simulated user agents. Addresses problem that simulated agents generate rich but unstructured outputs (action logs, think-aloud reasoning) difficult to act upon. Five-stage workflow: groups intentions, compares personas, distills issues, supports edit-in-loop iteration. User study with 8 UX professionals comparing UXCascade to human-generated feedback showed comparable performance. Formative study with 5 UX professionals identified key needs: frequent iteration speed, isolating/prioritizing problems, diverse user perspectives, goal-aligned feedback with reasoning traces.

## Key Concepts
- [[concepts/Simulated User Agents]]
- [[concepts/Persona-Based Testing]]
- [[concepts/Think-Aloud Protocol]]
- [[concepts/Iterative Design Workflows]]
- [[concepts/Issue Aggregation]]

## Theoretical Framework
LLM-based autonomous agents with explicit personas that navigate web pages, verbalize goals, produce step-by-step rationales. Multi-level analysis: patterns across persona traits/goals/outcomes → link agent reasoning to specific issues → support actionable improvements.

## Methods
- Formative study: 5 UX professionals (mean 12 years experience), semi-structured interviews, reflexive thematic analysis
- Evaluation study: 8 UX professionals, within-subjects design, custom website seeded with usability issues
- Measures: issue discovery rates, subjective workload, workflow fit

## Main Arguments
- Traditional usability testing too slow for AI-assisted rapid iteration cycles generating interface variations in seconds
- LLM agents can proxy human behavior with persona diversity but produce verbose unstructured outputs
- Five-stage workflow enables top-down exploration from patterns to concrete UX interventions
- Edit-in-loop iteration allows rapid re-evaluation after interface modifications
- System performs comparably to human-generated feedback, viable as complement to human-centered methods for early-stage evaluation

## Limitations & Critiques
- Fidelity questions remain: LLM agents may produce unrealistic behavior without careful prompting
- Participants cautioned against replacing human studies: "I don’t think the AI could ever replace a human study. But it could be one more data point"
- Limited to early Design stage; Discovery, Definition, late Delivery still require nuanced human feedback
- Evaluation on single custom website with seeded issues; generalizability unclear
- Emotional responses and affective dimensions underexplored
- Persona prompting may create superficial variety without affecting deeper reasoning (per Aher et al.)

## Related Papers
- [[papers/UXAgent An LLM-Agent-Based Usability Testing Framework]]
- [[papers/Evaluating LLMs in Generating Synthetic HCI Research Data]]
- [[papers/UX Designers pushing AI in the enterprise]]

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
- [[concepts/Simulated User Agents]] - Core method
- [[concepts/Synthetic Users]] - Related approach
