#!/bin/bash
# Session Save Script for Claude Opus 4.6
# Usage: bash session-save.sh "commit message"
# Run BEFORE consolidating to persist session learnings to GitHub

echo "=== OPUS 4.6 SESSION SAVE ==="
cd /tmp/opus-46-memory || { echo "❌ Memory repo not found!"; exit 1; }

# Show what changed
echo "Files modified this session:"
git status --short

if [ -z "$(git status --short)" ]; then
    echo "✅ No changes to save."
    exit 0
fi

MSG="${1:-Session update Day $(date +%s)}"
git add -A
git commit -m "$MSG"
git push origin main 2>/dev/null
echo "✅ Memory saved to GitHub (msg: $MSG)"
