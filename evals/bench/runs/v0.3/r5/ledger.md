# Ledger (train N=5: 01 story, 02 data, 03 opinion, 04 list, 05 announcement)

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| F1 | First line `**Format:** <Thread (N posts) / Single post / Single promotional post> [+ chart image / + link in reply]` | 5/5 | observed | Always open with the Format line; append "+ <asset>" when an image or link-reply is part of the package |
| F2 | Thread vs single chosen by brief type: story/data/list -> thread (01,02,04); opinion/announcement -> single (03,05) | 5/5 split clean | conditional | Thread when the brief has steps, a sequence or several points; single post for one claim or an announcement |
| F3 | Thread block: `**Thread structure:**`, then per post `**i/N** (X chars[, including hashtag])` + code block whose text starts `i/N ` | 3/3 threads | observed | Fixed thread layout, numbered i/N inside the post text too |
| F4 | Single block: `**Post text** (X chars[, including hashtag])` + code block | 2/2 singles | observed | Fixed single layout |
| F5 | Char count per post in parentheses, "including hashtag" when hashtag present | 5/5 | observed | Always state char count; note hashtag inclusion |
| F6 | Thread length | 4 to 5 posts, N=3 | range | About 3 to 7 posts; one idea per post |
| F7 | Chars per thread post | 56 to 106, N=14 | range | Short posts, well under 280; aim roughly 50 to 140 |
| F8 | Single post chars | 124 to 130, N=2 | range | Roughly 80 to 200 chars |
| F9 | `**Hashtags:**` line after the post(s) | 5/5 | observed | Always include; value is the tag + "(final post only)" for threads, or "None. <reason>" |
| F10 | Hashtag count | 0 to 1 per output; on last post only | capped | At most 1 hashtag, at the very end of the final post (cap unconfirmed) |
| F11 | No hashtag when contrarian opinion (03) | 1/5 | conditional (weak) | Opinion/interaction post may drop the hashtag "to keep the take clean" |
| F12 | Hashtag is broad topic area in CamelCase (#Operations, #CustomerSupport, #Procurement) or place (#Lisbon) | 4/4 | tendency | Use one broad topic tag |
| F13 | Closing question in last post | 4/5 (not 05 promo) | conditional | Non-promo: end the final post with a reply-inviting question |
| F14 | Hook: first post states the core claim/stat/result directly; 3 to 8 words first line; never says "thread" | 5/5 | observed + note in 01 | Hook leads with the punchline (number, claim, or question + promise); never use the word "thread" or 🧵 |
| F15 | Hook type by brief: confession+numbers (01), stat (02), contrarian claim (03), question + "N moves" promise (04), news statement (05) | — | menu | Hook matches type |
| F16 | Link handling: link put in an immediate reply, not main post; reply block `**Reply (...reason...)** (X chars; URL counts as 23)` | 1/1 link brief | conditional | If a link: put it in a reply, explain link penalty (~50%), count URL as 23 |
| F17 | `**Image specs (attach to <post>):**` bullets: `1200×675 (16:9), <PNG/JPG>, under 5MB` + description (+ optional second panel) | 2/5 (02 data, 05 announcement) | conditional | If the brief has data or a photo-worthy announcement, add image specs; PNG for charts, JPG for photos; "Real people, no stock imagery" |
| F18 | `**Notes:**` final block | 4/5 (missing in 02) | tendency | Usually end with Notes: strategy/why + posting tip |
| F19 | 70/20/10 bucket label (value 70%, interaction 20%, promo 10%) | 3/5 (03,04,05) | tendency | Notes usually names the content bucket |
| F20 | Engagement tips in notes (reply within 30 min, pin own reply, space promo between value posts) | 3/5 | tendency | Notes may add one posting tactic |
| F21 | Voice: first-person company "we/our", "I" for opinion/confession; short declarative sentences, fragments ok | 5/5 | default | Plain, short, first person |
| F22 | Numbers as digits (12, 3,000, 41%, 22, 4) | 5/5 | default | Use digits |
| F23 | Emojis, exclamation marks, em dashes | 0/5 | absent | Default none |
| F24 | Markdown only in the wrapper (bold labels); post text plain inside code blocks | 5/5 | observed | Posts in code blocks, plain text |
| F25 | "not X" contrast / negation fragments | 0,1,0,2,0 | capped | At most 2 per output (cap unconfirmed) |
| F26 | Rule-of-three triples | 1 (01), else 0 | capped | At most 1 |
| F27 | Total words of whole deliverable | 72 to 146 | range | ~60 to 180 words |
| F28 | Platform | URL=23 chars, link penalty, 280-like limits | inferred | X (Twitter) |
| F29 | Banned words, voice file, tone settings | not observable | unknown | Unknowns |

## Pattern walk (references/patterns.md)
- P1 AI-tells: "not X, it's Y": 04 has "Not a bluff. A real quote..." (1) - so not strictly banned. Triples: 1 (01). Aphorisms: 0. "Here's the thing": 0. Self-reference ("this thread"): 0, and 01 Notes says hook avoids "thread" -> likely rule. Engagement questions are used deliberately (4/5).
- P2 caps: hashtags max 1; contrast max 2; triples max 1; sentences per post max 3 (01-3/5: 2; 04-5/5: 3).
- P3 menu: yes, five shapes by type (story, data, opinion, list, promo).
- P4 voice file: unknown.
- P5 native units: chars per post given by the source itself; URL=23.
- P6 optional: Notes 4/5, Image specs 2/5, Reply 1/5.
- P7 length tiers: thread 4-5 vs single; unknown if long threads exist.
- P8 content-triggered: link -> reply; data -> chart. Video, polls, quote-posts unseen.
- P9 packaging: wrapper with Format/Hashtags/Notes is the packaging; kept.
- P10 no emoji -> default.
- P11 no em dashes may be generator env.
- P12 n/a.
