---
source_file: 2026/i609-sustainability/The Dark Data Quandary.pdf
type: paper
authors: Daniel J. Grimm
community: Sustainable Computing
tags:
- sustainability
- i609
- dark-data
- legal-risk
- data-governance
- privacy
- HIPAA
- FTC
- Big-Data
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

This comprehensive legal analysis examines "dark data" - the vast quantities of data that organizations collect but never analyze - and its implications for legal risk, judicial decision-making, and data governance. Grimm argues that dark data creates invisible risks under existing legal frameworks (HIPAA, FTC Section 5) while also distorting Big Data's promise of objective, comprehensive analysis. The paper estimates that 80-90% of enterprise data is dark, creating a "capability gulf" between storage technology and analytical tools that poses significant challenges for organizations and courts alike.

## Research Overview

**Central Problem:** Organizations are collecting and storing data at unprecedented rates, but analytical capabilities have not kept pace. The result is massive accumulations of "dark data" - data that is retained but never analyzed or understood.

**Scope of Analysis:**
- Legal risks of dark data under medical privacy (HIPAA) and consumer protection (FTC) frameworks
- Dark data's impact on judicial proceedings and Big Data evidence
- The "storage imperative" driving data accumulation
- Emerging legal regimes (GDPR) and their dark data implications

**Key Statistics:**
- 80-90% of enterprise data is "dark" (never analyzed)
- Less than 1% of unstructured data is ever analyzed
- Global data volumes are increasing faster than analytical capacity
- Storage costs continue to decline while analysis costs remain high

## Theoretical Framework

Grimm develops a framework analyzing dark data through three lenses:

1. **Invisible Risk**: Dark data as a vector for legal liability
   - HIPAA: Unanalyzed medical data may contain PHI requiring protection
   - FTC: Retained consumer data creates cybersecurity vulnerabilities
   - The organization cannot manage risks it cannot see

2. **Decision Distortion**: Dark data undermines Big Data's analytical promise
   - The "N=All" myth: Big Data claims comprehensiveness but operates only on visible data
   - Subjective choices about what to analyze embed bias
   - Courts may over-rely on Big Data conclusions that exclude relevant dark data

3. **Storage Imperative vs. Analysis Gap**: Institutional drivers of dark data accumulation
   - Cheap storage encourages data hoarding
   - Organizations store data hoping future tools will unlock value
   - "We have all become hoarders" - retaining data simply because we can

## Central Arguments

### 1. Dark Data Creates Invisible Legal Risk

Organizations cannot comply with data protection laws if they don't know what data they have:
- **HIPAA Privacy Rule**: Medical dark data may contain protected health information (PHI) that triggers compliance obligations
- **HIPAA Security Rule**: Risk assessments cannot account for e-PHI buried in dark data
- **FTC Section 5**: Retaining unnecessary data creates cybersecurity vulnerabilities; FTC has pursued companies for storing data without business need

### 2. The Storage Imperative Drives Irrational Accumulation

Modern data practices are shaped by:
- Declining storage costs (Kryder's Law)
- Big Data narrative promising future value extraction
- "Compulsive data hoarders" - organizations that store everything
- Asymmetry: storage is cheap; analysis is expensive

### 3. Big Data's Promise is Distorted by Dark Data

Claims of Big Data objectivity and comprehensiveness are undermined:
- **"N=All" is a myth**: Analytical tools only process visible, structured data
- **Correlation without causation**: Big Data finds patterns but doesn't explain them
- **Hidden subjectivity**: Choices about what to analyze embed human judgment
- **Missing exculpatory evidence**: In legal contexts, dark data may contain evidence favorable to defendants

### 4. Courts Must Exercise Gatekeeping Function

Judges should:
- Recognize that Big Data conclusions may be incomplete
- Question what data was excluded from analysis
- Apply heightened scrutiny to algorithmic evidence
- Demand transparency about dataset construction

### 5. Emerging Legal Regimes Heighten Dark Data Risks

GDPR and similar frameworks:
- Require organizations to know what personal data they hold
- Grant data subjects rights to access, correction, and erasure
- Apply to all personal data, including unstructured dark data
- Penalties can reach 4% of global revenue

## Evidence

**Regulatory Enforcement Examples:**

*HIPAA Cases:*
- New York Presbyterian Hospital: $3.3 million settlement for data breach and failure to conduct thorough risk assessment
- University of California: Resolution agreement following breach disclosure failures
- Memorial Healthcare System: $5.5 million for failing to manage access controls

*FTC Section 5 Cases:*
- Accretive Health: Failed to remove data no longer needed for business purposes
- Ceridian Corp: "Created unnecessary risks to personal information by storing it indefinitely"
- DSW Inc.: Stored information in multiple files without business need
- Upromise: Inadvertently collected sensitive data due to overly narrow filter definitions

**Statistical Evidence:**
- McKinsey: Organizations "swimming in an expanding sea of data that is either too voluminous or too unstructured to be managed and analyzed through traditional means"
- IBM: 80% of data is unstructured and dark
- Gartner: Dark data is growing faster than analyzed data

## Conclusion

Dark data poses a fundamental challenge to contemporary data governance. Organizations must:
1. Recognize that retention without analysis creates risk, not value
2. Develop inventory processes to identify and assess dark data
3. Implement deletion policies for data without continuing business need
4. Ensure compliance programs account for unanalyzed data

Courts must:
1. Scrutinize Big Data evidence for completeness
2. Question what data was excluded from analysis
3. Resist the "aura of objectivity" surrounding algorithmic conclusions
4. Ensure dark data containing relevant evidence is identified and produced

Until analytical technology catches up with storage capacity, organizations must "devote newfound attention to the invisible risks that may lie buried within their dark data."

## APA Citation

Grimm, D. J. (2019). The dark data quandary. *American University Law Review, 68*(3), 761-821.

## Discussion Questions

1. How should organizations balance the potential future value of data against the present risks of retention?

2. The paper suggests courts should scrutinize Big Data evidence more carefully. What practical standards could judges apply?

3. How does the dark data problem interact with data minimization principles in privacy regulations like GDPR?

4. What role might AI/ML play in reducing dark data - and what new risks might automated analysis create?

5. Should there be legal requirements for organizations to conduct regular data inventories and purge unneeded data?

## Connections

- **Digital hoarding research**: Organizations exhibit behaviors analogous to personal digital hoarding - retaining data "just in case" without clear purpose
- **User understanding of deletion**: If users don't understand that deleted data persists, they may not realize they're contributing to organizational dark data
- **Data center sustainability**: Dark data consumes storage and energy resources without generating value - pure environmental cost
- **Environmental footprint research**: The 80-90% of enterprise data that is dark represents a massive sustainability problem
- **Cybersecurity and privacy**: Dark data creates attack surface and potential for inadvertent privacy violations
- **Big Data ethics**: Challenges claims of algorithmic objectivity and comprehensiveness
