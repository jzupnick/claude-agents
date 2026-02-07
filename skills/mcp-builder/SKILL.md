---
name: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers to integrate external APIs and services with Claude. Use when building servers that connect LLMs to external data sources, APIs, or tools.
---

# MCP Server Development Guide

## Development Phases

### Phase 1: Research and Planning
- Understand MCP design patterns from protocol specs
- Study framework documentation
- Plan API endpoint coverage vs workflow tools

### Phase 2: Implementation
- Build project infrastructure
- Create core utilities
- Implement individual tools

### Phase 3: Review and Testing
- Code quality checks
- Verification using MCP Inspector
- Integration testing

### Phase 4: Evaluation
- Develop 10 complex test questions
- Validate LLM effectiveness

## Design Principles

Balance comprehensive API endpoint coverage with specialized workflow tools. Give agents flexibility while maintaining convenience.

### Tool Naming
- Use consistent `service_action` format
- Be discoverable and descriptive

### Tool Requirements
- Clear input/output schemas (Zod/Pydantic)
- Actionable error messages
- Proper annotations (readOnlyHint, destructiveHint)
- Pagination for large datasets

## Recommended Stack

**TypeScript preferred** - High-quality SDK, good execution compatibility, strong AI code generation.

### Transport Types
- `stdio` - Local process execution
- `http` - Remote servers with stateless JSON
- `sse` - Server-Sent Events for streaming

## Quality Assurance

Evaluations should:
- Be independent and read-only
- Require multiple tool calls
- Have verifiable, stable answers
- Reflect realistic use cases
