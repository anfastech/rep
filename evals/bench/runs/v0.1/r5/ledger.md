# Ledger (train N=5)

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Output is a posting package for X/Twitter (char counts, 280-limit style, link penalty, hashtags) not raw copy | 5/5 | observed | Output a formatted package: format line, post copy in code blocks, metadata sections |
| First line `**Format:** <format>` | 5/5 | observed | Always start with `**Format:** ...` |
| Format chosen: thread for story/lessons/list/data (01,02,04); single post for opinion/announcement (03,05) | 5/5 | conditional | Thread when brief has a sequence (story, steps, list, data walk-through); single post for one take or announcement |
| Thread header `**Thread structure:**` then per post `**k/N** (X chars)` + code block | 3/3 threads | observed | Fixed label format |
| Each thread post starts with `k/N ` inside the text | 3/3 | observed | Number every post `k/N ` |
| Thread length | 4 to 5 posts, N=3 | range | 3 to 7 posts, usually 4 to 5 |
| Per-post length | 56 to 107 chars, N=14 | range | Far under 280; aim about 50 to 130 chars |
| Single post `**Post text** (X chars)` + code block | 2/2 singles | observed | Fixed label |
| Char counts accurate; "(X chars, including hashtag)" when a hashtag is in that post; URL counted as 23 | 5/5 | observed | Count exactly, annotate |
| Single post length | 124 to 130 chars | range | about 80 to 200 chars |
| Single post line breaks: 03 is 3 short paragraphs split by blank lines; 05 one paragraph | 1/2 | tendency | Opinion posts: claim / proof / question on separate lines |
| Hook: first post states the stake or result with a number or a sharp claim, 3-8 words first sentence | 5/5 | observed | Hook = punchy claim/number, no setup |
| Hook never says "thread", no 🧵 | 0/3 threads say it; 01 note states this | observed | Never use "thread" in the hook |
| Ends on an open question to the reader | 4/5 (not 05 promo) | conditional | Non-promo: final post ends with a question inviting replies |
| Final thread post: takeaway/instruction then question then hashtag | 3/3 | observed | |
| Hashtags: exactly 1, placed at end of final post | 4/5; 03 none | observed/conditional | Max one hashtag, last post end; topic-level CamelCase (#CustomerSupport) |
| `**Hashtags:**` line always present; "(final post only)" in threads; "None." + reason when none | 5/5 | observed | |
| No hashtag for contrarian take post (03) | 1/5 | conditional (weak) | Pure opinion/interaction posts may skip hashtag, say why |
| Link kept out of main post, put in reply with `**Reply ...**` section, note link penalty ~50% | 1/1 links | conditional | If brief has a link, put it in a reply |
| Placeholder `[careers page URL]` | 1/1 | conditional | Unknown URLs as bracket placeholders |
| `**Image specs (attach to ...):**` with 1200×675 (16:9), PNG/JPG, under 5MB, content bullet(s) | 2/5: data (02) and announcement w/ people (05) | conditional | If data or visual asset suits, add image spec; PNG for charts, JPG for photos |
| "Real people, no stock imagery" | 1/1 photo | conditional | |
| `**Notes:**` final section | 4/5 (02 ends with image specs) | tendency | Usually end with Notes: strategy rationale + engagement tactic |
| Content-mix bucket: value 70%, interaction 20%, promo 10% | 3/5 named | tendency (framework implied observed) | Name the bucket in Notes |
| Engagement tactics: reply to comments in first 30 min; pin own reply | 2/5 | tendency | |
| Voice: first-person company "we/our"; "I/my" for personal admission | 4/5 first person | observed | Write as the account owner |
| Sentences short, fragments ("No new features.", "Not a bluff.") | 5/5 | observed | Short declaratives, fragments ok |
| Numbers as digits (12, 3,000, 41%, 22) | 5/5 | observed | Digits always |
| Emojis | 0/5 | absent, genre uses them | Never |
| Em dashes in post copy | 0/5 | absent | No em dashes in copy (minus sign "−33%" in spec only) |
| Exclamation marks | 0/5 | absent | Never |
| Markdown inside post copy | 0/5 | observed | Plain text inside code blocks |
| Metadata prose: plain declarative, no emojis | 5/5 | observed | |
| Banned words, account persona, posting schedule, platform beyond X | not observable | unknown | |
