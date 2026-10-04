---
title: A Formative Study to Explore the Design of Generative UI Tools to Support UX Practitioners and Beyond
source_file: AI collaboration related articles/A Formative Study to Explore the Design
  of Generative UI Tools to Support UX Practitioners and Beyond.pdf
type: paper
authors: Chen et al.
community: GenAI in UX and Design Practice
tags: null
year: 2024
builds_on:
- '[[frameworks/Human-Centered Design]]'
- '[[methods/Grounded Theory]]'
- '[[concepts/Design Ideation]]'
critiques: []
tensions_with:
- '[[concepts/De-skilling]]'
- '[[concepts/Ironies of Automation]]'
supports:
- '[[concepts/Democratization of Design]]'
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/Creativity Support Tools]]'
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/Design Fixation]]'
- '[[concepts/AI Tool Dependence]]'
key_claims:
- GenUI demonstrates 'good first draft, tough last mile' phenomenon—excels at rapidly
  producing initial prototypes but requires significant editing effort to reach production-ready
  standards, with UXD4 finding manual Figma creation faster than using GenUI's sketch-to-UI
  feature
- GenUI democratizes UX design for non-designer roles (PMs, developers, researchers)
  by enabling independence from designer resources, with evidence that PMs use it
  to visualize product vision, developers for visual specifications, and researchers
  for study planning
- 'Seven critical gaps prevent GenUI adoption: problem formulation with context, assimilating
  user intent, constrained generation to design systems, multimodal input/output needs,
  connecting UI elements consistently, quality and originality issues, and insufficient
  editing/iteration support'
- Future GenUI tools must integrate seamlessly into existing workflows (Figma, IDEs,
  documentation systems) and support organizational design systems through fine-tuning
  to achieve practical adoption beyond conceptual exploration
methodology: '[[methods/Mixed Methods]]'
sample_size: 37
sample_type: UX-related professionals (11 UX designers, 12 developers, 7 product managers,
  7 UX researchers)
context: Individual one-week exercises using state-of-the-art GenUI tool for mindful
  micro-activities app design project
study_type: empirical
---

# A Formative Study to Explore the Design of Generative UI Tools to Support UX Practitioners and Beyond

## Summary
AI can now generate high-fidelity UI mock-up screens from a highlevel textual description, promising to support UX practitioners’ work However, it remains unclear how UX practitioners would adopt such Generative UI (GenUI) models in a way that is integral and beneficial to their work To answer this question, we conducted a formative study with 37 UX-related professionals that consisted of four roles: UX designers, UX researchers, developers, and product managers.

## Key Concepts
- **Generative UI (GenUI) models**: AI systems capable of creating high-fidelity UI mock-up screens from textual descriptions, sketches, or screenshots, promising to transform prototyping practices across UX-related roles
- **Democratization of UX design**: GenUI lowers barriers to prototyping for non-UXD roles (PMs, developers, researchers), enabling them to gain independence from designer resources and accelerate their work
- **"Good first draft, tough last mile" phenomenon**: GenUI excels at rapidly producing initial prototypes but suffers from quality issues requiring significant editing effort to reach production-ready standards
- **Role-specific support patterns**: Different professional roles (UXD, UXR, PM, Dev) adopt GenUI for distinct purposes—designers for early ideation, PMs for visualizing product vision, developers for visual specifications, and researchers for study planning
- **Workflow integration challenges**: Critical need for seamless transfer between GenUI tools and existing design ecosystems (Figma, IDEs, documentation systems) to realize practical adoption
- **Visual communication as nexus**: GenUI prototypes serve dual purposes—individual design exploration and cross-functional stakeholder communication—positioning GenUI as potential collaborative workspace
- **Constrained generation requirements**: Generated UIs must adhere to organizational design systems, domain-specific patterns, and accessibility standards to provide practical value beyond conceptual exploration
- **Multimodal interaction paradigm**: Users require diverse input modalities (text prompts, sketches, requirement documents, user flows) and output formats (high/low-fidelity prototypes, study plans, feature summaries) matching their role-specific workflows

## Theoretical Framework
**Dual Purposes of Prototyping Framework** (Houde & Hill 1997, Lichter et al. 1994, Lauff et al. 2020): Prototypes serve two complementary functions: (1) facilitating iterative design and development—from exploring early ideas to evolving working versions toward product-ready artifacts, and (2) enabling communication by providing shared understanding across different roles and stakeholders. This dichotomy structures the paper's analysis of GenUI's promises and gaps.

**Anatomy of Prototypes** (Lim et al. 2008): Prototypes comprise two dimensions—filtering (selecting certain aspects of system design) and manifesting (representing the prototype in specific media). For designers, prototypes should stimulate thinking, communicate design decision rationales, and enable discovering possibilities in the design space rather than merely matching requirements. This framework informs understanding of GenUI output fidelity and iteration needs.

**Grounded Theory Approach** (Charmaz 2006): Used for qualitative analysis through iterative coding—breaking data into atomic segments with low-level codes, developing higher-level codes into a codebook (28 codes), then converging to themes addressing research questions. This methodological framework enabled systematic distillation of workflow patterns, promises/opportunities, and gaps from participant experiences.

## Methods
interview

## Main Arguments
- **GenUI benefits all UX-related roles through universal support mechanisms**: The study demonstrates three cross-role promises: (1) supporting early-stage ideation by providing design possibilities and helping users overcome "cold start" problems, (2) saving time and effort to create "first draft" prototypes compared to manual approaches, particularly valuable under tight deadlines, and (3) facilitating visual communication across roles by transforming abstract ideas into tangible artifacts that align stakeholder thinking. Evidence includes UXD2 using varied prompts to explore design possibilities, Dev12 noting GenUI eliminated time spent on CSS/HTML styling, and UXR7 describing how prototypes enabled gathering initial colleague reactions.

- **GenUI democratizes UX for non-designer roles but requires role-specific adaptations**: Beyond supporting UXD work, GenUI empowers non-designers to gain independence from designer resources—particularly critical when designer availability is limited. For PMs, GenUI visualizes product vision and reduces requirement ambiguity (PM3 noting how seeing "modern" translated visually clarified terminology for PRDs). For developers, it provides visual specifications to guide coding and enables quick idea bootstrapping before committing to implementation. For UXR, it aids understanding product features, formulating research questions, and communicating proposals. However, democratization requires tailored support: non-UXD users struggle with UX-specific terminology and interface complexity, necessitating simplified interaction modes.

- **Seven critical gaps prevent GenUI from realizing its full potential**: The research identifies systematic challenges spanning the prototyping process: (1) **Problem formulation with context**—tools lack support for defining design problems before exploring solutions, forcing users to external language models; (2) **Assimilating user intent**—difficulty following explicit instructions and inferring implicit design goals leads to outputs that miss "core essence" despite understanding surface details; (3) **Constrained generation**—need for adherence to organizational design systems and accessibility standards; (4) **Multimodal input/output**—requirement for diverse formats beyond text prompts (sketches, requirement docs, user flows) and outputs beyond high-fidelity screens (study plans, feature summaries); (5) **Connecting UI elements**—failure to maintain consistent styles, shared context, and hierarchical layouts across screens; (6) **Quality, fidelity, and originality**—production-readiness issues and lack of thoughtful problem-solving beyond templated solutions; (7) **Support for editing and iteration**—insufficient tools for refining individual elements or enabling rapid comparison of design options.

- **The "last mile problem" defines GenUI's current utility boundary**: While GenUI excels at rapidly producing good-enough first drafts, the quality issues requiring significant editing create a paradox—the effort needed to reach production-ready designs may exceed manual creation time for experienced users. UXD4 found crafting UIs manually in Figma faster than using GenUI's sketch-to-UI feature. The path forward requires either improving back-end model quality (likely as code generation AI advances) or accepting GenUI tools should remain lightweight, focusing on first drafts and handing off editing to specialized tools like Figma. This reframes GenUI not as end-to-end solution but as catalytic starting point.

- **Future GenUI tools must address practical organizational constraints to achieve adoption**: Technical capability alone proves insufficient—tools must integrate seamlessly into existing workflows, support organizational design systems through fine-tuning, expand beyond consumer apps to domain-specific applications (internal tools, dashboards), and automatically enforce accessibility best practices. Without these practical considerations, teams cannot adopt GenUI results beyond conceptual exploration. The research reveals workflow integration as the most common concern, with participants needing export to Figma/Slides, transfer to study plans, and incorporation into development codebases. This echoes prior findings that "simplistic automation" fails without deep workflow integration.

## Limitations & Critiques
**Methodological Limitations**: The study employed only one state-of-the-art GenUI tool, limiting generalizability across different GenUI implementations with varying technical back-ends and interactive front-ends. While the researchers believe identified gaps likely exist in other GenUI tools given similar underlying technologies, the single-tool constraint prevents comparative analysis. The authors explicitly acknowledge this limitation and plan follow-up studies incorporating newer GenUI tools to validate and expand findings.

**Participant Context Constraints**: Study required participants to avoid work-related content and perform tasks during personal time to comply with company regulations, potentially limiting ecological validity. The artificial mini-project scenario (mindful micro-activities app) may not fully capture how professionals would integrate GenUI into actual production projects with established codebases, design systems, and team dynamics.

**Duration and Depth Trade-offs**: One-week individual exercises, while providing hands-on grounding, captured only initial adoption patterns rather than long-term integration into established workflows. The study does not examine how GenUI usage might evolve with extended familiarity, how teams would collaboratively use GenUI beyond individual exercises, or how generated prototypes would flow through complete product development cycles.

**Role Distribution Imbalance**: Participant numbers varied across roles (11 UXD, 12 Dev, 7 PM, 7 UXR), partly reflecting organizational distribution but potentially over-representing designer and developer perspectives in the aggregated findings. The snowball sampling used to fill demographic gaps may introduce network-based biases.

**Quality Issues as Moving Target**: The "last mile problem" and quality concerns identified may rapidly become dated as generative AI models improve. Since many GenUI tools build on code generation AI showing continuous advancement, findings about output quality represent a snapshot rather than inherent limitations. The research does not establish threshold criteria for when quality improvements would fundamentally shift the utility calculus.

**Limited Exploration of Team-Level Dynamics**: While the study identifies untapped potential for team-level support and communication, the individual-focused methodology provides limited empirical evidence about collaborative GenUI practices. Findings about cross-role communication rely primarily on participant speculation about how GenUI could support collaboration rather than observed collaborative interactions.

## Connections
- [[methods/Interview]] - Research methodology
- [[communities/GenAI in UX and Design Practice]] - Research community

