---
source_file: "research_docs/synth users/Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents - Morocho et al - 2026.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
  - synthetic-users
  - persona-prompting
  - survey-simulation
  - LLM-evaluation
  - subgroup-fidelity
  - algorithmic-bias
year: "2026"
authors: "Morocho et al"
doi: "10.1145/3774905.3795477"
venue: "WWW Companion '26 (35th ACM Web Conference), Dubai, UAE, April 13–17, 2026"
arxiv: "arXiv:2602.18462v1"
---

# Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents (Morocho et al., 2026)

## Summary
Morocho, Cima, Fagni, Avvenuti, and Cresci conduct a large-scale empirical evaluation of whether multi-attribute persona-conditioned LLMs reliably simulate survey respondents, using 70,000+ respondent-item instances drawn from U.S. microdata from the World Values Survey wave 7 (WVS-7). Evaluating two open-weight chat models — Llama-2-13B and Qwen3-4B — against a random-guesser baseline, they find that persona prompting does not yield a clear aggregate improvement in survey alignment and in many cases significantly degrades performance. Persona effects are highly heterogeneous: most items are minimally affected, but a small subset of items and underrepresented subgroups experience disproportionate distortions. The paper warns that demographic conditioning can redistribute errors in ways that undermine subgroup fidelity and risk misleading downstream social science analyses, precisely because aggregate metrics can look acceptable while subgroup-level errors remain severe.

## Key Concepts
- **Subgroup fidelity**: agreement between LLM simulated responses and real human responses within demographic subgroups, not just in aggregate; preservation of between-subgroup differences
- **External validity**: aggregate agreement of the synthetic population with survey-grounded population response patterns
- **Persona prompting failure**: multi-attribute demographic conditioning does not reliably improve LLM survey alignment over a matched vanilla (unconditioned) baseline
- **Error redistribution**: persona conditioning shifts errors from some items/groups to others, concentrating distortions in underrepresented small-n subgroups
- **Hard similarity (HS)**: exact-match accuracy between LLM response and ground-truth WVS-7 response code
- **Soft similarity (SS)**: ordinal metric based on Normalized Match Distance (NMD) for the 22 of 31 items that are ordinal (e.g., Likert scales); reduces to 0/1 mismatch for non-ordinal items
- **World Values Survey wave 7 (WVS-7)**: large cross-national survey dataset (wave conducted 2017–2021) used as ground truth for evaluating synthetic respondents
- **Vanilla baseline (V)**: identical prompt structure without demographic clauses — key methodological contribution; most prior work lacks this matched control

## Theoretical Framework
Situated at the intersection of (1) LLMs as synthetic survey respondents and opinion predictors, (2) persona conditioning and demographic alignment research, (3) LLM-based social simulation, and (4) methodological critique of LLM-generated data for computational social science. Draws on Argyle et al.'s "silicon samples" and "algorithmic fidelity" concept (GPT-3 conditioned on U.S. sociodemographic backstories), and on Alkhamissi et al.'s WVS-based persona evaluation framework, but challenges optimistic conclusions by using a larger, more demographically diverse benchmark and applying stricter subgroup-level evaluation with a matched vanilla control design.

## Methods
- **Dataset**: WVS-7 U.S. respondent-level microdata; 31 curated items spanning social trust, confidence in institutions, immigration attitudes, political participation, religion, and values
- **Unit of evaluation**: respondent-question instance — each of ~2,300–2,600 U.S. respondent records paired with each of 31 items; over 70,000 respondent-item instances total
- **Models**: Llama-2-13B and Qwen3-4B (open-weight chat models)
- **Persona attributes (8)**: gender, age, highest educational level, employment status, occupational group, income level, religious denomination, ethnic group — extracted from WVS-7 respondent records
- **Prompting conditions**:
  - *Vanilla (V)*: identical prompt structure without demographic clauses
  - *Persona-based (PB)*: demographic clauses prepended as declarative bullet statements; model instructed to answer strictly from the persona's point of view
  - *Random guesser (R)*: uniform sampling from valid response options per item — theoretical chance baseline
- **Decoding**: temperature 0.3; one completion per instance; responses parsed by normalizing casing/punctuation and matching option index or text span to valid WVS-7 response categories
- **Evaluation metrics**: HS (exact-match accuracy) and SS (ordinal soft similarity via NMD) computed at aggregate level and within each demographic subgroup partition; Wilcoxon signed-rank tests for PB vs. V and PB vs. R significance

## Key Results (Tables 1 and 2)

### Aggregate external validity (Table 1)

| Condition | HS | SS |
|---|---|---|
| Random guesser (R) | 0.273 | 0.537 |
| Llama-2-13B Vanilla (V) | 0.366 | 0.612 |
| Llama-2-13B Persona-based (PB) | 0.370 | 0.621 |
| Qwen3-4B Vanilla (V) | 0.398 | 0.627 |
| Qwen3-4B Persona-based (PB) | 0.391 | 0.627 |

- Both models substantially exceed random guesser
- For Llama-2-13B, PB slightly *reduces* both HS and SS relative to V (PB vs. V: HS p < 0.05, SS p < 0.01 — statistically significant *degradation*)
- For Qwen3-4B, PB yields modest HS increase but leaves SS unchanged (not statistically significant)
- Aggregate metrics look acceptable; subgroup behavior is where the problem shows

### Subgroup fidelity (Table 2) — selected findings

- **Black respondents**: HS consistently lowest across both models; PB does not improve over V (Llama V: 0.337, PB: 0.339; Qwen V: 0.352, PB: 0.368); most disadvantaged group receives the least benefit from conditioning
- **White respondents**: HS consistently highest; PB marginally improves Qwen (0.407 vs. 0.396 V)
- **Higher education**: higher HS (Llama 0.375, Qwen 0.413) vs. lower education (Llama 0.362, Qwen 0.361)
- **Small-n strata instability**: Farm owner (n=4): Qwen3-4B PB HS = 0.336 vs. R = 0.242 — PB significantly worse than random chance (p < 0.1); persona conditioning introduces high-variance distortions precisely where ground-truth estimates are already unstable
- **One notable PB gain**: "Never had a job" (n=13): Llama PB HS = 0.392 vs. Llama V HS = 0.306 — one of few strata where PB substantially outperforms V; tiny n makes this unreliable

## Main Arguments
- Persona prompting does not yield systematic aggregate improvement in LLM survey alignment; the null/negative result is the central finding
- Effects are highly heterogeneous: most items are minimally affected by persona conditioning, but a small subset shows large distortions in both directions
- Underrepresented demographic subgroups bear disproportionate error concentration — the most consequential failure mode for equity-sensitive research
- The adverse impact on already-marginalized groups calls into question standard practices in computational social science that assume conditioning = improvement
- Practical recommendation: always report matched vanilla baselines alongside persona-based results; audit item- and subgroup-level behavior rather than relying solely on aggregate scores

## Limitations & Critiques
- Evaluation restricted to WVS-7 U.S. participants only; results may not transfer to other national contexts, cultural settings, or survey domains
- Only two open-weight models evaluated; whether proprietary frontier models (GPT-4o, Claude, etc.) exhibit the same patterns is unknown
- Single decoding run per instance (temperature 0.3); generation variance across repeated runs is not estimated
- Soft similarity relies on an ordinality assumption for scale items — coarse approximation for items whose semantics are not strictly linear
- Persona conditioning derived from 8 sociodemographic attributes; does not capture the full context behind a respondent's beliefs
- WVS-7 responses themselves contain measurement noise, social desirability bias, and respondent inconsistency
- No alternatives to persona prompting are proposed or tested

## Connections
- [[GenAI in UX and Design Practice]] - synthetic user research and LLM-driven simulation practices
- [[Responsible AI and Ethics]] - subgroup fidelity failures and disproportionate error concentration in underrepresented groups
- [[Synthetic Users and AI Personas]] - central to the paper's contribution; directly challenges reliability assumptions in persona-based simulation
- [[Simulating Human Opinions with Large Language Models (Kaiser et al., 2025)]] - parallel empirical study of LLM survey simulation
- [[Persona-Based Simulation of Human Opinion at Population Scale (Li et al., 2026)]] - alternative approach addressing the demographic grounding problem
- [[Lost in Simulation LLM-Simulated Users are Unreliable Proxies for Human Users (Seshadri et al., 2026)]] - concurrent finding on demographic conditioning and failure for minority groups
- [[The Use of LLMs in HCI A Critical Analysis of Synthetic Users (Salminen et al., 2025)]] - broader critique of synthetic user validity
- [[Evaluating LLMs in Generating Synthetic HCI Research Data (Hamalainen et al., 2023)]] - foundational validation work this paper extends to the subgroup level
