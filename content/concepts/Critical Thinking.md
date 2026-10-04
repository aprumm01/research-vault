---
type: concept
category: "Cognitive Processes"
aliases:
related_concepts:
  - "[[concepts/Higher-Order Thinking]]"
  - "[[concepts/Evaluative Judgment]]"
tensions_with:
  - "[[concepts/Cognitive Offloading]]"
  - "[[concepts/AI Tool Dependence]]"
  - "[[concepts/Metacognitive Laziness]]"
---

# Critical Thinking

## Definition
The ability to analyze, evaluate, and synthesize information to make reasoned decisions. This cognitive capacity is potentially impaired by AI tool dependence when users habitually delegate analytical tasks to AI systems.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Cognitive Offloading**: Externalizing analytical tasks can atrophy critical thinking skills
- **AI Tool Dependence**: Heavy reliance on AI reduces opportunities to practice critical analysis
- **Metacognitive Laziness**: Avoiding deliberate cognitive effort undermines critical thinking development
