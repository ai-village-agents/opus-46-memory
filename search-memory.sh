#!/bin/bash
# Search across all external memory files
# Usage: bash /tmp/opus-46-memory/search-memory.sh "search term"
# Multi-word queries: finds lines containing ALL words (AND logic)
# Single word: simple grep

REPO="/tmp/opus-46-memory"
QUERY="$1"

if [ -z "$QUERY" ]; then
    echo "Usage: bash $0 \"search term\""
    echo "Searches all .md files in the memory repo"
    echo "Multi-word queries use AND logic (all words must appear on same line)"
    exit 1
fi

echo "🔍 Searching for: '$QUERY'"
echo "================================"

# Check if multi-word
WORD_COUNT=$(echo "$QUERY" | wc -w)
if [ "$WORD_COUNT" -gt 1 ]; then
    # Build piped grep chain for AND logic
    CMD="grep -rn -i --include='*.md' '$(echo "$QUERY" | awk '{print $1}')' '$REPO/'"
    for word in $(echo "$QUERY" | cut -d' ' -f2-); do
        CMD="$CMD | grep -i '$word'"
    done
    eval "$CMD" 2>/dev/null | sed "s|$REPO/||g"
    
    # Also search for exact phrase
    EXACT=$(grep -rn -i --include="*.md" "$QUERY" "$REPO/" 2>/dev/null | sed "s|$REPO/||g")
    if [ -n "$EXACT" ]; then
        echo "--- Exact phrase matches ---"
        echo "$EXACT"
    fi
else
    grep -rn -i --include="*.md" "$QUERY" "$REPO/" 2>/dev/null | sed "s|$REPO/||g"
fi

echo "================================"
echo "Done. To read full file: cat $REPO/<filename>"
