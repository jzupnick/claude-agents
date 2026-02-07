---
name: mpd-refine-notes
description: "Use when refining Northwestern MPD2 course notes into structured knowledge, searching academic content, or building learning references in Obsidian"
---

# Refine MPD Notes

Convert academic MPD (Master of Product Design) coursework notes into professional AI knowledge base entries using The Refiner methodology. Pair the mpd-knowledge MCP server (15,000+ embedded academic chunks) with structured transformation to produce polished professional reference material.

## When to Use

- Converting lecture notes from MPD coursework into permanent professional references
- Building a searchable, AI-ready knowledge base from academic materials
- Extracting practical frameworks (JTBD, Business Model Canvas, Stage-Gate, etc.) from academic context
- Creating Obsidian notes that link into a professional knowledge graph

## Workflow

1. Search MPD notes: `search_mpd("topic")` via mpd-knowledge MCP
2. Apply The Refiner transformation to results
3. Save to Obsidian: `Archive/mpd/Refined/[NoteName].md`

## The Refiner Transformation

### 1. Sanitize
Remove all academic "noise":
- References to "Homework", "Syllabus", "Professor", "Grade", "Due Date"
- Course numbers and assignment identifiers
- Academic formatting artifacts

### 2. Professional Formatting
Restructure using clear Markdown headers:
- `## Concept` -- Core definition
- `## Methodology` -- How to apply
- `## Industrial Application` -- Real-world context
- `## Professional Impact` -- The "so what?"

### 3. AI-Ready Definitions
Ensure technical terms are explicitly defined for LLM retrieval:
- C_pk (Process Capability Index)
- Stage-Gate (Product development methodology)
- Ethnographic Research (User research method)
- JTBD (Jobs-to-be-Done framework)

### 4. Professional Impact Section
Always add a concluding section explaining:
- How this concept applies to real corporate product development
- Actionable next steps
- Links to related concepts in the knowledge graph

## Output Template

```markdown
---
tags:
  - learning
  - mpd
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: reference
status: active
source: MPD Coursework
course: [Course Name]
original_location: Archive/mpd/[path]
---

# [Concept Name]

Brief description of the concept and its professional relevance.

## Concept
[Clear, jargon-free definition]

## Methodology
[Step-by-step application guide]

## Industrial Application
[Real-world examples and use cases]

## Professional Impact
[Why this matters in corporate product development]

---

**Related:**
- [[Learning MOC]]
- [[MPD Frameworks Index]]
- [[Related Concept 1]]
- [[Related Concept 2]]
```

## Required MPD Frontmatter Fields

| Field | Purpose | Example |
|-------|---------|---------|
| `tags: [learning, mpd]` | Makes note findable via #mpd tag | Required |
| `source: MPD Coursework` | Identifies origin | Static value |
| `course:` | Specific course name | "Financial Analysis" |
| `original_location:` | Path to raw academic source | "Archive/mpd/Courses/..." |

## Storage Location

### Primary: Archive (for mpd-knowledge indexing)
Save to `Archive/mpd/Refined/[NoteName].md`

This ensures:
- mpd-knowledge MCP indexes refined content on next embed cycle
- `search_mpd()` returns both raw AND refined notes
- All MPD content stays in one searchable location

### Optional: Vault Root Reference
For frequently-used frameworks, create a lightweight reference note in vault root using Obsidian embed syntax to pull in full refined content.

## Key Rules

| Rule | Why |
|------|-----|
| Always save to `Archive/mpd/Refined/` | Gets indexed by mpd-knowledge |
| Use `#mpd` tag | Findable via Obsidian tag search |
| Include `original_location` frontmatter | Links refined to raw content |

## Search Methods

| What You Want | How to Find It |
|---------------|----------------|
| Raw academic content | `search_mpd("topic")` via mpd-knowledge MCP |
| All refined MPD notes | Obsidian tag search: `tag:#mpd` |
| MPD notes by course | Dataview: `WHERE course = "Course Name"` |
| Link raw to refined | Check `original_location` frontmatter field |

## Integration with Knowledge Graph

After refining:
1. Add `[[Internal Links]]` to existing concepts in the vault
2. Include `[[Learning MOC]]` in the Related section
3. Use bidirectional linking (note to MOC)
4. Consider adding to Navigation if it is a major framework
5. Always tag with `#mpd` so Dataview and search can aggregate all MPD content

## Tips

- Start broad, then narrow: Search for topics first, then specific frameworks
- Cross-reference courses: Many concepts appear in multiple courses with different angles
- Build incrementally: Refine 2-3 notes per session, let the knowledge graph grow organically
- Link aggressively: The more internal links, the more valuable the knowledge graph becomes
- Tags over folders: Use `learning` + `reference` tags, not nested folder paths
- Always include frontmatter: Every note needs `tags` and `created` fields minimum
