---
name: mcp-integrations
description: Orchestrate MCP integrations for maximum productivity. Use when connecting multiple MCP servers into cohesive workflows, when designing cross-service automations, or when optimizing data flow between tools like Gmail, Calendar, Drive, Figma, Linear, and GitHub.
---

# MCP Integration Orchestration

Connect and optimize Model Context Protocol integrations to create seamless AI-powered workflows across multiple services.

## Core Philosophy

MCP connectors are most powerful when they work together. True productivity comes from seamless data flow between tools, not just individual tool automation.

## Integration Design Process

### 1. Map Available Connectors
Inventory all MCP servers and their capabilities:
```
MCP Server         Capabilities
────────────────────────────────────
gmail              Read/send/search email
calendar           Events, scheduling
drive              File read/write/search
figma              Design extraction, screenshots
linear             Issues, projects, cycles
github             Repos, PRs, issues
slack              Messages, channels
obsidian           Notes, knowledge base
```

### 2. Identify Workflow Opportunities
Look for manual data transfer between tools:
- Email → Issue creation (gmail → linear)
- Design approval → Task update (figma → linear)
- PR merge → Slack notification (github → slack)
- Meeting notes → Action items (calendar → linear)

### 3. Design Integration Chains
Map data flow between services:
```
Trigger: New Figma design comment mentioning "approved"
  → Extract design specs (figma MCP)
  → Create implementation issue (linear MCP)
  → Notify dev channel (slack MCP)
  → Add to sprint backlog (linear MCP)
```

### 4. Implement with Error Handling
- Validate data at each step before passing to next service
- Log integration chain execution for debugging
- Handle partial failures gracefully (don't lose data mid-chain)
- Implement retry logic for transient failures

## Common Integration Patterns

### Research → Documentation
```
Web search → Extract insights → Create Obsidian note → Link to project
```

### Code Review Pipeline
```
PR created → Read diff → Generate review comments → Post to GitHub
```

### Design-to-Development
```
Figma design → Extract specs → Create Linear issue → Assign to sprint
```

### Meeting Follow-up
```
Calendar event ended → Check notes → Create action items in Linear → Send summary to Slack
```

## Security Considerations

- **Principle of least privilege**: Only request permissions each MCP server actually needs
- **Data classification**: Be aware of what data flows between services
- **Audit trail**: Log all cross-service data transfers
- **Authentication**: Ensure each MCP server has valid, scoped credentials

## When NOT to Use
- For single-service automation that doesn't need integration
- When security requirements prohibit cross-service data sharing
- For simple tasks that don't benefit from orchestration overhead

## Success Metrics
- Reduction in manual task switching between tools
- Increased data consistency across platforms
- Time saved through automated workflow execution
