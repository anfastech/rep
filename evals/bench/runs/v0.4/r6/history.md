# History

Checks (train N=5, originals in brackets):
- K1 wrapper fixed lines exact (Saved line format, 4 fixed lines, 2 quoted bullets)
- K2 shape choice matches original
- K3 caption words within 58-92
- K4 caption non-blank lines within 5-9
- K5 first line words within 12-16
- K6 only question = closing line
- K7 no emoji/hashtag/dash/markdown in caption
- K8 list items unnumbered, no bullets (04)
- K9 Shape note length (orig 14-25 words on the line)

## Round 1

| Check | A1 strict | B1 menu | C1 loose |
|---|---|---|---|
| K1 wrapper | 5/5 | 5/5 | 0/5 (Saved line as "**Saved to:** path", bullets in blockquote) |
| K2 shape | 4/5 (01 -> Show the thing) | 5/5 | 5/5 (name "Lesson from a mistake", missing "The") |
| K3 words | 4/5 (04=118) | 4/5 (01=105) | 4/5 (01=93) |
| K4 lines | 4/5 (01=10) | 4/5 (01=10) | 5/5 |
| K5 first line | 2/5 (19,12,11,16,11) | 5/5 | 1/5 (10-12) |
| K6 question | 5/5 | 5/5 | 5/5 |
| K7 mechanics | 5/5 | 5/5 | 5/5 |
| K8 list | 0/1 (numbered 1-4 with explanations) | 1/1 | 1/1 |
| K9 Shape note | 5/5 (17-23) | 0/5 (29-49, too long) | 5/5 |

style_stats compare: A1 9 flags, B1 9 flags (mean/max sentence words driven by long Shape notes), C1 7 flags.

Diffs by block:
- A1 01: no mistake shape in the menu, so failure brief was forced into Show the thing. A1 04 added a "most teams" setup line and a closing aphorism; numbered list.
- B1: captions closest to originals; Shape justifications run 2-3 long clauses. 01 caption 10 lines / 105 words (extra "Here's what I'd do now." line plus a split "I believed" line).
- C1: wrapper drift (no fixed Saved line, blockquote bullets, quoted first line inside First line pick); first lines short (10-12 words).
- All: A1 and C1 add a closing aphorism ("Slower on paper...") in 01; originals have it 2/5 (02, 03), never in 01.

Winners: K1 A/B, K2 B, K5 B, K8 B/C, K9 A/C, K4 C.
v2 plan: B1 base + A1's short Shape note (one sentence, ~15-25 words) + cap caption at ~100 words / 9-10 lines + first line 12-16 words stated + "no numbers or bullets on step lines" + "never the hook's text quoted inside First line pick".

## Round 2 (v2 = B1 base + A1 short Shape note + caps)

| Check | v2 |
|---|---|
| K1 wrapper | 5/5 |
| K2 shape | 5/5 |
| K3 words 58-92 | 4/5 (02=57, inside the widened 55-100 default) |
| K4 lines 5-9 | 5/5 |
| K5 first line 12-16 | 5/5 |
| K6 question | 5/5 |
| K7 mechanics | 5/5 |
| K8 list | 1/1 |
| K9 Shape note 14-25 | 4/5 (01=29) |

style_stats compare: 6 flags. max_sentence_words flagged x5: traced to the runner-up block. Originals write one runner-up as two short sentences or question+answer in 4/5 (01, 02, 04, 05); v2 runner-ups are all single long sentences (0/5). Runner-up word counts are fine (orig 8-15, v2 11-14).
Remaining diffs: captions a little shorter (57-82 vs 58-92); 04 playbook steps lack the short reason the original adds after 3 of 4 steps (seen once -> Unknown, not a rule).
v3 plan: v2 + runner-up form tendency.

## Round 3 (v3 = v2 + runner-up form)

| Check | v3 |
|---|---|
| K1 wrapper | 5/5 |
| K2 shape | 5/5 |
| K3 words 58-92 | 4/5 (05=50) |
| K4 lines 5-9 | 5/5 |
| K5 first line 12-16 | 5/5 |
| K6 question | 5/5 |
| K7 mechanics | 5/5 |
| K8 list | 1/1 |
| K9 Shape note 14-25 | 4/5 (01=29) |
| K10 runner-up two-sentence form (orig: exactly one bullet in 4/5 outputs) | overshoot: both bullets two-sentence in 5/5 |

style_stats compare: 6 flags but all whole-file length/sentence features now inside or at the edge of the original range (lines, nonblank, sentences, mean sentence words all in range; max_sentence_words now low 23-26 vs 24-46).
Diffs: 04 replay adds a contrast line "Little leverage isn't the same as none." (within cap 2). Captions run slightly short (50-82).
Round limit reached (3). Final = v3 with the runner-up rule tightened to "one of the two (not both)" to correct the overshoot; this wording is tested only by the held-out replay.
