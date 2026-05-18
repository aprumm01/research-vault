---

source_file: "research_docs/P526.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2026"
---

# Persona-Based Simulation of Human Opinion at Population Scale (Li et al., 2026)

## Summary
Li and Conrad introduce SPIRIT (Semi-structured Persona Inference and Reasoning for Individualized Trajectories), a framework for simulating individual-level human opinions rather than predicting group-level demographic correlations. SPIRIT infers psychologically grounded personas from public social media posts — combining structured attributes (personality traits, world beliefs) with unstructured narrative text — and uses these to condition LLM agents when answering survey questions. Using the Ipsos KnowledgePanel (a nationally representative U.S. probability sample), they show that SPIRIT-conditioned simulations recover self-reported responses more faithfully than standard demographic persona prompting and reproduce human-like heterogeneity in response patterns, including the capacity to function as virtual respondent panels for both stable attitudes and time-sensitive public opinion.

## Key Concepts
- SPIRIT framework: Semi-structured Persona Inference and Reasoning for Individualized Trajectories — persona built from social media, not demographics
- Demographic vs. simulation paradigm: critiques approaches that predict from demographic correlations vs. those that model individuals
- Psychological grounding: personas encode personality traits, world beliefs, and narrative identity, not just age/gender/education
- Population-level calibration: using probability-sample panel data (Ipsos KnowledgePanel) to validate that persona banks are representative
- Virtual respondent panels: persona banks used as standing substitutes for repeated-survey human panels

## Theoretical Framework
Draws on survey methodology (probability sampling, calibration, design-based inference) and computational social science; situates LLM simulation within the stance that demographics alone underdetermine opinion — invoking personality psychology (Big Five), narrative identity theory, and political identity as the missing variables. Methodologically positioned against both demographic-prompting approaches and non-probability sampling concerns.

## Methods
SPIRIT personas inferred from public social media posts for a subset of Ipsos KnowledgePanel respondents; simulations ran against survey questions on attitudes and public opinion; responses compared to actual self-reported panel responses; validation metrics include individual-level accuracy and population-level distribution recovery; time-sensitive public opinion scenarios also tested to evaluate whether persona banks track opinion change.

## Main Arguments
- Demographic-based persona prompting is a predictive, not simulation, paradigm: it cannot generate the within-group variability observed in real populations
- SPIRIT recovers individual responses more accurately than demographic prompting because it captures psychological and narrative dimensions that demographics miss
- Persona banks derived from social media can function as virtual respondent panels, enabling low-cost, rapid opinion polling without recruiting new participants
- Population-level distribution recovery depends on probability-sample grounding: non-probability personas (e.g., scraped from online forums) cannot support population inference without calibration

## Limitations & Critiques
Social media as a persona source introduces platform-specific biases (users skew younger, more engaged, politically vocal); the framework depends on public social media posts, raising privacy questions about using real individuals as simulation targets; validation is limited to U.S. English-language contexts and the Ipsos panel, so generalizability across languages and cultures is untested.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Simulating Human Opinions with Large Language Models (Kaiser et al., 2025)]] - parallel approach to LLM-based opinion simulation with different grounding strategy
- [[Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents (Morocho et al., 2026)]] - critical evaluation of persona-conditioned survey simulation
