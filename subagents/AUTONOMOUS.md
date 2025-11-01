# Autonomous Subagent Delivery

How to make subagents that can run without human babysitting.

## The Goal

**Bad:** Subagent needs constant human input, can't make progress alone.
**Good:** Subagent accepts input, processes autonomously, delivers artifacts/deliverables.

## Three Requirements

### 1. CLI Tools (Hands)
Subagent needs tools to gather data, process it, output results.

### 2. LLM Configuration (Brain)
Subagent needs the right model for its specific job.

### 3. Health Checks (Self-Awareness)
Subagent checks if its tools and model are still working/relevant.

## CLI Tools: What Subagents Need

### Required vs Optional

**Required:** Subagent fails without these.
- Example: `jq` for parsing JSON artifacts
- Example: `git` for accessing codebase history

**Optional:** Subagent works but is enhanced by these.
- Example: `gh` for richer GitHub context
- Example: `fzf` for interactive selection

### Common Tool Categories

**Data gathering:**
- `curl` - Fetch URLs, test APIs
- `git` - Access version history
- `gh` - Query GitHub issues/PRs
- Analytics CLIs - Pull metrics

**Data processing:**
- `jq` - JSON manipulation
- `csvkit` - CSV processing
- `sqlite3` - Local data querying
- `yq` - YAML manipulation

**Code analysis:**
- `grep/ripgrep` - Pattern searching
- `cloc/tokei` - Code metrics
- `ast-grep` - AST-level searching
- Language-specific analyzers

**Testing/Validation:**
- `shellcheck` - Bash linting
- `yamllint` - YAML validation
- `jsonlint` - JSON validation
- Domain-specific validators

### Autonomous Usage Pattern

The key: Chain tools to go from input → artifacts → deliverables without human intervention.

**Example pattern:**
```bash
# 1. Gather data
curl -s https://api.example.com/data | jq '.' > raw_data.json

# 2. Process data
jq '.items[] | select(.active == true)' raw_data.json > filtered.json

# 3. Analyze (with LLM)
cat filtered.json | llm-cli analyze --model claude-sonnet-4-5 > analysis.json

# 4. Generate deliverable
jq -r '.recommendations[]' analysis.json > recommendations.md
```

**Without humans:** All steps execute automatically.
**With humans:** Only if process fails or needs validation.

## LLM Configuration: Matching Model to Job

### Why This Matters

Different jobs need different model capabilities:
- **Deep reasoning** (technical assumptions) → Claude Sonnet 4.5
- **Fast iteration** (code generation) → Claude Sonnet 4 or GPT-4o
- **Strategic thinking** (product strategy) → Claude Sonnet 4.5
- **Cheap/fast** (simple parsing) → Haiku or GPT-4o-mini

**Wrong model = subagent underperforms.**

### Model Selection Criteria

**Context window:**
- How much data does subagent need to process?
- Technical doc + code samples → Need 100K+ tokens
- Simple feature list → Can work with 20K tokens

**Reasoning capability:**
- Pre-mortem analysis → Needs multi-step reasoning
- Simple classification → Basic pattern matching OK

**Speed requirements:**
- Real-time feedback → Need fast model (<5s)
- Strategic analysis → Can wait 30-60s for quality

**Cost tolerance:**
- High-value, infrequent → Can pay $5-10 per run
- High-frequency automation → Need cheap model

### Model Fallback Strategy

Always define fallbacks:

1. **Primary:** Best model for the job
2. **Secondary:** Acceptable alternative if primary unavailable
3. **Minimum:** Degraded but functional

**Example:**
```
Primary: claude-sonnet-4-5 (best reasoning)
Secondary: claude-sonnet-4 (slightly weaker)
Minimum: gpt-4o (acceptable but misses edge cases)
```

**Why:** Production systems need resilience.

### Performance Benchmarks

Track specific metrics to know if model degrades:

**For technical reasoning:**
- Assumption detection rate (target: 95%)
- False positive rate (target: <10%)
- Edge case coverage (target: 80% of prod issues)

**For product strategy:**
- Job clarity (target: clear statement 90% of time)
- Feature classification accuracy (target: 85% team agreement)
- Actionability (target: stakeholders act within 1 day)

**When benchmarks drop:** Trigger model review.

## Health Checks: Staying Current

### Two Types of Checks

**1. Tool Check** (`check_subagent_tools.sh`)
- Are required tools installed?
- Are they working correctly?
- What's missing?

**2. Model Check** (`check_model_currency.sh`)
- Is assigned model still relevant?
- When was it last reviewed?
- Are newer alternatives available?
- Do benchmarks suggest degradation?

### When to Run Checks

**Tool checks:**
- Before first use (setup)
- After system upgrades
- When subagent fails unexpectedly
- In CI/CD for deployed subagents

**Model checks:**
- Every 3 months (scheduled)
- When performance degrades
- When new models released
- When benchmarks drop below targets

### Review Schedule

**Every 3 months:**
1. Run `check_model_currency.sh`
2. Review performance benchmarks
3. Test new models on sample inputs
4. Update model if >10% improvement found
5. Update "Last reviewed" date

**Between reviews:**
1. Monitor performance metrics
2. Trigger early review if degradation detected
3. Test new major model releases as they drop

## Making Subagents Autonomous

### Pattern 1: Batch Processing

**Job:** Analyze 100 PRs for risk.

**Autonomous flow:**
```bash
# List all PRs
gh pr list --json number,title,author > prs.json

# For each PR, run risk analysis
jq -r '.[] | .number' prs.json | while read pr; do
  gh pr view $pr --json files,body > pr_${pr}.json
  
  # LLM analyzes
  cat pr_${pr}.json | \
    llm-cli analyze-risk \
      --model claude-sonnet-4-5 \
      --output risk_${pr}.json
done

# Aggregate results
jq -s '.' risk_*.json > all_risks.json

# Generate deliverable
jq -r 'sort_by(.risk_score) | reverse | 
       .[] | "PR #\(.pr_number): \(.risk_level) - \(.summary)"' \
  all_risks.json > risk_report.md
```

**Human involvement:** Review final report, not each PR.

### Pattern 2: Event-Driven

**Job:** Flag risky deployments in CI/CD.

**Autonomous flow:**
```yaml
# In CI/CD pipeline
- name: Risk Assessment
  run: |
    # Gather context
    git diff origin/main...HEAD > changes.diff
    git log origin/main...HEAD --oneline > commits.txt
    
    # Run subagent
    ./scripts/assess_deployment_risk.sh \
      --changes changes.diff \
      --commits commits.txt \
      --model claude-sonnet-4-5 \
      --output risk_assessment.json
    
    # Check result
    risk_level=$(jq -r '.risk_level' risk_assessment.json)
    if [ "$risk_level" == "high" ]; then
      echo "::warning::High risk deployment detected"
      jq -r '.concerns[]' risk_assessment.json
      exit 1
    fi
```

**Human involvement:** Only when risk detected.

### Pattern 3: Scheduled Analysis

**Job:** Weekly product strategy review.

**Autonomous flow:**
```bash
# Cron job runs weekly
# 0 9 * * 1 /path/to/weekly_review.sh

# Gather last week's data
start_date=$(date -d '1 week ago' +%Y-%m-%d)
end_date=$(date +%Y-%m-%d)

# Pull analytics
analytics-cli export \
  --start $start_date \
  --end $end_date \
  --format json > weekly_usage.json

# Pull feature requests
gh issue list \
  --label "feature-request" \
  --created ">$start_date" \
  --json title,body,comments > feature_requests.json

# Run strategy analysis
cat weekly_usage.json feature_requests.json | \
  llm-cli analyze-strategy \
    --model claude-sonnet-4-5 \
    --output strategy_insights.json

# Generate deliverable
jq -r '.summary' strategy_insights.json > weekly_insights.md

# Send to stakeholders
mail -s "Weekly Product Insights" team@company.com < weekly_insights.md
```

**Human involvement:** Read report, decide on actions.

## Monitoring Autonomous Subagents

### What to Track

**Performance metrics:**
- Execution time (is it getting slower?)
- Success rate (how often does it complete?)
- Artifact quality (are outputs useful?)
- Deliverable actionability (do people act on them?)

**Resource usage:**
- API calls (cost tracking)
- Token consumption (cost tracking)
- Compute time (efficiency)

**Model performance:**
- Benchmark scores (degradation detection)
- Human feedback (quality assessment)
- Error rates (failure patterns)

### When to Intervene

**Automated alerts:**
- Execution failures (can't complete)
- Performance degradation (>50% slower)
- Cost spikes (>2x expected)
- Benchmark drops (>20% decrease)

**Manual reviews:**
- Every 3 months (scheduled)
- After major changes (model updates, tool changes)
- When team questions outputs (trust erosion)

## Example: Fully Autonomous Subagent

See `subagents/examples/challenge_technical_assumptions.md`:

**Has CLI tools:**
- git, jq, curl, grep (required)
- gh, cloc, tokei (optional)
- Health check script

**Has LLM config:**
- Primary: claude-sonnet-4-5 (deep reasoning)
- Fallbacks: claude-sonnet-4, gpt-4o
- Review schedule: Every 3 months
- Benchmarks: Detection rate, false positives, edge cases

**Autonomous usage:**
```bash
# Runs without human intervention
./scripts/assess_technical_assumptions.sh \
  --proposal architecture_proposal.md \
  --codebase . \
  --model claude-sonnet-4-5 \
  --output assessment.json

# Produces artifacts (for other subagents)
# assessment.json: Full analysis with scores

# Produces deliverable (for humans)
# recommendations.md: Clear go/no-go + rationale
```

## Your Challenge

Pick one subagent. Make it autonomous:

1. **List required tools** - What CLI tools does it need?
2. **Define LLM config** - Which model? Why? Fallbacks?
3. **Set benchmarks** - How do you know if it's working well?
4. **Write usage pattern** - Show the autonomous flow (input → output)
5. **Test it** - Run without human intervention. Did it work?

If it can't run autonomously, it's not ready. Fix the gaps first.

What subagent are you making autonomous first?
