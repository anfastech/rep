# Report: reconstructed "operator-linkedin-post" skill

Source: 7 outputs, user split 5 train / 2 held out. Final skill: SKILL.md (25 rules incl. 20b).

## Rules by class
- observed: 13 (plain text, hook one sentence alone, line 2 short, digits, reframe, first person, lesson block, close line, calm tone)
- absent (hard never): 6 (emojis, hashtags, contractions, dashes, exclamation marks, question/engagement close), 0/7
- range: 3 (words 211 to 242, blocks 14 to 18, sentence length mean 7.2 to 9.7, max 18 to 30)
- tendency: 4 (key number early 4/5, admit mistake 3/5, "Here is what" pivot 3/5, parallel triple 4/5)
- conditional: 4 (plain-line list 2/5, numbered tactics 1/5, announcement 1/5, personal-change list 1/7 held-out only)

## Ledger
See ledger.md.

## Replay rounds (train, compare flags)
| Round | Flags | Main form diffs | Fix |
|---|---|---|---|
| v1 | 8 | words 194 to 207 (short), mean sentence 6.5 to 8.2, max 12 to 21, two-sentence hooks | length target, require 2 long sentences, one-clause hook |
| v2 | 7 | max sentence 43, hooks joined by "and", optional moves in 5/5 replays ("Same" triple, "Here is what", "rule") | cap 30 words, mark optional slots, vary shapes |
| v3 | 8, all at range edge | words 212 to 225 in range; result stated in line 3 (02) | save result for second half |

## Held-out (06, 07), skill vs generic-prompt control
| Check | Skill | Control |
|---|---|---|
| Mechanics: emoji, hashtag, contractions, dashes, "!", "?" | pass 2/2 | pass 2/2 (not discriminating) |
| Hook: one sentence alone on line 1 | pass 2/2 | 1/2 (06 has 3 sentences on line 1) |
| No bullet symbols / numbers in personal lists | pass 2/2 | fail 0/2 ("1." in 06, "- " in 07) |
| Words (orig 217 to 242) | fail, 208 to 209 | fail, 184 to 202 |
| Blocks (orig 16 to 18) | near, 15 | fail, 11 to 13 |
| Max sentence (orig 18 to 21) | over, 22 to 27 | in range, 17 to 20 |
| Close form | partial: both used "X. Then Y." (orig 06 is a mirrored aphorism) | soft CTA, weaker |
| Personal-change list (06: statement line + explanation) | fail, plain one-line items | partial, numbered |
| compare flags | 8 | 7 |

Negative control: structurally worse (hook, list symbols, block count), but the statistical compare does NOT discriminate (7 vs 8 flags). The briefs already carry the facts and plain phrasing, and the base model avoids emojis and contractions here by default.

Post-held-out revisions (so held-out is no longer a clean test for these): rule 7 length floor, rule 8 block target, rule 20b personal-change list, rule 23 varied close forms.

## Leak check
SKILL.md vs train: 0 shared 6-word runs. vs held-out: 0. (Two leaks found and removed in v3.)

## Unknowns
- Banned word or phrase list.
- Persona: fixed in the skill or given per brief? All 7 read as head of operations at a logistics software company.
- British spelling required? One instance ("favours").
- Behaviour for brief types not seen (celebration, opinion with no data, book review).
- Whether the source states a word count or hook formula list.
