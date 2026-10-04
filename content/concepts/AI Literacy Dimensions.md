---
type: concept
category: "Pedagogical Approaches"
aliases:
  - "AI Literacy"
  - "AI Competencies"
related_concepts:
  - "[[concepts/Prompt Engineering]]"
  - "[[concepts/Evaluative Judgment]]"
tensions_with:
  - "[[concepts/Metacognitive Laziness]]"
  - "[[concepts/AI Overreliance]]"
---

# AI Literacy Dimensions

## Definition
A multi-dimensional framework encompassing Technical Understanding (data-driven aspects), Critical Appraisal (ethical evaluation), and Practical Application (appropriate AI usage).

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Metacognitive Laziness**: AI literacy requires active critical engagement with AI systems, which is undermined when learners fail to monitor their own thinking processes during AI interactions.
- **AI Overreliance**: Developing robust AI literacy stands in tension with tendencies to trust AI outputs uncritically, bypassing the critical appraisal dimension entirely.
