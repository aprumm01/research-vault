---
source_file: "synth users/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025.pdf"
type: paper
authors: "SONJA M.H. TERVOLA, Aalto University, Finland"
community: "GenAI in UX and Design Practice"
tags:
---

# Creating and Evaluating Personas Using Generative AI - Amin et al - 2025

## Summary
This scoping review (arXiv version) analyzes 81 articles published between 2022-2025 examining generative AI application in persona development. Key findings: 61% of studies demonstrate good reproducibility by sharing resources; 86% rely solely on GPT models; 45% lack persona evaluation; conversational persona interfaces are emerging alongside traditional profiles. Critical concerns identified include circularity in evaluation (same model generates and evaluates), diminished human developer involvement, and amplified ethical risks around bias and representation. The review maps current practices, identifies gaps in standardization and best practices, and proposes guidelines for responsible GenAI integration emphasizing human-in-the-loop approaches. Positions GenAI personas within the evolution from manual qualitative methods through data-driven approaches to LLM-augmented generation.

## Key Concepts
- **GenAI personas**: Personas created using generative AI, particularly LLMs
- **Automatic persona development**: Generating personas with minimal human involvement
- **Circularity risk**: Same GenAI model both generates and evaluates outputs
- **Conversational persona interfaces**: Dialogue-based, interactive persona systems vs. static profiles
- **Human-in-the-loop**: Maintaining human decision-making in GenAI-assisted creation
- **Hallucinations**: LLM fabrication of information not grounded in data
- **Prompt engineering**: Crafting LLM instructions for persona tasks
- **User-centered design (UCD)**: Design approach focusing on user needs that personas support

## Theoretical Framework
Builds on HCI persona theory (Cooper, Pruitt & Grudin, Nielsen) and earlier automatic persona generation research (An et al., Chapman & Milham). Integrates traditional persona validation frameworks (Chapman & Milham, Matthews et al.) with emerging GenAI capabilities and risks literature (Amin et al. 2024). Situates work within evolution of persona methods: manual qualitative → data-driven approaches → LLM-augmented generation. Draws on UX/HCI practice literature emphasizing personas as shared reference points for empathy and user-centered decision-making.

## Methods
**Scoping review** following HCI literature review guidelines (Kitchenham & Brereton). Five databases searched (ACM DL, IEEE Xplore, Web of Science, Scopus, arXiv) through August 25, 2025. Query development combined GenAI terms (LLM, GPT, generative AI, etc.) AND persona terms with Boolean operators. Database-specific syntax adaptations required. Initial 885 articles → 90 after inclusion/exclusion screening → 93 after snowball sampling → 81 final corpus after detailed screening. Phrase matching ("persona", "personas") used instead of wildcards to avoid false positives. Data extraction focused on: GenAI technologies used, development stages, evaluation methods, ethical considerations, reproducibility.

## Main Arguments
- LLMs address longstanding automatic persona generation limitations by enabling interpretive tasks (narrative writing, contextual summarization) that previous AI couldn't handle
- Current practice lacks standardization: heavy GPT reliance (86%), varying methodological choices (model family, version, hyperparameters, prompts), no consensus on optimal approaches
- Evaluation gap is critical: 45% of studies lack validation; methods range from automated metrics to user studies without clear frameworks for GenAI-specific concerns (consistency, hallucinations, prompt reliability)
- Circularity creates validity concerns when same model generates and judges its own outputs
- Reduced human involvement risks undermining stakeholder engagement that traditionally builds buy-in for personas
- GenAI amplifies ethical challenges: algorithmic bias, marginalized group representation, data privacy, transparency
- Human-in-the-loop is essential but undertheorized in GenAI persona context
- Conversational interfaces represent paradigm shift from static profiles but implications remain underexplored
- Good reproducibility (61% resource sharing) suggests emerging methodological rigor despite other gaps

## Limitations & Critiques
Scoping review maps breadth but doesn't systematically assess individual study quality. Rapid GenAI evolution means findings may date quickly. English-language articles only; gray literature excluded. Corpus reflects GPT market dominance and possible publication bias. Proposed guidelines lack empirical testing. Ethical considerations drawn from literature not primary data on actual harms. Does not address how awareness of risks varies across HCI researchers implementing GenAI personas. Limited examination of stakeholder attitudes toward GenAI personas vs. traditional approaches.

## Related Papers
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 CHI]]
- [[papers/From Disruptions to Discussions How GenAI Impacts Human Interactions in Software]]
- [[papers/Exploring the Potential of Metacognitive Support Agents for Human-AI Co-Creation]]
- [[papers/Towards Distributed Creativity Understanding Generative AI in th]]
## Connections
- [[communities/GenAI in UX and Design Practice]] - Research community
- [[topics/GenAI into persona]] - Key concept
- [[topics/GenAI use creates]] - Key concept
- [[topics/Generative AI]] - Key concept
- [[topics/Generative AI, LLM, Personas,]] - Key concept
- [[topics/Generative AI: A Scoping]] - Key concept