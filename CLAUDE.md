# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Architecture

This is a collection of Claude Code agents, subagents, skills, tools, and workflows organized around the jobs-to-be-done methodology. The structure optimizes for discoverability and reusability, incorporating best practices from the wshobson/agents template structure.

### Core Structure
```
agents/          # Complete, production-ready solutions
subagents/       # Reusable components organized by job-to-be-done
skills/          # Domain knowledge and capabilities  
tools/           # Executable utilities and scripts
workflows/       # Multi-step processes
examples/        # Real usage patterns and implementations
journals/        # Work journals for continuous improvement
scripts/         # Health checks and monitoring tools
```

### Philosophy
- **Ship within a year**: No agent takes more than a year to ROI
- **Follow your doubt**: If it feels wrong, it probably is
- **Prototype the hard thing**: Test the differentiation early
- **Think slow, act fast**: Deep understanding, rapid execution
- **Jobs-to-be-done**: Name by the job you're hiring them to do

## Template Structure

All templates now include structured metadata tables and enhanced sections inspired by the wshobson/agents approach:

**Metadata Table Format:**
```markdown
| name | description | model | category |
|------|-------------|-------|----------|
| [component-name] | [One-line description] | [sonnet/haiku/etc] | [domain/type] |
```

**Enhanced Template Sections:**
- **Core Philosophy** - Guiding principles for the component
- **Capabilities** - Structured expertise areas with subsections
- **Behavioral Traits** - How the component operates
- **Example Interactions** - Real usage scenarios with inputs/outputs
- **Key Distinctions** - What makes this different from alternatives

## File Organization Principles

1. **Flat is better than nested** (until it's not) - avoid deep nesting unless folders have 20+ files
2. **Names should be searchable** - use descriptive filenames like `reduce_deployment_risk.md` not `agent1.md`
3. **README.md is the index** - every folder has a catalog of its contents
4. **Cross-reference explicitly** - use full paths like `subagents/file_name.md`
5. **Metadata tables** - consistent structured information at the top of each file

### Naming Conventions
- **Agents**: `[verb]_[noun]_[context].md` (e.g., `reduce_deployment_risk.md`)
- **Subagents**: `[job_outcome]_[context].md` (e.g., `challenge_technical_assumptions.md`)
- **Skills**: `[domain]_[specific_knowledge].md` (e.g., `postgres_query_optimization.md`)
- **Tools**: `[action]_[target].[ext]` (e.g., `deploy_to_staging.sh`)
- **Workflows**: `[process_name]_workflow.md` (e.g., `feature_development_workflow.md`)

## Development Workflow

### Essential Commands
```bash
# Setup GitHub repository
./setup_and_push_github.sh [repo-name] [public|private]

# Health checks for subagent tools
./scripts/check_subagent_tools.sh [subagent_name]

# Check LLM model currency
./scripts/check_model_currency.sh [subagent_name]

# Check current LLM leaderboards
./scripts/check_llm_leaderboards.sh [job_type]
```

### When Adding Content

**Before adding anything, ask:**
1. Does this solve a real problem I had? (not hypothetical)
2. Have I used it at least once?
3. Would this help me in 6 months when I've forgotten the context?

**For Agents:**
1. Place in `agents/` directory
2. Use the enhanced template from `agents/README.md`
3. Include metadata table with name, description, model, category
4. Add real example to `examples/`
5. Update the catalog in `agents/README.md`

**For Subagents:**
1. Ensure it's actually reusable (used in 2+ agents)
2. Name by job-to-be-done (when would you hire this?)
3. Follow complete template in `subagents/README.md`
4. Include metadata table and enhanced sections
5. Include LLM configuration and model selection
6. Set up work journal in `journals/[subagent_name]/`

**For Skills:**
1. Use the enhanced skills template with metadata table
2. Include Core Concepts, Best Practices, Common Pitfalls
3. Provide Implementation Examples with code
4. Add Resources section

## Subagent Architecture

Subagents are organized around jobs-to-be-done and include:

- **Metadata table** with name, description, model, category
- **Core Philosophy** and hiring moment
- **Capabilities** with structured subsections
- **Behavioral Traits** describing how they operate
- **Input/Output specification** (artifacts vs deliverables)
- **Tool requirements** and health checks
- **LLM configuration** with model selection criteria
- **Work journals** for continuous improvement
- **Collaboration patterns** with other subagents

### LLM Model Management

All subagents specify:
- Ideal model with reasoning (check leaderboards quarterly)
- Minimum requirements (context, reasoning, speed, cost)
- Model fallbacks (primary, secondary, minimum)
- Performance benchmarks and review schedule

Use the model checking scripts to validate choices:
```bash
./scripts/check_model_currency.sh [subagent_name]
./scripts/check_llm_leaderboards.sh [job_type]
```

## Navigation

**Finding things:**
- Complete solution → `agents/README.md`
- Build something custom → `subagents/README.md`
- Domain expertise → `skills/README.md`
- Executable utilities → `tools/README.md`
- Multi-step process → `workflows/README.md`
- See it in practice → `examples/README.md`

**Key reference files:**
- `PROJECT_MAP.md` - Quick navigation guide
- `FILE_ORGANIZATION.md` - Detailed structure principles
- `CONTRIBUTING.md` - Rules for adding content
- `GAP_ANALYSIS.md` - Comparison with other agent repositories
- `CLAUDE_CODE_INTEGRATION.md` - Export to `.claude/commands/`

## Template Improvements

### From wshobson/agents Integration:
- **Structured metadata tables** for consistent information
- **Core Philosophy** sections to capture guiding principles
- **Capabilities sections** with organized subsections
- **Behavioral Traits** describing operational characteristics
- **Example Interactions** with real input/output scenarios
- **Key Distinctions** highlighting unique value propositions

### Progressive Disclosure:
1. **Metadata** - Always loaded (name, description, model, category)
2. **Core Sections** - Loaded when activated (philosophy, capabilities)
3. **Details** - Loaded on-demand (examples, resources, implementation)

## Code Quality Standards

- Scripts must be executable and include error handling
- Use `set -euo pipefail` in bash scripts
- Include clear usage documentation in script headers
- Test tools thoroughly before adding to repository
- Follow the principle: fail fast and loud
- Use metadata tables for consistent structure
- Include behavioral traits and example interactions

## Repository Management

**Maintenance schedule:**
- Monthly: Delete unused files (6+ months old)
- Quarterly: Update examples with new learnings, review LLM models
- Semi-annually: Reorganize if structure doesn't fit usage

**Git workflow:**
- Use pull requests for significant changes
- Test cross-agent compatibility
- Update documentation with changes
- Use `git-workflow-manager` for git-related tasks

## Integration Features

This repository is designed to integrate with:
- **Claude Code** via `.claude/commands/` export
- **MCP servers** for tool integration
- **GitHub workflows** for automation
- **LLM leaderboards** for model selection
- **Community platforms** for knowledge sharing