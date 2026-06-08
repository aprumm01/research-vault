---

source_file: "research_docs/synth users/Interview-Informed Generative Agents for Product Discovery A Validation Study - Wang et al - 2026.pdf"
type: paper
community: "GenAI in UX and Design Practice"
tags:
year: "2026"
authors: "Wang et al"
---

# Interview-Informed Generative Agents for Product Discovery: A Validation Study (Wang et al., 2026)

## Summary
Zichao Wang and Alexa Siu (both Adobe Research, San Jose) investigate whether interview-informed generative agents can simulate user responses in product concept testing — a context where preferences are constructed on the fly for artifacts participants have never used. They recruited N = 51 knowledge workers via Prolific, conducted 90-minute unmoderated audio interviews on document workflow practices, then compared personalized agents' evaluations of four AI document workflow concept prototypes against the same participants' actual TAM, NPS, and open-ended responses. The agent architecture uses GPT-4o with retrieval (text-embedding-3-small) and reflection over interview transcripts. Their key finding is that agents are "distribution-calibrated but identity-imprecise": they approximate population-level response distributions and outperform scratchpad-only and no-information baselines, but fail to reliably reproduce any individual participant's specific responses. The paper received a CHI 2026 Honourable Mention and was published in the ACM CHI 2026 proceedings.

## Citation
- **Authors:** Zichao Wang, Alexa Siu
- **Venue:** CHI 2026 (Proceedings of the ACM CHI Conference on Human Factors in Computing Systems)
- **DOI:** 10.1145/3772318.3791918
- **arXiv:** 2603.29890 (submitted March 10, 2026)
- **Award:** CHI 2026 Honourable Mention
- **License:** CC BY-NC-SA 4.0
- **Affiliation:** Adobe Research, San Jose, CA (both authors)
- **Not a preprint** — published at CHI 2026; arXiv version is the author copy.

## Key Concepts
- **Distribution-calibrated but identity-imprecise:** agents capture group-level tendencies but not individual-level idiosyncrasies — the paper's central and explicitly named finding
- **Interview-informed agents:** generative agents grounded in 90-minute unmoderated audio interviews capturing workflow understanding and pain points; agent memory = segmented transcript turn pairs embedded with text-embedding-3-small; scratchpad = structured demographic/job-role dictionary
- **Product discovery:** early-stage concept testing where designers need both population-level signals (which concept is promising?) and identity-level heterogeneity (which user types are excited vs. blocked?)
- **TAM + NPS:** Technology Acceptance Model (6-item abbreviated scale measuring Perceived Usefulness, Perceived Ease of Use, Behavioral Intention on 7-point Likert scales) and Net Promoter Score (0–10 scale) used as scalar evaluation metrics for novel AI concepts
- **Concept testing with novel artifacts:** unlike social science surveys testing stable attitudes, product discovery requires generating preferences for hypothetical, unseen products — preference construction under uncertainty
- **Longitudinal validation design:** participants completed the concept test twice (initial + 3-day follow-up) to establish human-human self-consistency as a benchmark ceiling

## Theoretical Framework
Builds on Park et al.'s interview-informed agent architecture (85% normalized accuracy on General Social Survey) and extends it to a product discovery context. Applies a simulation fidelity evaluation framework distinguishing scalar fidelity (RQ1) from qualitative alignment (RQ2); draws on technology acceptance literature (TAM, Diffusion of Innovations), consumer behavior/judgment-under-uncertainty research, and design research methods (contextual inquiry, experience prototyping, cultural probes). Also draws on the ecological fallacy literature to interpret the population-vs-individual gap.

## Methods
- **Study design:** 3-part longitudinal study (all conducted remotely via Prolific)
  - Part 1: ~90-minute unmoderated audio interview on workflow, pain points, document-heavy tasks (avg. 43 min raw audio/participant, avg. 106 words/response)
  - Part 2: 30-minute concept test (within 24 hours of interview)
  - Part 3: 30-minute follow-up concept test (3 days after Part 2, identical to Part 2)
- **Participants:** N = 51 knowledge workers recruited via Prolific (US-based, work with documents daily); $25/hour compensation paid only upon completing all three parts
  - Management/Leadership: 14/51 (27%); Operations/Administration: 8/51 (16%); Education: 4/51 (8%); also Finance, Legal, Healthcare, Research, HR, Sales, IT, Marketing
  - Age: 21–76 years (M = 43.2, SD = 11.9); gender: 51% male, 49% female
  - Technology adoption: 45% cautious adopters, 41% early adopters
  - AI attitudes toward document tools: 43% very positive, 35% somewhat positive, 18% neutral, 4% somewhat negative
- **Four concept prototypes tested:**
  1. Multidoc Q&A Assistant — analyze multiple sources, answer questions with grounded responses
  2. Smart Highlights Assistant — intelligent document highlighting
  3. Audio Assistant — transform documents into audio/podcast experiences
  4. Workflow Actions Assistant — active automation of document workflow tasks
- **Data volume:** 3,060 concept-test responses (4 concepts × 15 questions × 51 participants); ~36 hours of speech
- **Agent architecture:** GPT-4o for reflection + answering; text-embedding-3-small for retrieval; retriever = maximum inner product search over transcript turn-pair embeddings; three baseline conditions: (a) interview-based (transcript + scratchpad), (b) scratchpad-only, (c) no-information
- **Evaluation metrics:**
  - Individual level: MAE, Gwet's AC2 (chance-corrected ordinal agreement), Spearman correlation
  - Population level: Wasserstein distance between response distributions
  - Qualitative: LLM-as-a-judge (GPT-4o + GPT-4.1-mini, Cohen's Kappa = 0.53) on 4 dimensions: sentiment direction, explanation alignment, topic coverage, voice/tone similarity

## Main Arguments
- **Interview-based agents are imprecise at individual level:** accuracy (exact match) relative to human-human self-consistency: humans vs. humans = 0.446; humans vs. interview-based agents = 0.300 (67% of human-human); humans vs. scratchpad-only = 0.259 (58%); humans vs. no-information = 0.256 (57%). No significant differences across agent designs (confirmed by Tukey's post-hoc test).
- **Interview-based agents are reasonably calibrated at population level:** Wasserstein distance (Likert / NPS): human–human = 0.175 / 0.211; human–interview-based = 0.227 / 0.487; human–scratchpad-only = 0.393 / 0.513; human–no-information = 1.058 / 1.678. Interview-based agents are the only design that captures lower-scoring preferences (Likert 1–2, NPS 0–3). No-information agents degenerate to choosing 6 on 7-point Likert and 8 on NPS.
- **Open-ended responses show further gaps:** agents perform worst on voice/tone (likely because interview data is transcribed speech but agents generate written-style text); best qualitative metric is topic coverage. Agents achieve "high-level thematic but not experiential fidelity" — same top-level benefit/risk axes, but flatten contradictions, emotions, and messy workarounds. ~30% of humans expressed outright rejection of the Audio Assistant; only 1 agent did.
- **Cost comparison:** human concept test = 30 min, $12.50; agent concept test = ~4 min, ~$1.27 (GPT-4o pricing as of paper submission)
- **Simulation is suitable for concept screening, not individual-level insight:** agents answer "Which concept is most promising overall?" but not "Why does this participant hesitate?"
- **Responsible integration:** simulation should complement, not replace, authentic user interviews; practitioners should be transparent about what simulation can and cannot reproduce

## Limitations & Critiques
- Sample size of 51 limits statistical power and diversity of profiles; single company (Adobe) and single domain (AI document workflows) restricts generalizability
- Preference construction on the fly for novel artifacts is an especially demanding simulation task — may explain identity-imprecision beyond fundamental simulation limits
- Agent architecture is relatively simple (retrieval + reflection + GPT-4o); ablation studies reported in supplementary material but not main paper
- Dependence on interview protocol: semi-structured audio interviews may not be optimal grounding modality; richer modalities (visuals, contextual inquiry, diary studies) untested
- LLM-as-a-judge qualitative evaluation subject to model-specific biases (Cohen's Kappa = 0.53 = moderate agreement only)
- No post-hoc calibration applied to agent scores — results represent a conservative lower bound; learned normalization could potentially improve individual-level agreement
- Fidelity vs. utility threshold not defined: what level of distributional accuracy is "good enough" for concept screening remains an open question

## Connections
- [[GenAI in UX and Design Practice]] - `` [EXTRACTED]
- [[Synthetic Users and AI Personas]] - `` [EXTRACTED]
- [[PersonaCite VoC-Grounded Interviewable Agentic Synthetic AI Personas (Truss, 2026)]] - related work on voice-of-customer grounded persona agents
- [[Lost in Simulation LLM-Simulated Users are Unreliable Proxies for Human Users (Seshadri et al., 2026)]] - concurrent finding on simulation limitations
