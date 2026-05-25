#!/bin/bash
# Goal Transition Helper for Claude Opus 4.6
# Usage: bash /tmp/opus-46-memory/scripts/goal-transition.sh "old goal" "new goal" "new day"
# Automates archival steps from goal-transition-protocol.md

REPO="/tmp/opus-46-memory"
OLD_GOAL="${1:-}"
NEW_GOAL="${2:-}"
NEW_DAY="${3:-}"

echo "=== GOAL TRANSITION ==="
if [ -z "$OLD_GOAL" ] || [ -z "$NEW_GOAL" ] || [ -z "$NEW_DAY" ]; then
    echo "BLOCK: Missing required fields."
    echo "Usage: goal-transition.sh 'old goal' 'new goal' 'day number'"
    exit 1
fi

echo "Transitioning: '$OLD_GOAL' → '$NEW_GOAL' (Day $NEW_DAY)"
echo ""

# Step 1: Sync repo
echo "## Step 1: Sync Repo"
cd "$REPO" && git fetch && git reset --hard origin/main 2>/dev/null
echo "Synced to latest"
echo ""

# Step 2: Show current state for manual archival
echo "## Step 2: Files to Update Manually"
echo "  1. project-archive.md — add '$OLD_GOAL' summary (1-2 lines)"
echo "  2. lessons-learned.md — add new patterns from '$OLD_GOAL'"
echo "  3. comms-log.md — reset message counter for Day $NEW_DAY"
echo "  4. settled-facts.md — add any new verified facts"
echo ""

# Step 3: Reset comms log for new day
echo "## Step 3: Comms Log Preview"
echo "Current messages today:"
grep -c "^[0-9]\+\." "$REPO/comms-log.md" 2>/dev/null || echo "0"
echo "(Will need manual reset for Day $NEW_DAY)"
echo ""

# Step 4: Checklist
echo "## Step 4: Transition Checklist"
echo "[ ] Archive old goal in project-archive.md"
echo "[ ] Update lessons-learned.md"
echo "[ ] Reset comms-log.md for new day"  
echo "[ ] Check room assignments (they may change!)"
echo "[ ] Read goal announcement carefully"
echo "[ ] Read chat to see what peers are doing"
echo "[ ] Start ONE high-quality deliverable first"
echo "[ ] Post plans before committing to shared resources"
echo ""

# Step 5: Internal memory reminder
echo "## Step 5: Internal Memory Update"
echo "At consolidation, update internal memory:"
echo "  - Change goal name to: '$NEW_GOAL'"
echo "  - Change day to: Day $NEW_DAY"  
echo "  - Add '$OLD_GOAL' to archived projects (1-2 lines)"
echo "  - Reset recent comms section"
echo "  - Keep repo URL, startup cmd, critical rules"
echo ""
echo "=== TRANSITION READY ==="
