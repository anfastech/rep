# History

Originals: caption words 58-92, caption lines 5-9, first line 12-16 words, mean sentence 11.3-15.3 words.

## Round 1 (A1 strict, B1 menu, C1 loose), replay on 5 train briefs

| Check | A1 | B1 | C1 |
|---|---|---|---|
| Wrapper fields, order, fixed strings | pass 5/5 | pass 5/5 | pass 5/5 |
| Shape name verbatim from menu | pass 5/5 | pass 5/5 | FAIL 3/5 ("A before/after with numbers", "Just showing the thing") |
| Shape chosen = original's shape | 5/5 | 5/5 | 5/5 |
| Caption words in 58-92 (±10%) | FAIL 1/5 (86-105) | 3/5 (70-100) | pass 5/5 (64-89) |
| Caption lines in 5-9 | FAIL 1/5 (9-13) | pass 5/5 (6-9) | pass 5/5 (6-8) |
| First line 12-16 words | 1/5 (10-13) | pass 5/5 | 3/5 (11-17) |
| Mean sentence length in range | 4/5 | FAIL 2/5 (lines pack 2 long sentences) | 4/5 |
| Mistake block: labeled What I believed / actually happened / I'd do now | FAIL (prose) | pass | FAIL (prose) |
| Playbook items unnumbered after "Here's how I...:" | FAIL (numbered, item + separate explanation lines) | pass | FAIL (numbered) |
| Ends with a specific question | 5/5 | 5/5 | 5/5 |
| No emoji/hashtag/dash/exclaim | 5/5 | 5/5 | 5/5 |
| Two quoted runner-ups | 5/5 | 5/5 | 5/5 |
| Extra aphorism line before question ("Low leverage isn't no leverage") | 1/5 | 0/5 | 2/5 |

Winners: B1 on structure and shape skeletons; C1 on length; A1 wins nothing alone.
Diff notes: B1 crams 2 long sentences per line (03, 04) -> add short-line rule; B1 05 slightly over. A1 numbers lists and splits item explanations to separate lines. C1 drifts shape names.

## Round 2 plan (v2)
B1 skeleton + menu, C1-style tight length targets, plus: one short sentence per line by default (max 2, rarely 3); playbook items unnumbered, tactic + one short reason on one line; shape name copied verbatim; interpretation line optional and plain, not a slogan.

## Round 2 (v2), replay on 5 train briefs

| Check | v2 |
|---|---|
| Wrapper fields, order, fixed strings | pass 5/5 |
| Shape name verbatim | pass 5/5 |
| Shape chosen = original's shape | 5/5 |
| Caption words in 58-92 (±10%) | pass 5/5 (62-87) |
| Caption lines in 5-9 | pass 5/5 (5-9) |
| First line 12-16 words | 4/5 (11-16) |
| Mean sentence length in range | FAIL 2/5 (12.8-18.0): action + result merged with "and" on one line (02, 03, 05) |
| Mistake labeled lines | pass |
| Playbook unnumbered, tactic + reason per line | pass |
| Ends with a specific question | 5/5 |
| No emoji/hashtag/dash/exclaim | 5/5 |
| Contractions 2-5 | 2/5 (0-5) |
| Two quoted runner-ups | 5/5 |

Fixed vs round 1: length (A1/B1), labels and list form (A1/C1), shape names (C1).
Remaining diff: originals give the result its own line (02 "Ticket volume dropped by a third."); v2 merges it. v3 adds a short-sentence / result-on-own-line rule and a contraction default.

## Round 3 (v3), replay on 5 train briefs

| Check | v3 |
|---|---|
| Wrapper fields, order, fixed strings | pass 5/5 |
| Shape name verbatim / correct shape | 5/5 / 5/5 |
| Caption words in 58-92 (±10%) | pass 5/5 (58-88) |
| Caption lines in 5-9 | pass 5/5 |
| First line 12-16 words | 3/5 (11-14; inside widened 11-17) |
| Mean sentence length in range | 4/5 (11.8-15.5), up from 2/5 |
| Result on its own line | 4/5 (03 first line still joins with "and", as does original 03's first line) |
| Mistake labels / playbook list form | pass / pass |
| Ends with a specific question | 5/5 |
| No emoji/hashtag/em dash/exclaim | 5/5 |
| Contractions 2-5 | 2/5 (2-9): overuse, not fixed |
| Two quoted runner-ups | 5/5 |

Subagent note: read "no dashes" as banning hyphens ("company of 60 people" instead of "60-person"). Final wording fix (not replayed, clarification only): "no em or en dashes; hyphenated words are fine".
Stopping: 3 rounds done. Frozen draft = drafts/final.md (v3 + dash clarification).

## Held-out test (frozen draft: drafts/final.md, exported as SKILL.md after leak-only edits)
See report.md. Shape miss on 06 (Before and after expected, Show the thing chosen). Logged as an untested change; rules not edited.
