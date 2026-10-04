---
source_file: 2026/i609-sustainability/soups2018-murillo.pdf
type: paper
authors: Ambar Murillo, Andreas Kramm, Sebastian Schnorf, Alexander De Luca
community: Sustainable Computing
tags:
- sustainability
- i609
- data-deletion
- mental-models
- privacy
- user-understanding
- Google
year: 2018
builds_on:
- '[[frameworks/Cognitive Load]]'
- '[[frameworks/Human-Centered Design]]'
critiques: []
tensions_with: []
supports:
- '[[concepts/Illusion of Competence]]'
- '[[concepts/Technological Anxiety]]'
key_claims:
- 82% of users (18/22) are 'Backend-Aware' and suspect data persists after deletion,
  while 18% (4/22) are 'UI-Based' and believe deletion is immediate and complete
- Even technically sophisticated users fail to consider that deleted data may have
  generated derived information (analytics, aggregations, ML training data) that persists
  indefinitely
- Current deletion interfaces create a transparency gap that leads to either false
  confidence in complete data removal or unnecessary anxiety about data persistence
- 'Users'' mental models of data deletion are incomplete regardless of technical background,
  with experts identifying six dimensions of data persistence users fail to understand:
  Backend, Time, Backup, Derived Information, Anonymization, and Shared Copy'
methodology: '[[methods/Mixed Methods]]'
sample_size: 29
sample_type: 22 general users (11 technical, 11 non-technical backgrounds; ages 19-61)
  and 7 privacy/security domain experts
context: Online data deletion practices across various digital services
study_type: empirical
---

# "If I press delete, it's gone" - User Understanding of Online Data Deletion and Expiration

## Summary

This Google-conducted study investigates how users understand what happens when they delete their online data. Through interviews with 22 participants and focus groups with 7 privacy/security experts, the research identifies two dominant mental models: "UI-Based" users (4/22) who believe deletion happens immediately and completely when they press delete, and "Backend-Aware" users (18/22) who recognize data may persist in backend systems. The study reveals significant gaps between user expectations and technical reality, with implications for transparent privacy design and sustainable computing.

## Research Overview

**Research Questions:**
1. How do users understand what happens when they delete their online data?
2. What mental models do users hold about data deletion?
3. What concerns and misconceptions exist about data persistence?

**Method:** 
- Phase 1: Semi-structured interviews with 22 participants (11 female, 11 male; ages 19-61; 11 technical, 11 non-technical backgrounds)
- Phase 2: Two focus groups with 7 domain experts (3 + 4 participants) in privacy and security
- Qualitative analysis using open and axial coding

**Key Findings:**
- Two primary mental models identified: UI-Based (4 users) and Backend-Aware (18 users)
- Even "aware" users had significant misconceptions about data persistence
- Expert focus groups identified 6 key themes: Backend, Time, Backup, Derived Information, Anonymization, and Shared Copy
- Users want more transparency about what deletion actually means

## Theoretical Framework

The paper employs **mental models theory** from cognitive psychology, which posits that people form internal representations of how systems work based on their experiences and understanding. Mental models:

1. Are often incomplete or inaccurate
2. Guide user expectations and behavior
3. Can be influenced by interface design and feedback
4. Differ based on technical background and experience

The framework also draws on **privacy research** traditions examining:
- User understanding of data collection
- Trust in service providers
- The gap between privacy attitudes and behaviors

## Central Arguments

1. **Mental Model Dichotomy**: Users fall into two categories - those who take interfaces at face value (UI-Based) and those who suspect backend persistence (Backend-Aware). Neither group fully understands the technical complexity.

2. **Transparency Gap**: Current deletion interfaces fail to communicate what actually happens to deleted data, leading to false confidence or unnecessary anxiety.

3. **Derived Data Blindspot**: Even sophisticated users rarely consider that their deleted data may have generated derived information (analytics, aggregations, ML training data) that persists.

4. **Shared Copy Complexity**: Users struggle to understand what happens when deleted data has been shared with or copied by third parties.

5. **Time Dimension**: The temporal aspects of deletion (immediate vs. gradual, backup retention periods) are poorly understood.

## Evidence

**Mental Model Distribution:**
- UI-Based: 4/22 participants (18%)
- Backend-Aware: 18/22 participants (82%)

**UI-Based Model Characteristics:**
- Believe deletion is immediate and complete
- Trust the interface feedback ("If I press delete, it's gone")
- Don't consider backend systems or backup processes
- Typical quote: "If I delete a photo from Google Photos, I expect it to be deleted from everywhere"

**Backend-Aware Model Characteristics:**
- Suspect data persists in some form after deletion
- Recognize backups and caching may retain data
- Often uncertain about specifics
- Typical quote: "I think Google still has the information even if I delete it"

**Expert-Identified Themes:**
1. **Backend**: Data may exist in multiple backend systems beyond user-visible storage
2. **Time**: Deletion may be immediate, delayed, or partial
3. **Backup**: Backup systems retain data on different schedules
4. **Derived Information**: Analytics, aggregations, and ML models trained on data persist
5. **Anonymization**: "Deleted" data may be retained in anonymized form
6. **Shared Copy**: Data shared with or by third parties may persist independently

**User Concerns:**
- Fear of data being used against them
- Desire for genuine control over personal information
- Frustration with lack of transparency
- Requests for clearer deletion status information

## Conclusion

The study demonstrates that users lack accurate mental models of data deletion, even when they are "Backend-Aware." The gap between user expectations and technical reality creates privacy risks (false confidence) and trust issues (unnecessary suspicion). 

The authors recommend that services:
1. Provide clearer feedback about what deletion actually accomplishes
2. Explain retention periods for backups and derived data
3. Give users meaningful choices about different levels of deletion
4. Help users understand the limitations of deletion for shared content

From a sustainability perspective, the findings suggest users may not understand that "deleted" data continues to consume storage and energy resources until truly purged.

## APA Citation

Murillo, A., Kramm, A., Schnorf, S., & De Luca, A. (2018). "If I press delete, it's gone" - User understanding of online data deletion and expiration. In *Fourteenth Symposium on Usable Privacy and Security (SOUPS 2018)* (pp. 329-339). USENIX Association.

## Discussion Questions

1. How might interface design better communicate the reality of data deletion without overwhelming users with technical details?

2. Should there be regulatory requirements for services to provide specific information about data deletion practices?

3. The study found technical background didn't clearly differentiate mental models. What factors do influence user understanding of deletion?

4. How do the two mental models (UI-Based vs. Backend-Aware) affect users' digital accumulation behaviors and sustainability impact?

5. What ethical obligations do services have to users who believe pressing "delete" genuinely removes their data?

## Connections

- **Digital hoarding research**: Users who don't believe deletion is real may accumulate more data, knowing they can always "delete" it later without consequence
- **Dark data problem**: Data that users think is deleted but persists in backends becomes dark data - stored but inaccessible to the user
- **Data center sustainability**: "Deleted" data that persists continues to consume storage and energy
- **Privacy regulation**: GDPR "right to erasure" raises questions about what deletion actually means legally and technically
- **Trust and transparency in HCI**: Broader theme of designing honest interfaces that don't mislead users about system behavior
