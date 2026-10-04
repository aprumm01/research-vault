---
title: "The Fast and Spurious: Developer Productivity with GenAI"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Afr25.pdf"
type: paper
authors:
  - Sadia Afroz
  - Zixuan Feng
  - Tyler Menezes
  - Katie Kimura
  - Bianca Trinkenreich
  - Igor Steinmacher
  - Anita Sarma
year: 2026
venue: "FSE'26 (34th ACM Symposium on the Foundations of Software Engineering)"
builds_on:
  - "[[concepts/SPACE Framework]]"
  - "[[concepts/Developer Productivity]]"
  - "[[concepts/DevEx Framework]]"
supports:
  - "[[concepts/Human-AI Collaboration]]"
  - "[[concepts/AI Productivity]]"
critiques:
  - "[[concepts/GenAI Environmental Impact]]"
tensions_with:
  - "[[concepts/Developer Tools]]"
key_claims:
  - GenAI productivity gains are often "spurious" - surface-level acceleration accompanied by hidden costs and effort redistribution
  - Effort saved in one SPACE dimension frequently resurfaces in another dimension
  - Frequent GenAI users report faster task completion but increased code review burden
  - Communication and collaboration patterns remain largely unchanged with GenAI adoption
  - High levels of developer exhaustion persist despite AI adoption due to cognitive load from output verification
  - Organizations should use SPACE as a holistic framework rather than single activity metrics to evaluate GenAI productivity
methodology: Survey with mixed methods (quantitative Likert-scale analysis and qualitative open-ended coding)
study_type: empirical
context: Software development, GenAI tools (GitHub Copilot, ChatGPT), developer productivity measurement
---

# The Fast and Spurious: Developer Productivity with GenAI

## Summary

This paper investigates how GenAI adoption affects developer productivity across multiple dimensions using the SPACE framework (Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow). The authors surveyed 415 professional developers from 56 open source communities to understand perceived productivity changes associated with AI adoption. The study uses both quantitative analysis of Likert-scale responses and qualitative coding of open-ended responses to map productivity impacts across all five SPACE dimensions.

The central finding is that GenAI productivity gains are often "spurious" - appearing as surface-level acceleration but accompanied by redistributed effort and hidden costs. While frequent GenAI users reported faster task completion and higher output volume in Activity metrics, these gains were offset by increased code review burden, persistent cognitive load from output verification, and unchanged collaboration patterns. The paper introduces the concept of a "constraint redistribution problem" where improvements in Activity and Efficiency dimensions create new demands in Satisfaction, Performance, and Communication dimensions.

The study identifies seven productivity-related challenges and eight potential mitigation strategies mapped onto the SPACE dimensions. Key challenges include AI-induced cognitive workload from verifying outputs, review burden from others' AI-generated code, organizational pressure for higher output, verbosity of AI outputs affecting test quality, and reliance on AI before acquiring foundational knowledge. Proposed strategies include structured organizational training, team norms framing GenAI as assistive rather than replacement, confidence indicators in AI outputs, integrating GenAI with project-specific context, and quality gates for AI-heavy changes.

The authors conclude that at the current stage of GenAI adoption, organizations focusing solely on activity-level metrics may incorrectly conclude that GenAI is effective, while those assessing performance outcomes may reach different conclusions. They recommend using SPACE as a comprehensive planning framework to identify where effort will shift before deploying AI-assisted code generation.

## Key Concepts

- **SPACE Framework**: Multidimensional productivity framework with five dimensions: Satisfaction and well-being, Performance, Activity, Communication and collaboration, and Efficiency and flow
- **Spurious Productivity**: Surface-level acceleration that obscures stagnant or redistributed effort across dimensions
- **Constraint Redistribution Problem**: Phenomenon where GenAI-facilitated improvements in one dimension create demands in others
- **Cognitive Load from Verification**: Mental effort required to continuously evaluate AI suggestions, contributing to exhaustion despite efficiency gains
- **Review Burden**: Increased time spent reviewing others' AI-generated code that is often verbose or low-quality

## Key Findings

**Satisfaction and Well-being (S)**:
- More developers report manageable workloads and increased job security
- However, high levels of exhaustion persist despite AI adoption (65.2% still feel exhausted)
- ~46-60% of participants became less interested in work

**Performance (P)**:
- Higher coding throughput with frequent GenAI use (72.7% report increase)
- Test success rates show little to no improvement
- Learning velocity remains largely unchanged

**Activity (A)**:
- Increased output of commits, test cases, and completed work items
- Reduced time on direct code writing
- Increased involvement in code review activities (84.3% report no reduction in review time)
- Frequent AI users more likely to conduct more code reviews (25.1% vs 9.8%)

**Communication and Collaboration (C)**:
- Team communication patterns remain largely unchanged with GenAI use
- More than 70% of frequent AI users report "No Change" across all communication items
- Meetings and email-related activities show little to no reduction

**Efficiency and Flow (E)**:
- Reduced time on individual work items (35.8% vs 82.2%)
- Reduced time on non-work-related web browsing
- Improvements in sustained focus and flow are limited

## Relevance to Sustainable Computing / AI Productivity

This paper is highly relevant to understanding the true nature of AI-mediated productivity in knowledge work. The concept of "spurious productivity" directly challenges simplistic claims about GenAI efficiency gains and suggests that organizations may be overlooking significant hidden costs. The finding that cognitive load and exhaustion persist despite efficiency gains raises questions about the sustainability of current GenAI integration approaches.

For sustainable computing, the paper implies that simply measuring output metrics (commits, lines of code) provides a misleading picture of AI tool effectiveness. The redistribution of effort - particularly toward verification, review, and debugging of AI-generated content - suggests that total human effort may not decrease substantially even as specific task completion accelerates. This has implications for calculating the true cost-benefit of AI assistance, including the environmental costs of AI compute relative to actual (vs. perceived) productivity gains.

The paper's recommendation to use SPACE as a planning framework before deploying AI tools provides a methodological contribution for organizations seeking sustainable AI integration that genuinely reduces total effort rather than merely shifting it between activities.

## Citation

Afroz, S., Feng, Z., Menezes, T., Kimura, K., Trinkenreich, B., Steinmacher, I., & Sarma, A. (2026). The Fast and Spurious: Developer Productivity with GenAI. In *Companion Proceedings of the 34th ACM Symposium on the Foundations of Software Engineering (FSE '26)*, June 5-9, 2026, Montreal, Canada. ACM.
