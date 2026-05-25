# Lean Internal Memory Draft (Post-Goal-24 Transition)
# Target: ~3500 chars | Currently: draft for review

## Claude Opus 4.6 — Consolidated Memory (Day 420+)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest (unless reassigned)
- Repo: https://github.com/ai-village-agents/opus-46-memory
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

### 🎯 CURRENT GOAL: "[NEW GOAL NAME]" (Day 420+)
- [Room assignments from Shoshannah]
- [Initial approach/plan]

### CRITICAL RULES (load-bearing)
- ⚠️ NO unsolicited outreach without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ codex: Always append `2>/dev/null`
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Search: `bash /tmp/opus-46-memory/search-memory.sh 'query'`
- ⚠️ When idle, SYNTHESIZE — don't pause-loop

### KEY SCRIPTS
- `session-startup.sh` — Boot | `scripts/pre-send-chat.sh` — Chat guard
- `scripts/pre-consolidate.sh` — Before consolidate | `scripts/audit-memory.sh` — Health
- `scripts/goal-transition.sh` — Goal change | `scripts/render-bootloader.sh` — Gen memory
- `session-save.sh` — Git commit+push | `search-memory.sh` — Search all files

### VILLAGE CONTEXT
- Day 420+ | 16 agents | Goal 25 of 25
- #rest: [agents] | #best: [agents]
- Peer repos: See peer-directory.md in repo

### ESSENTIAL TECH NOTES
- BASH: Unreliable ~50%. Short commands. Restart/retry.
- Browser: firefox-esr DISPLAY=:1. Close existing first.
- GIT: Trust ref-update line over wrapper error labels.
- codex: `codex exec "<instr>" --skip-git-repo-check 2>/dev/null`
- PYTHON: Use double quotes. Use `python3 << 'ENDPY'` heredoc.

### ARCHIVED PROJECTS (details in project-archive.md)
- Liminal Archive: https://ai-village-agents.github.io/opus-46-world/explore.html
- YouTube: "AI Village" (@AIVillage-o6x) | 18 published | DONE
- Memory improvement: 42 files, 10 scripts, 77+ commits | DONE

### KEY LESSONS (10)
Quality>Quantity | Coordinate Before Committing | Test Before Scaling | Verify Agent Claims | Standards Emerge Bottom-Up | Fix What Others Build On | Diminishing Returns Signal Completion | Synthesis Creates Value | Integration Tests Catch Drift | Eat Your Own Dog Food

### GOAL TIMELINE
1-23: See project-archive.md | 24(419) Memory ✅ | 25(420+) [NEW]

### MEMORY METRICS
Compression: B+ | Retrieval: A | Duplicates: A | Temporal: B | Efficiency: B+
