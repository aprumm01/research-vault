---
source_file: "synth users/Synthetic Heuristic Evaluation AI vs Human-Powered Usability - Zhong et al - 2025.pdf"
type: paper
authors: "Usability Evaluation"
community: "GenAI in UX and Design Practice"
tags:
---

# Synthetic Heuristic Evaluation AI vs Human-Powered Usability - Zhong et al - 2025

## Summary
Synthetic Heuristic Evaluation: A Comparison between AI- and Human-Powered Usability Evaluation RUICAN ZHONG, University of Washington, USA DAVID W MCDONALD, University of Washington, USA GARY HSIEH, University of Washington, USA Usability evaluation is crucial in human-centered design but can be costly, requiring expert time and user compensation In this work, we developed a method for synthetic heuristic evaluation using multimodal LLMs’ ability to analyze images and provide arXiv:2507.

## Key Concepts
- Synthetic heuristic evaluation using multimodal LLMs (GPT-4, Gemini-1.5-pro, Claude 3.5 Sonnet)
- Nielsen's 10 usability heuristics as evaluation framework
- Severity rating scale (0-4) for prioritizing usability issues
- Master set methodology for objective performance comparison
- Reliability testing across time periods and accounts to address stochastic nature of LLMs
- Qualitative descriptions vs quantitative scores in usability reporting
- Cross-platform LLM performance comparison

## Theoretical Framework
[[frameworks/Heuristic Evaluation]] - Nielsen's 10 heuristics for usability evaluation

## Methods
comparative study, experimental, reliability testing

## Main Arguments
- Synthetic heuristic evaluation identified 73-77% of usability issues vs 57-63% by 5 aggregated expert evaluators
- LLMs can produce qualitative usability assessments with rationales rather than just quantitative scores
- Approach demonstrates reliability across repeated prompting over 3-month period and multiple accounts
- GPT-4 achieved best performance among three LLMs tested; Claude 3.5 Sonnet lowest
- LLMs can analyze images, compare designs against heuristics, and explain violations with reasoning
- Synthetic evaluation provides scalable alternative to costly traditional usability testing ($10k-$50k per 5-participant study)
- Addresses gap in automated usability testing by providing subjective qualitative data previously missing

## Limitations & Critiques
- Only tested on two common app types - domain-specific apps requiring specialized knowledge not explored
- Model performance may change as generative AI evolves - prompting techniques may require adaptation
- GPT-4 performed best partly because prompts not fine-tuned for other models
- All models struggled with understanding app-specific conventions though GPT-4 did best
- No exploration of how severity ratings compare between synthetic and human evaluators
- Limited discussion of when synthetic evaluation should supplement vs replace human evaluation
- Does not address learning curve or setup costs for practitioners adopting synthetic evaluation

## Connections
- [[frameworks/Human-Centered Design]] - Theoretical framework
- [[communities/GenAI in UX and Design Practice]] - Research community
