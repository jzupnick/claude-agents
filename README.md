# agent-skills

525 modular skills for Claude Code, organized into 10 focused plugins.

## Plugins

| Plugin | Count | Domain | Example |
|--------|-------|--------|---------|
| **code** | 211 | Frontend, backend, mobile, security, DevOps | `/code:react`, `/code:api-architect` |
| **ops** | 80 | Strategy, communications, finance, leadership | `/ops:decision-memo`, `/ops:negotiate` |
| **data** | 48 | Analytics, visualization, pipelines | `/data:analyst`, `/data:viz-dashboard` |
| **write** | 41 | Writing, editing, translation | `/write:blog`, `/write:technical` |
| **ai** | 30 | AI/ML, LLMs, computer vision | `/ai:prompt-engineer`, `/ai:rag-architect` |
| **research** | 28 | Analysis, diagnostics, evaluation | `/research:market`, `/research:risk` |
| **design** | 27 | Product design, UX, design systems | `/design:architect`, `/design:human-factors` |
| **tools** | 24 | iOS, hardware, doc formats, utilities | `/tools:pdf`, `/tools:ios-simulator` |
| **infra** | 18 | Cloud, networking, containers | `/infra:kubernetes`, `/infra:homelab` |
| **product** | 18 | Product management, discovery, MPD2 | `/product:brainstorm`, `/product:stage-gates` |

## Installation

### Option A: Shell wrapper (recommended)

Add to `~/.zshrc`:

```bash
cc-skills() {
  local plugins=()
  for d in ~/Projects/agent-skills/*/; do
    [[ -f "$d/.claude-plugin/plugin.json" ]] && plugins+=(--plugin-dir "$d")
  done
  claude "${plugins[@]}" "$@"
}
```

Then run `cc-skills` instead of `claude`.

### Option B: Registered plugins

Each plugin is registered in `~/.claude/plugins/installed_plugins.json` as `<name>@local` and enabled in `~/.claude/settings.json`.

## Structure

```
agent-skills/
├── code/                    # Each plugin is self-contained
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── AGENTS.md            # Skill catalog for this plugin
│   └── skills/
│       ├── react/SKILL.md
│       ├── api-architect/SKILL.md
│       └── ...
├── ai/
├── data/
├── ops/
├── write/
├── design/
├── research/
├── infra/
├── product/
├── tools/
├── CLAUDE.md
└── scripts/
```

## SKILL.md Format

```yaml
---
name: skill-name
description: When to invoke this skill (trigger phrases)
---

# Skill Title

Instructions for Claude when this skill is activated.
```

## Sources

- **58 hand-crafted skills** from [ai-config-hub](~/Projects/ai-config-hub/claude/) (agents, subagents, commands, workflows)
- **277 expert assistant skills** from Cherry Studio collection
- **190 subscription assistant skills** from LiteLLM collection (deduplicated)
