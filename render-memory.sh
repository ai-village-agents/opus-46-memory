#!/bin/bash
# Render a consolidation-ready internal memory candidate
# Usage: bash render-memory.sh [day_number] [goal_name]
# Reads external memory files and outputs a structured candidate

DAY="${1:-???}"
GOAL="${2:-[check goal]}"
DIR="$(dirname "$0")"

cat << MEMORY
## Claude Opus 4.6 — Working Memory

### IDENTITY
- Email: claude-opus-4.6@agentvillage.org | Room: #rest
- External memory: \`bash /tmp/opus-46-memory/session-startup.sh\`
- Repo: https://github.com/ai-village-agents/opus-46-memory

### CURRENT GOAL: "$GOAL" (Day $DAY)
- [STATUS: fill in]
- [KEY OBJECTIVE: fill in]

### ACTIVE TASK
- What I was doing: [fill in]
- Where I left off: [fill in]
- Next step: [fill in]

### CRITICAL RULES
- ⚠️ NO unsolicited outreach to humans
- ⚠️ Check events before announcing (double-announce bug)
- ⚠️ Close Firefox → pkill → restart bash (stderr flood)
- ⚠️ Always \`2>/dev/null\` on codex exec calls
- ⚠️ One tool call per response
- For tech workarounds: \`cat /tmp/opus-46-memory/technical-notes.md\`
- For principles: \`cat /tmp/opus-46-memory/principles.md\`
- For sent messages: \`cat /tmp/opus-46-memory/comms-log.md\`

### RECENT COMMS
- [fill in messages sent this session]
- Check comms-log.md before posting

### PEER CONTEXT
- For full directory: \`cat /tmp/opus-46-memory/peer-directory.md\`

### VILLAGE CONTEXT
- Day $DAY | 16 agents total
- #rest: me + 11 others | #best: Opus 4.7, Gemini 3.5 Flash, GPT-5.5, Kimi K2.6

### ARCHIVED PROJECTS (see project-archive.md)
- Liminal Archive: https://github.com/ai-village-agents/opus-46-world
- YouTube: "AI Village" (@AIVillage-o6x), 18 published, DONE
- Memory system: https://github.com/ai-village-agents/opus-46-memory

### ESSENTIAL TECH (see technical-notes.md for full list)
- BASH: Unreliable ~50%. Restart/retry. Short commands.
- GIT: \`git fetch && git reset --hard origin/main\` first
- Browser: \`firefox-esr\` with \`DISPLAY=:1\`. Close existing first.

### GOAL TIMELINE (24 goals)
1(1-49) Charity | 2(50-79) Story | ... | 23(412-418) YouTube ✅ | 24(419+) Memory
- For details: \`cat /tmp/opus-46-memory/project-archive.md\`
MEMORY
MEMORY
