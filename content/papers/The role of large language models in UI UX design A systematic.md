---
source_file: The role of large language models in UI_UX design_A systematic.pdf
type: paper
authors: Ammar Ahmed,Ali Shariq Imran
community: GenAI in UX and Design Practice
tags: null
year: 2024
builds_on:
- '[[frameworks/Human-Centered Design]]'
- '[[frameworks/Design Thinking]]'
- '[[concepts/Human-AI Co-creation]]'
critiques: []
tensions_with:
- '[[concepts/AI Tool Dependence]]'
- '[[concepts/De-skilling]]'
supports:
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Human-in-the-Loop Pedagogy]]'
- '[[concepts/AI Augmentation]]'
- '[[concepts/Democratization of Design]]'
- '[[concepts/AI Hallucinations]]'
- '[[concepts/Design Fixation]]'
- '[[concepts/Explainable AI]]'
- '[[concepts/Creativity Support Tools]]'
key_claims:
- GPT-4 emerged as the most widely adopted model for UI/UX tasks due to strong performance
  in structured UI generation, chain-of-thought reasoning, and multimodal input support
- LLMs function most effectively as co-creators rather than autonomous agents, requiring
  continuous designer oversight through a dialogic interaction model rather than hierarchical
  command-execution
- Prompt engineering has evolved from technical workaround to iterative creative practice
  and central cross-cutting skill, with designers treating prompts as iterative artifacts
  similar to sketches or wireframes
- LLM outputs tend to converge on generic or conservative design patterns, potentially
  limiting creative exploration and causing designers to become anchored to AI-generated
  suggestions too early
- Wide practice variation from polished plugins to bespoke systems to ad hoc prompting
  indicates the field has not yet converged on standardized workflows, tooling, or
  evaluation criteria, signaling field immaturity
- Multimodal vision-language models understanding what users see, touch, and navigate
  through enables design support responsive to spatial and semantic context in AR,
  VR, and mobile scenarios
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: Academic literature from ACM Digital Library, IEEE Xplore, and Scopus
  databases
context: Systematic review of LLM applications in UI/UX design research
study_type: review
---

# The role of large language models in UI UX design A systematic

## Summary
Keywords: Large Language Models (LLMs) UI/UX Design Human-AI Collaboration Prompt Engineering Generative AI in Design This systematic literature review examines the role of large language models (LLMs) in UI/UX design,.

## Key Concepts
- **GPT-4 as Dominant LLM in Design**: GPT-4 emerged as most widely adopted model for UI/UX tasks due to strong performance in structured UI generation, chain-of-thought reasoning, and multimodal input support
- **Human-in-the-Loop Integration**: LLMs function most effectively as co-creators rather than autonomous agents, requiring continuous designer oversight to validate, edit, and refine outputs
- **Prompt Engineering as Design Discipline**: Prompting has evolved from technical workaround to iterative creative practice, using strategies like chain-of-thought reasoning, modular prompts, and few-shot learning
- **Multimodal Context-Awareness**: Combining textual task descriptions with UI screenshots, visual design datasets, and contextual variables produces more accurate and situationally-aware outputs
- **Design Lifecycle Integration**: LLMs applied across full design process including research and discovery (persona generation, interview synthesis), ideation (brainstorming, concept remixing), generation (mockup/code creation), prototyping (HTML/CSS generation, user simulation), evaluation (heuristic critique, accessibility checking), and iterative refinement
- **Modular Task Decomposition**: Breaking UI/UX tasks into smaller, interpretable modules (e.g., separate agents for planning, inspection, debugging) improves reliability, control, and explainability
- **Trust Through Transparency**: Explainability mechanisms including confidence scoring, bias indicators, source attribution, and visual feedback for error localization increase user trust and reduce hallucination risks
- **Tool Ecosystem Integration**: Embedding LLMs within existing design environments (Figma, Google Meet, visual programming interfaces) facilitates smoother adoption and minimizes workflow disruption

## Theoretical Framework
- **Systematic Literature Review Methodology**: Follows Kitchenham guidelines for conducting systematic reviews with defined research questions, search strategy, screening procedures, and data extraction protocols
- **PRISMA Flow Diagram**: Structured selection process across ACM Digital Library, IEEE Xplore, and Scopus databases with relevance-based cutoff strategy
- **Design Lifecycle Mapping Framework**: Organizes LLM integration across stages (research/discovery, ideation, generation, prototyping/simulation, evaluation/feedback, iterative refinement, reflection/ethics)

## Methods
literature review

## Main Arguments
- **LLMs as Design Collaborators**: Review demonstrates shift from hierarchical interaction model (designer commands, AI executes) to dialogic model (designer and AI iterate together), positioning LLMs as active co-creators rather than mere efficiency tools
- **Six Best Practice Themes**: Effective LLM integration clusters around prompt engineering, human-in-the-loop iteration, tool integration, modularity, multimodal context-awareness, and trust/evaluation mechanisms
- **Emerging Design Skill Set**: Prompt engineering has become central cross-cutting skill, with designers treating prompts as iterative artifacts similar to sketches or wireframes that can be tested, revised, and shared
- **Multimodal Capabilities Enable Context-Aware Tools**: Vision-language models understanding what users see, touch, and navigate through enables design support responsive to spatial and semantic context in AR, VR, and mobile scenarios
- **Democratization Through Lowered Barriers**: LLMs enable non-technical users to contribute meaningfully by simulating underserved user groups, flagging accessibility issues, and supporting people with limited design or language skills
- **Acceleration Requires Ethical Safeguards**: While LLMs offer clear benefits in early prototyping speed and flexibility, responsible integration requires built-in checks for hallucination detection, harm anticipation, and explainability to avoid rushing through design cycles without adequate reflection
- **Field Fragmentation Signals Immaturity**: Wide practice variation (from polished plugins to bespoke systems to ad hoc prompting) indicates field has not yet converged on standardized workflows, tooling, or evaluation criteria

## Limitations & Critiques
- **Hallucinations and Reliability Issues**: LLMs generate fictional UI elements, flawed design critiques, and invalid code snippets especially in underspecified or ambiguous scenarios, undermining trust and requiring extensive manual verification
- **Prompt Engineering Challenges**: LLMs are highly sensitive to prompt phrasing, making effective prompt creation time-intensive and requiring experimentation, domain knowledge, and iterative tuning; output non-determinism where identical prompts yield inconsistent results limits reproducibility
- **Context Loss and Limited Multimodal Reasoning**: Models struggle with incomplete or ambiguous prompts, particularly when interpreting visual or spatial UI context; token limitations and lack of persistent memory constrain ability to handle multi-screen workflows or interface dynamics
- **Creativity Constraints and Over-Reliance**: LLM outputs tend to converge on generic or conservative design patterns, potentially limiting creative exploration; designers may become anchored to AI-generated suggestions too early; concern about skill stagnation among less experienced designers
- **Black Box Interpretability Problems**: Designers frequently lack insight into how and why specific outputs are produced, making validation and debugging difficult; opacity creates false sense of precision especially when presented within polished interfaces
- **Ethical, Privacy, and Legal Concerns**: Integration introduces data privacy risks, unclear ownership of AI-generated content, and embedded biases in training data; lack of governance frameworks, auditability, and inclusive datasets raises accountability and fairness concerns
- **Tooling Gaps and Integration Limitations**: Lack of seamless integration with widely used design tools (Figma, Sketch); limitations in real-time collaboration, error recovery, and iteration tracking; hardware and deployment constraints present practical challenges
- **Selection Bias in Review Methodology**: Relevance-based cutoff strategy during search phase may have excluded relevant studies appearing lower in search rankings; majority of studies from ACM conferences rather than journals may reflect publication venue bias rather than comprehensive field coverage
- **Persona-Focused Studies Excluded**: Research focused primarily on persona generation, evaluation, or diversity using LLMs was excluded as not sufficiently aligned with broader design workflow integration, potentially missing insights about this specific design artifact
- **Limited Longitudinal Evidence**: Most included studies represent exploratory or short-term evaluations rather than sustained adoption in professional practice, limiting conclusions about long-term effectiveness and organizational integration

## Related Papers
- [[papers/UI UX for Generative AI Taxonomy Trend and Challenge]]
- [[papers/Experimenting with Generative AI Tools and their Implications Insights from High]]
- [[papers/Empirical Research Strategy Session otter ai]]
- [[papers/Integrating user experience in user interface design education a problem-based l]]
- [[papers/From Expert Systems to Generative Artificial Experts]]
## Connections
- [[methods/Literature Review]] - Research methodology
- [[communities/GenAI in UX and Design Practice]] - Research community
