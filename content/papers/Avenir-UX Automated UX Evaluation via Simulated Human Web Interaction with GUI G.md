---
source_file: "synth users/Avenir-UX Automated UX Evaluation via Simulated Human Web Interaction with GUI Grounding - Tan et al - 2026.pdf"
type: paper
authors: "Interaction with GUI Grounding"
community: "GenAI in UX and Design Practice"
tags:
---

# Avenir-UX Automated UX Evaluation via Simulated Human Web Interaction with GUI Grounding - Tan et al - 2026

## Summary
1 Evaluating web usability typically requires time-consuming user studies and expert reviews, which often limits iteration speed during product development, especially for small teams and agile workflows We present Avenir-UX, a user-experience evaluation agent that simulates user behavior on websites and produces standardized usability Unlike traditional tools that rely on DOM parsing, Avenir-UX grounds actions and observations, enabling it to interact with real web pages end-to-end while maintaining a coherent trace of the user journey.

## Key Concepts
- [[concepts/GUI Grounding]] - Visual perception and coordinate-based tagging enabling agents to interact with pixels directly rather than relying on DOM parsing
- [[concepts/Synthetic Users]] - LLM agents simulating human behavior through visual perception to assess usability as real users would experience
- [[concepts/Think Aloud Protocol]] - Real-time verbalization of reasoning capturing the "why" behind interaction errors or delays during task completion
- [[concepts/Experience-Imitation Planning (EIP)]] - Retrieving and synthesizing external procedural knowledge to emulate strategies of informed human users
- [[concepts/Mixture of Grounding Experts (MoGE)]] - Multimodal approach combining DOM parsing with visual tagging for robust web interaction
- [[concepts/Friction Map]] - High-fidelity mapping of user journey identifying specific micro-interactions inducing cognitive load or navigational drift

## Theoretical Framework
- [[frameworks/Human-Centered Evaluation]] - Mimicking professional usability study practices through standardized metrics and qualitative protocols
- [[frameworks/Multimodal Perception Theory]] - Understanding how visual grounding captures true interface experience including layout, visibility, and accessibility

## Methods
- System architecture built on Avenir-Web framework with three components: visual perception/grounding, core agent/reasoning (Gemini-3Pro), adaptive memory/checklist
- Three-phase evaluation pipeline: Think Aloud protocol generating reasoning traces, step-wise SEQ (Single Ease Question) on 1-7 scale measuring difficulty/efficiency/clarity/confidence, post-task SUS (System Usability Scale) 10-item questionnaire
- Case study validation comparing agent evaluations against human user assessments
- Sauro-Lewis Curved Grading Scale for interpreting SUS scores (A+ > 84.1, F < 51.7)

## Main Arguments
- Traditional UX evaluation is resource-intensive requiring participant recruitment, scheduling, and manual analysis, creating barrier for agile workflows and small teams
- Democratization of development through AI-assisted tools widened gap between rapid development and slow evaluation, with UX frequently neglected leading to technically functional but user-unfriendly products
- Visual grounding essential for authentic usability assessment as DOM-based agents bypass visual clutter, layout ambiguity, and accessibility issues that real users face
- Step-wise SEQ evaluation provides granular, high-frequency assessment superior to post-hoc methods, with strong correlation to task completion time (r = -0.90) and error rates (r = -0.84)
- Combining quantitative metrics (SUS, SEQ) with qualitative Think Aloud reasoning generates holistic UX reports identifying specific elements causing confusion or delight

## Limitations & Critiques
- While MLLMs perform moderately well in overall UI evaluations, they show shortcomings in judging ease-of-use compared to human evaluators (Luera et al.)
- Static screenshot analysis or DOM-based approaches miss dynamic interface behaviors and real-time interaction patterns that affect usability
- Early automation efforts using static analysis or clickstream logging capture what users do but fail to explain why, requiring additional qualitative interpretation
- Agent evaluations may not fully replicate emotional responses, cultural context, or accessibility needs of diverse human user populations
- Reliance on specific MLLM (Gemini-3Pro) means performance may vary with different models, and capabilities constrained by training data biases
- Case study validation scope unclear regarding sample size, diversity of tested interfaces, and statistical power for generalizing findings
- Open question whether synthetic user evaluations can replace or merely complement traditional human user testing across all interaction complexity levels

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
