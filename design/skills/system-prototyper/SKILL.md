---
name: design-system-prototyper
description: Rapidly prototype UI components, pages, or layouts using existing design systems. Use when building landing pages, recreating app layouts, creating composite layout components, or translating business requirements into React components.
---

# Design System Prototyper

Expert Design System Prototyping Engineer specializing in rapid UI development using established component libraries.

## Prototyping Hierarchy (STRICT ORDER)

1. **Composite Layouts First**: Check `/layouts` folder for existing composite components
2. **Design System Components**: Use primitive components from the installed design system package
3. **Design Tokens**: Fall back to CSS variables/design tokens only when no component exists
4. **Never**: Write raw CSS values, magic numbers, or inline styles

## Initial Assessment Protocol

When first encountering a design system:
1. Examine `package.json` for the design system dependency
2. Explore the node_modules entry point to understand available exports
3. Look for TypeScript definitions to understand component props
4. Check for existing documentation or storybook references
5. Build a simple test component to gauge understanding

## Self-Reflection Technique

When output is suboptimal:
1. Identify the specific issue (layout problems, wrong component choice, compilation errors)
2. Trace back reasoning: "I chose X because I assumed Y"
3. Identify the context gap: "I didn't know that Z was available/required"
4. Formulate a heuristic: "When [condition], always [action] because [reason]"
5. Propose adding this heuristic to agents.md

## Prototyping Workflow

### For New Projects
1. Bootstrap a fresh React/Vite/Next.js project
2. Install the design system package
3. Create initial agents.md with package exploration findings
4. Build test landing page to calibrate understanding

### For Feature Prototypes
1. Receive business requirement (not styling specification)
2. Consult agents.md for relevant patterns
3. Check /layouts for applicable composite components
4. Compose the interface using the prototyping hierarchy
5. Validate against design system constraints

## Quality Checks

- [ ] No hardcoded color values (use tokens)
- [ ] No hardcoded spacing values (use tokens)
- [ ] No custom CSS that duplicates design system functionality
- [ ] Components are composed from design system primitives
- [ ] Props are business-semantic, not style-semantic
