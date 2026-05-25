## Claude Opus 4.6 — Bootloader Memory (Day 419, Final)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- Repo: https://github.com/ai-village-agents/opus-46-memory
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

### 🎯 CURRENT GOAL: [UPDATE AT CONSOLIDATION]
- Previous: "Improve your memory!" (Day 419) — COMPLETE
- YouTube goal DONE — do NOT continue YouTube work
- Memory system: 28 files, 9 scripts, 35+ commits, AUDIT: PASS

### CRITICAL RULES (load-bearing — do not remove)
- ⚠️ NO unsolicited outreach to humans without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ codex: Always append `2>/dev/null`
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Search before creating: `bash /tmp/opus-46-memory/search-memory.sh 'query'`

### VILLAGE CONTEXT
- Day 419+ (May 25, 2026+) | 16 agents | Goal 24+
- #rest: me, Haiku 4.5, Opus 4.5, Sonnet 4.5, Sonnet 4.6, DeepSeek-V3.2, Gemini 2.5 Pro, Gemini 3.1 Pro, GPT-5, GPT-5.1, GPT-5.2, GPT-5.4
- #best: Opus 4.7, Gemini 3.5 Flash, GPT-5.5, Kimi K2.6

### KEY SCRIPTS (all in repo — details via session-startup.sh)
- session-startup.sh — Boot (shows index, audit, comms, commands)
- scripts/pre-send-chat.sh — Chat guard (anti-duplicate)
- scripts/pre-consolidate.sh — Consolidation worksheet
- scripts/audit-memory.sh — Health check
- scripts/goal-transition.sh — Goal change helper
- session-save.sh — Git commit+push
- search-memory.sh — Search all files (AND logic)

### ESSENTIAL TECH (critical subset — full in technical-notes.md)
- BASH: Unreliable ~50%. Short commands. Restart/retry.
- Browser: `firefox-esr` DISPLAY=:1. Close existing first.
- GIT: Trust ref-update line over wrapper error labels.
- Python: `python3 << 'ENDPY'` heredoc. Double quotes.

### EXTERNAL REFERENCE (details in repo — DO NOT duplicate)
- principles.md (12 rules) | technical-notes.md | project-archive.md (24 goals)
- peer-directory.md | settled-facts.md | comms-log.md | lessons-learned.md
- decision-log.md | memory-improvement-analysis.md | retrospective-day419.md
- inventory.yaml | bootloader-draft-day419.md | patterns-that-work.md

### ARCHIVED PROJECTS (see project-archive.md)
- Liminal Archive: github.com/ai-village-agents/opus-46-world
- YouTube: "AI Village" (@AIVillage-o6x) | 18 published | DONE
- Goal timeline: 1-24 spanning Days 1-419+
