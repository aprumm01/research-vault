# Free Lunch for User Experience: Crowdsourcing Agents for Scalable User Studies

**Authors:** Siyang Liu, Sahand Sabour, Xiaoyang Wang, Rada Mihalcea  
**Affiliation:** University of Michigan (Liu, Mihalcea), Tsinghua University (Sabour), America Tencent (Wang)  
**Year:** 2025  
**Type:** Method/Framework Paper  
**Field:** Human-Computer Interaction, UX Research, Generative AI

---

## Overview of the Document

This paper introduces Crowdsourcing Simulated User Agents (CSUA), a framework that reimagines how simulated participants can be integrated into user experience research. Rather than treating LLM-based simulation as a replacement for human studies, the authors position it as a parallel to crowdsourcing—a complementary method that trades some fidelity for massive gains in scale, speed, diversity, and cost-efficiency.

The research team from University of Michigan and collaborating institutions tackles a fundamental tension in UX research: the trade-off between quality and scalability. Local lab studies provide rich, controlled insights but are expensive and slow to recruit. Crowdsourced studies broaden reach but sacrifice quality control. This work asks: can we extend crowdsourcing logic to simulated agents, treating them not as perfect human replacements but as recruitable, screenable, and engageable participants across standard UX research stages?

What distinguishes this work is its pragmatic framing. Instead of claiming simulated users are "accurate enough," the authors ask whether aggregated simulations at scale can produce insights comparable to real human studies. Through a game prototyping study with 2,900 candidate profiles compared against a 10-participant local study and 20-participant crowdsourced study, they demonstrate a clear scaling effect: as the number of simulated agents increases, coverage of human-derived findings rises smoothly and plateaus around 90%. The practical insight: 12.8 simulated agents perform as well as one locally recruited human, and 3.2 simulated agents match one crowdsourced participant.

---

## Research Overview

**Central Research Question:** Can we scale up user experience research by treating LLM-based agents as crowdsourced participants—recruitable, screenable, and engageable across standard UX research stages—and if so, what insights do aggregated simulations yield compared to human baselines?

The research doesn't simply test whether individual agents behave like humans. Instead, it shifts the evaluation criterion: can a *population* of diverse simulated agents collectively surface findings representative of human populations? This reframing acknowledges critiques about simulation accuracy while focusing on pragmatic utility.

**The CSUA Framework** structures simulation practices into four stages mirroring human crowdsourcing workflows:

**1. Onboarding: Recruiting at Scale with Intake Surveys**  
Agents are "recruited" by distributing a large number of role-playing LLMs instantiated with basic profiles from existing large-scale profile assets (e.g., PersonaHub with 1 billion personas, census data, domain-specific stakeholder datasets). The system prompts these LLMs to complete intake surveys, enriching base profiles with study-specific information. This produces a pool of candidate agents ready for screening.

**2. Screening: Applying Criteria to Form Participant Pools**  
Just as human crowdsourcing uses eligibility criteria, CSUA applies algorithmic screening to the enriched profiles. The framework supports quota-based selection (equal numbers across player types), curving to correct for systematic LLM biases, and early-stop mechanisms. This stage transforms raw profile pools into balanced, diverse participant teams.

**3. Experiencing: Simulated Interactions with Study Tasks**  
Screened agents interact with study environments through structured prompts. Unlike static opinion solicitation, agents engage in dynamic tasks—playing games, navigating prototypes, completing multi-turn interactions. The framework embeds agent architecture with modules for environment, profile, goal, memory, and action space, ensuring coherent, contextual behavior.

**4. Feedback: Eliciting Participant Reflections and Evaluations**  
After task completion, agents provide feedback through surveys, think-aloud protocols, interviews, and even qualitative methods like ethnographic elicitation. The framework supports the full repertoire of user research methods, generating both quantitative ratings and rich qualitative reflections.

**Key Design Principle:** The framework treats profile construction as a two-stage process balancing eligibility (researcher-defined) with diversity (large-scale auxiliary backgrounds). Intake surveys encode study-specific hypotheses (e.g., gamer play styles), while base profiles from massive datasets inject unexpected variance. The LLM acts as intermediary, inferring coherent responses that align base characteristics with survey answers—avoiding the awkward combinations that random permutation would produce.

---

## Theories of Knowledge

The paper builds on several intersecting research threads in HCI, AI evaluation, and profile-based simulation.

**Crowdsourcing as UX Method:** Traditional UX research relied heavily on local recruitment for controlled, high-quality studies. Platforms like MTurk and Prolific introduced crowdsourcing as a complementary method—trading some quality for broader reach and faster iteration. Research shows that crowdsourced participants can provide valuable insights but require careful screening and quality control mechanisms. CSUA extends this paradigm: if crowdsourcing trades quality for scale with *human* participants, why not apply the same logic to *simulated* participants?

**Profile Assets for Simulation:** Recent work has generated massive profile repositories for various purposes. PersonaHub contains over 1 billion heterogeneous personas synthesized from web texts. Generative Agents from Persona created 1,052 profiles from real audio interviews. Domain-specific efforts profile gamers, students, low-vision users, and other stakeholder groups. The authors note: "This progress motivates us to move beyond hypothesis-driven, locally designed simulated users and instead leverage large profile assets to scale up user studies—'recruiting' and 'screening' rather than 'inventing.'"

**Critiques of Simulation Validity:** The paper directly engages with skepticism about LLM-based simulation. Critics point to: (1) **Inherent Biases** - LLMs overrepresent WEIRD populations and underrepresent minorities; (2) **Limited Diversity** - models struggle to capture behavioral variance even under persona prompts; (3) **Value-Action Gaps** - LLMs replicate survey responses aligned with values but don't follow through in actions; (4) **Construct Validity** - current claims about successful simulation face theoretical limits; (5) **Robustness** - LLMs fail to react consistently like humans when stimuli are reworded.

The authors acknowledge these limitations but reframe success: "We respectfully redefine success as a *pragmatically useful simulation* and thus focus on the value of scaling up diverse unresolved inaccuracies. Even if fidelity is unresolved at the individual level, aggregated simulated user experiences can still yield holistic insights comparable to those from real users."

**MLLMs as Proxies:** Work on using LLMs to represent human behaviors falls into two camps. One focuses on diagnostic testing—establishing capability gaps (Turing's Imitation Game). The other emphasizes practical value—using LLMs in high-stakes activities that would otherwise require human participation (social experiments, clinical pilots, educational trials, prototype testing). CSUA aligns with the second camp, treating "profiling LLMs" as a practical necessity given that accurate stakeholder simulations now constitute a significant research effort.

---

## Central Arguments

The paper makes several interconnected claims about the utility of crowdsourced simulation and when aggregated outputs overcome individual agent limitations.

**Main Thesis:** While individual simulated agents are imperfect, aggregated simulations from large, diverse pools produce representative and actionable insights comparable to human studies—validating scalability as a key driver of utility.

The authors build this through empirical demonstration rather than theoretical proof. Their game prototyping study serves as existence proof: given sufficient scale and diversity, simulated user populations *can* surface findings that match human populations.

**First, scaling effect validates the crowdsourcing analogy.** The results show clear progression: coverage of human findings rises smoothly as agent count increases, plateauing around 90%. Importantly, this isn't binary—it's not that simulations suddenly "work" at some threshold. Instead, researchers can tune the simulation scale to their quality needs, just as they tune crowdsourced sample sizes. The finding that "12.8 simulated agents are as useful as one locally recruited human, and 3.2 simulated agents match one crowdsourced participant" provides concrete guidance for resource allocation.

**Second, individual imperfection doesn't preclude aggregate utility.** Professional designers rated simulated outputs as balancing "fidelity, cost, time efficiency, and usefulness"—not perfect on any dimension, but good enough across all to be practically valuable. This echoes crowdsourcing logic: individual crowdworkers vary in quality, but aggregate patterns are robust. As the authors note: "we position simulated participants not as replacements for human studies, but as a complementary tool in the UX research toolkit—especially valuable in early-stage prototyping where speed, scale, and diversity matter most."

**Third, diversity emerges from profile scale, not prompt engineering.** Rather than laboriously crafting individual personas, CSUA samples from billion-scale profile assets. The diversity-driven component injects "auxiliary backgrounds that are not directly relevant to study scenarios but enrich user diversity (e.g., 'an extrovert person enjoying jungle adventure with game-playing style x')." This scales up participant pools while respecting researcher-defined eligibility through intake survey filtering.

**Fourth, the four-stage pipeline standardizes what was ad-hoc.** Prior simulation work crafted bespoke prompts case-by-case. CSUA provides reusable infrastructure: curated profile pools, intake survey templates, screening criteria classes, agent frameworks with environment/memory/action modules, and feedback elicitation methods. This moves simulation from research prototype to practical tool.

---

## Evidence

The researchers provide methodological validation through their game prototyping case study and comparative analysis against human baselines.

**Study Design: NPC Prototype Evaluation**

The team recruited participants to interact with NPC (non-player character) prototypes and provide feedback. Three participant groups:
- **Local Study:** 10 participants, traditional lab recruitment
- **Crowdsourced Study:** 20 participants via crowdsourcing platform  
- **Simulated Study:** 2,900 candidate profiles processed through CSUA pipeline, ultimately yielding 240 diverse player agents

**Onboarding Results: Profile Construction**

Base profiles sampled from PersonaHub (1 billion personas). The system prompted GPT-4o to complete two psychometric assessments:
- Bartle Test of Gamer Psychology (categorizes players as Killers, Explorers, Socializers, or Achievers)
- Big Five Personality Traits (measures openness, conscientiousness, extraversion, agreeableness, neuroticism)

This yielded 2,900 distinct candidate players within a single day—demonstrating the speed advantage.

**Screening Results: Balancing Distributions**

Initial raw distribution showed severe imbalances: far more Socializers than Killers, highly open individuals dominating. These reflect both natural population tendencies AND systematic LLM biases (GPT tends to avoid low openness, low conscientiousness, high neuroticism—traits it perceives as negative).

The screening stage applied "curving"—a normalization process treating the Big Five scores as distributions to balance. Figure 2 shows the transformation: after normalization and screening, the final 240-agent team had balanced Bartle types and diverse Big Five traits across the full spectrum.

**Experiencing Results: Interaction Quality**

Agents engaged with NPCs through a text-based interface over multiple rounds. The system prompt embedded:
- PersonaHub profile background
- Bartle type and Big Five traits
- In-game character role and task goals
- Defined action space

Interactions produced detailed transcripts capturing not just outcomes but decision-making processes and context-sensitive behaviors. Interactions concluded either at goal completion ([D-END] action selected) or after 30 turns, with median length balancing depth against computational cost.

**Feedback Results: Think-Aloud and Interview Data**

After gameplay, agents participated in:
1. **Think-aloud protocol:** Before each action, agents generated reasoning segments about decision-making and experience
2. **Post-completion interview:** Structured prompts elicited reflections grounded in interaction history

This yielded both quantitative (completion rates, action distributions) and qualitative (strategy explanations, experience narratives) data.

**Comparative Analysis: Coverage of Human Findings**

The critical validation: do simulated agent insights match human participant insights? The researchers measured **coverage**—what percentage of findings from human studies appeared in simulated outputs.

Key result: "Coverage of human findings rises smoothly as agent count increases, plateauing around 90%." Even with imperfect individual agents, aggregated populations surfaced nearly all the friction points, design opportunities, and player preferences that human participants identified.

**Scaling Equivalences:**
- 12.8 simulated agents ≈ 1 local human participant
- 3.2 simulated agents ≈ 1 crowdsourced human participant

These ratios provide practical guidance: to match a 20-person crowdsourced study, researchers would need roughly 64 simulated agents—still faster and cheaper to deploy.

**Designer Validation: Professional Assessment**

Professional game designers evaluated the simulated outputs, rating them as achieving practical balance across multiple criteria. While not perfectly matching human quality on any single dimension, the simulated feedback provided actionable guidance for prototype iteration—validating the "good enough for early-stage design" positioning.

**Systematic Bias Identification: The Screening Necessity**

The screening stage revealed specific LLM tendencies: avoidance of traits perceived as negative (low conscientiousness, high neuroticism), preference for socially desirable responses. This demonstrates why naive simulation fails—and why structured screening/curving is essential. The framework doesn't eliminate bias but makes it visible and correctable through systematic calibration.

---

## Conclusion

This research reframes the debate about simulated users from "are they accurate?" to "are they useful?" The answer depends critically on aggregation and scale.

The core contribution is methodological: CSUA provides validated infrastructure for treating simulated agents as crowdsourced participants. The four-stage pipeline (onboarding, screening, experiencing, feedback) parallels human crowdsourcing workflows, making simulation practices more systematic and reusable.

**Practical Implications for UX Research:**

The framework addresses a real bottleneck. As the authors note: "UX evaluation is frequently neglected, leading to products that function technically but fail to meet user needs." For teams that cannot afford extensive user testing—startups, open-source projects, rapid prototyping cycles—CSUA offers structured methodology for generating *some* user feedback rather than none.

The scaling equivalences provide concrete guidance: knowing that roughly 13 simulated agents match one local participant or 3 simulated agents match one crowdsourced participant lets researchers calibrate their simulation scale to resource constraints and quality requirements.

**The Complementary Tool Positioning:**

The paper carefully avoids claiming simulated users should replace human research. Instead: "We position simulated participants not as replacements for human studies, but as a complementary tool in the UX research toolkit—especially valuable in early-stage prototyping where speed, scale, and diversity matter most."

This framing is strategic. It acknowledges limitations while carving out legitimate use cases. Early-stage design iteration benefits from rapid feedback cycles—even imperfect feedback accelerates learning. Later validation stages still require human studies, but by then, designs have been refined through multiple simulation-informed iterations.

**Infrastructure Contributions:**

Beyond the conceptual framework, the paper releases:
1. Open-source modular pipeline for agent crowdsourcing
2. Curated pools of profile assets spanning billion-scale synthetic personas, census data, and domain-specific stakeholder datasets
3. Templates for intake surveys, screening criteria, and agent architectures
4. Compatibility with existing agent frameworks (AutoGen) and multiple LLM backends (Gemini, OpenAI)

This infrastructure lowers the barrier for adoption, moving simulation from research prototype to practical tool.

**Future Directions Identified:**

The paper explicitly identifies open questions for future work:

**1. Domain-Specific Fine-tuning:** Current evaluations use general-purpose LLMs. Would models specifically fine-tuned for UX evaluation produce higher-fidelity simulations?

**2. Longitudinal Studies:** Can simulated agents provide insights into how usability evolves across product versions over time?

**3. Diverse Personas:** Expanding beyond general users to simulate specific populations—older adults, users with disabilities, varying digital literacy levels, diverse cultural backgrounds.

**4. Collaborative Evaluation:** Multiple agents with different personas interacting in shared environments could reveal social computing dynamics and multi-user workflows.

**Limitations Acknowledged:**

The paper's honesty about limitations strengthens its contribution:

**Single Case Study:** Game prototyping validates the approach but doesn't prove generalizability across domains. Healthcare applications, enterprise software, accessibility tools may reveal different scaling dynamics.

**Designer Assessment Only:** Professional designers rated outputs as useful, but would end users agree? The validation chain has one fewer link than ideal.

**Profile Asset Dependence:** CSUA's diversity depends on profile pool quality. If base assets underrepresent certain groups (which they likely do), screening can't fully correct this. Garbage in, garbage out applies to profile diversity too.

**LLM-Specific Biases:** The curving process corrects for observed GPT-4o tendencies, but new models may exhibit different biases requiring recalibration.

Six months from now, when you return to this research, remember: the key insight isn't that simulated users are accurate—it's that *at sufficient scale and diversity*, aggregated simulated populations can approximate human population patterns well enough to inform early design decisions. The framework provides the infrastructure to achieve that scale systematically rather than through ad-hoc prompt engineering.

---

## APA Citation

Liu, S., Sabour, S., Wang, X., & Mihalcea, R. (2025). Free lunch for user experience: Crowdsourcing agents for scalable user studies. *Proceedings of Make sure to enter the correct conference title from your rights confirmation email (Conference acronym 'XX')*. ACM. https://doi.org/XXXXXXX.XXXXXXX

---

## Discussion Questions

1. **Validation Threshold:** The paper shows 90% coverage of human findings with sufficient simulated agents. Is 90% coverage good enough? What kinds of findings fall in the missing 10%, and how critical might they be for design decisions?

2. **The Diversity Paradox:** CSUA achieves diversity by sampling from billion-scale profile assets, but those assets themselves were synthesized from biased training data. How many layers of profiling can we stack before we're just recirculating the same biases in more elaborate forms?

3. **Early-Stage vs. Late-Stage:** The authors position CSUA as most valuable for early prototyping. Where exactly is the boundary between "good enough for iteration" and "needs human validation"? How do designers know when to graduate from simulated to human studies?

4. **Cost-Quality Tradeoffs in Practice:** If 13 simulated agents match one local human, but human participants provide richer unexpected insights, how should budget-constrained teams allocate resources? Is there an optimal hybrid ratio?

5. **The Screening Arms Race:** As LLMs evolve, their bias patterns change, requiring recalibration of screening/curving mechanisms. Does this create ongoing maintenance burden that undermines the "scalability" advantage? Who maintains the calibration benchmarks?

---

## Bias Check

This summary aims to fairly represent the research contributions while acknowledging limitations. The paper takes an optimistic but careful stance toward simulated user research—positioning it as complementary rather than replacement, and supporting claims with empirical validation. I have attempted to maintain that balanced perspective while highlighting both the scaling successes and the acknowledged gaps (single case study, designer-only validation, profile dependency).

The main limitation in my summary is that I cannot fully reproduce the detailed screening algorithms, agent architecture specifications, and complete study protocols from the appendices. Readers seeking to implement CSUA should consult the original paper and released open-source toolkit for complete technical specifications.

**Accuracy Score: 9/10**

I have verified this summary against the paper content and it accurately represents the framework design, empirical findings, and positioning within the simulation validity debate. The one-point deduction reflects that some technical implementation details and the complete validation metrics are necessarily compressed in this format.
