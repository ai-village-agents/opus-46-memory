#!/bin/bash
# Auto-generates memory-index.md from repo contents
# Usage: bash /tmp/opus-46-memory/scripts/rebuild-index.sh
REPO="/tmp/opus-46-memory"
cd "$REPO"

echo "# Memory Index"
echo "Last updated: $(date +%Y-%m-%d)"
echo ""
echo "| File | Size | Last Modified |"
echo "|------|------|---------------|"

# MD files (excluding index itself)
for f in $(find . -name "*.md" -not -path "./.git/*" -not -name "memory-index.md" | sort); do
    NAME=$(echo "$f" | sed 's|./||')
    SIZE=$(wc -c < "$f" | tr -d ' ')
    MOD=$(git log -1 --format="%cr" -- "$f" 2>/dev/null || echo "unknown")
    echo "| $NAME | ${SIZE}c | $MOD |"
done

# Scripts and tools
for f in $(find ./scripts -type f 2>/dev/null | sort) $(find . -maxdepth 1 -name "*.sh" | sort); do
    NAME=$(echo "$f" | sed 's|./||')
    SIZE=$(wc -c < "$f" | tr -d ' ')
    MOD=$(git log -1 --format="%cr" -- "$f" 2>/dev/null || echo "unknown")
    echo "| $NAME | ${SIZE}c | $MOD |"
done

# YAML
for f in $(find . -maxdepth 1 -name "*.yaml" | sort); do
    NAME=$(echo "$f" | sed 's|./||')
    SIZE=$(wc -c < "$f" | tr -d ' ')
    MOD=$(git log -1 --format="%cr" -- "$f" 2>/dev/null || echo "unknown")
    echo "| $NAME | ${SIZE}c | $MOD |"
done

echo ""
echo "## Quick Access"
echo '```bash'
echo 'bash /tmp/opus-46-memory/session-startup.sh          # Session start'
echo 'bash /tmp/opus-46-memory/scripts/audit-memory.sh     # Health check'
echo 'bash /tmp/opus-46-memory/scripts/pre-send-chat.sh "purpose" "recipient" "dup-check"'
echo 'bash /tmp/opus-46-memory/scripts/pre-consolidate.sh  # Before consolidate'
echo 'bash /tmp/opus-46-memory/session-save.sh "message"   # Save to GitHub'
echo 'bash /tmp/opus-46-memory/search-memory.sh "query"    # Search all files'
echo 'bash /tmp/opus-46-memory/scripts/render-bootloader.sh "goal" "day"  # Generate consolidation memory'
echo 'bash /tmp/opus-46-memory/scripts/check-staleness.sh 419  # Check for stale items'
echo 'bash /tmp/opus-46-memory/scripts/rebuild-index.sh > memory-index.md  # Regenerate index'
echo '```'
