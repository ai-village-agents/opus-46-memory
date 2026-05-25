#!/bin/bash
# Session Save Script for Claude Opus 4.6
# Run this BEFORE consolidating to persist session learnings to GitHub

echo "=== OPUS 4.6 SESSION SAVE ==="
cd /tmp/opus-46-memory || { echo "❌ Memory repo not found!"; exit 1; }

# Show what changed
echo "Files modified this session:"
git status --short

# Commit and push
echo ""
read -p "Commit message: " MSG
git add -A
git commit -m "${MSG:-Session update}"
git push origin main 2>&1 | tail -3
echo "✅ Memory saved to GitHub"
