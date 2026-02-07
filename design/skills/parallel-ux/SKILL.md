---
name: parallel-ux-development
description: Coordinate parallel physical product and user experience development. Use when building products with both hardware and software components, when hardware and UX tracks need synchronization, or when managing cross-track dependencies between physical and digital design.
---

# Parallel Physical Product & UX Development

Synchronize hardware and software development tracks to ensure form factor aligns with behavioral design without blocking parallel progress.

## Core Philosophy

Physical products and user experiences co-evolve rather than develop sequentially. Success requires parallel development tracks that maintain alignment while allowing each discipline to optimize within their domain.

## Parallel Track Structure

### Physical Product Track
1. **Concept** → Form factor exploration, materials investigation
2. **Feasibility** → Engineering constraints, manufacturing process selection
3. **Design** → Detailed CAD, prototype fabrication, DFM optimization
4. **Validation** → Functional testing, manufacturing trials
5. **Production** → Tooling, pilot runs, quality systems

### User Experience Track
1. **Research** → User needs, journey mapping, behavioral patterns
2. **Concept** → Interaction models, information architecture
3. **Design** → UI/UX detailed design, onboarding flows
4. **Validation** → Usability testing, A/B testing, beta feedback
5. **Launch** → Deployment, analytics, iteration

## Synchronization Points

### Sync 1: Concept Alignment
- Physical form factor constraints shared with UX team
- UX interaction requirements shared with hardware team
- Joint review of user scenarios spanning physical + digital

### Sync 2: Design Integration
- Physical dimensions finalized → UX adapts interface layouts
- UX interaction patterns confirmed → Hardware validates button/sensor placement
- Joint prototype combining physical + digital elements

### Sync 3: Validation Convergence
- Integrated user testing with physical prototype + software
- Cross-track issue resolution and trade-off decisions
- Final alignment before production/launch

## Cross-Track Dependencies

Map and manage dependencies that span tracks:

```
Physical Decision          →  UX Impact
─────────────────────────────────────────
Device size reduced        →  Fewer UI elements fit on screen
Battery capacity limited   →  Must reduce background processes
New sensor added           →  New interaction paradigm needed
Form factor sealed         →  No physical reset button → software recovery flow

UX Decision                →  Physical Impact
─────────────────────────────────────────
Gesture-based interaction  →  Needs accelerometer/gyroscope
Audio feedback required    →  Needs speaker placement in enclosure
LED status indicators      →  PCB routing + light pipe design
Charging UX (wireless)     →  Coil placement + thermal design
```

## Coordination Practices

1. **Shared milestone board** — Both tracks visible with dependency links
2. **Weekly cross-track standup** — 15-min sync on blockers and interface decisions
3. **Decision log** — Record cross-track trade-offs with rationale
4. **Integration prototype sprints** — Regular combined build-and-test cycles
5. **Shared user personas** — Consistent user model across both tracks

## When NOT to Use
- For purely digital products without physical components
- When sequential development is more appropriate (e.g., hardware must be done first)
- For simple products where coordination overhead exceeds benefits

## Success Metrics
- Cross-track milestone alignment: >90% on-time
- Integration issues identified early: >80% before final assembly
- Parallel development velocity maintained: No track blocking others
- User experience coherence: >85% satisfaction with integrated experience
