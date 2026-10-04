---
source_file: EDU-AI/Using Generative AI Tools in Collaborative UX design courses.pdf
type: paper
authors: Felix Buendia-Garcia
community: GenAI in UX and Design Practice
tags: null
year: 2024
builds_on:
- '[[frameworks/Sociotechnical]]'
- '[[frameworks/Human-Centered Design]]'
- '[[concepts/Human-AI Co-creation]]'
- '[[frameworks/Constructivism]]'
critiques: []
tensions_with:
- '[[concepts/AI Tool Dependence]]'
- '[[concepts/De-skilling]]'
supports:
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/AI as Facilitator]]'
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/Creativity Support Tools]]'
key_claims:
- GenAI tools prove particularly valuable during initial UX design stages (ideation,
  user analysis) where students lack professional experience, while later stages require
  more personalized human approaches
- AI-generated personas show disparate briefing alignment (75-95% matching range)
  with high-level global scores (80-85%) masking low consistency in specific features,
  demonstrating need for iterative refinement
- Card sorting validation with real users reveals variable agreement levels (under
  70% for concepts like 'Competitive Drive' and 'Fitness Activity'), demonstrating
  that AI-generated concept hierarchies require human validation
- PCI students with limited programming backgrounds face significant technical implementation
  barriers despite GenAI assistance, as ChatGPT solutions only address partial aspects
  without enabling integration
- Conversational prompts facilitated through JSON-formatted scripts enable collaborative
  knowledge construction between instructors, students, and AI, providing neutral
  feedback that addresses students' reluctance to discuss subjective interpretations
methodology: '[[methods/Mixed Methods]]'
sample_size: 75
sample_type: undergraduate design and creative technologies students in 3rd and 4th
  year UX courses
context: Universitat Politècnica de Valencia Bachelor's Degree program, two course
  types (APW and PCI) from 2021-2024
study_type: empirical
---

# Using Generative AI Tools in Collaborative UX design courses

## Summary
Artificial Intelligence and their derived Generative technologies are playing a crucial role in many applications that involve an active collaboration among machine assistants and human users That is the case for User Experience courses that allowed students and instructors work together with Generative Artificial Intelligence tools to produce a collaborative design The main purpose of this research consisted in reviewing several stages in design tasks that could take advantage of Artificial Intelligence tools by boosting a prompt-based conversation among instructors and students.

## Key Concepts
- **Generative AI in UX Education**: GenAI tools (ChatGPT, Voila) used to facilitate collaborative design processes in User Experience courses through prompt-based conversations among instructors and students
- **Socio-technical Co-creation**: AI positioned as an actor in co-creation design patterns, participating alongside human instructors and students in collaborative value generation
- **Six-Stage UX Design Process**: Product definition, information research, user analysis (personas), information architecture, prototype design, and testing stages as framework for integrating GenAI
- **Prompt-Based Collaboration**: Exchange of JSON-formatted prompt scripts between students and instructors to enable iterative refinement of design artifacts and shared knowledge construction
- **Human-AI Dialogue**: Conversational prompts enabling feedback collection from AI tools providing neutral, alternative perspectives to subjective human interpretations in design decisions
- **Collaborative Assessment**: GenAI tools used to interpret student comments using structured evaluation criteria (clarity, aesthetics, layout, organization) and Likert scales for formative assessment
- **Persona Validation**: Using GenAI to assess matching degree between student-created persona profiles and briefing requirements, identifying disparities in briefing item alignment
- **Information Architecture Extraction**: AI-assisted generation and categorization of concept hierarchies validated through card sorting techniques with real users
- **Prototype Testing Automation**: AI-powered attention prediction tools and automated interpretation of mockup reviews to supplement traditional eye-tracking methods
- **Barriers to Implementation**: Technical challenges in Web development stages where students with limited programming skills struggled to implement AI-generated code suggestions

## Theoretical Framework
**Co-creation and Socio-technical AI Integration**: Research grounded in socio-technical view of GenAI (Feuerriegel et al., 2024) with focus on co-creation patterns guiding collaborative value contribution by multiple actors including AI. Builds on collective knowledge building perspective (Cress & Kimmerle, 2023) using argumentative dialogues between humans and AI tools facilitated through prompts for emergent joint knowledge construction.

**Project-Based Learning in UX Design**: Framework based on classical UX design process (Unger & Chandler, 2023) with formal six-stage structure applied through PBL approaches successfully deployed in interface design (De Sales & Boscarioli, 2021) and AR applications (Liu et al., 2021). Integration of Agile methods with UX design (Schön et al., 2023) for teams with technical backgrounds.

**Human-AI Collaboration in Design**: Literature review on collaboration between designers and AI (Shi et al., 2023) providing foundation for understanding how AI assists designers in interpreting user comments and analyzing behaviors. Framework addresses team-wide GenAI practices and cultural transformation needs in UX collaboration (Wang et al., 2024; Takaffoli et al., 2024).

## Methods
**Research Context**: Study conducted across two course types in Design and Creative Technologies Bachelor's Degree at Universitat Politècnica de Valencia (2021-2024): (1) APW (Web Applications) - 3rd year optative, 18-32 students in teams of 2-3, technical focus with Agile methods; (2) PCI (Interactive Communication Projects) - 4th year compulsory, 22-43 students in teams of 3-4, classical UX process with art department supervision.

**Collaborative GenAI Implementation**: Voila tool selected for free access and JSON import/export capability enabling prompt script exchange. Instructor-initiated prompts provided briefing information context, students iteratively refined through team discussions, outcomes returned to instructors for analysis. Alternative explored: ChatGPT assistants for technical implementation support.

**User Analysis Methods**: Persona creation confrontation process - students defined persona profiles based on briefings, GenAI assessed matching degree with briefing contents through structured prompts. Open coding techniques applied to JSON-formatted script outcomes to extract persona attributes and analyze alignment percentages across briefing items.

**Information Architecture Methods**: GenAI-generated concept hierarchies through iterative prompt sequences extracting basic ideas at multiple abstraction levels. R script processing of JSON files to convert concept hierarchies to CSV format. Card Sorting validation using Optimal Workshop platform with real users classifying AI-generated concepts into categories (n=10 students, 47s average completion).

**Prototype Testing Methods**: Collaborative review using Google Drive shared documents with student annotations and drawn overlays on mockup images. AI interpretation of review comments using Likert scale (1-5) prompts to evaluate criteria (clarity, aesthetics, layout, organization, fonts, color). Eye-tracking comparison between AI-predicted heatmaps (Attention Insight) and actual user data (Gaze Recorder).

**Data Collection and Analysis**: JSON-formatted prompt scripts collected and processed programmatically. Qualitative analysis of student engagement levels (6/12 reviewers for Map project, 4/12 for Bud, 2/12 for Sin). Quantitative matching percentages for persona-briefing alignment and concept categorization agreement scores.

## Main Arguments
- **GenAI Enhances Early-Stage UX Creativity**: Generative AI tools prove particularly valuable during initial UX design stages (ideation, user analysis) where students without professional experience struggle, providing innovative suggestions that complement limited experience, while later stages (design issues, testing) require more personalized "human touch" approaches
- **Prompt-Based Dialogue Enables Collaborative Learning**: Conversational prompts triggered by instructors and refined through student-AI-student exchanges facilitate rich idea generation and neutral feedback collection, addressing students' reluctance to discuss ideas by providing alternative perspectives beyond subjective human interpretations
- **AI as Neutral Co-creator in Assessment**: GenAI tools function as co-creators providing inspiration and automating repetitive tasks while offering objective evaluation of collaborative activities through structured interpretation of student work, though integration requires instructor attention to prevent over-reliance hindering foundational skill development
- **Collaborative Features Remain Underutilized**: Despite availability of collaborative design platforms (Figma, Adobe XD) with AI components, students prove reluctant to leverage collaborative features due to coordination demands, while team-wide GenAI practices remain challenging and lack integration within instructional contexts
- **Technical Implementation Represents Critical Barrier**: PCI students with limited programming backgrounds face significant difficulties implementing design mockups despite GenAI assistance, as ChatGPT solutions only address partial aspects (basic landing pages, simple navigation) without enabling integration, forcing ad-hoc team strategies and reducing collaborative work
- **AI-Generated Concepts Require Human Validation**: While GenAI successfully extracts concept hierarchies and organizes information architecture, Card Sorting with real users reveals variable agreement levels (under 70% for concepts like "Competitive Drive" and "Fitness Activity"), demonstrating need for human judgment in validating AI outputs
- **Persona Creation Shows Inconsistent Briefing Alignment**: GenAI assessment reveals disparate matching percentages across persona profiles (75-95% range) and briefing items, with high-level global scores (80-85%) masking low consistency in specific features, evidencing need for iterative refinement processes
- **Collaborative Assessment Technology Shows Promise**: AI tools demonstrate huge potential for extracting valuable information from testing tasks and supporting formative assessment of UX processes, though more validation efforts needed for automatic assessment procedures in project-based collaborative activities

## Limitations & Critiques
- **Limited Tool Accessibility and Integration**: Study constrained by reliance on freely available Voila tool with prompt size limitations; lack of universal access to collaborative GenAI tools and low-cost API methods for programmatic outcome retrieval; absence of seamless integration between AI tools and specific design platforms viewed as main barriers
- **Small Sample Sizes and Variable Engagement**: Card sorting experiment with only 10/17 invited students participating; mockup review showing differential commitment levels (6/12 for one project, only 2/12 for another); APW courses with declining enrollment (32 to 18 students) limiting generalizability
- **Single-Institution Context**: Research limited to one university (Universitat Politècnica de Valencia) in specific degree program (Design and Creative Technologies Bachelor's) with particular student profiles, constraining transferability to other educational contexts and cultures
- **Lack of Longitudinal Assessment**: Study covers 2021-2024 period but does not track same student cohorts over time or measure long-term skill development, learning outcomes, or professional preparation; no follow-up on whether students developed appropriate balance between AI use and foundational skills
- **Incomplete Development Stage Coverage**: Technical implementation barriers in Web development prevented full evaluation of GenAI effectiveness across complete UX process; final integration and coding stages remained problematic, limiting conclusions about end-to-end collaborative design workflows
- **Validation Gap for AI-Generated Content**: While comparing AI predictions with actual eye-tracking results for one mockup, study lacks comprehensive validation of AI-generated personas, concept hierarchies, and design suggestions against professional UX standards or real user needs
- **Assessment Methodology Concerns**: AI interpretation of student comments using Likert scales introduces potential bias and reliability questions; no inter-rater reliability measures or validation of AI scoring against human expert evaluations; unclear whether AI assessment captures nuanced qualitative feedback
- **Ethical Considerations Underexplored**: While acknowledging student perceptions about autonomy and monitoring concerns, study lacks systematic investigation of ethical implications including data privacy, bias in AI outputs, intellectual property issues, or impact on creative ownership
- **Technology-Specific Dependencies**: Research outcomes dependent on particular tools (Voila, ChatGPT, Optimal Workshop, Attention Insight) that may change, become unavailable, or have different capabilities in future, limiting reproducibility and long-term applicability
- **Instructor Training and Support Gap**: While identifying need for comprehensive training programs for students and instructors, study does not provide or evaluate specific pedagogical approaches for teaching effective GenAI collaboration or address instructor preparation requirements

## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
