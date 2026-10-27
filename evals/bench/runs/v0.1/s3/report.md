# Report: s3 (LinkedIn operator post)

Split: user's. 5 train, 2 held out. Final skill: SKILL.md (= drafts/v3.md). Ledger: ledger.md. Briefs: briefs.md, briefs-heldout.md.

## Rules: 23
| Class | Count | Rules |
|---|---|---|
| observed 5/5 | 6 | 1, 3, 15, 16, 17, 18 |
| conditional | 9 | 2, 5, 8 to 14 (post type: mistake, data, opinion, how-to, announcement; 1/5 each) |
| tendency | 3 | 6 (4/5), 7 (3/5), 19 (4/5) |
| range | 2 | 4 (181 to 251 words), 20 (mean sentence 10.5 to 15.1) |
| absent | 3 | 21, 22, 23 |

## Rounds
- v1 replay: 8 features flagged. Form diffs: reframe forced to sit last (01 order flipped), extra reframe block added to opinion (03) and announcement (05), small numbers written as digits ("4 moves", "3 screens", "9 people"), sentences shorter than originals (longest 18 to 26 vs 21 to 31).
- v2 fixes: per-type block order, reframe exactly once and none in announcements, spell out one to nine, one or two long sentences. v2 replay: 7 flags, all small overshoots; block order matched 5/5. Longest sentence 35 vs 31.
- v3: sentence cap about 32. Stopped; next round would fix nothing structural.

## Held-out (06 reflection after leave, 07 team win). Neither type was in train.
| Check | 06 | 07 |
|---|---|---|
| Originals inside train ranges (17 of 18 features) | pass (i_my 16 vs 1 to 4) | pass |
| Hook: standalone, 1 sentence, 15 to 18 words | pass | pass |
| Words / blocks in range | pass (226, 8) | pass (210, 8) |
| Only question is closing ask about reader's experience | pass | pass |
| 3 CamelCase hashtags incl. #Operations | pass | pass |
| One reframe block | pass | pass |
| Advice line "If ..., do X" | n/a | pass |
| No emoji, dash, exclamation, bold, links | pass | pass |
| Numbers (words under ten, digits for $ and %) | pass | pass |
| Hook number callback | pass | pass |
| Block order | partial: replay added a context paragraph the original lacks | pass |
| Hook pattern for the type | unknown: no rule for these types | unknown |

Negative control (generic prompt, same briefs): 14 features flagged vs 7 for the skill replay. 283 to 328 words, 13 to 14 blocks, no closing question, 4 hashtags, arrow bullets, bold-style list headers, "Proud doesn't quite cover it." Comparison discriminates.

## Leak check
0 shared 6-word runs vs train, 0 vs held-out. v1 had 4 (persona phrase, one example sentence); removed.

## Unknowns
- Persona beyond role and company size.
- Whether post type comes from the brief or the skill picks it.
- Hook and block order for unseen types (reflection, team win, event recap).
- Banned words.
- Hashtag selection beyond count and casing.
- Whether sentence length or reading level is set explicitly.
