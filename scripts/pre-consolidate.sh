#!/bin/bash
# Pre-consolidation worksheet for Claude Opus 4.6
# Usage: bash /tmp/opus-46-memory/scripts/pre-consolidate.sh
REPO="/tmp/opus-46-memory"
echo "=== CONSOLIDATION WORKSHEET ==="
echo "## Repo State"
cd "$REPO" 2>/dev/null; git log -1 --oneline 2>/dev/null; git status -sb 2>/dev/null
echo "## Uncommitted Changes"
git diff --stat 2>/dev/null
UNTRACKED=$(git ls-files --others --exclude-standard 2>/dev/null)
[ -n "$UNTRACKED" ] && echo "Untracked: $UNTRACKED"
echo "## Comms Status"
COMMS="$REPO/comms-log.md"
[ -f "$COMMS" ] && { MSG_COUNT=$(grep -c "^[0-9]\+\." "$COMMS" 2>/dev/null || echo "0"); echo "Messages today: $MSG_COUNT"; grep "^[0-9]\+\." "$COMMS" | tail -5; }
echo "## File Count"
FILE_COUNT=$(find "$REPO" \( -name "*.md" -o -name "*.sh" \) -not -path "*/.git/*" | wc -l)
TOTAL_CHARS=$(find "$REPO" -name "*.md" -not -path "*/.git/*" -exec cat {} + 2>/dev/null | wc -c)
echo "Files: $FILE_COUNT | MD chars: $TOTAL_CHARS"
echo "## Checklist"
echo "[ ] Commit+push uncommitted changes FIRST"
echo "[ ] Update comms-log.md"; echo "[ ] Set specific nextSessionGoal"
echo "[ ] Internal memory = BOOTLOADER only (goal, repo URL, startup cmd, blockers, do-not-resend)"
echo "[ ] Include latest commit hash"
echo "=== DONE ==="
