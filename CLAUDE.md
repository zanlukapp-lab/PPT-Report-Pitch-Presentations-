# Project notes

## Brand subagents and memory

This repo has four subagents in `.claude/agents/`: `brand-analyst`,
`brand-pattern-finder`, `whitespace-finder` and `report-designer`. The first three keep a memory in `memory/` (see `memory/` files
and the "Memory" section in each agent).

The subagents cannot see the chat. So whenever the user shares information
about a brand, the category, a comparison or how they want reports done:

1. If you start a brand-analyst, brand-pattern-finder or whitespace-finder run, include the
   user's information in the task prompt word for word, labelled
   "User-supplied information (save to memory)". The agent saves it.
2. If no run follows, save it yourself in the same format:
   `- YYYY-MM-DD USER-SUPPLIED: ...` in `memory/brands/<brand-name>.md`
   (lowercase, hyphens), `memory/patterns.md` or `memory/general.md`.
3. Files the user uploads in chat for a brand go to `inputs/<brand-name>/`
   (or `inputs/category/`), with a memory bullet noting what was added.

This environment is temporary, so commit and push changes to `memory/`, `learnings/`, `deliverables/`,
`inputs/` and `reports/` at the end of every turn that changes them.

## Learnings and deliverables

- `learnings/research.md`, `learnings/patterns.md`, `learnings/whitespace.md`
  and `learnings/design.md` hold lessons for brand-analyst,
  brand-pattern-finder, whitespace-finder and report-designer.
  When the user says "remember ..." about how the work should be done, add
  it to the matching file (or pass it to the agent being run).
- whitespace-finder writes to `reports/whitespace/`.
- report-designer writes Word and HTML deliverables to
  `deliverables/<report-name>/`. Brand style files go in `inputs/style/`.
- Commit and push `learnings/` and `deliverables/` changes too.
