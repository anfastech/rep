# Ledger (train N=5: 01-05)

Caption = text inside the ``` block. Wrapper = everything around it.

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| 1 | Wrapper order: Saved line, Platform, Shape, First line pick, code block, Runner-up first lines, Comment keyword, Next action | 5/5 | observed | Always output exactly this skeleton |
| 2 | Line 1 `**Saved to `~/captions/<YYYY-MM-DD>-<kebab-slug>.md`**` | 5/5 | observed | Save the deliverable to ~/captions/ with date + topic slug; report the path first |
| 3 | Slug = 3-5 topic words, kebab-case | 4-5 words, N=5 | range | 3 to 6 topic words |
| 4 | `**Platform:** LinkedIn` | 5/5 | observed (value) | Platform line fixed; value LinkedIn in all 5 — whether other platforms exist is Unknown (P4/P5) |
| 5 | `**Shape:** <Shape name>. <why it fits, citing brief facts>` | 5/5 | observed | Name the chosen shape, then 1-2 sentences of justification |
| 6 | Shape "Before and after" (02, 03): brief has a measured contrast (before number vs after number) | 2/5 | menu (conditional) | If brief has a real measured contrast -> Before and after |
| 7 | Shape "Show the thing" (04, 05): no mistake and no measured contrast; brief is a thing/playbook/announcement | 2/5 | menu (conditional) | Fallback shape: say what it is and who it's for |
| 8 | Shape "The lesson from a mistake" (01): failure at scale + "what I'd do now" | 1/5 | unknown (shape seen once) | Folded; name kept since note calls it "highest-trust", trigger an Unknown |
| 9 | Priority order of shapes: 01 "highest-trust shape"; 04 "no mistake or measured contrast to build on" | 2 notes | tendency (inferred) | Check mistake first, then measured contrast, else Show the thing |
| 10 | `**First line pick:**` one-two sentences on why the hook stops the scroll | 5/5 | observed | Explain the hook choice in 1-2 sentences |
| 11 | `**Runner-up first lines:**` + exactly 2 quoted bullets, each a different angle | 5/5 | observed (count 2) | Give 2 alternative first lines (count could be configurable: unknown) |
| 12 | `**Comment keyword:** none (no link)` | 5/5, all briefs had no link | conditional (only no-link branch seen) | If no link: "none (no link)". With-link behaviour Unknown |
| 13 | `**Next action:** Post it, and reply to every comment within the first hour.` | 5/5 | observed fixed string | Verbatim |
| 14 | Caption: one sentence (sometimes 2-3) per line, blank line between every line | 5/5 | observed | Every line its own paragraph |
| 15 | Caption non-blank lines | 5 to 9 | range | about 5 to 11 lines |
| 16 | Caption words | 58 to 92 | range | about 50 to 110 words |
| 17 | First line words | 12 to 16 (61-90 chars) | range | ~10 to 18 words, under ~100 chars (fits before "see more") |
| 18 | First line content: concrete fact/number or flipped assumption; no setup | 5/5 (number in 3/5) | tendency | Lead with the most concrete fact; numbers in hook when brief has them |
| 19 | Line 2 short follow-up that adds stakes/proof | 5/5 | tendency | Usually |
| 20 | Last caption line = question to reader about their own experience | 5/5 | observed | End with one specific question (05: referral ask framed as question) |
| 21 | Questions in caption | 1 (only the closing one) | capped | Only the closing line is a question |
| 22 | Role skeleton: hook -> stakes/detail -> turn/insight or steps -> question | 5/5 | observed (roles) | |
| 23 | Mistake caption labels "What I believed: / What actually happened: / What I'd do now:" | 1/5 | unknown | Not a rule; question |
| 24 | List in Show-the-thing playbook: intro line ending ":" then one item per line, imperative, no bullets/numbers | 1/5 (04) | unknown/folded | Allowed in Show the thing; no bullets seen |
| 25 | Emojis, hashtags, exclamation marks in caption | 0/5 | absent | Default none (LinkedIn genre often has hashtags -> moderately strong) |
| 26 | Em/en dashes | 0/5 | absent | Default none (P11: may be generator setting) |
| 27 | Markdown inside caption | 0/5 | absent | Plain text caption |
| 28 | Numbers as digits (3, 9, 12, 41%, 3,000) | 5/5 mostly; "Two" sentence-initial, "a third" | tendency | Digits for numbers, words at sentence start |
| 29 | Voice first person (I/we), plain, contractions 2-5 | 5/5 | default | Conversational first person, contractions |
| 30 | Contrast lines ("not X", "X. It happened in Y") | 0-2 per output (02:2, 04:2, 03:1) | capped | At most 2 (cap unconfirmed) |
| 31 | Closing aphorism before question | 2/5 (02, 03) | tendency | Optional one-line takeaway before the question |
| 32 | "Here's how" bridge | 1/5 (04, list intro) | capped | at most 1 |
| 33 | Mean sentence words | 11-15 | range | short sentences |
| 34 | Hashtags/links in caption | 0 | unknown | Link handling: likely in comments with a keyword |

## Pattern walk (references/patterns.md)
- P1 AI tells: contrasts appear (max 2), "Here's how" once, aphorism 2/5, triple "Not 3 features. Not 3 bugs. 3 screens" once. So no strict ban visible; Unknown whether banned in stricter form. Don't add them to the template.
- P2 caps: rows 21, 30, 32.
- P3 menu: Shape line proves a named menu exists. 2 shapes seen twice, 1 once; more shapes likely exist (Unknown).
- P4 voice file: Unknown; voice is plain, consistent.
- P5 platform limits: hook <=90 chars suggests "see more" awareness; Unknown for other platforms.
- P6 optional sections: closing aphorism optional; runner-ups/keyword maybe configurable.
- P7 length tiers: all short (58-92 words). Unknown.
- P8 content-triggered: links -> Comment keyword (only "none" seen). Unknown.
- P9 packaging: visible here (save file, code block, notes, next action). Captured fully? Unknown if there is an approval step.
- P10 defaults: no hashtags/emoji as default.
- P11 dashes absent: may be generator setting.
- P12 voice protection: Unknown.
- P13 rotation: closing questions vary in form ("How do you", "When did you", "Which ... would you", "Which of these", "who should I") -> vary close (rotation unconfirmed). Next action is fixed, not rotated.
- P14 role skeleton: row 22.
