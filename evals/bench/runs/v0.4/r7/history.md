# History

Checks: `tools/checks.py` (form checks per file) + `style_stats.py compare train replay/<d>` (flags outside train range) + manual block diff.
Media per brief: 01 reel, 02 carousel, 03 single image, 04 carousel, 05 single photo.

## Round 1: A1 (strict), B1 (menu), C1 (loose)

| Check | A1 | B1 | C1 |
|---|---|---|---|
| two_fences | 5/5 | 5/5 | 5/5 |
| card_fields | 5/5 | 5/5 | 5/5 |
| visible_correct | 5/5 | 5/5 | 5/5 |
| line1_le125 | 5/5 | 5/5 | 5/5 |
| alternating_blank | 5/5 | 5/5 | 5/5 |
| hashtag_line_3_lower | 5/5 | 5/5 | 5/5 |
| no_tags_elsewhere | 5/5 | 5/5 | 5/5 |
| body_paras_4to7 | 5/5 | 5/5 | 4/5 |
| no_link | 5/5 | 5/5 | 5/5 |
| no_emoji_excl_dash | 5/5 | 5/5 | 5/5 |
| search_2_correct_lines | 5/5 | 5/5 | 5/5 |
| job_B_still (exact "B - <format>, line one is the hook") | 4/4 | 0/4 | 4/4 |
| job_A_for_reel | 1/1 | 0/1 (format "A, ...") | 1/1 |
| no_alt_for_reel | 1/1 | 1/1 | 0/1 |
| alt_form | 4/4 | 4/4 | 4/4 |
| compare flags (outside train range) | 3 (words low x2) | 5 (words low x3) | 6 (lines/paras high) |

Manual diff findings:
- Hook line 1 length: originals 75-111 chars (4/5 at 105-111). Replays A1 74-89, B1 58-78: hooks too short, second hook sentence (the "for 18 months" twist) moved to its own line. -> v2: hook uses most of the 125 characters, often 2 sentences.
- Takeaway labelled "Our takeaway:" (A1/03, C1/03) — never in originals, which open the takeaway with "If you ..." / "Before you ...". -> v2 default.
- C1/04 and C1/03 add an extra summary/aphorism line before the ask ("These four usually are."). Originals: ask follows the last body line directly. -> v2: no recap line.
- B1 job line format drifted ("B, line one is the hook"); needs the literal format in the card template. A1 and C1 had it.
- C1 gave the reel alt text (originals: none for the reel). A1 kept it off.
- Search phrases: C1/01 used a 3-word phrase; originals always 2 words. -> v2.
- List items (04): replays wrote noun fragments ("1. Your renewal deadline."); original items open with an imperative and add 1-2 explanation sentences (seen once, default only).
- Word counts: A1/B1 slightly short (hook compression, fewer explanation sentences).

Winner per check: A1 on job lines, reel alt, para count, compare flags; C1 equal on job lines. v2 = A1 base + B1's ask menu (worked, all asks matched type) + fixes above.

## Round 2: v2 (A1 base + B1 ask menu + round-1 fixes)

| Check | v2 |
|---|---|
| two_fences, card_fields, visible_correct, line1_le125, alternating_blank | 5/5 each |
| hashtag_line_3_lower, no_tags_elsewhere, body_paras_4to7, no_link, no_emoji_excl_dash | 5/5 each |
| search_2_correct_lines | 5/5 |
| job_B_still | 4/4 |
| job_A_for_reel | 1/1 (followed the Unknowns description) |
| no_alt_for_reel | 1/1 |
| alt_form | 4/4 |
| compare flags | 5 (sentences x1, mean sentence words x1, hyphens, digits, we_our: each one file, small margins); words now inside the range |

Manual diff:
- Hook length fixed: 88 to 119 chars (train 75 to 111). Fine.
- No "Takeaway:" labels and no recap line before the ask: fixed.
- List items are imperative + explanation now: fixed.
- Remaining: the reel replay (01) adds a reader-takeaway line after the "Now ..." line; the original has none. The reel shape was seen once, so no rule can be written for it. Logged as an Unknown.
- 05: a 2-word search phrase includes a place name ("Lisbon office"). The original also used a place ("jobs in Lisbon"). Acceptable.

Stopping here: a third round has nothing left to fix that 2+ outputs support. v2 = final draft.
