#!/usr/bin/env python3
"""
Import gist-sourced assistants into agent-skills plugin format.

Downloads two Cherry Studio JSON gists, deduplicates, and generates
a SKILL.md for each unique assistant.

Usage:
    python3 scripts/import-gist-assistants.py [--dry-run]
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent / "skills"

GIST_280 = "ecd46461ff8da95ae4dcff4990ed651e"
GIST_210 = "e7f2fb8be94b2e550c25fbbb8eca2934"

# Category prefix mapping for the 280-expert collection
GROUP_PREFIX_MAP = {
    ("Development", "Backend"): "dev-backend",
    ("Development", "Frontend"): "dev-frontend",
    ("Development", "Cloud/DevOps"): "dev-infra",
    ("Development", "Cloud", "DevOps"): "dev-infra",
    ("Development", "Mobile"): "dev-mobile",
    ("Development", "Security"): "dev-security",
    ("Development", "Testing"): "dev-testing",
    ("Business", "Product"): "biz-product",
    ("Business", "Strategy"): "biz-strategy",
    ("Business", "Communication"): "biz-comm",
    ("Data", "Analysis", "AI"): "data",
    ("Data", "Analysis", "Visualization"): "data-viz",
    ("AI", "Development"): "ai",
    ("Design", "UX"): "design",
    ("Cloud", "Architecture"): "cloud",
    ("Writing", "Documentation"): "writing",
}


def kebab_case(name: str) -> str:
    """Convert a name to kebab-case."""
    s = re.sub(r"[^a-zA-Z0-9\s-]", "", name.strip())
    s = re.sub(r"[\s_]+", "-", s)
    return s.lower().strip("-")


def get_group_prefix(group: list) -> str:
    """Map a group array to a category prefix."""
    # Try exact match first
    key = tuple(group)
    if key in GROUP_PREFIX_MAP:
        return GROUP_PREFIX_MAP[key]

    # Try without 'Free' prefix (LiteLLM collection uses Free/X)
    cleaned = [g for g in group if g != "Free"]
    if cleaned:
        key = tuple(cleaned)
        if key in GROUP_PREFIX_MAP:
            return GROUP_PREFIX_MAP[key]

    # Fallback: use first meaningful group element
    for g in cleaned or group:
        g_lower = g.lower().replace("/", "-")
        if g_lower not in ("free",):
            return kebab_case(g_lower)

    return "general"


def extract_keywords(prompt: str, name: str) -> list:
    """Extract key domain words from the prompt for the description."""
    # Common filler words to skip
    stop = {
        "you", "are", "a", "an", "the", "and", "or", "with", "for", "in",
        "of", "to", "on", "is", "that", "this", "be", "as", "at", "by",
        "it", "from", "your", "their", "expert", "senior", "provide",
        "clear", "accurate", "actionable", "responses", "tailored",
        "task", "hand", "experience", "years", "write", "clean",
        "efficient", "code", "following", "best", "practices", "explain",
        "approach", "working", "solutions", "proper", "error", "handling",
    }
    words = re.findall(r"\b[a-zA-Z]{3,}\b", prompt.lower())
    seen = set()
    keywords = []
    for w in words:
        if w not in stop and w not in seen:
            seen.add(w)
            keywords.append(w)
        if len(keywords) >= 5:
            break
    return keywords


def build_description(name: str, prompt: str, group: list) -> str:
    """Generate a trigger-phrase description from the assistant info."""
    # Extract first meaningful sentence from prompt
    first_sentence = ""
    for line in prompt.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("-"):
            # Remove "You are a/an..." prefix
            cleaned = re.sub(
                r"^You are (?:a |an )?(?:senior |expert )?", "", line
            )
            if cleaned and len(cleaned) > 10:
                first_sentence = cleaned.rstrip(".")
                break

    keywords = extract_keywords(prompt, name)
    domain = " ".join(keywords[:3]) if keywords else name.lower()

    if first_sentence and len(first_sentence) < 120:
        return (
            f"Use when you need expert guidance on {domain}. "
            f"{first_sentence}."
        )
    else:
        group_str = "/".join(group) if group else "general"
        return (
            f"Use when you need expert guidance on {domain}. "
            f"Domain: {group_str}."
        )


def rewrite_to_imperative(prompt: str) -> str:
    """Rewrite 'You are a...' style prompts to imperative form."""
    lines = prompt.strip().split("\n")
    result = []
    for line in lines:
        # "You are a X" -> "Act as a X" (only first occurrence)
        if line.strip().startswith("You are"):
            line = re.sub(r"^(\s*)You are", r"\1Act as", line)
        result.append(line)
    return "\n".join(result)


def generate_skill_md(name: str, prompt: str, group: list) -> str:
    """Generate a complete SKILL.md for an assistant."""
    skill_name = kebab_case(name)
    description = build_description(name, prompt, group)
    body = rewrite_to_imperative(prompt)

    return f"""---
name: {skill_name}
description: {description}
---

# {name}

{body}
"""


def download_gist(gist_id: str, filename: str) -> list:
    """Download and parse a gist JSON file."""
    result = subprocess.run(
        ["gh", "gist", "view", gist_id, "-f", filename],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"Error downloading gist {gist_id}: {result.stderr}")
        sys.exit(1)
    return json.loads(result.stdout)


def load_existing_skills() -> set:
    """Get set of existing skill directory names (Part A hand-crafted)."""
    if not SKILLS_DIR.exists():
        return set()
    return {
        d.name for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    }


def main():
    dry_run = "--dry-run" in sys.argv

    print("Downloading gist: 280 Expert Assistants...")
    gist_280 = download_gist(GIST_280, "assistants-optimized.json")
    print(f"  Found {len(gist_280)} assistants")

    print("Downloading gist: LiteLLM Subscription Assistants...")
    gist_210 = download_gist(GIST_210, "cherry-studio-assistants.json")
    print(f"  Found {len(gist_210)} assistants")

    # Build unified list, dedup by kebab name
    # Prefer 280-expert version (richer prompts) over LiteLLM version
    seen_names = {}

    for assistant in gist_280:
        name = assistant["name"]
        kname = kebab_case(name)
        group = assistant.get("group", [])
        if isinstance(group, str):
            group = [group]
        prefix = get_group_prefix(group)
        skill_dir_name = f"{prefix}-{kname}" if prefix != "general" else kname
        seen_names[kname] = {
            "name": name,
            "prompt": assistant["prompt"],
            "group": group,
            "dir_name": skill_dir_name,
            "source": "280-expert",
        }

    for assistant in gist_210:
        name = assistant["name"]
        kname = kebab_case(name)
        if kname in seen_names:
            continue  # 280-expert version takes priority
        group = assistant.get("group", [])
        if isinstance(group, str):
            group = [group]
        prefix = get_group_prefix(group)
        skill_dir_name = f"{prefix}-{kname}" if prefix != "general" else kname
        seen_names[kname] = {
            "name": name,
            "prompt": assistant["prompt"],
            "group": group,
            "dir_name": skill_dir_name,
            "source": "litellm-sub",
        }

    # Exclude any that collide with existing hand-crafted skills
    existing = load_existing_skills()
    collisions = []
    for kname, info in list(seen_names.items()):
        if info["dir_name"] in existing:
            collisions.append(info["dir_name"])
            del seen_names[kname]

    print(f"\nDedup results:")
    print(f"  Total unique: {len(seen_names)}")
    print(f"  Collisions with Part A (skipped): {len(collisions)}")
    if collisions:
        print(f"    {', '.join(collisions[:10])}{'...' if len(collisions) > 10 else ''}")

    # Also check for dir_name collisions within gist skills
    dir_names_seen = {}
    deduped = {}
    for kname, info in seen_names.items():
        dn = info["dir_name"]
        if dn in dir_names_seen:
            # Append a suffix
            dn = f"{dn}-2"
            info["dir_name"] = dn
        dir_names_seen[dn] = True
        deduped[kname] = info

    if dry_run:
        print(f"\n[DRY RUN] Would create {len(deduped)} skills")
        for kname, info in sorted(deduped.items()):
            print(f"  {info['dir_name']}/SKILL.md  ({info['source']})")
        return

    # Generate SKILL.md files
    created = 0
    for kname, info in sorted(deduped.items()):
        skill_dir = SKILLS_DIR / info["dir_name"]
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_file = skill_dir / "SKILL.md"

        content = generate_skill_md(info["name"], info["prompt"], info["group"])
        skill_file.write_text(content)
        created += 1

    print(f"\nCreated {created} gist-sourced skills")

    # Summary by source
    from_280 = sum(1 for v in deduped.values() if v["source"] == "280-expert")
    from_210 = sum(1 for v in deduped.values() if v["source"] == "litellm-sub")
    print(f"  From 280-expert: {from_280}")
    print(f"  From LiteLLM: {from_210}")


if __name__ == "__main__":
    main()
