# Example: Repo Setup

## Problem
Needed a structured place to save Claude Code agents without creating future organizational debt.

## First Attempt
Could have just dumped files in a folder. But that creates findability problems within weeks.

## Solution
Created opinionated structure with clear boundaries:
- Agents = complete solutions
- Subagents = composable pieces
- Skills = knowledge domains
- Tools = executables
- Workflows = processes
- Examples = real usage

## Key Decisions

**Why separate agents from subagents?**
Agents are what you run. Subagents are what you compose. Different use cases, different discoverability needs.

**Why examples folder?**
Documentation lies. Examples show what actually worked.

**Why this structure?**
It maps to how you actually think about the problem: "Do I have something that does X?" vs "How do I build Y?"

## What Would Make This Better

- Template generator script
- Quick search tool
- Usage analytics (what's actually getting used?)
- Version tracking for agents that evolve

## Time Investment
30 minutes to set up. Saves hours in the long run.
