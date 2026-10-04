---
source_file: Computing Education in the Era of Generative AI.pdf
type: paper
authors: Paul Denny, James Prather, Brett A. Becker, James Finnie-Ansley, Arto Hellas,
  Juho Leinonen, Andrew Luxton-Reilly, Brent N. Reeves, Eddie Antonio Santos, Sami
  Sarsa
community: HCI Education and Pedagogy
tags: null
year: 2023
builds_on:
- '[[frameworks/Constructivism]]'
- '[[frameworks/Situated Cognition]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Illusion of Competence]]'
- '[[concepts/AI Tool Dependence]]'
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Process-centric Education]]'
- '[[concepts/Sustainable Assessment]]'
key_claims:
- AI models including Codex and GPT-4 can already solve most introductory programming
  (CS1) problems with high pass rates, fundamentally undermining the 'many small programs'
  pedagogy that has been a cornerstone of computing education for decades
- Students with greater prior knowledge are better positioned to use AI tools productively;
  uncritical adoption of AI in computing education risks widening achievement gaps
  between well-prepared and struggling learners
- Assessment in computing education must shift from take-home coding exercises to
  proctored exams, oral assessments, process-oriented assignments, and AI-proof tasks
  that require explanation and reflection
- LLMs enable instructors to generate exercise variations, code explanations, and
  error message enhancements at scale with quality comparable to student-generated
  resources, transforming learning resource creation efficiency
- New core competencies must be explicitly taught in computing curricula including
  prompt engineering, problem decomposition, critical evaluation of AI output, and
  the ability to recognize incorrect or insecure generated code
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: null
context: Computing education, primarily introductory programming courses (CS1/CS2)
  in English-language Western universities
study_type: review
---

# Computing Education in the Era of Generative AI

## Summary
This article examines the challenges and opportunities that large language models (LLMs) capable of generating source code present to computing educators, with a focus on introductory programming courses. Drawing on two foundational articles from 2022 as anchors, the authors synthesize emerging evidence about how AI code-generation tools are transforming both assessment and pedagogy. The paper argues that educators must adapt their strategies—updating what is taught, how it is assessed, and how learning resources are created—in response to AI tools that can already solve most introductory programming exercises.

## Key Concepts
- **LLM code generation**: Neural network models (e.g., Codex, GPT-4, GitHub Copilot) trained on vast code repositories that can synthesize working code from natural-language prompts
- **Academic integrity in CS education**: The challenge of distinguishing genuine student work from AI-generated solutions when AI can solve most introductory assignments
- **AI overreliance**: The risk that students accept AI-generated code without understanding it, creating surface-level learning and false competence
- **Prompt engineering as a skill**: The emerging pedagogical goal of teaching students to decompose problems and specify programming tasks accurately for AI systems
- **Automated exercise generation**: The use of LLMs to efficiently create customized, varied programming exercises and code explanations at scale
- **Many-small-programs pedagogy**: The traditional CS1 approach of assigning many small coding tasks, now disrupted because AI can trivially complete them
- **Metacognition in programming**: Self-regulation and problem-solving awareness that students must develop, and that AI tools may undermine if used as a crutch

## Theoretical Framework
The paper is grounded in computing education research (CER) traditions, specifically the evidence-based pedagogy of introductory programming (CS1/CS2). It frames the AI disruption through two lenses: (1) the affordances and constraints AI tools impose on traditional pedagogical structures, and (2) the opportunity to reconceptualize what computing literacy means when AI can handle routine code synthesis. The authors draw on Bommasani et al.'s foundation model literature to contextualize the societal magnitude of the shift, while situating their analysis within the specific learning science of novice programming.

The article does not adopt a single theoretical framework but uses an integrative review approach, synthesizing findings from benchmark studies of model performance on CS1 problems, educator response surveys, and early classroom adoption experiments. This positions it as a pragmatic policy-oriented synthesis rather than a theory-building paper.

## Methods
This is a research synthesis and perspective article published in Communications of the ACM, not an empirical study. The authors draw on two previously published benchmark papers (evaluating code-generating model performance on CS1 problems and on generating learning resources) and contextualize them with emerging empirical work, educator blog posts, SIGCSE workshop discussions, and classroom experiments. The synthesis covers model capability assessments, educator attitude surveys, and documented pedagogical innovations.

## Main Arguments
- **AI models can already solve most introductory programming problems**: Codex, GPT-4, and similar models achieve high pass rates on CS1 exercises, undermining the "many small programs" pedagogy that has been a cornerstone of computing education for decades.
- **Educators face an urgent dilemma between banning and integrating AI**: Responses range from prohibition (to preserve authentic assessment) to full integration (to prepare students for AI-augmented professional workflows), with no consensus having yet emerged.
- **Assessment must be redesigned**: Proctored exams, oral assessments, process-oriented assignments, and AI-proof tasks that require explanation and reflection are proposed as alternatives to take-home coding exercises.
- **AI tools enable scalable, personalized learning resource creation**: Instructors can use LLMs to generate exercise variations, code explanations, and error message enhancements far more efficiently than manual authoring, with quality comparable to student-generated resources.
- **New skills must be taught**: Prompt engineering, problem decomposition, critical evaluation of AI output, and the ability to recognize incorrect or insecure generated code are emerging competencies that computing curricula must explicitly address.
- **Equity concerns require attention**: Students with greater prior knowledge are better positioned to use AI tools productively; uncritical adoption risks widening achievement gaps between well-prepared and struggling learners.

## Limitations & Critiques
The article is a perspective piece rather than a primary empirical study, so its claims about educational impact are largely extrapolated from model performance benchmarks and early anecdotal classroom evidence rather than rigorous learning outcome research. The pace of AI development means that specific capability claims may be quickly outdated. The paper also focuses primarily on English-language, Western university contexts, leaving open questions about how the challenges differ in under-resourced or non-English educational environments.

The authors acknowledge that "the current pace of development in this area is staggering," which itself limits the durability of specific recommendations. The paper does not systematically address how the pedagogical recommendations could be implemented at scale in large introductory courses with limited TA support.

## Connections
- [[communities/HCI_Education_and_Pedagogy]] - Research community
- [[methods/Literature_Synthesis]] - if applicable
- [[frameworks/CS1_Pedagogy]] - if applicable
