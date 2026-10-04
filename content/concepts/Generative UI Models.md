---
type: concept
category: "Human-AI Collaboration"
aliases:
  - "GenUI"
  - "Good First Draft Phenomenon"
related_concepts:
  - "[[concepts/Democratization of Design]]"
  - "[[concepts/Prompt Engineering]]"
tensions_with:
  - "[[concepts/Visual Homogenization]]"
  - "[[concepts/Ownership Ambiguity]]"
---

# Generative UI Models

## Definition
AI systems capable of creating high-fidelity UI screens from textual descriptions, exhibiting a 'good first draft, tough last mile' phenomenon—excelling at initial prototypes but requiring significant editing for production-ready standards.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Visual Homogenization**: Models trained on common patterns may produce aesthetically convergent outputs
- **Ownership Ambiguity**: Questions of authorship when AI generates substantial portions of UI designs
