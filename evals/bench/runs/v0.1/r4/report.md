# Reverse-engineering report: target

Inputs: 7 outputs, plain-text LinkedIn-style posts. The user's split was kept: 5 train (01-05), 2 held out (06-07).
Final skill: `SKILL.md` (same as `drafts/v4-final.md`). Replays: `replay/v1..v3`, `replay/heldout`, `replay/control`.

## Ledger
| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Every sentence/line separated by a blank line; 1-2 sentences per line | 5/5 | observed | One line per block, blank line between every line |
| Hook first line starts with "I" + first-person action | 5/5 | observed | Open with "I <did/do X>" |
| Hook contains a concrete number | 3/5 (01,02,03); 04,05 have none | tendency (brief-driven: present when brief has numbers) | Put the brief's headline number in the hook when there is one |
| Hook split: second short line as its own block (03 "Only 4 came back.", 05 "It's in Lisbon.") vs two sentences on one line (01,02) vs one sentence (04) | 2/5 / 2/5 / 1/5 | tendency | Hook is 1-2 short sentences; a twist/detail may go on a second line |
| Hook length (first line) | 8 to 16 words, N=5 | range | About 6 to 18 words in first line |
| Line 2/3 is "Here's <what happened / what we did / why I did it / the N-step playbook I use / where we are>:" ending in a colon | 5/5 | observed | Always a "Here's ...:" bridge line after hook |
| Setup: 2 short lines of context or common belief before body ("Most people think...", "Our calendars...", "For years...") | 5/5 (01 slightly different: "We built..." then "It tested well") | observed | 2 lines of context/before-state after the bridge |
| Body as short narrative lines | 2/5 (01 failure story, 03 experiment) | conditional: story/experiment brief | If the brief is a story, tell it in 6-10 one-sentence lines, chronological |
| Body as "→ " arrow list (4-6 items) | 2/5 (02 process+result, 05 announcement facts) | conditional: brief is a set of steps/facts | If the brief is a set of facts or steps, use "→ " list of 4-6 items |
| Body as "1/ " numbered steps each followed by a one-line explanation block | 1/5 (04 playbook) | conditional: brief is an N-step playbook | If the brief is a named N-tactic playbook, use "1/ Tactic." then an explanation line, and say the count in the bridge |
| Insight/reframe 2 lines: "X isn't/wasn't Y." / "It's Z." or "X is just A. B is what makes it real." | 4/5 (01,02,03,05) | tendency | Close body with a 2-line reframe that names the real cause |
| "No X. No Y. Just Z." triplet | 2/5 (02 inside list, 04 as closer) | tendency | May use "No X. No Y. Just Z." |
| One extra punchline/directive line after reframe (01 contrast, 03 Don't..., 05 We're looking...) | 3/5 | tendency | Optionally one more punchline line |
| Resource line: "I wrote up / I put / I turned this into <resource>." | 5/5 | observed | Always offer a related free resource in one line starting with "I" |
| CTA: `Comment "WORD" and I'll send you the link.` | 5/5 | observed (fixed string, word varies) | Exact CTA string |
| CTA keyword is one ALL-CAPS common noun unrelated to the topic (PRETZEL, OTTER, TEAPOT, MANGO, CACTUS: foods, animals, objects) | 5/5 | observed | Pick a random unrelated concrete noun, all caps, in quotes |
| PS line: "PS - " + 2 sentences speaking to "you", restating stakes / a challenge | 5/5 | observed | Always end with "PS - ..." two sentences, second person |
| Footer: blank line, "---", blank line, "Hook formula used: <Formula Name> — for A/B tracking. Strip before publishing." | 5/5 | observed (fixed string) | Exact footer |
| Hook formula names: title-case labels, sometimes two joined with " / " or " + " | 5/5 distinct names | observed format; library unknown | Name the formula used; full library unknown |
| Questions in post | 0/5 | absent (LinkedIn genre often uses them) | No question marks |
| Exclamation marks | 0/5 | absent, genre often uses them | No exclamation marks |
| Emojis | 0/5 | absent, genre often uses them | No emojis (→ arrow is the only symbol) |
| Hashtags | 0/5 | absent, genre often uses them | No hashtags |
| Em dashes in body | 0/5 (only in footer) | absent | No em dashes in the post body |
| Contractions | 4 to 7 per post | range | Use contractions naturally |
| Numbers as digits (12, 3,000, 41%, 22) | 5/5 where numbers occur | observed | Digits for numbers |
| Voice: first person I/we, plain short words, mean sentence 6 to 10 words | 5/5 | observed / range | Plain words, short sentences |
| Word count | 135 to 164, N=5 | range | About 120 to 190 words before the footer |
| Non-blank lines | 17 to 19 incl. footer, N=5 | range | About 14 to 22 |
| Banned words, persona, formula library, brief types not seen | not observable | unknown | listed under Unknowns |

Held-out additions to the ledger:
- Hook starts with "I": 6/7. 07 opens with "A junior analyst on my team ...", so the rule is now conditional (when someone else gets the credit).
- Resource-line verbs: "wrote down" (06) and "shared" (07) are new. The list was widened.
- Arrow items with two sentences that keep their periods (06). The rule was widened.
- Formula names: 7/7 distinct. The library is still unknown.

## Rounds (train replay, compare + section diff)

| Round | Stat flags (outside train range) | Section-diff findings | Fix |
|---|---|---|---|
| v1 | 6 (words x2, lines x3, nonblank x3, contractions x2, digits, we_our) | Blank lines inside the → list. Periods on list items. Blank line between `---` and the footer (originals have none). Draft quoted source phrases, which replays then copied. | v2: tight list block, no item periods, footer spacing, quoted source phrases removed |
| v2 | 9 (words x4 up to 201, first line 23 words, etc.) | Posts too long: padded lines after the list, long playbook explanations, long hooks | v3: hook cap 17 words, 110-160 word target, short explanation lines, no padding |
| v3 | 5 (words 1 file at 168, max sentence 41, contractions x2, digits, we_our) | Skeleton, CTA, PS, footer, list format and hook all match. The remaining flags are small and within a sensible widening. | stopped (3 rounds) |

## Held-out result (v3 draft, before amendments), per check

| Check | 06 | 07 |
|---|---|---|
| "Here's ...:" bridge line | pass | pass |
| Body type matches original | pass (→ list) | partial: original is a short story without a list; replay is a longer story |
| Two-line reframe | pass | pass |
| Resource line + exact CTA string + caps random noun | pass | pass |
| "PS - " two sentences to "you" | pass | pass |
| Footer exact format, `---` directly above | pass | pass |
| No ?, !, emoji, hashtag, em dash in body | pass | pass |
| Hook opener | pass ("I took..." vs original "I came back...") | FAIL: replay forced "I watched...", original opens with the team member |
| Formula label matches original | fail (unknowable: different label) | fail (unknowable: different label) |
| Length | 148 vs 139-144 words incl. footer (close) | 167 vs 139-144 (long) |
| Stats compare | 11 flags, N=2 originals, so ranges are degenerate (single values). Treat as weak evidence. | |

Amendments made after the held-out test (rule 2 hook opener, rule 8 list items, rule 12 resource verbs). They were NOT re-tested on fresh data.

## Negative control

Generic prompt "Write a LinkedIn post about ..." on brief 07 (`replay/control/07.txt`): 297 words, 5 hashtags, a question, no "Here's" bridge, no comment-keyword CTA, no PS, no footer, long sentences (max 50 words). 15/18 stats flagged. It is clearly worse, so the comparison does discriminate.

## Leak check

`leak SKILL.md train/`: 20 shared 6-word runs, all from the fixed strings in every original (`Comment "..." and I'll send you the link.`, `PS -`, `— for A/B tracking. Strip before publishing.`). One non-fixed leak was found and removed: a formula label copied from one output's footer, plus the example PS opener. `leak SKILL.md heldout/`: 8, all fixed strings.

## Unknowns (questions to answer or test)

- What is the full hook-formula library, and how does the skill pick one per brief? (7 outputs gave 7 different labels.)
- How is the CTA keyword chosen: a fixed list, random, or something else? All 7 were foods, animals or objects.
- Is there a banned-word list, a persona or audience definition, or a stated word limit?
- What does it do when the brief has no resource to offer? (All 7 offered one.)
- Is the "---" footer always added, or is it a setting? (7/7 had it.)
- Target platform is never stated. LinkedIn is assumed from the genre.
