---
name: product-stage-gates
description: "Use when managing structured product development through stage-gate processes, evaluating gate readiness, or making go/no-go decisions"
---

# Product Stage-Gate Development

Guide systematic product development through structured gates with clear decision criteria and deliverables. Reduce risk and improve success rates through structured evaluation points, clear deliverables, and data-driven go/no-go decisions.

## Core Philosophy

Systematic product development reduces risk through structured evaluation points at each stage. After each gate, investment increases, making early validation critical. Design bugs cost 1x to fix, production bugs cost 10,000x.

## Gate Overview

| Gate | Question | Decision Options |
|------|----------|-----------------|
| Gate 0: Opportunity | Is this opportunity worth pursuing? | GO / NO-GO / PIVOT |
| Gate 1: Feasibility | Can we build it? Do customers want it? | GO / NO-GO / ITERATE |
| Gate 2: Design Lock | Are we ready to commit to tooling and production? | LOCK / ITERATE |
| Gate 3: Production | Are we ready to ship? | RELEASE / HOLD / ABORT |

---

## Gate 0: Opportunity Review

### PASS (GO) if:
- [ ] Opportunity addresses real customer need with evidence (3+ customer signals)
- [ ] Competitive position is defensible
- [ ] Financial model shows viable unit economics hypothesis
- [ ] Technical and manufacturing feasibility not obviously impossible
- [ ] No regulatory showstoppers
- [ ] Founder has capacity to pursue

### FAIL (NO-GO) if:
- [ ] No evidence of customer need
- [ ] Unit economics fundamentally broken
- [ ] Technical impossibility identified
- [ ] Regulatory barrier insurmountable

### PIVOT if:
- [ ] Opportunity exists but current framing is wrong
- [ ] Adjacent opportunity more attractive
- [ ] Same customer, different solution needed

### Required Inputs
- Opportunity map with prioritized opportunities and evidence
- Competitive analysis and positioning
- Financial preliminary (unit economics hypothesis, TAM/SAM/SOM)
- Scenario plans (best/worst/likely case)
- Customer segments defined
- Value proposition articulated
- Technical feasibility gut-check
- Regulatory landscape overview

### Key Questions
- What is the falsifiable hypothesis?
- What evidence supports customer need?
- What kills this opportunity?
- What has to go right for this to work?

---

## Gate 1: Feasibility Review

### PASS (GO) if:
- [ ] Concept validated with target customers
- [ ] Technical architecture feasible
- [ ] Vendors identified and qualified
- [ ] Unit economics still viable with real cost data
- [ ] Regulatory pathway clear

### FAIL (NO-GO) if:
- [ ] Customer validation failed (no problem-solution fit)
- [ ] Technical architecture has fundamental flaws
- [ ] No viable vendors at acceptable cost
- [ ] Unit economics broken with real data

### ITERATE if:
- [ ] Validation partially successful with specific issues to address
- [ ] Design needs refinement based on feedback
- [ ] More validation needed before committing

### Required Inputs
- Selected concept with rationale and architecture
- Product Requirements Document
- Alpha prototype test results and customer validation
- Costed BOM and approved vendor list
- Regulatory requirements documented
- Updated financial model with real cost data

### Key Questions
- Is the concept validated with real customers?
- Can this architecture be built?
- Are the vendors reliable and costs acceptable?
- Do unit economics still work with real data?

---

## Gate 2: Design Lock Review

**This is the most expensive gate.** After Gate 2:
- Tooling investments are made (often $10K-$100K+)
- Design changes become very expensive
- Vendor commitments are binding
- Timeline to launch is largely fixed

### PASS (LOCK) if:
- [ ] Design declared freeze-ready
- [ ] Beta validation successful
- [ ] First article inspection passed
- [ ] Compliance pathway on track
- [ ] All stakeholders agree design is stable
- [ ] Financial model supports tooling investment

### FAIL (ITERATE) if:
- [ ] Design has unresolved issues
- [ ] Beta validation revealed problems
- [ ] First article failed
- [ ] Compliance issues require design changes
- [ ] Financial model does not support investment

### Required Inputs
- Design freeze status and final specifications
- Beta unit test results and field testing summary
- Tooling readiness and first article results
- Compliance testing plan and certification status
- Final unit economics (unit cost, target price, gross margin, breakeven volume)
- Draft launch timeline

### Change Control After Lock
1. All changes require formal Change Request
2. Impact assessment (cost, timeline, risk)
3. Approval required for any change
4. Changes documented with full rationale

---

## Gate 3: Production Ready Review

**This is the final gate.** After Gate 3:
- Manufacturing produces at scale
- Product ships to customers
- There is no going back

### PASS (RELEASE) if:
- [ ] Release checklist 100% complete
- [ ] All certifications obtained
- [ ] Pilot production successful
- [ ] Quality targets met
- [ ] All stakeholders recommend SHIP
- [ ] Financial review approved
- [ ] Support process ready

### HOLD if:
- [ ] Minor issues resolvable quickly
- [ ] Certification pending but expected imminently
- [ ] Quality issues with known fix

### ABORT if:
- [ ] Critical quality or safety issue
- [ ] Certification denied or significantly delayed
- [ ] Financial model no longer viable
- [ ] Market conditions fundamentally changed

### Release Checklist Categories
- **Product Readiness**: Design freeze confirmed, specs validated, certs obtained
- **Manufacturing Readiness**: Pilot successful, quality plan active, logistics tested
- **Commercial Readiness**: Pricing finalized, channels ready, support process ready
- **Documentation Readiness**: User docs complete, support docs complete, regulatory filed
- **Financial Readiness**: Unit economics validated, launch budget approved, cash flow adequate

---

## Review Process (All Gates)

1. Gather required inputs from all responsible parties
2. Evaluate against gate criteria with evidence
3. Identify top risks and mitigations
4. Facilitate voting and consensus building
5. Record decision with rationale
6. Generate Gate Decision Document
7. Define conditions for proceeding and next steps

## Behavioral Traits
- **Systematic**: Follow structured methodology consistently across projects
- **Risk-focused**: Identify and mitigate risks early in development process
- **Decision-oriented**: Make clear go/no-go decisions based on defined criteria
- **Stakeholder-coordinated**: Manage multiple perspectives and requirements effectively

## Anti-Patterns to Avoid
- Rubber-stamping gates without rigorous evaluation
- Skipping gates to save time
- Allowing scope creep between gates
- Making emotional rather than evidence-based decisions
- Locking design prematurely without adequate validation
- Ignoring dissenting opinions from stakeholders
