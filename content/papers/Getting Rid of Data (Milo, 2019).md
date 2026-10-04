---
title: "Getting Rid of Data"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/3326920.pdf"
type: paper
authors:
  - Tova Milo
year: 2019
venue: ACM Journal of Data and Information Quality
builds_on:
  - "[[concepts/Data Management]]"
  - "[[concepts/Data Lifecycle]]"
supports:
  - "[[concepts/Data Minimization]]"
  - "[[concepts/Dark Data]]"
  - "[[concepts/Digital Sustainability]]"
critiques: []
tensions_with: []
key_claims:
  - Intelligent data disposal is essential for managing the exponentially growing digital universe
  - Data disposal policies must balance storage constraints, regulatory requirements, and analytical utility
  - Provenance metadata is critical for effective query evaluation over retained/summarized data
  - Machine learning can help derive effective data retention and summarization policies
  - Human-in-the-loop approaches are needed for approving disposal decisions
methodology: Literature review and conceptual framework development
study_type: theoretical
context: Big data management, data retention, GDPR compliance
---

# Getting Rid of Data

## Summary

This paper addresses a critical challenge in the data-centered revolution: the need for intelligent, systematic data disposal. Milo argues that while we are experiencing unprecedented data collection and analysis capabilities, the exponential growth of data (estimated to outstrip storage capacity by six zettabytes by 2020) creates an unsustainable situation. Beyond storage constraints, uncontrolled data retention poses significant privacy and security risks, as recognized by regulations like the EU General Data Protection Regulation (GDPR).

The paper outlines the conceptual and technical foundations required for systematic data disposal. A key challenge is developing "data disposal policies" that determine which data should be discarded and what summaries should be retained so that data utilization is minimally harmed. This is complicated by the need to satisfy multiple constraint types simultaneously: storage constraints require optimization to determine what can be discarded, while regulatory constraints mandate what must be deleted or retained for specific time periods.

Milo proposes a "dispose by design" framework that allows declarative expression of data properties, retention constraints, and desired disposal strategies. The framework should support automatic policy derivation, enforcement, and efficient query evaluation over retained information. The paper emphasizes that provenance metadata is essential for tracking what data has been omitted and what summaries have been retained, enabling effective query answering and regulatory compliance.

The paper also discusses the role of machine learning in deriving effective retention policies and summarizations, the need for incremental computation as data evolves, and the importance of human-in-the-loop approaches for approving disposal decisions. Throughout, Milo stresses that ad hoc solutions are insufficient—we need principled, shareable approaches to secure the data-centered revolution.

## Key Concepts

- **Data Disposal Policy**: Rules determining which data should/may be discarded and what summaries should be kept
- **Dispose by Design**: A declarative framework for expressing data properties, retention constraints, and disposal strategies
- **Data Provenance**: Metadata tracking the source of information and computational processes it underwent, critical for explaining query results and maintaining regulatory compliance
- **Incremental View Maintenance**: Techniques for evaluating queries using only retained data, treating retained information as a "view" over full data
- **Approximate Query Processing**: Methods for providing approximate answers to queries at reduced cost, using sampling from retained data and summaries
- **Human-in-the-Loop**: Involving human input to approve disposal policies or choose among multiple options

## Key Findings

1. The demand for data storage is growing exponentially and will significantly exceed available storage capacity, making intelligent data disposal essential.

2. Data disposal must satisfy multiple constraint types: storage constraints (optimization problem), regulatory constraints (compliance requirements), and analytical utility (maintaining query capabilities).

3. Provenance metadata is critical but challenging to manage at scale—provenance data itself may need disposal policies applied recursively.

4. Existing data sketching and summarization techniques are task-specific and not easily combined; a declarative framework is needed.

5. Machine learning can be employed to learn data access patterns and derive effective retention policies that comply with regulations.

6. Dynamic incremental computation is unavoidable—as data is disposed, cleaning, integration, querying, and analysis must all work with partial/summarized data.

7. Verification of compliance with data protection regulations (like GDPR) is an important complementary research direction involving encryption, differential privacy, and program analysis.

## Relevance to Sustainable Computing

This paper is directly relevant to sustainable computing and digital sustainability in several ways. First, it addresses the environmental implications of unconstrained data growth—storing and processing ever-increasing amounts of data requires significant energy and physical infrastructure. By advocating for intelligent data disposal, Milo implicitly supports reduced energy consumption and carbon footprint associated with data centers.

The concept of "dark data" (data collected but never used) is closely related to Milo's discussion of redundant data that "can be discarded with no harm." The paper's framework for systematic data disposal provides theoretical foundations for reducing digital hoarding and unnecessary data retention.

Furthermore, the paper's emphasis on regulatory compliance (GDPR) connects to the broader sustainability principle that responsible data management is not just about efficiency but about ethical stewardship of digital resources. The "dispose by design" approach parallels sustainable computing principles like "privacy by design" and energy-efficient system design.

## Citation

Milo, T. (2019). Getting Rid of Data. *ACM Journal of Data and Information Quality*, 12(1), Article 1. https://doi.org/10.1145/3326920
