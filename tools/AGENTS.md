# tools — Agent Skills

| Skill | Description |
|-------|-------------|
| `action-items` | Extract and organize action items from meeting notes, conversations, and documents with assignee and deadline tracking |
| `assistant` | Provide general-purpose task assistance with structured responses, step-by-step guidance, and contextual recommendations |
| `builder` | Guide for creating high-quality MCP (Model Context Protocol) servers to integrate external APIs and services with Claude. Use when building servers that connect LLMs to external data sources, APIs, or tools. |
| `default` | Handle general requests with adaptive responses, task decomposition, and appropriate tool selection |
| `development` | Use when developing iOS apps, implementing Swift/SwiftUI features, optimizing app performance, or setting up CI/CD for iOS projects |
| `docx` | Create, edit, and analyze Word documents (.docx files). Supports tracked changes, comments, formatting, and text extraction. |
| `electronics-engineer` | Use when designing circuits, programming microcontrollers (ESP32, Arduino, STM32), simulating in SPICE, or debugging hardware issues |
| `emergency-systems` | Use when designing emergency alert systems, implementing safety-critical iOS features, or building NFPA/UL-compliant notification systems |
| `general` | Provide versatile assistance for miscellaneous tasks with clear explanations and structured output |
| `helper` | Assist with quick tasks, answer questions, and provide concise guidance on a variety of topics |
| `integrations` | Orchestrate MCP integrations for maximum productivity. Use when connecting multiple MCP servers into cohesive workflows, when designing cross-service automations, or when optimizing data flow between tools like Gmail, Calendar, Drive, Figma, Linear, and GitHub. |
| `iphone-apps` | Build professional native iPhone apps in Swift with SwiftUI and UIKit. Full lifecycle - build, debug, test, optimize, ship. CLI-only, no Xcode. Targets iOS 26 with iOS 18 compatibility. |
| `kicad-design` | AI-powered KiCad PCB design assistant. Use when designing PCBs, creating schematics, generating BOMs, exporting manufacturing files, or sourcing components via DigiKey/JLCPCB. |
| `mailbox` | Check inbox and send handoffs between agent sessions. Use at session START to check for pending work, and at session END to hand off context. |
| `meeting-summary` | Summarize meetings with key decisions, discussion points, action items, and follow-up deadlines |
| `mobile-testing` | Test mobile apps on simulators and devices with automated UI interaction, screenshot capture, and accessibility checks |
| `pdf` | Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging, splitting, and form handling. |
| `pptx` | Create, edit, and analyze PowerPoint presentations (.pptx). Supports layouts, templates, charts, and OOXML manipulation. |
| `quick-answer` | Provide fast, concise answers to straightforward questions with relevant context and source references |
| `research` | Research open source hardware, electronic components, and certifications. Use when designing hardware projects, sourcing components, or validating open source compliance. Leverages OSHWA and DigiKey MCP servers. |
| `simulator` | 21 production-ready scripts for iOS app testing, building, and automation. Provides semantic UI navigation, build automation, accessibility testing, and simulator lifecycle management. Optimized for AI agents with minimal token output. |
| `swiftui-patterns` | Advanced SwiftUI optimization techniques for smooth, responsive interfaces. Use when SwiftUI views render slowly, animations drop frames, or memory usage is higher than expected. |
| `verify` | Require actual verification before claiming work is complete. Use when about to claim work is done, fixed, or passing - evidence before assertions always. |
| `xlsx` | Create, edit, and analyze Excel spreadsheets (.xlsx, .xlsm, .csv, .tsv). Supports formulas, formatting, and data analysis. |

**Path:** `~/Projects/agent-skills/tools/skills/<skill-name>/SKILL.md`

To use a skill, read its SKILL.md file for full instructions.
