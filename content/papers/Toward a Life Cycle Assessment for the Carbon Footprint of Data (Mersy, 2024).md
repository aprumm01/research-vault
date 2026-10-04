---
title: "Toward a Life Cycle Assessment for the Carbon Footprint of Data"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/Toward a Life Cycle Assessment for the Carbon Footprint of Data-Mer.pdf"
type: paper
authors:
  - Gabriel Mersy
  - Sanjay Krishnan
year: 2024
venue: "ACM SIGENERGY Energy Informatics Review"
volume: 4
issue: 5
pages: "25-33"
doi: ""
builds_on:
  - "[[Life Cycle Assessment]]"
  - "[[Carbon Footprint Measurement]]"
  - "[[Data Provenance]]"
supports:
  - "[[Sustainable Computing]]"
  - "[[Green Data Centers]]"
  - "[[Carbon-Aware Computing]]"
critiques:
  - "[[Data Center Carbon Accounting]]"
tensions_with:
  - "[[Performance-First Computing]]"
key_claims:
  - "Data should be treated as a manufactured good with embodied and operational carbon costs"
  - "Carbon provenance can track lifecycle emissions across the entire data value chain"
  - "Carbon-responsive data techniques can reduce emissions through approximation and lossy aging"
  - "Two-thirds of ICT carbon emissions come from user devices and networking outside data centers"
methodology: "Conceptual framework with empirical estimation of data collection and transfer carbon costs"
study_type: "Position paper with empirical analysis"
context: "Growing data economy with increasing environmental impact from data collection, transfer, and storage"
tags:
  - life-cycle-assessment
  - carbon-footprint
  - data-management
  - environmental-impact
  - sustainable-computing
  - carbon-provenance
  - edge-computing
---

# Toward a Life Cycle Assessment for the Carbon Footprint of Data

## Summary

This paper introduces the concept of **carbon provenance** - a life cycle assessment framework for tracking the carbon footprint of data across its entire value chain. The authors argue that data should be viewed as a manufactured good, similar to hardware, with both **embodied carbon** (emissions from collection, transfer, and storage) and **operational carbon** (emissions from data use). The paper proposes a system where carbon annotations travel with data through APIs, enabling end-to-end carbon accounting across organizations.

The key insight is that traditional carbon accounting at the data center level misses approximately two-thirds of ICT emissions that occur at edge devices and during network transfer. By tracking carbon costs at the data item level, organizations can make informed decisions about data optimization, storage, and transmission.

## Key Concepts

### Carbon Provenance
A metadata annotation scheme that tracks the cumulative carbon footprint of data items as they move through the data economy. Inspired by data provenance systems, carbon provenance uses four HTTP-style headers:
- `X-Message-Carbon-Embodied`: Carbon from previous collection, transfer, and storage
- `X-Message-Carbon-Operational`: Carbon from previous use of the data
- `X-Message-Unique-Identifier`: Unique ID for cost aggregation across entities
- `X-Message-Carbon-Estimation-Method`: Accounting standard used for consistency

### Embodied vs Operational Carbon for Data
- **Embodied carbon**: Emissions separated from data use - incurred at sensors, during network transfer, in storage operations
- **Operational carbon**: Emissions accumulated during data use - processing, inference, analysis

### Carbon-Responsive Data
Techniques for reducing emissions by modulating data quality/quantity based on carbon intensity:
1. **Carbon-adaptive Approximation**: Adjusting sampling rates or query precision based on grid carbon intensity
2. **Carbon-adaptive Compression**: Choosing compression levels based on predicted network path carbon intensity (multiresolution compression)
3. **Lossy Data Aging (Data Wrinkles)**: Progressively reducing data quality over time to save storage and network resources

## Key Findings

### Data Collection Carbon Costs
- Collecting 24 laptop webcam videos (26 seconds each, 30 FPS, MJPEG) produces 74-119 mg CO2e depending on grid carbon intensity
- In MISO grid (similar to US average), daily collection of 3394-5460 such videos equals driving a car one mile

### Data Communication Carbon Costs
- Network transfer between Midwest and data center produces approximately 1.51 g CO2e per GB
- Transferring 268 GB would equal emissions from driving a car one mile
- A 1 GB video upload would require 267 complete video views to match transfer emissions

### Key Technical Contributions
- Open-source API toolkit for on-device carbon estimation
- Two-phase energy estimation: hardware statistics gathering + process-level estimation
- Machine learning models combining CPU/power statistics with I/O device models

## Relevance to Sustainable Computing

This paper is highly relevant to sustainable computing research for several reasons:

1. **Shifts Focus to Data Layer**: Most carbon accounting focuses on hardware or data centers; this paper argues for tracking carbon at the data granularity level

2. **End-to-End Value Chain**: Addresses Scope 3 emissions by tracking carbon across organizational boundaries - critical for comprehensive sustainability reporting

3. **Actionable Optimization**: Carbon-responsive techniques (approximation, compression, aging) provide concrete mechanisms for reducing emissions while maintaining utility

4. **Edge Computing Implications**: Highlights that edge devices contribute two-thirds of ICT emissions, suggesting optimization opportunities outside traditional data center focus

5. **Trade-off Framework**: Introduces the concept of "dark data" - data where embodied costs exceed operational value, indicating wasted resources

### Limitations Acknowledged
- Current focus is on hardware energy use
- Open questions about apportioning hardware embodied carbon among data items
- Security implications of carbon headers not fully addressed

## Citation

Mersy, G., & Krishnan, S. (2024). Toward a life cycle assessment for the carbon footprint of data. *ACM SIGENERGY Energy Informatics Review*, *4*(5), 25-33.
