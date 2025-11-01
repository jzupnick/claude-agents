# Contributing (to Your Future Self)

## Before You Add Anything

Ask:
1. **Does this solve a real problem I had?** Not a hypothetical one.
2. **Have I used it at least once?** If not, it doesn't belong here yet.
3. **Would this help me in 6 months?** When I've forgotten the context.

## Adding an Agent

1. Put it in `agents/`
2. Use the template in `agents/README.md`
3. Add a real example to `examples/`
4. Update the catalog

## Adding a Subagent

1. Make sure it's actually reusable (used in 2+ agents)
2. Put it in `subagents/`
3. Show how it composes with others

## Adding a Skill

1. Make it specific (not "python" but "python_async_patterns")
2. Make it opinionated (what works, not what exists)
3. Include anti-patterns (what NOT to do)

## Adding a Tool

1. Make it executable
2. Make it fail fast
3. Include one real usage example

## Adding a Workflow

1. Wait until you've done it 3+ times
2. Document decision points (where you think, not just execute)
3. Include time estimates (be honest)

## Maintenance

- **Every month**: Delete what you haven't used in 6 months
- **Every quarter**: Update examples with new learnings
- **Every 6 months**: Reorganize if structure doesn't fit usage

## Red Flags

Stop if you find yourself:
- Creating categories with only one item
- Writing documentation for things you haven't built
- Adding "might be useful" instead of "this solved X"
- Creating structure for its own sake
