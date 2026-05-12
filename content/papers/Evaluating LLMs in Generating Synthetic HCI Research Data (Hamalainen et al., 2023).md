---

source_file: "research_docs/P448.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2023"
---

# Evaluating Large Language Models in Generating Synthetic HCI Research Data: A Case Study (Hamalainen et al., 2023)

## Summary
Hamalainen, Tavast, and Kunnari investigate whether LLMs (specifically GPT-3) can generate synthetic user research data that is indistinguishable from real human responses. Using a case study in which participants describe art experiences in video games, they run three experiments: (1) a quantitative study asking 155 people to distinguish GPT-3 from real responses, (2) a qualitative analysis of GPT-3 errors, and (3) a computational analysis comparing content of synthetic and real data. GPT-3 responses were largely indistinguishable from human responses (experiment 1), though qualitative analysis revealed characteristic errors (overconfidence, formulaic phrasing, absence of genuine hesitation). The authors conclude that LLMs can generate believable HCI data useful for piloting and ideation, but any findings must be validated with real participants. They also flag misuse risk: LLMs on crowdsourcing platforms could make self-report data fundamentally unreliable.

## Key Concepts
- LLM as synthetic HCI data generator: GPT-3 role-playing as interview participants
- Indistinguishability: 155 raters failed to reliably identify synthetic responses
- Characteristic GPT-3 errors: repetition, overconfidence, shallow emotional depth
- Synthetic data as pilot study tool: fast, cheap, useful for experiment ideation
- Misuse risk: fake responses on Prolific/MTurk becoming undetectable
- In-context learning and Transformer generalization as the mechanism behind believable outputs

## Theoretical Framework
Computational user modeling tradition in HCI (Oulasvirta et al.); large language model literature (Brown et al. GPT-3); situated within a case study methodology using an existing open dataset on gaming-as-art experiences (Bopp et al.); uses Prolific for participant recruitment in the distinguishability study; presented at CHI 2023 (Hamburg).

## Methods
GPT-3 used to generate synthetic open-ended questionnaire responses mimicking participants in the Bopp et al. art-in-games study; Experiment 1: 155 Prolific participants rate pairs of real vs. synthetic responses for authenticity; Experiment 2: qualitative analysis of failure modes in GPT-3 outputs; Experiment 3: computational text similarity analysis comparing themes in synthetic vs. human data; Bopp et al. dataset selected specifically because it post-dates GPT-3 training data, preventing contamination.

## Main Arguments
- GPT-3 can generate believable HCI self-report data: participants failed to reliably distinguish synthetic from human responses, suggesting LLMs encode enough experiential knowledge to pass surface-level validity checks
- Synthetic data is useful for ideating experiments, piloting interview guides, and exploring research directions -- but it is not a substitute for real data and any conclusions must be validated with human participants
- GPT-3 makes characteristic errors: formulaic sentence structure, over-confidence, absence of personal quirks, and occasional factual inconsistency -- these patterns may become less reliable as models improve
- The misuse scenario is the most urgent finding: if deployed maliciously on crowdsourcing platforms, LLMs could fundamentally corrupt the validity of self-report HCI data

## Limitations & Critiques
Only one dataset and one domain (gaming as art); GPT-3 is now outdated and the results may not generalize to newer models; the indistinguishability finding applies to a specific type of open-ended qualitative data and may not extend to more personal or emotionally complex domains; sample of raters skews toward English-fluent Prolific users; the paper does not test fine-tuned or domain-specific models.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[The Use of LLMs in HCI A Critical Analysis of Synthetic Users (Salminen et al., 2025)]] - directly engages with this paper's claims
