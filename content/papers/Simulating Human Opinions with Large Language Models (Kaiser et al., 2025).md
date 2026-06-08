---
source_file: "research_docs/synth users/Simulating Human Opinions with Large Language Models - Kaiser et al - 2025.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
  - synthetic-users
  - survey-simulation
  - digital-twins
  - LLMs
  - consumer-research
  - opinion-modeling
year: "2025"
authors: "Kaiser et al"
venue: "UMAP Adjunct '25 — Adjunct Proceedings of the 33rd ACM Conference on User Modeling, Adaptation and Personalization"
doi: "https://doi.org/10.1145/3708319.3733685"
---

# Simulating Human Opinions with Large Language Models: Opportunities and Challenges for Personalized Survey Data Modeling (Kaiser et al., 2025)

## Summary
Carolin Kaiser, Jakob Kaiser, Vladimir Manewitsch, Lea Rau, and Rene Schallner (Nuremberg Institute for Market Decisions; LMU Munich) develop and evaluate ASPIRE (Automated Synthetic Persona Interview and Response Engine), a tool that pairs each human survey participant with a demographic-matched "digital twin" and generates synthetic responses via LLM. Using a representative U.S. sample (n=461) on consumer preferences for eight soft drink brands (four well-known, four lesser-known), synthetic data achieved above-chance accuracy (~78-79% agreement for both binary and Likert items) and correctly reproduced aggregate trends distinguishing popular from lesser-known brands. However, LLM-generated responses systematically overestimated positive attitudes and showed substantially reduced variance compared to real human data. No sociodemographic bias in simulation accuracy was detected across age, gender, ethnicity, education, profession, or financial situation.

## Key Concepts
- **ASPIRE** (Automated Synthetic Persona Interview and Response Engine): a custom-built tool that creates a "digital twin" persona mirroring each real participant's demographic features and prompts an LLM to complete a survey from that perspective, using JSON Mode for structured output
- **Digital twin / synthetic persona**: a persona constructed from a real participant's demographic profile used to generate LLM survey responses on their behalf
- **Positive response bias**: the observed tendency for LLMs to overestimate favorable attitudes, particularly toward well-known brands; described as a possible artifact of LLMs defaulting to socially desirable responses
- **Variance compression**: synthetic data exhibited significantly lower inter-individual variability than real data, indicating a lack of individual differentiation (confirmed via Brown-Forsythe tests)
- **Marketing funnel model**: the survey framework — brand awareness, consideration, and purchase — used as the basis for questionnaire design
- **Above-chance accuracy**: mean agreement of 78.64% (SD=8.68) for binary items and 78.65% (SD=11.20) for Likert ratings, both significantly better than chance
- **No demographic bias detected**: regression predicting match accuracy from sociodemographic characteristics found no significant predictors — a narrow but notable finding given that other papers find demographic disparities

## Theoretical Framework
Situates within the emerging literature on using LLMs as stand-ins for human participants in social science and market research. Draws on the "homo silicus" / "silicon participant" framing (Horton 2023; Argyle et al. 2023) where LLMs conditioned on demographic profiles simulate survey respondents. The marketing funnel model provides the survey architecture. Acknowledges the premise that LLMs encode population-level patterns from training data may not adequately capture individual-level variability or culturally specific norms outside of American contexts.

## Methods
- **Empirical sample**: 492 participants recruited via Prolific and QuestionPro; 461 retained after exclusions (mean age = 46.4 years, range 18-82; 52.8% female; 48 U.S. states represented); quota-matched to U.S. population on age, gender, and ethnicity
- **Survey design**: assessed attitudes toward 4 well-known brands (Coca-Cola, Pepsi, Sprite, 7UP) and 4 lesser-known brands (Dry, Moxie, Blue Sky, Orangina); binary selections (awareness/consideration/purchase) and numerical Likert-style ratings (n=201 for rating analysis, restricted to recognized brands)
- **Synthetic data generation**: ASPIRE created a demographic-matched digital twin for each participant and used an LLM API with JSON Mode to generate responses following the same survey structure
- **Analysis**: ANOVA with BRAND TYPE (well-known/lesser-known) × DATA TYPE (empirical/synthetic) for aggregate comparisons; Brown-Forsythe tests for variance comparisons; multiple regression predicting individual-level match accuracy from sociodemographic characteristics

## Main Arguments
1. LLMs can approximate aggregate opinion trends — synthetic data accurately captured the direction of differences between well-known and lesser-known brands on both binary and numeric items
2. Above-chance individual accuracy is insufficient for high-stakes use — mean agreement of ~79% looks acceptable but the systematic bias and reduced variance make individual-level prediction unreliable
3. Positive response bias is a consistent failure mode — synthetic data overestimated item selection frequency and positive ratings for both brand types (both p < .001), with larger overestimation for well-known brands
4. Variance compression limits representativeness — synthetic participants responded more uniformly than real humans (Brown-Forsythe p < .001, eta²=0.185 for binary; eta²=0.029 for Likert), understating real opinion diversity
5. No demographic bias detected — but the domain was benign: the authors explicitly caution that sensitive domains (health, politics, medicine) carry substantially higher bias risk

## Limitations & Critiques
- Domain ceiling: consumer preferences for soft drinks are an easy, familiar, low-stakes topic; results likely overestimate LLM performance relative to sensitive or politically charged domains
- Demographics-only personas: digital twins constructed only from demographic data; richer individual-level information (personality, prior behavior, domain expertise) not used
- LLM not specified: the paper does not identify which LLM model was used, making replication and cross-model comparison difficult
- No cross-cultural validation: U.S.-only sample; American cultural alignment of LLM training data likely inflates performance in this context
- Work-in-progress scope: described as ongoing research; ASPIRE is still under active development
- Positive response bias unexplained mechanistically: the paper identifies the overestimation pattern but does not test hypotheses about its cause

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Evaluating LLMs in Generating Synthetic HCI Research Data (Hamalainen et al., 2023)]] - prior validation work on LLMs as synthetic HCI participants cited by this paper
- [[Lost in Simulation LLM-Simulated Users are Unreliable Proxies for Human Users (Seshadri et al., 2026)]] - related critique of LLM-simulated users; Kaiser et al. provide empirical grounding for the reliability concerns raised there
- [[Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents (Morocho et al., 2026)]] - direct thematic neighbor on LLM-based synthetic survey respondents
- [[Persona-Based Simulation of Human Opinion at Population Scale (Li et al., 2026)]] - related work on scaling persona-based opinion simulation with richer social-media grounding
