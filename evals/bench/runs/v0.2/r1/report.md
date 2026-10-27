# Report: r1 reconstruction (reverse-engineer-skill v0.2)

Result: `SKILL.md`, a LinkedIn ghostwriting skill. It outputs a full deliverable wrapper: header, hook and 2 alternatives, post with typed slots, hashtags, first comment, Edit note checklist, Claims and facts, Open gaps, and a fixed closing line.

## Rules
19 rules, 4 defaults, a 5-row post-shape menu (lesson, data insight, contrarian, how-to list, announcement), 5 untested changes. Evidence tags are inline in SKILL.md. Ledger: `ledger.md`.

## History (train, 15 structural checks via ../../tools/checks.py)
See `history.md`. A1 14/15 (one length miss), B1 15/15, C1 13/15 (3 alt hooks, 1 hook too short); total words high for all three (709 to 853 vs 588 to 652). v2 fixed slots, gaps and claims (634 to 681). v3: 15/15, total words inside range.

## Held-out (final.md, 2 outputs), per check
header 2/2, block order 2/2, hook verbatim 2/2, hook length 2/2 (but the originals fail the frozen rule 0/2: 06 is 1 sentence, 07 is 151 chars), alt hooks = 2 2/2, post words 2/2, paragraphs 2/2, slots 2/2, clean body 2/2, hashtags 2/2, first comment 2/2, Edit note core 2/2, Claims rows 2/2, Open gaps first line 2/2, closing line 2/2.
Diff misses: 06 is a reflection that closes on a question (no shape for it); the replay used 8 Edit note bullets where the originals used 6; the replay used a triplet the original avoided; 07 adds a second PERSON YES NEEDED line for the named analyst. All 5 are logged as Untested changes.
style_stats compare: 10 features flagged (brief-driven pronoun and digit counts); total words 605 to 626 vs 593 to 633, in range. A second replay run overwrote the first; both scored 15/15 with 8 Edit note bullets.

## Negative control
A generic prompt on brief 07 failed 15/15 checks. It had no wrapper and no slots, and included "Not X. Not Y." lines, a colon reveal, questions and invented actions. The checks discriminate.

## Leak
0 non-fixed 6-word matches after rewording 9 phrases. 117 train and 48 held-out matches remain, all from fixed strings: the closing line 5/5, the voice offer 5/5, and "First comment: none (no link in this post)." in every no-link output.

## Unknowns
Listed in SKILL.md: the banned word list; other formats (calendar, "social pieces"); voice card slots; whether the alt hook count is fixed; length tiers; what each sign-off scope means; whether the dash ban comes from the generator; whether the first draft is kept; whether the draft file is written.
