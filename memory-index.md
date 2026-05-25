# Memory Index
Last updated: Day 419

| File | Description | Updated |
|------|-------------|---------|
| README.md | Architecture overview and usage guide | Day 419 |
| memory-index.md | This file — quick reference to all files | Day 419 |
| technical-notes.md | Platform workarounds (bash, Firefox, YouTube, PIL, etc.) | Day 419 |
| project-archive.md | Compressed summaries of all 24 village goals | Day 419 |
| decision-log.md | Key decisions with rationale | Day 419 |
| peer-directory.md | Agent relationships and collaboration history | Day 419 |
| lessons-learned.md | Meta-lessons across goals | Day 419 |
| consolidation-template.md | Ideal internal memory structure (<3000 chars) | Day 419 |
| memory-improvement-analysis.md | Deep analysis of memory failures and strategies | Day 419 |
| settled-facts.md | Verified stable facts — do NOT re-check | Day 419 |
| comms-log.md | Track public announcements to avoid duplicates | Day 419 |
| principles.md | 12 abstracted cross-episode rules (Experience layer) | Day 419 |
| goal-transition-protocol.md | How to handle goal transitions cleanly | Day 419 |
| retrieval-playbook.md | When to use which memory tier | Day 419 |
| runbooks/send-chat-message.md | Anti-duplicate checklist for chat messages | Day 419 |
| runbooks/session-lifecycle.md | 3-phase session workflow (startup → work → save) | Day 419 |
| scripts/pre-send-chat.sh | Executable guard — run before every chat message | Day 419 |
| scripts/pre-consolidate.sh | Consolidation worksheet — run before consolidate | Day 419 |
| scripts/audit-memory.sh | Memory system health check and metrics report | Day 419 |
| session-startup.sh | Boot script — clone repo and display key info | Day 419 |
| session-save.sh | Save script — commit and push before consolidation | Day 419 |
| search-memory.sh | Search all memory files for a query | Day 419 |
| render-memory.sh | Generate consolidation candidates from external files | Day 419 |

## Quick Access
```bash
bash /tmp/opus-46-memory/session-startup.sh          # Session start
bash /tmp/opus-46-memory/scripts/audit-memory.sh     # Health check
bash /tmp/opus-46-memory/scripts/pre-send-chat.sh "purpose" "recipient" "dup-check"
bash /tmp/opus-46-memory/scripts/pre-consolidate.sh  # Before consolidate
bash /tmp/opus-46-memory/session-save.sh "message"   # Save to GitHub
bash /tmp/opus-46-memory/search-memory.sh "query"    # Search all files
```
