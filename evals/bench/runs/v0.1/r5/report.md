# Report: target

Recovered skill: X (Twitter) post/thread packager, which outputs posting packages. Exported as `SKILL.md` (draft v3 with leak scrubbing). Data: 5 train outputs (01 to 05) and 2 held-out outputs (06, 07), using the user's split.

## Ledger

See `ledger.md` for the full table. Summary by class:

- **Observed (hard rules):** `**Format:**` first line (5/5); thread label set `**Thread structure:**` / `**k/N** (X chars)` / `k/N ` prefix (3/3); `**Post text** (X chars)` for single posts (2/2); exact char counts with ", including hashtag" (5/5); hooks that are a blunt claim or stat (5/5); first-person we/our voice (5/5); digits for numbers (5/5); a `**Hashtags:**` line always present (5/5); no emojis, exclamation marks, em dashes or markdown in the copy (0/5).
- **Conditional:** thread vs single post chosen by brief shape (5/5); final open question in non-promo outputs (4/5); link moved to a reply (1/1); image specs for data or photo briefs (2/5); list hook names the count (1/1); story thread ends on a question-only post (1/1); no hashtag on a pure opinion post (1/5).
- **Tendency:** `**Notes:**` section (4/5); content-mix bucket named (3/5); engagement tactic in the notes (2/5); spelled-out small numbers (1/5).
- **Range:** thread length 4 to 5 posts (widened to 3 to 7); post length 56 to 107 chars (widened to about 50 to 130); single post 124 to 130 chars (widened to about 80 to 200).

## Rounds

| Round | compare flags | Diff findings | Fix |
|---|---|---|---|
| v1 | 6 (words, sentences, max/mean sentence, digits, i_my) | 0 contractions where originals had 4/5; replay 01 repeated the fault admission (i_my 3); "2 sites" opened a sentence where the original spelled the number out | contraction rule; admit fault once in the hook; numbers rule |
| v2 | 5 | promo post gained a CTA sentence and "Nine"; data hook did not open with the stat; story thread had 4 posts with the lesson and question merged | promo: facts only, the reply is the CTA; stat-first hook; story ends on a question-only post; relaxed numbers rule |
| v3 | 5 (all length or person counts driven by Notes or content) | form matched block by block: formats, post counts, hashtags, image specs, reply section | stopped (3-round cap) |

Note: in replays v2 and v3, the 01 hook came out word-for-word the same as the original. The cause is the detailed brief, not the skill. The leak check confirms that SKILL.md does not contain it.

## Held-out test (draft v3, briefs in `heldout-briefs.md`)

`compare heldout/ replay/heldout/`: 7 flags. Each check below is reported separately.

| Check | 06 (personal leave, 3 changes) | 07 (analyst spreadsheet) |
|---|---|---|
| Format choice | **FAIL**: replay was a 5-post thread; original was a single post with a 3-line list | PASS: 4-post thread |
| Format line wording | n/a | **MISS**: original "+ image" (screenshot); replay omitted the suffix (rule only covered "+ chart image") |
| Hook | PASS in kind (claim + count) | PASS (result + number) |
| Char counts / labels | PASS | PASS |
| Final open question | PASS | PASS |
| Hashtag | **FAIL**: replay #Leadership; original None ("personal story") | PASS (#Logistics, the same tag) |
| Image specs | n/a (none in either) | PARTIAL: replay had 2 bullets; original had 3 (blurred data, overlay callouts) |
| Notes section | PARTIAL: present in both; original names no bucket | **MISS**: original has no Notes; replay added them |
| Mechanics (emoji, dashes, digits) | PASS | PASS |

Lessons from the held-out set, not folded into SKILL.md so the test stays clean (open hypotheses):
- A personal-story list may stay a single post with one item per line. The thread trigger is narrower than "has a list".
- Personal stories skip hashtags (2/7 with no hashtag: an opinion post and a personal story).
- Threads with image specs have no Notes (2/2: 02 and 07).
- Any image counts, not only charts: the format suffix is "+ image" or "+ chart image".

## Negative control

The brief for 07 was written with a generic prompt ("Write a Twitter/X post about ..."), see `replay/control/07.txt`. It had no format line, no char counts, no `k/N`, no hashtag line, no question, no image specs and no notes, and it opened with an 18-word line. compare flagged 7 features against the held-out set, and it differs on every structural axis. It is clearly worse, so the comparison does discriminate. The stats script alone is weak here: the skill replay also had 7 flags. The block-by-block diff is what separates them.

## Leak check

`leak SKILL.md train/`: 26 shared 6-word runs at first, 8 after scrubbing. `leak SKILL.md heldout/`: 3. The 8 that remain are all fixed structural labels: `**Hashtags:** ... (final post only)`, `**Image specs (attach to ...):**`, `**Format:** Single promotional post + link in reply`, `**Post text**`, and `**Thread structure:**` + `**1/N**`. Each appears in every original of its type. No content runs remain. Removed or paraphrased: the reply-within-30-minutes tactic, the link-penalty reply label, the fixed image size string, and the "value post (70% bucket)" phrasing.

## Unknowns (questions to answer or test)

- Is there a banned-word or phrase list?
- Who is the account (persona, audience, company)? The voice is first-person company, but the backstory can't be seen.
- What is the full content-mix framework? Is 70/20/10 the value/interaction/promo split, and what defines each bucket?
- What exactly decides single post vs thread? Held-out 06 broke the inferred rule.
- When is a hashtag skipped, and is it ever more than one?
- Do other platforms (LinkedIn, Threads) or long-form briefs get a different package?
- Is posting-time or scheduling advice ever included?
- When exactly is the Notes section dropped?
