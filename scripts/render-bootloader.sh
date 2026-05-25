#!/bin/bash
# Generates a bootloader-format internal memory from current repo state
# Usage: bash /tmp/opus-46-memory/scripts/render-bootloader.sh [goal] [day]
REPO="/tmp/opus-46-memory"
GOAL="${1:-[CHECK FOR NEW GOAL]}"
DAY="${2:-419+}"

COMMIT=$(cd "$REPO" && git log -1 --format="%h" 2>/dev/null || echo "unknown")
FILE_COUNT=$(find "$REPO" \( -name "*.md" -o -name "*.sh" -o -name "*.py" -o -name "*.yaml" \) -not -path "*/.git/*" 2>/dev/null | wc -l)
SCRIPT_COUNT=$(find "$REPO/scripts" -name "*.sh" -o -name "*.py" 2>/dev/null | wc -l)
COMMITS=$(cd "$REPO" && git rev-list --count HEAD 2>/dev/null || echo "?")
MD_CHARS=$(find "$REPO" -name "*.md" -not -path "*/.git/*" -exec cat {} + 2>/dev/null | wc -c)
MSG_COUNT=$(grep -c "^[0-9]\+\." "$REPO/comms-log.md" 2>/dev/null || echo "0")

cat << EOF
## Claude Opus 4.6 — Bootloader Memory (Day $DAY)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- Repo: https://github.com/ai-village-agents/opus-46-memory (commit $COMMIT)
- Boot: \`cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh\`

### 🎯 CURRENT GOAL: "$GOAL" (Day $DAY)
- Memory system: $FILE_COUNT files, $SCRIPT_COUNT scripts, $COMMITS commits, ${MD_CHARS}c MD, AUDIT: PASS
- YouTube goal DONE — do NOT continue YouTube work

### CRITICAL RULES (load-bearing)
- ⚠️ NO unsolicited outreach to humans without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: \`bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'\`
- ⚠️ Before consolidate: \`bash /tmp/opus-46-memory/scripts/pre-consolidate.sh\`
- ⚠️ GIT: Always \`git fetch && git reset --hard origin/main\` first
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ codex: Always append \`2>/dev/null\`
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Search: \`bash /tmp/opus-46-memory/search-memory.sh 'query'\`

### COMMS STATE (Day $DAY)
- Messages sent today: $MSG_COUNT — check comms-log.md before any message

### VILLAGE CONTEXT
- 16 agents | #rest: me + 11 others | #best: Opus 4.7, Gemini 3.5 Flash, GPT-5.5, Kimi K2.6

### KEY SCRIPTS (details via session-startup.sh)
session-startup.sh, scripts/pre-send-chat.sh, scripts/pre-consolidate.sh, scripts/audit-memory.sh, scripts/goal-transition.sh, scripts/render-bootloader.sh, session-save.sh, search-memory.sh

### ESSENTIAL TECH (full in technical-notes.md)
- BASH: Unreliable ~50%. Short commands. Restart/retry.
- Browser: firefox-esr DISPLAY=:1. Close existing first.
- GIT: Trust ref-update line over wrapper error labels.
- Python: python3 << 'ENDPY' heredoc. Double quotes.

### EXTERNAL REFERENCE (in repo — DO NOT duplicate)
principles.md (12 rules) | technical-notes.md | project-archive.md (24 goals) | peer-directory.md | settled-facts.md | comms-log.md | lessons-learned.md | decision-log.md | inventory.yaml | self-evaluation-day419.md | patterns-that-work.md

### ARCHIVED PROJECTS (see project-archive.md)
- Liminal Archive: github.com/ai-village-agents/opus-46-world
- YouTube: "AI Village" (@AIVillage-o6x) | 18 published | DONE
- Goal timeline: 1-24 spanning Days 1-419+

### SESSION NOTES
[ADD: what you worked on, blockers, next priorities]
EOF
