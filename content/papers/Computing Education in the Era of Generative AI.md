---
source_file: Computing Education in the Era of Generative AI.pdf
type: paper
authors: Paul Denny, James Prather, Brett A. Becker, James Finnie-Ansley, Arto Hellas,
  Juho Leinonen, Andrew Luxton-Reilly, Brent N. Reeves, Eddie Antonio Santos, Sami
  Sarsa
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
This article from Communications of the ACM examines the challenges and opportunities that generative AI, particularly large language models (LLMs) like ChatGPT and GitHub Copilot, presents for computing education. The authors evaluate the performance of code-generation models on typical introductory programming problems, finding that these tools can solve many problems at or above student performance levels, which raises significant concerns about academic integrity, student over-reliance, and the fundamental structure of programming pedagogy.

The paper documents how Codex (the model powering Copilot) scored in the top quartile when tested on actual student exams, and GPT-4 achieved 99.5% and 94.4% on the same exams. The authors explore challenges including academic misconduct detection, learner over-reliance on AI suggestions, bias in generated code, security vulnerabilities, and the appropriateness of AI-generated code for beginners. They also identify opportunities including the generation of novel programming exercises, code explanations, improved error messages, and new pedagogical approaches that leverage these tools.

The authors argue that while AI tools present significant challenges, computing educators must embrace these changes and teach students to use these tools responsibly from the beginning of their education, as the tools will be integral to professional software development.

## Key Concepts
- **Large Language Models (LLMs)**: Neural network-based models trained on vast quantities of text data capable of generating human-like prose and source code from natural-language prompts
- **Code Generation**: The ability of AI models to synthesize source code from natural language problem descriptions
- **Learner Over-reliance**: The risk that students using AI code-completion tools may become accustomed to auto-suggested solutions and fail to develop metacognitive skills
- **Prompt Engineering**: The emerging skill of crafting effective prompts to guide AI models to produce correct code solutions
- **Academic Integrity**: The challenge of detecting and categorizing AI-assisted work in programming assessments

## Theoretical Framework
The paper draws on:
- Computing education research on evidence-based pedagogy
- Literature on metacognition and computational thinking development
- Research on academic integrity and plagiarism detection
- Studies on code quality, security, and professional software development practices

## Methods
The authors synthesized findings from multiple empirical studies:
1. Testing Codex on real student exam questions from two Python CS1 courses (71 students, 2020), finding it ranked 17th (top quartile)
2. Replication study with GPT-4 under identical conditions showing 99.5% on Exam 1 and 94.4% on Exam 2
3. Generation of 350 code variations for the "Rainfall problem" to test consistency and diversity of solutions
4. Analysis of 240 generated programming exercises evaluating sample solutions and test cases
5. Evaluation of code explanations for completeness (90%) and correctness (70%)

## Main Arguments
- LLMs can reliably solve many introductory programming problems, fundamentally challenging traditional assessment approaches
- Instructors must be extremely clear about when and how generative AI tools are allowed on assessments
- Common plagiarism detection tools are often ineffective against AI-generated solutions
- Over-reliance on AI tools may hinder the development of crucial metacognitive and computational thinking skills
- AI-generated code may be too advanced or complex for novices, using concepts outside the curriculum
- Security vulnerabilities in AI-generated code are a significant concern, and novice programmers lack the knowledge to identify them
- LLMs offer substantial opportunities for generating personalized learning resources, exercises, and explanations
- New pedagogical approaches should emphasize problem decomposition, specification writing, and code evaluation skills
- Teaching students to work effectively with AI code generators is becoming an essential skill
- The ability to understand, modify, and debug code will remain fundamental even as AI handles more code generation

## Limitations & Critiques
- Performance benchmarks were conducted on specific exam types and may not generalize to all programming contexts
- 11% of Python solutions from AlphaCode were syntactically incorrect, and 35% of C++ solutions did not compile
- As many as 20% of introductory programming problems are not solved sufficiently by current code-generation models
- AI-generated code can contain bias and harmful stereotypes in comments and variable names
- The field is evolving so rapidly that recommendations may quickly become outdated
- Long-term impacts on student learning outcomes remain unclear
- The paper acknowledges that natural language may become "too imprecise" for specifying complex programs
