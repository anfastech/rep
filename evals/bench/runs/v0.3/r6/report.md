# Reverse-engineering report: target

Source: 7 outputs from one unknown skill (5 train: 01-05, 2 held out: 06-07, user's split). All are LinkedIn captions with a handover wrapper. Exported skill: `SKILL.md`. Workspace files: `briefs.md`, `ledger.md` (full evidence), `history.md`, `drafts/`, `replay/`.

## What was recovered (rule, class, evidence)

| Rule | Class | Evidence |
|---|---|---|
| Wrapper: Saved-to path `~/captions/<date>-<slug>.md`, Platform, Shape, First line pick, caption in code block, Runner-up first lines, Comment keyword, Next action | observed | 7/7 |
| Fixed strings: "Comment keyword: none (no link)", "Next action: Post it, and reply to every comment within the first hour." | observed | 7/7 |
| Exactly 2 quoted runner-up first lines | observed | 7/7 |
| Shape menu, checked in priority order: The lesson from a mistake > Before and after > Show the thing | conditional | 1/5, 2/5, 2/5 train; 06 Before and after, 07 Show the thing |
| Mistake shape uses "What I believed: / What actually happened: / What I'd do now:" lines | conditional | 1/1 mistake brief (01) |
| Playbook: "Here's how I ...:" then unnumbered tactic lines | conditional | 1/1 playbook brief (04) |
| One line per paragraph, blank line between every line | observed | 7/7 |
| Caption ends with one specific question to the reader | observed | 7/7 |
| First person (I for decisions, we for team results) | observed | 7/7 |
| Caption length | range | 58 to 92 words, 5 to 9 lines (train); 58, 58 (held out). Skill says about 55 to 100 |
| First line length | range | 12 to 16 words (train), 15 to 16 (held out). Skill says about 11 to 17 |
| Sentences per line | capped | max 3, mostly 1 |
| Comment keyword "none (no link)" | conditional | 7/7, all briefs had no link. The with-link branch was never seen |
| No emoji, hashtags, exclamation marks or em dashes | absent (default) | 0/7 |
| Contrast moves at most 2, triples at most 1 | capped | 0 to 2, 0 to 1 per caption |
| Contractions 2 to 5 | range/default | train 2 to 5 |

## History (per check, see history.md for detail)

| Check | A1 | B1 | C1 | v2 | v3/final |
|---|---|---|---|---|---|
| Wrapper and fixed strings | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Shape name verbatim | 5/5 | 5/5 | 3/5 | 5/5 | 5/5 |
| Shape matches original | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Caption words in range | 1/5 | 3/5 | 5/5 | 5/5 | 5/5 |
| Caption lines in range | 1/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| First line 12 to 16 words | 1/5 | 5/5 | 3/5 | 4/5 | 3/5 (all within 11 to 17) |
| Mean sentence length in range | 4/5 | 2/5 | 4/5 | 2/5 | 4/5 |
| Mistake labels | fail | pass | fail | pass | pass |
| Playbook list form | fail | pass | fail | pass | pass |
| Closing question | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Mechanics (no emoji, hashtags or em dashes) | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Contractions 2 to 5 | n/a | 2/5 | 2/5 | 2/5 | 2/5 |

The final draft is B1's structure and menu, plus C1's length targets and the v3 short-line rule. After round 3 it got one clarification that was not replayed: hyphenated words are fine (a replay agent had read "no dashes" as banning hyphens).

## Held-out result (2 outputs, frozen draft, blind replay)

| Check | 06 | 07 |
|---|---|---|
| Wrapper fields, order, fixed strings | pass | pass |
| Shape matches original | **FAIL** (original: Before and after; replay: Show the thing) | pass |
| Caption words (orig 58 / 58) | 69, pass | 59, pass |
| Caption lines (orig 6 / 6) | 6, pass | 6, pass |
| First line words (orig 15 / 16) | 12, pass (in range) | 17, pass (edge of range) |
| Body form matches original | fail (imperative playbook lines; the original uses plain "I ..." statements) | pass (one fact per line, a "no new platform" line, then the question) |
| Mean sentence length (style_stats, whole file) | over (16.3 vs 12 to 13) | over (14.4) |
| Closing question | pass | pass |
| Mechanics (no emoji, hashtags or em dashes) | pass | pass |
| Contractions (orig 3) | over (5 to 6) | over |
| Two quoted runner-ups | pass | pass |

style_stats `compare heldout/ replay/heldout/` flagged 6 features. `compare heldout/ replay/control/` flagged 13.

## Negative control

A generic prompt ("Write me a LinkedIn post about this") on the same 2 held-out briefs gave 158 and 171 words of caption (originals: 58 and 58). It had no wrapper, no runner-ups, no saved path, numbered and bulleted lists, multi-sentence paragraphs, and "no X, no Y, no Z" triples. It is clearly worse on every structural check, so the comparison discriminates.

## Leak check

`style_stats.py leak SKILL.md train/`: 65 shared 6-word runs. All of them come from the two fixed lines found in all 5 originals (Comment keyword, Next action), 13 runs per file. Two other matches were removed before export: a trigger phrase that echoed 01, and the example's Shape line, which only 01 contained. Those 2 lines were reworded, and the example now shows only the caption.

## Untested changes (suggested by held-out results; NOT applied to SKILL.md)

1. Widen the Before and after trigger. It should include a qualitative before/now contrast (habits before leave vs after), not only a measured number. Evidence: 06 is "Before and after" with no measured numbers.
2. For a Before and after made of several changes, the original lists the changes as plain first-person lines ("I delegate more.") after a bridge line ("That's one of three things that changed."), not as imperative tactics.
3. 07 suggests that a single measured result with no before-number (a team win) stays in Show the thing. The current skill already does this; it is noted here for confirmation.
4. Contractions run high in replays (up to 9); the originals use 2 to 5. A tighter contractions rule might help.

## Unknowns (questions for the user)

- Are there more shapes than the three seen (contrarian take, how-to, story)? The "highest-trust" wording implies a ranked list that may be longer.
- When the brief has a link, what does the comment keyword look like (for example "Comment X and I'll send it")? Where does the link go?
- Is the platform fixed to LinkedIn, or does the skill also write for other platforms with different rules?
- Are AI-tell devices banned ("Here's the thing" bridges, engagement bait, slogan closers)? None appeared, but contrast moves did (up to 2).
- Is there a per-user voice file that sets tone, CTA or banned words?
- Is there a character limit or a "see more" target for the first lines? Are there length tiers?
- Did the em dash absence come from the skill or from the generator's global settings?
- Is the "reply within the first hour" line always fixed, or does it change by platform?
- Does the skill really save the file to ~/captions, or is the "Saved to" line just packaging?
