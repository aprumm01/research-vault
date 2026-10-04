---
source_file: "LLM Agent Meets Agentic AI Can LLM Agents Simulate Customers - Sun et al - 2025.pdf"
type: paper
authors: "Lu Sun, Shihan Fu, Bingsheng Yao, Yuxuan Lu, Wenbo Li, Hansu Gu, Jiri Gesi, Jing Huang, Chen Luo, Dakuo Wang"
year: 2025
---

# LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-based Shopping Assistants?

## Summary

This paper investigates whether LLM agents can serve as "digital twins" of human customers to evaluate agentic AI-based conversational shopping assistants (CSAs) like Amazon Rufus. The authors conducted a two-stage study: first, a human study with 40 participants interacting with Amazon Rufus to establish ground truth data on shopping behaviors, interaction traces, and UX feedback. Second, they created persona-grounded LLM agents using the UXAgent framework to role-play as digital twins of the same participants and complete identical shopping tasks.

The study found that while LLM agents can meaningfully approximate human behavior in multi-turn interactions with agentic AI systems, important gaps exist. Agents matched humans on structural measures like task completion (F1 score of 0.9) and turn counts, and their opening queries showed alignment with humans' first queries (similarity > 0.4). However, only about 2% of agent-human pairs selected the exact same product, and agents explored more broadly while humans narrowed constraints more selectively. On UX evaluations, agents aligned with humans on objective dimensions but systematically overestimated their own satisfaction compared to human self-reports.

This research is the first to quantify how closely LLM agents can mirror human multi-turn interaction with agentic AI systems, highlighting both the promise of LLM-based digital twins for scalable early-stage evaluation and the continued need for human studies to capture nuanced, affective aspects of user experience.

## Key Concepts

- **Digital Twins**: LLM agents instantiated with real human personas (demographics, shopping habits, personality traits) to simulate human customers in AI evaluation studies
- **Conversational Shopping Assistants (CSAs)**: AI-powered interfaces like Amazon Rufus that enable natural language shopping interactions, transforming traditional search-and-filter into conversational dialogues
- **Agent-as-a-Judge**: Paradigm where LLM agents evaluate other AI systems, extended here to multi-turn human-AI interactions rather than single-turn responses
- **UXAgent**: A persona-driven LLM agent framework for web-based usability testing that enables realistic task execution and reflective UX reasoning

## Theoretical Framework

The study builds on research in LLM-based simulation of human behavior, extending the Agent-as-a-Judge paradigm from single-turn evaluations to dynamic multi-turn interactions. It draws on UX evaluation methodology, combining quantitative behavioral metrics with qualitative assessment of user experience dimensions (satisfaction, usability, helpfulness, trust, cognitive load).

## Methods

- **Stage 1 Human Study**: 40 participants recruited from Prolific completed shopping tasks with Amazon Rufus across utilitarian (monitor, chair) and hedonic (wedding outfit, hiking jacket) categories. A custom Chrome extension logged all interactions. Participants completed demographic surveys, personality inventories (Big Five, MBTI), and post-task UX evaluations.
- **Stage 2 Agent Simulation**: Using UXAgent with Claude 3.7 Sonnet (temperature=0.2), LLM agents were initialized with participant personas and completed identical tasks. Agents generated structured UX evaluations using the same survey instruments.
- **Measures**: Task outcome alignment (F1 scores on purchase decisions), interaction behavior alignment (turn counts, message similarity, Levenshtein distance of action traces), and UX evaluation alignment (paired t-tests on 5-point Likert scales).

## Main Arguments

- LLM agents can complete assigned shopping tasks and match humans on structural behavioral measures, demonstrating potential for scalable early-stage evaluation
- Agents favor breadth-first exploration (clicking more recommendations, longer queries), while humans use more selective, goal-directed constraint narrowing
- Agents systematically underrate their satisfaction compared to humans' satisfaction with chosen products, suggesting they cannot fully capture affective dimensions
- Hybrid evaluation strategies combining agent-based simulation with human feedback are necessary for comprehensive UX assessment of agentic AI systems
- The goal is not to replace human participants but to complement them, enabling rapid iteration while reserving human studies for capturing nuance

## Limitations & Critiques

- Single domain (online shopping) and single platform (Amazon Rufus) limits generalizability to other agentic AI applications
- Agent simulations relied on one implementation (UXAgent with Claude 3.7); different LLMs or architectures may yield different alignment levels
- The study captures behavioral and attitudinal alignment but cannot assess whether agents truly "understand" user preferences or reasoning
- Human-agent divergence in exploration strategies may reflect fundamental differences in how LLMs versus humans approach decision-making under uncertainty
