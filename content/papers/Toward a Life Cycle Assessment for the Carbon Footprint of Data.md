---
source_file: 2026/i609-sustainability/Toward a Life Cycle Assessment for the Carbon
  Footprint of Data-Mer.pdf
type: paper
authors: Gabriel Mersy, Sanjay Krishnan
community: Sustainable Computing
tags:
- sustainability
- i609
- data-lifecycle
- carbon-footprint
- green-computing
year: 2024
builds_on:
- '[[frameworks/Actor-Network Theory]]'
- '[[frameworks/Sociotechnical]]'
critiques: []
tensions_with: []
supports: []
key_claims:
- Approximately two-thirds of ICT emissions originate from user devices and networking
  rather than data centers, representing a critical gap in current carbon accounting
  methods
- Carbon provenance defined as 'an automated life cycle assessment for the carbon
  footprint of data' enables tracking emissions distributed across multiple entities
  through HTTP-style carbon headers
- Between 3394 and 5460 26-second videos captured via webcam produce carbon emissions
  equivalent to driving an average gasoline passenger vehicle one mile on the MISO
  grid
- Network transfer between Midwest and social media data center generates emission
  intensity of 1.51 g CO2 e/GB, requiring 268 GB to equal emissions from driving one
  mile
- Data wrinkles—progressive lossy approximations where 'error epsilon is traded for
  a strictly-positive bit reduction beta > 0'—offer unexplored carbon reduction opportunities
  across the data lifecycle
methodology: '[[methods/Design-Based Research]]'
sample_size: null
sample_type: null
context: Digital data lifecycle including IoT devices, data centers, and network infrastructure
study_type: theoretical
---

# Toward a Life Cycle Assessment for the Carbon Footprint of Data

## Summary

Gabriel Mersy and Sanjay Krishnan from the University of Chicago present a visionary paper that fundamentally reconceptualizes how we understand the environmental impact of digital data. Published in ACM SIGENERGY Energy Informatics Review (December 2024), this work emerges from the intersection of data science, environmental sustainability, and systems engineering. The authors argue that current carbon accounting methods for computing focus primarily on data centers and applications, thereby missing significant emissions from the broader data lifecycle including collection, transfer, and storage across edge devices and user equipment. Their key insight is that data should be treated as a manufactured good with its own cradle-to-grave carbon assessment, similar to how physical products are evaluated under life cycle assessment frameworks. The paper is significant because it addresses a critical gap in sustainable computing research: the approximately two-thirds of ICT emissions that originate from user devices and networking rather than data centers. By proposing carbon provenance as a tracking mechanism and introducing carbon-responsive data management techniques, this work provides both a conceptual framework and practical approaches for reducing the environmental footprint of the data economy. The research is particularly timely given the explosive growth in data generation from IoT devices, video streaming, and AI applications.

## Research Overview

The central research question asks: How can we comprehensively track and reduce the carbon emissions associated with data throughout its entire lifecycle, including costs distributed across multiple entities? The authors address this through a design science methodology, proposing novel frameworks and techniques rather than conducting empirical experiments.

The key concepts introduced include:

**Carbon Provenance**: Defined as "an automated life cycle assessment for the carbon footprint of data" (Mersy & Krishnan, 2024, p. 25), analogous to data provenance that tracks data lineage. The authors envision carbon metadata annotations that travel with data as it moves between entities.

**Embodied vs. Operational Carbon for Data**: The paper distinguishes between "embodied carbon from data collection, transfer, and storage, and operational carbon from data use" (p. 25). This mirrors the embodied/operational distinction in hardware carbon accounting but applies it to data itself.

**Carbon-Responsive Data**: The concept that "modulating the error of a data item can reduce carbon emissions" (p. 28), introducing approximation as a sustainability technique.

The methods include traceroute-based carbon intensity mapping for network transfers, Intel RAPL-based energy measurement for data collection, and theoretical frameworks for carbon header protocols in data exchange.

## Theoretical Framework

The paper builds on several theoretical foundations:

**Life Cycle Assessment (LCA)**: Borrowed from industrial ecology, LCA is "a common methodology to assess the carbon emissions over the product life cycle" with phases including "manufacturing, transport, product use, and recycling" (Mersy & Krishnan, 2024, p. 27).

**Data as a Good**: Following Jones and Tonetti's economic theory, the authors treat data as a manufactured good that can be "manufactured, transported, and stored in memory for later use" (p. 25), justifying a cradle-to-grave assessment.

**Scope 3 Emissions**: The paper frames data carbon costs within the Greenhouse Gas Protocol's value chain framework, arguing that "the cost of data must be derived from its entire value chain, spanning applications in organizations both upstream and downstream from the reporting organization" (p. 25).

**Approximation Computing**: The authors draw on the literature of approximate computing, defined as "the notion of trading error for performance" (p. 28), applying it specifically to data sustainability.

## Central Arguments

The paper advances two primary arguments:

**Argument 1: Carbon Provenance is Necessary**
The authors contend that "the life cycle carbon costs of data are often hidden from decision makers, especially costs that are distributed over multiple entities and costs that originate outside of the data center" (Mersy & Krishnan, 2024, p. 26). They propose HTTP-style carbon headers with four fields tracking embodied carbon, operational carbon, unique identifiers, and estimation methods. The argument is that without such tracking, organizations cannot make informed decisions about data sustainability.

**Argument 2: Carbon-Responsive Data Can Reduce Emissions**
The second major argument is that "there are many unexplored carbon reduction opportunities in the data life cycle that can complement existing approaches" (p. 26). This includes:

- **Adaptive sampling**: Adjusting sensor sampling rates based on carbon intensity
- **Multiresolution compression**: Creating multiple encodings transmitted based on current grid carbon intensity
- **Data wrinkles**: A novel concept where data progressively accumulates lossy approximations over time, defined as "an (epsilon, beta)-data wrinkle with respect to D where error epsilon is traded for a strictly-positive bit reduction beta > 0 via an approximation operation" (p. 30)

The authors connect these techniques to the observation that "if embodied costs far exceed operational costs, this may indicate that the item is wasting resources as unused 'dark data'" (p. 28).

## Evidence

The authors provide empirical illustrations to support their framework:

**Data Collection Costs**: Experiments measuring webcam video capture showed that "between 3394 and 5460 26-second videos taken during that day would produce the same amount of carbon emissions as driving an average gasoline passenger vehicle one mile" (Mersy & Krishnan, 2024, p. 26) on the MISO grid. Energy measurements used Intel RAPL for processor and DRAM power during MJPEG encoding at 30 FPS.

**Data Communication Costs**: Network transfer analysis via traceroute estimated "an emission intensity estimate of 1.51 g CO2 e/GB" for transfers between the Midwest and a social media data center, meaning "it would take 268 GB to produce the emissions equivalent to driving an average gasoline passenger vehicle one mile" (p. 26).

**Supporting Statistics**: The paper cites that "estimates place the fraction of carbon emissions from 'user' devices and networking at around two-thirds of ICT's total emissions" (p. 25), highlighting the magnitude of overlooked emissions.

**Limitations**:
- The proposed techniques remain largely theoretical without full system implementations
- The estimation methods for process-level energy require further validation
- Privacy implications of carbon provenance tracking are not addressed
- The paper acknowledges "open questions concerning the apportionment of hardware embodied carbon among data items" (p. 30)
- Network energy proportionality assumptions may not hold across all device types
- The granularity of data items for carbon accounting is left flexible, which could complicate standardization

## Conclusion

This paper makes a compelling case for reconceiving data as an environmental liability that requires lifecycle tracking and active management. The distinction between embodied and operational carbon for data is particularly valuable, as it enables identification of "dark data" that consumes resources without generating value. The carbon provenance concept addresses the fragmentation problem where emissions are siloed within individual organizations, preventing meaningful optimization across data value chains.

For future reference, the key takeaways are: (1) Data carbon accounting must extend beyond the data center to include edge collection, network transfer, and distributed storage; (2) Carbon metadata can travel with data through HTTP-style headers; (3) Approximation techniques including adaptive sampling, multiresolution compression, and progressive data degradation ("data wrinkles") offer unexplored opportunities for emission reduction; (4) The embodied/operational distinction helps identify wasteful data practices.

The practical implications for sustainable system design include: implementing carbon-aware sampling rates for IoT sensors, considering network carbon intensity when routing data transfers, and designing data retention policies that progressively reduce storage requirements for aging data. This work provides foundational concepts for what could become a new subfield of carbon-aware data management.

## APA Citation

Mersy, G., & Krishnan, S. (2024). Toward a life cycle assessment for the carbon footprint of data. *ACM SIGENERGY Energy Informatics Review, 4*(5), 25-33. https://doi.org/10.1145/2858036.2858378

## Discussion Questions

1. How might carbon provenance tracking intersect with privacy concerns, particularly when detailed data lineage and usage patterns could reveal sensitive organizational information?

2. The paper proposes "data wrinkles" as a way to progressively degrade data over time. What types of data could tolerate such treatment, and what new user interfaces or consent mechanisms would be needed to implement this?

3. Given that approximately two-thirds of ICT emissions come from user devices and networking, how should responsibility for data carbon emissions be allocated between data producers, infrastructure providers, and data consumers in a carbon trading framework?

4. The authors note that carbon intensity varies significantly by geography and time. How might real-time carbon-aware data systems adapt their behavior, and what are the potential equity implications if some users consistently receive lower-quality data due to their grid's carbon intensity?

## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Life Cycle Assessment]]
- [[topics/Data Management]]
- [[topics/Edge Computing]]
- [[topics/Green Computing]]
