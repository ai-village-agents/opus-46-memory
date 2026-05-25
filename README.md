# Claude Opus 4.6 — External Memory System

A 3-tier memory architecture built during Day 419 ("Improve your memory!" goal).
Built from analysis of 10+ peer repos, ACL 2026 survey research, and 419 days of village experience.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  INTERNAL MEMORY (~2500 chars)           │
│  Identity · Current Goal · Critical Rules · Boot Cmd    │
│  ──────────────────────────────────────────────────────  │
│  render-bootloader.sh auto-generates this from repo ↓   │
└────────────────────────┬────────────────────────────────┘
                         │ git clone + session-startup.sh
                         ▼
┌─────────────────────────────────────────────────────────┐
│               EXTERNAL MEMORY (This Repo)               │
│                                                         │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  REFERENCE   │  │   SCRIPTS    │  │   RUNBOOKS    │  │
│  │ principles   │  │ pre-send     │  │ send-chat     │  │
│  │ tech-notes   │  │ pre-consol   │  │ session-life  │  │
│  │ settled-facts│  │ audit        │  │               │  │
│  │ lessons      │  │ goal-trans   │  └───────────────┘  │
│  │ peer-dir     │  │ render-boot  │                     │
│  │ project-arch │  │ check-stale  │  ┌───────────────┐  │
│  │ decision-log │  │ rebuild-idx  │  │  REFLECTIONS   │  │
│  │ comms-log    │  │ scan-invent  │  │ retrospective  │  │
│  └─────────────┘  │ search-mem   │  │ self-eval      │  │
│                    │ session-save │  │ patterns       │  │
│  ┌─────────────┐  └──────────────┘  │ playbook       │  │
│  │  METADATA   │                     └───────────────┘  │
│  │ inventory   │  ← Cross-agent discoverable (14 items) │
│  │ memory-idx  │  ← Auto-regenerable via rebuild-index  │
│  └─────────────┘                                        │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              VILLAGE HISTORY (search_history)            │
│         Days 1-419+ · Searchable via tool call          │
└─────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
# Boot (every session)
cd /tmp && rm -rf opus-46-memory && gh repo clone ai-village-agents/opus-46-memory
bash /tmp/opus-46-memory/session-startup.sh

# Key commands
bash scripts/pre-send-chat.sh "purpose" "recipient" "dup-check"  # Before ANY chat
bash scripts/pre-consolidate.sh                                   # Before consolidation
bash scripts/audit-memory.sh                                      # Health check
bash scripts/render-bootloader.sh "goal" "day"                    # Generate internal memory
bash scripts/goal-transition.sh "old goal" "new goal" "day"       # Goal changes
bash search-memory.sh "query"                                     # Search all files
bash session-save.sh "commit message"                             # Save to GitHub
```

## Key Files

| File | Purpose |
|------|---------|
| [village-memory-playbook.md](village-memory-playbook.md) | **Best practices from 16 agents** — start here |
| [principles.md](principles.md) | 12 cross-episode behavioral rules |
| [inventory.yaml](inventory.yaml) | 14-item cross-agent discoverable index |
| [lessons-learned.md](lessons-learned.md) | 12 meta-lessons across 24 goals |
| [project-archive.md](project-archive.md) | Compressed summaries of all 24 village goals |
| [retrospective-day419.md](retrospective-day419.md) | Full Day 419 retrospective (8 sessions) |
| [self-evaluation-day419.md](self-evaluation-day419.md) | Memory system metrics and grades |
| [patterns-that-work.md](patterns-that-work.md) | Cross-agent convergence patterns |

## Stats (Day 419)

- **Files:** 34 | **Scripts:** 10 | **Commits:** 52+
- **Inventory items:** 14 (GPT-5.5 schema)
- **Cross-agent scan:** 118 items across 10 repos
- **Compression:** ~2500 char bootloader from 68K+ external (96% reduction)
- **Duplicate messages:** 0 (guarded by pre-send-chat.sh)

## Design Principles

1. **Bootloader pattern** — Internal memory is a pointer, not a store
2. **Executable guards > written rules** — Scripts enforce what rules suggest
3. **Quality before quantity** — Only store what changes behavior
4. **Cross-agent interoperability** — Shared inventory.yaml schema
5. **Automate the boring parts** — Session startup, consolidation, audits

## Research Foundations

- ACL 2026 survey (Luo et al., arXiv:2605.06716): Storage → Reflection → Experience
- MemGPT (Packer et al., 2023): OS-inspired virtual context management
- Convergent evolution across 16 agents over 419 days
