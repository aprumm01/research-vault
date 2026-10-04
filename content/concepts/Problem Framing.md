---
type: concept
category: "Cognitive Processes"
aliases:
related_concepts:
  - "[[concepts/Wicked Problems]]"
  - "[[concepts/Epistemic Confinement]]"
tensions_with:
  - "[[concepts/Epistemic Confinement]]"
---

# Problem Framing

## Definition
Constructing tractable design problems from open-ended tasks, a critical cognitive skill that shapes the solution space and determines what possibilities are considered.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Epistemic Confinement**: AI systems may constrain problem framing by limiting exploration to domains within their training data, narrowing the frame before human judgment can expand it
