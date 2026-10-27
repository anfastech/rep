# Ledger (train N=5)

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| 4 sections, headers "## 1. Thread Outline", "## 2. Full Thread", "## 3. Hook Variations", "## 4. Posting Instructions", in order | 5/5 | observed | Always output these 4 headers verbatim, nothing before or after |
| Outline opens "Template: <Name> (<N> tweets)" | 4/5 | conditional (brief fits a menu template) | Name the template and tweet count |
| Outline opens "Format: Short announcement thread (<N> tweets)" | 1/5 (05 announcement) | conditional (brief fits no template) | Use "Format: <free description>" when no template fits |
| Outline: one "- Role: one-line content note" bullet per tweet, same count as tweets | 5/5 | observed | One bullet per tweet |
| Template menu: Story, Case Study, Contrarian Take, Tutorial (+ announcement fallback) | 1 each | menu (P3) | Pick by brief type; skeletons per template |
| Tweet header "Tweet N (X chars)" + blank line; X equals exact body length | 50/50 tweets exact | observed | Count real characters |
| Tweet length | 111 to 231 chars, N=49 | range | Each tweet under 280, usually 110 to 240 |
| Tweet count | 8 to 11; 8 only for short announcement | range + conditional | 10 to 12 standard; 7 to 9 short |
| One sentence or fragment per line, blank line between lines | 5/5 | observed (skeleton) | Every sentence its own paragraph |
| Lines per tweet | 2 to 6 | range | 3 to 6 typical |
| Mean sentence length | 9.1 to 9.8 words | range | Short, about 6 to 12 words |
| Hook tweet: number-led claim/result, 3 to 4 lines | 4/5 number in line 1 | tendency | Lead with the most concrete number |
| Hook ends with "Here's <what/how>...:" teaser | 3/5 (not tutorial, not announcement) | tendency | Usually end with a colon teaser |
| Tweet 2 opens "Some context." / "Some background." | 3/5 | tendency | Context tweet often opens this way |
| Arrow list (→ items, no blank lines) | 4/5, max 1 per thread, 2 to 4 items | capped | At most 1 arrow list per thread |
| Numbered list "1. ..." only in TL;DR/playbook tweet | 5/5 | observed | TL;DR as numbered list |
| TL;DR tweet "TL;DR:" second to last | 4/5; 02 replaced by "How to run this yourself:" playbook | conditional | Case study: playbook doubles as summary |
| TL;DR items | 4 to 5 | range | 3 to 6 |
| "Save this ..." line | 3/5 (story, case, tutorial) | tendency | Usually close the summary tweet with a save prompt |
| Last tweet CTA: follow me for more + "Retweet the first tweet ..." + question/ask | 5/5 retweet-first-tweet, 5/5 follow, 4/5 question "Reply below." | observed (parts), order varies | Final tweet has all three |
| Announcement CTA: tag someone / [link] placeholder | 1/5 | conditional | Use [link] placeholder for links |
| Hook Variations: exactly 4, "A." to "D.", "<Letter>. <Type label>" then hook text | 5/5 | observed | 4 alternates, labeled |
| Variation types differ from tweet 1 angle; Contrarian in 4/5 | 4/5 | tendency | Include a contrarian option usually |
| Variations usually end with ":" | 14/20 | tendency | |
| Posting: "Suggested posting time: <day(s)>, <time> ET. <audience reason>." | 5/5 | observed | |
| Posting: "Post all at once as a native thread. No delays between tweets." | 5/5 identical | observed fixed string | |
| Posting: "Recommended first reply: ..." bonus asset | 5/5 | observed | |
| Posting: "Engagement plan for the first hour:" + 4 sub-bullets, first "Stay online for 60 minutes after posting." | 5/5 | observed fixed | |
| "Retweet the hook once ... after 30 minutes if replies are slow." | 3/5 | tendency | |
| Emojis | 1 total (flag in announcement) | capped/absent | Default none; at most 1 when it adds meaning |
| Hashtags | 0/5 | absent | Default none |
| Em/en dashes | 0/5 | absent | Default none (P11 maybe generator) |
| Exclamation marks | 0/5 | absent | Default none |
| Bold/markdown in tweets | 0/5 | absent | Plain text tweets |
| Numbers as digits ("1 site", "4 moves") | 5/5; "one" only in idiom | default | |
| Contrast lines ("wasn't X. It was Y.", "Not X. Y.") | 01:3, 02:4, 03:2, 04:3, 05:1 | tendency | Used; not banned |
| Repetition triplets ("Same X. Same Y. Same Z.") | 3/5 | tendency | |
| Contractions | 10 to 18 per output | default | Conversational |
| Voice: first person (I or we), persona from brief | 5/5 | observed | |
| Banned words, voice file, length tiers | not observable | unknown | Unknowns |
