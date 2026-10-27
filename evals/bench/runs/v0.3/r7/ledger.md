# Ledger (train N=5: 01-05)

Genre inference: Instagram captions (125-character "more" cut, "link in bio", alt text, reels/carousels, 3 hashtags). Not stated in outputs; inferred from P5 units.

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| 1 | Deliverable = fenced caption block, then optional "Alt text" line, then fenced "CAPTION READY" card | 5/5 | observed | Always output in this order |
| 2 | Card first line "CAPTION READY" | 5/5 | observed (fixed string) | Verbatim |
| 3 | Card fields in order job, visible, ask, hashtags, search, first comment, linter; values aligned to column 13 (first comment unpadded) | 5/5 | observed | Verbatim labels and alignment |
| 4 | `linter:     READY, checked by hand against caption.py's rules` | 5/5 | observed (fixed string) | Verbatim when linter not run; implies a caption.py linter exists (unknown what it checks) |
| 5 | job: "A - the reel carries the hook (...)" vs "B - <format>, line one is the hook" | A 1/5 (reel), B 4/5 (carousel cover, single image, single photo) | conditional: format | Reel whose video shows the hook = job A; otherwise B. Other jobs (C?) unknown |
| 6 | Job A: caption line 1 is the ask (comment keyword + what they get); no closing ask; keyword also said out loud in video | 1/5 (01) | conditional: job A | If A, line 1 = keyword ask |
| 7 | Job B: line 1 is the hook, 1-2 sentences, fully visible before the cut | 4/4 B | conditional | If B, line 1 is hook |
| 8 | Line-1 length | 75-111 chars, all <=125 | range + hard ceiling | Line 1 <= 125 chars (platform cut); observed 75-111; aim 70-120 |
| 9 | visible: "<n> of 125 characters used before the cut" with n = chars of line 1 | 5/5 | observed | Count exactly |
| 10 | Hook type | number-result (02,03), question+claim (04), announcement fact (05) | tendency | Concrete fact/number or reader's situation; no hype |
| 11 | Exactly one ask per caption | 5/5 | observed | ask: "one, <ask>" |
| 12 | Ask kind follows brief goal: comment keyword (lead magnet), save (useful/reference), comment question (opinion), link in bio (hiring/link) | 5/5 distinct | conditional: goal | Menu |
| 13 | Ask placement: last paragraph before hashtags (B); first line (A) | 5/5 | conditional | |
| 14 | Takeaway/lesson paragraph before ask ("If you want...", "Before you...", "Now every...") | 3/5 (01,02,03 stories); absent in list (04) and announcement (05) | conditional: story/lesson briefs | |
| 15 | Hashtags: exactly 3, lowercase, no camelcase, last caption line, niche + broader | 5/5 | observed (count) | 3 hashtags; count may be configurable |
| 16 | hashtags field: "3" | 5/5 | observed | |
| 17 | search: 2 quoted keyword phrases with line numbers (line numbers count blank lines); one usually in line 1 or 3, the other in the takeaway/ask line | 5/5 | observed | Place 2 search phrases, report their line numbers |
| 18 | first comment: "none, no link" ; when brief has a link: "none, the link lives in the bio, not the caption" | 4/5 / 1/5 | conditional: link | No links in caption |
| 19 | Alt text line outside fences: "Alt text (cover slide): ..." for carousel, "Alt text: ..." for single image/photo, none for reel | 4/5 | conditional: format | |
| 20 | Every paragraph separated by a blank line; paragraphs 1-3 sentences | 5/5, max 3 | capped | At most 3 sentences per paragraph |
| 21 | List briefs: numbered "1. " items, each its own paragraph, bold label sentence then 1-2 explanation sentences | 1/5 (04) | conditional: list | |
| 22 | Paragraph count (caption incl. hashtags) | 5-8 | range | about 4-9 |
| 23 | Caption words | 74-138 (chars 426-811) | range | about 60-160 words |
| 24 | Emojis | 0/5 | absent | default none |
| 25 | Em/en dashes | 0/5 | absent | default none (P11: may be generator setting) |
| 26 | Exclamation marks | 0/5 | absent | default none |
| 27 | Markdown bold/headers inside caption | 0/5 | absent | plain text (Instagram does not render markdown) |
| 28 | Contractions | 1-5 per output | default | conversational |
| 29 | Person: I/we for company stories, you for advice | mixed | tendency | |
| 30 | Contrast lines ("not X", "X. What failed was Y", "weren't X. They were Y") | 0-2 per output (04 has 2 "not" phrases; 01,02 one reveal each) | capped | at most 2 (cap unconfirmed) |
| 31 | Rule-of-three triples | 0 strict triples | absent | likely banned? (Unknown) |
| 32 | Closing aphorism | 0/5 (closings are concrete asks) | absent | Unknown if banned |
| 33 | "Here's the thing"/reveal bridges | 0/5 | absent | Unknown |
| 34 | Engagement bait ("Agree?") | 0/5 except genuine question in 03 | absent | Unknown |
| 35 | Numbers as digits (3,000; 41%; 22) | 5/5 | default | digits for data; "Nine"/"Two" spelled at sentence start |
| 36 | Short sentences, mean 10-19 words | range | default | |
| 37 | Reel-only note: "(say KEYWORD out loud in the video too)" | 1/1 A | conditional | |
| 38 | Hook paraphrased in card for A: "(<presenter> on camera, "<hook>" in the first two seconds)" | 1/1 | conditional | |
| 39 | Banned words list | not observable | unknown | |
| 40 | Voice file | not observable | unknown | |
