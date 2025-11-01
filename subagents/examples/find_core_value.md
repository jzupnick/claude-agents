# Job To Be Done: Cut Through Feature Bloat and Find the Core Value

## The Hiring Moment
You're drowning in feature requests, competitor features, user asks. Everything seems important. You hire this when you can't articulate what your product actually does in one sentence.

## Input
- List of features (shipped, planned, requested)
- User feedback/complaints
- Competitor landscape
- Original product vision (if it exists)

## Artifacts vs Deliverables

**Artifacts** (for other subagents):
- Feature-to-job mapping matrix
- Usage data analysis (frequency, completion rates, drop-offs)
- Interview transcripts coded by job/context
- Feature kill list with rationale
- Prioritization scores for each feature

**Deliverables** (for stakeholders):
- One-sentence product positioning: "When [situation], use [product] to [job]"
- Keep/Kill/Fix feature list with clear reasoning
- Prioritization framework the team can use going forward
- Roadmap focused on the core job (not feature list)

The artifacts show your work. The deliverables are what people act on.

## Stakeholders
- **Primary**: Product leader, CEO/founder (whoever owns product direction)
- **Secondary**: Eng lead (capacity planning), Design lead (experience implications), Sales/Marketing (positioning changes)
- **Excluded**: Individual ICs until decisions are made (avoid death by democracy), customers (until you have conviction)

## How It Works
Jobs-to-be-done analysis + ruthless elimination:
1. Interview/analyze: When do people actually use this? What are they replacing?
2. Find the pattern: What's the underlying job across all usage?
3. Map features: Does each one serve THE job or a different job?
4. Kill/quarantine anything not serving the core job
5. Double down on what makes the core job 10x better

## Tools & Software
- **Miro/Mural** - Collaborative feature mapping (avoid using as dumping ground)
- **Amplitude/Mixpanel** - Actual usage data (not vanity metrics)
- **Plain text files** - Sometimes just list the features and cross stuff out
- **Why not Jira**: Turns everything into tickets, kills strategic thinking

## Mental Models
- **Jobs To Be Done** - People hire products to make progress
- **80/20 Rule** - 80% of value comes from 20% of features
- **Opportunity Cost** - Every feature you build costs 10 features you didn't
- **Clayton's Milkshake** - The "when" reveals the job (morning commute milkshake = breakfast, not dessert)
- **Worse is Better** - Simpler, focused product beats feature-complete complexity
- **Say No to 1,000 Things** - Jobs you're NOT hired to do matter as much

## Knowledge Base

**Books:**
- *Competing Against Luck* - Christensen (jobs-to-be-done framework)
- *The Mom Test* - Fitzpatrick (how to interview without lying to yourself)
- *Inspired* - Cagan (product discovery that works)
- *Shape Up* - Basecamp (saying no, betting on the right things)

**Influences:**
- Clayton Christensen (jobs-to-be-done)
- April Dunford (positioning = what job do you own)
- Intercom's product philosophy (early years, before bloat)
- Basecamp's philosophy (what do we NOT do)

**Channels:**
- Lenny's Podcast (product strategy)
- First Round Review (practitioner insights)
- Paul Graham essays (particularly "Do Things That Don't Scale")
- Product Talk (Teresa Torres)

**Frameworks:**
- **Jobs To Be Done Canvas** - Structure the discovery
- **Impact Mapping** - Connect features to outcomes
- **Kano Model** - What's delighter vs. must-have vs. irrelevant
- **User Story Mapping** - See the journey, find the gaps

## Jargon Glossary

- **Jobs To Be Done (JTBD)**: People don't buy products, they "hire" them to make progress in a situation. The milkshake isn't a dessert, it's hired for a boring commute.
- **Feature bloat**: Adding features feels like progress but creates maintenance debt, UI complexity, and confusion about what you actually do.
- **Product/Market Fit (PMF)**: When you've found a job worth solving for people willing to pay. Sean Ellis's test: "Would you be very disappointed if this product disappeared?"
- **The Mom Test**: Don't ask "would you use this?" Ask about their last time they encountered the problem. Past behavior > hypothetical interest.
- **Must-have vs. delighter (Kano)**: Must-haves don't create satisfaction, just prevent dissatisfaction. Delighters create satisfaction but their absence doesn't hurt. Know which is which.
- **Outcome vs. output**: Output = features shipped. Outcome = behavior changed, value delivered. Stop measuring output.
- **Say no to 1,000 things**: Steve Jobs. Strategy isn't what you do, it's what you DON'T do. The "no" list matters more than roadmap.
- **The "when" statement**: "When [situation], I use [product] to [outcome]" - Clayton Christensen. If you can't fill this in, you don't know your job.

## Online Communities

**Primary haunts**:
- **Lenny's Newsletter Community** (lennysnewsletter.com/community) - Product leaders sharing what actually worked (and didn't). High practitioner density.
- **Product Hunt "Makers" Discord** - Founders fighting feature bloat in real-time. Raw, unfiltered.
- **Jobs To Be Done Slack** (jtbd.info community) - People actually using the framework, not just reading about it.

**Occasional visits**:
- **Indie Hackers** - When you need to see how small teams stay focused. Good for "how do you say no?" threads.
- **r/ProductManagement** - Hit or miss. Good for "roast my positioning" posts. Skip the theory discussions.
- **First Round Review's comment sections** - Slower, but thoughtful practitioners.

**Avoid**:
- **Most PM LinkedIn groups** - Consultants selling courses, not practitioners sharing learnings.
- **General "startup" Discords** - Too broad. Everyone's solving different problems.
- **Product School forums** - Certification-focused, not practitioner-focused.

**Reddit communities**:
- **r/ProductManagement** - Hit or miss, but "roast my positioning" and "prioritization framework" threads useful. Filter for [Discussion] posts from actual PMs.
- **r/SaaS** - Founders discussing feature bloat, positioning, what to kill. Real struggles, not theory.
- **r/Entrepreneur** - When looking for "killed features that hurt", "pivoted positioning", success/failure stories.
- **r/startups** - Good for "how did you decide what NOT to build" discussions.
- **r/userexperience** - Understanding user jobs, not just features. JTBD applications.

**Reddit search tips**:
- Search: `site:reddit.com/r/ProductManagement "feature bloat" OR "killed features"`
- Search: `site:reddit.com/r/SaaS "positioning" "jobs to be done"`
- Look for: AMAs from successful founders, "postmortem" posts
- Best sorting: Top → Past Year for current practices
- Watch for: Real numbers (usage %, revenue impact) not vague "it worked"

**When you need specific expertise**:
- **User research**: UXPA, ResearchOps community
- **Pricing/monetization**: Price Intelligently community, Patrick Campbell's stuff
- **B2B specifically**: SaaStr community (but filter the sales noise)
- **Consumer specifically**: Reforge community (alumni only, but worth it)

**Where the best insights hide**:
- **Company blog post comments** (Intercom, Basecamp, Linear) - Real debates about tradeoffs
- **Twitter threads from founders** who've actually killed features - search "killed feature" or "removed feature"

## Educational Background

**Required:**
- Talked to actual users (not just read feedback)
- Shipped features that nobody used (painful learning)
- Understanding of product/market fit vs. growth stage

**Helpful:**
- Marketing (positioning, differentiation)
- UX research (interview techniques, bias awareness)
- Business model understanding (how money flows)

## Hardware Requirements
None. Maybe a whiteboard.

## CLI Tools for Autonomous Delivery

**Required tools:**
- `jq` - Parse analytics JSON exports, user feedback data
- `sqlite3` - Query local analytics databases
- `csvkit` - Process CSV exports from analytics tools
- `git` - Track feature addition history, correlate with metrics

**Optional tools:**
- `gh` - Pull GitHub issues/discussions for feature requests
- `datadog-cli` or similar - Pull usage metrics directly
- `notion-cli` or similar - Extract product docs/requirements
- `fzf` - Interactive feature selection/filtering

**Installation:**
```bash
# Required
brew install jq sqlite csvkit  # macOS
apt install jq sqlite3 csvkit  # Linux

# Optional
brew install gh fzf
```

**Health check:**
```bash
./scripts/check_subagent_tools.sh find_core_value
```

**Autonomous usage pattern:**
```bash
# Extract feature list from git history
git log --all --pretty=format:"%s" --grep="feat:" > features.txt

# Parse analytics export
jq '.events[] | select(.event_name == "feature_used") | .properties' \
  analytics_export.json > feature_usage.json

# Correlate features with usage
jq -s 'group_by(.feature_name) | 
       map({feature: .[0].feature_name, count: length})' \
  feature_usage.json > usage_analysis.json

# Generate feature-to-job mapping (requires LLM)
# Artifacts: usage_analysis.json, features.txt
# Deliverable: job_statement.md, keep_kill_list.md
```

## LLM Configuration

**Ideal model:** `claude-sonnet-4-5-20250929` (as of 2025-11-01)

**Why this model:**
- **Jobs-to-be-done reasoning** - Understands user motivation, not just stated needs
- **Pattern recognition** - Finds the underlying job across disparate features
- **Strategic thinking** - Balances qualitative insight with quantitative data
- **Communication clarity** - Produces clear positioning statements

**Minimum requirements:**
- Context window: 50K tokens (feature lists + user feedback + usage data)
- Reasoning capability: Must understand abstract jobs from concrete features
- Speed: <60s for analysis (not urgent, quality matters)
- Cost: ~$2-4 per analysis acceptable (high-leverage strategic work)

**Model fallbacks:**
1. Primary: `claude-sonnet-4-5-20250929` - Best at strategic abstraction
2. Secondary: `gpt-4o-2024-08-06` - Good pattern recognition, slightly weaker strategy
3. Minimum: `claude-sonnet-4-20250514` - Acceptable but less nuanced on jobs-to-be-done

**Model check script:**
```bash
./scripts/check_model_currency.sh find_core_value
```

**Review schedule:**
- Check model currency: Every 3 months
- Last reviewed: 2025-11-01
- Next review: 2026-02-01

**Performance benchmarks:**
Track these to know if model needs updating:
- **Job clarity**: Target clear one-sentence statement 90% of time - Actual: TBD
- **Feature classification accuracy**: Target 85% agreement with team - Actual: TBD
- **Contrarian insights**: Target 2+ non-obvious insights per analysis - Actual: TBD
- **Actionability**: Target: stakeholders can act within 1 day - Actual: TBD

If team starts questioning recommendations regularly, trigger model review.

**When to upgrade model:**
- New model better at strategic abstraction (test on sample features)
- Current model's recommendations consistently off-target
- New model at comparable cost but faster (lets you iterate more)

## When NOT to Use
- Pre-launch (you don't have enough data yet)
- When you're actually nailing one job (don't overthink it)
- When the problem is execution, not strategy
- When you're using this to avoid hard conversations

## Collaborates With

**Upstream** (depends on these subagents):
- `extract_user_jobs.md` - Provides: Raw job insights from interviews/data
- `map_competitive_landscape.md` - Provides: What jobs competitors own
- `analyze_usage_patterns.md` - Provides: What users actually do vs. say

**Downstream** (feeds into these subagents):
- `surface_hidden_costs.md` - Consumes: List of features to cost-analyze
- `design_minimal_viable_test.md` - Consumes: Core job hypothesis to validate
- `communicate_tough_decisions.md` - Consumes: Feature kill list with rationale
- `rewrite_positioning.md` - Consumes: Clear job statement for messaging

**Parallel** (runs alongside, shares context):
- `identify_leverage_points.md` - Coordinates: What 20% creates 80% of value?
- `assess_market_timing.md` - Coordinates: Is this the right job for right now?

**Conflicts With** (don't run together):
- `add_feature_parity.md` - Because: This kills features; that adds them
- `please_all_stakeholders.md` - Because: This makes hard choices; that appeases everyone

## Example Integration

Combine with:
- `surface_hidden_costs.md` - Calculate cost of maintaining bloat
- `communicate_tough_decisions.md` - Tell stakeholders why we're killing their pet feature
- `design_minimal_viable_test.md` - Validate the "one job" hypothesis

Workflow:
1. This subagent identifies the core job and bloat
2. `surface_hidden_costs.md` quantifies maintenance burden
3. `design_minimal_viable_test.md` tests if users care about the features we're cutting
4. `communicate_tough_decisions.md` handles the internal politics

## Success Metrics
- Can you explain your product in one "when [situation], I use [product] to [job]" statement?
- Did usage/engagement of core features increase after cutting?
- Did development velocity increase (less maintenance)?
- Are support tickets about edge cases decreasing?
- Can new team members understand what you do in <5 minutes?
