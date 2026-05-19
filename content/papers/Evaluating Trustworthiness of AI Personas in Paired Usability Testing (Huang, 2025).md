---

source_file: "research_docs/P449.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Huang"
---

# Evaluating the Trustworthiness of AI Personas in Paired Usability Testing: A Mixed-Methods Study with Looma.ai (Huang, 2025)

## Summary
Huang presents a mixed-methods study comparing AI agent personas to matched human participants in usability testing of Looma.ai, an AI-powered educational web application. Using a paired design (each human paired with an AI "twin" given the same background information), 10 human-AI pairs completed the same usability tasks. Data were collected across three streams: attitudinal Likert surveys (pre/post), qualitative think-aloud feedback, and behavioral performance metrics. Results show 75.3% correlation in attitudinal change patterns, 92% overlap in qualitative themes, and moderate-to-high behavioral similarity. However, AI personas consistently underestimated human experiences of cognitive load and emotional frustration. The paper concludes AI personas can reliably reproduce structural and task-oriented insights but cannot replicate emotional and affective dimensions of user experience.

## Key Concepts
- Paired human-AI design: each human paired with a matched AI "twin"
- Three validation streams: attitudinal, qualitative, behavioral
- 75.3% correlation in attitudinal changes across 13 Likert items
- Affective fidelity gap: AI personas underestimate cognitive load and emotional frustration
- Think-aloud protocol extended to AI agents via UI/UX Observer Agent running in parallel
- Looma.ai as testbed: AI-powered educational web app requiring multi-step cognitive tasks

## Theoretical Framework
UX usability testing tradition (Nielsen's think-aloud protocol); generative agents literature (Park et al.); Zhong et al. on synthetic heuristic evaluation; UXAgent framework (Lu et al.); applies tri-method validation approach -- triangulating attitudinal, qualitative, and behavioral data; presented at CSAI 2025 (Beijing).

## Methods
10 undergraduate/graduate student participants; each completed a personal attribute form (demographics, AI familiarity, learning app experience) that was fed into an AI agent system prompt; both human and AI "twin" completed identical tasks on Looma.ai; AI agent used web-ui framework (Playwright/Chromium headless browser) with GPT-4o at temperature 0.6; attitudinal data analyzed with paired t-tests and Pearson correlation; qualitative data coded thematically across four app sections; behavioral metrics logged automatically.

## Main Arguments
- AI personas reliably reproduce structural patterns of human usability feedback: 92% theme overlap in qualitative think-aloud data and directionally consistent attitudinal changes suggest AI can serve as a useful proxy for surface-level usability insights
- The key failure mode is affective fidelity: AI agents systematically underestimate cognitive load and emotional frustration, making them unreliable proxies for any research question centered on user wellbeing, emotional response, or stress
- AI usability testing is most appropriate as a preliminary screening tool -- to identify obvious interface failures before recruiting human participants -- rather than a standalone evaluation method
- The paired design is a methodological contribution: comparing individual AI to matched individual human is more rigorous than comparing aggregated AI outputs against aggregated human panels

## Limitations & Critiques
Small sample (n=10) limits quantitative generalizability; Looma.ai is a custom testbed, not a real-world commercial application, which may not capture the complexity of genuine UX contexts; sample is entirely students; the AI framework (web-ui + GPT-4o) is one specific architecture and results may vary with other agent systems; Bonferroni correction may have been overly conservative given sample size.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Synthetic Heuristic Evaluation AI vs Human-Powered Usability (Zhong et al., 2025)]] - related synthetic evaluation study
