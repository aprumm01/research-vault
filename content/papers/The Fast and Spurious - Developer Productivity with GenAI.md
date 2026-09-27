---
source_file: "2026/i609-sustainability/Afr25.pdf"
type: paper
authors: "Sadia Afroz, Zixuan Feng, Tyler Menezes, Katie Kimura, Bianca Trinkenreich, Igor Steinmacher, Anita Sarma"
community: "Sustainable Computing"
tags: [sustainability, i609, GenAI, developer-productivity, software-engineering, SPACE-framework]
---

# The Fast and Spurious: Developer Productivity with GenAI

## Summary

This 2026 paper by Afroz et al., published at the ACM Symposium on the Foundations of Software Engineering (FSE'26), presents empirical research on how Generative AI (GenAI) adoption affects developer productivity across multiple dimensions. The research team spans Oregon State University, CodeDay, Colorado State University, and Northern Arizona University, bringing expertise in software engineering, human-computer interaction, and developer experience research. The study surveyed 415 professional software developers using the SPACE framework (Satisfaction, Performance, Activity, Communication, Efficiency and flow) to assess perceived productivity changes. The paper's significance lies in challenging the prevailing narrative that GenAI tools like GitHub Copilot and ChatGPT uniformly boost productivity, instead revealing a pattern of "spurious productivity"—surface-level acceleration accompanied by hidden costs and effort redistribution. This research is relevant to sustainable computing because it examines the hidden human and organizational costs of AI-assisted development, with implications for understanding whether AI tools genuinely improve efficiency or merely shift effort to different activities.

## Research Overview

The paper addresses two research questions: "RQ1. How does GenAI adoption affect developer productivity across multiple dimensions?" and "RQ2. What productivity-related gaps, challenges, and strategies do developers perceive in GenAI adoption?" (Afroz et al., 2026, p. 2).

The methodology combined quantitative survey analysis with qualitative thematic coding. The researchers "conducted a large-scale survey of 415 professional developers grounded in the SPACE framework" (Afroz et al., 2026, p. 2), recruiting from 56 open-source communities including IBM, Oracle, Google, and data science projects like PyTorch. Participants were categorized as frequent (Often, Always) or non-frequent (Never, Rarely, Sometimes) GenAI users based on self-reported usage frequency.

Key concepts include the **SPACE framework**, which "conceptualizes productivity as a combination of interpersonal and technical dimensions" emphasizing that "productivity arises from the interplay among human, technical, and organizational factors" (Afroz et al., 2026, p. 2). The framework comprises five dimensions: **Satisfaction and well-being** (fulfillment, motivation, support), **Performance** (quality and impact of outcomes), **Activity** (volume of work performed), **Communication and collaboration** (team interaction), and **Efficiency and flow** (progress with minimal interruptions).

Qualitative analysis of 206 open-ended responses achieved "90% agreement on inter-rater reliability" using the Jaccard index, identifying seven challenges and eight potential strategies mapped to SPACE dimensions.

## Theoretical Framework

The SPACE framework, proposed by Forsgren et al. (2021), serves as the primary theoretical lens. It "views productivity as a system of interdependent dimensions rather than isolated metrics. High activity without corresponding performance gains may indicate redistributed rather than reduced effort" (Afroz et al., 2026, p. 2).

The paper critiques traditional productivity metrics: "Traditional metrics such as lines of code (LoC), commit counts, and task completion rates capture only narrow aspects of work and can be misleading or easily gamed" (Afroz et al., 2026, p. 2). This aligns with Brooks' observation from *The Mythical Man-Month* that "there can be no single metric for programmer productivity, and that attempts to find one typically measure volume rather than performance" (Afroz et al., 2026, p. 8).

The concept of **spurious productivity** is central: perceived productivity gains that are "surface-level acceleration, often accompanied by redistributed effort and hidden costs" (Afroz et al., 2026, p. 1). This connects to concerns about **technical debt** where "Moreschini et al. showed that GenAI can incur prompt engineering debt and explainability debt, leaving teams with code that may 'work' but lacks clarity, testability, or adaptability" (Afroz et al., 2026, p. 1).

The **Developer Experience (DevEx) framework** is referenced as complementary, "which highlights feedback loops, cognitive load, and flow state as key drivers of developer effectiveness" (Afroz et al., 2026, p. 2).

## Central Arguments

The paper's central argument is that GenAI adoption creates a "constraint redistribution problem" where "effort saved in one SPACE dimension often resurfaces in another" (Afroz et al., 2026, p. 4). The authors contend that "at the current stage of GenAI adoption, perceived productivity gains may be spurious—surface-level acceleration, often accompanied by redistributed effort and hidden costs" (Afroz et al., 2026, p. 1).

Supporting sub-claims include:

1. **Activity gains offset by review burden**: "While frequent GenAI users reported faster task completion and higher output volume, these gains were offset by increased code review burden, persistent cognitive load from output verification, and unchanged collaboration patterns" (Afroz et al., 2026, p. 1). Specifically, "the majority of frequent users (84.3%) reported that GenAI did not reduce the time spent on code reviews" (Afroz et al., 2026, p. 8).

2. **Cognitive load from verification**: "AI-generated code unfairly puts more onus on code reviewers to understand how the code works and find bugs or security issues" (Afroz et al., 2026, p. 5, quoting participant P204).

3. **Limited collaboration impact**: "More than three-quarters of all users reported no positive change" in communication and collaboration, with "No Change responses dominate across all four items, exceeding 70% in each case" (Afroz et al., 2026, p. 6).

4. **Persistent exhaustion**: Despite efficiency gains, "more than half of respondents still reported feeling exhausted (S2: 65.2% vs. 62.8%)" (Afroz et al., 2026, p. 4).

## Evidence

The study provides substantial quantitative evidence. Regarding Activity dimension gains: "a larger share of frequent users reported producing more commits (A1): 48.3% vs 7.9%; more test cases (A3): 56.5% vs 24.8%; and completing more work items (A5): 55.9% vs 9.1%, compared to non-frequent users" (Afroz et al., 2026, p. 5).

However, Performance gains are limited: "Non-frequent AI users predominantly reported no change in work quality or outcomes across performance-related items (P1: 66.7%, P2: 83.1%, P3: 66.7%)" while frequent users showed mixed results with "test case pass rates (P2) and learning velocity (API methods learned per day, P3), most of the frequent AI users—67.4% and 58.6% respectively—reported no change or a decline" (Afroz et al., 2026, p. 5).

Qualitative evidence includes participant quotes revealing hidden costs: "I spend more time reviewing code and docs wastes time — coworkers are (accidentally but carelessly) sabotaging our work by 'creating work'. The LLMs save these coworkers time because they are faster at producing content, but other coworkers have to spend disproportionately more time to review and correct all that content" (Afroz et al., 2026, p. 5, P127).

**Limitations** acknowledged include reliance on self-reported perceptions rather than objective productivity outcomes, and that "no single sample can fully represent the global software workforce" though the dataset "includes 415 software practitioners from 56 organizations, which is comparable in scale and diversity to prior empirical studies" (Afroz et al., 2026, p. 8). The study does not measure environmental costs of GenAI usage.

## Conclusion

For recall six months from now, this paper provides critical empirical evidence that GenAI productivity gains in software development are often "spurious"—apparent acceleration that redistributes rather than reduces total effort. Using the SPACE framework across 415 developers, key findings are: (1) Activity increases (more commits, test cases, completed items) for frequent GenAI users; (2) No corresponding Performance improvements in test pass rates or learning velocity; (3) Dramatically increased code review burden with 84.3% reporting no time reduction; (4) Persistent developer exhaustion despite efficiency features; (5) Unchanged team communication and collaboration patterns. Seven challenges mapped to SPACE dimensions include cognitive load from verification (Ch1), review burden of others' AI outputs (Ch2), organizational pressure from "AI = faster output" expectations (Ch3), verbosity of AI outputs (Ch4), and reliance on AI before acquiring foundational knowledge (Ch5). Eight strategies include organizational training on GenAI (St1), framing GenAI as assistive rather than replacement (St2), confidence indicators and explanation norms (St3), and quality gates for AI-heavy changes (St7). The sustainability relevance is indirect but important: if GenAI tools shift effort rather than reduce it, the energy costs of running these services may not be offset by genuine productivity gains.

## APA Citation

Afroz, S., Feng, Z., Menezes, T., Kimura, K., Trinkenreich, B., Steinmacher, I., & Sarma, A. (2026). The fast and spurious: Developer productivity with GenAI. In *Companion Proceedings of the 34th ACM Symposium on the Foundations of Software Engineering (FSE '26)*, June 5-9, 2026, Montreal, Canada. ACM. https://doi.org/XXXXXXX.XXXXXXX

## Discussion Questions

1. If GenAI tools redistribute effort rather than reduce it (e.g., from code writing to code review), what are the implications for the environmental sustainability claims made by AI companies about productivity improvements?

2. How should organizations measure "true" productivity gains from GenAI adoption, and what role should the SPACE framework play in evaluating AI tools before widespread deployment?

3. The paper identifies "spurious productivity" where surface metrics improve while total effort remains constant. How might this concept apply to other AI-augmented work contexts beyond software development?

4. Given that 84.3% of frequent GenAI users reported no reduction in code review time despite faster code generation, what organizational policies might address this effort redistribution problem?


## Related Papers
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025]]
- [[papers/Generative AI Personas Considered Harmful - Amin et al - 2025]]
- [[papers/Creating and Evaluating Personas Using Generative AI - Amin et al - 2025 CHI]]
- [[papers/From Disruptions to Discussions How GenAI Impacts Human Interactions in Software]]
## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/AI Ethics]]
- [[topics/Developer Experience]]
- [[topics/Technical Debt]]
