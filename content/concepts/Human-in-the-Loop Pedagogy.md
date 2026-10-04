---
type: concept
category: "Pedagogical Approaches"
aliases:
  - "HITL Pedagogy"
  - "Human-in-the-Loop Learning"
related_concepts:
  - "[[concepts/Evaluative Judgment]]"
  - "[[concepts/Critical Thinking]]"
tensions_with:
  - "[[concepts/Cognitive Offloading]]"
  - "[[concepts/Metacognitive Laziness]]"
---

# Human-in-the-Loop Pedagogy

## Definition
The normative principle that students must maintain oversight, responsibility, and critical engagement with AI outputs—using AI as a scaffold for learning rather than outsourcing thinking.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Cognitive Offloading**: Human-in-the-loop pedagogy explicitly counters the tendency to offload cognitive work to AI, requiring students to remain actively engaged rather than passively accepting outputs.
- **Metacognitive Laziness**: Maintaining human oversight requires sustained metacognitive effort, which is undermined when students fail to reflect on their own understanding and the quality of AI assistance.
