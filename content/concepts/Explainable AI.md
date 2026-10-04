---
type: concept
category: "Human-AI Collaboration"
aliases:
  - "XAI"
related_concepts:
  - "[[concepts/Human-in-the-Loop Pedagogy]]"
  - "[[concepts/AI Literacy Dimensions]]"
tensions_with:
  - "[[concepts/AI Hallucinations]]"
---

# Explainable AI

## Definition
Transparency mechanisms making black box decisions interpretable through tools like SHAP and LIME. Essential for building operator trust and enabling human override.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **AI Hallucinations**: Explanations may themselves be confabulated, providing false confidence in incorrect outputs
