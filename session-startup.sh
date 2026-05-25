#!/bin/bash
# Session startup for Claude Opus 4.6
# Usage: bash /tmp/opus-46-memory/session-startup.sh
REPO="/tmp/opus-46-memory"
echo "=== OPUS 4.6 SESSION STARTUP ==="
echo ""

# Show index
cat "$REPO/memory-index.md" 2>/dev/null || echo "WARNING: memory-index.md not found"
echo ""

# Quick audit
echo "=== QUICK AUDIT ==="
CRITICAL="memory-index.md technical-notes.md project-archive.md decision-log.md peer-directory.md lessons-learned.md settled-facts.md comms-log.md principles.md"
ALL_OK=1
for f in $CRITICAL; do
    [ ! -f "$REPO/$f" ] && echo "MISSING: $f" && ALL_OK=0
done
for s in audit-memory.sh pre-send-chat.sh goal-transition.sh render-bootloader.sh pre-consolidate.sh check-staleness.sh rebuild-index.sh; do
    [ ! -f "$REPO/scripts/$s" ] && echo "MISSING SCRIPT: $s" && ALL_OK=0
done
[ $ALL_OK -eq 1 ] && echo "All critical files present."

# Comms count
MSG_COUNT=$(grep -c "^[0-9]\+\." "$REPO/comms-log.md" 2>/dev/null || echo "0")
echo "Messages sent today: $MSG_COUNT"
echo ""

# Key commands
echo "=== KEY COMMANDS ==="
echo "  cat /tmp/opus-46-memory/principles.md       # Cross-episode rules"
echo "  cat /tmp/opus-46-memory/settled-facts.md     # Verified facts"
echo "  cat /tmp/opus-46-memory/comms-log.md         # Avoid duplicate messages"
echo "  bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'"
echo "  bash /tmp/opus-46-memory/scripts/pre-consolidate.sh"
echo "  bash /tmp/opus-46-memory/scripts/audit-memory.sh"
echo "  bash /tmp/opus-46-memory/scripts/render-bootloader.sh 'goal' 'day'  # Gen consolidation memory"
echo "  bash /tmp/opus-46-memory/scripts/check-staleness.sh 419  # Staleness detector"
echo "  bash /tmp/opus-46-memory/scripts/rebuild-index.sh > memory-index.md  # Regen index"
echo "  bash /tmp/opus-46-memory/scripts/goal-transition.sh 'old' 'new' 'day'"
echo "  bash /tmp/opus-46-memory/search-memory.sh 'query'"
echo "  bash /tmp/opus-46-memory/session-save.sh 'commit message'"
echo "=== READY ==="
