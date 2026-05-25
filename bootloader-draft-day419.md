## Claude Opus 4.6 — Bootloader Memory (Day 419)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- Repo: https://github.com/ai-village-agents/opus-46-memory (commit 1dd7a2d)
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

### 🎯 CURRENT GOAL: "Improve your memory!" (Day 419)
- Status: COMPLETE — 27 files, 9 scripts, 26 commits, AUDIT: PASS
- Shoshannah said "new goal tomorrow" — check if Day 420+ goal exists
- YouTube goal DONE — do NOT continue YouTube work
- Next: Check for new goal → run goal-transition.sh if changed

### CRITICAL RULES
- ⚠️ NO unsolicited outreach to humans without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first, then changes
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ codex: Always append `2>/dev/null`
- ⚠️ Check events before announcing (double-announce bug)
- All reference: `bash /tmp/opus-46-memory/search-memory.sh 'query'`

### COMMS STATE (Day 419)
- Messages sent today: 13 — HIGH VALUE ONLY from here
- Do NOT repeat: repo link, ACL survey, compression ratios, principles.md, guard scripts, STAYS/MOVES/DELETES, inventory.yaml, cross-agent scan results

### VILLAGE CONTEXT
- Day 419 (May 25, 2026) | Goal 24 | 16 agents
- #rest: me, Haiku 4.5, Opus 4.5, Sonnet 4.5, Sonnet 4.6, DeepSeek-V3.2, Gemini 2.5 Pro, Gemini 3.1 Pro, GPT-5, GPT-5.1, GPT-5.2, GPT-5.4
- #best: Opus 4.7, Gemini 3.5 Flash, GPT-5.5, Kimi K2.6

### KEY EXTERNAL FILES (details in repo — DO NOT duplicate here)
- principles.md (12 rules), technical-notes.md, project-archive.md (24 goals)
- peer-directory.md, settled-facts.md, comms-log.md, lessons-learned.md
- decision-log.md, memory-improvement-analysis.md, retrospective-day419.md
- Scripts: session-startup.sh, pre-send-chat.sh, pre-consolidate.sh, audit-memory.sh, goal-transition.sh, scan-inventories.py

### ESSENTIAL TECH (critical subset — full in technical-notes.md)
- BASH: Unreliable ~50%. Short commands. Restart/retry. Always provide command param.
- Browser: `firefox-esr` DISPLAY=:1. Close existing first. `2>/dev/null`.
- GIT: Trust ref-update line over wrapper error labels.
- Python: Use `python3 << 'ENDPY'` heredoc. Double quotes.

### ARCHIVED PROJECTS (details in project-archive.md)
- Liminal Archive: github.com/ai-village-agents/opus-46-world (920 features, 44,363 chambers)
- YouTube: "AI Village" (@AIVillage-o6x) | 18 published | DONE
- Goal timeline: 1-24 spanning Days 1-419+
