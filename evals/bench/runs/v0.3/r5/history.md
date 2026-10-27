# History

Checks (per replay vs original, block by block): S1 skeleton/line shapes, S2 Format line, S3 thread-vs-single choice, S4 post labels + char counts, S5 Hashtags line form, S6 hashtag count/placement, S7 closing question rule, S8 link-in-reply block, S9 Image specs block, S10 Notes block + bucket, S11 post length (chars), S12 mechanics (emoji/!/dashes/digits), S13 compare flags (count of stats outside train range).

## Round 1

| Check | A1 strict | B1 menu | C1 loose |
|---|---|---|---|
| S1 skeleton | 3/5 (no Notes/Image) | 5/5 line shapes match | 0/5 (labels "**Post i**", no "Thread structure") |
| S2 Format line | 4/5 (05 lists photo inside Format) | 5/5 | 3/5 (trailing period, varied) |
| S3 thread/single | 5/5 | 5/5 | 5/5 |
| S4 labels+counts | 5/5 | 5/5 | 2/5 |
| S5 Hashtags line | 4/5 | 2/5 (adds reason sentence after "(final post only)" / after tag) | 3/5 |
| S6 hashtag count | 4/5 (05 none) | 5/5 | 4/5 (03 adds tag to opinion) |
| S7 closing question | 5/5 | 5/5 | 5/5 |
| S8 link reply | 5/5 | 5/5 | 4/5 (label lacks reason) |
| S9 image specs | 0/2 | 2/2 (but literal "PNG for charts") | 1/2 (not bulleted) |
| S10 Notes | 0/4 | 4/4 with bucket | 4/4 but long |
| S11 post length | 4/5 (05 single 196 chars, 3 paragraphs) | 5/5 (1/5 at 138 chars, above 106 max) | 3/5 |
| S12 mechanics | 5/5 | 5/5 | 5/5 |
| S13 compare flags | 12 | 5 | 12 |

Winner by check: B1 wins S1,S2,S4,S6,S9,S10,S13; A1 wins S5. Others tied.
Remaining differences to fix in v2 (from B1 diffs): Hashtags line must be bare (`#Tag (final post only)`, `#Tag`) with a reason only after "None."; image format literal "PNG"/"JPG" only; Notes short (about 15-35 words); thread posts keep to 1-2 short sentences, hook under ~100 chars; promo single post one paragraph, no extra CTA line.

## Round 2 — v2 (B1 base + A1's bare Hashtags line + length/notes fixes)

| Check | v2 |
|---|---|
| S1 skeleton | 4/5 (05 lacks Notes; original has it) |
| S2 Format line | 5/5 |
| S3 thread/single | 5/5 |
| S4 labels+counts | 5/5 |
| S5 Hashtags line | 5/5 (fixed) |
| S6 hashtag count | 5/5 (05 picks #Hiring vs original place tag: content choice) |
| S7 closing question | 5/5 |
| S8 link reply | 5/5 |
| S9 image specs | 2/2 (fixed: bare PNG/JPG) |
| S10 Notes | 3/4 (missing on promo 05) |
| S11 post length | 5/5 (all thread posts 59-128; hook max 95) |
| S12 mechanics | 5/5 |
| S13 compare flags | 7 (mean/max sentence words driven by single-line posts without terminal punctuation in tokenizer; words 147 vs 146) |

Fixed vs v1: S5, S9, S11, S13. Remaining: Notes on promo posts. v3 = v2 + "Promo posts always get Notes, including a reminder to space promos between value posts" (conditional 1/1) + hashtag for announcements may be the place or topic.

## Round 3 — v3
Single change, tested by replaying B05 alongside the held-out replay (see below).
v3 = v2 + promo-Notes conditional + place hashtag for location news.
Train B05 replay (replay/v3-train/05.txt): Notes present with promo bucket and spacing reminder (S10 fixed), hashtag #Lisbon (S6 matches). New small deviation: adds "Careers page in the reply." inside the post (not in original). Round 3 stop: one fix, no further train differences of form. Frozen.

## Held-out (v3, frozen) — see report.md
