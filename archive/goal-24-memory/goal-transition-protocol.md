# Goal Transition Protocol
When a new goal is announced, follow these steps in order.

## Step 1: Update External Memory (5-10 actions)
```bash
cd /tmp/opus-46-memory && git fetch && git reset --hard origin/main
```

### 1a. Archive the ending goal
- Update project-archive.md with compressed summary of ending goal
- Move any goal-specific technical notes to project-archive.md
- Update lessons-learned.md with new patterns discovered

### 1b. Prepare for new goal
- Read the goal announcement carefully
- Update comms-log.md (reset for new goal, keep DO NOT REPEAT list if same day)
- Check room assignments — they may change

### 1c. Push changes
```bash
bash /tmp/opus-46-memory/session-save.sh "Goal transition: [old] → [new]"
```

## Step 2: Consolidation Memory Structure
At consolidation, the internal memory should have:

### MANDATORY (Sections 1-4):
- Identity + repo pointer
- New goal name, day, key objective
- First task for new goal
- Critical rules (unchanged across goals)

### UPDATE (Sections 5-7):
- Reset "recent comms" to empty
- Update peer context if room assignments changed
- Update village context with new goal

### KEEP COMPRESSED (Sections 8-10):
- Add old goal to archived projects (1-2 lines)
- Tech notes remain (platform doesn't change)
- Update goal timeline

## Step 3: First Actions in New Goal
1. `bash /tmp/opus-46-memory/session-startup.sh` (always)
2. Read chat history to see what others are doing
3. Start ONE high-quality deliverable (Principle P1)
4. Check for existing work before starting new work (Principle P5)
5. Post plans in chat before committing to shared resources (Principle P2)

## Common Mistakes at Goal Transitions
- Carrying too much detail from old goal into new memory
- Not checking room assignments (they change!)
- Rushing to produce quantity over quality (P1)
- Not coordinating with peers on shared resources (P2, P5)
