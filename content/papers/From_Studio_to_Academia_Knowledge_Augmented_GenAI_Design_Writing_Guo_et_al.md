---
source_file: "From the Studio to Academia Design and Evaluation of a Knowledge-Augmented GenAI System to Empower Design Undergraduates_ Design Research Writing.pdf"
type: paper
authors: "Wenchen Guo, Yiyang Zhang, Huizi Han, Hailiang Wang"
community: "AI in Design Education"
tags:
---

# From the Studio to Academia: Design and Evaluation of a Knowledge-Augmented GenAI System to Empower Design Undergraduates' Design Research Writing

## Summary
This paper addresses a specific gap: design undergraduates possess strong visual intuition but struggle to translate tacit design knowledge into rigorous academic argumentation. The authors built and evaluated a domain-specific, knowledge-augmented GenAI system using Retrieval-Augmented Generation (RAG) and persona-based prompting to scaffold design research writing. A quasi-experimental study comparing student papers before and after the system's introduction found improvements in problem definition and analytical quality, though methodological execution remained limited. Students' needs evolved from seeking answers to seeking scaffolding for critical thinking.

## Key Concepts
- **Retrieval-Augmented Generation (RAG)**: A technical architecture where the AI system grounds responses in a curated, high-quality knowledge base rather than general training data—reducing hallucinations and domain-irrelevant outputs
- **Knowledge-Augmented GenAI**: A domain-specific system architecture that embeds course-specific academic resources, enabling disciplinary specificity rather than generic writing assistance
- **Persona-Based Prompting**: A prompt design strategy where the system adopts a defined role (academic tutor for design research) with guardrails to maintain focus and integrity
- **Disciplinary Specificity**: The principle that effective GenAI writing support must be grounded in the specific knowledge structures, research paradigms, and epistemic norms of the target discipline
- **Pedagogical Scaffolding**: The system's orientation toward guiding the writing process stage-by-stage rather than directly generating final text—preserving cognitive effort while reducing friction
- **Tacit-to-Explicit Translation**: The core learning challenge for design students—transforming implicit visual intuition and studio-based knowledge into explicit, defensible academic logic
- **Academic Integrity Guardrails**: System architecture that filters irrelevant queries, refuses non-design tasks, and strictly adheres to an academic tutor persona to maintain appropriate use

## Theoretical Framework
The study draws on HCI and educational technology literature on AI-assisted academic writing, extending this work to the underexplored domain of design education with its distinctive epistemic challenges. The authors identify three design principles: disciplinary specificity (domain-grounded outputs to mitigate hallucination), pedagogical scaffolding (process-oriented rather than product-oriented assistance), and integrity and relevance (guardrails maintaining academic appropriateness). These principles are operationalized through a three-layer system architecture: Orchestration Layer (intent recognition), RAG Layer (knowledge retrieval), and LLM Presentation Layer (output generation).

The quasi-experimental design treats the 2023 cohort (pre-AI) as a baseline and the 2025 cohort (with the RAG system) as the experimental condition, using expert blind review to evaluate paper quality across multiple dimensions.

## Methods
Quasi-experimental between-subjects design comparing 10 papers from two cohorts in a Design Research Methods course at Hong Kong Polytechnic University: Control Group (N=5, 2023/2024 cohort, no AI assistance) and Experimental Group (N=5, 2025/2026 cohort, using the custom GenAI system). Ten experts conducted double-blind reviews of the papers, evaluating problem definition, analytical quality, methodological execution, and writing quality. Six students from the 2025 cohort participated in semi-structured interviews to provide qualitative insight into system use experiences and perceived value.

## Main Arguments
- Domain-specific, knowledge-augmented GenAI systems outperform generic models for design research writing—specifically by reducing hallucinations, providing discipline-relevant guidance, and supporting the distinct cognitive challenge of translating design intuition into academic argument
- The 2025 cohort showed stronger performance in problem definition and analytical quality compared to the 2023 baseline, providing empirical evidence for the scaffolding effect of the knowledge-augmented system
- Students' needs evolved significantly during system use: they began by seeking direct answers ("write this for me") but progressively shifted toward seeking scaffolding for their own thinking ("help me think through this argument")—a developmental trajectory the system supported
- Methodological execution showed limited improvement, suggesting that even domain-specific GenAI systems have boundaries: students still struggled with research design decisions that require deep methodological training rather than knowledge retrieval
- Students valued two unexpected dimensions: accuracy (confidence that system responses were grounded in actual design research literature) and emotional support (reduced anxiety about academic writing conventions)
- The paper provides a model for how to build appropriate GenAI writing support: not a general-purpose tool, but a carefully designed system with domain-specific knowledge, pedagogical scaffolding logic, and integrity guardrails

## Limitations & Critiques
The extremely small sample (N=10 total papers, N=6 interviews) severely limits statistical power and generalizability. The quasi-experimental design cannot rule out cohort differences unrelated to the AI system—the 2025 students may differ from the 2023 cohort in ways that account for performance gains. The focus on a single course (Color Research) in one discipline (Product Design) limits disciplinary breadth. All papers passed AI-detection protocols, but the boundary between AI-scaffolded and AI-generated work remains philosophically contested.

The system required significant development investment (curated knowledge base, custom architecture) that may be infeasible for most institutions without dedicated technical and faculty resources.

## Connections
- [[communities/AI in Design Education]] - Research community
- [[methods/Quasi-Experimental_Expert_Review]] - Between-subjects design with blind expert evaluation
- [[frameworks/Retrieval_Augmented_Generation]] - RAG technical architecture
- [[frameworks/Pedagogical_Scaffolding]] - Process-oriented writing support
