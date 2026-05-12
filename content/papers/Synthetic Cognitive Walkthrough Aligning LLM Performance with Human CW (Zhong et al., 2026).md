---

source_file: "research_docs/P460.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2026"
---

# Synthetic Cognitive Walkthrough: Aligning Large Language Model's Performance with Human Cognitive Walkthrough (Zhong et al., 2026)

## Summary
Zhong, McDonald, and Hsieh from the University of Washington explore whether LLMs (GPT-4 and Gemini 2.5 Pro) can simulate human behavior in cognitive walkthrough (CW) usability evaluations. Comparing LLM-prompted walkthroughs against human participants, they find that while LLMs can navigate interfaces and provide reasonable rationales, their behavior differs systematically: LLMs achieve higher task completion rates, follow more optimal paths, and identify fewer potential failure points than humans. However, follow-up studies show that with additional prompting (instructing LLMs to predict human-identified failure points), alignment with human CW performance improves substantially. The paper positions synthetic CW as a scalable complement to traditional CW rather than a direct substitute.

## Key Concepts
- Synthetic cognitive walkthrough (CW): LLMs simulating the four-question CW usability method
- LLMs achieve higher task completion than humans in CW tasks (systematic over-performance)
- LLMs follow more optimal navigation paths, missing the sub-optimal paths humans take
- Failure point gap: LLMs identify fewer potential user failure points than humans
- Alignment improvement through additional prompting: instructing LLMs to predict human failures closes the gap
- Scalable CW: the value proposition is breadth and speed, not equivalence to human evaluators

## Theoretical Framework
Cognitive walkthrough usability evaluation literature (Lewis et al., Wharton et al.); HCI usability testing tradition; LLM agent capabilities literature; builds on Zhong et al.'s prior Synthetic Heuristic Evaluation (2025); visual reasoning and UI navigation capabilities of GPT-4 and Gemini 2.5 Pro; presented at CHI 2026 (Barcelona, April 2026).

## Methods
Comparison study: LLMs (GPT-4 and Gemini 2.5 Pro) prompted to perform cognitive walkthroughs on the same interfaces tested with human participants; human CW sessions conducted following standard four-question CW protocol; comparison across task completion rates, navigation paths, and failure points identified; follow-up study with modified prompting (failure point prediction mode) to test whether alignment can be improved; quantitative analysis of completion rates and failure point overlap.

## Main Arguments
- LLMs simulate the outcome of CW (task completion) more readily than the process of CW (human-like navigation errors and failure points), because LLMs approach interfaces as optimal problem solvers rather than as users with realistic cognitive limitations
- The failure point gap is the critical finding: since identifying potential failure points is the core purpose of CW in UX practice, LLMs in default mode systematically miss what matters most about the method
- Additional prompting can partially close the gap: when explicitly instructed to predict where humans would fail rather than to succeed at the task themselves, LLMs produce failure point lists that better overlap with human evaluators
- Synthetic CW is most valuable as a breadth-scaling tool -- running CW across many screens, flows, and edge cases that human teams lack the time to cover -- rather than as a replacement for expert human evaluation

## Limitations & Critiques
Limited to two LLM systems (GPT-4 and Gemini 2.5 Pro); the specific interfaces and tasks used may not generalize across all interface types; human participant sample characteristics not fully specified; the follow-up prompting improvement is promising but not systematically validated at scale; no comparison of cost-effectiveness against alternative usability methods.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Synthetic Heuristic Evaluation AI vs Human-Powered Usability (Zhong et al., 2025)]] - companion paper from same research group
