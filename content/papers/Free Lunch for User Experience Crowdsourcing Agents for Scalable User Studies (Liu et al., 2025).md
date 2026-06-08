---
source_file: "research_docs/synth users/Free Lunch for User Experience Crowdsourcing Agents for Scalable User Studies - Liu et al - 2025.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
  - synthetic-users
  - crowdsourcing
  - LLM-agents
  - UX-research
  - simulation
  - scalability
  - generative-agents
year: "2025"
authors: "Liu, Sabour, Wang, and Mihalcea"
venue: "arXiv:2505.22981v2 (submitted to ACM CHI)"
---

# Free Lunch for User Experience: Crowdsourcing Agents for Scalable User Studies (Liu et al., 2025)

## Summary
Liu, Sabour, Wang, and Mihalcea (University of Michigan / Tsinghua) introduce Crowdsourcing Simulated User Agents (CSUA), a method that recruits LLM-based agents from billion-scale persona profile assets to act as UX study participants at scale. Rather than crafting bespoke simulated users, CSUA treats agents as recruitable, screenable, and engageable entities — analogous to crowdsourcing platforms for human workers. A game prototyping study deployed 240 agents (selected from 2,900 candidates drawn from PersonaHub) and compared their insights against a 10-participant local university study and a 20-participant Prolific crowdsourced study. A clear scaling effect was found: coverage of human-derived findings rises smoothly as agent count increases, plateauing around 90%. The authors estimate that 12.8 simulated agents are as useful as one locally recruited participant, and 3.2 agents are as useful as one crowdsourced participant. Professional game designers rated the agentic study outputs as competitive on time efficiency and cost while maintaining solid fidelity and insight helpfulness. An open-source modular toolkit is released alongside the paper.

## Key Concepts
- **Crowdsourcing Simulated User Agents (CSUA)**: LLM agents instantiated from billion-scale profile pools (PersonaHub, census datasets, etc.) and recruited via a structured pipeline analogous to human crowdsourcing
- **Scaling effect**: coverage of human-derived findings increases smoothly with agent count, plateauing near 90% — individual imperfection is overcome by aggregation
- **Agent efficiency ratios**: 12.8 simulated agents equivalent to one locally recruited human; 3.2 simulated agents equivalent to one Prolific crowdsourced human
- **Four-stage pipeline**: onboarding (intake surveys + profile enrichment), screening (quota-based + curving for LLM bias), experiencing (interactive task with think-aloud), feedback (semi-structured interview)
- **PersonaHub**: 1 billion synthetic personas derived from web text, used as the base profile pool; 2,900 sampled and scored on Bartle player types and Big Five personality traits, then screened down to 240
- **Bartle player types**: Killers, Explorers, Socializers, Achievers — used as eligibility criteria during screening
- **Big Five curving**: GPT-4o systematically over-assigns high Openness, high Conscientiousness, and low Neuroticism; the paper applies normalization (curving around group means, e.g., mean Openness = 4.69/5) before final selection
- **48-code codebook**: inductive coding across all three study transcripts yielded a unified codebook of 48 codes; most frequent agent code = "Redundant response/repetition" (518 instances); least frequent = "Confused by low-fidelity setting" (2 instances)
- **Cost comparison**: agentic study $0.28/agent ($6.03/insight via API calls); Prolific crowdsourced $20.50/participant ($31.53/insight); local study $40.00/participant ($33.33/insight); LLM-as-generic-user $0.14 total ($0.028/insight but near-zero useful insight)
- **ICC for expert agreement**: ICC(2,1) = 0.817, 95% CI [0.640, 0.920] — strong agreement among three game developer experts rating the four study configurations
- **LLM-as-generic-user baseline**: a single GPT-4.1-mini agent with no persona; cheapest option but lowest fidelity and insight helpfulness, demonstrating that profile grounding (not just LLM capability) drives quality
- **NPC prototype**: 8 NPCs drawn from four game universes (Zelda, Stardew Valley, Elden Ring, Black Myth: Wukong), each designed to elicit a particular Bartle type; 18-action type space; AutoGen multi-agent framework

## Theoretical Framework
Builds on the crowdsourcing platforms literature (MTurk, Prolific) and reframes simulated users as a scalable participant pool rather than perfect individual models. Responds directly to critique literature by redefining "successful simulation" as pragmatic usefulness rather than individual accuracy. Draws on Park et al. generative agents (2023), Hamalainen et al. synthetic HCI data (2023), Argyle et al. silicon sampling (2023), and PersonaHub (Ge et al. 2024). Uses Bartle's (2004) player typology and Goldberg's (1992) Big Five as structured profiling axes. Expert evaluation uses NDCG for ranked insight helpfulness and Jaccard index for insight fidelity against human reference sets.

## Methods
- **Study context**: game NPC prototyping; participants interact with LLM-driven NPCs (text-based, no visuals) across 8 NPC interactions per participant
- **Agent construction**: 2,900 PersonaHub personas scored via GPT-4o on Bartle Test and Big Five; Big Five scores curved to correct for GPT's positive-trait bias; final 240 agents selected with balanced Bartle type distribution and diverse Big Five profiles
- **Human baselines**: 10 local university students (8M/2F, mean age 25.3, $40/hr compensation); 20 Prolific workers (7F/12M/1NB, mean age 31.7, $20.50/session)
- **LLM-as-generic-user baseline**: single GPT-4.1-mini agent with minimal role description
- **Interaction protocol**: think-aloud embedded before each action turn; 30-turn maximum or [D-END] action; semi-structured interview with 9 questions after all 8 NPC interactions
- **Analysis**: two authors independently coded all transcripts using inductive coding; codes consolidated across studies into 48-code unified codebook; subsampling (team sizes 1, 2, 4 ... 128, 240; 10 repetitions each) models coverage curve; expert evaluation by 3 game developers rating on time efficiency, cost efficiency, fidelity (behavior + insight Jaccard), and insight helpfulness (NDCG@10)

## Main Arguments
- Individual agent imperfection is irrelevant at scale: aggregated outputs from enough agents reliably converge on human-level coverage of UX insights, even if no single agent is faithful
- The crowdsourcing analogy is more productive than the replacement analogy: CSUA should be understood as a scalable, cheap participant pool, not a perfect user model
- CSUA is most valuable in early-stage prototyping where speed, breadth, and cost matter more than precise individual fidelity; traditional human studies remain better for later-stage, high-stakes evaluations
- The 90% coverage plateau represents a practical ceiling for simulation-based insight generation; the remaining ~10% — likely the most surprising or edge-case findings — still requires human participants
- Profile grounding is essential: the LLM-as-generic-user baseline demonstrates that raw LLM capability without structured persona profiles produces near-worthless insights despite identical underlying models
- Screening and curving are not optional: without correcting for GPT's systematic Big Five bias, the agent pool would be unrepresentatively skewed toward high Openness and high Agreeableness

## Limitations & Critiques
- Tested in a single game prototyping context; coverage ratios (12.8:1, 3.2:1) are domain-specific and unlikely to generalize without re-validation
- Coverage is measured against human-derived themes, presupposing those themes are the correct ground truth; truly novel simulation-only insights are not credited
- PersonaHub profiles are themselves synthetically generated, raising potential circularity: synthetic profiles generating synthetic participants being compared to human-derived codes
- Expert ratings of fidelity and usefulness are subjective and drawn from a small convenience sample (3 game developers)
- The paper was submitted with placeholder ACM fields indicating it is a preprint not yet formally published
- Scaling curves are estimated via subsampling of a fixed 240-agent pool rather than independent replications, which may understate variance at small team sizes

## Connections
- [[GenAI in UX and Design Practice]] - community anchor node
- [[Synthetic Users and AI Personas]] - direct topical overlap; CSUA is a scalable instantiation of synthetic user methods
- [[Evaluating LLMs in Generating Synthetic HCI Research Data (Hamalainen et al., 2023)]] - foundational prior work on synthetic HCI data generation; Liu et al. extend from case-by-case to crowdsourced scale
- [[UXAgent An LLM-Agent-Based Usability Testing Framework for Web Design (Lu et al., 2025)]] - concurrent LLM agent usability testing framework; different approach (web design focus) but same crowdsourcing-to-simulation logic
- [[Creating and Evaluating Personas Using Generative AI A Scoping Review (Amin et al., 2026)]] - circularity risk identified in CSUA's validation approach (master issue set partly LLM-derived)
