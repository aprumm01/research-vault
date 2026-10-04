---
source_file: Co-Constructed or Constrained How AI Collaboration Tools Reshape UI Design
  Practice in a Time-Boxed Design Challenge.pdf
type: paper
authors: Charlotte Kobiella, Lukas Schneider, Albrecht Schmidt, Nađa Terzimehić
community: GenAI in UX and Design Practice
tags: null
year: 2026
builds_on:
- '[[frameworks/Creativity Support Tools]]'
- '[[concepts/Design Fixation]]'
- '[[frameworks/Human-Centered Design]]'
critiques: []
tensions_with:
- '[[concepts/AI-driven Creativity]]'
- '[[concepts/Democratization of Design]]'
supports:
- '[[concepts/Design Fixation]]'
- '[[concepts/Visual Homogenization]]'
- '[[concepts/Cognitive Offloading]]'
- '[[concepts/De-skilling]]'
- '[[concepts/Ownership Ambiguity]]'
- '[[concepts/AI Tool Dependence]]'
key_claims:
- AI-assisted design shifts from an additive process (building iteratively from scratch)
  to a subtractive process (refining AI-generated drafts through deletion and modification),
  fundamentally changing the nature of creative decision-making in UI design
- NASA-TLX workload scores showed significantly lower perceived cognitive workload
  for AI-assisted tasks compared to conventional design tasks, but participants reported
  narrower design exploration and reduced feelings of ownership and accomplishment
- Computational analysis revealed that AI-assisted UI designs were more visually and
  structurally homogeneous than manually created designs, clustering more tightly
  in visual and structural feature space and providing empirical evidence for design
  diversity concerns
- AI-generated starting points introduce fixation risks distinct from example-based
  inspiration because they are immediately actionable, making it harder for designers
  to maintain critical distance and explore alternative directions
- Professional designers with greater expertise developed adaptive strategies over
  time, using AI for initial structure then deliberately breaking from it, suggesting
  that expertise enables more strategic AI collaboration
methodology: '[[methods/Mixed Methods]]'
sample_size: 16
sample_type: professional UX designers with varying seniority and company sizes
context: High-fidelity UI design tasks completed with FigmaAI in professional design
  tool environment
study_type: empirical
---

# Co-Constructed or Constrained? How AI Collaboration Tools Reshape UI Design Practice in a Time-Boxed Design Challenge

## Summary
This CHI 2026 paper presents a within-subject study with 16 professional UX designers who completed high-fidelity UI design tasks both conventionally and with FigmaAI. Through think-aloud protocols, semi-structured interviews, post-task questionnaires, and computational analysis of resulting interfaces, the study finds that GenAI shifts UI design from an additive to a subtractive process — designers refine AI drafts rather than build from scratch. While AI reduces workload, it also constrains exploration, limits perceived ownership, and produces more visually homogeneous outputs.

## Key Concepts
- **Additive vs. subtractive design processes**: The core finding — conventional design is additive (building iteratively from nothing), while AI-assisted design is subtractive (starting with an AI draft and removing/refining toward the intended result)
- **FigmaAI**: The specific GenAI feature within Figma studied — an embedded generative tool that can create initial UI layouts, suggest components, and generate design drafts from text prompts within the professional design environment
- **Design fixation**: The risk that exposure to AI-generated designs constrains ideation by anchoring designers to early AI outputs, reducing the breadth of design exploration
- **Perceived ownership and authorship**: Designers' sense of creative agency over their work — which several participants reported being undermined by AI-generated starting points
- **Visual and structural homogenization**: The computational analysis finding that AI-assisted designs were more visually and structurally similar to each other than manually created designs, suggesting convergence toward AI's training distribution
- **NASA-TLX workload measure**: The validated cognitive load instrument used to show that AI-assisted tasks had significantly lower perceived workload

## Theoretical Framework
The paper is grounded in Creativity Support Tools (CST) research in HCI, drawing on the foundational "grand challenge" framing of CSTs and subsequent work on their limitations in professional contexts. It engages with design fixation research (the tendency to anchor on existing examples), inspiration-seeking literature (serendipitous browsing vs. targeted search), and human-AI collaboration research on how AI affects creative identity and experienced competence.

The conceptual contribution — the additive/subtractive distinction — is inductively derived from the data and represents the paper's primary theoretical advance. The paper also engages with the research-practice gap literature, arguing that studying embedded professional tools in real workflows provides more ecologically valid insights than lab prototypes.

## Methods
Within-subject study with 16 professional UX designers (varying seniority and company size). Each participant completed two high-fidelity UI design tasks: one with conventional Figma (no AI), one with FigmaAI. Counterbalancing was used to control for order effects. Sessions involved concurrent think-aloud protocols, capturing 25 hours and 51:50 minutes of video recordings total. Post-task semi-structured interviews explored experiences and reflections. Post-task questionnaires included the NASA-TLX workload scale. Computational analysis of resulting UI artifacts measured visual and structural characteristics (element types, layout patterns, color distributions) to compare AI-assisted vs. manual outputs objectively.

## Main Arguments
- **AI-assisted design shifts from additive to subtractive process**: Rather than building iteratively from a blank canvas, designers using FigmaAI began with an AI-generated draft and refined it through deletion, replacement, and modification — fundamentally changing the nature of creative decision-making.
- **AI reduced cognitive workload but constrained exploration**: NASA-TLX scores showed significantly lower perceived workload for AI-assisted tasks, but participants reported feeling their design exploration was narrower — they stayed closer to AI-generated directions rather than pursuing alternative ideas.
- **Perceived ownership and accomplishment were undermined**: Multiple participants questioned whether they could claim authorship of AI-assisted designs, and reported reduced feelings of accomplishment compared to manually created work — even when the AI-assisted outputs were comparable in quality.
- **AI-assisted interfaces were computationally more homogeneous**: The computational analysis revealed that AI-generated designs clustered more tightly in visual and structural feature space than manual designs, providing empirical evidence for the design diversity concern.
- **AI introduced fixation risks specific to generative tools**: Unlike example-based inspiration (where designers choose what to look at), AI-generated starting points are immediately actionable, making it harder to maintain critical distance and explore alternatives.
- **Professional designers developed adaptive strategies over time**: Participants who were initially frustrated by AI constraints developed workarounds — using AI for initial structure then deliberately breaking from it — suggesting that expertise enables more strategic AI collaboration.

## Limitations & Critiques
The within-subject design with 16 participants, while appropriate for the research questions, limits statistical power and generalizability. The 22-minute time-boxed task format may exaggerate AI's workload reduction benefits (the main advantage of AI in reducing repetitive setup work) compared to longer, more complex real-world projects. The study focuses specifically on UI design (screen-level visual work), not the broader UX design process including research and information architecture.

The computational similarity analysis methodology is novel but not fully validated — the specific metrics chosen (element counts, color distributions) may not fully capture the perceptual and conceptual dimensions of design diversity. The study cannot determine whether the observed homogenization persists in extended workflows or whether it diminishes as designers develop more sophisticated AI integration strategies.

## Connections
- [[communities/GenAI_in_UX_and_Design_Practice]] - Research community
- [[methods/Within_Subject_Study]] - if applicable
- [[frameworks/Creativity_Support_Tools]] - if applicable
