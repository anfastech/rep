# History

Checks: tools/checks.py (structural, per file) + style_stats compare + manual block diff.

## Round 1 (A1 strict, B1 menu, C1 loose), train briefs 01-05

| Check | A1 | B1 | C1 |
|---|---|---|---|
| 3 fences + order, card head, fields, alignment, linter string | 5/5 | 5/5 | 5/5 |
| line1 <=125 and visible count exact | 5/5 | 5/5 | 5/5 |
| line1 length in orig band (75-111) | 1/5 (47-77, too short) | 2/5 (63-107) | 3/5 (69-103) |
| 3 lowercase hashtags last line | 5/5 | 5/5 | 5/5 |
| alt-text conditional (none for reel) | 5/5 | 5/5 | 5/5 |
| <=3 sentences/paragraph, single blank lines | 5/5 | 5/5 | 5/5 |
| no dash/emoji/!/link | 5/5 | 5/5 | 5/5 |
| words 60-160 (caption) | 4/5 (03: 57) | 5/5 | 5/5 |
| search line numbers true (count blank lines) | 5/5 | 5/5 | 0/5 (counted paragraphs) |
| paragraph count vs orig (diff) | 4/5 match ±1 | 5/5 match exactly | 1/5 (all 7-8, padded) |
| shape per brief type (story/list/announcement) | partial: 03 dropped context para | 5/5 | 03 adds "Takeaway:" label, extra para |
| style_stats flags | 5 (words low x2) | 4 (max_sentence_words low x5) | 4 (contractions 1-1) |
| ask field style (short lowercase paraphrase) | 5/5 | 0/5 (pastes caption sentence) | 5/5 |
| hyphenated words kept | n/a | 0 (agent read "no dashes" as no hyphens) | 0 (same) |
| alt text describes the visible content (data/list on cover) | 2/4 | 1/4 | 2/4 |

Winners: B1 for shape and length; A1/C1 for ask field; A1/B1 for search line numbering.

Differences to fix in v2 (rule behind each):
- Hook too short -> say line 1 should use most of the visible 125 chars (observed 75-111), often 2 sentences: fact + turn.
- Ask field -> short lowercase paraphrase ("one, save it").
- "No dashes" ambiguous -> "no em or en dashes; normal hyphenated words are fine".
- Alt text -> describe what the image shows, including any chart result or text listed on the cover.
- Search line numbering -> keep explicit "count blank lines; paragraphs fall on lines 1,3,5...".
- Long sentences: original's longest sentences were in list items / card; B1 fine on caption. No rule change.

## Round 2 (v2 = B1 shapes + A1/C1 ask field + fixes)

| Check | v2 |
|---|---|
| structural checks (fences, card, alignment, linter, visible exact, tags, alt conditional, <=3 sent, mechanics, search lines) | 5/5 all pass |
| line1 length in orig band | 5/5 (93-105) — fixed |
| words 60-160 | 5/5 |
| paragraph count vs orig | 5/5 exact (6,7,7,8,5) |
| ask field style | 5/5 — fixed |
| alt text describes content | 3/4 (04 cover gives title only; orig names the items) |
| style_stats flags | 3 (words 150 vs 153 min, digits 15, we_our 8) — minor |
| shape per brief type | 5/5 |

Subagent-reported ambiguities: list items as paragraphs; job A ending; search phrase reporting; takeaway openers required or examples.
Fixes for v3: alt text names listed items; list items are separate paragraphs; job A ends on the new-practice paragraph with no second ask; search phrases are exact strings, prefer two different phrases on different lines; takeaway openers are examples.

## Round 3 (v3 = v2 + clarifications + contrast cap + example + unknowns)

| Check | v3 |
|---|---|
| structural checks (all tools/checks.py) | 5/5 all pass |
| line1 length in orig band | 5/5 (90-105) |
| paragraph count vs orig | 5/5 exact |
| ask field style | 5/5 |
| job A ending (practice last, no 2nd ask) | 1/1 |
| alt text names cover items | 0/1 applicable (04: replay brief did not list the cover's items; brief limitation, not a rule gap) |
| style_stats flags | 5 marginal (each 1 file, within ~10% of range edge) |

Round 3 fixed only ambiguity, nothing form-level left to fix. Stop. v3 is the final draft.

## Step 8 held-out (final.md = v3, frozen) — see report.md for per-check table.
## Step 9 leak: removed 3 copied caption-level phrases (bio-link ask wording, comment-ask card wording). Remaining matches are card fixed strings only.
