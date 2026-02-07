# agent-skills

A Claude Code plugin providing 530+ modular skills for product development, hardware engineering, iOS development, design systems, team management, Northwestern MPD2 frameworks, and domain-expert assistants.

## Installation

Add this plugin to your Claude Code environment:

```bash
# Clone the repo
git clone <repo-url> ~/Projects/agent-skills

# Or symlink into your Claude Code plugins directory
```

## Structure

```
agent-skills/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── skills/
│   ├── <skill-name>/
│   │   └── SKILL.md         # Skill definition (YAML frontmatter + instructions)
│   │   └── scripts/         # Optional bundled scripts
│   │   └── references/      # Optional reference docs
│   └── ...                  # 530+ skill directories
├── scripts/
│   └── import-gist-assistants.py  # Batch import script for gist collections
└── README.md
```

## Skill Categories

### Hand-Crafted Skills (58)

Deep, workflow-rich skills built from real usage patterns.

#### General Purpose (16)
| Skill | Description |
|-------|-------------|
| `brainstorming` | Structured brainstorming workflows |
| `skill-creator` | Guide for creating new skills |
| `writing-plans` | Technical writing plan creation |
| `verification-before-completion` | Pre-completion verification checklists |
| `systematic-debugging` | Structured debugging methodology |
| `test-driven-development` | TDD workflow guidance |
| `pdf` / `docx` / `pptx` / `xlsx` | Office document generation |
| `webapp-testing` | Web application testing strategies |
| `mcp-builder` | MCP server development guide |
| `brain-dump-assistant` | Obsidian vault organization |
| `agent-mailbox` | Inter-agent handoff protocol |
| `linear-project-management` | Linear + codebase sync workflows |
| `effective-communication` | Cross-functional communication frameworks |

#### Hardware Engineering (3)
| Skill | Description |
|-------|-------------|
| `hw-electronics-engineer` | ESP32, circuit design, SPICE simulation |
| `hw-research` | Hardware research methodology |
| `hw-kicad-design` | KiCad PCB design with MCP integration |

#### iOS Development (6)
| Skill | Description |
|-------|-------------|
| `ios-development` | iOS development acceleration |
| `ios-simulator` | iOS simulator testing workflows |
| `ios-mobile-testing` | Mobile iOS testing strategies |
| `ios-iphone-apps` | iPhone app development expertise |
| `ios-swiftui-patterns` | SwiftUI performance optimization |
| `ios-emergency-systems` | Safety-critical iOS emergency alerts |

#### Design (4)
| Skill | Description |
|-------|-------------|
| `design-architect` | Design-to-code architecture |
| `design-system-prototyper` | Rapid UI prototyping with design systems |
| `design-compounding-coder` | Context-compounding design implementation |
| `design-review` | Product architecture and spec creation |

#### Product Management (8)
| Skill | Description |
|-------|-------------|
| `product-discovery` | Market discovery and opportunity validation |
| `product-design-strategy` | Product design strategy and lean principles |
| `product-prioritization` | Feature prioritization and backlog grooming |
| `product-prototype-plan` | Prototype planning and MVP design |
| `product-vendor-management` | Vendor sourcing and supply chain |
| `product-compliance` | Regulatory certification navigation |
| `product-release` | Launch coordination and release management |
| `product-stage-gates` | Stage-gate development process |

#### Strategy & Decision Making (6)
| Skill | Description |
|-------|-------------|
| `decision-memo` | Executive decision memos |
| `red-team-analysis` | Plan stress-testing and failure modes |
| `negotiate-prep` | Negotiation strategy preparation |
| `gtm-narrative` | Go-to-market narrative and positioning |
| `refactor-plan` | Safe, incremental refactor roadmaps |
| `trade-off-analysis` | Multi-criteria trade-off evaluation |

#### Team & Organization (3)
| Skill | Description |
|-------|-------------|
| `team-coaching` | Team coaching plans and feedback |
| `team-orchestration` | Cross-functional team coordination |
| `materials-selection` | Materials evaluation and selection |

#### Northwestern MPD2 (3)
| Skill | Description |
|-------|-------------|
| `mpd-refine-notes` | MPD2 course note refinement |
| `mpd-portfolio-strategy` | Innovation portfolio optimization |
| `mpd-concept-evaluation` | Product concept validation |

#### Specialty (9)
| Skill | Description |
|-------|-------------|
| `homelab-network-engineer` | Homelab and network infrastructure |
| `human-factors-engineering` | Usability and ergonomics |
| `ai-toolkit-expert` | AI agent development workflows |
| `test-automation` | Test strategy and CI/CD quality gates |
| `ogsmt-framework` | OGSMT strategic planning |
| `parallel-ux-development` | Parallel product/UX coordination |
| `validate-design-feasibility` | Design feasibility assessment |
| `mcp-integrations` | MCP server orchestration |
| `v2mom-cascade` | V2MOM cascading goal alignment |

### Gist-Sourced Skills (~467)

Domain-expert assistants auto-imported from curated collections. Each is a small, focused skill with clear role activation.

| Category | Count | Prefix |
|----------|-------|--------|
| Development (Backend) | 25 | `dev-backend-` |
| Development (Frontend) | 25 | `dev-frontend-` |
| Development (Cloud/DevOps) | 20 | `dev-infra-` |
| Development (Security) | 15 | `dev-security-` |
| Development (Testing) | 15 | `dev-testing-` |
| Development (Mobile) | 15 | `dev-mobile-` |
| Data/Analysis/AI | 40 | `data-` |
| AI/LLM | 20 | `ai-` |
| Design/UX | 20 | `design-` |
| Business/Product | 20 | `biz-product-` |
| Business/Strategy | 20 | `biz-strategy-` |
| Business/Communication | 15 | `biz-comm-` |
| Cloud/Architecture | 15 | `cloud-` |
| Writing/Documentation | 15 | `writing-` |
| + LiteLLM collection | ~190 | various |

## SKILL.md Format

Every skill follows the Claude Code plugin format:

```yaml
---
name: skill-name          # kebab-case identifier
description: Trigger phrase describing when to use this skill.
---

# Skill Title

Instructions in imperative form...
```

## Regenerating Gist Skills

To re-import the gist-sourced skills (e.g., after updates):

```bash
python3 scripts/import-gist-assistants.py
```

Use `--dry-run` to preview without writing files.

## Verification

```bash
# Total skill count
ls skills/*/SKILL.md | wc -l

# All skills have name frontmatter
grep -rL '^name:' skills/*/SKILL.md

# All skills have description frontmatter
grep -rL '^description:' skills/*/SKILL.md
```
