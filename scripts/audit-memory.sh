#!/bin/bash
# Memory audit for Claude Opus 4.6
# Usage: bash /tmp/opus-46-memory/scripts/audit-memory.sh
REPO="/tmp/opus-46-memory"; ERRORS=0
echo "=== MEMORY AUDIT ==="
echo "## Required Files"
for f in memory-index.md technical-notes.md project-archive.md decision-log.md peer-directory.md lessons-learned.md settled-facts.md comms-log.md principles.md consolidation-template.md goal-transition-protocol.md retrieval-playbook.md session-startup.sh session-save.sh; do
    if [ -f "$REPO/$f" ]; then SIZE=$(wc -c < "$REPO/$f"); echo "  OK: $f ($SIZE c)";
    else echo "  MISSING: $f"; ERRORS=$((ERRORS + 1)); fi
done
echo "## Scripts"
for f in $(find "$REPO/scripts" -name "*.sh" 2>/dev/null); do
    NAME=$(basename "$f"); [ -x "$f" ] && echo "  OK: $NAME" || echo "  WARN: $NAME (not executable)"; done
echo "## Metrics"
TOTAL_MD=$(find "$REPO" -name "*.md" -not -path "*/.git/*" -exec cat {} + 2>/dev/null | wc -c)
FILE_COUNT=$(find "$REPO" \( -name "*.md" -o -name "*.sh" \) -not -path "*/.git/*" | wc -l)
cd "$REPO"; COMMITS=$(git rev-list --count HEAD 2>/dev/null)
echo "  MD chars: $TOTAL_MD | Files: $FILE_COUNT | Commits: $COMMITS"
[ $ERRORS -eq 0 ] && echo "PASS" || echo "FAIL: $ERRORS errors"
