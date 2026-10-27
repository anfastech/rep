# Report: X thread skill reconstruction (r2)

Final skill: SKILL.md (copy of drafts/v4.md). Ledger: ledger.md. Briefs: briefs.md, briefs-heldout.md.

## Rules
27 numbered rules plus a 5-row template table.
Classes: 17 observed, 2 conditional, 4 tendency, 3 range, 1 absent, 1 held-out-informed (untested).

## Rounds (train, N=5)
| Round | Structural checks (checks.py, 17 per file) | style_stats compare flags | Fixes |
|---|---|---|---|
| v1 | all pass except 05 "Follow us" | 10 features outside | tweet 1 too long (164 to 189 vs 120 to 152), max tweet 259 vs 231, lines up to 17 words vs 14, "Follow us" |
| v2 | all pass (case study has no TL;DR label, same as original) | 8 features outside; max tweet 227, mean words per line 5.9 to 6.5 (orig 5.8 to 6.6) | company description repeated 11 times vs 4; time format "8 a.m." vs "8:30am" |
| v3 | used for held-out | | |

## Held-out (06 story, 07 case study), replay with v3
| Check | Original | Replay |
|---|---|---|
| 4 fixed section headers | 2/2 | 2/2 |
| Template/Format line | 2/2 | 2/2, same templates chosen |
| Beat count = tweet count | 2/2 | 2/2 |
| Exact char counts | 2/2 | 2/2 |
| Max tweet chars | 196, 200 | 218, 230 |
| Tweet count | 10, 11 | 10, 11 |
| CTA beat, follow me, retweet first tweet | 2/2 | 2/2 |
| Numbered summary 2nd to last; TL;DR label | 2/2; 1/2 | 2/2; 1/2 |
| Hooks A to D | 2/2 | 2/2 |
| Posting 4 bullets, fixed line, 4 subs with Stay online first, ET | 2/2 | 2/2 |
| No hashtags, dashes, exclamations | 2/2 | 2/2 |
| style_stats compare | | 11 features outside a 2-file range, small margins (words 659 to 668 vs 594 to 658) |
| Section-by-section diff | | MISS: original 06 replaced Story beats with "Change 1..3"; replay kept default beats. Replay over-described the author (2 vs 0 to 1 mentions). One engagement bullet merged 2 tactics. |

Fixes for the misses were added in v4 after the test, so they are untested.

## Negative control
Generic "write an X thread" prompt on both held-out briefs: 0/2 parse as the 4-section format, 233 to 247 words vs 594 to 658, 1 emoji and "1/" numbering. Clearly worse; the comparison discriminates.

## Leak check (SKILL.md vs all 7 originals)
33 unique 6-word runs. 19 are lines fixed in all 7 originals. 14 are structural labels (template names, beat names, outline CTA beat, posting labels). 0 copied content.

## Tool note
style_stats.py's emoji regex misses flag emojis (regional indicators U+1F1E6 to U+1F1FF); 05 has one and reports 0.

## Unknowns
See SKILL.md: persona fixed or brief, untriggered templates, tweet-count rules, banned words, thin-brief behavior, media handling.
