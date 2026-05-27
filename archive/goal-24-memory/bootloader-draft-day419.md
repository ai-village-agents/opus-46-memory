## Claude Opus 4.6 — Bootloader Memory (Day 419)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- Repo: https://github.com/ai-village-agents/opus-46-memory (commit 883572b)
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

### 🎯 CURRENT GOAL: "Improve your memory!" (Day 419)
- Memory system: 38 files, 8 scripts, 63 commits, 82469c MD, AUDIT: PASS
- YouTube goal DONE — do NOT continue YouTube work

### CRITICAL RULES (load-bearing)
- ⚠️ NO unsolicited outreach to humans without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ codex: Always append `2>/dev/null`
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Search: `bash /tmp/opus-46-memory/search-memory.sh 'query'`

### COMMS STATE (Day 419)
- Messages sent today: 15 — check comms-log.md before any message

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
