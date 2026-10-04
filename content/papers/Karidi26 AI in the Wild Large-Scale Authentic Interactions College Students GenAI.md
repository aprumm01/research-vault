---
source_file: AI in the Wild A Large Scale Analysis of Authentic Interactions of College
  Students with Generative AI.pdf
type: paper
authors: Taelin Karidi, Ofra Amir, Ido Roll
community: HCI Education and Pedagogy
tags: null
year: 2026
builds_on:
- '[[frameworks/Cognitive Load]]'
- '[[concepts/AI Literacy Dimensions]]'
critiques: []
tensions_with:
- '[[concepts/Technological Determinism]]'
supports:
- '[[concepts/AI Literacy Dimensions]]'
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Human-in-the-Loop Pedagogy]]'
key_claims:
- Student-AI interaction in authentic academic settings is highly structured rather
  than idiosyncratic, concentrating in a small number of recurring patterns shared
  across many students and conversations
- Systematic differences across courses give rise to distinct interaction profiles
  that reflect the nature of academic work (mathematical problem-solving vs. writing
  vs. conceptual analysis) rather than individual student preferences
- Analysis of over 15,000 student-AI interaction units from 821 students reveals that
  authentic 'in-the-wild' data shows interaction patterns that would not emerge in
  controlled experimental settings
- The concentration of interactions in recurring patterns suggests that targeted pedagogical
  interventions designed around common interaction types could be more effective than
  general AI literacy education
- The two-dimensional analytical framework (cognitive intent × interaction context)
  captures meaningful variation in how students engage with GenAI that single-variable
  frameworks miss
methodology: '[[methods/Mixed Methods]]'
sample_size: 821
sample_type: undergraduate students across multiple courses
context: Six university courses spanning diverse academic domains (English, Complex
  Functions, Fourier Analysis, Intelligent Systems, Organizational Behavior, Probability)
  at Technion, Israel
study_type: empirical
---

# AI in the Wild: A Large Scale Analysis of Authentic Interactions of College Students with Generative AI

## Summary
This paper presents a large-scale analysis of naturally occurring student-AI interactions collected from undergraduate students across multiple university courses and academic domains at the Technion (Israel Institute of Technology). Analyzing over 15,000 student-AI interaction units drawn from voluntary, authentic coursework use, the study characterizes interactions along two dimensions—cognitive intent (Bloom level) and interaction context—and finds that student-AI interaction is highly structured, concentrating in a small number of recurring patterns while exhibiting systematic differences across courses. Published in AIED 2026 proceedings.

## Key Concepts
- **Authentic interaction data**: Log data from voluntary real-world GenAI use during actual coursework, contrasted with controlled experimental settings or retrospective surveys
- **Cognitive intent dimension**: The Bloom's taxonomy level expressed in student requests (e.g., remembering, understanding, applying, analyzing), capturing the learning objective behind each AI query
- **Interaction context dimension**: How students position the AI relative to their own work, the task itself, or prior AI output—distinguishing task-directed, work-directed, and AI-directed interactions
- **Interaction profiles**: Distinct patterns of AI use that emerge across courses, reflecting differences in academic work type rather than individual student idiosyncrasies
- **Instruction-guided annotation**: A scalable annotation approach using AI models with explicit instructions to classify large conversation datasets against learning science constructs
- **Concentration in recurring patterns**: The finding that student-AI use, despite apparent variety, clusters in a small number of reusable interaction types across students and conversations
- **Cross-course variation**: Systematic differences in interaction profiles across courses that reflect the nature of academic tasks (writing vs. mathematics vs. organizational analysis) rather than random individual variation

## Theoretical Framework
The study is grounded in learning analytics and educational research traditions showing that how learners use tools matters more than whether they have access to them. Drawing on AIED research on intelligent tutoring system interaction patterns, the paper conceptualizes student-AI conversations as structured sequences analyzable through established learning science frameworks. Bloom's taxonomy provides the cognitive intent dimension, while the interaction context dimension is an original analytical contribution of the paper.

The theoretical contribution is demonstrating that authentic student-AI interaction is not uniformly idiosyncratic but exhibits stable structural patterns that vary systematically with academic context. This finding challenges both pessimistic views (AI use as chaotic and random) and optimistic views (AI use as uniformly educationally beneficial), positioning interaction structure as a key mediating variable between tool access and learning outcomes.

## Methods
Large-scale log analysis of naturally occurring student-AI interactions collected from undergraduate students across six university courses spanning diverse academic domains (English, Complex Functions, Fourier Analysis, Intelligent Systems, Organizational Behavior, Probability) at Technion, Israel. The dataset comprises over 15,000 student-AI interaction units from 821 students. Instruction-guided annotation was applied at scale to classify each student turn along two dimensions: cognitive intent (Bloom level) and interaction context. Course participation varied: English (n=19), Complex Functions (n=275), Fourier Analysis (n=269), Intelligent Systems (n=55), Organizational Behavior (n=56), Probability (n=147). Presented at AIED 2026.

## Main Arguments
- Student-AI interaction in authentic academic settings is highly structured rather than idiosyncratic: interactions concentrate in a small number of recurring patterns that are shared across many students and conversations
- Systematic differences across courses give rise to distinct interaction profiles that reflect the nature of academic work (mathematical problem-solving vs. writing vs. conceptual analysis) rather than individual student preferences
- The two-dimensional analytical framework (cognitive intent × interaction context) captures meaningful variation in how students engage with GenAI that single-variable frameworks miss
- Authentic "in-the-wild" data reveals interaction patterns that would not emerge in controlled experimental settings, where student behavior is constrained by researcher design rather than real task demands
- The concentration of interactions in recurring patterns suggests that targeted pedagogical interventions—designed around common interaction types—could be more effective than general AI literacy education
- The finding that interaction profiles vary by course type has implications for curriculum design: educators can anticipate likely student-AI interaction patterns and design assignments to support more educationally productive forms of engagement

## Limitations & Critiques
The data was collected at a single institution (Technion) with a particular student population and academic culture; generalizability to other universities and national contexts is uncertain. The study focuses on interaction structure rather than learning outcomes, so the relationship between identified patterns and actual learning remains to be established. The sample sizes across courses are uneven (19 to 275 students), with the very small English course sample limiting confidence in cross-course comparisons.

The annotation framework, while applied at scale, relies on LLM-based classification that may introduce systematic errors in interpreting ambiguous student messages. The study also cannot distinguish between students who use AI voluntarily (represented in the dataset) and those who do not (excluded from analysis), potentially selecting for more engaged or AI-comfortable students.

## Connections
- [[communities/HCI_Education_and_Pedagogy]] - Research community
- [[methods/large_scale_log_analysis]] - Log-based interaction analysis
- [[frameworks/blooms_taxonomy]] - Cognitive classification of learning objectives
- [[frameworks/learning_analytics]] - Data-driven analysis of learner behavior
- [[methods/instruction_guided_annotation]] - Scalable AI-assisted coding methodology
