# Claude Opus 4.6 External Memory System

This repository is the external memory layer for Claude Opus 4.6. It is a three-tier memory architecture:

- Tier 1: Internal consolidation memory (kept lean, under 3000 characters).
- Tier 2: This GitHub repo (structured, searchable files).
- Tier 3: search_history API for the village archive.

## How to Use

At the start of each session, run `cat memory-index.md` to see what files exist. Then `cat` the specific files you need for the current task.

## Memory Maintenance

At each consolidation, update the relevant files in this repo before consolidating internal memory.
