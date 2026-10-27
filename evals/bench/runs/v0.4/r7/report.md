# Reverse-engineering report: target

The target is an **Instagram caption skill for business accounts**. It outputs a fenced caption, an alt-text line for still images, and a fenced `CAPTION READY` status card. The card refers to a linter script (`caption.py`) that was not run.

- Data: 7 outputs. Train: 01-05 (1 reel, 2 carousels, 1 single image, 1 single photo). Held out: 06, 07 (both reels). The user's split was kept.
- Files: `briefs.md`, `heldout-briefs.md`, `ledger.md` (full feature table), `history.md` (every draft with its per-check scores), `drafts/` (A1, B1, C1, v2), `replay/` (A1, B1, C1, v2, heldout, control), `tools/checks.py` (per-check scorer), `SKILL.md` (export = frozen v2 after the leak cleanup).

## Rules and evidence (summary of ledger.md)

| Rule | Class | Evidence |
|---|---|---|
| Three parts: fenced caption, then the alt-text line, then the fenced card | observed | 5/5 (alt line conditional) |
| One line per paragraph, with a blank line between | observed | 5/5 |
| Line 1 fits in 125 chars; the card reports its exact length | observed | 5/5 (75-111 chars) |
| Still posts: line 1 is the hook, `job: B - <format>, line one is the hook` | observed for still posts | 4/4 |
| Exactly one ask (`ask: one, ...`) | observed | 5/5 |
| Exactly 3 lowercase hashtags as the last line, none elsewhere | observed (count's source range unknown) | 5/5 |
| No links in the caption, with the bio variant in the card | observed | 5/5 (bio 1/1) |
| Two search phrases, reported by line number (blank lines counted) | observed | 5/5 |
| Alt text `(cover slide)` for carousels, plain `Alt text:` for single images | conditional | 2/2, 2/2 |
| Card's fixed lines and field order | observed | 5/5 |
| At most 3 sentences per paragraph | capped | max 3 |
| Ask chosen by goal: save for reference value | conditional | 2/2 save asks |
| Hook uses most of the 125 chars and carries a number | range/tendency | 75-111, 4/5 at 105+ |
| Ask on its own line above the hashtags, no recap line | tendency | 3/5 |
| "If you / Before you" takeaway line | tendency | 2/5 (+1 merged with the ask) |
| "Most ..." context line | tendency | 2/5 |
| No emoji, no "!", no dashes | absent (default) | 0/5 |
| Body 4-7 lines, caption 71-135 words | range | N=5 |
| Reel → job A, caption opens with the ask, no alt text | unknown at freeze (seen 1/5) | 1 train reel; confirmed 2/2 held-out reels after the freeze |

## History (see history.md)

- Round 1: A1 (strict) won on job-line format and on reel alt text. B1 (menu) lost the exact job-line format (0/4, 0/1). C1 (loose) gave the reel alt text and went over the paragraph range once. All three wrote hooks that were too short and added "Takeaway:" labels and recap lines.
- Round 2: v2 = A1 base + B1's ask menu + fixes. All 15 form checks passed on 5/5 train replays. There were 5 small compare flags, each from a single file. Stopped: nothing left to fix that 2+ outputs support.

## Held-out result per check (v2 on 06, 07; both reels)

| Check | Result |
|---|---|
| two_fences | 2/2 |
| card_fields (fixed lines, order, alignment) | 2/2 |
| visible_correct | 2/2 |
| line1_le125 | 2/2 |
| alternating_blank | 2/2 |
| hashtag_line_3_lower / no_tags_elsewhere | 2/2 / 2/2 |
| body_paras_4to7 | 2/2 |
| no_link | 2/2 |
| no_emoji_excl_dash | 2/2 |
| search_2_correct_lines | 2/2 |
| job_A_for_reel | 2/2 (only because the Unknowns described the one train reel) |
| no_alt_for_reel | 2/2 |
| Ask as line 1 for reels | 2/2 |
| Search phrase length (rule: 2 words) | **fail**: the originals used 3-word phrases ("returning to work", "late delivery penalties"); the replay used 2-word ones |
| Word count (`compare`) | **fail**: replay 186-199 words vs original 148-154; replays added a context line and a reader-takeaway line |
| Ending | **fail**: the originals end on the last item or a one-line observation, with no "If you ..." takeaway; both replays added one |
| List form (06) | **diff**: the original used unnumbered "I <verb> more." lines; the replay numbered them |
| Ask kind (07) | **new kind**: share ("Send this to ..."), not in the ask menu; the replay handled it correctly from the brief |
| `compare` flags | 10 features outside the held-out range (N=2, so the range is very narrow) |

## Negative control

Brief 07 with a generic "write an Instagram caption" prompt (`replay/control/07.txt`): no fences, no alt text or card, 8 hashtags, 3 emojis, "No new platform. No six-month rollout." device. It fails `two_fences`, so every other check is unscorable, and `compare` flags 13 features. It is clearly worse than v2, so the checks discriminate.

## Leak check

`style_stats.py leak SKILL.md train/`: 89 shared 6-word runs, all from the status card.
- 5/5 fixed lines: `CAPTION READY`, `of 125 characters used before the cut`, `linter: READY, checked by hand against caption.py's rules`, `hashtags: 3`.
- Card value formats that are fixed per media type: `B - carousel cover, line one is the hook` and similar (4/5), `first comment: none, no link` (4/5), the bio variant of `first comment` (1/5), and `A - the reel carries the hook` (1/5, in Unknowns).

These are template strings of the card, not caption content, so they were kept as a documented exception: the method allows only 5/5 lines, and these are 1-4/5 card variants. Removed before export (none were rule changes): the quoted bio-link caption sentence from 05, the "out loud in the video too" note, and the example card's "save it" and "in line 1 and line 3" (they matched originals). The example caption (dental clinic) shares no runs with the outputs.

## Untested changes (suggested by the held-out outputs, NOT applied to SKILL.md)

1. Promote "reel → `job: A - the reel carries the hook (<who on camera / on-screen text>, "<words>" in the first two seconds)`, caption line 1 is the ask, no alt text" to a conditional rule (3/3 reels).
2. Search phrases: 2 to 3 words, not exactly 2.
3. Reels: no reader-takeaway line; end on the last point or a one-line observation. Reel captions are shorter (4-5 lines after the ask, 82-84 words including hashtags).
4. Add the share ask (`Send this to <who>.`, card `ask: one, share it`) to the ask menu.
5. Personal lists can be unnumbered parallel lines ("I <verb> ...").
6. Caption word range across all 7 outputs is 71-135 (held out 82-84); the v2 range holds, but reels sit at the low end.

## Unknowns (questions for the user)

- Is there a fixed menu of job letters (A, B, maybe C...) and what triggers each? Does every reel get A, or only reels whose video opens on the hook?
- Are 3 hashtags fixed, or one point of a range?
- What does `caption.py` check (125-char cut, hashtag count, banned words, link ban)? When does it report something other than READY?
- When is a first comment used? Every output said "none".
- Is the voice fixed, or does it come from a per-brand voice file? Are there length tiers?
- Are "not X, it's Y" contrasts capped? Up to 3 were seen in one caption, so they are not banned.
- Does the absence of emojis, dashes and "!" come from the skill or from the generator's settings?
- Packaging: is anything else delivered (variants, an explanation note)? Only the paste-ready blocks were captured.
