---

source_file: "research_docs/synth users/Persona-Based Simulation of Human Opinion at Population Scale - Li et al - 2026.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags: [synthetic-users, persona-simulation, LLMs, public-opinion, survey-methodology, computational-social-science]
year: "2026"
authors: "Li and Conrad"
doi: "arXiv:2603.27056v1"
---

# Persona-Based Simulation of Human Opinion at Population Scale (Li et al., 2026)

## Summary
Li and Conrad (University of Michigan, Institute for Social Research) introduce SPIRIT (Semi-structured Persona Inference and Reasoning for Individualized Trajectories), a two-stage framework for simulating individual-level human opinions rather than predicting from demographic correlations. The Painter module infers psychologically grounded, semi-structured personas from public social media posts (Reddit and/or Twitter/X), encoding Big Five personality traits, primal world beliefs, values/identities, life experiences, and opinions in a typed JSON schema, plus a third-person narrative summary. The Reasoner module then prompts an LLM conditioned on that persona to answer survey items, returning a response value, a confidence rating, and a brief rationale. Using the Ipsos KnowledgePanel — a nationally representative U.S. probability sample — the authors link 1,410 Twitter/X and 893 Reddit handles (n = 1,517 unique personas after raking) to panelists' self-reported survey responses across 81 questions. SPIRIT personas outperform demographic personas by 8–9 percentage points in exact-match accuracy across six models (Gemma-3-4B, LLaMA-3.1-8B, Gemma-3-27B, GPT-5-mini, GPT-5.2, and one intermediate), with gains plateauing at mid-size models because the task requires stable comprehension rather than advanced reasoning. SPIRIT personas also produce far broader, more heterogeneous response distributions (resembling real human variance) compared to the compressed, near-identical distributions produced by demographic prompting. The resulting Persona Bank is calibrated to U.S. Census/ACS benchmarks via iterative raking on six margins (gender, education, race/ethnicity, region, age group, 2024 presidential vote), producing weights with SD = 1.32, median = 0.63. Validated against real polls on four topics — abortion, immigration, the Epstein files, and U.S. military actions in Venezuela — the Persona Bank reproduces coherent within-cluster directional patterns. The authors also identify a "deliberation bias": simulated agents reason through causal chains rather than satisficing, causing them to almost never select low-engagement options like "not a threat" (0% vs. 39% in CBS polls for Venezuela Q14) and to massively overselect analytically derived answers like "would increase drugs" (48.6% vs. 7% in CBS for Venezuela Q19).

## Key Concepts
- **SPIRIT framework**: Semi-structured Persona Inference and Reasoning for Individualized Trajectories — a two-stage pipeline where a Painter infers persona from posts and a Reasoner conditions an LLM on that persona
- **Painter / Reasoner architecture**: Painter outputs a typed JSON persona (Big Five, primal world beliefs, values/identities, life experiences, opinions, interaction style) plus a third-person narrative; Reasoner uses both to answer survey questions with confidence ratings
- **Demographic vs. simulation paradigm**: demographic prompting is a predictive approach that collapses within-group variation; SPIRIT is a simulation approach that models the individual
- **Persona Bank**: collection of n = 1,517 SPIRIT personas derived from Ipsos KnowledgePanel participants' social media, calibrated via raking to function as a virtual probability-based respondent panel
- **Deliberation bias**: LLM agents systematically avoid low-effort satisficing responses and instead construct mechanistic causal chains, producing distributions that diverge from human survey marginals on factual/consequential items
- **Population-level calibration**: raking on six Census/ACS/election margins aligns persona-bank aggregates with U.S. adult population benchmarks; weights rescaled to mean = 1 (SD = 1.32, range 0.012–14.42)
- **8–9% accuracy advantage**: SPIRIT's absolute improvement over demographic persona prompting, consistent across all six tested models
- **Position-weighted composite score**: each user's 52-item response profile collapsed to a single scalar using question-sequence weights to assess distributional heterogeneity

## Theoretical Framework
Draws on survey methodology (probability sampling, design-based inference, raking/calibration) and computational social science. Argues that demographics underdetermine individual opinion because key psychological factors — Big Five personality (Mairesse et al., 2007), primal world beliefs (Clifton et al., 2019), narrative identity (McAdams, 2011), political identity (Jost & Amodio, 2012), and information environments (Schwartz et al., 2013) — are not captured by age, race, gender, education, income, and urbanicity. Situates the work against both the over-reliance on demographic prompting (Argyle et al., 2023; Horton, 2023) and the non-probability sampling problem that undermines population inference in most existing synthetic-respondent pipelines. Also engages satisficing theory (Krosnick, 1991) to explain why LLMs deviate from human survey behavior on cognitively demanding items.

## Methods
- **Panel**: Ipsos KnowledgePanel (probability-based U.S. adult panel); panelists consented to social media account linkage
- **Sample**: 1,410 Twitter/X handles and 893 Reddit handles; 452 had both; only valid, retrievable public accounts retained; final calibrated Persona Bank n = 1,517
- **Persona construction (Painter)**: all public posts concatenated chronologically; Painter LLM outputs a schema-validated JSON covering personality_big5, primal_world_beliefs, values_and_identities, life_experiences, opinions_and_beliefs, interaction_style, and meta — no demographic fields; up to 10 retry attempts for schema compliance
- **Inference evaluation (Reasoner)**: 52 held-out non-demographic survey items; exact-match accuracy computed per user, then averaged; position-weighted composite score captures distributional heterogeneity
- **Models tested**: Gemma-3-4B, LLaMA-3.1-8B, Gemma-3-27B, GPT-5-mini, GPT-5.2 plus one intermediate; smaller models failed schema compliance for nontrivial user fractions
- **Off-by-one rate**: GPT-5.2 and GPT-5-mini with SPIRIT personas achieved ~83% exact-match-or-one-category-off (off-by-one rates: 0.18 and 0.19 respectively)
- **Persona Bank external validation**: four polling topics — abortion (Pew), immigration (Pew), Epstein files (YouGov/Economist, late 2025), U.S. military actions in Venezuela (CBS News, 2025); time-sensitive topics used a three-step persona-guided web search protocol (Tavily) via Gemma-3-27b-it on a vLLM endpoint
- **Calibration**: iterative proportional fitting (raking) on PPGENDER, PPEDUC5, PPETHM, PPREG4, age group (18–29, 30–44, 45–64, 65+), and 2024 presidential vote; convergence threshold < 0.001, max 50 iterations
- **Compute**: 8x NVIDIA H100 (80GB) GPUs; inference-only (no fine-tuning)

## Main Arguments
1. Demographic-based persona prompting is a predictive, not simulation, paradigm: it collapses within-group variance and produces compressed response distributions concentrated around a small set of stereotyped answers
2. SPIRIT recovers individual responses 8–9 percentage points more accurately than demographic prompting because it captures psychological dimensions (personality, world beliefs, narrative identity) that demographics systematically miss
3. SPIRIT persona distributions better resemble actual human response heterogeneity; demographic personas yield median composite scores concentrated near 1.5 with systematically negative defaults
4. Persona Banks derived from probability samples can function as calibrated virtual respondent panels, enabling rapid-response public opinion measurement without new recruitment
5. Time-sensitive simulation is achievable via persona-conditioned web retrieval, but deliberation bias remains a systematic distortion: LLMs treat factual/consequential survey items as reasoning tasks rather than opinion expressions

## Key Empirical Findings
- **Accuracy**: 8–9% absolute advantage for SPIRIT over demographic personas, consistent across all six models; gains plateau at Gemma-3-27B / GPT-5-mini tier
- **Distribution**: demographic personas produce near-identical composite scores across users; SPIRIT personas produce distributions resembling human heterogeneity
- **Category-level accuracy** (GPT-5-mini across all 81 items): highest in Military (0.929), Voting (0.832), Health (0.764); lowest in Finances (0.245) and Technology (0.257)
- **Deliberation bias — Venezuela Q14** (threat level): agents selected "not a threat" 0% vs. 39% in CBS poll; concentrated on "minor threat" (79.9% vs. 48%)
- **Deliberation bias — Venezuela Q19** (drugs): agents selected "would increase drugs" 48.6% vs. 7% in CBS poll; "no change" only 11.8% vs. 56%
- **Sample demographic skews** (vs. U.S. population): both Twitter (N=1,031) and Reddit (N=774) samples ~61% male, >50% with Bachelor's or higher; Reddit 58.8% Liberal vs. Twitter 42.4%

## Limitations & Critiques
- Social media as persona source introduces platform-specific biases: both samples are male-dominated (~61%), highly educated (>50% Bachelor's), and politically left-skewed, especially Reddit (58.8% Liberal); raking corrects aggregates but cannot eliminate persona-level bias
- Consent and linkage requirements add additional eligibility filters beyond the KnowledgePanel's own selection, introducing potential self-selection confounds
- Deliberation bias is unresolved: LLMs consistently over-reason on factual/consequential items, and the paper does not demonstrate a fix — only diagnosing the pattern
- SPIRIT performs poorly on short-horizon behavioral items (e.g., beer consumption last week) because social media posts reflect long-run tendencies, not recent states
- Privacy constraints prevent public release of persona artifacts (JSON or narrative) and raw posts; only aggregated results and external survey instruments released
- Framework validated exclusively on U.S. English-language contexts and one panel provider; generalizability across languages, cultures, and panel designs is untested
- Smaller models produce nontrivial schema-compliance failures; results for these should be treated as lower-bound references only

## Connections
- [[GenAI in UX and Design Practice]] — situates persona simulation as a design-research tool for rapid, low-cost user opinion modeling
- [[Synthetic Users and AI Personas]] — core contribution to the synthetic-user literature; directly addresses the accuracy and representativeness problems identified in that space
- [[Simulating Human Opinions with Large Language Models (Kaiser et al., 2025)]] - parallel approach to LLM-based opinion simulation with a different grounding strategy; both confront the demographic-prompting ceiling
- [[Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents (Morocho et al., 2026)]] - critical evaluation of persona-conditioned survey simulation; read alongside as the skeptical counterpart
- [[LLM Generated Persona is a Promise with a Catch (Li et al., 2025)]] - identifies systematic bias in LLM persona generation that SPIRIT partially addresses through social media grounding
