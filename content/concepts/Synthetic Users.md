---
type: concept
category: "Research Methodology"
aliases:
  - "Persona-Conditioned LLMs"
  - "GenAI Personas"
related_concepts:
  - "[[concepts/Interactive Virtual Personas]]"
tensions_with:
  - "[[concepts/Human-Centered Design]]"
---

# Synthetic Users

## Definition
LLM agents simulating human behavior through visual perception to assess usability as real users would experience, used as proxies for human participants in research contexts.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **[[concepts/Human-Centered Design]]**: Synthetic users raise fundamental questions about centering actual humans in design processes when AI proxies are used instead of real participants.
