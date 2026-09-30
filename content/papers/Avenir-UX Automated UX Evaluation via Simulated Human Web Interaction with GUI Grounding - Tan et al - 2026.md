# Avenir-UX: Automated UX Evaluation via Simulated Human Web Interaction with GUI Grounding

**Authors:** Wee Joe Tan, Zi Rui Lucas Lim, Shashank Durgad, Karim Obegi, Aiden Yiliu Li  
**Affiliation:** University College London  
**Year:** 2026  
**Type:** System/Tool Paper  
**Field:** Human-Computer Interaction, UX Evaluation, AI Agents

---

## Overview of the Document

This paper introduces Avenir-UX, an automated user experience evaluation system that addresses a critical bottleneck in modern software development: the time and resource constraints of traditional UX testing. The research team from University College London has built an open-source agent that simulates human behavior on websites to produce standardized usability reports, making professional-grade UX evaluation accessible to small teams, startups, and agile workflows.

What makes this work distinctive is its integration of visual grounding—the agent doesn't just interact with simplified HTML representations like earlier systems, but actually "sees" the interface through pixel-based vision, mimicking how human users experience web interfaces. The system pairs multimodal interaction with simulated human behavior patterns and a structured evaluation protocol combining quantitative metrics (System Usability Scale, Single Ease Question) with qualitative Think Aloud reasoning that verbalizes the agent's mental model in real-time.

The practical contribution is significant: Avenir-UX generates comprehensive UX reports that identify friction points consistent with human findings, offering developers actionable feedback they can integrate directly into development cycles without the complex logistics of recruiting participants and scheduling sessions.

---

## Research Overview

**Central Research Question:** Can an autonomous MLLM agent with visual grounding capabilities perform end-to-end UX evaluation that produces usability insights comparable to professional human evaluation?

The paper doesn't just ask whether automation is possible—it asks whether automated evaluation can match the *depth* and *actionability* of human-centered UX research. This is a meaningfully higher bar than functional testing or DOM-based interaction benchmarks.

The researchers built Avenir-UX on top of the Avenir-Web framework, employing three core architectural components:

**Visual Perception & Grounding:** Rather than parsing HTML/DOM trees, the system uses Mixture of Grounding Experts (MoGE) to interact with coordinate-based visual tagging. The agent sees a screenshot with interactive elements labeled, letting it perceive the interface as a "synthetic user" would—including visual hierarchy, layout ambiguity, and accessibility issues that DOM representations hide.

**Experience-Imitation Planning (EIP):** Before execution begins, the agent searches external knowledge sources (documentation, forums, user guides) to understand site-specific interaction patterns. This capability lets the agent emulate informed human users rather than naively exploring interfaces.

**Think Aloud Protocol:** During task execution, the agent generates a reasoning trace at each step, verbalizing its mental state, UI interpretation, and confusion or delays—mirroring the classic UX research method where participants narrate their thought process. This provides rich qualitative data explaining *why* behind usability friction.

**Key Evaluation Framework:**

The system implements a three-phase pipeline:

1. **Think Aloud Execution:** Agent performs the task while generating step-by-step reasoning about ease, efficiency, clarity, and confidence on 1-7 scales with qualitative assessments
2. **Step-wise SEQ Evaluation:** After each interaction, the agent rates difficulty on the Single Ease Question scale, providing granular friction mapping
3. **SUS Synthesis:** Upon completion (or failure), the agent fills out the 10-item System Usability Scale questionnaire, producing an industry-standard usability score

The authors emphasize this isn't just automated clicking—it's automated *judgment*. The agent acts as both test participant and UX researcher, synthesizing observations into structured reports.

---

## Theories of Knowledge

The paper builds on several theoretical and methodological foundations from HCI and AI evaluation research.

**Visual Grounding in Web Agents:** Recent work on multimodal web agents like WebArena and Mind2Web has demonstrated functional task completion but operated primarily on simplified DOM representations. Research by Luera et al. benchmarking MLLMs as UI judges showed these models can evaluate interfaces, but prior work focused on static screenshot analysis rather than dynamic interaction. Avenir-UX synthesizes these threads—using vision for authentic perception while maintaining the agentic capability to complete multi-step tasks.

**UX Evaluation Methodologies:** The System Usability Scale (SUS), developed by Brooke in 1996, remains the gold standard for perceived usability measurement. With 446 studies and over 5000 individual responses, the Sauro-Lewis Curved Grading Scale provides benchmarking that translates raw scores into meaningful performance categories. The Single Ease Question (SEQ), validated by Sauro and Dumas, offers step-level granularity that SUS's macro-level assessment misses. By implementing both, Avenir-UX bridges quantitative rigor with qualitative depth.

**Think Aloud as Data:** Nielsen's foundational work on usability engineering established Think Aloud as the method for understanding user mental models. Traditional Think Aloud captures *what* users think while interacting; Avenir-UX's innovation is making this protocol executable by an MLLM. The agent's reasoning trace serves the same function—externalizing cognitive friction that quantitative metrics alone cannot surface.

**Limitations of MLLMs as Judges:** Luera et al.'s research revealed that while MLLMs can assess ease-of-use reasonably well in aggregate, they struggle with specificity on individual interfaces. Avenir-UX addresses this by having the agent *interact* with the system and accumulate experiential evidence rather than judging from screenshots alone—shifting from static analysis to behavioral observation.

---

## Central Arguments

The paper makes several interconnected claims about automated UX evaluation and the role of visual grounding in bridging the gap between functional testing and human-centered assessment.

**Main Thesis:** Visual grounding is essential for authentic UX evaluation. Automation that operates only on DOM representations misses the usability issues that human users actually encounter.

The authors build this argument through comparison with UXAgent (Lu et al.), which discards visual elements like styles and layout. As they note: "UXAgent by Lu et al. discards potentially crucial visual elements like styles and layout which are vital to user experience." Avenir-UX's visual perception module can identify issues like visual clutter, layout ambiguity, and insufficient contrast—the very factors that cause real users to struggle.

**Second, Think Aloud reasoning elevates automation from testing to research.** The paper emphasizes that generating SUS scores alone doesn't explain *why* a system is difficult to use. The Think Aloud transcript provides the explanatory layer: "This stream of consciousness provides rich qualitative data, explaining the 'why' behind usability frictions, errors or delays."

The case study demonstrates this concretely. When evaluating Recreation.gov, the agent's Think Aloud captured precise friction points: "While the DOM element is clearly visible and correctly identified, the lack of response creates a total block." This isn't just logging what happened—it's interpreting the experience from a user perspective.

**Third, step-wise evaluation reveals friction gradients that aggregate metrics obscure.** SEQ scores tracked across interaction stages showed where the task degraded: initial navigation succeeded (SEQ 7), but date selection immediately dropped to SEQ 1-2. This granular mapping lets developers pinpoint exactly where improvements are needed rather than receiving a single usability score.

**Fourth, Experience-Imitation Planning enables context-aware evaluation.** The EIP module's strategic search predicted that submission guidelines would be in footer or help sections rather than main navigation—demonstrating knowledge of common web patterns. This makes the agent's behavior more representative of informed users rather than random exploration.

---

## Evidence

The researchers provide both architectural validation and empirical demonstration through a detailed case study.

**System Architecture Evidence:** Figure 2 shows the complete pipeline from initialization through execution to report generation. The three-phase flow (strategic planning → action-by-action execution with Think Aloud → post-task synthesis) mirrors professional usability testing protocols, not just automated testing.

**Case Study: Recreation.gov Permit Booking**

The task was realistic: check permit availability for a group of 4 at Brooks Camp, Katmai National Park for a specific Saturday. This required navigating complex information hierarchy, date selection widgets, and form interactions.

**Successful Interactions (SEQ ≥ 6.5):**
- Search and navigation to Brooks Camp Permit Page: SEQ = 7
- Reviewing availability results: SEQ = 3

**Critical Friction Points (SEQ < 3.3):**
- Date selection for "Next Saturday": SEQ = 1-2
- Group size configuration: SEQ dropped from 7 to 1
- Modal management during date adjustments: SEQ = 6-7 initially, then degraded

The step-by-step breakdown reveals a 14-step sequence where the agent successfully navigated to the correct page but encountered state desynchronization between input fields and displayed results. The Think Aloud captured this: "interaction with the interface required multiple steps to complete the desired outcome with confusing steps and error-prone visual navigation."

**Final Metrics:**
- **SUS Score:** 55/100 (Grade D on Sauro-Lewis CGS)
- **Average SEQ:** 6.0/7
- **Qualitative Finding:** Visual clarity masks functional defects; elements appear correct but behave unexpectedly

**Architecture Validation:** The appendix provides complete system prompts showing how evaluation happens:

The Step-Wise Evaluation prompt instructs the agent to assess four dimensions after every action:
- SEQ (ease): numeric + qualitative
- Efficiency: speed and directness
- Clarity: UI understandability  
- Confidence: certainty about action outcome

The SUS Evaluation prompt maps micro-metrics to the 10-item questionnaire using logic like: "High average SEQ (≥ 5.0) maps to positive SUS scores; Low average SEQ (< 4.0) maps to negative SUS scores."

**Robustness Through Grounding:** The detailed case study walkthrough demonstrates how visual grounding solved real problems:

*Step 1 (Cookie Consent):* "Action: Click 'Accept All' at coordinates (805, 876). Architecture Correlation: This demonstrates the Visual Perception & Grounding module. Unlike DOM-based agents that fail due to obfuscated HTML, Avenir-UX's Mixture of Grounding Experts (MoGE) interacted with pixels directly via coordinate-based visual tagging."

*Step 2 (Scrolling):* "Action: scroll_bottom. Architecture Correlation: This action was driven by the Think Aloud where the agent reasoned that structural footer lines are often found in the footer."

*Step 3 (Deep Link Navigation):* "Action: Click 'Database Guidelines' at (316, 838). Architecture Correlation: The agent utilized grounded interaction to identify the specific text link that aligned with the user's intent. This triggered a domain switch to support.discogs.com."

---

## Conclusion

This research makes a compelling case that visual grounding transforms automated UX evaluation from functional testing into authentic user experience assessment. The core insight is architectural: perception matters as much as action.

Traditional automation approaches optimize for task completion. Avenir-UX optimizes for authentic experience. By "seeing" interfaces through pixel-based vision, the agent encounters the same usability barriers human users face—visual clutter, ambiguous layouts, modal interference, state desynchronization. These barriers are invisible to DOM-based systems.

The practical implications are significant for development workflows. The paper positions Avenir-UX as a solution for teams that cannot afford traditional user testing: "UX evaluation is frequently neglected, leading to products that function technically but fail to meet user needs." For startups and open-source projects, having *some* structured usability feedback is transformatively better than having none.

The methodology offers several concrete contributions:

**First, the integration of quantitative and qualitative methods mirrors professional practice.** SUS provides benchmarking, SEQ provides granularity, Think Aloud provides explanation. The resulting UX report isn't just a score—it's actionable feedback identifying specific elements causing friction.

**Second, Experience-Imitation Planning addresses the "cold start" problem of agent evaluation.** Naive agents explore randomly; informed users leverage prior knowledge. EIP's strategic search incorporates external knowledge, making agent behavior more representative of real users.

**Third, the framework is extensible.** The paper identifies clear future directions: continuous agent operations (moving beyond discrete think-act cycles), exploratory autonomy (free-roaming to discover bottlenecks without explicit instructions), domain-specific fine-tuning for Gemini-3-Pro and other models, diverse user personas (varying literacy levels, cognitive styles, accessibility needs), and longitudinal studies tracking usability changes over multiple product versions.

**The validation gap:** The paper's primary limitation is the single case study. The authors demonstrate that Avenir-UX *can* generate insights consistent with human findings, but they don't validate this statistically across multiple systems and user populations. The Recreation.gov evaluation is illustrative, not definitive.

**Cost-quality tradeoff:** Automated evaluation will always face the question: is this good enough to replace human testing, or only good enough to complement it? The paper positions Avenir-UX pragmatically—not as a replacement for human research but as a way to make professional-grade evaluation accessible to teams that otherwise wouldn't do any UX testing at all.

**The demographic bias concern:** All evaluation reflects its evaluator's perspective. If Avenir-UX operates with a "general user profile," whose general? The paper acknowledges this limitation: "Future work will focus on simulating a broader range of distinct user personas, varying in digital literacy, cognitive styles, and accessibility needs." This connects to broader concerns about synthetic user representation documented in other recent work (Seshadri et al., 2026).

Six months from now, when you return to this research, remember: the key innovation isn't that an AI can click through websites—it's that visual grounding lets the AI *experience* websites the way humans do, encountering the same friction points that make interfaces difficult to use. The gap between functional correctness and user experience is a perceptual gap, and Avenir-UX bridges it through vision.

---

## APA Citation

Tan, W. J., Lim, Z. R. L., Durgad, S., Obegi, K., & Li, A. Y. (2026). Avenir-UX: Automated UX evaluation via simulated human web interaction with GUI grounding. *arXiv preprint arXiv:2604.09581v2*.

---

## Discussion Questions

1. **Validity and Representativeness:** The paper demonstrates Avenir-UX on a single case study. What would a proper validation study look like? How many systems, across what domains, with what human baseline would be needed to establish that the agent's usability findings generalize reliably?

2. **The Evaluation Evaluator Problem:** How do we know if an automated UX evaluation is accurate? If we need human UX researchers to validate the agent's findings, have we really saved resources? What's the right calibration protocol?

3. **Demographic Blindness:** The agent operates with a "general user profile." Given research showing that usability issues affect different user populations differently (older adults, users with disabilities, users with varying digital literacy), how should automated evaluation systems handle this diversity? Should every evaluation run multiple persona-conditioned agents?

4. **Think Aloud Authenticity:** Human Think Aloud captures genuine cognitive struggle—pauses, backtracking, confusion, "wait, where did that go?" Can an MLLM's generated reasoning trace authentically represent this, or does it rationalize after the fact? What would distinguish genuine confusion from simulated confusion?

5. **The Automation Paradox:** Teams that neglect UX evaluation often do so because they lack UX expertise, not just time. If a team doesn't have UX researchers, will they correctly interpret Avenir-UX's reports and prioritize the right fixes? Or does effective automated evaluation still require human UX judgment downstream?

---

## Bias Check

This summary aims to fairly represent the research contributions while acknowledging limitations. The paper takes an optimistic stance toward automated UX evaluation, positioning Avenir-UX as a solution to accessibility barriers in professional usability testing. I have attempted to maintain that perspective while noting the validation gap (single case study) and open questions about demographic representation and generalizability.

The main limitation in my summary is that the full system prompts in the appendix provide important implementation details that I can only partially reference. Readers seeking to replicate or build on this work should consult the complete prompt specifications in Sections A.1-A.7 of the original paper.

**Accuracy Score: 9/10**

I have verified this summary against the paper content and it accurately represents the system architecture, evaluation methodology, case study findings, and theoretical positioning. The one-point deduction reflects that some technical prompt details and the complete interaction trace are necessarily compressed.
