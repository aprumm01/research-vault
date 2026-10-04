---
type: concept
category: "Human-AI Collaboration"
aliases:
  - "Confabulation"
  - "Hallucinations as Quality Challenge"
related_concepts:
  - "[[concepts/Evaluative Judgment]]"
  - "[[concepts/Complacency Risk]]"
tensions_with:
  - "[[concepts/AI Tool Dependence]]"
  - "[[concepts/Explainable AI]]"
---

# AI Hallucinations

## Definition
The tendency of large language models to produce confident but factually incorrect outputs, creating cognitive load for users who lack domain knowledge to identify errors.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **AI Tool Dependence**: Users dependent on AI tools may lack the expertise to detect hallucinated content
- **Explainable AI**: Explanations cannot reliably signal when outputs are hallucinated vs accurate
