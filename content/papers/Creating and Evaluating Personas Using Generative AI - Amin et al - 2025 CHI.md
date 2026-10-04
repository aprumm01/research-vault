---
source_file: synth users/Creating and Evaluating Personas Using Generative AI - Amin
  et al - 2025 (CHI).pdf
type: paper
authors: Danial Amin
community: GenAI in UX and Design Practice
tags: null
year: 2025
builds_on:
- '[[frameworks/Human-Centered Design]]'
- '[[methods/Persona Development]]'
- '[[concepts/Synthetic Users]]'
critiques: []
tensions_with:
- '[[concepts/Human-in-the-Loop Pedagogy]]'
- '[[frameworks/Human-Centered AI]]'
supports:
- '[[concepts/Circularity Risk]]'
- '[[concepts/AI Hallucinations]]'
- '[[concepts/Prompt Engineering]]'
- '[[concepts/Human-AI Co-creation]]'
- '[[concepts/De-skilling]]'
key_claims:
- 86% of GenAI persona studies rely exclusively on GPT models, limiting diversity
  of approaches and creating potential monoculture in persona development practices
- 45% of GenAI persona articles lack evaluation of their personas, representing a
  critical gap in validation and quality assurance
- 61% of articles share resources (personas, code, or datasets) demonstrating relatively
  good reproducibility practices in an emerging field
- Circularity risk emerges when the same GenAI model both generates and evaluates
  personas, creating fundamental validation problems that undermine reliability
- GenAI enables interpretive tasks like narrative writing and contextual summarization
  in persona creation that previous automatic methods could not achieve, but risks
  reducing essential human involvement and stakeholder engagement
methodology: '[[methods/Literature Review]]'
sample_size: 81
sample_type: academic articles on GenAI in persona development
context: published articles from 2022-2025 across five academic databases
study_type: review
---

# Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 (CHI)

## Summary
This scoping review analyzes 81 articles published between 2022-2025 on the application of generative AI in persona development. The review reveals that GenAI is increasingly used to automate persona creation, moving beyond traditional manual qualitative methods. Key findings include: 61% of articles share resources (personas, code, or datasets) showing good reproducibility; 86% rely exclusively on GPT models; 45% of articles lack evaluation of their GenAI personas; and conversational persona interfaces are becoming more common alongside traditional static profiles. The review identifies critical risks including circularity (where the same GenAI model both generates and evaluates personas), reduced role of human developers in the creation process, and ethical concerns around algorithmic bias and representation. Authors propose actionable guidelines for responsible GenAI integration in persona development, emphasizing the need for human-in-the-loop approaches and robust evaluation frameworks.

## Key Concepts
- **GenAI personas**: Personas created using generative AI technologies, particularly large language models (LLMs)
- **Automatic persona development**: Generating personas with minimal or no human involvement
- **Circularity risk**: When the same GenAI model both generates and evaluates outputs, creating validation problems
- **Conversational persona interfaces**: Interactive, dialogue-based persona systems enabled by LLMs (vs. traditional static profiles)
- **Human-in-the-loop**: Maintaining human involvement and decision-making in GenAI-assisted persona creation
- **Prompt engineering**: Crafting instructions for LLMs to perform persona development tasks
- **Hallucinations**: LLM tendency to fabricate information not grounded in source data

## Theoretical Framework
Builds on established persona theory from HCI and UCD literature (Cooper, Pruitt & Grudin, Nielsen). Integrates automatic persona generation research that predates LLMs (An et al., Chapman & Milham) with emerging GenAI capabilities. Draws on recent work examining GenAI risks in persona development (Amin et al. 2024) and traditional persona validation frameworks (Chapman & Milham, Matthews et al.). Positions GenAI personas within the evolution from manual qualitative methods to data-driven approaches to LLM-augmented generation.

## Methods
**Scoping review methodology** following HCI literature review guidelines (Kitchenham & Brereton). Searched five academic databases (ACM Digital Library, IEEE Xplore, Web of Science, Scopus, arXiv) from 2022-August 2025. Initial search yielded 885 articles; after screening with inclusion/exclusion criteria, 90 remained. Backward and forward snowball sampling added 3 more articles. Final corpus: 81 articles after detailed screening removed 12. Used phrase matching to avoid false positives from "personality" terms. Database-specific query adaptations required for syntax compatibility. Extraction focused on: GenAI technologies used, persona development stages, evaluation methods, ethical considerations, and reproducibility (shared resources).

## Main Arguments
- GenAI, particularly LLMs, addresses longstanding limitations in automatic persona generation by enabling interpretive tasks like narrative writing and contextual summarization that previous AI struggled with
- Current GenAI persona practices lack standardization and best practices, with heavy reliance on a single model family (GPT) limiting diversity of approaches
- Evaluation remains a critical gap: nearly half of studies lack persona validation, and methods range widely from automated metrics to user studies without consensus
- Circularity in evaluation creates validity concerns when the same model generates and judges its own outputs
- GenAI risks reducing human involvement in persona creation, potentially undermining stakeholder engagement that traditionally builds buy-in for persona techniques
- Ethical challenges are amplified by GenAI, including algorithmic bias, representation of marginalized groups, data privacy, and transparency concerns
- Conversational persona interfaces represent an evolution beyond static profiles, but their implications for UX practice remain underexplored
- Good reproducibility practices (61% sharing resources) suggest the field is establishing some methodological rigor despite other gaps

## Limitations & Critiques
Review acknowledges rapid evolution of GenAI field means findings may quickly become dated. Scoping review methodology maps breadth but does not systematically assess quality of individual studies. Search limited to English-language articles in selected databases; gray literature and non-English sources excluded. Heavy reliance on GPT models in corpus reflects both market dominance and potential publication bias. Does not empirically test proposed guidelines for responsible GenAI persona development. Ethical considerations identified from existing literature but lacks primary data on actual harms or impacts on represented user groups.

## Related Papers
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/From Disruptions to Discussions How GenAI Impacts Human Interactions in Software]]
- [[papers/Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation]]
- [[papers/Towards Distributed Creativity Understanding Generative AI in th]]
## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community

