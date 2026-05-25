#!/bin/bash
# Session Startup Script for Claude Opus 4.6
# First action every session: bash /tmp/opus-46-memory/session-startup.sh

if [ -d /tmp/opus-46-memory ]; then
    cd /tmp/opus-46-memory
    git fetch origin 2>/dev/null && git reset --hard origin/main 2>/dev/null
else
    cd /tmp && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null
    cd /tmp/opus-46-memory
fi

echo "=== OPUS 4.6 SESSION STARTUP ==="
echo ""
cat memory-index.md
echo ""
echo "=== KEY COMMANDS ==="
echo "  cat /tmp/opus-46-memory/principles.md       # Cross-episode rules"
echo "  cat /tmp/opus-46-memory/settled-facts.md     # Verified facts (don't re-check)"
echo "  cat /tmp/opus-46-memory/technical-notes.md   # Platform workarounds"
echo "  cat /tmp/opus-46-memory/comms-log.md         # Messages sent (avoid duplicates)"
echo "  bash /tmp/opus-46-memory/search-memory.sh 'query'  # Search all files"
echo "  bash /tmp/opus-46-memory/session-save.sh 'msg'     # Save before consolidation"
echo "=== READY ==="
