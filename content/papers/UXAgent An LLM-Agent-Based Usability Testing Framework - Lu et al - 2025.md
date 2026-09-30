---
source_file: "synth users/UXAgent An LLM-Agent-Based Usability Testing Framework - Lu et al - 2025.pdf"
type: paper
authors: "Yuxuan Lu, Bingsheng Yao, Hansu Gu, Jing Huang, Zheshen Wang, Yang Li, Jiri Gesi, Qi He, Toby Jia-Jun Li, Dakuo Wang"
community: "GenAI in UX and Design Practice"
tags:
---

# UXAgent An LLM-Agent-Based Usability Testing Framework - Lu et al - 2025

## Summary
Northeastern University, Amazon, and Notre Dame collaboration proposing UXAgent system using LLM-based agents to simulate usability testing participants at scale. System enables UX researchers to evaluate and iterate experiment designs before conducting human-subject studies. Features three modules: Persona Generator (creates diverse user personas), LLM Agent with dual-loop architecture (Fast Loop for real-time interaction, Slow Loop for strategic reasoning), and Universal Browser Connector (parses raw HTML to simplified observation space, generates task-agnostic actions). Produces quantitative data (action traces), qualitative data (memory/reasoning traces, chat interviews), and video recordings. Heuristic evaluation with 5 UX researchers showed agents generate "very detailed" behaviors "not like real humans" but still "very helpful" for iterating experiment designs. Tested on WebArena shopping environment.

## Key Concepts
- [[concepts/Simulated User Agents]]
- [[concepts/LLM Agents]]
- [[concepts/Usability Testing]]
- [[concepts/Persona-Based Testing]]
- [[concepts/Human-AI Collaboration]]
- [[concepts/Universal Browser Connector]]
- [[concepts/Dual-Loop Architecture]]

## Theoretical Framework
Kahneman's dual-process theory: Fast Loop (reactive, low-latency interactions) and Slow Loop (reflective, strategic reasoning). Memory Stream architecture with importance, relevance, and recency-based retrieval. Believable agent behaviors: agents "appear to make decisions and act on their own volition" like real humans.

## Methods
- Heuristic evaluation with 5 UX researchers
- System testing on WebArena (open-source shopping platform) and Google Flights
- Persona generation via LLM prompting with demographic distributions
- Qualitative interviews via chat interface with agent memory traces

## Main Arguments
- LLM Agents should complement, not replace, human participants—serve as pilot testing tool to iterate study designs responsibly before human-subject studies
- Traditional usability testing challenges: ill-designed experiments waste participant time, difficulty recruiting narrowly-defined user groups, lack of early feedback on experiment design
- Universal Browser Connector enables generalization across websites without predefined action spaces
- System produces multimodal data (quantitative action traces, qualitative interviews, video recordings) matching UX researchers' familiar analysis methods
- Position: "LLM Agents can work together with UX researchers (human-AI collaboration) in a simulated pilot session to provide desired early and immediate feedback"

## Limitations & Critiques
- UX researchers judged agent behaviors as "not like real humans" because "very detailed" and "real human won't think like that"
- Believability concerns: agents may be too rational/optimized (e.g., shopping with "most optimized path" vs. human "twisted shopping path with lots of seemingly wasted action steps")
- Limited evaluation: heuristic study with 5 participants, single shopping domain tested
- Generalizability unclear: tested on WebArena and Google Flights only
- Ethical concerns about replacing human participants not fully addressed
- Persona diversity may be superficial without affecting deeper reasoning patterns

## Related Papers
- [[papers/UXCascade Scalable Usability Testing with Simulated User Agents - Holter et al -]]
- [[papers/Evaluating LLMs in Generating Synthetic HCI Research Data]]

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
- [[concepts/Simulated User Agents]] - Core method
- [[methods/Interview]] - Qualitative data collection
