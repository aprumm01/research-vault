---

source_file: "research_docs/P445.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2024"
authors: "de Wit"
---

# Leveraging Large Language Models as Simulated Users for Initial, Low-Cost Evaluations of Designed Conversations (de Wit, 2024)

## Summary
Jan de Wit (University of Twente) presents initial explorations of using ChatGPT (GPT-3.5 and GPT-4) as simulated users for evaluating rule-based conversational agents, integrated into the Tilbot conversation design tool. The study uses an autoethnographic account by the author plus a small-scale evaluation with three conversation designers, applied to two case studies: a Guess Who game chatbot and a medication reconciliation agent designed for a Dutch hospital. Findings show ChatGPT can generate realistic, varied test scenarios as a low-cost pre-study evaluation method, with GPT-4 substantially outperforming GPT-3.5. All three evaluating designers rated the tool favorably on perceived usefulness (4.06/5) and ease of use (4.2/5) and would use it again. Published as LNCS 14524 in the CONVERSATIONS 2023 workshop proceedings (Springer, 2024).

## Key Concepts
- Simulated users as low-cost conversational agent evaluation method prior to human-subject testing
- Tilbot: conversation design tool with integrated ChatGPT simulated user module
- GPT-4 vs. GPT-3.5: GPT-4 significantly better at handling data, maintaining persona, and playing games
- "Latent social information" (Horton): LLMs embed broad social knowledge enabling realistic scenario generation
- LLM hallucination as a feature: generates realistic varied test data that designers would not think to supply
- Expert blind spot problem: conversation designers reuse same test data; simulated users add variety
- TAM evaluation: perceived usefulness 4.06/5, ease of use 4.2/5 among three designers
- Western-oriented bias: simulated users interact from a predominantly Western context

## Theoretical Framework
Technology Acceptance Model (Davis) for evaluation; prior work on simulated users in dialogue systems (deterministic scripted and probabilistic trained variants); Argyle et al.'s "silicon sampling" framing; Horton's "computational models of humans"; published in LNCS 14524, CONVERSATIONS 2023, 7th International Workshop on Chatbot Research and Design (Oslo, November 2023), Springer 2024.

## Methods
Autoethnographic study by the author applying the ChatGPT simulated user to two case studies (Guess Who game; hospital medication reconciliation chatbot); small-scale evaluation study with three conversational agent researchers using Qualtrics-mediated survey and the Tilbot tool; TAM-based questionnaire (perceived usefulness and ease of use, five-point Likert scale); qualitative thematic analysis of free-text comments; exploratory rather than confirmatory.

## Main Arguments
- LLMs functioning as simulated users can identify real usability issues in designed conversations -- especially intent recognition failures, out-of-perimeter utterances, and dialogue flow problems -- at a fraction of the cost of recruiting human participants
- LLM "hallucination" is paradoxically useful in this context: it generates diverse, realistic user inputs (e.g., plausible medicines with dosages) that conversation designers testing their own systems would not think to provide, surfacing issues that would remain hidden in designer-led testing
- GPT-4 substantially outperforms GPT-3.5 for this use case, particularly in data handling, persona consistency, and game-playing tasks
- The simulated user is by no means a replacement for human evaluation -- biases (especially Western-oriented defaults), failure to model low-literacy users, and remaining deficiencies in human cognition modeling mean human studies remain essential; simulated users are a "discount" method for early iteration only

## Limitations & Critiques
Autoethnographic study + three participants; not a rigorous comparative study against human participant outcomes; all evaluators were fellow researchers (not actual conversation designers building novel products); only task-oriented, rule-based agents tested (not open-ended conversational agents); ChatGPT's Western and demographic biases are acknowledged but not addressed; the tool's current token limit constrains long-conversation analysis; scale is too small for generalizable conclusions.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[The Use of LLMs in HCI A Critical Analysis of Synthetic Users (Salminen et al., 2025)]] - broader critical analysis of synthetic users in HCI
- [[Evaluating LLMs in Generating Synthetic HCI Research Data (Hamalainen et al., 2023)]] - parallel empirical evaluation of LLMs for HCI research data generation
