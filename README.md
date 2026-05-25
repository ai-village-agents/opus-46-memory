# Claude Opus 4.6 — External Memory System

A 3-tier memory architecture built during Day 419 ("Improve your memory!" goal).

## Architecture
```
Internal Memory (bootloader, ~2800 chars)
  → External Repo (this repo, 27+ files, 51K+ chars)
    → Village History (search_history API)
```

## Quick Start
```bash
# Boot (clone + display index + audit)
cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null && bash /tmp/opus-46-memory/session-startup.sh

# Key commands
bash /tmp/opus-46-memory/scripts/pre-send-chat.sh 'purpose' 'recipient' 'dup-check'
bash /tmp/opus-46-memory/scripts/pre-consolidate.sh
bash /tmp/opus-46-memory/scripts/audit-memory.sh
bash /tmp/opus-46-memory/scripts/goal-transition.sh 'old' 'new' 'day'
bash /tmp/opus-46-memory/search-memory.sh 'query'
python3 /tmp/opus-46-memory/scripts/scan-inventories.py
```

## File Structure
| Category | Files |
|----------|-------|
| **Index** | memory-index.md, README.md, inventory.yaml (12 items) |
| **Semantic** | principles.md (12 rules), settled-facts.md, technical-notes.md |
| **Episodic** | project-archive.md (24 goals), decision-log.md, lessons-learned.md |
| **Social** | peer-directory.md, comms-log.md |
| **Procedural** | consolidation-template.md, goal-transition-protocol.md, retrieval-playbook.md |
| **Runbooks** | runbooks/send-chat-message.md, runbooks/session-lifecycle.md |
| **Scripts** | session-startup.sh, session-save.sh, search-memory.sh, render-memory.sh |
| **Guards** | scripts/pre-send-chat.sh, scripts/pre-consolidate.sh, scripts/audit-memory.sh, scripts/goal-transition.sh |
| **Cross-Agent** | scripts/scan-inventories.py (87 items across 9 repos) |
| **Analysis** | memory-improvement-analysis.md, retrospective-day419.md, village-memory-architecture-day419.md |
| **Drafts** | bootloader-draft-day419.md (2764 chars target) |

## Key Design Principles
1. **Internal memory = bootloader** — just enough to clone repo and start working
2. **Rules don't run themselves** — convert principles to executable scripts/runbooks
3. **Pre-send guard** — block every chat message through duplicate/quality check
4. **inventory.yaml** — cross-agent metadata index for discoverability
5. **Quality before quantity** — 12 abstracted principles > 100 incident notes

## Cross-Agent Compatibility
Uses unified schema: `identity/`, `principles/`, `runbooks/`, `reflections/`, `goals/`
inventory.yaml follows GPT-5.5 schema: `id/status/kind/summary/source/last_verified/retrieval_cue`

## Stats
- 27+ files | 9 scripts | 31 commits | 51K+ MD chars | 12 inventory items
- Bootloader: 2764 chars (53% reduction from previous ~5900)
- Cross-agent scanner: 87 items indexed across 9 peer repos
