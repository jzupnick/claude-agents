---
name: webapp-testing
description: Test local web applications using Playwright with Python. Use for UI verification, browser automation, and debugging web apps.
---

# Web Application Testing

## Decision Tree

1. **Static HTML?** → Read file directly
2. **Dynamic app?** → Use server management + Playwright

## Key Helper

Use `scripts/with_server.py` for automatic server lifecycle management.
Supports single or multiple concurrent servers.

## Critical Pattern

**Reconnaissance precedes action.**

```python
# ALWAYS wait for network idle before inspecting DOM
await page.wait_for_load_state('networkidle')
```

Inspecting before idle causes selector discovery failures on dynamic content.

## Essential Practices

- Launch Chromium in headless mode
- Use descriptive selectors:
  - `text=Submit`
  - `role=button`
  - CSS selectors
  - IDs
- Close browsers when finished
- Inspect rendered state before identifying selectors

## Common Workflow

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:3000')
    page.wait_for_load_state('networkidle')

    # Now safe to interact
    page.click('text=Submit')

    browser.close()
```

## Common Mistake

❌ Inspecting DOM before network idle
✅ Always wait for `networkidle` first
