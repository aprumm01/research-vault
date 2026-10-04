---
source_file: AI collaboration related articles/From_Disruptions_to_Discussions_How_GenAI_Impacts_Human_Interactions_in_Software_Development.pdf
type: paper
authors: Impacts Human Interactions in
community: Design Theory and Cognition
tags: null
year: 2024
builds_on:
- '[[frameworks/Sociotechnical]]'
- '[[frameworks/Activity Theory]]'
critiques: []
tensions_with:
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/Social Isolation (AI-induced)]]'
supports:
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/Peer Learning Erosion]]'
- '[[concepts/AI Augmentation]]'
key_claims:
- GenAI substantially reduces routine technical questions (API documentation, syntax
  clarification, error resolution) while increasing strategic discussions about architectural
  decisions, design tradeoffs, and business requirements, transforming rather than
  reducing collaboration quality
- AI consultation lacks critical social and contextual dimensions of human interaction
  including contextual awareness of project specifics, bidirectional learning between
  asker and answerer, relationship building for team bonds, and tacit knowledge transfer
  of implicit wisdom and judgment
- Junior developers disproportionately adopt AI for learning and question-answering,
  potentially reducing mentorship interactions with senior colleagues and raising
  concerns about professional socialization, knowledge transfer across experience
  levels, and long-term team capability development
- Initial GenAI adoption creates disruption in established communication patterns,
  but teams develop new norms over time about appropriate AI versus human consultation,
  though optimal patterns require deliberate cultivation rather than self-organization
- GenAI impacts interact with work modality contexts, with remote/hybrid teams potentially
  experiencing exacerbated isolation if AI further reduces interaction touchpoints,
  while co-located teams may benefit from reduced interruptions without losing informal
  interaction opportunities
methodology: '[[methods/Mixed Methods]]'
sample_size: null
sample_type: software developers
context: software development teams using GenAI tools
study_type: empirical
---

# From Disruptions to Discussions How GenAI Impacts Human Interactions in Software Development

## Summary
work, such as how generative AI (GenAI) can help a developer write code New technologies can also impact how people interact with one another, such as how GenAI’s ability to summarize API documentation can reduce the need for developers to ask each other technical questions In this paper, we report on a two-phase mixed-method study exploring how GenAI influences how humans interact in software development.

## Key Concepts
- **GenAI-mediated communication patterns**: Changes to how software developers interact with each other as generative AI tools (ChatGPT, GitHub Copilot, documentation assistants) intermediate information exchange, potentially reducing synchronous questions, altering knowledge-sharing dynamics, and reshaping team communication norms
- **Technical question displacement**: Reduction in routine technical inquiries (API usage, syntax questions, error debugging) as developers increasingly query AI tools rather than colleagues, shifting human interaction toward higher-level discussions about architecture, design decisions, and strategic choices
- **Collaboration quality vs. quantity tradeoff**: Potential tension between decreased interaction frequency (efficiency gain from AI self-service) and collaboration depth/richness, raising questions about tacit knowledge transfer, team cohesion, mentorship, and organizational learning when routine exchanges diminished
- **From disruption to discussion**: Evolution from initial AI-induced disruption of established communication patterns toward new equilibrium where human interactions concentrate on discussions requiring collective judgment, contextual understanding, and social coordination that AI cannot replicate
- **Asynchronous knowledge access shifts**: Movement from synchronous colleague interruptions toward asynchronous AI consultation for information needs, with implications for workflow continuity, cognitive load, social connection, and distribution of knowledge-provider burden across team

## Theoretical Framework
**Computer-Mediated Communication (CMC) Theory**: Applying frameworks from CMC research to understand how AI tools function as new form of mediation in developer communication, examining how GenAI characteristics (always available, no social cost, broad knowledge, lack of context) differentially shape interaction patterns compared to human colleagues.

**Transactive Memory Systems**: Drawing on organizational cognition theory about how teams develop shared systems for encoding, storing, and retrieving knowledge across members, examining how GenAI integration potentially disrupts transactive memory by changing who/what developers consult for different knowledge types and implications for team expertise coordination.

## Methods
**Two-phase mixed-methods study**: 
- **Phase 1 - Survey**: Quantitative assessment (n=XXX developers) measuring GenAI adoption rates, usage contexts, perceived impacts on communication frequency/type/quality, and attitudes toward AI-mediated versus human interaction across development tasks
- **Phase 2 - Interviews**: Qualitative exploration (n=XX developers) through semi-structured interviews examining detailed experiences, specific interaction changes, adaptation strategies, and nuanced perspectives on collaboration transformation

**Communication pattern analysis**: Systematic examination of developer interaction changes across dimensions including frequency (how often), modality (synchronous vs. asynchronous), content (technical vs. strategic), and participant roles (peers, senior developers, managers), comparing pre-GenAI and post-GenAI adoption patterns.

## Main Arguments
- **GenAI substantially reduces routine technical questions but increases strategic discussions**: Study reveals significant decrease in basic technical inquiries (API documentation, syntax clarification, common error resolution) as developers self-serve through AI tools, reducing interruptions and improving individual productivity. However, human interactions increasingly concentrate on higher-value discussions: architectural decisions, design tradeoffs, business requirement interpretation, code review discussions. Net effect not reduced collaboration but qualitatively transformed collaboration focused on judgments requiring collective deliberation and contextual understanding beyond AI capabilities.

- **AI consultation lacks critical social and contextual dimensions of human interaction**: While GenAI efficiently answers technical questions, interactions lack several valuable dimensions of colleague consultation: (1) contextual awareness—colleagues understand project specifics, team conventions, organizational constraints, (2) bidirectional learning—questions educate both asker and answerer, (3) relationship building—interactions strengthen team bonds, trust, shared mental models, (4) tacit knowledge—experienced developers convey implicit wisdom, judgment, and nuance beyond explicit answers. Efficiency gains from AI consultation may incur hidden costs in organizational learning, team cohesion, and knowledge quality.

- **Generational and role-based differences in adaptation and implications**: Junior developers disproportionately adopt AI for learning and question-answering, potentially reducing mentorship interactions with senior colleagues—benefiting through reduced intimidation and 24/7 availability but potentially missing guidance, feedback, and professional socialization. Senior developers use AI for efficiency but continue human consultation for complex problems. This divergence raises concerns about junior developer formation, knowledge transfer across experience levels, and long-term team capability development if generational practices differ substantially.

- **From disruption toward emergent norms requiring deliberate cultivation**: Initial GenAI adoption period characterized by uncertainty about when to consult AI versus colleagues, creating disruption in established communication patterns and potential team fragmentation. Over time, teams develop new norms (explicitly discussed or implicitly emerged) about appropriate AI versus human consultation. However, optimal patterns not self-organizing—teams benefit from deliberate discussions establishing expectations, ensuring preserved valuable human interactions, and preventing over-reliance on AI where inadequate.

- **Communication transformation interacts with work arrangement contexts**: GenAI impacts interact with work modality—remote/hybrid teams already facing collaboration challenges may experience exacerbated isolation if AI further reduces interaction touchpoints, while co-located teams may benefit from reduced interruptions without losing informal interaction opportunities. Organizational context (startup versus enterprise, project type, team maturity) mediates whether communication changes net positive or problematic.

## Limitations & Critiques
**Self-report reliability and perception vs. reality gaps**: Reliance on developer perceptions of communication changes through surveys/interviews may not accurately reflect actual interaction patterns, which could be validated through communication platform analytics, observational studies, or longitudinal tracking of messaging/meeting data before and after GenAI adoption.

**Temporal scope and normalization effects**: Study captures relatively early GenAI adoption period where novelty effects, experimental usage, and transitional uncertainty prominent. Long-term equilibrium patterns, generational shifts as AI-native developers enter workforce, and stabilized norms may differ substantially from currently observed disruption-to-discussion trajectory.

**Sample limitations**: Developer population characteristics (company size, domain, technology stack, team structure, seniority distribution) affect generalizability. Findings may not extend to different development contexts (embedded systems, academic research computing, legacy system maintenance) where collaboration dynamics and AI applicability differ.

**Insufficient causal evidence**: Correlation between GenAI adoption and communication changes does not establish causation—other factors (pandemic recovery, organizational changes, development methodology shifts, tooling evolution beyond GenAI) could contribute to observed patterns, requiring more controlled comparative or longitudinal designs to isolate GenAI effects.

**Limited examination of productivity and quality outcomes**: While documenting communication changes, insufficient assessment of ultimate impacts on development outcomes—does reduced routine communication and increased strategic discussion actually improve software quality, team productivity, innovation, or satisfaction? Communication transformation might be neutral, beneficial, or harmful depending on unmeasured outcome dimensions.

**Missing organizational and power dimensions**: Limited attention to how communication changes differentially affect developers based on position power, social capital, demographic characteristics—who benefits from AI self-service versus who marginalized when informal interaction opportunities reduced? Potential for AI to exacerbate existing inequities in voice, visibility, and influence within development teams.

## Related Papers
- [[papers/From code to collaboration]]
- [[papers/AI Hasn t Fixed Teamwork But It Shifted Collaborative Culture - A Longitudinal S]]
- [[papers/Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation]]

## Related Papers
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 CHI]]
- [[papers/Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation]]
- [[papers/Towards Distributed Creativity Understanding Generative AI in th]]
## Connections
- [[methods/Survey]] - Research methodology
- [[methods/Interview]] - Research methodology
- [[communities/Design Theory and Cognition]] - Research community
