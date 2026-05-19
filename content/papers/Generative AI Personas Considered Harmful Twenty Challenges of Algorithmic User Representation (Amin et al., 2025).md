---

source_file: "research_docs/P451.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Amin, Salminen, Jansen, Shin, and Kim systematically analyze twenty challenges of using generative AI in persona development, organized by Shneiderman"
---

# Generative AI Personas Considered Harmful? Twenty Challenges of Algorithmic User Representation in HCI (Amin et al., 2025)

## Summary
Amin, Salminen, Jansen, Shin, and Kim systematically analyze twenty challenges of using generative AI in persona development, organized by Shneiderman's Human-Centered AI (HCAI) principles (transparency, fairness, reliability, control, privacy, safety, user experience). Inspired by Dijkstra's "Go To Statement Considered Harmful," the paper combines a literature review of twenty challenges with an expert survey of seventeen persona researchers. Experts rated all twenty challenges as problematic (mean > 4.0 out of 7), with highest concerns for hallucinations (M=5.94), over-sanitization (M=5.82), and lack of standardization (M=5.59). Twelve of twenty challenges were rated as more problematic for GenAI personas than for conventional personas. The authors conclude that GenAI transforms rather than eliminates traditional persona challenges and that responsible implementation requires human-AI collaboration prioritizing user welfare over technical efficiency.

## Key Concepts
- Twenty challenges organized under seven HCAI principles: transparency, fairness, reliability, control, privacy, safety, user experience
- Hallucination as the top concern (M=5.94): GenAI fabricates plausible but unverifiable user characteristics
- Over-sanitization (M=5.82): GenAI systematically scrubs negative, taboo, or extreme user perspectives
- Lack of standardization (M=5.59): no agreed protocols for prompt design, evaluation, or disclosure
- Dijkstra's "considered harmful" framing applied to persona design practice
- 12 of 20 challenges rated worse for GenAI than for conventional DDPs

## Theoretical Framework
Shneiderman's HCAI framework (2022) as organizing structure; persona science tradition (Cooper, Nielsen, Salminen); challenge taxonomy derived from systematic literature review and expert survey; three analysis phases: snowball sampling, empirical case studies of four published GenAI persona studies, expert survey (n=17 persona researchers); published in International Journal of Human-Computer Studies (2025).

## Methods
Snowball literature sampling to identify and map twenty challenges; empirical case study analysis of four published GenAI persona studies showing how challenges manifest; expert survey with 17 subject matter experts (persona researchers and practitioners) rating each challenge on severity (1-7 Likert) and comparing GenAI personas to conventional DDPs; descriptive statistics and challenge rankings analyzed; stakeholder impact framing across persona developers, persona users, and represented target groups.

## Main Arguments
- GenAI transforms traditional persona challenges into amplified, algorithmic-scale versions rather than solving them: bias becomes algorithmic bias at scale, validation difficulty becomes opacity, inconsistency becomes hallucination with convincing fabricated content
- Hallucination is the most severe challenge: unlike human-authored errors, GenAI hallucinations present as plausible, polished content, making them harder to detect and more dangerous in design decision contexts
- Over-sanitization -- GenAI's tendency to suppress extreme, taboo, or marginal user perspectives -- is a critical concern for representing underserved groups or edge-case users who most need HCD attention
- Responsible GenAI persona use requires human-AI collaboration structures, explicit bias detection protocols, and institutional disclosure norms rather than relying on automation alone

## Limitations & Critiques
Expert survey has small n (17) and may reflect the biases of an already specialized academic community; the twenty challenges were identified through literature review by the authors and may not be exhaustive; the HCAI framework is applied as a descriptive lens rather than tested empirically; most challenge severity ratings reflect expert perception rather than measured real-world impact; the paper does not present a validated mitigation framework, only principles.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Creating and Evaluating Personas Using Generative AI A Scoping Review (Amin et al., 2026)]] - companion scoping review by same first authors
- [[Responsible AI and Ethics]] - `` [EXTRACTED]
