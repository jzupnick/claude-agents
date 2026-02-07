#!/bin/bash
# Patch the Zed Claude Code ACP adapter to auto-load plugins from installed_plugins.json
# Re-run this after Zed updates the adapter

ACP_DIR="$HOME/Library/Application Support/Zed/external_agents/claude-code-acp"
LATEST=$(ls -1 "$ACP_DIR" 2>/dev/null | sort -V | tail -1)

if [ -z "$LATEST" ]; then
  echo "Error: Claude Code ACP adapter not found"
  exit 1
fi

TARGET="$ACP_DIR/$LATEST/node_modules/@zed-industries/claude-code-acp/dist/acp-agent.js"

if [ ! -f "$TARGET" ]; then
  echo "Error: acp-agent.js not found at $TARGET"
  exit 1
fi

if grep -q '_autoPlugins' "$TARGET"; then
  echo "Already patched (version $LATEST)"
  exit 0
fi

cp "$TARGET" "$TARGET.bak"

# Use Python for reliable patching
python3 -c "
import re

with open('$TARGET') as f:
    content = f.read()

# Insert plugin loading code before 'Configure thinking tokens'
patch_code = '''        // Auto-load enabled local plugins from installed_plugins.json
        const _autoPlugins = (() => {
            try {
                const pluginsFile = path.join(os.homedir(), \".claude\", \"plugins\", \"installed_plugins.json\");
                const settingsFile = path.join(os.homedir(), \".claude\", \"settings.json\");
                if (!fs.existsSync(pluginsFile) || !fs.existsSync(settingsFile)) return [];
                const installed = JSON.parse(fs.readFileSync(pluginsFile, \"utf-8\"));
                const settings = JSON.parse(fs.readFileSync(settingsFile, \"utf-8\"));
                const enabled = settings.enabledPlugins || {};
                const plugins = [];
                for (const [id, entries] of Object.entries(installed.plugins || {})) {
                    if (!enabled[id]) continue;
                    const entry = Array.isArray(entries) ? entries[0] : entries;
                    if (entry?.installPath && fs.existsSync(entry.installPath))
                        plugins.push({ type: \"local\", path: entry.installPath });
                }
                return plugins;
            } catch (e) { return []; }
        })();
'''

content = content.replace(
    '        // Configure thinking tokens from environment variable',
    patch_code + '        // Configure thinking tokens from environment variable',
    1
)

# Add plugins spread to options
content = content.replace(
    'settingSources: [\"user\", \"project\", \"local\"],',
    'settingSources: [\"user\", \"project\", \"local\"],\n            ...(_autoPlugins.length > 0 && { plugins: _autoPlugins }),',
    1
)

with open('$TARGET', 'w') as f:
    f.write(content)

print(f'Patched successfully')
"

echo "Patched Claude Code ACP adapter v$LATEST"
echo "Restart Zed to apply changes"
