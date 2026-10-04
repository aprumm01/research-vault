---
title: "The Dark Data Quandary"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/The Dark Data Quandary.pdf"
type: paper
authors:
  - Daniel J. Grimm
year: 2019
venue: American University Law Review
volume: 68
issue: 3
pages: 761-821

# Relationships
builds_on:
  - "[[concepts/Dark Data]]"
  - "[[concepts/Big Data]]"
  - "[[concepts/Data Lifecycle]]"
supports:
  - "[[concepts/Data Minimization]]"
  - "[[concepts/Legal and Regulatory Issues]]"
  - "[[concepts/Privacy Regulation]]"
critiques:
  - "[[concepts/Big Data Analytics]]"
  - "[[concepts/Data-Driven Decision Making]]"
tensions_with:
  - "[[concepts/Storage Imperative]]"
  - "[[concepts/Data Hoarding]]"

# Academic metadata
key_claims:
  - Dark data represents the vast majority of the digital universe (estimated 80-93% of all data)
  - Organizations retain massive quantities of data they cannot presently know or effectively manage
  - Dark data creates invisible legal risks under privacy, cybersecurity, and consumer protection laws
  - The "storage imperative" drives organizations to hoard data in anticipation of future analytics value
  - Big Data analytics are not omnipotent - dark data challenges claims of completeness and objectivity
  - Dark data can embed hidden subjectivity and produce "decision distortion" in legal proceedings
  - Courts and fact finders should exercise heightened scrutiny of Big Data-derived evidence

methodology: Legal analysis and doctrinal synthesis
study_type: theoretical/legal analysis
context: U.S. legal framework including HIPAA, FTC Act Section 5, and emerging GDPR implications
---

# The Dark Data Quandary

## Summary

Grimm examines the legal and organizational challenges posed by "dark data" - data that organizations collect and store but cannot readily analyze or understand. Despite advances in artificial intelligence and Big Data analytics, organizations are accumulating data far faster than they can process it. The gap between data storage capabilities (cheap and expanding) and analytical capabilities (expensive and limited) has created a vast reservoir of dark data that poses significant but often invisible risks.

The article argues that dark data creates three categories of problems:
1. **Invisible organizational risk** under privacy and data protection laws (HIPAA, FTC Section 5)
2. **Cybersecurity vulnerabilities** as dark data becomes an attractive target for hackers
3. **Decision distortion** when Big Data evidence used in legal proceedings omits or obscures dark data

Grimm critiques the "storage imperative" - organizations' tendency to hoard all data in anticipation that future analytics will unlock hidden value. This practice, while economically rational given cheap storage, conflicts fundamentally with legal requirements for data minimization and creates cascading compliance risks.

## Key Concepts

### Dark Data Defined
- Data that is collected but not analyzed, often unstructured or text-based
- Characterized as "hidden," "undigested," "uncategorized, unmanaged, and unanalyzed"
- Occupies a "visibility spectrum" from light (structured, accessible) to dark (unstructured, invisible)
- Can be both structured and unstructured - darkness is about organizational visibility, not data format

### Sources of Dark Data
1. **Default data creation** - automatic byproducts of digital activity (exhaust data)
2. **Situational effects** - employee actions, system failures, data theft creating unknown copies
3. **Organizational effects** - data silos, poor integration between departments
4. **Deliberate creation** - intentional deprioritization of certain data management

### The Storage Imperative
- Falling costs of cloud storage and distributed systems enable mass data hoarding
- Organizations store data "just in case" future analytics unlock latent value
- Creates tension with data minimization principles in privacy law
- FTC has specifically warned against keeping data organizations "don't need"

### The N=All Myth
- Big Data promises conclusions drawn from "all" relevant data points
- Dark data undermines this claim - large datasets often contain only a small sliver of structured data
- Less than 1% of unstructured data is typically analyzed
- Popular discourse on Big Data ignores the largest component of data: unstructured dark data

## Key Findings

### Legal Risk Under HIPAA
- HIPAA's Privacy Rule applies to protected health information (PHI) regardless of structure
- Dark data may contain PHI that organizations cannot identify or protect
- Security Rule requires risk assessments that must account for all e-PHI locations
- Dark data frustrates compliance with de-identification requirements
- OCR can bring enforcement actions even when organizations are unaware PHI is buried in dark data

### FTC Consumer Protection Implications
- Section 5 prohibits "unfair or deceptive acts or practices"
- FTC treats data security as a consumer protection issue
- Dark data's low priority for protection makes it vulnerable to cybercriminals
- FTC has brought enforcement actions against inadvertent collection of sensitive dark data (Upromise, Compete cases)
- Organizations can face liability for storing data with "no continuing use" that becomes a security risk

### Decision Distortion in Legal Proceedings
- Big Data increasingly influences judicial decision-making (e.g., recidivism risk assessments)
- Algorithms may derive conclusions from databases containing significant dark data
- Dark data can cause digital blind spots leading to incomplete or biased conclusions
- The "illusion of objectivity" shields Big Data methods from appropriate scrutiny
- Wrongful conviction cases demonstrate dangers of invisible exculpatory evidence

### Judicial Gatekeeping
- Courts should recognize dark data limits Big Data's claimed omnipotence
- Daubert gatekeeping role becomes critical for AI-derived evidence
- Judges should demand that algorithms be "inspectable" and explainable
- Litigants must identify what data was left dark and why

## Relevance to Sustainable Computing

This article has significant implications for sustainable computing research:

1. **Data Minimization as Environmental Practice**: The storage imperative Grimm describes has both legal and environmental costs. Storing massive quantities of dark data consumes energy and physical resources. Data minimization principles, while framed here in legal terms, align with sustainability goals of reducing unnecessary data storage.

2. **Data Center Energy Consumption**: The article documents explosive growth in data storage (80-93% of data is "dark"). This unused data represents wasted computational and storage resources with real environmental footprints.

3. **E-Waste and Hardware Lifecycle**: Dark data accumulation drives demand for ever-expanding storage infrastructure, accelerating hardware obsolescence and e-waste generation.

4. **Cost-Benefit Analysis**: Grimm's analysis of the storage imperative (cheap storage vs. expensive analytics) should incorporate environmental externalities. The "true cost" of dark data includes its carbon footprint.

5. **Policy Frameworks**: Legal frameworks like GDPR's data minimization requirements and "right to be forgotten" create regulatory pressure that aligns legal compliance with environmental sustainability.

6. **Organizational Data Governance**: The article calls for organizations to develop better awareness of their dark data - a prerequisite for any data lifecycle management that could include environmental considerations.

## Citation

Grimm, D. J. (2019). The dark data quandary. *American University Law Review*, *68*(3), 761-821. https://digitalcommons.wcl.american.edu/aulr/vol68/iss3/2
