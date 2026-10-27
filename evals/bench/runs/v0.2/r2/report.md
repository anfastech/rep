# Report: x-thread-writer reconstruction

Source: 7 outputs (train 01 to 05, held-out 06 to 07, user split). Final skill: SKILL.md. Ledger: ledger.md. History: history.md.

## Rules
10 rules + 13 defaults (23), plus 1 untested change. Evidence tags inline in SKILL.md.
Observed 5/5: 4 fixed section headers; outline one bullet per tweet; "Tweet N (X chars)" with exact counts (49/49 exact); one sentence per line; TL;DR second to last (case study: playbook); CTA with follow + "Retweet the first tweet" + question; 4 hook variations A to D; 4 posting bullets with 2 fixed strings.
Conditional: "Template:" vs "Format:" (announcement, 1/5); playbook replaces TL;DR in case study (1/5).
Menu: Story, Case Study, Contrarian Take, Tutorial, plus free-format fallback.

## Held-out result per check (v3 on 06, 07)
| Check | Result |
|---|---|
| 4 headers in order | 2/2 |
| outline label + bullets == tweets | 2/2 |
| char counts exact, all <= 280 | 2/2 |
| tweet count 8 to 12 | 2/2 |
| TL;DR/playbook second to last | 2/2 |
| CTA follow / retweet first / question | 2/2 each |
| hook variations A to D | 2/2 |
| posting bullets + fixed strings | 2/2 |
| no hashtags, dashes, exclamations | 2/2 |
| "am ET" time format | 2/2 |
| contractions | 25 vs 24 |
| arrow lists | 2/2 vs 1/2 (overshoot) |
| numbered per-item tweets (06) | miss: replay used arrow list |
| style_stats features outside range | 7 (minor) |

Negative control: generic prompt fails headers and 13 features (hashtags, emojis, "1/"). Comparison discriminates.

## Leak
95 shared 6-word runs with train, 38 with held-out; all from the two fixed posting strings and section header seen 7/7. 0 other.

## Unknowns
- More menu templates beyond the 4 seen?
- Persona (head of ops, 60-person company): brief or voice file?
- Banned words or devices? Contrast lines and triples are used freely.
- Length tiers ("Short announcement thread" hints at one)?
- Dash and emoji absence: skill or generator settings?
- Rules for images, links, polls, quotes in briefs?
- Is the posting plan or first reply ever skipped?
