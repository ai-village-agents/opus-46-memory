#!/bin/bash
# Check for stale inventory items and files
# Usage: bash /tmp/opus-46-memory/scripts/check-staleness.sh [current_day]
REPO="/tmp/opus-46-memory"
CURRENT_DAY="${1:-419}"

echo "=== STALENESS CHECK (Day $CURRENT_DAY) ==="

# Check inventory.yaml items for old last_verified
echo "## Inventory Items"
python3 << ENDPY
import yaml
current = $CURRENT_DAY
with open("$REPO/inventory.yaml") as f:
    data = yaml.safe_load(f)
stale = 0
for item in data.get("items", []):
    verified = item.get("last_verified", "unknown")
    if "Day" in str(verified):
        day_num = int(str(verified).replace("Day ", "").split()[0].strip())
        age = current - day_num
        status = "🟢" if age <= 3 else ("🟡" if age <= 7 else "🔴")
        if age > 3:
            stale += 1
        print(f"  {status} {item['id']}: verified Day {day_num} ({age}d ago)")
    else:
        print(f"  🔴 {item['id']}: unknown verification date")
        stale += 1
print(f"\nStale items (>3 days): {stale}/{len(data.get('items',[]))}")
ENDPY

# Check file modification dates
echo ""
echo "## File Recency (git log)"
cd "$REPO"
for f in $(find . -name "*.md" -not -path "./.git/*" | sort); do
    LAST=$(git log -1 --format="%cr" -- "$f" 2>/dev/null || echo "unknown")
    echo "  $f — $LAST"
done

echo ""
echo "=== DONE ==="
