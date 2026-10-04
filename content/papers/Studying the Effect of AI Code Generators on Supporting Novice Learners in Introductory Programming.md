---
source_file: Studying the effect of AI Code Generators on Supporting Novice Learners
  in Introductory Programming.pdf
type: paper
authors: Majeed Kazemitabaar, Justin Chow, Carl Ka To Ma, Barbara J. Ericson, David
  Weintrop, Tovi Grossman
community: HCI Education and Pedagogy
tags: null
year: 2023
builds_on:
- '[[frameworks/Cognitive Load]]'
- '[[frameworks/Constructivism]]'
- '[[frameworks/Situated Cognition]]'
critiques:
- '[[concepts/AI Tool Dependence]]'
tensions_with: []
supports:
- '[[concepts/Zone of Proximal Development with AI]]'
- '[[concepts/AI Augmentation]]'
- '[[concepts/Human-in-the-Loop Pedagogy]]'
key_claims:
- Codex group showed 1.15x higher completion rate, 1.8x higher correctness scores,
  0.59x fewer errors, and 0.57x less time on code-authoring tasks compared to baseline
  group
- AI access did not impair manual code-modification ability—both Codex and baseline
  groups performed similarly on code-modification tasks, suggesting AI users developed
  sufficient understanding
- Students with higher prior programming competency (Scratch scores) who had Codex
  access performed significantly better on one-week retention post-tests, suggesting
  AI tools amplify advantages for students with foundational knowledge
- Under structured learning conditions with educational scaffolding and progressive
  difficulty, AI code generation access did not create harmful dependency or impair
  learning retention
- Novice learners demonstrated understanding of AI-generated code through their ability
  to engage with, modify, and extend generated solutions in subsequent manual tasks
methodology: '[[methods/Controlled Experiment]]'
sample_size: 69
sample_type: novice learners ages 10-17 with no prior text-based programming experience
context: three-week programming camp using custom Python learning environment (Coding
  Steps)
study_type: empirical
---

# Studying the Effect of AI Code Generators on Supporting Novice Learners in Introductory Programming

## Summary
This CHI 2023 paper presents the first controlled experiment studying how AI code generators (OpenAI Codex) affect learning and retention for introductory programming novices. In a three-week study with 69 young learners (ages 10–17), students with Codex access significantly outperformed peers on code-authoring tasks during training, showed no degradation in manual code-modification ability, and performed similarly on post-tests — with tentative evidence that students with stronger prior knowledge benefited more on retention.

## Key Concepts
- **AI code generation vs. manual coding**: The experimental contrast between students who could generate Python code from natural language via Codex versus those who wrote code entirely manually
- **Generate-modify pattern**: The observed interaction where students use AI to generate initial code and then modify it — a core workflow that the study was designed to assess for learning implications
- **Code-authoring vs. code-modification**: The distinction between generating new code (where AI helps significantly) and modifying existing code (where both groups performed similarly), used to assess transfer of understanding
- **Learning retention**: Whether performance advantages from AI use persist when AI is removed, measured via a one-week post-test
- **Coding Steps**: The custom self-paced learning environment built for the study, incorporating novice-friendly documentation and progressively complex Python programming tasks
- **Prior programming competency**: Pre-study Scratch experience as a moderating variable — students with more prior competency showed greater retention benefits from Codex access

## Theoretical Framework
The study is grounded in cognitive and constructivist learning theories as applied to computer science education. The core theoretical question is whether AI scaffolding that reduces cognitive load during learning transfers into durable skill acquisition, or whether it creates a dependency that collapses when support is removed. This draws on debates about desirable difficulties in learning and the difference between performance (how well someone does with a tool) and learning (what they can do without it).

The natural language programming tradition within HCI also informs the design, framing Codex as a tool that bridges the gap between human natural-language thinking and formal programming syntax. The study contributes to ongoing HCI discussions about how to design educational interfaces that leverage AI affordances while preserving learning outcomes.

## Methods
Controlled experiment with 69 novice learners (ages 10–17, M=12.5, SD=1.8) with no prior text-based programming experience, recruited through a programming camp. Participants were randomly assigned to a Codex group (n=35) or a Baseline group (n=34). All students used Coding Steps, a custom self-paced Python learning environment. The study ran over three weeks with three phases: (1) a Scratch introduction and pre-test, (2) seven Python training sessions with 45 code-authoring tasks each followed by a manual code-modification task, and (3) an immediate post-test and a one-week retention test. Performance was measured by completion rate, correctness score, error rate, and completion time.

## Main Arguments
- **AI code generation significantly boosted code-authoring performance during training**: The Codex group showed 1.15x higher completion rate, 1.8x higher correctness scores, 0.59x fewer errors, and 0.57x less time compared to the Baseline group — demonstrating clear productivity benefits.
- **AI access did not impair manual code-modification ability**: On the code-modification tasks that followed each AI-generated solution, both groups performed similarly, suggesting that Codex users developed sufficient understanding to make manual changes.
- **Retention effects were positive but did not reach statistical significance**: On the one-week retention test, Codex group students performed slightly better on coding tasks and multiple-choice questions, but the difference was not significant — suggesting AI use at minimum does not harm retention.
- **Prior programming competency moderates the retention benefit**: Students with higher pre-study Scratch scores who had Codex access performed significantly better on retention post-tests, suggesting that AI tools may amplify advantages for students with foundational knowledge.
- **Novices demonstrated understanding of generated code**: Evidence from the code-modification tasks suggests students were not treating AI output as opaque black-box code — they could engage with it, modify it, and extend it.
- **The study challenges the overreliance narrative for structured learning contexts**: Under the conditions of this experiment (structured tasks, educational scaffolding, progressive difficulty), AI access did not create harmful dependency, though the authors note this may not generalize to less structured environments.

## Limitations & Critiques
The study population of 10–17 year olds at a programming camp may not generalize to university students or adult learners. The controlled environment with structured tasks and close supervision differs substantially from real classroom settings. The one-week retention interval is relatively short, and longer-term effects on sustained programming skill development remain unknown.

The Codex group showed slightly better retention, but the non-significant result means these findings are not definitive. The study does not examine higher-order programming skills (design, algorithm selection, debugging complex programs) — only introductory Python concepts. The custom Coding Steps environment may create artificial conditions that differ from commercial AI-integrated IDEs like Copilot.

## Connections
- [[communities/HCI_Education_and_Pedagogy]] - Research community
- [[methods/Controlled_Experiment]] - if applicable
- [[frameworks/Cognitive_Load_Theory]] - if applicable
