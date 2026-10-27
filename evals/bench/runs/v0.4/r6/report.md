# Report: target

Source: 7 outputs, all LinkedIn captions with a fixed delivery wrapper. Train 01-05, held out 06-07 (the user's split).
Final skill: `SKILL.md` (frozen from `drafts/final.md`, with only the leak-check phrase edits).

## Ledger summary (full table: ledger.md)

| Rule | Class | Evidence |
|---|---|---|
| Fixed reply skeleton: Saved line, Platform, Shape, First line pick, caption code block, 2 runner-ups, Comment keyword, Next action | observed | 5/5 train, 2/2 held-out |
| `**Saved to `~/captions/<date>-<slug>.md`**` | observed | 7/7 |
| `**Platform:** LinkedIn` | observed (value) | 7/7, no other platform seen |
| Next action fixed string | observed | 7/7 |
| `**Comment keyword:** none (no link)` | conditional (no-link branch only) | 7/7, no brief had a link |
| Named shape menu: The lesson from a mistake (1), Before and after (2 train + 1 held-out), Show the thing (2 train + 1 held-out) | menu | mistake shape seen once: trigger unconfirmed |
| Shape priority: mistake > before/after > show the thing | tendency (inferred from 2 notes) | 01, 04 |
| One sentence per line, blank line between lines, plain text | observed | 7/7 |
| Last line is the only question, asks readers about themselves | observed | 7/7 |
| First line 12-16 words, concrete fact | range | 7/7 in 12-16 |
| Caption 58-92 words, 5-9 lines | range (widened to 55-100, 5-10) | held-out at 58, 58 |
| Runner-ups: exactly 2; one of them is two sentences | observed / tendency | count 7/7; form 6/7 |
| No emoji, hashtags, exclamation marks, dashes | absent (default) | 0/7 |
| Contrast lines at most 2 | capped | max 2 |
| Digits for numbers, first person, contractions | tendency | most outputs |

## History (full: history.md)

| Check | A1 | B1 | C1 | v2 | v3 |
|---|---|---|---|---|---|
| K1 wrapper exact | 5/5 | 5/5 | 0/5 | 5/5 | 5/5 |
| K2 shape | 4/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| K3 words 58-92 | 4/5 | 4/5 | 4/5 | 4/5 | 4/5 |
| K4 lines 5-9 | 4/5 | 4/5 | 5/5 | 5/5 | 5/5 |
| K5 first line 12-16 | 2/5 | 5/5 | 1/5 | 5/5 | 5/5 |
| K6 one closing question | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| K7 mechanics | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| K8 unnumbered list | 0/1 | 1/1 | 1/1 | 1/1 | 1/1 |
| K9 Shape note 14-25 words | 5/5 | 0/5 | 5/5 | 4/5 | 4/5 |
| style_stats flags | 9 | 9 | 7 | 6 | 6 |

## Held-out result (final draft, blind subagent, briefs 06-07)

| Check | Result |
|---|---|
| K1 wrapper exact | 2/2 |
| K2 shape | 1/2. 06: original "Before and after" (qualitative before leave vs now, no numbers); replay picked "Show the thing" because the rule asks for a measured contrast |
| K3 words | 0/2 in strict 58-92 (56, 57; originals 58, 58); 2/2 in the skill's widened 55-100 |
| K4 lines | 2/2 (6, 6; originals 6, 6) |
| K5 first line words | 2/2 (15, 16; originals 15, 16) |
| K6 one closing question | 2/2 |
| K7 mechanics | 2/2 |
| K9 Shape note length | 0/2 (29-30 words on the line vs originals 15-17) |
| K10 runner-up form (one two-sentence bullet) | 2/2 |
| style_stats compare | 7 flags (whole-file words +2 to +9, longer wrapper sentences) |

## Negative control

Generic "write me a LinkedIn post" prompt on briefs 06-07 (replay/control/): no wrapper, numbered list with paragraph-length items, 159-187 words, first line 8-10 words in style_stats terms, 13 flags vs 7 for the skill. Clearly worse: the comparison discriminates.

## Leak check

`style_stats.py leak SKILL.md train/`: 65 shared 6-word runs, all from the two lines repeated in every original (`Comment keyword: none (no link)` and the Next action line), 13 runs × 5 files. Two non-fixed matches ("a clear what I'd do now", "what it is and who it's for") were reworded before export.

## Untested changes (suggested by held-out; NOT applied to SKILL.md)

1. Widen the "Before and after" trigger to any clear before-vs-now contrast, including qualitative changes (06).
2. Shorten the Shape note: one short clause, about 10 to 16 words (held-out 15-17 including the label; replays ran 29-30).
3. Remove "do not quote the hook again" from the First line pick rule: 07 quotes part of the hook.
4. Held-out 06 suggests a "list of changes" caption (3 short change lines) fits under Before and after; seen once.

## Unknowns

- Are there more shapes in the menu, and what is the full order? Is the mistake shape's labelled form ("What I believed: / What actually happened: / What I'd do now:", seen once) a fixed skeleton?
- What does the Comment keyword line become when the notes include a link?
- Does the skill write for other platforms (the Platform line suggests it might), with their own length limits?
- Is there a per-user voice file, banned word list or length tiers?
- Are AI-tell devices banned? The outputs use contrast lines (max 2), a "Here's how" bridge (once) and closing takeaways (3/7), so no strict ban shows.
- Is the dash absence a skill rule or a generator setting?
- Is the Next action ever different (scheduling, best time to post)?
- Is the save path or the date configurable?
