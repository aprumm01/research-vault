---
type: concept
category: "Human-AI Collaboration"
aliases: []
related_concepts:
  - "[[concepts/Human-AI Co-creation]]"
  - "[[concepts/Hybrid Intelligence]]"
tensions_with:
  - "[[concepts/AI Tool Dependence]]"
  - "[[concepts/Epistemic Substitution]]"
  - "[[concepts/De-skilling]]"
---

# AI Augmentation

## Definition
Using AI to enhance human capabilities through real-time insights and decision support rather than replacement, positioning AI as extending rather than substituting human cognitive abilities.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **AI Tool Dependence**: Augmentation may gradually shift to dependence if humans lose underlying skills
- **Epistemic Substitution**: Risk of AI insights replacing rather than informing human judgment
- **De-skilling**: Extended augmentation may atrophy the very capabilities being enhanced
