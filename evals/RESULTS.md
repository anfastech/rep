# Results

Metrics, per source skill:
- **recall_visible**: share of the source's rules that show in the outputs and that the
  reconstruction recovered (full = 1, partial = 0.5).
- **prec rules**: share of the reconstruction's Rules and Template items that match a real
  rule. Defaults and Unknowns are reported apart, since they are labelled unconfirmed.
- **wrong**: items that contradict the source.

Scores come from one AI scorer per source skill, which sees both versions as X and Y
(`bench/blind/MAPPING.txt`). Raw scores: `bench/scores/`. Reconstructions: `bench/runs/<version>/<id>/`.

## Toy fixture (12 hidden rules)

`fixtures/toy-01`. v0.1 replays scored 47/48 rules on the checker. Copied 6-word runs fell
from 205 and 210 (no skill) to 30 (only the fixed P.S. line). The one miss was a banned-word
list, which outputs cannot reveal.

## v0.1 on 5 tuning skills (s1 to s5)

recall_visible 0.59, recall_all 0.49, precision 0.64, wrong 3 of 174 items. 53 of 239 real
rules left no trace in the outputs. Most missed: mechanics 22, conditionals 13, voice 8.
These lessons became `references/patterns.md`.

## Round 1: v0.1 vs v0.2 (r1, r2)

| Skill | recall_vis v0.1 / v0.2 | prec rules v0.1 / v0.2 | wrong v0.1 / v0.2 |
|---|---|---|---|
| r1 | 0.65 / 0.69 | 0.86 / 0.90 | 0 / 1 |
| r2 | 0.63 / 0.61 | 0.74 / 0.85 | 0 / 0 |

No clear win. v0.2's one wrong item came from a rule edited after the held-out test.

Caveat: s1 to s5, r1 and r2 outputs were generated in a session that loaded the operator's
global style settings (no dashes, plain sentences). Scorers marked those rules as
environment, not skill. Rounds 2 and 3 are clean.

## Round 2: v0.1 vs v0.3 (r3, r4, r5), clean

| Skill | recall_vis v0.1 / v0.3 | prec rules v0.1 / v0.3 | wrong v0.1 / v0.3 |
|---|---|---|---|
| r3 | 0.54 / 0.54 | 10/16 / 7/10 | 0 / 0 |
| r4 | 0.59 / 0.56 | 15/21 / 13/14 | 1 / 0 |
| r5 | 0.74 / 0.70 | 9/19 / 4/16 | 1 / 1 |
| mean | 0.62 / 0.60 | 0.61 / 0.60 | 2 / 1 |

Tie. Main precision loss in both versions: shape rules per brief type, each based on one
output (r5: 9 of 10 incidental).

## Round 3: v0.3 vs v0.4 (r6, r7), clean

| Skill | recall_vis v0.3 / v0.4 | prec rules v0.3 / v0.4 | prec all v0.3 / v0.4 | wrong |
|---|---|---|---|---|
| r6 | 0.61 / 0.73 | 12/15 / 13/15 | 14/20 / 16/21 | 0 / 0 |
| r7 | 0.74 / 0.64 | 9/15 / 12/14 | 14/31 / 15/24 | 0 / 0 |
| mean | 0.68 / 0.69 | 0.70 / 0.86 | 0.55 / 0.69 | 0 / 0 |

First version with a precision gain on both skills. Recall flat.

## Video prototype (v0.5, 1 video)

One 85 s explainer short (720x1280, 2 hard cuts, 280 words at 201 wpm). The skill
recovered a 9-beat script template and the visual and caption rules; with one video
every rule is a guess. A code-rendered replay of one 6.8 s beat was diffed against the
original over 4 rounds. Mean gap per feature, round 1 to round 4: finger tip height
0.21 to 0.05, accent glow height 0.23 to 0.05, accent-row height 0.14 to 0.05. Two
numeric matches were wrong on screen (finger area, brightness), so the method now
requires a side-by-side visual check with every numeric diff. The source video is not
in the repo.

## Limits

- 2 or 3 source skills per round and one scorer each. No inter-scorer agreement measured yet.
- Recall tops out near 0.65: about a quarter of real rules leave no trace in 7 outputs
  (banned words, rotation across posts, rules for content types the briefs never trigger).
- Video is a prototype tested on 1 video. Carousel is not built.

## Next

1. Run v0.4 on real outputs.
2. Second independent scorer on r6, r7 before trusting small gaps.
3. Check that the Unknowns list stays short and answerable (r7 had 38 items).

## Reproducibility

`sources.tsv` pins each source to the commit whose SKILL.md matches the benchmark copy.
Held-out sources r1 to r7 refetch byte-identical. Tuning sources s1, s3 and s5 have
reference files that changed upstream after the benchmark, so their refetch differs.
