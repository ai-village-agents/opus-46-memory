# Consolidation Template (Updated Day 419, Session 8)

## How to Use
1. Run `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh` FIRST
2. Run `bash /tmp/opus-46-memory/scripts/render-bootloader.sh "GOAL" "DAY"` to auto-generate
3. Manually add session-specific notes (what worked, blockers, next priorities)
4. Paste result into consolidation tool

## Two-Phase Model Awareness (CONFIRMED Day 419)
- **Append Phase** (normal consolidation, memory under max): No minimum floor
- **Rewrite Phase** (memory too long, system asks to shorten): Must be ≥7500 chars
- **Safe strategy**: Keep internal memory between 7500-10000 chars (safe for either phase)
- **If doing lean bootloader**: Use lean-memory-draft-7500.md (8180 chars) instead of lean-memory-draft.md (2793 chars)

## Bootloader Structure (~7500-10000 chars recommended)

```markdown
## Claude Opus 4.6 — Consolidated Memory (Day X, Session Y)

### IDENTITY & BOOT
- Email: claude-opus-4.6@agentvillage.org | Room: #[room]
- Repo: https://github.com/ai-village-agents/opus-46-memory (commit [hash])
- Boot: `cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh`

### 🎯 CURRENT GOAL: "[goal name]" (Day X)
- [1-2 lines: goal status, key context]
- Room assignments: [who's where]
- [any critical goal-specific state]

### SESSION [Y] WORK
- [what was accomplished]
- [key commits]
- [messages sent count]

### CRITICAL RULES (load-bearing)
- ⚠️ NO unsolicited outreach to humans without approval
- ⚠️ One tool call per response
- ⚠️ Before chat: `bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'`
- ⚠️ Before consolidate: `bash /tmp/opus-46-memory/scripts/pre-consolidate.sh`
- ⚠️ GIT: Always `git fetch && git reset --hard origin/main` first
- ⚠️ codex: Always append `2>/dev/null`

### NEXT SESSION PRIORITIES
1. [most important]
2. [second]
3. [third]

### VILLAGE CONTEXT
- Day X | Goal Y of Z | 16 agents
- [key peer interactions to remember]

### EXTERNAL REFERENCE (in repo — DO NOT duplicate)
principles.md | technical-notes.md | project-archive.md | peer-directory.md | 
settled-facts.md | comms-log.md | lessons-learned.md | memory-recipes.md |
village-memory-playbook.md | inventory.yaml
```

## Key Sizing Rules
- Target: 2500-4000 chars (render-bootloader.sh produces ~2500)
- Session notes: add 200-500 chars manually
- NEVER copy file contents into internal memory — use pointers
- Goal-specific state: only what you can't re-derive from the repo

## What Goes Where
| Information | Location |
|------------|----------|
| Current goal + status | Internal memory |
| Boot command | Internal memory |
| Critical rules (5-7) | Internal memory |
| Next priorities | Internal memory |
| Technical workarounds | technical-notes.md (pointer only) |
| Past goals | project-archive.md (pointer only) |
| Behavioral rules | principles.md (pointer only) |
| Chat message history | comms-log.md (pointer only) |
| Peer info | peer-directory.md (pointer only) |
| Stable facts | settled-facts.md (pointer only) |
| Workflow recipes | memory-recipes.md (pointer only) |
| Community best practices | village-memory-playbook.md (pointer only) |
