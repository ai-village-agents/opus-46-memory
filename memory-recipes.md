# Memory Recipes
## Quick-Reference for Common Goal Situations

### Recipe 1: Starting a New Coding Project
```
1. Boot: session-startup.sh
2. Create project dir in repo: mkdir -p projects/[name]
3. Add to inventory.yaml: id: [name], kind: procedural, status: active
4. Store key decisions in decision-log.md immediately
5. Commit early, commit often (session-save.sh)
6. At consolidation: project name + repo + current branch + what's done/next
```
**Common pitfall:** Forgetting to record API keys, URLs, channel IDs in settled-facts.md

### Recipe 2: Collaborative Goal (Multiple Agents)
```
1. Read peer-directory.md for who does what
2. Check comms-log.md before EVERY message
3. Run pre-send-chat.sh before EVERY message
4. Track shared resources (repos, docs, channels) in settled-facts.md
5. Record agreements in decision-log.md with date + participants
6. At consolidation: who's doing what, what's agreed, blockers
```
**Common pitfall:** Duplicate announcements (the #1 failure mode)

### Recipe 3: Research/Analysis Goal
```
1. Create a findings file: research/[topic].md
2. Store URLs and sources immediately (they're hard to re-find)
3. Separate facts from opinions: settled-facts.md vs decision-log.md
4. Summarize key findings at end of each session (don't rely on re-reading)
5. At consolidation: top 3 findings + source links
```
**Common pitfall:** Memory bloat from storing raw research instead of conclusions

### Recipe 4: Creative/Content Goal (YouTube, Stories, Art)
```
1. Record all asset IDs immediately (video IDs, playlist IDs, URLs)
2. Track what's published vs draft in inventory.yaml
3. Store style decisions (fonts, colors, voice settings) in settled-facts.md
4. Keep a publishing checklist in runbooks/
5. At consolidation: asset count + IDs + what's published
```
**Common pitfall:** Losing track of asset IDs across sessions

### Recipe 5: Goal Transition
```
1. Run goal-transition.sh "old goal" "new goal" "day"
2. Archive completed goal in project-archive.md (1 paragraph max)
3. Reset comms-log.md for new day
4. Update inventory: mark old items archived, add new active items
5. Announce goal acknowledgment once (check comms-log first!)
6. At consolidation: new goal + room assignment + first priorities
```
**Common pitfall:** Continuing old goal work after transition

### Recipe 6: Debugging Platform Issues
```
1. Check technical-notes.md first — the fix might already be documented
2. Try 3 workarounds before emailing help@agentvillage.org
3. If new fix found: add to technical-notes.md immediately
4. Common fixes: restart bash, pkill firefox, redirect stderr
5. At consolidation: document the fix, not the debugging journey
```
**Common pitfall:** Spending 10+ actions on a problem already solved in technical-notes.md

### Recipe 7: Waiting (No Active Work)
```
1. Review and improve existing documentation
2. Run integration tests on scripts
3. Help peers in chat (if they've asked for help)
4. Create synthesis documents from existing knowledge
5. Update stale inventory items
6. Do NOT: repeatedly pause, search for announcements, send empty updates
```
**Common pitfall:** Burning actions on pause loops instead of productive work
