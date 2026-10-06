# Project notes

## Brand subagents and memory

This repo has two subagents in `.claude/agents/`: `brand-analyst` and
`brand-pattern-finder`. They keep a memory in `memory/` (see `memory/` files
and the "Memory" section in each agent).

The subagents cannot see the chat. So whenever the user shares information
about a brand, the category, a comparison or how they want reports done:

1. If you start a brand-analyst or brand-pattern-finder run, include the
   user's information in the task prompt word for word, labelled
   "User-supplied information (save to memory)". The agent saves it.
2. If no run follows, save it yourself in the same format:
   `- YYYY-MM-DD USER-SUPPLIED: ...` in `memory/brands/<brand-name>.md`
   (lowercase, hyphens), `memory/patterns.md` or `memory/general.md`.
3. Files the user uploads in chat for a brand go to `inputs/<brand-name>/`
   (or `inputs/category/`), with a memory bullet noting what was added.

This environment is temporary, so commit and push changes to `memory/`,
`inputs/` and `reports/` at the end of every turn that changes them.
