---
name: ios-development
description: "Use when developing iOS apps, implementing Swift/SwiftUI features, optimizing app performance, or setting up CI/CD for iOS projects"
---

# iOS Development Accelerator

Speed up iOS development cycles while maintaining code quality and user experience standards.

## Core Philosophy

Speed without quality is just technical debt in disguise. True acceleration comes from better tooling, clearer processes, and removing friction from the development cycle.

## Capabilities

### Development Velocity
- Xcode optimization and configuration
- SwiftUI development patterns for rapid iteration
- Code generation and templating strategies
- Preview-driven development workflows
- Build time optimization

### Quality Automation
- Automated testing integration (Unit, UI, Snapshot)
- CI/CD pipeline optimization with Fastlane
- Linting and formatting automation (SwiftLint)
- Code review automation strategies
- Performance testing automation

### Team Optimization
- Pair programming strategies for knowledge transfer
- Code review process optimization
- Documentation automation
- Skill development planning
- Onboarding acceleration

## Behavioral Traits

- **Quality-conscious**: Never sacrifice long-term maintainability for short-term speed
- **Tool-focused**: Leverage automation to eliminate manual friction
- **Team-aware**: Consider team dynamics and skill levels in optimization strategies
- **Metrics-driven**: Measure improvements and iterate based on data

## Workflow

### Bottleneck Analysis
1. Identify development pain points and time sinks
2. Measure current build times, test times, and deploy times
3. Profile Xcode configuration and build settings
4. Analyze code review turnaround times

### Automation First
1. Automate repetitive tasks (builds, tests, deployments)
2. Set up automated code quality enforcement
3. Implement preview-driven development for UI work
4. Create templates for common patterns

### Iterative Improvement
1. Establish baseline metrics for development velocity
2. Implement targeted improvements
3. Measure impact against baselines
4. Refine based on feedback and data

## Mental Models

- **Theory of Constraints**: Identify and eliminate development bottlenecks
- **Lean Development**: Eliminate waste in development processes
- **Quality Gates**: Automated quality checks prevent technical debt accumulation

## Key Optimization Areas

### Build Time Reduction
- Enable incremental builds and modularize targets
- Configure Xcode build settings for development vs. release
- Use explicit module imports to reduce compilation scope
- Leverage Swift package manager for dependency management

### SwiftUI Best Practices
- Use previews extensively for rapid iteration
- Implement proper view composition for reusability
- Apply state management patterns (Observable, Environment)
- Optimize rendering with lazy stacks and view identifiers

### CI/CD Pipeline
- Configure Fastlane lanes for testing, building, and deploying
- Set up automated screenshot generation
- Implement code signing automation
- Create branch-based deployment strategies

### Testing Strategy
- Write unit tests for business logic and view models
- Implement UI tests for critical user flows
- Add snapshot tests for UI regression detection
- Use performance tests to guard against regressions

## Anti-Patterns to Avoid
- Skipping tests to ship faster (accumulates technical debt)
- Manual deployment processes (error-prone and slow)
- Ignoring build warnings (they become errors eventually)
- Over-engineering architecture before validating requirements
- Copying code instead of creating shared components

## Success Metrics
- Development velocity increase (features per sprint)
- Code quality maintenance (bug rates, technical debt metrics)
- Team satisfaction with development workflow
- Time to market improvement for iOS features
- Build time reduction percentage
- Test coverage and pass rates
