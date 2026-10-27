# Reverse-engineering report: target

Source: 7 outputs (train 01-05, held out 06-07). Genre inferred: Instagram captions with a status card (125-character "more" cut, link in bio, alt text, reels and carousels).
Exported skill: `reverse-runs/target/SKILL.md` (frozen v3 plus leak-only wording edits).

## What the skill produces

1. A fenced caption block.
2. An alt-text line for carousels (`Alt text (cover slide): ...`) and images (`Alt text: ...`). Reels get none.
3. A fenced `CAPTION READY` card with the fields job / visible / ask / hashtags / search / first comment / linter.

## Ledger summary (full table in ledger.md)

| Rule | Class | Evidence |
|---|---|---|
| Caption block, then alt text, then card, in that order | observed | 7/7 (alt text only for non-reels: 4/4 non-reels, 0/3 reels) |
| `CAPTION READY` header, the field order, and values aligned to column 13 | observed | 7/7 |
| `linter:     READY, checked by hand against caption.py's rules` | observed, fixed string | 7/7 |
| `hashtags:   3`; exactly 3 lowercase hashtags on the last line | observed | 7/7 |
| `visible: n of 125 ...` where n is the exact length of line 1 | observed | 7/7 (checked by script) |
| Job A (the reel carries the hook) puts the ask on line 1; job B puts the hook on line 1 | conditional on format | A 3/3 reels, B 4/4 non-reels |
| Exactly one ask; in job B it is the last paragraph | observed | 7/7 |
| Ask type follows the goal: comment keyword, save, comment question, share, link in bio | conditional on goal | 1, 2, 2, 1, 1 of 7 |
| Takeaway paragraph before the end | conditional on story briefs | 3/3 train stories, 1/1 held-out story; absent in the list, announcement and reflection briefs |
| Numbered list items, one paragraph each | conditional on list/how-to briefs | 1/1 |
| Search phrases: 2, with true line numbers that count blank lines | observed | 7/7 |
| `first comment: none, ...`, no links in the caption | observed / conditional | 7/7; the bio wording appears only when the brief has a link (1/7) |
| Line-1 length | range | 73-111 characters, all ≤125 |
| Caption length | range | 74-138 words; 5-8 paragraphs |
| At most 3 sentences per paragraph | capped | max 3 |
| Contrast lines | capped | 0-2 per caption (cap unconfirmed) |
| No emojis, em dashes or exclamation marks; digits for data | absent/default | 0/7 for each |

## Replay history (details in history.md)

| Check | A1 strict | B1 menu | C1 loose | v2 | v3 |
|---|---|---|---|---|---|
| Structural checks (fences, card, alignment, fixed strings, tags, alt rule, mechanics) | 5/5 | 5/5 | 5/5 | 5/5 | 5/5 |
| Search line numbers correct | 5/5 | 5/5 | 0/5 | 5/5 | 5/5 |
| Line-1 length in the original band | 1/5 | 2/5 | 3/5 | 5/5 | 5/5 |
| Paragraph count matches the original | 4/5 | 5/5 | 1/5 | 5/5 | 5/5 |
| Card ask-field style | 5/5 | 0/5 | 5/5 | 5/5 | 5/5 |
| style_stats flags | 5 | 4 | 4 | 3 | 5 (marginal) |

## Held-out result (06, 07; both job A reels), per check

| Check | Result |
|---|---|
| Fences, order, card header, fields, alignment, linter string | 2/2 pass |
| Job A detected and written on the card (including the on-screen-text hook in 07) | 2/2 |
| No alt text for reels | 2/2 |
| Line 1 is the ask, ≤125 characters, exact visible count | 2/2 |
| Line-1 length | replay 117 and 118 vs original 101 and 73. Longer: the "use most of the space" rule overfills job A |
| Paragraph count | 2/2 exact (6 and 6) |
| 3 lowercase hashtags | 2/2 (06 identical to the original) |
| Search line numbers true | 2/2 |
| Mechanics (no emoji, dash or !, ≤3 sentences, no link) | 2/2 |
| Caption words | in range (98-105 vs 82-84 original). Somewhat long |
| Ending | 0/2. Replay forced a "Now every ..." last line in both. Original 06 ends on its last list item and 07 on its takeaway |
| Ask-field wording | 1/2. 06 is close; 07 is a long paraphrase (original: "share it") |
| Ask menu covers the goal | 1/2. "share/send this to" is missing from the menu |
| style_stats compare | 7 marginal flags (words, sentences and max sentence length a little high) |

## Negative control

Brief 07 written from a generic "write an Instagram caption" prompt (`replay/control/07.txt`): 5 emojis, 10 hashtags, no card, no fences, an emoji bullet list, a "Here's what it does" bridge and "Not new software. A spreadsheet." It fails the structural check and has 12 style_stats flags against the held-out originals, versus 7 marginal flags for the skill's replay. The comparison discriminates.

## Leak check

`style_stats.py leak SKILL.md train/`: the first run found 3 caption-level copied phrases (the bio-link ask wording from 05 and the comment-ask card wording from 03), and they were reworded. The remaining 111 matched 6-word runs all come from the card's fixed strings and field labels (`CAPTION READY`, `... characters used before the cut`, the linter line, `first comment: none, no link`, `job: A/B ...`), which repeat across the originals. The example uses a new topic (dental no-shows).

## Unknowns (questions for the user)

- What does caption.py check, and what does the linter line say when it actually runs or fails? "checked by hand" suggests a fallback.
- Are there jobs beyond A and B?
- Are 3 hashtags and the 125-character cut fixed, or settings?
- Are em dashes, rule-of-three lists, closing aphorisms, "Here's the thing" bridges and engagement bait banned, or only absent? Could the no-dash habit come from the generator's settings (P11)?
- Is there a per-brand voice file (P4), a banned-word list, or keyword conventions for comment CTAs?
- How are content types the sample never triggered handled: a link that must go in the caption, a real first comment, or long-form tiers (P7, P8)?
- Is the deliverable handed over with anything else, such as alternatives or notes (P9)?
- Are there voice-protection rules for ghostwritten accounts (P12)?

## Untested changes (suggested by held-out; NOT applied to SKILL.md)

1. Job A ending: drop the requirement that the last paragraph is a "Now every ..." practice. End on the brief's natural last beat (the new practice, the takeaway or the final item). Evidence: 06 and 07.
2. Add a "share" row to the ask menu (send this to <specific person>), with the card value "one, share it". Also allow the job A line 1 to be any ask type, not only a lead-magnet keyword. Evidence: 06 (comment question) and 07 (share).
3. Job A line 1: drop "use most of the visible space". The originals run 73-105 characters.
4. Card ask value: keep it to 2-5 words ("share it", "answer in the comments").
