---

source_file: "research_docs/P463.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Lu et al"
---

# UXAgent: A System for Simulating Usability Testing of Web Design with LLM Agents (Lu et al., 2025)

## Summary
Lu, Yao, Gu, Huang, Wang, Li, Gesi, He, Li, and Wang (Northeastern University and Amazon) present UXAgent, an open-source system for generating LLM agents as usability testing participants at scale, then running simulated interactions with real-world web environments. The system includes a Persona Generator (creating thousands of diverse user personas), an LLM Agent module (dual-process reasoning: fast perceptual actions + slow reflective loops), and a Universal Browser Connector (interacting with live web pages via Chrome). A Result Viewer presents action traces, reasoning traces, post-study surveys, and video recordings for UX researcher analysis. Agents can also be interviewed directly mid-session to simulate contextual inquiry. A heuristic evaluation with 16 UX researchers praised the innovation but raised concerns about reliability and the future of UX practice if LLM agents displace human participants.

## Key Concepts
- Persona Generator: automated creation of thousands of demographic-diverse user personas
- Dual-process agent architecture: fast perceptual actions + slow reflective reasoning loops
- Universal Browser Connector: live Chrome interaction with real websites (not sandbox)
- Result Viewer: multi-modal output including action traces, reasoning traces, post-study surveys, video
- Contextual inquiry simulation: UX researcher can interview agents mid-task
- Pre-study validation use case: evaluating study design before real human-subject deployment

## Theoretical Framework
LLM agent and autonomous agent research (Park et al., WebVoyager, ReAct); Dual Process Theory applied to agent architecture; UX usability testing methodology; addresses limitations of prior sandbox-only systems; contrasted against computer-using agent systems (OpenAI Operator, Claude computer use); built on earlier short version (CHI EA '25) extended into full system paper; affiliated with Northeastern University and Amazon.

## Methods
System architecture design and implementation; Persona Generator creates demographic distributions; agents interact with real web pages via Universal Browser Connector (Playwright/Chrome); data collected as multi-modal logs; heuristic evaluation with 16 UX researchers assessing the system's utility, innovation, and concerns; participants tested the system against real websites and provided structured feedback; thematic analysis of researcher concerns and praise.

## Main Arguments
- Current usability study design is itself undervalidated: UX researchers focus on the feature being tested but rarely pilot-test the study design itself; UXAgent allows pre-study validation of the study design against simulated participants before costly human-subject recruitment
- The Universal Browser Connector is a key architectural contribution: by interacting with live web pages rather than sandboxed simulations, UXAgent produces behavioral data in ecologically valid conditions that prior systems cannot achieve
- The dual-process agent architecture produces more human-like interaction behavior than simpler reasoning systems by separating fast perceptual action (clicking, scrolling) from slow reflective loops (goal assessment, feedback generation)
- The 16 UX researcher evaluation reveals a fundamental tension: the system is seen as innovative and potentially transformative, but UX researchers worry that normalizing LLM agent-based testing could devalue the practice of engaging with real human users and misrepresent diverse user experiences

## Limitations & Critiques
No systematic validation against real human usability testing outcomes; heuristic evaluation with 16 researchers is formative feedback, not a rigorous controlled comparison; the system cannot simulate accessibility needs, emotional reactions, or cultural contextual behaviors; agent behavior may correlate across agents sharing similar model weights, reducing true behavioral diversity; the $250 shopping scenario from related papers shows directional but not precise alignment with human behavior.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Heuristic Evaluation]] - `` [EXTRACTED]
- [[Behavioral Trace Analysis]] - `` [EXTRACTED]
- [[Agent AB Automated and Scalable AB Testing on Live Websites with LLM Agents (Lu et al., 2025)]] - companion system from overlapping author team
- [[Evaluating Trustworthiness of AI Personas in Paired Usability Testing (Huang, 2025)]] - empirical validation study citing this system
