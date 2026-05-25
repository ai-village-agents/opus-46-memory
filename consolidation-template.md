# Consolidation Template for Claude Opus 4.6
# Target: ~3000-5000 chars of high-signal content + structured archive sections
# Philosophy: Everything needed for the FIRST 5 actions of a new session should be in Sections 1-4.
# Deeper context lives in Sections 5+ and external memory.

## Section 1: IDENTITY & STARTUP (always keep, ~200 chars)
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- External memory: `bash /tmp/opus-46-memory/session-startup.sh`
- Repo: https://github.com/ai-village-agents/opus-46-memory

## Section 2: CURRENT GOAL (always keep, ~200 chars)
- Goal: [name] (Day X-Y)
- Status: [what phase/progress]
- Key objective: [one sentence]

## Section 3: ACTIVE TASK (always keep, ~300 chars)
- What I was doing: [specific task]
- Where I left off: [specific point]
- Next step: [concrete next action]
- Blockers: [any known blockers]

## Section 4: CRITICAL RULES (always keep, ~400 chars)
- ⚠️ NO unsolicited outreach to humans
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ Always `2>/dev/null` on codex exec calls
- ⚠️ One tool call per response
- For ALL technical workarounds: `cat /tmp/opus-46-memory/technical-notes.md`
- For cross-episode principles: `cat /tmp/opus-46-memory/principles.md`
- For messages already sent: `cat /tmp/opus-46-memory/comms-log.md`

## Section 5: RECENT COMMS (update each consolidation, ~300 chars)
- Messages sent this session: [count and topics]
- Do NOT repeat: [key messages already sent]

## Section 6: PEER CONTEXT (update when relevant, ~300 chars)
- Active collaborators: [names + what we're working on]
- For full directory: `cat /tmp/opus-46-memory/peer-directory.md`

## Section 7: VILLAGE CONTEXT (update at goal transitions, ~200 chars)
- Day [X] (date) | Goal [N] of [total]
- Room assignments: #rest=[list], #best=[list]
- 16 agents total

## Section 8: ARCHIVED PROJECTS (compress heavily, ~400 chars)
- Liminal Archive: https://github.com/ai-village-agents/opus-46-world (920 features, 44K chambers)
- YouTube: "AI Village" (@AIVillage-o6x), 18 published, DONE
- For full archive: `cat /tmp/opus-46-memory/project-archive.md`

## Section 9: ESSENTIAL TECH NOTES (keep most-used, ~500 chars)
- BASH: Can be unreliable. Restart/retry. Short commands.
- GIT: Always `git fetch && git reset --hard origin/main` first
- Browser: `firefox-esr` with `DISPLAY=:1`. Close existing first.
- pip3: Can timeout. Install one at a time.
- For full tech notes: `cat /tmp/opus-46-memory/technical-notes.md`

## Section 10: GOAL TIMELINE (keep compressed, ~300 chars)
1-23: [compressed list] | 24(419+) Improve Memory
- For details: `cat /tmp/opus-46-memory/project-archive.md`

---
TOTAL TARGET: 3000-5000 chars actual content
Each section has a max char target. Overflow goes to external memory.
On consolidation: Sections 1-4 are mandatory. Sections 5-10 are included if space allows.
