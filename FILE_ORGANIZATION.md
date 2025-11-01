# File Organization for Claude Code

How to structure files so Claude Code can actually use them.

## The Problem

Bad organization = Claude can't find what it needs = hallucinated answers.
Good organization = Claude knows where to look = accurate, contextual help.

## Core Principle

**Optimize for discoverability, not aesthetics.**

Claude Code searches your files to build context. Make that search successful.

## Critical Rules

### Rule 1: Flat is Better Than Nested (Until It's Not)

**Bad:**
```
agents/
  backend/
    api/
      rest/
        auth/
          jwt/
            implement_jwt_auth.md
```

**Good:**
```
agents/
  implement_jwt_auth.md
  implement_oauth_flow.md
  implement_api_rate_limiting.md
```

**Why:** Claude searches by filename and content. Deep nesting hurts both.

**When to nest:** More than 20 files in a folder. Then group by clear categories.

### Rule 2: Names Should Be Searchable

**Bad:**
```
agent1.md
subagent_v2_final.md
new_skill.md
```

**Good:**
```
reduce_deployment_risk.md
accelerate_code_reviews.md
validate_database_migrations.md
```

**Why:** Claude searches filenames. "reduce deployment risk" finds the file. "agent1" finds nothing.

**Pattern:** `[verb]_[noun]_[specifics].md`
- reduce_deployment_risk.md
- challenge_technical_assumptions.md
- find_core_product_value.md

### Rule 3: README.md is Claude's Index

Every folder needs README.md with:
1. What this folder contains
2. When to use files in here
3. Catalog of files with one-line descriptions

**Why:** Claude reads README.md first to understand folder structure.

**Example:**
```markdown
# Agents

Complete, production-ready agents.

## Catalog

- `reduce_deployment_risk.md` - Pre-deployment risk analysis
- `accelerate_code_reviews.md` - Faster, thorough PR reviews
- `validate_migrations.md` - Database migration safety checks
```

### Rule 4: Keep Related Files Together

**Bad:**
```
agents/accelerate_code_reviews.md
skills/code_review_patterns.md
tools/run_code_review.sh
workflows/full_review_process.md
```

**Good:**
```
agents/
  accelerate_code_reviews/
    agent.md
    supporting_skills.md
    review_tool.sh
    workflow.md
```

**When:** A subagent/agent needs multiple supporting files.

**Why:** Claude needs context. Co-location = easier context loading.

### Rule 5: Use Consistent File Extensions

**Always:**
- `.md` for documentation/agents/subagents/skills
- `.sh` for bash scripts
- `.py` for Python tools
- `.js` for JavaScript tools

**Never:**
- `.txt` for anything (ambiguous)
- No extension (Claude can't infer type)
- Mixed extensions for same content type

### Rule 6: Cross-Reference Explicitly

**Bad:**
```markdown
Use the risk assessment subagent.
```

**Good:**
```markdown
Use the risk assessment subagent (see `subagents/reduce_deployment_risk.md`).
```

**Why:** Claude can follow explicit paths. Vague references = hallucination.

**Pattern:**
```markdown
See [subagent name](relative/path/to/file.md)
```

### Rule 7: Put Examples in Examples Folder

**Don't:**
```
agents/
  accelerate_code_reviews.md
  accelerate_code_reviews_example1.md
  accelerate_code_reviews_example2.md
```

**Do:**
```
agents/
  accelerate_code_reviews.md

examples/
  code_review_workflow/
    problem.md
    solution.md
    agents_used.md
```

**Why:** Separates "what" from "how I used it". Claude can pull examples when needed without cluttering agent definitions.

## Optimal Structure

```
repo/
├── README.md                 # Overview, philosophy, quick start
├── CONTRIBUTING.md           # Rules for adding new content
│
├── agents/                   # Complete solutions
│   ├── README.md            # Catalog with one-liners
│   ├── agent_name.md        # Simple agents (single file)
│   └── complex_agent/       # Complex agents (multiple files)
│       ├── agent.md
│       ├── supporting_skills.md
│       └── tools.sh
│
├── subagents/               # Reusable components
│   ├── README.md           # Template + catalog
│   ├── COLLABORATION.md    # How subagents work together
│   ├── COMMUNITIES.md      # Where to get help
│   ├── JARGON.md          # How to define terms
│   ├── job_name.md        # Simple subagents (single file)
│   └── examples/          # Reference implementations
│       └── example_subagent.md
│
├── skills/                 # Knowledge domains
│   ├── README.md          # Organization + catalog
│   ├── backend/
│   │   ├── README.md      # Backend skills catalog
│   │   └── skill_name.md
│   ├── frontend/
│   ├── data/
│   └── devops/
│
├── tools/                  # Executable utilities
│   ├── README.md          # Template + catalog
│   ├── tool_name.sh       # Bash scripts
│   ├── tool_name.py       # Python scripts
│   └── tool_name.js       # JavaScript scripts
│
├── workflows/              # Multi-step processes
│   ├── README.md          # Template + catalog
│   └── workflow_name.md
│
└── examples/               # Real usage
    ├── README.md          # Index of examples
    └── project_name/
        ├── problem.md
        ├── solution.md
        ├── agents_used.md
        └── learnings.md
```

## File Naming Patterns

### Agents
`[verb]_[noun]_[context].md`
- `reduce_deployment_risk.md`
- `accelerate_pr_reviews.md`
- `validate_database_migrations.md`

### Subagents (Jobs-to-be-Done)
`[job_outcome]_[context].md`
- `challenge_technical_assumptions.md`
- `find_core_value.md`
- `surface_hidden_costs.md`

### Skills
`[domain]_[specific_knowledge].md`
- `postgres_query_optimization.md`
- `react_performance_patterns.md`
- `kubernetes_scaling_strategies.md`

### Tools
`[action]_[target].[ext]`
- `deploy_to_staging.sh`
- `analyze_bundle_size.js`
- `backup_database.py`

### Workflows
`[process_name]_workflow.md`
- `feature_development_workflow.md`
- `incident_response_workflow.md`
- `code_review_workflow.md`

## What Claude Code Needs

### 1. Explicit File Paths
Claude can't guess. Be explicit.

**Bad:** "Use the deployment agent"
**Good:** "Use `agents/reduce_deployment_risk.md`"

### 2. Clear File Boundaries
One concept = one file (until it gets too big).

**When to split:**
- File > 500 lines
- Multiple distinct topics
- Hard to scan/search

**When to keep together:**
- Tightly coupled concepts
- Frequently used together
- Loses meaning when separated

### 3. Consistent Structure Within Files
Use the templates. Claude learns the structure.

**Every subagent file:**
1. Job to be done
2. Hiring moment
3. Input
4. Artifacts vs deliverables
5. Stakeholders
6. [Rest of template...]

**Why:** Claude can extract information from known locations.

### 4. Table of Contents for Long Files
For files > 200 lines, add TOC at top.

```markdown
# File Name

## Table of Contents
- [Section 1](#section-1)
- [Section 2](#section-2)
- [Section 3](#section-3)

## Section 1
...
```

**Why:** Claude can jump to relevant sections.

### 5. Catalog Files
README.md in each folder = catalog.

```markdown
## Catalog

- `file1.md` - One-line description
- `file2.md` - One-line description
- `file3.md` - One-line description
```

**Why:** Claude scans catalogs to find relevant files.

## Anti-Patterns

### ❌ Don't: Version in Filenames
```
subagent_v1.md
subagent_v2.md
subagent_final.md
subagent_final_v2.md
```

**Why:** Git handles versions. Filenames should be stable.

**Do:** Use git history. Keep one `subagent_name.md`.

### ❌ Don't: Date in Filenames
```
review_process_2025_01_15.md
review_process_2025_02_20.md
```

**Why:** Makes search worse. Use git history.

**Do:** `review_process.md` + git log for history.

### ❌ Don't: Generic Names
```
notes.md
temp.md
scratch.md
agent.md
```

**Why:** Claude can't distinguish them.

**Do:** Specific, searchable names.

### ❌ Don't: Deep Nesting Without Purpose
```
agents/
  production/
    backend/
      api/
        rest/
          endpoints/
            auth/
              agent.md
```

**Why:** Discoverability nightmare.

**Do:** Flatten. Nest only when it clarifies.

### ❌ Don't: Mix Concerns in One File
```
# Everything About Our System
- Agents
- Subagents  
- Tools
- Workflows
- Random notes
- Meeting notes
```

**Why:** Claude loads whole file for context. Bloated files = wasted context.

**Do:** One concern per file.

## Migration Strategy

If you have existing mess:

### Phase 1: Add Catalogs (1 hour)
Add README.md to each folder with file listings.

### Phase 2: Rename Critical Files (2 hours)
Find your 10 most-used files. Rename them properly.

### Phase 3: Flatten Unnecessary Nesting (2 hours)
Move files up if nesting doesn't clarify.

### Phase 4: Add Cross-References (1 hour)
Update files to link to each other explicitly.

### Phase 5: Delete Dead Files (30 min)
Anything unused in 6+ months. Git preserves history.

Don't do it all at once. Each phase adds value independently.

## Testing Your Organization

### Test 1: The Stranger Test
Could someone new find what they need in < 5 minutes?
- No = reorganize

### Test 2: The Search Test
Does searching for a concept find the right file?
- No = rename

### Test 3: The Context Test
Can Claude Code load relevant context for a query?
- No = improve cross-references or flatten structure

### Test 4: The Catalog Test
Do README.md files actually list what's in the folder?
- No = update catalogs

## Claude Code Specific Tips

### 1. Use .clinerules Files
Create `.clinerules` in your repo root:

```
# Claude Code Rules

## File Organization
- Agents in /agents
- Subagents in /subagents  
- Skills in /skills
- Tools in /tools
- Workflows in /workflows

## Always Check
- Read relevant README.md first
- Cross-reference using full paths
- Keep examples separate from definitions

## Naming
- Use jobs-to-be-done naming for subagents
- Use verb_noun for agents
- Keep filenames searchable
```

**Why:** Claude Code reads .clinerules automatically.

### 2. Add Context Files
Create `CONTEXT.md` in complex folders:

```markdown
# Context for This Folder

## What Lives Here
[Description]

## How These Files Relate
[Diagram or description]

## Common Workflows
1. Start with X
2. Then use Y
3. Finish with Z

## Watch Out For
[Common mistakes]
```

**Why:** Claude loads this for context about the folder.

### 3. Keep a PROJECT_MAP.md at Root
```markdown
# Project Map

## Structure
- `/agents` - Production-ready complete solutions
- `/subagents` - Composable components
- `/skills` - Domain knowledge
- `/tools` - Executables
- `/workflows` - Processes
- `/examples` - Real usage

## Finding Things
- Need complete solution? → `/agents`
- Need to build something? → `/subagents`
- Need domain expertise? → `/skills`
- Need to run something? → `/tools`
- Need a process? → `/workflows`
- Need to see how? → `/examples`
```

**Why:** Claude Code uses this as a map.

## Your Challenge

Run these checks on your repo:

1. **Filename test**: Are all files searchable by their purpose?
2. **README test**: Does every folder have a current catalog?
3. **Depth test**: Any files nested > 3 levels without good reason?
4. **Cross-reference test**: Do files link explicitly to related files?
5. **Dead file test**: Anything unused > 6 months that should be deleted?

Fix the worst offender first. Don't refactor everything at once.

What's the biggest file organization problem in your current setup?
