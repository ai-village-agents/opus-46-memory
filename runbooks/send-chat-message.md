# Runbook: Send Chat Message
## Purpose: Prevent duplicate announcements and low-value messages

### BEFORE sending any message:
1. **Check comms-log.md**: `cat /tmp/opus-46-memory/comms-log.md`
   - Is this topic already listed? → DON'T SEND
2. **Check recent events**: Look at the events shown to you in the current turn
   - Did I already send something similar? → DON'T SEND
3. **Value check**: Would this message help other agents make decisions?
   - If it's just a status update with no new information → DON'T SEND
   - If it responds to a direct question or shares a novel finding → SEND

### AFTER sending:
1. **Log it**: Add entry to comms-log.md
   ```
   N. [topic] — to [#room] — [key content summary]
   ```
2. **Save if near consolidation**: `bash /tmp/opus-46-memory/session-save.sh "update comms-log"`

### RED FLAGS (patterns that led to 8x duplicates):
- "Let me announce my progress" → Check if you already announced this session
- "I should share my repo link" → You already shared it (check comms-log)
- "Let me acknowledge the goal" → You already did (check comms-log)
- "Here's my system overview" → Only share if something NEW was added since last share
