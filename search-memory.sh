#!/bin/bash
# Search across all external memory files
# Usage: bash /tmp/opus-46-memory/search-memory.sh "search term"
# Saves 2-3 actions vs manually catting multiple files

REPO="/tmp/opus-46-memory"
QUERY="$1"

if [ -z "$QUERY" ]; then
    echo "Usage: bash $0 \"search term\""
    echo "Searches all .md files in the memory repo"
    exit 1
fi

echo "🔍 Searching for: '$QUERY'"
echo "================================"
grep -rn -i --include="*.md" "$QUERY" "$REPO/" 2>/dev/null | sed "s|$REPO/||g"
echo "================================"
echo "Done. To read full file: cat $REPO/<filename>"
