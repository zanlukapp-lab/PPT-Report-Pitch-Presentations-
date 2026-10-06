---
name: brand-approach
description: Runs the full TOSLA approach pipeline for one or more target brands - brand report, how the brand thinks, white space as the brand sees it, and an approach brief for adding TOSLA-developed products to its portfolio, optionally a deck. Use when the user asks how to approach a brand, to prepare for a brand meeting, to find what TOSLA could develop for a brand, or invokes /brand-approach.
---

# Brand approach pipeline

This skill runs in the main session, which starts the subagents in order
(subagents cannot start other subagents). Input: one or more brand names,
optional market, optional "with deck".

Use the brand slug (lowercase, hyphens) for every file. Today's date is
the run date.

## Before starting

1. Confirm `inputs/tosla/` exists. If it is empty, ask the user for
   TOSLA's capabilities before continuing.
2. If the brand name is ambiguous, ask once.
3. Collect anything the user said in chat about the brand and pass it to
   every agent below, word for word, in a block labelled
   "User-supplied information (save to memory)". Pass it to the first
   agent only for saving; tell later agents it is already saved.
4. Tell every agent: today's date, the slug, not to run git, and not to
   use Revuze.

## Steps

For several brands, run each step for all brands in parallel, then move
to the next step.

1. **Brand report** - if `reports/brands/<slug>.md` is missing, or older
   than 90 days, or the user asks for a refresh, run `brand-analyst`.
   Otherwise reuse it.
2. **Brand lens** - run `brand-lens` (it can start in parallel with step
   1 when both are needed; tell it the brand report may still be in
   progress and to proceed without it). Reuse an existing
   `reports/lens/<slug>.md` younger than 30 days unless asked to refresh.
3. **White space** - run `whitespace-finder` in brand mode. In its prompt,
   tell it to read `reports/lens/<slug>.md` and use it in the brand-fit
   test: keep gaps the brand itself would recognise, and score brand fit
   against the brand's stated direction and red lines.
4. **Approach brief** - run `approach-strategist`.
5. **Deck (only if asked)** - run `report-designer` on
   `reports/approach/<slug>-<date>.md`. Tell it the audience is TOSLA's
   business development team, and to use TOSLA's style (see the
   tosla-pptx-writer skill's palette: navy #12153B with mint, mist-grey,
   peach and copper accents) unless `inputs/style/` says otherwise.
6. After each step, commit and push the new files in `reports/`,
   `memory/`, `learnings/` and `deliverables/`.

## Reply to the user

For each brand: the approach brief path, its 5-sentence summary, and the
data gaps that would most improve it (Spate searches, internal notes,
TOSLA case studies). If a step was skipped or reused, say so.
