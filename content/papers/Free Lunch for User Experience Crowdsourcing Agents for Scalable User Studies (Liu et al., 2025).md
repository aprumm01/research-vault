---

source_file: "research_docs/P450.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
---

# Free Lunch for User Experience: Crowdsourcing Agents for Scalable User Studies (Liu et al., 2025)

## Summary
Liu, Sabour, Wang, and Mihalcea introduce Crowdsourcing Simulated User Agents (CSUA), a method that recruits LLM-based agents from billion-scale persona profile assets to act as UX study participants at scale. Rather than crafting bespoke simulated users, CSUA treats agents as recruitable, screenable, and engageable entities -- analogous to crowdsourcing platforms for human workers. A game prototyping study deployed 240 agents (selected from 2,900 candidates) and compared their insights against a 10-participant local user study and a 20-participant crowdsourced study. A clear scaling effect was found: coverage of human findings rises smoothly as agent count increases, plateauing around 90%. The authors estimate that 12.8 simulated agents are as useful as one local participant, and 3.2 agents are as useful as one crowdsourced worker. They release an open-source toolkit.

## Key Concepts
- Crowdsourcing Simulated User Agents (CSUA): LLM agents drawn from billion-scale profile pools
- Scaling effect: coverage of human findings increases with more agents, plateauing near 90%
- Agent efficiency: 12.8 simulated agents equivalent to one locally recruited participant
- Four-stage pipeline: onboarding, screening, experiencing, feedback
- Persona Hub (1 billion personas) as the profile asset base
- Open-source toolkit released for broader adoption

## Theoretical Framework
Builds on crowdsourcing platforms literature (MTurk, Prolific); positioned against the "locally designed simulated user" paradigm; draws on Park et al. generative agents, Hamalainen et al. synthetic data, and Argyle et al. silicon sampling; presents a practical utility framing rather than a validity-focused framing; expert designer evaluation for perceived fidelity and usefulness; affiliated with University of Michigan and Tsinghua.

## Methods
Game prototyping study: 240 simulated agents recruited from 2,900 candidate profiles (from Persona Hub); agents completed a structured UX evaluation pipeline (onboarding, screening, experiencing, feedback); compared against 10-participant local study and 20-participant Prolific crowdsourcing study; coverage of human-derived findings measured as agents scale from small to large numbers; professional designers (not study authors) rated simulated outputs on fidelity, cost, time, and usefulness.

## Main Arguments
- Individual agent imperfection is irrelevant at scale: while any single simulated agent may be unreliable, aggregated outputs from enough agents reliably converge on human-level coverage of UX insights
- The crowdsourcing analogy is more productive than the replacement analogy: CSUA should be understood as a scalable, cheap participant pool, not a perfect user model
- CSUA is most valuable in early-stage prototyping where speed, breadth, and cost matter more than precise individual fidelity
- The 90% coverage plateau suggests a practical ceiling for simulation-based insight generation, reinforcing the need for human studies to catch the final 10% -- which may include the most surprising and novel findings

## Limitations & Critiques
Only tested in a game prototyping context; coverage is measured against human-derived themes, which presupposes those themes are the ground truth worth covering; the Persona Hub profiles are themselves synthetic, raising circularity concerns; the 12.8-to-1 efficiency estimate is domain-specific and may not generalize; designer ratings of output quality are subjective.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Evaluating LLMs in Generating Synthetic HCI Research Data (Hamalainen et al., 2023)]] - foundational synthetic data study
