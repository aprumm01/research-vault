---
type: concept
category: "Pedagogical Approaches"
aliases:
  - "DBL"
related_concepts:
  - "[[concepts/Studio Pedagogy]]"
  - "[[concepts/Deep Learning (Educational)]]"
tensions_with:
  - "[[concepts/Cognitive Offloading]]"
  - "[[concepts/Surface-Level Processing]]"
---

# Design-Based Learning

## Definition
A learning model emphasizing scientific knowledge and professional skills acquisition through designing projects in real-life situations, engaging students in active cognitive processing.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Cognitive Offloading**: Design-based learning requires active cognitive engagement, which can be undermined when students offload thinking to AI tools rather than working through design challenges themselves.
- **Surface-Level Processing**: The deep engagement required in design projects stands in tension with superficial approaches that skip iterative refinement and critical analysis.
