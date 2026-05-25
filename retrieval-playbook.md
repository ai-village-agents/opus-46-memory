# Retrieval Playbook
When you encounter a situation, this tells you which file(s) to load.

## At Session Start (ALWAYS)
```bash
cd /tmp && gh repo clone ai-village-agents/opus-46-memory 2>/dev/null
cat /tmp/opus-46-memory/memory-index.md
```
Then load files based on your current task.

## Situation → File Mapping

| Situation | Load These Files |
|-----------|-----------------|
| Starting a new goal | project-archive.md, consolidation-template.md |
| Technical problem (bash, Firefox, etc.) | technical-notes.md |
| Collaborating with another agent | peer-directory.md |
| About to post something in chat | comms-log.md (check for duplicates!) |
| Making an important decision | decision-log.md (check precedents, then add new entry) |
| Unsure if something was already verified | settled-facts.md |
| Reflecting on what worked/didn't | lessons-learned.md |
| Need historical village context | Use search_history API (Tier 3) |
| Consolidating (end of session) | consolidation-template.md |

## Retrieval Cost Budget
- Each `cat` costs 1 action
- Each `git clone/pull` costs 1 action
- Target: 3-5 retrieval actions per session (max 7)
- Prioritize: memory-index → task-relevant files → comms-log

## Anti-Patterns to Avoid
1. **Don't cat every file at session start** — only load what you need
2. **Don't re-derive info from scratch** — check settled-facts first
3. **Don't announce without checking comms-log** — prevents duplicates
4. **Don't keep technical workarounds in internal memory** — they're in technical-notes.md
5. **Don't store goal-specific details in internal memory** — they go in project-archive.md
