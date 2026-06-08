---
source_file: "research_docs/synth users/LLM Agent Meets Agentic AI Can LLM Agents Simulate Customers - Sun et al - 2025.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Sun et al"
---

# LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-Based Shopping Assistants? (Sun et al., 2025)

## Summary
Sun et al. recruited 40 Prolific participants to conduct real shopping sessions with Amazon Rufus, then created a "digital twin" LLM agent for each participant -- grounded in that participant's own survey data -- and had the agents repeat the same tasks. Pairwise comparison of human and agent traces shows that digital twins matched humans on high-level outcomes (F1 = 0.9 on buy/no-buy decision, similar turn counts, cosine similarity of first messages = 0.49) but diverged sharply at the trajectory level (NED = 0.89, only 1.3% exact product-level agreement). Agents favored breadth-first exploration, expressed almost no frustration, and produced uniformly positive UX evaluations, while human accounts included frustration, ambivalence, and concerns about personalization and manipulation. The study is the first to quantify human-agent alignment in real-world, multi-turn agentic AI interaction, and its central finding is that high binary accuracy masks deep behavioral trajectory divergence.

## Key Concepts
- Digital twin agents: one-to-one LLM agents instantiated from a specific participant's persona data (demographics, Big Five, MBTI, Consumer Styles Inventory, open-ended self-descriptions)
- Binary vs. trajectory alignment: F1 = 0.9 on buy/no-buy masks NED = 0.89 trajectory divergence -- the headline tension of the paper
- Normalized Edit Distance (NED): Levenshtein distance over action sequences, used to quantify how different human and agent interaction paths are (NED = 0.89, SIM = 0.11)
- Breadth-first exploration: agents clicked significantly more recommended items (M = 1.9 vs. humans M = 1.2, p < 0.01) and asked more follow-up questions (M = 0.78 vs. M = 0.13, p < 0.01)
- Positivity bias in agent evaluation: agents rarely reported frustration or limitations; human accounts were more critical and emotionally varied
- UXAgent framework: the simulation infrastructure used -- a persona-driven LLM agent architecture for realistic task execution and reflective UX reasoning
- Claude 3.7 Sonnet at temperature = 0.2: the model used for all agent action prediction, selected for reasoning consistency

## Theoretical Framework
Positioned at the intersection of Agent-as-a-Judge evaluation (LLM-as-a-Judge, AgentBench, Mind2Web2) and digital twin / generative agent simulation (Park et al.'s 1,000-person simulation, generative agents). Prior work in agent-based UX evaluation (UXAgent, AgentA/B, SimUser) is extended here by grounding the simulation in empirical, ground-truth human data rather than synthetic personas. The study responds to the "Agent-as-a-Judge" paradigm's gap: existing approaches assess final outcomes or single-turn responses; this study is the first to compare agents and humans across full multi-turn interaction trajectories in a real commercial system. Submitted to CHI (arXiv preprint arXiv:2509.21501, September 2025).

## Methods
Two-stage design. Stage 1 (human study): N = 40 participants (of 50 recruited) from Prolific, diverse U.S. sample across age, gender, race, education, and income; compensated $15.50/hr; IRB approved. Participants completed a 15-minute persona survey (demographics, shopping habits, Big Five Inventory, self-reported MBTI, adapted 8-item Consumer Styles Inventory, open-ended self-descriptions and daily routine), then installed a custom Chrome extension that logged all Rufus interactions in real time to Amazon S3. Each participant completed two shopping tasks (one utilitarian, one hedonic) using Amazon Rufus: monitors, ergonomic chairs, summer wedding outfits, and hiking jackets -- with specific budget constraints per task. Average session duration: 375.9 seconds. Post-task UX survey measured satisfaction, trust, usability, helpfulness, cognitive load, and open-ended feedback. Stage 2 (agent simulation): each participant's persona data was translated into a natural-language prompt and used to initialize a Claude 3.7 Sonnet agent (temperature = 0.2) via the UXAgent framework, which operates on real web pages through a Universal Web Connector that converts raw HTML into semantic representations. Agents completed the same tasks and answered the same post-task survey. Analysis compared 80 human sessions vs. 80 agent sessions using Welch's t-tests, cosine similarity of first messages (sentence embeddings), and Levenshtein distance over action trajectory sequences.

## Main Arguments
- High binary alignment does not mean behavioral fidelity: F1 = 0.9 on the buy/no-buy decision looks strong, but only 1.3% of agent-human pairs chose the same product, and trajectory NED = 0.89 indicates agents follow systematically different paths
- Agents open conversations like humans but diverge quickly: cosine similarity of opening messages = 0.49 (some structural alignment); thereafter, agents explored more broadly rather than narrowing toward decision-relevant constraints as humans do
- Agent evaluations are functional but lack affective nuance: agents rated Rufus similarly to humans on query matching, coherence, helpfulness, and trust (all p > 0.1), but humans reported significantly higher satisfaction with their chosen product (p < 0.001) and stronger preference for Rufus over traditional search (p < 0.001) -- likely because agents did not experience frustration or indecision
- Persona-grounded simulation is feasible but incomplete: grounding agents in real survey data (Big Five, MBTI, CSI, open-ended descriptions) produces agents that mirror structural interaction metrics but not the heuristics, bounded rationality, and affective responses that drive human decision-making
- Hybrid evaluation is the appropriate response: agents are well-suited for scalable early-stage evaluation of task success and coherence; human evaluation remains indispensable for capturing affective, critical, and preference-sensitive dimensions

## Limitations & Critiques
Single domain (online shopping) and single platform (Amazon Rufus) -- findings may not transfer to other agentic AI contexts (productivity, healthcare, education). Only four task types, all common consumer goods; broader or more ambiguous tasks were not tested. All agents used one implementation (UXAgent with Claude 3.7 Sonnet); different LLMs or agent architectures may yield different alignment profiles. No behavioral measure of frustration was coded from agent traces -- the positivity bias observation is qualitative, not quantified with the precision reported in concurrent work (e.g., Seshadri et al., 2026). The MBTI was self-reported and optional, introducing variability in persona richness. The paper does not analyze whether specific persona dimensions (e.g., Big Five openness) predicted better or worse alignment.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Mind the Sim2Real Gap in User Simulation for Agentic Tasks (Zhou et al., 2026)]] - concurrent finding on behavioral divergence
- [[Lost in Simulation LLM-Simulated Users are Unreliable Proxies for Human Users (Seshadri et al., 2026)]] - concurrent finding on positivity bias and structural miscalibration