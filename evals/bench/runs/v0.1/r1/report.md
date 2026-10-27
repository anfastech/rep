# Report: linkedin-post-draft (reconstructed)

Split: train 01 to 05, held out 06 and 07 (user split). Ledger: ledger.md. Briefs: briefs.md, briefs-heldout.md.

## Rounds
- v1 replay: 10 features outside range. Edit note 215 to 278 words (orig 169 to 199); per-item attribution in Kept; full name in Voice; titles too long (first_line_words 7 to 10 vs 6 to 8). Body phrases lifted from originals found by reading, removed.
- v2 replay: 8 flags. Edit note 162 to 200 (in range), titles in range. Remaining: shorter sentences (mean 10.7 to 13.5 vs 11.6 to 17.0), more digits.
- v3: added sentence-length rule and held-back-fact rule. Final.

## Held-out (v3, briefs 06 and 07)
| Check | 06 | 07 |
|---|---|---|
| 7 fixed lines present | pass 7/7 | pass 7/7 |
| Header path + format line | pass | pass |
| Hook repeated verbatim, 2 alts | pass | pass |
| Claims 6 bullets, order | pass | pass |
| Slots in body (orig 4 / 3) | 3, pass | 4, pass |
| No emoji, dash, exclamation; 3 hashtags | pass | pass |
| Sign-off scope | FAIL (orig "product facts only; personal story, no brand claims") | pass |
| Close matches intent | FAIL (orig asks a question for replies; replay gave an action) | pass |
| Edit note bullet set | FAIL (added Skeptic, Swap test) | FAIL (added Skeptic, Readability) |
| Second person consent (named third party) | n/a | FAIL (orig lists "PERSON YES NEEDED (the analyst)") |
| Total words (orig 593 to 633) | FAIL 666 to 691 | FAIL |
| Mean sentence length (orig 14.8 to 15.4) | FAIL 12.8 | FAIL 12.8 |

## Negative control
Generic prompt on brief 07: 0/7 fixed lines, no hooks block, no slots, no edit note or claims, 5 capitalized hashtags, invented details ("on her own time", "she"). Clearly worse; the checks discriminate.

## Leak
Body-content 6-gram matches: 0. 39 template-wording matches in fewer than 5 originals (conditional fixed strings such as "speaking for the company", sign-off scopes, edit-note phrasing); 24 match all 5 (fixed lines). One copied edit-note phrase reworded.

## Unknowns
See SKILL.md Unknowns. Held-out added: intents beyond the 5 seen (personal reflection, team success), extra sign-off scopes, third-party consent handling.
