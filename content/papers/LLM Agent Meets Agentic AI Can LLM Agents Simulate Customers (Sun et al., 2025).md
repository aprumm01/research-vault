---

source_file: "research_docs/P453.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2025"
authors: "Sun, Fu, Yao, Lu, Li, Gu, Gesi, Huang, Wang, and Luo"
---

# LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-Based Shopping Assistants? (Sun et al., 2025)

## Summary
Sun, Fu, Yao, Lu, Li, Gu, Gesi, Huang, Wang, and Luo investigate whether LLM customer agents can serve as "digital twins" to evaluate agentic AI-based conversational shopping assistants. They establish human-study ground truth with diverse real customers making a $250 shopping decision, then compare LLM agent twins performing the same task. Analysis focuses on human-agent alignment across three dimensions: shopping decisions, open-ended feedback, and interaction traces. The study finds moderate alignment in shopping decisions and qualitative feedback, but substantial divergence in interaction patterns -- LLM agents are more systematic, less emotionally driven, and make fewer impulsive choices than human shoppers. The paper provides nuanced guidelines for when LLM customer simulation is and is not a valid substitute for human evaluation.

## Key Concepts
- Digital twins: LLM agents conditioned on human participant profiles to simulate their shopping behavior
- Three alignment dimensions: shopping decisions, open-ended feedback, interaction traces
- Behavioral divergence: LLM agents more systematic and rational, humans more emotionally driven
- Ground truth establishment: real human customer study with $250 shopping decision
- Guidelines for valid LLM customer simulation: scenarios where alignment is high vs. low
- Agentic AI shopping assistant evaluation as the practical context

## Theoretical Framework
Builds on generative agents (Park et al.); digital twin literature in HCI and engineering; agentic AI system evaluation; situated within a research collaboration spanning UC San Diego, Northeastern, and Amazon; published as arXiv preprint (September 2025).

## Methods
Human study: diverse real customers making structured $250 shopping decisions with an agentic conversational shopping assistant; each participant profiled (demographics, preferences, shopping history); LLM digital twins created using participant profiles as system prompts; LLM twins performed identical shopping tasks; alignment measured across decisions (purchase selection), feedback (qualitative content), and traces (interaction sequence, query patterns, navigation behavior); mixed quantitative and qualitative analysis.

## Main Arguments
- LLM agents can approximate human customers in structured shopping scenarios when the decision criteria are well-defined and product information is available, but diverge substantially in emotionally-driven and impulse-driven decisions
- The interaction trace is the most revealing alignment dimension: while final decisions and feedback can look similar, the path to get there differs systematically between human and LLM agents
- LLM simulation is most valid for evaluating the functional correctness of agentic shopping assistants (did it help the customer achieve a goal?) but least valid for evaluating experiential quality (did it feel natural, satisfying, or trustworthy?)
- The digital twin approach is more rigorous than generic persona simulation because it anchors each LLM agent to a real human participant's profile

## Limitations & Critiques
Single shopping context ($250 decision) limits generalizability; the shopping assistant being evaluated is itself an LLM-based system, creating potential for shared training data effects; human study sample size and demographic composition are not specified in detail; the alignment metrics do not include standardized validity tests; results may not generalize beyond e-commerce domains.

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[Digital Twins]] - `` [EXTRACTED]
- [[Agent AB Automated and Scalable AB Testing on Live Websites with LLM Agents (Lu et al., 2025)]] - overlapping author team, related evaluation context
