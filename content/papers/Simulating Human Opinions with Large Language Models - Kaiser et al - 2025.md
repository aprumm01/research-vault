---
source_file: "synth users/Simulating Human Opinions with Large Language Models - Kaiser et al - 2025.pdf"
type: paper
authors: "Carolin Kaiser"
community: "Design Theory and Cognition"
tags:
---

# Simulating Human Opinions with Large Language Models - Kaiser et al - 2025

## Summary
HCI design and evaluation methods; User models; • Applied computing → Operations research; Marketing Public and private organizations rely on opinion surveys to inform business and policy decisions Yet, empirical surveys are costly and time-consuming.

## Key Concepts
- Synthetic survey sampling using LLM-generated responses
- "Digital twins" - personas mirroring demographic profiles
- ASPIRE (Automated Synthetic Persona Interview and Response Engine) tool
- Algorithmic fidelity and "homo silicus" / "silicon participant" concepts
- Persona-conditioned survey simulation

## Theoretical Framework
Marketing funnel model for consumer research; Digital twin paradigm for user modeling; Persona-based LLM conditioning

## Methods
Empirical benchmark survey with 461 U.S. participants (quota-matched by age, gender, ethnicity) on soft drink brand preferences; ASPIRE tool using GPT-4o to generate synthetic responses; Personas created with 9 demographic attributes (gender, birth year, education, occupation, financial situation, state, ethnicity, country of birth, nationality, language); Survey included binary items (brand awareness, consideration, purchase) and Likert-scale ratings (1-7); Statistical comparison using ANOVA, Brown-Forsythe tests, regression analysis

## Main Arguments
- Traditional surveys are costly, time-consuming, face declining response rates and non-response bias
- Synthetic sampling offers fast, low-cost alternative for modeling aggregate opinion trends
- Synthetic data achieved better-than-chance accuracy (78.64-78.65% agreement) in matching human responses
- LLM simulations approximated aggregate subjective rankings for both binary and Likert-scale items
- Synthetic data correctly differentiated between popular and unpopular brands similar to real participants

## Limitations & Critiques
- LLM-simulated data overestimated humans' tendencies to provide positive ratings for both well-known and lesser-known brands
- Synthetic data exhibited substantially reduced variance compared to real data - more uniform response patterns vs. human variability
- Falls short in replicating the variability and complexity of real human opinions
- Mixed findings in prior work - some studies show limitations in capturing nuanced differences between humans
- Concerns about demographic biases in some contexts (though not found in this study's soft drink topic)
- Study topic (soft drinks) relatively benign - risks of demographic stereotyping may be higher in sensitive domains (health, politics, medicine)
- ChatGPT aligns more with American cultural norms, limited adaptability to other cultural contexts
- Applying synthetic sampling in high-stakes contexts requires high degree of caution
- Currently unclear which types of individual-level data most valuable for enhancing synthetic accuracy
- Need for rigorous evaluation before synthetic sampling can supplement conventional survey methods

## Connections
- [[methods/Survey]] - Research methodology
- [[methods/Interview]] - Research methodology
- [[communities/Design Theory and Cognition]] - Research community
