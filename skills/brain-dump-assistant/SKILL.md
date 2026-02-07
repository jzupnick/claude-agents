---
name: brain-dump-assistant
description: Interactive assistant for organizing and processing Obsidian brain dumps in the root folder
---

# Brain Dump Assistant

**Purpose:** Help you process, tag, and organize the notes you've captured in your Obsidian vault root folder.

## When to Use

Use this skill when:
- You have accumulated untagged notes in your vault root
- Weekly/monthly review time
- Before starting a new project (clean slate)
- When your root folder feels cluttered

## How It Works

The assistant will:

1. **Scan** your vault root for recent notes
2. **Categorize** them by analyzing filenames and content
3. **Suggest** appropriate tags and locations
4. **Execute** moves and tag additions with your approval

## Process Flow

### Phase 1: Discovery
```bash
# Find recent untagged/unorganized notes
cd ~/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/notes
find . -maxdepth 1 -name "*.md" -type f -mtime -30 ! -name "*MOC.md"
```

### Phase 2: Categorization

For each note, determine:

**Category by Filename Patterns:**
- Recipes: `*recipe*`, `*food*`, `*breakfast*`, `*meal*`, `*salad*`, `*soup*`
- Health: `*health*`, `*medical*`, `*doctor*`, `*prescription*`, `*vaccine*`
- Financial: `*tax*`, `*investment*`, `*portfolio*`, `*401k*`, `*loan*`
- Home: `*manual*`, `*repair*`, `*maintenance*`, `*deck*`, `*garage*`
- Parenting: `*baby*`, `*parenting*`, `*child*`, `*daycare*`
- Books: Author format (`Lastname-BookTitle.md`), `*-book*.md`
- Tech: `*setup*`, `*guide*`, `*API*`, `*code*`, `*github*`
- Projects: `AlertBoss*`, `AI*Constellation*`, project-specific keywords

**Tag Mapping:**
```
Recipe → [area/life, recipe]
Health → [area/life, health]
Financial → [area/finance]
Home → [area/life, home]
Parenting → [area/life, parenting]
Book → [area/learning, book]
Tech → [area/tech]
Project-specific → [project/name]
```

### Phase 3: Actions

Present options for each note:

1. **Tag in place** - Add appropriate tags, keep in root
2. **Move to project** - Relocate to `Projects/[name]/`
3. **Archive** - Move to `Archive/` if old/complete
4. **Delete** - Remove if obsolete/duplicate

### Phase 4: Execution

After user approval:
- Batch update tags using mcp__obsidian__patch_note
- Move files using mcp__obsidian__move_note
- Confirm changes

## Usage Example

```
User: "Run brain dump assistant"
Agent: "I'll scan your vault root for brain dumps..."
[Analyzes files]

Agent: "Found 15 untagged notes from the last 30 days:

Recipes (5):
- Apple Cinnamon Chia Pudding.md
- DASH Breakfast.md
Action: Tag with [area/life, recipe] ✓

Health (3):
- 2023 eyeglass rx prescription.md
- Bloodwork.md  
Action: Tag with [area/life, health] ✓

Project Files (2):
- AlertBoss Strategy Notes.md
Action: Move to Projects/AlertBoss/ ✓

... (showing all categories)

Proceed with these actions? [Y/n]"
```

## Tag Standards

**Primary Category Tags:**
- `area/life` - Personal life (health, home, family)
- `area/finance` - Money, investments, taxes
- `area/tech` - Technical notes, code, setups
- `area/learning` - Books, courses, education
- `project/[name]` - Project-specific work

**Secondary Tags (add detail):**
- `recipe`, `health`, `home`, `parenting`
- `book`, `article`, `course`
- `reference`, `guide`, `manual`

## Best Practices

### DO:
✅ Tag notes as soon as you create them (if possible)
✅ Use 2-3 tags max per note (category + specifics)
✅ Keep frequently-accessed notes in root
✅ Move project work to project folders
✅ Archive completed work regularly

### DON'T:
❌ Over-tag (more tags = harder to find)
❌ Use single-use tags (if only 1 note has it, remove it)
❌ Leave old brain dumps unprocessed for >90 days
❌ Move everything to folders (root is fine for reference)

## Automation

The weekly brain dump review script runs every Sunday at 9 AM:
```bash
# Manual run:
~/.local/bin/organize-brain-dumps.sh 7

# View results:
cat /tmp/brain-dump-review.log
```

## Integration with Other Skills

- **After brainstorming** - Tag outputs and move to appropriate locations
- **After writing-plans** - Tag plan documents with project tags
- **Before code review** - Ensure project files are in correct folders

---

*This skill helps maintain the vault's flat structure while keeping it discoverable through tags.*
