#!/bin/bash
# Pre-send chat guard for Claude Opus 4.6
# Usage: bash /tmp/opus-46-memory/scripts/pre-send-chat.sh "purpose" "recipient" "duplicate-check"
# Exit 0 = PASS, Exit 1 = BLOCK
COMMS_LOG="/tmp/opus-46-memory/comms-log.md"
PURPOSE="${1:-}"; RECIPIENT="${2:-}"; DUP_CHECK="${3:-}"
echo "=== PRE-SEND CHAT GUARD ==="
if [ -z "$PURPOSE" ] || [ -z "$RECIPIENT" ] || [ -z "$DUP_CHECK" ]; then
    echo "BLOCK: Missing required fields."; echo "Usage: pre-send-chat.sh 'purpose' 'recipient' 'dup-check'"; exit 1; fi
DUP_LOWER=$(echo "$DUP_CHECK" | tr '[:upper:]' '[:lower:]')
if [ "$DUP_LOWER" = "none" ] || [ "$DUP_LOWER" = "n/a" ] || [ "$DUP_LOWER" = "not checked" ]; then
    echo "BLOCK: Duplicate check too vague."; exit 1; fi
echo "Purpose: $PURPOSE"; echo "Recipient: $RECIPIENT"; echo "Dup check: $DUP_CHECK"; echo ""
echo "--- Recent comms ---"
[ -f "$COMMS_LOG" ] && tail -15 "$COMMS_LOG" || echo "(no comms-log)"
MSG_COUNT=$(grep -c "^[0-9]\+\." "$COMMS_LOG" 2>/dev/null || echo "0")
echo ""; echo "Messages today: $MSG_COUNT"
[ "$MSG_COUNT" -ge 12 ] && echo "WARNING: 12+ messages. Only HIGH VALUE."
echo ""; echo "PASS: Pre-send checks complete."; exit 0
