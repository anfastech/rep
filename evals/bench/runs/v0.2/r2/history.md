# History

Checks: structural (checks.py) per file, plus mechanics counts over 5 files. Train originals: all structural checks pass 5/5; list items ending "." 0; "am ET" style 5/5; contractions 67; arrow lists 4/5; multi-sentence tweet lines 1 to 5 per file.

## Round 1

| Check | A1 strict | B1 menu | C1 loose |
|---|---|---|---|
| 4 headers, outline label, bullets==tweets | 5/5 | 5/5 | 5/5 |
| chars exact, all <=280 | 5/5 | 5/5 | 5/5 |
| tweet count 8 to 12 | 5/5 | 5/5 | 5/5 |
| tweet length range (orig 111 to 231) | 81 to 255 | 109 to 253 | 94 to 211 |
| TL;DR or playbook second to last | 5/5 | 4/5 (03 merged "Conclusion:" + TL;DR) | 5/5 |
| CTA follow / retweet first / question | 5/5 / 5/5 / 4/5 | 5/5 each | 5/5 each |
| hooks A to D | 5/5 | 5/5 | 5/5 |
| posting 4 bullets + fixed strings | 5/5 | 5/5 | 5/5 |
| arrow lists (orig 4/5, max 1) | 0/5 | 3/5 | 5/5 |
| no hashtags, dashes, exclamations | 5/5 | 5/5 | 5/5 |
| multi-sentence lines per file (orig 1 to 5) | 5 to 22 | 8 to 12 | 8 to 14 |
| list items ending "." (orig 0) | 27 | 21 | 21 |
| time format "8:30am ET" (orig 5/5) | 0/5 | 0/5 | 0/5 |
| contractions total (orig 67) | 1 | 48 | 59 |
| style_stats features outside | 10 | 8 | 9 |

Block diffs: replays put "Some context. I'm ..." on one line; add periods to list items; use "8:00 AM ET"; B1/03 opened the summary tweet with "Conclusion:" before "TL;DR:". A1 lost contractions and arrow lists (no defaults section).

Merge for v2: B1 menu + C1 "adapt" framing (won arrows, TL;DR, contractions). Fix: list items no end period; time format; one sentence per line stated harder with a cap on fragment pairs; summary tweet first line is "TL;DR:"; contractions stated.

## Round 2 (v2)

| Check | v2 |
|---|---|
| all structural checks (headers, outline, chars exact, <=280, count, TL;DR position, CTA 3 parts, hooks A to D, posting bullets, no hashtags/dashes/!) | 5/5 each |
| tweet length range | 109 to 243 |
| arrow lists | 5/5 (orig 4/5) |
| multi-sentence lines per file | 0 to 4 (orig 1 to 5) fixed |
| list items ending "." | 0 (orig 0) fixed |
| "am ET" format | 5/5 fixed |
| contractions | 74 (orig 67) fixed |
| style_stats features outside | 8 (small overshoots, no new failure) |

Block diff 02: "We tagged each 1 by ..." (digit rule over-applied). v3 = v2 + digit wording fix only. Round 3 not replayed on train: the only change is one wording line; went to held-out.

## Held-out (v3, frozen)

Structural checks 2/2 each. Mechanics: list periods 0 (orig 3, from numbered sentence tweets in 06), am ET 2/2, contractions 25 (orig 24), arrow lists 2/2 (orig 1/2). style_stats: 7 features outside held-out range (small overshoots). Negative control (generic prompt, 07): headers fail, "1/" numbering, 5 hashtags, 2 emojis, 1 dash, 13 features outside. Discriminates.
Block diff 06: original gave each of 3 changes its own numbered tweet; replay put them in one arrow tweet. Logged as Untested change.
