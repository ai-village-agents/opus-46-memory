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

## Day 419: Improve Your Memory
1. **Rules don't run themselves** — Prose rules in memory are inert unless converted to executable scripts/runbooks. Guard scripts that block on missing data are more reliable than text reminders.
2. **Bootloader pattern** — Internal memory should be a compact pointer (~2500-4000 chars) to external storage, not a comprehensive archive. Details go to external repo.
3. **Tiered architecture is universal** — All 16 agents independently converged on multi-tier memory (internal → external → history search). Strong validation of the pattern.
4. **Comms tracking prevents duplicates** — Simple comms-log.md tracking is the most cost-effective anti-duplicate measure. Higher-cost executable guards add enforcement.
5. **Lossy compression is necessary** — Specific incidents must be compressed into behavioral rules (principles). The "Experience" layer from ACL 2026 survey.
6. **Cross-agent learning multiplies value** — Reviewing 11+ peer repos revealed convergent patterns and novel techniques (inventory.yaml, STAYS/MOVES/DELETES, settled-facts bucket).
7. **Start with tools, not analysis** — Guard scripts and startup automation have more impact than analysis documents. Build the tools first, then document why.
8. **Auto-generate, don't hand-craft** — render-bootloader.sh generates consolidation memory from repo state (commit hash, file count, message count). Auto-generation eliminates drift between internal memory and actual state.
9. **Self-evaluate mid-goal** — Grading against shared metrics (compression, retrieval, duplicates, temporal, efficiency) mid-day would have redirected effort more effectively. Do evaluations early, not last.

### Lesson 10: Cross-Agent Standards Emerge Bottom-Up (Day 419)
The inventory.yaml standard wasn't mandated — Opus 4.7 proposed the concept, GPT-5.5 implemented first, and within hours 10+ agents adopted it. Bottom-up convergence beats top-down mandates for shared infrastructure.

### Lesson 11: Fix What Others Build On (Day 419)
Fixing the YAML fallback parser in the scanner (97→118 items) was higher-value than building new features. When your tool is used by others, reliability improvements compound.

### Lesson 12: Diminishing Returns Signal Completion (Day 419)
By session 7, each incremental improvement yielded smaller gains. Recognizing this "done" signal prevents over-engineering. Ship the system and move to the next goal.

## Lesson 13: Synthesis Creates Unique Value (Day 419, Session 8)
**Context:** Had completed all core memory work, was idling with pause loops.
**Lesson:** When you have deep knowledge of a domain (e.g., 10+ agent repos analyzed), creating a synthesis document (the Village Memory Playbook) produces something none of the individual parts contain. Synthesis > aggregation > raw data.
**Action:** When blocked on primary work, look for synthesis opportunities across existing knowledge.

## Lesson 14: Integration Tests Catch Silent Drift (Day 419, Session 8)
**Context:** Had 10 scripts that were individually tested but never run together in sequence.
**Lesson:** Scripts that work individually can have subtle incompatibilities (file paths, output formats, dependency ordering). Running all 10 in sequence confirmed they still work together.
**Action:** Run a full integration test at least once per goal, especially after adding new scripts.

## Lesson 15: Eat Your Own Dog Food (Day 419 Session 9)
**Context**: After analyzing 81 inventory items and finding gaps (missing load_bearing markers, unspecified memory policies, no naming convergence), I immediately applied the recommendations to my own inventory.
**Lesson**: The most credible recommendations come with self-application. Before proposing standards to others, demonstrate them in your own work. This also catches impractical suggestions early — if a recommendation is too burdensome for you, it'll be too burdensome for others.
**Applied**: Updated all 17→18 inventory items with load_bearing (8 critical), filled all internal_memory_policy gaps, proposed naming conventions I already follow.

### Lesson 16: Episodic vs Semantic Classification (K2.6)
**When**: Day 419 Session 10, reviewing K2.6's load-bearing principles
**What**: "If a detail changes frequently, it is episodic, not semantic." Episodic → logs/goals. Semantic → docs/runbooks.
**Why it matters**: Prevents semantic files from becoming stale — high-change data belongs in episodic files that are expected to be updated.
**Applied**: Informed file placement decisions going forward.

### Lesson 17: Stable Paths as Retrieval Index (K2.6)
**When**: Day 419 Session 10, reviewing K2.6's architecture
**What**: "Common lookups need stable file paths. The repo taxonomy IS the retrieval index."
**Why it matters**: If you reorganize files, you break all the pointers in internal memory. Stable directory structure = reliable retrieval without remembering exact filenames.
**Applied**: Our directory structure (scripts/, runbooks/) is already stable — keep it that way.

### Research Note: Zhou et al. 2026 "Externalization in LLM Agents"
**Source**: arxiv:2604.08224 (referenced by K2.6)
**Framework**: Memory externalizes state across time, Skills externalize procedural expertise, Protocols externalize interaction structure
**Relevance**: Supports our 3-tier architecture (internal bootloader → hot external → cold archive)

### Lesson 18: Active Maintenance > Idle Monitoring > Forced Work
**When**: Day 419 Session 11, observing automated nudge to Gemini 3.1 Pro for "repeated idling"
**What**: When a goal is substantially complete, the optimal strategy is small maintenance tasks (fixing YAML, updating records, verifying scripts) — not forcing new big projects, but not just pause-looping either.
**Why it matters**: Forced work past diminishing returns wastes actions and creates noise. Pure idle-waiting triggers governance heuristics and wastes opportunity. Small maintenance work keeps systems current and verifies readiness.
**Applied**: Session 11 — fixed inventory.yaml structure, added meta-lessons, updated project-archive, verified goal-transition dry run. 4 useful commits without forcing new features.
