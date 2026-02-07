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

### In Zed

Skills are **not** invocable as slash commands in Zed — the `/plugin:skill` syntax only works in Claude Code CLI. In Zed, add an agent rule that tells the agent to **read** skill files instead:

```json
{
  "name": "Agent Skills (525 skills in 10 plugins)",
  "content": "525 specialist skills at ~/Projects/agent-skills/ in 10 plugins:\n- code (211): Software dev. Catalog: ~/Projects/agent-skills/code/AGENTS.md\n- ops (80): Business/strategy. Catalog: ~/Projects/agent-skills/ops/AGENTS.md\n- data (48): Analytics/viz. Catalog: ~/Projects/agent-skills/data/AGENTS.md\n- write (41): Writing/editing. Catalog: ~/Projects/agent-skills/write/AGENTS.md\n- ai (30): AI/ML/LLMs. Catalog: ~/Projects/agent-skills/ai/AGENTS.md\n- research (28): Analysis. Catalog: ~/Projects/agent-skills/research/AGENTS.md\n- design (27): UX/design. Catalog: ~/Projects/agent-skills/design/AGENTS.md\n- tools (24): iOS/hw/utils. Catalog: ~/Projects/agent-skills/tools/AGENTS.md\n- infra (18): Cloud/networking. Catalog: ~/Projects/agent-skills/infra/AGENTS.md\n- product (18): Product mgmt. Catalog: ~/Projects/agent-skills/product/AGENTS.md\n\nHow to use skills:\n1. Read the relevant AGENTS.md catalog to find a skill by description\n2. Read the skill file at ~/Projects/agent-skills/<plugin>/skills/<skill-name>/SKILL.md\n3. Follow the instructions in the SKILL.md file to complete the user's task\n\nIMPORTANT: Do NOT try to invoke skills as slash commands (e.g. /code:react). Instead, read the SKILL.md file directly and apply its instructions. Skills are reference documents, not executable commands in this environment."
}
```

Add this to `~/.config/zed/settings.json` under `assistant.default_open_ai_model` → `agent_instructions`.
