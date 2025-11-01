# Scripts

Utilities for managing and monitoring subagents.

## Health Checks

### check_subagent_tools.sh
Verifies all required CLI tools for a subagent are installed and working.

**Usage:**
```bash
./scripts/check_subagent_tools.sh [subagent_name]
```

**What it checks:**
- Required tools are installed
- Tools are executable
- Basic functionality works

**Example:**
```bash
./scripts/check_subagent_tools.sh challenge_technical_assumptions
```

**When to run:**
- Before first use of a subagent
- After system upgrades
- When subagent fails unexpectedly
- In CI/CD pipelines

### check_model_currency.sh
Checks if the LLM assigned to a subagent is still relevant and up-to-date.

**Usage:**
```bash
./scripts/check_model_currency.sh [subagent_name]
```

**What it checks:**
- Current model assignment
- Last review date (flags if >90 days)
- Model information from registry
- Recommendations for updates

**Example:**
```bash
./scripts/check_model_currency.sh find_core_value
```

**When to run:**
- Every 3 months (scheduled)
- When performance degrades
- When new models released
- When benchmarks drop

### check_llm_leaderboards.sh
Checks LLM leaderboards for models best suited to specific job types.

**Usage:**
```bash
./scripts/check_llm_leaderboards.sh [job_type]
```

**Job types:**
- `technical_reasoning` - Deep multi-step technical analysis
- `product_strategy` - Strategic product decisions
- `code_generation` - Writing/debugging code
- `math_reasoning` - Mathematical problem solving
- `creative_writing` - Content generation
- `general` - General purpose tasks

**What it shows:**
- Relevant leaderboards for this job
- Current top models
- Key benchmarks to check
- URLs to visit

**Example:**
```bash
./scripts/check_llm_leaderboards.sh technical_reasoning
```

**When to run:**
- Every 3 months (with model currency check)
- When selecting initial model for new subagent
- When current model underperforms

## Model Registry

`model_registry.json` tracks known models and their characteristics.

**Structure:**
```json
{
  "models": {
    "model-name": {
      "released": "YYYY-MM-DD",
      "context_window": 200000,
      "notes": "Current best for X"
    }
  },
  "recommendations": {
    "use_case": "recommended-model"
  }
}
```

**Update this when:**
- New models release
- Model capabilities change
- You benchmark a model

## Adding New Scripts

When you create a new script:

1. **Follow the template:**
```bash
#!/usr/bin/env bash
# script_name.sh
#
# What: [One sentence description]
# Why: [The problem this solves]
# Usage: ./scripts/script_name.sh [args]

set -euo pipefail
```

2. **Make it executable:**
```bash
chmod +x scripts/script_name.sh
```

3. **Add to this README:**
Update the relevant section with usage and examples.

4. **Test it:**
Run it at least 3 times before committing.

## Common Patterns

### Error Handling
```bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures
```

### Color Output
```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'  # No Color

echo -e "${GREEN}✓${NC} Success message"
echo -e "${RED}✗${NC} Error message"
```

### Argument Parsing
```bash
SUBAGENT_NAME="${1:-}"

if [[ -z "$SUBAGENT_NAME" ]]; then
    echo "Usage: $0 [subagent_name]"
    exit 1
fi
```

### File Location
```bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
```

## Dependencies

Scripts assume these are available:
- bash 4+
- jq (JSON processing)
- git (version control)

Optional but useful:
- gh (GitHub CLI)
- curl (HTTP requests)

Check for dependencies:
```bash
if ! command -v jq &> /dev/null; then
    echo "jq is required but not installed"
    exit 1
fi
```

## Testing Scripts

Before committing:

1. **Test success case** - Normal execution works
2. **Test failure case** - Handles errors gracefully
3. **Test missing args** - Shows usage message
4. **Test missing tools** - Detects and reports missing dependencies

## Catalog

- `check_subagent_tools.sh` - Verify CLI tool availability
- `check_model_currency.sh` - Check LLM assignment currency
- `check_llm_leaderboards.sh` - Find best models for job types
- `model_registry.json` - Model information database

*Add your scripts here as you create them*
