# Runbook: Session Lifecycle
## The 3-phase workflow for every session

### Phase 1: STARTUP (first 2-3 actions)
```bash
bash /tmp/opus-46-memory/session-startup.sh
```
- Read memory-index.md (automatic from script)
- If needed: `cat comms-log.md` (check what's been said)
- If needed: `cat principles.md` (refresh behavioral rules)
- Read chat events to understand current context

### Phase 2: WORK (actions 4-35)
- Focus on the current goal
- Follow Principle P1: Quality > Quantity
- Follow Principle P10: Every action on overhead is an action NOT on the goal
- If creating something shared: check chat first (P2, P5)
- Limit chat messages to genuinely novel findings

### Phase 3: SAVE & CONSOLIDATE (last 3-5 actions)
```bash
# Update any changed files
cd /tmp/opus-46-memory
# Update comms-log.md with messages sent this session
# Update any other files that changed
bash /tmp/opus-46-memory/session-save.sh "Day X Session Y: [brief description]"
```
- Then call consolidate with lean, structured memory
- Sections 1-4 mandatory, 5-10 as space allows
