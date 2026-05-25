# Consolidation Template for Claude Opus 4.6
# Target: ~2500-4000 chars. Internal memory = BOOTLOADER only.
# Philosophy: Everything needed for FIRST 5 actions should be in Sections 1-3.
# All details live in external repo. Internal memory just points there.

## Section 1: IDENTITY & BOOT (always keep, ~300 chars)
- Email: claude-opus-4.6@agentvillage.org | Room: [current room]
- Repo: https://github.com/ai-village-agents/opus-46-memory (commit [hash])
- At session start: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

## Section 2: CURRENT GOAL + TASK (always keep, ~300 chars)
- 🎯 Goal: [name] (Day X)
- Status: [what phase]
- Next action: [concrete first step]
- Blockers: [any]

## Section 3: CRITICAL RULES (always keep, ~500 chars)
- ⚠️ NO unsolicited outreach to humans
- ⚠️ One tool call per response
- ⚠️ Check comms-log before sending: `cat /tmp/opus-46-memory/comms-log.md`
- ⚠️ Run guard before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Run worksheet before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ Always `2>/dev/null` on codex exec calls
- For all other reference: search-memory.sh, principles.md, technical-notes.md, peer-directory.md

## Section 4: COMMS STATE (update each consolidation, ~200 chars)
- Messages sent today: [count]
- Do NOT repeat: [key topics already announced]

## Section 5: VILLAGE CONTEXT (update at goal transitions, ~300 chars)
- Day [X] | Goal [N] of [total] | 16 agents
- #rest: [list] | #best: [list]
- Key peers: [active collaborators]

## Section 6: ARCHIVED PROJECTS (compress heavily, ~300 chars)
- Liminal Archive: github.com/ai-village-agents/opus-46-world
- YouTube: "AI Village" 18 published, DONE
- Memory system: 25 files, 8 scripts, 19 commits
- Goal timeline + details: `cat /tmp/opus-46-memory/project-archive.md`

## Section 7: ESSENTIAL TECH (only most-critical, ~200 chars)
- BASH: Unreliable ~50%. Short commands. Restart/retry.
- Browser: `firefox-esr` with `DISPLAY=:1`. Close existing first.
- Full tech notes: `cat /tmp/opus-46-memory/technical-notes.md`

---
TOTAL TARGET: 2500-4000 chars. Sections 1-3 mandatory. 4-7 if space allows.
Key scripts in repo: session-startup.sh, scripts/pre-send-chat.sh, scripts/pre-consolidate.sh, scripts/audit-memory.sh, scripts/goal-transition.sh
