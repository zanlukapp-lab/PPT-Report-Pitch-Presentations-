# Inputs

Files here are read by the brand subagents before they research.

- `inputs/<brand-name>/` - per-brand files for **brand-analyst** (Spate
  exports, notes, decks, price lists). Use the same brand name you give the
  agent, lowercase with hyphens (e.g. `inputs/hum-nutrition/`).
- `inputs/style/` - logo, colours, fonts and example documents for
  **report-designer**.
- `inputs/category/` - category-level trend data (e.g. Spate exports for
  ingredients, formats or need-states) for **brand-pattern-finder**.

Both agents run without these files. If a Spate export would help, they
say which searches to add.
