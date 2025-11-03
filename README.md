# Claude Code Agents
*Enhanced with MPD2 Design Decision Methodologies*

A comprehensive design decision system that integrates Master of Product Design & Development (MPD2) academic frameworks with practical agents, tools, skills and workflows for Claude Code.

## Philosophy

- **Ship within a year**: No agent takes more than a year to ROI
- **Follow your doubt**: If it feels wrong, it probably is
- **Prototype the hard thing**: Test the differentiation early
- **Think slow, act fast**: Deep understanding, rapid execution
- **Academic rigor, practical application**: MPD2 frameworks enhance decisions without slowing execution
- **Enhancement over replacement**: Build upon existing capabilities rather than starting from scratch

## Structure

### Core System (Enhanced with MPD2)
```
design-system/      # MPD2 primitives (schemas, calculators, generators)
workflows/          # MPD2 enhanced processes
agents/             # Strategic, evaluator, and communicator agents
skills/             # Multi-agent orchestration capabilities
orchestration/      # Project-level coordination
```

### Supporting Infrastructure
```
subagents/          # Reusable agent components
tools/              # Executable utilities
templates/          # MPD2 project templates
examples/           # Real usage patterns including MPD2 applications
scripts/            # System health and monitoring
```

### MPD2 Integration
The system now includes systematic application of:
- **Knowledge Funnel**: Mystery → Heuristic → Algorithm progression
- **Three Horizons**: Portfolio balance across core, adjacent, and transformational opportunities
- **Stage-Gate**: Systematic development with decision rigor
- **Exploration-Exploitation**: Optimal balance based on uncertainty levels

See [FILE_ORGANIZATION.md](FILE_ORGANIZATION.md) for detailed file organization best practices optimized for Claude Code.

## Standard `.claude/` Directory Structure

**For other Claude agent repositories:** This project uses a specialized MPD2-enhanced structure, but we recommend a simpler `.claude/` convention for general-purpose agent repositories:

### Recommended Layout
```
.claude/
├── agents/          # Main, runnable agent files
├── subagents/       # Smaller, specialized agents used by other agents
├── skills/          # Reusable prompt snippets, patterns, playbooks
├── workflows/       # Checklists/processes (e.g., Baby Steps, TDD runs)
├── tools/           # Tool specs/configs (if any)
├── scripts/         # Helper shell/python scripts agents/workflows call
└── examples/        # Worked examples, references
```

### Minimal Frontmatter Examples

**Agent** (`.claude/agents/accessibility-first-ios-developer.md`):
```markdown
---
name: Accessibility-First iOS Developer
description: Builds iOS features with WCAG/ADA alignment.
model: claude-3.5-sonnet
---

See also: ./../skills/swiftui_performance_patterns.md, ./../workflows/baby-steps-tdd.md
```

**Subagent** (`.claude/subagents/translate_english_to_asl_style.md`):
```markdown
---
name: ASL Style Translator
kind: subagent
---

Guidelines...
```

**Skill** (`.claude/skills/emergency_alert_protocols.md`):
```markdown
---
name: Emergency Alert Protocols
kind: skill
---

Reusable rules...
```

**Workflow** (`.claude/workflows/baby-steps-tdd.md`):
```markdown
---
name: Baby Steps TDD
kind: workflow
---

1) Small change → 2) Build/test → 3) Document...
```

### Migration from `.claude-agents/`

Quick migration script (zsh):
```bash
mkdir -p .claude/{agents,subagents,skills,workflows,tools,scripts,examples}
[[ -d .claude-agents/agents ]] && mv .claude-agents/agents/* .claude/agents/ 2>/dev/null
[[ -d .claude-agents/subagents ]] && mv .claude-agents/subagents/* .claude/subagents/ 2>/dev/null
[[ -d .claude-agents/skills ]] && mv .claude-agents/skills/* .claude/skills/ 2>/dev/null
[[ -d .claude-agents/workflows ]] && mv .claude-agents/workflows/* .claude/workflows/ 2>/dev/null
[[ -d .claude-agents/examples ]] && mv .claude-agents/examples/* .claude/examples/ 2>/dev/null
```

### Documentation Tips
- In each agent, use relative links to `skills/`, `subagents/`, and `workflows/`
- Add a section in `CLAUDE.md` listing the structure and purpose of each folder
- Keep frontmatter minimal but consistent across similar file types

### Validation
```gherkin
Scenario: Project agent assets are correctly organized
  Given the repository contains Claude agents and related assets
  When I inspect the `.claude/` directory
  Then all runnable agents are under `.claude/agents/`
  And specialized helpers are under `.claude/subagents/`
  And reusable prompts are under `.claude/skills/`
  And process playbooks are under `.claude/workflows/`
  And no agent assets remain under `.claude-agents/`
```

## Quick Start

### For Immediate Use
1. Browse `agents/` for complete solutions
2. Check `examples/mpd2/` for MPD2 applications
3. Use `design-system/primitives/calculators/` for quick assessments

### For Complex Problems
1. Start with `skills/` for multi-agent coordination
2. Apply `orchestration/` for complete project management
3. Reference `INTEGRATION_MAP.md` for system overview

### For Custom Solutions
1. Mix from `subagents/` and existing `skills/` 
2. Enhance with MPD2 frameworks from `design-system/`
3. Add to `workflows/` when you find repeating patterns

## Contributing to Yourself

When you save something here, answer:
- What problem did this solve?
- What did you learn that wasn't obvious?
- What would you do differently next time?
- How does MPD2 methodology enhance the solution?

## MPD2 Features

### Academic Rigor with Practical Application
- **Evidence-based decision making** with confidence intervals
- **Systematic frameworks** for complex problem solving
- **Learning capture** for organizational capability building
- **Cross-validation** across multiple evaluation methodologies

### Complete System Integration
- **Backward compatibility** - All existing components remain functional
- **Progressive enhancement** - Adopt complexity as needed
- **Clear migration path** - From simple tools to complex orchestration
- **Quality assurance** - System health monitoring and validation

## Index

See individual folders for catalogs, with special attention to:
- `INTEGRATION_MAP.md` - MPD2 integration overview
- `examples/mpd2/` - Real MPD2 applications
- `scripts/system_health_check.sh` - Complete system validation
