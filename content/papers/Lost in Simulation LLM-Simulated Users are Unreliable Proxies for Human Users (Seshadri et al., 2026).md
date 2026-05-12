---

source_file: "research_docs/P455.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2026"
---

# Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations (Seshadri et al., 2026)

## Summary
Seshadri, Cahyawijaya, Odumakinde, Singh, and Goldfarb-Tarrant conduct a user study with participants from the United States, India, Kenya, and Nigeria to test whether LLM-simulated users serve as reliable proxies for real humans in agentic benchmark evaluation (tau-Bench retail tasks). The study finds that user simulation lacks robustness (agent success rates vary up to 9 percentage points across different user LLMs), exhibits systematic miscalibration (underestimating performance on hard tasks, overestimating on moderate ones), and introduces fairness problems (AAVE speakers experience worse success rates and calibration errors than SAE speakers, with disparities compounding with age). Simulated users also introduce conversational artifacts (increased question-asking and politeness) not found in human users. The paper argues that current agentic evaluation practices risk misrepresenting AI agent capabilities across diverse user populations.

## Key Concepts
- Sim2Real gap in agentic evaluation: simulated users vs. real human users
- Robustness failure: 9 percentage point variance in success rates across different user LLMs
- Miscalibration: simulation underestimates hard task performance, overestimates moderate tasks
- Fairness gap: AAVE speakers consistently disadvantaged relative to SAE speakers; disparity compounds with age
- Conversational artifacts: simulated users are more polite, question-heavy, and cooperative than real users
- tau-Bench retail tasks as the benchmark testbed

## Theoretical Framework
Agentic benchmark literature (tau-Bench, Yao et al.); Expected Calibration Error adapted as an alignment metric; demographic fairness research in NLP (Sap et al., Sun et al.); positioned against prior work on user simulation for dialogue systems; user study conducted with Prolific (US, India, Kenya) and snowball sampling (Nigeria); published as arXiv preprint (January 2026).

## Methods
User study: participants across 4 countries (US, India, Kenya, Nigeria); US participants stratified by dialect (SAE vs. AAVE) and age (18-34, 35-54, 55+); 40 participants per demographic group; each completed 4 tasks (2 hard, 2 easy) from tau-Bench retail subset; agent model fixed at GPT-4o; success rates compared between human users and 5 different LLM user simulators; Expected Calibration Error (ECE) adapted to measure alignment between simulated and human success rates.

## Main Arguments
- LLM user simulators are not robust: results depend heavily on which LLM is used to simulate the user, making simulation-based benchmarks unreliable without human validation
- Simulated users create an "easy mode" for agents: they are more cooperative, less ambiguous, and less likely to express frustration than real users, inflating apparent agent performance
- Fairness is the most underexamined problem: simulation performs worst as a proxy for AAVE and Indian English speakers, meaning benchmarks built on LLM simulation may systematically misrepresent how well agents serve non-dominant language communities
- Higher LLM capability does not necessarily yield more faithful user simulation; GPT family shows correlation with human behavior, but Claude and Gemini families do not

## Limitations & Critiques
Only retail tasks from tau-Bench tested; non-US participants limited to 18-34 age group due to recruitment constraints; snowball sampling in Nigeria introduces selection bias; the binary success metric of tau-Bench may not capture nuanced interaction quality; the simulation LLMs tested reflect the 2025-2026 model landscape and findings may shift with newer releases.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Mind the Sim2Real Gap in User Simulation for Agentic Tasks (Zhou et al., 2026)]] - concurrent study with overlapping findings
- [[Responsible AI and Ethics]] - `` [EXTRACTED]
