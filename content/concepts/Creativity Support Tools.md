---
type: concept
category: "Human-AI Collaboration"
aliases:
  - "CSTs"
related_concepts:
  - "[[concepts/Divergent Thinking]]"
  - "[[concepts/Convergent Thinking]]"
tensions_with:
  - "[[concepts/Design Fixation]]"
---

# Creativity Support Tools

## Definition
Digital tools designed to support creative work that predominantly support divergent thinking while neglecting convergent thinking—helping generate ideas but providing less support for narrowing to viable solutions.

## Key Papers
```dataview
LIST
FROM "papers"
WHERE contains(builds_on, this.file.link) OR contains(supports, this.file.link) OR contains(critiques, this.file.link)
SORT file.name ASC
```

## Tensions
- **Design Fixation**: Tools that generate many options may paradoxically anchor users to early suggestions rather than supporting genuine divergence
