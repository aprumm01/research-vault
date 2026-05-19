---

source_file: "research_docs/P461.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Zhong, McDonald, and Hsieh"
---

# Synthetic Heuristic Evaluation: A Comparison between AI- and Human-Powered Usability Evaluation (Zhong et al., 2025)

## Summary
Zhong, McDonald, and Hsieh from the University of Washington develop and evaluate a method for synthetic heuristic evaluation using multimodal LLMs (GPT-4, Gemini 1.5 Pro, Claude 3.5 Sonnet) analyzing UI screenshots to identify usability violations against Nielsen's 10 heuristics. Comparing synthetic against human heuristic evaluations across two apps, synthetic evaluation identified 73% and 77% of usability issues -- exceeding the aggregated performance of five experienced human evaluators (57% and 63%). Synthetic evaluation also showed more consistent performance across evaluation tasks and excelled in detecting layout and consistency issues. However, LLMs struggled with recognizing some UI components, understanding design conventions, and identifying across-screen violations. Reliability testing across accounts and over a three-month period showed stable performance. GPT-4 outperformed Gemini 1.5 Pro and Claude 3.5 Sonnet.

## Key Concepts
- Synthetic heuristic evaluation: LLMs prompted to apply Nielsen's 10 heuristics to UI screenshots
- 73-77% issue detection rate exceeding 5-evaluator human aggregation (57-63%)
- Consistent LLM performance across tasks vs. declining human evaluator performance
- Layout and consistency violations: LLM strength area
- Across-screen violations: LLM weakness area (requires multi-screen reasoning)
- Reliability: stable performance across two accounts over three months
- GPT-4 superiority among three tested LLMs

## Theoretical Framework
Nielsen's heuristic evaluation methodology (10 heuristics, 1994); usability testing literature; multimodal LLM image analysis capabilities; positioned against prior automated usability testing approaches (rule-based simulation, eye-tracking analysis); compared against traditional human evaluator benchmark; submitted to conference proceedings (manuscript version, 2025).

## Methods
Systematic prompting of multimodal LLMs to conduct heuristic evaluation from UI screenshots; three LLM systems tested (GPT-4, Gemini 1.5 Pro, Claude 3.5 Sonnet); two real mobile app interfaces used as test cases; human evaluation condition: aggregated output from five experienced UX practitioners; master set of ground truth issues established for comparison; performance measured as percentage of master set issues identified; reliability tested across two accounts and repeated over three months.

## Main Arguments
- Multimodal LLMs can perform heuristic evaluation effectively, detecting a higher proportion of usability issues than a standard five-evaluator human panel -- challenging the conventional assumption that expert evaluators are the gold standard
- The synthetic evaluation's main strength is consistency and perceptual pattern matching: it does not suffer the fatigue or attention lapses that cause human evaluator performance to decline across tasks
- The key limitation is a lack of cross-screen reasoning: LLMs cannot easily integrate information across multiple UI states to identify violations that only become apparent when considering the full user flow
- Reliability over time is a practically important finding: unlike human evaluators whose performance may drift, the LLM-based evaluation is reproducible -- though this also means errors are consistently repeated

## Limitations & Critiques
Only two apps evaluated, limiting generalizability; master set of issues constructed by the research team may not fully capture all legitimate usability problems; the human evaluator baseline (5 evaluators, 57-63%) reflects typical rather than ideal performance; the study tests heuristic evaluation specifically, which is less demanding than user testing or cognitive walkthroughs; evaluation context is screenshot-based and does not include interactive flow testing.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Heuristic Evaluation]] - `` [EXTRACTED]
- [[Synthetic Cognitive Walkthrough Aligning LLM Performance with Human CW (Zhong et al., 2026)]] - companion paper extending this work to cognitive walkthrough method
