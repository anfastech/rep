# Report: target

Source: 7 outputs from one unknown skill, user split (train 01-05, held out 06-07). Genre: plain first-person LinkedIn-style post plus a short note to the requester.
Final draft: drafts/v3.md (frozen after round 3), exported to SKILL.md with the template format and a new example (library story hour, a topic no output uses).

## Rules by class (evidence from 5 train outputs)

| Rule | Class | Evidence |
|---|---|---|
| Post, blank line, then note to requester, no separator | observed | 5/5 |
| Note: 2-3 sentences, starts "I", one craft choice + why | observed / range | 5/5; 24-37 words |
| Note ends with an adjustment offer | tendency | 4/5 |
| Plain first-person fact as the opening, no question | observed | 5/5; first para 19-32 words |
| Short takeaway / next-step closing | observed | 5/5; 13-23 words |
| Tips shape (numbered, imperative + reason) | conditional | 1/5, list brief (04) |
| Announcement shape with ask + thanks | conditional | 1/5, announcement brief (05) |
| One-line turn after the opening | conditional | 2/5, surprising-result briefs (02, 03) |
| No invented facts; flag in note | conditional | 2/5 notes (01, 05) |
| Calm, modest tone; contractions 2-6 | default / range | 5/5 |
| Sentence max ~26 words | range | 21-26, N=5 (held out shows 27-31; see Untested changes) |
| Body 120-200 words, 4-8 paragraphs | range | 126-199 body words, 4-7 paragraphs |
| No questions, exclaims, emoji, hashtags, dashes, markdown | absent (default) | 0/5 each |
| Contrast lines at most 2; no reveal forms | capped | 0-2 per post; strict reveals 0/5 |

Full ledger with the pattern walk: ledger.md. Briefs: briefs.md, briefs-heldout.md.

## History (summary; per-check tables in history.md)

| Round | Drafts | Main result |
|---|---|---|
| 1 | A1 strict, B1 menu, C1 loose | A1 too terse (no contractions, short); B1 overlong notes and sentences; C1 used `---` separator and reveal contrasts. B1 won structure, C1 won note content. |
| 2 | v2 | Most checks 4/5-5/5; turn line over-applied; one mild reveal; one padded announcement |
| 3 | v3 (final) | Fixed reveals and padding; thin announcement came out short (114 words); turn line still over-applied in 01 |

## Held-out result per check (v3 on briefs 06, 07)

| Check | Result |
|---|---|
| Post + note, no separator | 2/2 |
| Note 2-3 sentences, starts "I", craft choice + offer | 2/2 (34, 37 words; orig 28-36) |
| Total words (orig 191-203) | 2/2 (196, 193) |
| First paragraph length (orig 27-28) | 2/2 (30, 25) |
| No questions/exclaims/emoji/hashtags/dashes | 2/2 |
| Contractions present | 2/2 |
| Max sentence length (orig 27-31) | 0/2 (18-24; rule caps at ~26, too tight) |
| Paragraph structure | 1/2: 07 matches; 06 original gives each change its own paragraph, the replay merged two |
| Closing | 1/2: 06 matches; 07 replay added an "If you're planning..." advice line, the original ends on thanks |
| Number style | 0/2: originals spell out "six months", "two days"; replays use digits |
| No invented facts; missing name flagged in note (07) | 2/2 |

## Negative control

Brief 07 with a generic prompt ("Write a LinkedIn post based on this brief"): 8-word one-line hook, 10 short paragraphs, 4 hashtags, a staccato aphorism line ("Maybe they should be."), no note to the requester. Compare flags 9 features outside the held-out range against 6 for v3. Most of v3's flags are the sentence-length cap and number style. The control is clearly worse on the checks that define this skill (note, hashtags, opening length), so the comparison discriminates.

## Leak check

`leak SKILL.md train/`: 0 shared 6-word runs. `leak SKILL.md heldout/`: 0.

## Unknowns

- Are AI-tell devices banned outright (triples, closing aphorisms, "not X, it's Y")?
- Is there a per-user voice file, or is the style fixed?
- Is the lack of dashes and questions from the skill or from the generator's settings?
- Is there a character limit or "see more" target for the opening?
- Are there length tiers?
- How are links, tables, code or long briefs handled?
- Is the note ever skipped, or ever replaced by alternatives?
- Are there voice-protection rules?
- Is the platform always LinkedIn?
- Number style: do digits vs words depend on the kind of number? The train set used digits and the held-out set spelled out durations.

## Untested changes (suggested by held-out; NOT applied to SKILL.md)

1. Widen the sentence-length default to "under about 32 words". Held-out sentences reach 31.
2. Add a fourth shape, "Reflection list": several observations, each in its own paragraph that opens with "I + verb", not numbered and not imperative (06).
3. Closing: write "If you..., try..." advice only when the brief gives a takeaway for readers. Recognition posts end on thanks (07).
4. Number style: make it a weak default. Spell out durations like "six months" and "two days", and keep digits for counts, money and percentages.
5. One-line turn: still over-applied after round 3 (train 01). Consider "rare; at most where the brief itself names a surprise".
