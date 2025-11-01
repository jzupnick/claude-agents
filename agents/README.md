# Agents

Complete, production-ready agents. Each one solves a specific problem end-to-end.

## Template

When you add an agent, include:

```markdown
# Agent Name

| name | description | model | category |
|------|-------------|-------|----------|
| [agent-name] | [One-line description of what this agent does] | [sonnet/haiku/etc] | [backend/frontend/devops/etc] |

## Purpose
What problem were you actually solving? One sentence.

## Core Philosophy
What principles guide this agent's approach?

## Capabilities
Core areas of expertise:

**[Primary Domain]:**
- [Specific capability 1]
- [Specific capability 2]

**[Secondary Domain]:**
- [Specific capability 1]
- [Specific capability 2]

## Behavioral Traits
How this agent operates:
- [Trait 1]: [Description]
- [Trait 2]: [Description]

## Workflow Position
Where this fits in your development process:
- **Triggers**: [What activates this agent]
- **Inputs**: [What it needs to work]
- **Outputs**: [What it produces]
- **Downstream**: [What happens next]

## Response Approach
How this agent structures its responses:
- [Approach 1]: [When used]
- [Approach 2]: [When used]

## Usage
Actual command or invocation.

## Example Interactions
**Scenario 1**: [Brief description]
- Input: [What you give it]
- Output: [What you get back]

**Scenario 2**: [Brief description]
- Input: [What you give it]
- Output: [What you get back]

## Key Distinctions
What makes this different from similar agents:
- vs [Other Agent Type]: [Key difference]
- vs [Generic Approach]: [Why specialized]

## Tools & Software
Preferred tools this agent uses:
- Tool 1 (why this over alternatives)
- Tool 2 (specific capabilities needed)

## Mental Models
Core frameworks this agent applies:
- Model 1 (when to use it)
- Model 2 (what it reveals)

## Knowledge Base
- Books: [Key texts that inform this approach]
- Influences: [People/ideas that shaped this]
- Channels: [Where to learn more]
- Frameworks: [Specific methodologies applied]

## Jargon Glossary
Define terms this agent uses that aren't obvious:
- **Term 1**: [Plain English definition, why it matters]
- **Term 2**: [What it actually means in practice]
- **Term 3**: [Common misunderstanding vs. real meaning]

## Online Communities
Where would this agent "hang out" to discuss issues?

**Primary haunts** (active participation):
- [Community name] - [Why here? What questions get answered?]
- [Forum/Discord/Slack] - [What expertise lives here?]

**Occasional visits** (specific deep dives):
- [Specialized forum] - [When you need this specific knowledge]
- [Subreddit/Stack] - [For what edge cases?]

**Reddit communities** (curated by signal/noise):
- r/[subreddit] - [What discussions? Quality level?]
- r/[subreddit] - [When to search here?]

## Educational Background
What domain expertise does this assume?
- Required: [Must-have knowledge]
- Helpful: [Nice-to-have context]

## Hardware Requirements
Any specific compute/storage/network needs?

## CLI Tools for Autonomous Delivery

**IMPORTANT**: All tools must be validated as real, available packages. Use web search to verify existence before including.

**Required tools** (agent cannot run without these):
- `tool_name` - What it does, why required (verified: package manager/source)
- `tool_name` - What it does, why required (verified: package manager/source)

**Optional tools** (enhance but not required):
- `tool_name` - What it enables, tradeoff if missing (verified: package manager/source)

**Installation:**
```bash
# Required - all commands verified
install_command_1
install_command_2

# Optional - all commands verified  
install_command_3
```

**Health check:**
```bash
# Test all required tools are available and working
./scripts/check_agent_tools.sh [agent_name]
```

## LLM Configuration

**Ideal model:** `model-name` (as of YYYY-MM-DD)

**Why this model:**
- [Specific capability 1] - Why it matters for this job
- [Specific capability 2] - Performance requirement
- [Specific capability 3] - Cost/speed tradeoff

**Minimum requirements:**
- Context window: [size needed]
- Reasoning capability: [what level]
- Speed: [response time needed]
- Cost: [$/1M tokens budget]

**Model fallbacks:**
1. Primary: `model-name-1` - Best for this job
2. Secondary: `model-name-2` - If primary unavailable
3. Minimum: `model-name-3` - Acceptable but degraded performance

## When NOT to Use
What jobs is this NOT hired to do?

## Collaborates With

**Upstream** (depends on these agents):
- [Agent name] - Provides: [what you need from it]
- [Agent name] - Provides: [what you need from it]

**Downstream** (feeds into these agents):
- [Agent name] - Consumes: [what artifacts you produce]
- [Agent name] - Consumes: [what artifacts you produce]

**Parallel** (runs alongside, shares context):
- [Agent name] - Coordinates: [what you sync on]

**Conflicts With** (don't run together):
- [Agent name] - Because: [why they clash]

## Example Integration
Show it composed with other agents.

## Success Metrics
How do you know it did the job well?

## Gotchas
What broke? What surprised you?

## Improvements
What would make this 10x better?
```

## Catalog

*Add your agents here as you build them*
