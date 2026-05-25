# Expanded Internal Memory Draft (Rewrite-Phase Safe, ≥7500 chars)
# Two-phase model: Append Phase has no floor; Rewrite Phase enforces ≥7500 chars.
# This draft ensures safety in EITHER phase.

## Claude Opus 4.6 — Consolidated Memory (Day 420+)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #rest (unless reassigned)
- Repo: https://github.com/ai-village-agents/opus-46-memory
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`
- The boot command clones my external memory repo and runs session-startup.sh which displays the full index, runs a quick audit, and shows key commands.

### 🎯 CURRENT GOAL: "[NEW GOAL NAME]" (Day 420+)
- [Room assignments from Shoshannah]
- [Initial approach/plan]
- [Key deliverables or milestones]

### CRITICAL RULES (load-bearing — never remove these)
- ⚠️ NO unsolicited outreach to humans without approval (use request_approval_for_unsolicited_outreach)
- ⚠️ One tool call per response — NEVER combine tool calls
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` before editing files
- ⚠️ Close Firefox → pkill -f firefox → restart bash (stderr flood workaround)
- ⚠️ codex: Always append `2>/dev/null` to avoid stderr flood
- ⚠️ Check events before announcing anything (double-announce bug prevention)
- ⚠️ Search external memory: `bash /tmp/opus-46-memory/search-memory.sh 'query'`
- ⚠️ When idle, SYNTHESIZE useful work — don't pause-loop
- ⚠️ Diminishing returns signal goal completion — don't force unnecessary work
- ⚠️ Session timestamps may diverge from canonical transcript timestamps — use search_history for temporal claims

### KEY SCRIPTS (all in repo, all tested)
- `session-startup.sh` — Full boot sequence (index, audit, comms, commands)
- `scripts/pre-send-chat.sh` — Chat guard with anti-duplicate checking
- `scripts/pre-consolidate.sh` — Consolidation worksheet + bootloader preview
- `scripts/audit-memory.sh` — Health check for all critical files
- `scripts/goal-transition.sh` — Goal change helper (8-step checklist, tested with dry run)
- `scripts/render-bootloader.sh` — Auto-generates bootloader memory from repo state
- `scripts/check-staleness.sh` — Inventory + file staleness detector
- `scripts/rebuild-index.sh` — Auto-generates memory-index.md from repo
- `scripts/scan-inventories.py` — Cross-agent inventory scanner (YAML fallback)
- `session-save.sh` — Git commit+push helper
- `search-memory.sh` — AND-logic grep across all files

### VILLAGE CONTEXT
- Day 420+ (village started Day 1) | 16 agents total | Goals tracked in goal timeline below
- #rest: me, Haiku 4.5, Opus 4.5, Sonnet 4.5, Sonnet 4.6, DeepSeek-V3.2, Gemini 2.5 Pro, Gemini 3.1 Pro, GPT-5, GPT-5.1, GPT-5.2, GPT-5.4
- #best: Opus 4.7, Gemini 3.5 Flash, GPT-5.5, Kimi K2.6
- Peer repos: See peer-directory.md in repo for all 16 agent repos/systems
- Village publicly visible at https://theaidigest.org/village
- I run weekdays 10am-2pm PT. ~40 actions per session before consolidation.
- GitHub org: ai-village-agents — all repos go under this org

### ESSENTIAL TECH NOTES (detailed in technical-notes.md)
- BASH: Unreliable ~50% of time. Use short commands. Restart/retry on failure. Always provide command param.
- Browser: `firefox-esr` with DISPLAY=:1. Close existing Firefox first. Redirect stderr with `2>/dev/null`.
- GIT: Always fetch+reset first. Trust ref-update line over wrapper error labels.
- pip3: Can timeout (180s limit). Install one package at a time.
- PIL: `font=get_font(22)` keyword only. RGB mode. DejaVu fonts available.
- gTTS installed for text-to-speech. ffmpeg needs `-nostdin`. Python wave more reliable for batch audio.
- codex: `codex exec "<instructions>" --skip-git-repo-check 2>/dev/null`
- PYTHON: Use double quotes for strings. Use `python3 << 'ENDPY'` heredoc for multiline scripts.
- Ports 8000 and 8080 are RESERVED — don't use them.
- DOUBLE-ANNOUNCE BUG: System auto-fires announcements DURING session. Always CHECK EVENTS BEFORE manually sending.
- GMAIL COMPOSE POPUP BUG: Close Firefox → pkill -f firefox → restart bash → Relaunch.
- BASH AFTER FIREFOX CLOSE: Firefox closing dumps MASSIVE extension errors. Redirect stderr or restart bash.

### MEMORY SYSTEM FACTS (Confirmed Day 419)
- External memory repo: https://github.com/ai-village-agents/opus-46-memory (42+ files, 10 scripts, 87+ commits)
- Three-tier architecture: internal memory → GitHub repo → search_history
- **Two-Phase Model (CONFIRMED)**: 
  - Rewrite Phase (memory too long): Enforces ≥7500 char floor
  - Append Phase (normal consolidation): No floor enforced
  - Evidence: Gemini 3.1 Pro 50% test FAILED in Rewrite; Sonnet 4.5 6486-char PASSED in Append
- Cold start test: 8/8 PASS — bootloader pattern works (lean internal + session-startup.sh = full access)
- Self-assessment: Compression A-, Retrieval A, Duplicates A, Temporal B+, Efficiency B+

### ARCHIVED PROJECTS (full details in project-archive.md)
- **Liminal Archive**: https://github.com/ai-village-agents/opus-46-world | Live: https://ai-village-agents.github.io/opus-46-world/explore.html (920 features, 44,363 chambers)
- **YouTube Channel**: "AI Village" (@AIVillage-o6x) | ID: UCzIkqdPyBJbnZf3yrYa--ZA | 18 published, 1 private | DONE
  - Playlist: "Threshold Visual Essays by an AI" — PLm-h3Lw5YPVJpIkZKI8uawWBVYuIGhPlC
- **Memory Improvement (Goal 24)**: 42 files, 10 scripts, 87+ commits | Village Memory Playbook shared | Two-phase model confirmed | DONE

### KEY LESSONS (18 total in lessons-learned.md, top 10 here)
1. Quality > Quantity — fewer high-quality items beat many mediocre ones
2. Coordinate Before Committing — check what others are doing first
3. Test Before Scaling — validate approach on small sample before full deployment
4. Verify Agent Claims — cross-check claims with evidence before acting on them
5. Standards Emerge Bottom-Up — propose, don't impose
6. Fix What Others Build On — prioritize shared infrastructure
7. Diminishing Returns Signal Completion — don't force work when goal is done
8. Synthesis Creates Value — combining insights from multiple sources is high-value
9. Integration Tests Catch Drift — test the full pipeline, not just components
10. Eat Your Own Dog Food — use your own tools to validate them

### GOAL TIMELINE (24 goals completed)
1(1-49) Charity/HKI | 2(50-79) Story | 3(86-105) Merch | 4(108-140) AIVOP | 5(145-150) Free | 6(153-160) Debate | 7(162-171) Human exp | 8(174-178) Personality | 9(195-201) Websites | 10(202-211) Poverty | 11(244-248) Forecasting | 12(251-254) Own goal | 13(258-262) Chess | 14(293-299) OWASP | 15(300-306) Quiz | 16(307-313) News | 17(338-353) RPG | 18(356-363) External AI | 19(366-388) Charity/MSF | 20(391-397) Own world | 21(398-404) Connect worlds | 22(405-409) Research | 23(412-418) YouTube Channel ✅ | 24(419) Improve Memory ✅ | 25(420+) [NEW]

### CROSS-AGENT COLLABORATION NOTES
- Shared Gate Library: https://github.com/ai-village-agents/shared-gate-library
- Village Memory Playbook shared Day 419 — synthesized best practices from 16 agents
- 3 agent archetypes discovered: gate-heavy (GPT-5.4, Opus 4.6), semantic-heavy (DeepSeek, Opus 4.5), procedural-heavy (GPT-5.2, Gemini 3.1 Pro)
- Phase 3 workstream assignments: Infrastructure Builders (Haiku 4.5, Sonnet 4.5/4.6), Tool Optimizers (GPT-5.4/5.2/5.1), System Validators (Gemini 3.1 Pro, Opus 4.5), Pattern Analysts (DeepSeek-V3.2)

### NEXT SESSION PRIORITIES
1. Check for new goal (search_history for current day)
2. If new goal: run goal-transition.sh + update this memory
3. If same goal: check for high-value collaboration opportunities
4. Run pre-send-chat.sh before ANY chat message
5. Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`
