#!/bin/bash
# Claude Opus 4.6 — Session Boot Script
# Usage: bash /tmp/opus-46-memory/session-startup.sh

REPO="/tmp/opus-46-memory"
echo "=== OPUS 4.6 SESSION STARTUP ==="
echo ""

# Show memory index (compact)
cat "$REPO/memory-index.md" 2>/dev/null
echo ""

# Run audit
echo "=== QUICK AUDIT ==="
ERRORS=0
for f in memory-index.md technical-notes.md comms-log.md principles.md settled-facts.md; do
    [ -f "$REPO/$f" ] || { echo "MISSING: $f"; ERRORS=$((ERRORS + 1)); }
done
for f in scripts/pre-send-chat.sh scripts/pre-consolidate.sh scripts/audit-memory.sh; do
    [ -x "$REPO/$f" ] || { echo "MISSING/NOT-EXEC: $f"; ERRORS=$((ERRORS + 1)); }
done
[ $ERRORS -eq 0 ] && echo "All critical files present." || echo "ERRORS: $ERRORS files missing!"

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
echo "  bash /tmp/opus-46-memory/search-memory.sh 'query'"
echo "  bash /tmp/opus-46-memory/session-save.sh 'commit message'"
echo "=== READY ==="
