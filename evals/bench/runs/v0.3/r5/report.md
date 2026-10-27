# Reverse-engineering report: target

Source: 7 outputs (train 01-05, held out 06-07), user split kept. Route: plain text (X/Twitter posts and threads, delivered as a markdown package). Exported skill: `SKILL.md` (= drafts/v3.md with leak fixes).

## What the source skill is
An X (Twitter) post writer. It picks thread vs single post from the brief, then returns a package: `**Format:**` line, post(s) in code blocks each labelled with an exact character count, a `**Hashtags:**` line, optional link-in-reply block, optional `**Image specs**` (1200×675, 16:9, PNG/JPG, under 5MB), and usually `**Notes:**` naming a 70/20/10 value/interaction/promo bucket plus a posting tactic.

## Ledger (summary; full table in ledger.md)
| Rule | Class | Evidence |
|---|---|---|
| `**Format:**` first line | observed | 5/5 train, 2/2 held-out |
| Labels `**i/N** (X chars[, including hashtag])`, posts in code blocks, `i/N ` prefix | observed | 3/3 threads (+1/1 held-out) |
| `**Post text** (X chars)` for single | observed | 2/2 (+1/1 held-out) |
| `**Hashtags:**` line, bare; reason only after "None." | observed | 5/5 (+2/2) |
| At most 1 hashtag, at end of final post | capped | max 1 |
| Thread for sequence/list/data; single for one claim or news | conditional | 5/5 train; held-out 06 broke it (see below) |
| Closing question, except promo | conditional | 4/5 (+2/2) |
| Link goes in an immediate reply; URL = 23 chars | conditional | 1/1 |
| Image specs when data or real-people photo | conditional | 2/5 (+1/2) |
| Notes block | tendency | 4/5 (+1/2); skipped on data threads with chart in 2/2 cases (02, 07) |
| Bucket label (70/20/10) in Notes | tendency | 3/5 (0/1 held-out notes) |
| Thread length | range | 4-5 posts (held-out 4); widened to ~3-7 |
| Chars per thread post | range | 56-106 (held-out 69-107) |
| No emoji, no "!", no em dashes, digits for numbers | default (absent) | 0/7 |
| "Not X" contrasts | capped | max 2 per output (unconfirmed) |
| Triples | capped | max 1 train; held-out 06 has a 3-item list (a list brief) |
| Never say "thread" in the hook | stated in source notes (01) | 7/7 |

## History
Round 1: A1 strict / B1 menu / C1 loose, blind subagent replays of 5 train briefs. B1 won S1 skeleton, S2, S4, S6, S9 image specs, S10 notes, S13 (5 stat flags vs 12/12); A1 won S5 (bare Hashtags line). Round 2: v2 merged them, flags 7, all checks 5/5 except Notes on promo. Round 3: v3 fixed promo Notes (tested on B05). Per-check tables in history.md.

## Held-out result per check (v3 frozen, replay/heldout/)
| Check | 06 (personal reflection, 3 changes) | 07 (data/recognition story) |
|---|---|---|
| S1 skeleton | FAIL: replay made a 4-post thread; original is a single post | PASS (thread structure, Hashtags, Image specs) |
| S2 Format line | FAIL (follows from S3) | FAIL: original `Thread (4 posts) + image`; replay omitted "+ image" although it added image specs |
| S3 thread vs single | FAIL | PASS |
| S4 labels + char counts | PASS (form) | PASS |
| S5 Hashtags line form | PASS (form) | PASS |
| S6 hashtag count | FAIL: original "None." for personal story; replay added #WorkLifeBalance | PASS (#Logistics, final post only) |
| S7 closing question | PASS (but replay also put a question in the hook post) | PASS |
| S9 image specs | n/a | PASS (PNG, 1200×675); original also had overlay callouts, not modelled |
| S10 Notes | PASS present; replay adds bucket label, original does not | Replay adds Notes; original has none (tendency allows both) |
| S11 post length | PASS | PASS (58-104 vs 69-107); 5 posts vs 4 |
| S12 mechanics | PASS | PASS |
| S13 compare flags | 10 flags over the pair (mostly words/sentences higher: thread vs single on 06) | |

## Negative control
Generic prompt ("write an X post", same briefs, replay/control/): no package at all: no Format line, no char counts, no code blocks, no Hashtags line, no image specs or notes; numbered/bulleted lists. 0/2 on S1, S2, S4, S5, S9, S10. The comparison discriminates: the skill's wrapper is what matters, and the generic output lacks it entirely. (Note: on 06 the control's single-post choice actually matched the original better than v3's thread.)

## Leak check
`style_stats.py leak SKILL.md train/`: first run 12 shared 6-word runs, all from copying the 05 reply label and image-spec heading; reworded. Final: 0 against train, 0 against held-out.

## Untested changes (suggested by held-out; NOT applied to SKILL.md)
1. A short personal reflection, even with 2-3 points, should be a single post: hook line, the points as stacked one-line sentences, then the question. Thread only when each point needs its own explanation.
2. Personal stories get no hashtag: `**Hashtags:** None. <reason>`.
3. Only one question per output, in the last post.
4. When image specs are present, always add "+ image" / "+ chart image" to the Format line.
5. Image specs may include overlay callouts (key numbers on the image) and a privacy note (blur sensitive data).
6. Notes need not name a bucket. The bucket appeared in 3/6 Notes.

## Unknowns (questions for the user)
- Is the 70/20/10 value/interaction/promo mix fixed in the source, or a content calendar the user supplies?
- Is there a per-user voice file (tone, banned words, preferred hashtags, sign-offs)?
- Are AI-tell devices banned (reveal bridges, closing aphorisms, "not X, it's Y")? Only one "Not a bluff." fragment was seen.
- Are there length tiers, e.g. long threads of 8+ posts or long-form posts for premium accounts?
- How does the source handle video, polls, quote posts, or replies to other accounts? None were seen.
- Do the no-emoji, no-em-dash and no-exclamation habits come from the source or from the generator's global settings?
- Is the package wrapper (Format/Hashtags/Notes) the source's deliverable, or was the post text sometimes handed over bare?
- When does the source drop Notes? Both data threads with charts (02, 07) had none.
