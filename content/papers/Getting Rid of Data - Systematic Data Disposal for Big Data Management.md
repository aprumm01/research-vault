---
source_file: 2026/i609-sustainability/3326920.pdf
type: paper
authors: Tova Milo
community: Sustainable Computing
tags:
- sustainability
- i609
- data-management
- data-disposal
- GDPR
- big-data
year: 2019
builds_on:
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Human-in-the-Loop Pedagogy]]'
key_claims:
- By 2020, demand for storage will outstrip production by six zettabytes—nearly double
  the available storage capacity, necessitating systematic data disposal frameworks
  rather than continued accumulation
- Current data disposal approaches are ad hoc and application-specific, lacking solid
  scientific foundations for Web-scale data disposal that encompasses formal models,
  reasoning capabilities, and efficient query evaluation over partial data
- GDPR and similar regulations mandate data minimization and retention limits, transforming
  data disposal from optional optimization into legal requirement requiring 'dispose
  by design' frameworks
- Smaller data sets often require smaller processing resources and less sophisticated
  tools, providing economic benefits beyond storage savings through reduced computational
  costs
- Effective data disposal must retain the knowledge hidden in the data while respecting
  storage, processing, and regulatory constraints, requiring intelligent summarization
  rather than simple deletion
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: null
context: Database management and data governance in context of exponential data growth
  and GDPR compliance
study_type: theoretical
---

# Getting Rid of Data

## Summary

Tova Milo, a computer science professor at Tel Aviv University, authored this invited article for the ACM Journal of Data and Information Quality in 2019. The paper addresses the critical challenge of systematic data disposal in an era of exponential data growth, where storage demand is expected to exceed capacity by six zettabytes. Milo's background in database management and data-centric systems positions her as an authority on this emerging field. The article represents a theoretical and methodological contribution to information systems, particularly data management and governance. The paper's significance lies in its recognition that data disposal is not merely a storage problem but encompasses privacy, security, regulatory compliance (specifically GDPR), and computational efficiency concerns. Milo argues for developing comprehensive "dispose by design" frameworks rather than relying on ad hoc, application-specific solutions. The work is positioned at the intersection of database theory, privacy regulation, and sustainable computing, making it relevant for researchers studying the environmental implications of data retention and the organizational costs of digital storage.

## Research Overview

The central research question addresses how organizations can systematically determine what data to discard while maintaining the utility of retained information for analysis and query answering. Milo frames this as: "Given a dataset, a set of constraints, and an analysis workload expressed as a class of programs (the precise representation of the expected workload is a research goal), can we effectively derive a data disposal policy so the retained information is 'sufficient' (in a well-specified manner) for every program in the class?" (Milo, 2019, p. 1:2).

The methodology is conceptual and theoretical, synthesizing existing techniques from data sketching, summarization, compression, and deletion while identifying gaps requiring new research. Key concepts include **data disposal policy** (determining which data to discard and what summaries to retain), **data provenance** (tracking the origin and transformation history of data), and **dispose by design** (a framework for declaratively expressing data properties and retention constraints).

The paper emphasizes that "the difficulty notably stems from the distinct, intricate requirements that each of these types of constraints entails" (Milo, 2019, p. 1:2), highlighting the tension between storage optimization and regulatory compliance. The research connects to machine learning approaches for deriving retention policies and incremental computation for maintaining summaries as data evolves.

## Theoretical Framework

The paper draws on multiple theoretical foundations. **Data provenance theory** provides mechanisms for tracking "the source of information and the computational process it undergoes" (Milo, 2019, p. 1:3), essential for explaining query results over retained data. Provenance enables compliance verification and audit trails required by regulations like GDPR.

**Declarative specification frameworks** are proposed as alternatives to hard-coded disposal policies. Milo advocates for "a declarative framework that allows to express (a) data and data usage properties, (b) data deletion and summarization methods, as well as the resulting summary properties, and (c) privacy/retention constraints and criteria" (Milo, 2019, p. 1:4).

**Incremental view maintenance** theory addresses how retained data (viewed as "views" over original data) must be updated dynamically as new data arrives. The concept of **approximate query processing** is invoked to handle queries over summarized data, where exact answers may be unavailable but bounded approximations suffice.

The framework also incorporates **human-in-the-loop** considerations, recognizing that "data disposal may be executed automatically or may require human input to approve data disposal or choose among multiple (possibly prioritized) disposal policies" (Milo, 2019, p. 1:5).

## Central Arguments

Milo's primary argument is that current approaches to data management treat disposal as an afterthought, leading to unsustainable data accumulation with significant environmental, economic, and legal consequences. She contends that "if we do not learn how to effectively dispense with some of this data, then we will simply drown" (Milo, 2019, p. 1:1).

The paper argues for a paradigm shift from storage-centric to disposal-centric data management. The sub-claims supporting this include:

1. **Regulatory imperative**: GDPR and similar regulations mandate data minimization and retention limits, making disposal a legal requirement rather than optional optimization.

2. **Economic benefits**: "Smaller data sets often require smaller processing resources and less sophisticated tools" (Milo, 2019, p. 1:2), reducing computational costs.

3. **Knowledge preservation**: Effective disposal must retain "the knowledge hidden in the data while respecting storage, processing, and regulatory constraints" (Milo, 2019, p. 1:1), requiring intelligent summarization rather than simple deletion.

4. **Scalability necessity**: With sensor networks generating massive data volumes where "most of it (usually based on ad hoc decision rules) gets thrown away and is not even transmitted off the sensor to the base station/database" (Milo, 2019, p. 1:3), systematic disposal is already occurring but without principled frameworks.

The argument culminates in calling for "solid scientific foundations for Web-scale data disposal" that encompass formal models, reasoning capabilities, and efficient query evaluation over partial data.

## Evidence

Milo supports her arguments primarily through synthesis of existing research and extrapolation of current trends. The statistical projection that "by the year 2020 the demand for storage will outstrip production by six zettabytes—nearly double the available storage capacity" (Milo, 2019, p. 1:1, citing reference 27) establishes urgency.

Evidence from current practice demonstrates inadequacy: "Every single initiative has to battle, almost from scratch, the same tough challenges. The ad hoc solutions, even when successful, are application-specific and rarely sharable" (Milo, 2019, p. 1:2).

The paper cites research on data sketching techniques, graph summarization methods, and declarative specification approaches as partial solutions requiring integration. Reference to GDPR (General Data Protection Regulation) provides regulatory grounding for mandatory disposal requirements.

**Limitations** include the absence of empirical validation—the paper is entirely conceptual without case studies or experimental evaluation. The framework remains at a high level of abstraction, with implementation challenges acknowledged but not addressed: "But much more work is needed to extend these ideas to the modern big-data world of today" (Milo, 2019, p. 1:4).

The paper does not quantify environmental impacts of data storage or disposal, leaving the sustainability connection implicit. Additionally, the tension between disposal and potential future value of data ("retaining that data for a long time, hoping it may become valuable or needed some day, is unnecessarily costly and indefensibly risky") is noted but not empirically examined.

The scope is limited to structured data management, with less attention to unstructured data, multimedia content, or personal information management contexts where disposal decisions may differ significantly.

## Conclusion

For recall six months from now, this paper establishes the theoretical case for systematic data disposal as a first-class concern in data management, driven by storage constraints, regulatory requirements (particularly GDPR), and computational efficiency. Milo's "dispose by design" framework proposes declarative specification of disposal policies combining data provenance tracking, summarization methods, and retention constraints. The key insight is that disposal is not merely deletion but intelligent knowledge preservation through summarization and metadata retention. Critical gaps identified include: provenance annotation for summarized data, propagation of provenance through analysis pipelines, scalable disposal and query algorithms, and human-in-the-loop mechanisms for disposal decisions. The paper connects to sustainability through reduced storage and processing requirements, though environmental impacts are not quantified. For research on digital sustainability, this provides theoretical grounding for arguing that data minimization has technical merit beyond regulatory compliance.

## APA Citation

Milo, T. (2019). Getting rid of data. *Journal of Data and Information Quality*, *12*(1), Article 1, 1-7. https://doi.org/10.1145/3326920

## Discussion Questions

1. How might the "dispose by design" framework be adapted to address the specific environmental costs of data storage, and what metrics would quantify the sustainability benefits of systematic disposal?

2. Given that GDPR mandates data minimization, why do organizations continue to accumulate data, and what organizational or technical barriers prevent adoption of disposal policies?

3. How does the tension between potential future value of data and immediate disposal benefits map onto sustainability frameworks that balance present costs against future uncertainty?

4. What role should machine learning play in deriving disposal policies, and how do we ensure such automated systems respect both privacy regulations and organizational knowledge needs?

## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Data Governance]]
- [[topics/GDPR Compliance]]
- [[topics/Big Data Management]]
