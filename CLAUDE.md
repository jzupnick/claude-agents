# Agent Skills

525 skills organized into 10 focused plugins. Each plugin is a self-contained Claude Code plugin with its own `.claude-plugin/plugin.json`.

## Plugins

| Plugin | Skills | Invoke as | Domain |
|--------|--------|-----------|--------|
| **code** | 211 | `/code:<skill>` | Software development, frontend, backend, mobile, security, DevOps |
| **ops** | 80 | `/ops:<skill>` | Business strategy, communications, finance, leadership |
| **data** | 48 | `/data:<skill>` | Data engineering, analytics, visualization |
| **write** | 41 | `/write:<skill>` | Writing, editing, translation, content |
| **ai** | 30 | `/ai:<skill>` | AI/ML, LLMs, computer vision |
| **research** | 28 | `/research:<skill>` | Analysis, diagnostics, evaluation |
| **design** | 27 | `/design:<skill>` | Product design, UX, design systems |
| **tools** | 24 | `/tools:<skill>` | iOS, hardware, doc formats, utilities |
| **infra** | 18 | `/infra:<skill>` | Cloud, networking, containers, platforms |
| **product** | 18 | `/product:<skill>` | Product management, discovery, MPD2 frameworks |

## Auto-Invocation

Skills are automatically available as slash commands. Claude should proactively suggest relevant skills when the user's task matches a skill's description. For example:

- User asks about API design → suggest `/code:api-architect`
- User needs a decision framework → suggest `/ops:decision-memo`
- User wants to brainstorm → suggest `/product:brainstorm`
- User needs data visualization → suggest `/data:viz-dashboard`

## Loading

### Via shell wrapper (recommended)
```bash
# Add to ~/.zshrc
cc-skills() {
  local plugins=()
  for d in ~/Projects/agent-skills/*/; do
    [[ -f "$d/.claude-plugin/plugin.json" ]] && plugins+=(--plugin-dir "$d")
  done
  claude "${plugins[@]}" "$@"
}
```

### Via installed_plugins.json
Each plugin is registered in `~/.claude/plugins/installed_plugins.json` as `<name>@local`.
