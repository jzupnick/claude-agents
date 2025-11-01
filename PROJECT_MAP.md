# Project Map

Quick navigation for Claude Code and humans.

## Structure

```
claude-agents/
├── .clinerules              # Claude Code behavior rules
├── README.md                # Overview and philosophy
├── CONTRIBUTING.md          # Rules for adding content
├── FILE_ORGANIZATION.md     # How to organize files for Claude Code
├── PROJECT_MAP.md          # This file - quick navigation
├── INTEGRATION_MAP.md      # MPD2 integration strategy
│
├── design-system/          # MPD2 enhanced primitives
│   └── primitives/
│       ├── schemas/        # YAML data structures
│       ├── calculators/    # MPD2 scoring algorithms
│       └── generators/     # Analysis and decision support tools
│
├── agents/                  # Complete solutions
│   ├── README.md           # Template + catalog
│   ├── strategist/         # MPD2 strategic agents
│   ├── evaluator/          # Systematic evaluation agents
│   └── communicator/       # Decision support and briefing agents
│
├── subagents/              # Composable components
│   ├── README.md          # Template + catalog
│   ├── COLLABORATION.md   # How subagents work together
│   ├── COMMUNITIES.md     # Where to get help
│   ├── JARGON.md         # How to define terms
│   ├── AUTONOMOUS.md     # Making subagents self-running
│   └── examples/         # Reference implementations
│
├── skills/                 # Domain knowledge and orchestration
│   ├── README.md          # Organization guide
│   ├── mpd2-strategy/    # Portfolio optimization skills
│   ├── concept-development/      # Idea-to-prototype skills
│   ├── decision-making/          # Trade-off analysis skills
│   ├── backend/
│   ├── frontend/
│   └── [other domains]/
│
├── workflows/              # MPD2 enhanced processes
│   ├── README.md          # Template + catalog
│   ├── evaluation/        # Enhanced evaluation workflows
│   └── research/          # Strategic research workflows
│
├── orchestration/          # Project-level coordination
│   ├── README.md          # Project orchestration overview
│   ├── innovation-projects/     # Portfolio management orchestrators
│   └── product-development/     # Systematic development orchestrators
│
├── tools/                  # Executable utilities
│   └── README.md          # Template + catalog
│
├── templates/              # MPD2 project templates
│   └── mpd2-project-template.yaml
│
├── scripts/                # Management and monitoring
│   ├── README.md          # Script documentation
│   ├── system_health_check.sh   # Complete system validation
│   ├── check_subagent_tools.sh  # Verify CLI tools
│   ├── check_model_currency.sh  # Check LLM relevance
│   └── model_registry.json      # Model tracking
│
└── examples/               # Real usage and MPD2 applications
    ├── README.md          # Index of examples
    └── mpd2/ # MPD2 integration examples
```

## Finding Things

### "I need to solve a complete problem"
→ `/agents/README.md` - Check the catalog for existing solutions
→ `/orchestration/README.md` - For complex, multi-phase projects

### "I need MPD2 methodology application"
→ `/design-system/primitives/` - Core calculators and frameworks
→ `/skills/mpd2-strategy/` - Portfolio optimization
→ `/skills/concept-development/` - Systematic development
→ `/skills/decision-making/` - Trade-off analysis

### "I need to build something custom"
→ `/subagents/README.md` - Find composable pieces
→ `/subagents/COLLABORATION.md` - See how they work together

### "I need domain expertise"
→ `/skills/README.md` - Find the right domain folder

### "I need to run something"
→ `/tools/README.md` - Check available utilities

### "I need a systematic process"
→ `/workflows/README.md` - Find MPD2 enhanced workflows
→ `/workflows/evaluation/` - Stage-gate and evaluation processes

### "I want to see how it works in practice"
→ `/examples/README.md` - Browse real usage patterns
→ `/examples/mpd2/` - MPD2 methodology applications

### "I'm stuck and need help"
→ `/subagents/COMMUNITIES.md` - Find where experts hang out

### "I don't understand the terminology"
→ Look for "Jargon Glossary" section in relevant files
→ `/subagents/JARGON.md` - How to define terms

### "I'm organizing new files"
→ `/FILE_ORGANIZATION.md` - Best practices for Claude Code
→ `/.clinerules` - Rules Claude Code follows

## Navigation Pattern

1. Start with the appropriate README.md
2. Find the relevant file from the catalog  
3. Read that file
4. Follow cross-references to related files
5. Check examples for real usage

### MPD2 Navigation
For systematic methodology application:
1. Start with `/INTEGRATION_MAP.md` for overview
2. Use `/design-system/primitives/` for basic scoring and analysis
3. Apply `/skills/` for multi-agent coordination
4. Scale to `/orchestration/` for complete project management
5. Reference `/examples/mpd2/` for real applications

## Conventions

### File Naming
- Agents: `[verb]_[noun]_[context].md`
- Subagents: `[job_outcome]_[context].md`
- Skills: `[domain]_[specific_knowledge].md`
- Tools: `[action]_[target].[ext]`
- Workflows: `[process_name]_workflow.md`

### Cross-References
Always use explicit paths:
```markdown
See [description](relative/path/to/file.md)
```

### Catalogs
Every folder has a README.md with a catalog of its files.

## Quick Reference

### Adding New Content
1. Check if it already exists
2. Determine which folder it belongs in
3. Use the template from that folder's README.md
4. Update the catalog in README.md
5. Add cross-references where relevant

### Finding Related Files
1. Read the file's "Collaborates With" section
2. Check the "Example Integration" section
3. Look in `/examples` for real usage

### Understanding Subagent Relationships
1. Check "Upstream" (what it depends on)
2. Check "Downstream" (what depends on it)
3. Check "Parallel" (what runs alongside)
4. Check "Conflicts" (what it can't run with)

## Common Queries

**Q: Where do I put a new agent?**
A: `/agents/` if it's complete, or `/subagents/` if it's composable

**Q: How do I know if something is an agent vs subagent?**
A: Agent = run this to solve problem. Subagent = compose these to build solution.

**Q: Where do examples go?**
A: `/examples/project-name/` with problem.md, solution.md, agents_used.md, learnings.md

**Q: Can I nest folders deeper?**
A: Only if you have 20+ files and nesting adds clarity. Otherwise keep flat.

**Q: How do I reference other files?**
A: Always use explicit paths: `subagents/file_name.md`

**Q: What if a file doesn't fit the templates?**
A: Use the closest template and adapt. Update the template if you find a pattern.

## Philosophy Reminders

- **Think slow, act fast**: Plan the structure, then execute quickly
- **Follow your doubt**: If organization feels wrong, it probably is
- **Prototype the hard thing**: Test the structure with real usage
- **Delete, don't archive**: Git preserves history

## For Claude Code

When processing queries:
1. Read relevant README.md first
2. Load catalog to find specific files
3. Follow explicit cross-references
4. Check examples for real usage patterns
5. Consult .clinerules for repo conventions
