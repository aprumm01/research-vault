---
type: index
---

# Concepts

This folder contains the controlled vocabulary of concepts used for relationship metadata in the research vault. Each concept node can be linked from papers using `builds_on`, `supports`, `critiques`, or `tensions_with` frontmatter fields.

## Categories

### Cognitive Processes (18 concepts)
Mental processes, thinking, memory, attention, and reasoning patterns.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Cognitive Processes"
SORT file.name ASC
```

### Pedagogical Approaches (12 concepts)
Teaching methods, learning approaches, and educational strategies.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Pedagogical Approaches"
SORT file.name ASC
```

### Human-AI Collaboration (11 concepts)
Frameworks and patterns for how humans and AI work together.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Human-AI Collaboration"
SORT file.name ASC
```

### Educational Outcomes (10 concepts)
Results and effects of AI use in educational contexts.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Educational Outcomes"
SORT file.name ASC
```

### Critical Perspectives (11 concepts)
Critical theory, sociological, and ethical perspectives on AI.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Critical Perspectives"
SORT file.name ASC
```

### Research Methodology (4 concepts)
Research methods and methodological concepts.

```dataview
TABLE category, length(aliases) as Aliases
FROM "concepts"
WHERE category = "Research Methodology"
SORT file.name ASC
```

## All Concepts

```dataview
TABLE category, length(related_concepts) as "Related", length(tensions_with) as "Tensions"
FROM "concepts"
WHERE type = "concept"
SORT category ASC, file.name ASC
```

## Usage

Link to concepts from paper frontmatter:

```yaml
builds_on:
  - "[[concepts/Cognitive Load Theory]]"
  - "[[concepts/Scaffolding]]"
  
supports:
  - "[[concepts/Cognitive Offloading]]"
  
critiques:
  - "[[concepts/AI as neutral tool]]"
  
tensions_with:
  - "[[concepts/Behaviorism]]"
```

---

*Generated: 2026-10-02*
*Total concepts: 64*
