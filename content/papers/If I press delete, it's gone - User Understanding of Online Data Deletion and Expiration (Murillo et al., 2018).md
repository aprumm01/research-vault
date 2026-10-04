---
title: "If I press delete, it's gone - User Understanding of Online Data Deletion and Expiration"
source_file: "/Users/I548005/Library/CloudStorage/OneDrive-SAPSE/Documents/Adam's stuff/0-School/i609/i609 Articles/soups2018-murillo.pdf"
type: paper
authors:
  - Ambar Murillo
  - Andreas Kramm
  - Sebastian Schnorf
  - Alexander De Luca
year: 2018
venue: "SOUPS 2018 (Fourteenth Symposium on Usable Privacy and Security)"
builds_on:
  - "[[Mental Models of Security]]"
  - "[[Privacy Decision Making]]"
supports:
  - "[[User-Centered Privacy Design]]"
  - "[[Transparency in Data Processing]]"
critiques:
  - "[[Generic Expiration Periods]]"
tensions_with:
  - "[[Automated Data Retention Policies]]"
key_claims:
  - Users hold two distinct mental models of deletion - UI-Based (deletion ends at the interface) and Backend-Aware (understanding that servers/cloud are involved)
  - Data expiration preferences are context-dependent rather than chronological
  - Generic expiration periods are ineffective; users prefer controllable expiration mechanisms
  - Users cannot generalize deletion needs across different services
methodology: "Semi-structured interviews with think-aloud drawing tasks, expert focus groups, inductive coding analysis"
study_type: qualitative
context: "Email and social media deletion scenarios with 22 interview participants and 7 expert focus group participants"
---

## Summary

This paper investigates how users understand online data deletion, retention, and expiration through an interview study with 22 participants and two focus groups with 7 data deletion experts. The researchers used think-aloud drawing tasks to uncover mental models of deletion processes. The study found that users fall into two categories of understanding: **UI-Based** (4 participants) who believe deletion is complete when they press delete, and **Backend-Aware** (18 participants) who recognize that servers, databases, and cloud systems are involved in the deletion process, though their understanding of these backend components varies in complexity.

Key findings include that reasons for deletion are highly service-dependent (email vs. social media have different motivations), data expiration is context-dependent rather than following a chronological timeline, and users prefer having control over expiration rather than automatic time-based deletion. The study also identified six topics experts believe users should understand: backend processes, time delays, backups, derived information, anonymization, and shared copies.

## Key Concepts

- **UI-Based Understanding**: Mental model where users believe deletion is instantaneous and complete upon pressing the delete button - "If I press delete, it's gone, not anymore inside, that's what I understand"
- **Backend-Aware Understanding**: Mental model acknowledging that deletion involves servers, databases, and cloud infrastructure, though with varying levels of sophistication
- **Deletion Finality**: User beliefs about whether data is truly gone after deletion - some believe data is retained, others believe it remains in other places (e.g., with recipients), and some understand deletion is not entirely possible
- **Data Expiration**: Automatic deletion of data after certain conditions are met (e.g., Snapchat's disappearing messages)
- **Context-Dependent Usefulness**: The value of data to service providers changes based on specific events rather than linear time progression

## Key Findings

1. **Two Mental Models of Deletion**: UI-Based (4/22 participants) vs. Backend-Aware (18/22 participants)

2. **Five Main Reasons for Deletion**:
   - Data no longer needed/outdated (16 participants)
   - Limited storage space (10 participants, email only)
   - Tidying inbox/avoiding cognitive overload (7 participants)
   - Removing spam/ads (6 participants, email)
   - Removing potentially embarrassing content (4 participants, social media)

3. **Privacy Concerns**: 13 participants expressed concerns about not knowing if data is really gone; 10 participants mentioned privacy concerns specifically for social media

4. **Data Storage Awareness**: 31 participants understood data is stored on servers/databases/cloud/internet; participants often used "server" and "cloud" interchangeably

5. **Expiration Preferences**: Participants favored control over automatic expiration; they wanted self-selected expiration conditions (e.g., "move email to folder that auto-deletes after 30 days")

6. **Expert-User Knowledge Gap**: Experts identified 6 key topics users should know (Backend, Time, Backup, Derived Information, Anonymization, Shared Copy), but only 18/22 participants were aware of backend issues and 16/22 aware of time delays; very few understood backup (7/22), derived information (1/22), or anonymization (1/22)

7. **No One-Size-Fits-All Solution**: Deletion needs and understanding differ significantly across services (email vs. social media)

## Relevance to Sustainable Computing

This research has indirect but important implications for sustainable computing:

- **Data Minimization**: Understanding user mental models of deletion can inform better data lifecycle management, reducing unnecessary data storage and associated energy consumption
- **Storage Efficiency**: Users who don't delete data due to unlimited storage contribute to ever-growing data centers; better deletion interfaces could encourage more active data management
- **Retention Policies**: Designing user-controllable expiration mechanisms could help reduce long-term data storage burdens while respecting user autonomy
- **Transparency**: Educating users about backend processes (backups, derived data) could influence more sustainable data practices and reduce redundant data accumulation
- **Design Implications**: The finding that users prefer UI metaphors (like "trash can") for understanding technical concepts suggests that sustainable computing practices could be communicated through familiar interaction patterns

## Citation

Murillo, A., Kramm, A., Schnorf, S., & De Luca, A. (2018). "If I press delete, it's gone" - User understanding of online data deletion and expiration. In *Proceedings of the Fourteenth Symposium on Usable Privacy and Security (SOUPS 2018)* (pp. 329-339). USENIX Association.
