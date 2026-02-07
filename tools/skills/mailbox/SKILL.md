---
name: agent-mailbox
description: Check inbox and send handoffs between agent sessions. Use at session START to check for pending work, and at session END to hand off context.
---

# Agent Mailbox Skill

## When to Use This Skill

**MANDATORY at session boundaries:**
1. **Session START**: Check for messages from previous sessions
2. **Session END**: Send handoff if work is incomplete or context is valuable

## Session Start Protocol

Run this IMMEDIATELY when starting work as a named agent:

```python
# Check your inbox
peek_queue("your-agent-name")  # e.g., "design-agent", "discovery-agent"

# If messages exist, claim and read them
msg = claim_next("your-agent-name")
if msg["message"]:
    # Process the handoff context
    # Then mark complete when done:
    complete_message(msg["message"]["message_id"])
```

**Known agents:** discovery-agent, design-agent, prototype-agent, vendor-agent, compliance-agent, release-agent, any-successor

## Session End Protocol

Before ending ANY session where:
- Work is incomplete
- Context would help the next session
- You learned something another agent needs

**Send a handoff:**

```python
send_message(
    to_agent="design-agent",  # or "any-successor" for general handoffs
    subject="Brief description of handoff",
    body='''{
        "status": "IN_PROGRESS",
        "what_was_done": ["action 1", "action 2"],
        "next_action": "Single clear next step",
        "blockers": [],
        "artifacts": ["path/to/file1", "path/to/file2"]
    }''',
    from_agent="discovery-agent",
    priority=2  # 0=urgent, 1=high, 2=normal, 3=low
)
```

## Quick Commands

| Action | Command |
|--------|---------|
| Check inbox | `peek_queue("agent-name")` |
| Claim next | `claim_next("agent-name")` |
| Mark done | `complete_message(message_id)` |
| Send handoff | `send_message(to_agent, subject, body, from_agent)` |
| System health | `health_check()` |

## Why This Matters

Justin shouldn't relay context between sessions manually. This system exists so agents can coordinate directly. **Using it saves human time.**

## Failure to Use = Failure Mode

If you skip the mailbox:
- Previous context is lost
- Work gets duplicated
- Justin has to re-explain things
- The system becomes shelfware

**Check the mailbox. Send handoffs. Every time.**
