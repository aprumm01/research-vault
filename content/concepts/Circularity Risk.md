---
type: concept
category: "Critical Perspectives"
aliases:
related_concepts:
  - "[[concepts/AI Hallucinations]]"
  - "[[concepts/Evaluative Judgment]]"
tensions_with:
  - "[[concepts/Human Evaluation]]"
  - "[[concepts/Independent Validation]]"
---

# Circularity Risk

## Definition
When the same generative AI model both generates and evaluates outputs, creating validation problems where AI effectively judges its own work, undermining quality assurance.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Human Evaluation**: Circularity risk highlights why human judgment remains essential for validating AI outputs.
- **Independent Validation**: Self-referential AI evaluation systems cannot provide the independent verification needed for quality assurance.
