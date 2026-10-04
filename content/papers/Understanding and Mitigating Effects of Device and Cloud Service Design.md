---
source_file: 2026/i609-sustainability/Understanding and Mitigating the Effects of
  Device-Preist_Shein_Blevis.pdf
type: paper
authors: Chris Preist, Dan Schien, Eli Blevis
community: Sustainable Computing
tags:
- sustainability
- i609
- HCI
- interaction-design
- digital-infrastructure
- sustainable-HCI
year: 2016
builds_on:
- '[[frameworks/Human-Centered Design]]'
- '[[frameworks/Value Sensitive Design]]'
- '[[frameworks/Actor-Network Theory]]'
- '[[frameworks/Critical Theory]]'
critiques:
- '[[concepts/Technological Determinism]]'
tensions_with:
- '[[frameworks/Human-Centered Design]]'
supports:
- '[[concepts/Wicked Problems]]'
- '[[frameworks/Sociotechnical]]'
key_claims:
- Infrastructure can account for up to 85% of total environmental impact for some
  digital services, with total greenhouse gas impact estimated at 253 Mt CO2-e per
  annum
- Ten cornucopian design principles (PERSONAL, VARIETY, INSTANT, SHAREABLE, HIGH QUALITY,
  PERVASIVE, CONTINUOUS ACCESS, ETERNAL, EPHEMERAL, RICH/CROSS-MODAL/UBIQUITOUS) collectively
  drive unsustainable infrastructure growth
- Digital waste—accessing cloud services without meaningful use—is analogous to leaving
  lights on in empty rooms and represents a significant source of environmental impact
- Web pages have increased to approximately 150 times their size in 1995, now averaging
  over 2MB, demonstrating infrastructure demand growth
- 'The Rubric of Infrastructural Effects (RoIE) extends Blevis''s Material Effects
  framework with five evaluation questions to assess design impact on digital infrastructure:
  expansion/obsolescence, increased use, mitigation, digital waste, and infrastructure
  sharing'
methodology: '[[methods/Literature Review]]'
sample_size: null
sample_type: null
context: Digital infrastructure and cloud service design practices
study_type: theoretical
---

# Understanding and Mitigating the Effects of Device and Cloud Service Design Decisions on the Environmental Footprint of Digital Infrastructure

## Summary

Chris Preist and Dan Schien from the University of Bristol, along with Eli Blevis from Indiana University, present a landmark critique of interaction design practices and their environmental consequences in this CHI 2016 paper. The work emerges from the Sustainable HCI community but extends significantly beyond traditional device-focused sustainability research to address the often-invisible digital infrastructure that supports modern interactive services. The authors identify a critical blind spot in sustainable design: while designers focus on device efficiency, the cloud services, servers, and network equipment that enable interactive experiences can account for up to 85% of total environmental impact for some services. The paper is particularly significant for introducing the "cornucopian paradigm" as a lens for understanding how user-centered design principles inadvertently drive infrastructure growth through ten identified design principles (PERSONAL, VARIETY, INSTANT, etc.). By extending Blevis's influential Rubric of Material Effects to create the Rubric of Infrastructural Effects (RoIE), the authors provide designers with actionable questions to assess and mitigate the environmental impact of their design decisions. The work represents a bridge between Sustainable HCI and industrial ecology, situating design choices within larger systems of environmental impact including data centers, network equipment, and content creation infrastructure.

## Research Overview

The central research question asks: How do user-centered design decisions for interactive devices and services influence the environmental footprint of the digital infrastructure, and what design strategies can mitigate these effects?

The authors employ critical design analysis methodology, combining literature review with design criticism to identify patterns of problematic practice and propose alternatives. They explicitly position their work within the tradition of Sustainable Interaction Design (SID), which "describes papers oriented around using sustainability as a 'critical lens'...which tend to see a need to fundamentally rethink the methods of HCI in order address sustainability...see designers as complicit in the unsustainability of current interactive products, aiming to change design to encourage more sustainable effects" (Preist et al., 2016, p. 1325).

Key concepts include:

**Digital Infrastructure**: Defined as "the infrastructure that grows in support of interactive devices and the cloud services they use" including "servers, core and edge network equipment, and potentially content creation equipment such as cameras, sensors etc." (p. 1324).

**Cornucopian Paradigm**: The dominant design mindset "reinforced both by faith that Moore's law will continue to hold and deliver efficiency improvements, and by discourse around the cloud which emphasises the 'infinite scalability' of services" (p. 1327).

**Rubric of Infrastructural Effects (RoIE)**: An extension of Blevis's framework with five core evaluation questions for assessing design impact on infrastructure.

## Theoretical Framework

The paper synthesizes multiple theoretical traditions:

**Sustainable Interaction Design (SID)**: Following Blevis's foundational work, SID argues "that designers of digital products must also be responsible for explaining how resource use is impacted by the artefacts and services they design, as an intrinsic part of the design" (Preist et al., 2016, p. 1324). The paradigm distinguishes between "Sustainability in Design" (how to take account of sustainability as part of the material design of products) and "Sustainability through Design" (how to support sustainable lifestyles and decision-making through the design of technology) (p. 1325).

**IPAT Equation**: From environmental science, this framework shows how Impact = Population x Affluence x Technology, applied here to understand how design affects the technology multiplier.

**Reinforcing Feedback Loop**: A systems dynamics concept where "the provision of digital services to high-end users stimulates latent demand in mainstream users for such services, which means there is a market for infrastructure expansion provided it goes alongside cost reduction in bandwidth provision" (p. 1326-1327). This creates a growth spiral between infrastructure capacity, service design, and demand.

**Eco-Efficiency vs. Sufficiency Paradigms**: The authors position their work as initially reformist (eco-efficiency) but extending toward more radical paradigms including "computing within limits" and "collapse informatics."

## Central Arguments

**Argument 1: The Cornucopian Paradigm Drives Unsustainable Growth**

The authors identify ten design principles embedded in the cornucopian paradigm that collectively drive infrastructure demand:

1. **(C1) PERSONAL**: Services increasingly individualized rather than shared
2. **(C2) VARIETY**: Unlimited storage leading to unused content accumulation
3. **(C3) INSTANT**: Near-zero latency requirements driving server over-provisioning
4. **(C4) SHAREABLE**: Content sharing increasing cloud storage and bandwidth
5. **(C5) HIGH QUALITY**: Resolution increases outpacing efficiency gains
6. **(C6) PERVASIVE**: Multi-device access requiring synchronization infrastructure
7. **(C7) CONTINUOUS ACCESS**: Always-on expectations growing network coverage
8. **(C8) ETERNAL**: "Users expect content that they generate to be 'always alive and always available'" (p. 1327) increasing storage demands
9. **(C9) EPHEMERAL**: Paradoxically, throwaway content still requires storage
10. **(C10) RICH, CROSS-MODAL AND UBIQUITOUS**: Multiple simultaneous services amplifying all other factors

The authors argue that "in many ways, these principles are desirable to the user. This contrasts with design approaches such as Choreographed Obsolescence and Disposable Technology, which arguably encourage waste primarily to improve revenue rather than to benefit the user" (p. 1327-1328).

**Argument 2: Design Must Account for Infrastructure Beyond the Device**

Citing estimates that "the greenhouse gas impact of the manufacture and running of this digital infrastructure to be 253 Mt CO2-e per annum, of similar order of magnitude to that of computers and other end user devices (278 Mt CO2-e p.a.)" (p. 1324), the authors argue that device-centric sustainability analysis captures only half the picture. For specific services, "the infrastructure can account for up to 85% of the environmental impact" (p. 1325).

**Argument 3: The RoIE Framework Enables Infrastructure-Aware Design**

The Rubric of Infrastructural Effects poses five questions:
- "(E1) Does the design encourage infrastructural expansion or obsolescence?"
- "(E2) Does the design encourage increased infrastructural use?"
- "(E3) Does the design mitigate or reduce infrastructural use in some way?"
- "(E4) Does the design encourage digital waste, or the avoidance of it?"
- "(E5) Does the design promote the sharing of infrastructure?" (p. 1328)

## Evidence

The paper provides extensive examples illustrating each design principle and RoIE question:

**Digital Waste Evidence**: "Digital waste is the accessing of a cloud-based digital service without actually making use of it, or only making partial use of it. It is the digital equivalent of leaving the lights on in an empty room" (Preist et al., 2016, p. 1330). Specific examples include:
- YouTube videos played for audio only (background music streaming)
- Podcast downloads that are never listened to
- Automatic cloud photo backup of ephemeral images

**Infrastructure Growth**: "Action Cams are over 5m units per year and increasing" (p. 1329), with associated video content placing demands on storage and network infrastructure.

**Positive Design Examples**:
- BBC iPlayer defaulting to standard definition, requiring explicit opt-in for HD
- Spotify defaulting to 160Kbps ('normal') quality
- Video scrubber preview images reducing need to download entire videos
- Freifunk mesh network for WiFi sharing

**Scale of Impact**: "Web pages have increased to approximately 150 times their size in 1995, now averaging over 2MB" (p. 1330).

**Limitations**:
- Limited quantitative analysis of specific interventions
- Examples are primarily illustrative rather than empirically tested
- The paper acknowledges that "material effects of infrastructural use are often outside the 'boundary' of awareness of the designer" (p. 1333)
- Tension between user desires and sustainability not fully resolved

## Conclusion

This paper fundamentally reframes sustainable HCI by extending the scope of design responsibility from devices to the entire digital infrastructure ecosystem. The cornucopian paradigm critique is particularly valuable as it names and systematizes the implicit assumptions driving unsustainable design practices, making them visible and therefore contestable.

For future recall, the key insights are: (1) Infrastructure can dominate environmental impact, sometimes reaching 85% of total footprint; (2) Ten cornucopian design principles (C1-C10) collectively drive infrastructure growth; (3) The RoIE framework provides five evaluation questions for infrastructure-aware design; (4) "Digital waste" is a novel concept analogous to leaving lights on; (5) Default settings matter significantly for aggregate impact; (6) Moving beyond eco-efficiency may require consideration of "computing within limits" and similar paradigms.

The practical design implications include: defaulting to lower-quality options, detecting and reducing digital waste patterns, enabling and encouraging sharing of resources, questioning whether always-on availability is truly necessary, and designing for graceful degradation under constrained infrastructure scenarios. This work should be required reading for any designer working on cloud-connected services.

## APA Citation

Preist, C., Schien, D., & Blevis, E. (2016). Understanding and mitigating the effects of device and cloud service design decisions on the environmental footprint of digital infrastructure. In *Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems* (pp. 1324-1337). ACM. https://doi.org/10.1145/2858036.2858378

## Discussion Questions

1. The cornucopian paradigm is deeply embedded in user expectations. How might designers navigate the tension between user desires for unlimited, instant, high-quality services and sustainability imperatives without losing users to competitors who ignore sustainability?

2. The paper identifies "digital waste" such as streaming video for audio-only consumption. What technical mechanisms could detect and reduce such waste without being perceived as intrusive or paternalistic?

3. The authors suggest that some services may need to be restricted to stay within planetary boundaries. Who should make decisions about which services are essential enough to warrant infrastructure investment, and through what governance mechanisms?

4. How might the RoIE framework be operationalized in design practice? What would a "sustainability impact assessment" look like for a new cloud service, and who should be responsible for conducting and acting on such assessments?


## Related Papers

## Connections

- [[topics/Sustainable Computing]]
- [[communities/Sustainable Computing]]
- [[topics/Human-Computer Interaction]]
- [[topics/Sustainable Interaction Design]]
- [[topics/Cloud Computing]]
- [[topics/Design Ethics]]
- [[people/Eli Blevis]]
