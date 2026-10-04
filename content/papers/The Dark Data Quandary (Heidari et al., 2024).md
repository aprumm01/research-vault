---
source_file: The Dark Data Quandary.pdf
type: paper
authors: Daniel J. Grimm
year: 2019
builds_on:
- '[[frameworks/Actor-Network Theory]]'
- '[[frameworks/Sociotechnical]]'
- '[[frameworks/Critical Theory]]'
critiques:
- '[[concepts/Technological Determinism]]'
tensions_with:
- '[[concepts/Democratization of Design]]'
supports:
- '[[concepts/Complacency Risk]]'
- '[[concepts/Illusion of Competence]]'
- '[[concepts/Ironies of Automation]]'
key_claims:
- 80-90% of enterprise data is 'dark' (never analyzed), creating a fundamental 'capability
  gulf' between storage technology and analytical tools
- Dark data creates invisible legal risks under HIPAA and FTC frameworks because organizations
  cannot manage compliance obligations for data they have not analyzed or inventoried
- Big Data's promise of objective, comprehensive analysis (N=All) is fundamentally
  distorted by dark data exclusion, with subjective choices about what to analyze
  embedding hidden biases
- The 'storage imperative' driven by declining storage costs and Big Data narratives
  encourages irrational data hoarding, with organizations storing data 'just in case'
  without clear business purpose
- Courts must exercise heightened gatekeeping scrutiny of Big Data evidence, questioning
  what data was excluded from analysis and resisting the 'aura of objectivity' surrounding
  algorithmic conclusions
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: null
context: Legal and regulatory frameworks governing data retention and analysis in
  US organizations
study_type: theoretical
---

# The Dark Data Quandary

## Summary

This article examines the phenomenon of "dark data" - the vast quantities of data that organizations collect and store but cannot presently analyze, interpret, or even identify. Despite advances in artificial intelligence, machine learning, and cognitive computing, Big Data analytics have failed to keep pace with surging data production. The falling costs of cloud storage and distributed systems have made mass data storage cheaper and more accessible, creating a growing chasm between data that is stored and data that can be readily analyzed. Organizations now retain massive quantities of data they cannot presently know or effectively manage, and this "dark data" represents the vast majority of the digital universe.

Dark data presents a quandary for both organizations and the judicial system. For organizations, the inability to know the contents of retained dark data produces invisible legal and regulatory risk under privacy laws (HIPAA) and consumer protection frameworks (FTC Section 5). The article illustrates these risks through detailed analysis of medical privacy regulations and FTC enforcement actions, including the Upromise case where automated data collection filters failed to prevent the capture of sensitive information.

For courts increasingly confronted with Big Data-derived evidence, dark data may shield critical information from judicial view while embedding subjective influences within seemingly objective methods. The article argues that dark data challenges the prevailing narratives of Big Data omnipotence and objectivity, and that decision-makers must achieve new awareness of dark data's presence and its ability to undermine Big Data's vaunted advantages.

## Key Concepts

- **Dark Data**: Data that has been collected but not analyzed, often characterized as "hidden," "undigested," "uncategorized, unmanaged, and unanalyzed." Any data, in any form, can become dark. It represents the vast majority of the digital universe (estimated at 80-93% of all existing data).

- **Storage Imperative**: The organizational drive to collect and store more and more data, fueled by falling storage costs and the belief that advanced analytics will ultimately unlock hidden value within data repositories.

- **Visibility Spectrum**: A three-point framework connecting structured, unstructured, and semi-structured data to "light," "dark," and "grey" visibility. Structured data in relational databases is most visible ("light"), while unstructured data's defiance of analytics-readiness makes it least visible ("dark").

- **Invisible Risk**: The legal and regulatory risks that organizations face when they cannot identify or interpret data concealed within dark data stores, frustrating compliance with privacy, security, and data governance laws.

- **Decision Distortion**: Dark data's ability to quietly distort the promised completeness, accuracy, and objectivity of Big Data-driven evidence used in judicial proceedings.

- **N=All Myth**: The mistaken belief that Big Data produces knowledge from all or nearly all relevant data points, when in reality dark data means that large datasets often contain only a small sliver of structured data that common Big Data tools can digest.

## Theoretical Framework

The article employs a legal-regulatory framework to analyze dark data's implications across two domains: organizational risk management and judicial decision-making. Grimm draws on existing scholarship critiquing Big Data's claims to omnipotence and objectivity, synthesizing insights from information science, law, and technology studies.

The theoretical contribution centers on exposing the "information-data dichotomy" - the paradox at the heart of the information age where mass data creation makes it more difficult, rather than easier, to identify relevant information. The article challenges the prevailing narrative that data is "raw, objective, and neutral" by demonstrating how dark data embeds subjective choices in database framing and construction.

## Methods

This is a doctrinal legal analysis rather than an empirical study. The methodology includes:
- Analysis of statutory frameworks (HIPAA Privacy Rule, Security Rule, FTC Act Section 5)
- Review of regulatory guidance and enforcement actions (HHS, FTC)
- Case law analysis (State v. Loomis, Daubert v. Merrell Dow Pharmaceuticals)
- Synthesis of industry reports, white papers, and technical literature on data storage and analytics
- Application of legal doctrine to emerging technological phenomena

## Main Arguments

1. **The Capability Gulf**: There is a fundamental mismatch between data storage technologies (cheap, scalable) and analytical tools (expensive, limited), producing a vast accumulation of dark data that organizations cannot interpret.

2. **Invisible Regulatory Risk**: Dark data frustrates compliance with expanding data governance laws, including HIPAA's requirements for risk assessments, de-identification, and security safeguards, as well as FTC Section 5 enforcement against unfair and deceptive practices.

3. **Decision Distortion in Courts**: Big Data's natural appeal to judges and lawyers - promising objectivity, fact-inclusiveness, and freedom from human bias - is undermined by dark data, which can produce incomplete or erroneous conclusions that nonetheless carry unwarranted credibility.

4. **Critique of Big Data Objectivity**: Seemingly objective Big Data processes often remain stubbornly mired in subjective framing, as choices about what raw data to feed an algorithm and what data to leave dark inevitably affect the algorithm's conclusions.

5. **Need for Judicial Scrutiny**: Courts must recognize that dark data precludes Big Data-derived conclusions from deserving the gloss of fact-inclusive omnipotence they often receive. Judges should exercise their Daubert gatekeeping function to demand that algorithms producing courtroom evidence be "inspectable" and "able to explain their output."

## Limitations & Critiques

- **Scope Limitation**: The article does not advocate specific data management efforts or recommend how judges should treat particular types of Big Data evidence; it aims only to raise awareness and encourage appropriate skepticism.

- **Technological Optimism Caveat**: The article acknowledges that AI, blockchain, or other emerging technologies may ultimately out-engineer the dark data problem, but notes this possibility does not eliminate present concerns.

- **U.S.-Centric Analysis**: The legal analysis focuses primarily on U.S. regulatory frameworks (HIPAA, FTC), with limited discussion of international regimes like GDPR.

- **Practical Implementation Gap**: While calling for heightened judicial vigilance, the article offers limited guidance on how courts should practically assess the reliability of Big Data evidence in specific contexts.

- **Industry Perspective**: The article primarily addresses risks to organizations and courts but gives less attention to the privacy and autonomy interests of individuals whose data becomes dark.
