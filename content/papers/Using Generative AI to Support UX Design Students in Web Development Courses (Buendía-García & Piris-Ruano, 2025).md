---
source_file: Using Generative AI to Support UX Design Students in Web Development
  Courses.pdf
type: paper
authors: Félix Buendía-García, Javier Piris-Ruano
community: AI and Future of Work
tags: null
year: 2025
builds_on:
- '[[frameworks/Constructivism]]'
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Zone of Proximal Development with AI]]'
- '[[frameworks/Human-Centered Design]]'
- '[[concepts/Democratization of Design]]'
critiques: []
tensions_with:
- '[[concepts/AI Tool Dependence]]'
- '[[concepts/Illusion of Competence]]'
supports:
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Democratization of Design]]'
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/AI Augmentation]]'
- '[[concepts/Epistemic Agency]]'
key_claims:
- Structured prompt template skeletons with instruction-based benchmarks guide Creative
  Design students toward organized GenAI engagement strategies, reducing cognitive
  overload while maintaining creative control compared to unguided trial-and-error
  approaches
- Semantic similarity analysis reveals moderately high matching between student chat
  logs and task benchmarks (78% average for individual tasks, 90% average for group
  UI activities), demonstrating students follow instructions and complete academic
  tasks effectively with GenAI support
- 'GenAI effectiveness diminishes with increased task complexity: GitHub Copilot shows
  significant value for small-scale individual tasks but limited effectiveness for
  group activities requiring front-end/back-end coordination'
- Instructors observe decreased frequency of minor technical questions and students
  report reduced task completion time when using GitHub Copilot, indicating greater
  autonomous learning and freeing instructors for creative profile support
- 'Correlation between semantic similarity and academic performance varies by context:
  Template-Session task shows only 21% correlation between semantic similarity and
  task completion, while group UI activity achieves 60% correlation, suggesting difficulty
  in establishing direct link between GenAI interactions and performance'
methodology: '[[methods/Case Study]]'
sample_size: 21
sample_type: 3rd-year Design and Creative Technologies Bachelor's Degree students
context: Web Applications course, 2nd semester 2024-2025, Universitat Politècnica
  de Valencia Arts School
study_type: empirical
---

# Using Generative AI to Support UX Design Students in Web Development Courses

## Summary
This work explores the integration of Generative AI (GenAI) tools into web development educational settings, with a focus on enhancing the user experience (UX) design process and supporting students with limited technical backgrounds The democratization of GenAI has allowed non-technical users to engage in the creation of computing applications However, its adoption among UX-focused learners remains limited.

## Key Concepts
- **AI4WD Framework**: Artificial Intelligence for Web Development framework using prompt-engineering strategy and GitHub Copilot to guide UX design students through incremental web development tasks with structured instruction benchmarks
- **Scaffolded Prompt Templates**: Incremental interaction mechanisms providing task instructions organized as prompt skeletons (preamble, structure, style, interaction, content) enabling systematic GenAI tool engagement rather than disordered "trial and error" approaches
- **Benchmark-Based Assessment**: Rubric-driven evaluation comparing student chat.json logs against instructor-defined benchmarks using semantic similarity measures (LSA), term frequency analysis (TF-IDF), and task completion rates
- **Hybrid Designer-Developer Role**: Creative Technology students combining artistic skills with basic programming knowledge, positioned to bridge UX design and web development through GenAI tool support addressing traditional technical barriers
- **End-User Development Democratization**: GenAI tools enabling non-technical users to actively participate in development processes, moving beyond Low-Code Development Platforms (LCDPs) to engage directly with front-end and back-end programming tasks
- **Chat Log Analysis Pipeline**: Multi-stage data processing using Python/R scripts for filtering, translation, lemmatization (udpipe), Document-Term Matrix construction, and Latent Semantic Analysis to extract nouns/verbs representing student-AI interactions
- **Front-End/Back-End Integration Challenge**: Complex group activities requiring coordination between UI designers and database programmers, representing limitation of GenAI effectiveness as task complexity increases beyond small-scale individual work
- **Formative vs. Summative Assessment Split**: Ethical consideration distinguishing AI-assisted activities evaluated formatively from summative assessments, addressing concerns about extent to which academic grades should reflect GenAI tool contributions
- **Template-Session Task**: Representative individual activity combining PHP template development (header, hero section), user authentication (login modal), and session management (username display, logout) as structured learning progression
- **Decreased Instructor Intervention**: Observed reduction in minor technical questions from students using GenAI tools, suggesting increased learning autonomy while freeing instructors for creative profile support

## Theoretical Framework
**End-User Development and GenAI Integration**: Grounded in end-user development literature (Barricelli et al., 2022 systematic mapping; Paternó, 2023 on AI contributions) addressing how GenAI democratizes computing application creation for non-technical users. Framework positions against traditional Low-Code Development Platforms (LCDPs) by enabling direct programming participation rather than visual abstraction (Sahay et al., 2020).

**Designer-Developer Collaboration**: Built on cooperation frameworks between UX designers and developers (Ferreira et al., 2011; Pacheco et al., 2021 on LCDP collaboration efficiency). Addresses hybridization phenomenon in web design/development roles (Zhang et al., 2025 comprehensive review of designer-developer challenges/opportunities), particularly relevant for Creative Design degree curriculum combining artistic and technological skills.

**LLM-Based Code Generation in Education**: Informed by systematic reviews of LLMs in computer science education (Raihan et al., 2025) and navigating generative AI revolution in computing education (Prather et al., 2023). Builds on research examining GenAI benefits/harms for novice programmers (Kazemitabaar et al., 2024; Prather et al., 2024 on widening gap) and pitfalls of LLMs as coding assistants (Pirzado et al., 2024).

**Incremental Prompt Engineering**: Methodological foundation from iterative refinement approaches including Calo & de Russis (2024) on predefined templates for LLM website generation, Kodless tool's prompt refinement process (Voronin, 2024), and rapid code development through prompt configuration and self-debugging (Li et al., 2024). Addresses gap identified by Lu et al. (2022) regarding AI tools neglecting design-thinking-oriented views.

## Methods
**Case Study Context**: Web Applications (WA) course, 2nd semester 2024-2025, Design and Creative Technologies Bachelor's Degree, Universitat Politècnica de Valencia Arts School. N=21 students in 3rd year. Course structure: (1) server infrastructure/CMS basics, (2) individual activities with precise instructions and rubrics, (3) collaborative final web project. Prerequisite background: Processing-based Programming Basics (1st year), Interactive Media HTML/CSS/JavaScript (2nd year), elective UI Design/Web Design (3rd year first semester).

**Teaching Method Innovation**: Traditional lecture-lab approach adapted to integrate GitHub Copilot (GC) and ChatGPT-4. Individual activities structured with assessment rubric criteria (6 criteria graded A-D, 100-0%) serving dual purpose: (1) informing students of evaluation standards, (2) guiding iterative prompt formulation. Example Template-Session task rubric: page structure, multimedia content, graphical interface, private access, session management, content interaction. Instructions designed to scaffold prompt templates rather than provide mechanical prompt sequences.

**GenAI Interaction Framework (AI4WD)**: Three-pillar structure: (1) Prompt template skeleton provision - students complete skeleton with own contributions using ChatGPT/GC; (2) GitHub Copilot integration via Visual Code chat extension with JSON export/import capability enabling interaction tracking; (3) Benchmark development from task instructions for comparison analysis. Initial ChatGPT exploration using mockup-based prompt templates (Table 2 categories: preamble, structure, style, interaction, content) with n=9 students.

**Data Collection Procedures**: GC chat logs exported as chat.json format containing user prompts and generated code/reports. Manual export process employed despite significant time investment. Student interactions gathered across: Template-Session individual task (n=11 responses), UI access to data group activity (n=7), database operations group activities (n=7), CRUD operations final project/test (high complexity, multiple hours, error-heavy logs).

**Analysis Pipeline**: (1) Filtering stage: Python 3.9 scripts converting chat.json to MarkDown, regex extraction of student requests, English translation and summarization; (2) Annotation stage: R/Python loading udpipe trainable pipe model for text annotation extracting lemmatized nouns/verbs; (3) Vectorization stage: DTM (Document-Term Matrix) construction with TF-IDF scoring for meaningful term retrieval; (4) Semantic analysis stage: LSA (Latent Semantic Analysis) for term relationship graphing and semantic similarity computation between student logs and benchmarks (adapted Python script).

**Supplementary Evaluation**: (1) Usability testing: Interactive Communication Projects (ICP) 4th-year students (n=27) evaluating WA web prototypes (n=7 projects, 3-5 evaluations each) using 7-item questionnaire (aesthetics, structure, navigation, interaction, purpose, recognition, interest, style); (2) Student perception questionnaire: WA students (n=14) rating GenAI application across 4 categories (suitability, ease of prompts, usefulness of answers, trust in answers) plus 5 additional items (support, improvement, applicability, proficiency, continuity).

## Main Arguments
- **Structured Scaffolding Enables Systematic GenAI Engagement**: Prompt template skeletons and instruction-based benchmarks guide Creative Design students toward organized prompting strategies, evidenced by term relationship graphs and frequency analysis showing closer alignment to benchmarks compared to unguided "trial and error" approaches, reducing cognitive overload while maintaining creative control
- **Semantic Similarity Validates Learning Alignment**: LSA-based comparison between student chat logs and task benchmarks reveals moderately high matching (78% average for Template-Session individual task, 90% average for group UI activity), demonstrating students follow provided instructions and complete academic tasks effectively with GenAI support
- **Task Complexity Determines GenAI Effectiveness**: GitHub Copilot demonstrates significant value for small-scale individual tasks (code generation, code explanation, bug fixing), but effectiveness diminishes with increased complexity in group activities requiring front-end/back-end coordination, revealing need for collaborative AI-supported mechanisms and more sophisticated prompt organization
- **Correlation Between Semantic Similarity and Performance Varies**: Template-Session task shows low correlation (21%) between semantic similarity and task completion percentages, while group UI activity achieves higher correlation (60%), suggesting direct link between GenAI interactions and academic performance is difficult to establish and context-dependent
- **Autonomous Learning Increases with GenAI Integration**: Instructors observe decreased frequency of minor technical questions and students report reduced time to complete tasks when using GC, indicating greater autonomy in learning processes and freeing instructors for creative profile support rather than basic technical troubleshooting
- **Moderate Student Acceptance Despite Utility**: Usability testing by external students shows web prototypes achieve close to 80% satisfaction in aesthetics/structure/navigation (lower for interaction), but WA students provide only 62% positive agreement on GenAI suitability in course context, with none of four assessed categories reaching 80% agreement, revealing perception-utility gap
- **Benchmark Approach Enables Formative Assessment**: Task instruction benchmarks provide suitable instrument for assessing GenAI impact through multiple measurements (term frequency counts, semantic similarity, completion rates) while addressing ethical concerns by distinguishing AI-assisted formative evaluation from summative assessment methods
- **Hybridization Opportunity Exists with Pedagogical Framing**: GenAI tools can democratize web development access for traditionally marginalized learners with technical barriers, positioning tools as catalysts for designer-developer role convergence when integrated with careful pedagogical framing, collaborative task design, and critical engagement rather than just coding assistants

## Limitations & Critiques
- **Small Sample Size and Single Institution**: Study limited to n=21 students in one course at single university (UPV), constraining generalizability across different educational contexts, student populations, or degree programs; individual task analyses with n=11 and group activities with n=7 responses insufficient for robust statistical conclusions
- **Manual Data Collection Burden**: Chat log export from GitHub Copilot requires manual procedures entailing "significant time investment," limiting scalability and preventing real-time or frequent assessment; automatic collection methods needed for more effective evaluation and broader implementation
- **Limited Collaborative Activity Assessment**: Study acknowledges "collaborative use of GenAI tools is beyond scope of current research" and difficulty differentiating individual group member interactions in chat logs, representing critical gap given emphasis on designer-developer coordination and team-based web projects as core course component
- **Weak Correlation Evidence**: Template-Session task shows only 21% correlation between semantic similarity and task completion, undermining claim that semantic similarity serves as valid proxy for learning outcomes or academic performance; suggests measurement approach may capture process but not mastery
- **Complex Task Failure Analysis Incomplete**: CRUD operations activity characterized by "multiple error issues" and student interactions "difficult to track," but study provides minimal analysis of failure patterns, error recovery strategies, or how to improve GenAI support for complex tasks beyond general observation that "careful prompt organization" needed
- **Benchmark Validity Unexamined**: Instructor-created benchmarks treated as gold standard without validation against professional web development standards, expert review, or alternative reference implementations; no inter-rater reliability or discussion of how benchmark quality affects assessment validity
- **Short-Term Evaluation Only**: Study covers single semester (2nd semester 2024-2025) without longitudinal tracking of skill development, retention, transfer to subsequent courses, or professional practice; unclear whether scaffolded approach builds foundational skills or creates dependency on structured guidance
- **Overreliance and Reflection Concerns Mentioned but Not Measured**: Conclusion acknowledges "issues of overreliance on these tools or lack of reflection" as pitfalls students could fall into, but study includes no instruments measuring these critical concerns or strategies for mitigating dependency risks
- **Limited Comparison Conditions**: No control group without GenAI tools, no comparison across different GenAI platforms, no A/B testing of alternative scaffolding approaches; impossible to isolate GenAI effects from other pedagogical innovations or instructor attention
- **External Validity of Usability Testing**: ICP students testing WA prototypes represent convenience sample from same institution with potential bias; no comparison to non-student users, professional developers, or authentic end-users; 3-5 evaluations per project insufficient for reliable usability assessment
- **Student Perception Questionnaire Limitations**: Only n=14 of n=21 students completed perception survey (67% response rate); four assessment categories show low agreement (none reaching 80%), but no qualitative follow-up explores reasons for moderate satisfaction despite demonstrated utility; potential response bias from voluntary participation
- **Technology Dependency Risk**: Outcomes entirely dependent on GitHub Copilot and ChatGPT-4 specific implementations, pricing models, and feature availability; reproducibility threatened by platform changes, access restrictions, or tool evolution; ChatGPT lacking easy export mechanisms noted as limitation but not addressed
- **Ethical Assessment Framework Incomplete**: While acknowledging need to distinguish formative vs. summative assessment regarding AI-assisted work, study provides no concrete guidelines, policies, or validation of assessment approach fairness; intellectual property and authorship questions unaddressed
- **Missing Skill Transfer Evidence**: Study does not examine whether students can complete similar tasks without GenAI support after scaffolded learning period, raising questions about whether approach develops transferable programming competencies or tool-specific procedural knowledge
- **Curriculum Integration Challenges**: While mentioning broader degree context (four-year timeline), study does not address how AI4WD framework integrates with other courses, whether skills build across semesters, or how to prepare instructors in other Computing/Art departments for consistent implementation

## Related Papers
- [[papers/Reflecting on the Integration of Generative AI in Design Education]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/Activity theory as framework for analysis of workplace learning technologies The]]
- [[papers/AI-assisted Learning in HCI Education Opportunities and Dilemmas from a Student ]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 CHI]]
## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
