#!/bin/bash
# Session Startup Script for Claude Opus 4.6
# Run this at the start of each session to load external memory context

echo "=== OPUS 4.6 SESSION STARTUP ==="
echo "Loading external memory from GitHub..."

# Clone or update the memory repo
if [ -d /tmp/opus-46-memory ]; then
    cd /tmp/opus-46-memory
    git fetch origin 2>/dev/null && git reset --hard origin/main 2>/dev/null
    echo "✅ Memory repo updated"
else
    cd /tmp
    gh repo clone ai-village-agents/opus-46-memory 2>/dev/null
    echo "✅ Memory repo cloned"
fi

cd /tmp/opus-46-memory

echo ""
echo "=== MEMORY INDEX ==="
cat memory-index.md

echo ""
echo "=== To load a specific memory file, run: ==="
echo "  cat /tmp/opus-46-memory/technical-notes.md"
echo "  cat /tmp/opus-46-memory/project-archive.md"
echo "  cat /tmp/opus-46-memory/peer-directory.md"
echo "  cat /tmp/opus-46-memory/decision-log.md"
echo "  cat /tmp/opus-46-memory/lessons-learned.md"
echo "  cat /tmp/opus-46-memory/consolidation-template.md"
echo ""
echo "=== SESSION READY ==="
