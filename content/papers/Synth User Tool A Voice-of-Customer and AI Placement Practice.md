---
source_file: Synth_User_Tool_VoC_practice.pdf
type: paper
authors: Anonymous Author(s)
year: 2026
builds_on:
- '[[methods/Content Analysis]]'
- '[[methods/Persona Development]]'
- '[[frameworks/Human-Centered Design]]'
- '[[frameworks/Nielsen''s Usability Heuristics]]'
critiques:
- '[[concepts/Synthetic Users]]'
tensions_with: []
supports:
- '[[concepts/Human-in-the-Loop Pedagogy]]'
- '[[concepts/AI Augmentation]]'
- '[[concepts/Explainable AI]]'
key_claims:
- Synthetic personas grounded in 65,141 actual customer feedback records rather than
  demographic assumptions removes the most common source of systematic bias while
  maintaining traceability to real user statements
- The tool's top finding matched a human-moderated usability study's top finding in
  a comparison study with 5 participants, identifying the same primary friction point
- AI handles volume well—processing tens of thousands of feedback entries to identify
  patterns at speeds human teams cannot match—but does not identify systemic problems,
  only surfacing symptoms that require human judgment
- Synthetic user tools should be evaluated as precursors to human research rather
  than substitutes for it, most useful in validation phases rather than discovery
  when audiences are new
- Weight-based personas representing distributions of pain points that update monthly
  as feedback patterns shift provide longitudinal tracking of how user concerns evolve
  as products change
methodology: '[[methods/Mixed Methods]]'
sample_size: 65141
sample_type: customer feedback records from global enterprise travel platform users
  across US, EU, and Asia; 5 participants in comparison usability study
context: Enterprise travel and expense platform with tens of thousands of corporate
  customers over 8-month deployment (December 2025 to July 2026)
study_type: empirical
---

# Synth User Tool: A Voice-of-Customer and AI Placement Practice

## Summary
This paper presents the Synth User Tool, a voice-of-customer system built for an enterprise travel and expense platform that takes a fundamentally different approach to synthetic user research. Rather than prompting an LLM to generate users from demographic attributes, the tool instructs the LLM to code and categorize tens of thousands of real customer feedback records. The system generates weight-based personas representing distributions of pain points rather than demographic profiles, with every output traceable to specific customer comments. Over an eight-month deployment period (December 2025 to July 2026), the system accumulated 65,141 unique feedback records from global markets.

The tool works through four stages: (1) data collection of approximately 80,000 monthly customer responses; (2) content analysis using LLM coding adapted from Herring's discourse analysis framework; (3) persona generation aggregating coded feedback into five personas based on user concern types that update monthly; and (4) design evaluation using a layered protocol combining persona pain points, Nielsen's usability heuristics, WCAG accessibility standards, and enterprise design system patterns. A comparison study with five participants showed the tool's top finding matched a human-moderated usability study's top finding, with both identifying the same primary friction point.

The paper argues that synthetic user tools should be evaluated as precursors to human research rather than substitutes for it, demonstrating where AI-driven analysis can redirect rather than replace human research and design efforts.

## Key Concepts
- **Voice-of-Customer Grounding**: Building synthetic personas from actual customer language and feedback rather than demographic assumptions, ensuring traceability to real user statements
- **Weight-Based Persona Architecture**: Representing users as distributions of pain points rather than demographic profiles, with personas updating monthly as feedback patterns shift
- **Longitudinal Tracking**: Monitoring how persona pain points change over time as products evolve, preserving variance rather than averaging it out
- **Layered Design Evaluation Protocol**: A four-layer review combining persona pain points, usability heuristics, accessibility standards, and design system patterns to prioritize issues
- **Precursor vs. Substitute Positioning**: Framing synthetic user tools as directing human research attention rather than replacing human judgment

## Theoretical Framework
The paper engages with literature on synthetic user research at the intersection of HCI and LLMs, drawing on discourse analysis frameworks (Herring's CMDA framework), persona development traditions, and design evaluation methodologies. The theoretical contribution lies in repositioning the synthetic user debate from accuracy validation to appropriate placement within design processes, arguing the right test is whether designers using the tool make better-focused decisions.

## Methods
- **Deployment Context**: Global enterprise travel and expense platform serving tens of thousands of corporate customers across US, EU, and Asia
- **Data Collection**: In-product surveys collecting satisfaction scores and written comments; 65,141 unique feedback records over 8 months
- **Content Analysis**: LLM-automated coding using adapted discourse analysis framework; themes emerge inductively with actionability filtering
- **Personas**: Five market-specific personas (Alex the Navigator, Morgan the Modifier, Casey the Comparison Shopper, Drew the Policy-Conscious, Sam the First-Timer) updated monthly
- **Evaluation Study**: Comparison against moderated usability study with 5 participants completing 4 tasks on the same prototype

## Main Arguments
- Most synthetic user approaches fail because they condition personas on demographic assumptions rather than real user language, introducing systematic bias
- Grounding personas in actual customer feedback removes the most common source of systematic bias while maintaining traceability
- AI handles volume well—processing tens of thousands of feedback entries to identify patterns at speeds human teams cannot match
- AI does not identify systemic problems; it surfaces symptoms that require human judgment to connect to underlying workflow issues
- Synthetic user tools are most useful in validation phases of the design process, less useful for discovery when audiences are new
- The distinction between tool as precursor versus substitute matters most when stakes are highest and products serve underrepresented users
- Tool placement is key—it augments priorities, effort, time, and efficiency rather than replacing human research

## Limitations & Critiques
The tool depends on organizations having continuous VoC collection at meaningful volume, limiting applicability to organizations without established feedback pipelines. The tool cannot simulate first-time users opening something new with no prior context—navigation and discoverability are its clearest blind spots. AI cannot understand mental models or simulate prior product experience. The tool's persona output should be treated as grounded hypotheses requiring human confirmation, not substitutes for user research. Standard content analysis calls for multiple independent coders to establish inter-rater reliability, which was not done. The tool draws on gated VoC data accessible through the author's dual role as UX researcher and PhD student, creating replication challenges.
