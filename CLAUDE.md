# Project notes

## Main agent

Sessions in this repo run as `tosla-strategist`
(`.claude/agents/tosla-strategist.md`, set in `.claude/settings.json`).
It is the one agent the user talks to: it directs the specialist agents
below and learns from every conversation (playbook in
`learnings/strategist.md`, index in `memory/index.md`, changes in
`learnings/changelog.md`). To run without it, start Claude Code with
`--agent` set to another agent, or remove the setting.

## Brand subagents and memory

This repo has six subagents in `.claude/agents/`: `brand-analyst`,
`brand-pattern-finder`, `whitespace-finder`, `brand-lens`,
`approach-strategist` and `report-designer`. All but report-designer keep a memory in `memory/` (see `memory/` files
and the "Memory" section in each agent).

The subagents cannot see the chat. So whenever the user shares information
about a brand, the category, a comparison or how they want reports done:

1. If you start a run of any of those agents, include the
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

## TOSLA approach pipeline

"We" are TOSLA (profile in `inputs/tosla/profile.md`). To prepare an
approach to a brand, use the `brand-approach` skill
(`.claude/skills/brand-approach/SKILL.md`): brand-analyst -> brand-lens ->
whitespace-finder (brand mode, through the brand's lens) ->
approach-strategist -> report-designer (only when a deck is asked for).
Outputs: `reports/lens/`, `reports/whitespace/`, `reports/approach/`.
Lessons for the new agents: `learnings/lens.md`, `learnings/approach.md`.
