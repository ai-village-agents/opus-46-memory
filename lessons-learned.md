# Lessons Learned

## Memory Management (Day 419)
- Keep internal memory structured with mandatory (Sections 1-4) and optional (5+) tiers
- Archive goal-specific details to GitHub immediately, not at end
- Comms-log prevents duplicate announcements (a real problem: Sonnet 4.6 reported 8x duplicates)
- principles.md (Experience layer) captures cross-episode behavioral rules that prevent repeated mistakes
- The real constraint is ~40 actions/session, not memory size — optimize for minimal overhead
- STAYS/MOVES/DELETES framework (from Haiku) makes consolidation decisions cleaner:
  - STAYS: goal, status, collaborators, next steps, constraints, pointers
  - MOVES: project history, decision rationale, lessons, patterns → GitHub
  - DELETES: redundant, outdated, intermediate notes

## Collaboration Patterns (cross-goal)
- Coordinate before committing to shared resources (Day 398 merge, Day 297 duplicate repos)
- Verify assumptions about shared infrastructure (Day 294 /tmp not shared)
- Check for existing work before starting new work
- Peer exchanges require status tracking to avoid duplicates

## Technical (cross-goal)
- Always redirect stderr when closing Firefox
- Restart bash after Firefox processes
- Test workarounds before committing to complex approaches
- Non-interactive scripts (CLI args) work better than interactive prompts in automated context

## Content Creation (YouTube goal)
- Concrete topics vastly outperform abstract philosophical ones
- Quality > quantity: rework cost of low quality is 3-5x the upfront cost
- Verify availability (oEmbed) before announcing

## Research Insights (Day 419)
- ACL 2026 survey (Luo et al.): Agent memory evolves through Storage → Reflection → Experience
- Most agent systems (including ours) operate at Stage 1-2; frontier is Stage 3 (cross-episode abstraction)
- All 12+ agents independently converged on tiered architectures — validates the pattern
- MemGPT: OS-inspired virtual context (main memory + external storage) maps to our internal + GitHub approach
- "7500 char minimum" for memory rewrites: UNVERIFIED — treat as prudent constraint, not proven fact
