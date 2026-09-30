---
source_file: "ACM/Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation.pdf"
type: paper
authors: "Human-AI Co-Creation"
community: "GenAI in UX and Design Practice"
tags:
---

# Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation

## Summary
Despite potential of generative AI design tools to enhance design processes, professionals struggle to integrate AI into workflows due to fundamental cognitive challenges: (1) intent formulation - need to specify all design criteria as distinct parameters upfront, (2) problem exploration - reduced cognitive involvement due to cognitive offloading leading to insufficient problem exploration and underspecification, (3) outcome evaluation - limited ability to evaluate outcomes when problem understanding is limited. Study explores novel metacognitive support agents through Wizard of Oz prototyping with 20 mechanical designers using three agent probes: SocratAIs (reflective questions), HephAIstus (task planning/diagramming with suggestions), and external experts (freeform support). Agent-supported users created more feasible designs than unsupported users, with differing impacts between strategies. Question-asking prompting mental simulations and sketching helped intent formulation and problem exploration, but was less impactful when users had solidified incorrect assumptions. Findings reveal agent support can also lead to additional overreliance, highlighting design tradeoffs.

## Key Concepts
- Metacognitive support agents - AI assistants that help designers reflect on and regulate their own thinking to improve decision-making and problem-solving strategies
- Intent formulation challenge - requirement to specify all design criteria as distinct parameters upfront instead of iterative modeling/testing
- Cognitive offloading - reduced cognitive involvement in design process due to GenAI workflow automation fostering overreliance
- Problem exploration - thoroughly thinking through many design problem facets (explicit/implicit) necessary for sufficient solutions
- Outcome evaluation - assessing generated designs relative to design problem understanding
- Think-aloud computing - prompting designers to verbalize thoughts while working to foster deeper reflection-in-action
- Reflection-in-action - thinking through processes while actively engaging in design task
- GenAI black box operation - designers specify objectives then examine generated designs without iterative trial-and-error workflow
- Voice-based metacognitive support - using voice modality to reduce cognitive load for highly visual-spatial CAD work

## Theoretical Framework
**Metacognition Theory**: Mental processes of thinking about one’s own thinking, enabling individuals to regulate and improve cognitive strategies by reflecting on decisions and problem-solving approaches. Applied to GenAI workflows where automation can reduce cognitive engagement.

**Exploratory Prototyping Approach**: Using design probes (Sengers & Gaver, 2006) to explore design space through Wizard of Oz technique where human operator controls agent probes flexibly within probe-dependent constraints.

**Cognitive Offloading in AI-Assisted Design**: Drawing on research showing GenAI workflow automation fosters reduced cognitive involvement and overreliance, making problem exploration and definition more challenging (empirical finding that geometric modeling leads to more semantic-level actions and unexpected discoveries vs parametric environments’ top-down processes).

**Question-Asking in Design and Problem-Solving**: Questioning supporting thinking and fostering deeper cognitive engagement during problem-solving, particularly deep-level reasoning questions probing underlying principles.

## Methods
**Study Design**: Formative Wizard of Oz elicitation study with exploratory prototyping approach

**Participants**: 20 trained mechanical engineers new to working with generative AI systems

**Task**: Realistic mechanical design task using Autodesk Fusion 360 "Generative Design" extension (commercial CAD software with 3D geometric GenAI solver)

**Agent Probes** (three support strategies plus control):
1. **SocratAIs**: Asks reflective questions to prompt deeper reflection-in-action
2. **HephAIstus**: Prompts task planning and diagramming supported by suggestions for design strategies and software operation
3. **External Experts**: External experts in mechanical and generative design from Autodesk providing freeform interpretation of metacognitive support strategies
4. **Control**: No agent support

**Wizard of Oz Implementation**: 
- First author enacted SocratAIs and HephAIstus agents
- Autodesk experts acted as wizards for external expert condition
- Voice modality used for all agent interactions to reduce cognitive load for visual-spatial CAD work
- Think-aloud protocol: designers verbalized thoughts while working to foster reflection-in-action

**Data Collection**:
- Video interaction analysis of design processes
- Design outcome quality assessment
- Post-task interviews with participants

**Analysis**: Thematic analysis of video interactions and interview transcripts comparing design processes, outcome quality, and perceived benefits/challenges across conditions

**Research Questions**:
- RQ1: How do different agent support strategies impact the design process?
- RQ2: What are perceived benefits and challenges of metacognitive support agents?

## Main Arguments
- Metacognitive support agents can address fundamental cognitive challenges of GenAI workflows (intent formulation, problem exploration, outcome evaluation) - agent-supported users created more feasible designs than unsupported users
- Different metacognitive support strategies have distinct impacts - question-asking prompting mental simulations and sketching helped intent formulation and problem exploration regarding mechanical loads, but was less impactful when users solidified incorrect assumptions
- Voice-based agent support reduces cognitive load for visual-spatial design tasks while enabling deeper reflection-in-action through think-aloud protocols
- GenAI workflow automation poses unique cognitive challenges requiring different support than traditional CAD - shift from iterative modeling/testing to upfront parameter specification demands new attitudes, skills, and mental processes
- Metacognitive support has both benefits and risks - while most users actively engaged and appreciated support in thinking through tasks, agent support can lead to additional overreliance
- Effective GenAI design support requires rethinking parametric design tools and developing systems supporting designers in parametric modeling and computational thinking, not just improving black box AI models
- Design tradeoffs exist in metacognitive support strategies - balancing depth of cognitive engagement with efficiency, preventing incorrect assumption solidification while avoiding overwhelming users

## Limitations & Critiques
**Study Design Limitations**:
- Wizard of Oz technique means agents were human-operated, not autonomous - may not reflect actual AI agent capabilities or limitations
- First author as wizard for two conditions introduces potential bias and consistency issues vs external experts
- Single design task limits generalizability across different mechanical design challenges
- Formative study with 20 participants provides preliminary insights but insufficient sample for statistical generalization
- No longitudinal observation - cannot assess long-term impacts of metacognitive support on skill development or independence

**Methodological Concerns**:
- "Feasibility" of designs not clearly operationalized - unclear what criteria determined one design more feasible than another
- No objective performance metrics beyond feasibility assessment
- Think-aloud protocol may alter natural design processes and cognitive load
- Comparison across different agent types and control challenging when wizard operators differ
- Selection of mechanical engineers "new to working with generative AI" may not represent experienced GenAI users who may need different support

**Conceptual Tensions**:
- Paper identifies cognitive offloading as problem but some cognitive offloading is intentional benefit of AI tools - unclear where boundary lies between helpful automation and problematic overreliance
- Tension between supporting reflection and maintaining design flow - reflective questioning may interrupt creative momentum
- Metacognitive support assumes designers should maintain deep cognitive engagement throughout process - may not align with efficiency goals motivating GenAI adoption
- Focus on individual designer metacognition may miss collaborative design dynamics

**Generalization Limitations**:
- Study specific to mechanical design with Autodesk Fusion 360 - unclear how findings apply to other design domains (graphic, UX, architectural) or other GenAI tools
- Voice-based support may not be appropriate for all design contexts (e.g., collaborative environments, accessibility needs)
- External expert condition confounds metacognitive support with domain expertise - unclear which contributed to outcomes

**Practical Concerns**:
- Implementation challenges for autonomous metacognitive agents not addressed - WoZ flexibility difficult to replicate with actual AI
- Cost and scalability of providing metacognitive support unclear
- User preferences showed variation - one-size-fits-all approach may not work
- Paper doesn’t address how to prevent additional overreliance identified as risk

## Related Papers
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 CHI]]
- [[papers/From Disruptions to Discussions How GenAI Impacts Human Interactions in Software]]
- [[papers/Towards Distributed Creativity Understanding Generative AI in th]]
## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
