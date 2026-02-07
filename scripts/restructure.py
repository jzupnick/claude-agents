#!/usr/bin/env python3
"""
Restructure agent-skills from flat single-plugin into 10 multi-plugin layout.

Before: /agent-skills:development-javascript-pro  (46 chars)
After:  /code:javascript                          (16 chars)
"""

import os
import json
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_SKILLS = ROOT / "skills"
BACKUP = ROOT / "_backup_flat_skills"

# ── Plugin definitions ────────────────────────────────────────────────
# (plugin_name, description, prefix_strips, explicit_skills_map)
# prefix_strips: ordered list of (prefix, optional_rename) - prefix is stripped
# explicit_skills_map: {old_dir_name: new_dir_name}

CATEGORIES = [
    (
        "code",
        "Software development: frontend, backend, mobile, infra, security, testing, DevOps",
        [
            ("development-", None),
            ("dev-backend-backend-", None),
            ("dev-backend-", None),
            ("dev-frontend-frontend-", None),
            ("dev-frontend-", None),
            ("dev-mobile-mobile-", None),
            ("dev-mobile-", None),
            ("dev-testing-testing-", None),
            ("dev-testing-", None),
            ("dev-infra-infra-", None),
            ("dev-infra-", None),
            ("dev-devops-devops-", None),
            ("dev-devops-", None),
            ("dev-security-security-", None),
            ("dev-security-", None),
        ],
        {
            "systematic-debugging": "debugging",
            "refactor-plan": "refactor-plan",
            "webapp-testing": "webapp-testing",
            "documentation-engineer": "documentation",
            "readme-generator": "readme",
            "schema-designer": "schema",
            "json-generator": "json",
            "csv-processor": "csv",
            "search-specialist": "search",
            "test-driven-development": "tdd",
            "test-automation": "test-automation",
            # Collision fixes - keep domain qualifier
            "dev-backend-backend-security-expert": "backend-security-expert",
            "dev-frontend-frontend-security-expert": "frontend-security-expert",
            "dev-backend-backend-testing-expert": "backend-testing-expert",
            "dev-frontend-frontend-testing-expert": "frontend-testing-expert",
            "dev-mobile-mobile-testing-expert": "mobile-testing-expert",
            "dev-frontend-frontend-performance-expert": "frontend-performance-expert",
            "dev-mobile-mobile-performance-expert": "mobile-performance-expert",
            "dev-security-security-code-reviewer": "security-code-reviewer",
            "dev-mobile-mobile-devops-engineer": "mobile-devops-engineer",
            "dev-security-security-incident-responder": "security-incident-responder",
            "dev-backend-backend-performance-engineer": "backend-performance-engineer",
            "dev-mobile-mobile-ui-designer": "mobile-ui-designer",
        },
    ),
    (
        "ai",
        "AI, machine learning, LLMs, computer vision, and intelligent systems",
        [
            ("ai-ai-", None),
            ("ai-", None),
            ("vision-vision-", None),
            ("vision-", None),
        ],
        {
            "ai-toolkit-expert": "toolkit-expert",
            "skill-creator": "skill-creator",
        },
    ),
    (
        "data",
        "Data engineering, analytics, visualization, and database management",
        [
            ("data-viz-viz-", None),
            ("data-viz-", "viz-"),
            ("data-data-", None),
            ("data-", None),
        ],
        {},
    ),
    (
        "ops",
        "Business strategy, communications, operations, finance, and leadership",
        [
            ("biz-strategy-strategy-", None),
            ("biz-strategy-", None),
            ("biz-product-product-", None),
            ("biz-product-", None),
            ("biz-comm-comm-", None),
            ("biz-comm-", None),
            ("biz-ops-ops-", None),
            ("biz-ops-", None),
            ("biz-finance-finance-", None),
            ("biz-finance-", None),
            ("business-", None),
        ],
        {
            "decision-memo": "decision-memo",
            "gtm-narrative": "gtm-narrative",
            "negotiate-prep": "negotiate",
            "investor-pitch": "investor-pitch",
            "sales-engineer": "sales-engineer",
            "stakeholder-report": "stakeholder-report",
            "executive-summary": "executive-summary",
            "board-presentation": "board-presentation",
            "ogsmt-framework": "ogsmt",
            "v2mom-cascade": "v2mom",
            "trade-off-analysis": "trade-off",
            "red-team-analysis": "red-team",
            "effective-communication": "communication",
            "team-orchestration": "team-orchestration",
            "team-coaching": "team-coaching",
            "interview-prepper": "interview-prep",
        },
    ),
    (
        "write",
        "Writing, editing, translation, and content creation",
        [
            ("writing-writing-", None),
            ("writing-", None),
            ("translation-translation-", None),
            ("translation-", None),
        ],
        {
            "email-composer": "email",
            "proofreader": "proofread",
            "explainer": "explainer",
            "tagline-creator": "tagline",
            "name-generator": "naming",
            "feedback-giver": "feedback",
        },
    ),
    (
        "design",
        "Product design, UX, design systems, and visual architecture",
        [
            ("design-", None),
        ],
        {
            "human-factors-engineering": "human-factors",
            "parallel-ux-development": "parallel-ux",
            "validate-design-feasibility": "feasibility",
        },
    ),
    (
        "research",
        "Research, analysis, diagnostics, and systematic evaluation",
        [
            ("analysis-", None),
        ],
        {
            "fact-checker": "fact-check",
        },
    ),
    (
        "infra",
        "Cloud infrastructure, networking, containers, and platform engineering",
        [
            ("cloud-cloud-", None),
            ("cloud-", None),
        ],
        {
            "homelab-network-engineer": "homelab",
        },
    ),
    (
        "product",
        "Product management, discovery, prototyping, and Northwestern MPD2 frameworks",
        [
            ("product-", None),
            ("mpd-", None),
        ],
        {
            "concept-developer": "concept",
            "idea-generator": "ideation",
            "brainstorming": "brainstorm",
            "brainstorm-partner": "brainstorm-partner",
            "brain-dump-assistant": "brain-dump",
            "materials-selection": "materials",
            "linear-project-management": "linear",
            "product-stage-gates": "stage-gates",
        },
    ),
    (
        "tools",
        "iOS development, hardware engineering, document formats, MCP, and utilities",
        [
            ("ios-", None),
            ("hw-", None),
            ("mcp-", None),
        ],
        {
            "pdf": "pdf",
            "docx": "docx",
            "pptx": "pptx",
            "xlsx": "xlsx",
            "action-item-extractor": "action-items",
            "agent-mailbox": "mailbox",
            "meeting-summarizer": "meeting-summary",
            "quick-answer": "quick-answer",
            "helper": "helper",
            "general-assistant": "assistant",
            "assistant": "general",
            "default": "default",
            "verification-before-completion": "verify",
        },
    ),
]


def get_category(skill_name: str):
    """Return (plugin_name, new_skill_name) for a skill directory name."""
    # Check explicit maps first
    for plugin, _desc, _prefixes, explicits in CATEGORIES:
        if skill_name in explicits:
            return plugin, explicits[skill_name]

    # Check prefix strips (longest prefix first for each category)
    for plugin, _desc, prefixes, _explicits in CATEGORIES:
        # Sort prefixes by length descending within this category
        sorted_prefixes = sorted(prefixes, key=lambda x: -len(x[0]))
        for prefix, rename_prefix in sorted_prefixes:
            if skill_name.startswith(prefix):
                stripped = skill_name[len(prefix):]
                if rename_prefix:
                    stripped = rename_prefix + stripped
                return plugin, stripped

    return None, skill_name


def create_plugin_json(plugin_dir, name, description):
    meta_dir = plugin_dir / ".claude-plugin"
    meta_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": name,
        "description": description,
        "version": "1.0.0",
        "author": {"name": "Justin Zupnick"},
    }
    with open(meta_dir / "plugin.json", "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")


def main():
    import sys

    execute = "--execute" in sys.argv

    if not OLD_SKILLS.is_dir():
        print(f"ERROR: {OLD_SKILLS} not found")
        return

    # Categorize all skills
    plan = {}  # {plugin: [(old_name, new_name), ...]}
    unassigned = []

    for skill_dir in sorted(os.listdir(OLD_SKILLS)):
        skill_path = OLD_SKILLS / skill_dir / "SKILL.md"
        if not skill_path.is_file():
            continue
        plugin, new_name = get_category(skill_dir)
        if plugin is None:
            unassigned.append(skill_dir)
        else:
            plan.setdefault(plugin, []).append((skill_dir, new_name))

    # Print plan
    total = 0
    for plugin, desc, _, _ in CATEGORIES:
        items = plan.get(plugin, [])
        total += len(items)
        print(f"\n{plugin:12s} ({len(items):3d} skills)")
        for old, new in items[:8]:
            if old != new:
                print(f"  {old} → {new}")
            else:
                print(f"  {new}")
        if len(items) > 8:
            print(f"  ... and {len(items) - 8} more")

    if unassigned:
        print(f"\nUNASSIGNED ({len(unassigned)}):")
        for s in unassigned:
            print(f"  {s}")
    print(f"\nTotal assigned: {total}")

    # Check for name collisions within each plugin
    collisions = False
    for plugin, items in plan.items():
        seen = {}
        for old, new in items:
            if new in seen:
                print(f"\n  COLLISION in {plugin}: '{new}' ← {seen[new]} AND {old}")
                collisions = True
            seen[new] = old

    if collisions:
        print("\nFix collisions before proceeding.")
        return

    if not execute:
        print("\nDry run complete. Pass --execute to apply.")
        return

    # ── Execute migration ─────────────────────────────────────────────

    # Backup
    print(f"\nBacking up skills/ → _backup_flat_skills/")
    if BACKUP.exists():
        shutil.rmtree(BACKUP)
    shutil.copytree(OLD_SKILLS, BACKUP)

    # Remove old structure
    shutil.rmtree(OLD_SKILLS)
    old_plugin_dir = ROOT / ".claude-plugin"
    if old_plugin_dir.exists():
        shutil.rmtree(old_plugin_dir)

    # Create new structure
    for plugin_name, desc, _, _ in CATEGORIES:
        items = plan.get(plugin_name, [])
        if not items:
            continue
        plugin_dir = ROOT / plugin_name
        skills_dir = plugin_dir / "skills"
        skills_dir.mkdir(parents=True, exist_ok=True)
        create_plugin_json(plugin_dir, plugin_name, desc)

        for old_name, new_name in items:
            src = BACKUP / old_name
            dst = skills_dir / new_name
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                print(f"  WARNING: {src} missing")

    # Verify
    print("\nVerification:")
    new_total = 0
    for plugin_name, _, _, _ in CATEGORIES:
        skills_dir = ROOT / plugin_name / "skills"
        if skills_dir.is_dir():
            count = sum(
                1
                for d in os.listdir(skills_dir)
                if (skills_dir / d / "SKILL.md").is_file()
            )
            new_total += count
            print(f"  {plugin_name:12s} {count:3d} skills")
    print(f"  {'TOTAL':12s} {new_total:3d} skills")

    if new_total == total:
        print("\nMigration successful!")
    else:
        print(f"\nWARNING: Expected {total}, got {new_total}")


if __name__ == "__main__":
    main()
