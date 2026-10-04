---
type: concept
category: "Research Methodology"
aliases:
  - "IVPs"
  - "Over-Optimism Bias"
related_concepts:
  - "[[concepts/Synthetic Users]]"
tensions_with:
  - "[[concepts/AI Hallucinations]]"
  - "[[concepts/Circularity Risk]]"
---

# Interactive Virtual Personas

## Definition
LLM-powered conversational agents that designers can interview and gather feedback from in real-time, exhibiting over-optimism bias—providing overly positive feedback lacking critical perspectives.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **[[concepts/AI Hallucinations]]**: IVPs may generate fabricated or inaccurate feedback that doesn't reflect real user behavior or needs.
- **[[concepts/Circularity Risk]]**: Feedback from AI-generated personas may reinforce existing design assumptions rather than providing genuinely novel user perspectives.
