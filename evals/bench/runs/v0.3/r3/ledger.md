# Ledger (train N=5: story, data, experiment/opinion, list, announcement)

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| L1 | Output = post body, then a blank line, then a short note to the requester about choices made | 5/5 | observed | Always end with a 2-3 sentence note to the user (not part of the post) |
| L2 | Note opens with "I" + past-tense choice verb (kept/opened/used/avoided) and names one specific craft choice and why | 5/5 | observed | Note names the main choice and its reason |
| L3 | Note ends with an offer/invitation to adjust ("I can make it...", "Tell me if...", "can be sharper if you want", "Swap in...") | 4/5 explicit offer (04 has no offer) | tendency | Usually end the note with one adjustment offer |
| L4 | Note length | 24-37 words, 2-3 sentences, N=5 | range | About 20-45 words |
| L5 | Note flags invented/missing facts (01 "left out any detail... not in the brief", 05 "Swap in something from the actual office") | 2/5 | conditional (brief thin on a detail) | If brief lacks a detail, don't invent; say so in note |
| L6 | Hook = first paragraph is a plain factual statement of what happened/situation, no question, no stat-bomb, no "thrilled" | 5/5 | observed | Open with the plain fact/situation in first person |
| L7 | First paragraph length | 19-32 words, 1-3 sentences | range | ~15-35 words |
| L8 | Very short second paragraph as a turn ("They weren't." "Four came back.") | 2/5 (02, 03: brief with a surprising result) | conditional | If the brief has a surprising result, may land it in a 1-line paragraph |
| L9 | Big number held back to give weight (02 note) | 1/5 explicit | tendency | Let the key number land after setup |
| L10 | Middle: explanation of why/what was learned, longest paragraph (52-72 words) for stories | 3/5 (01,02,03) | tendency | Middle paragraph explains the cause |
| L11 | Numbered list shape "1." with blank lines, each item: bold-free imperative + one-line reason; intro line "Here's what has worked for us anyway:" | 1/5, only list brief | conditional (brief is N separate tips) | Use numbered list when brief is discrete moves; each item imperative + 1-3 sentence reason |
| L12 | Announcement: lead with plain fact, one real observation, CTA with how to apply, thanks line | 1/5 (05) | conditional | Announcement shape |
| L13 | Closing body line: short takeaway / plain advice ("If your... try...") / reframe | 5/5 last paragraph 13-23 words | observed (presence) / range | End body with a short plain takeaway or practical next step |
| L14 | Body paragraph count | 4-7 | range | ~4-8 paragraphs |
| L15 | Body words | 126-199 (whole file 163-227) | range | ~110-230 words |
| L16 | Sentence length | mean 10-14, max 21-26 | range | Plain mid-length sentences, under ~28 words |
| L17 | Questions | 0/5 | absent | Default: no questions (incl. no hook questions, no engagement questions) |
| L18 | Exclamation marks | 0/5 | absent | Default: none |
| L19 | Emojis | 0/5 | absent (genre usually has some) | Default: none — strong evidence |
| L20 | Hashtags | 0/5 | absent (genre usually has some) | Default: none — strong evidence |
| L21 | Em/en dashes | 0/5 | absent | Default: none (may be generator setting, P11) |
| L22 | Markdown bold/headers | 0/5 | absent | Plain text only |
| L23 | Contractions | 2-6 per post | tendency | Conversational, contractions fine |
| L24 | Person: I/we first person; "you" used for advice | 5/5 | observed (voice) | First person; author's own voice |
| L25 | Tone: calm, modest, self-critical where relevant, no hype; hedges ("I don't think...", "I'm not suggesting...") | 5/5 | default | Calm, measured |
| L26 | Numerals for numbers ("12", "3,000", "41%", "22"), word at sentence start ("Four", "Nine") | 5/5 | default | Digits, spelled out at sentence start |
| L27 | Explicit engagement-bait CTA ("Agree?", "Thoughts?") | 0/5 | absent | Default: none |
| L28 | Contrast devices ("X looks slower. It is much faster...", "None of this makes you bigger. It does make you harder...", "before lunch, not the next day") | 0-2 per post | capped | At most 2 (cap unconfirmed); never "not X, it's Y" reveal form literally (0/5) |
| L29 | Rule-of-three triples | 0-1 loose | capped | At most 1 |
| L30 | Reveal bridges ("Here's the thing", "The kicker") | 0/5 ("Here's what has worked" in list intro only) | absent | Likely banned (Unknown) |
| L31 | Closing aphorism | 2/5 mild (03 "Most of my calendar was habit.", 04) | tendency | Allowed but plain |
| L32 | Hiring/action CTA only when brief has an ask | 1/5 (05) conditional; 02 has advice CTA | conditional | CTA only if brief has an ask |
| L33 | Platform | not stated; shape = LinkedIn post | unknown | |

## Pattern walk (references/patterns.md)

| P | Evidence | Outcome |
|---|---|---|
| P1 AI-tell bans | "not X, it's Y": 0/5 literal; "no X, no Y": 0/5; triples: ~0-1; "Here's the thing": 0/5; engagement bait 0/5; commenting on post itself: 0/5 in body (the note does it, outside the post) | Unknown: likely banned list. Contrasts exist (L28) so not a full ban on contrast |
| P2 caps | contrast <=2, triples <=1, sentences/para up to 6 (01 p3) | Capped rows L28-29 |
| P3 template menu | story/data/experiment share a shape; list (04) and announcement (05) differ | Menu: narrative / numbered tips / announcement |
| P4 voice file | 05 note "Swap in something from the actual office" and 01 "more or less hard on myself" imply user adjusts; no evidence of file | Unknown |
| P5 platform limits | body 126-199 words, first para 19-32 words (~100-190 chars) — fits a "see more" cut around 2-3 lines | Unknown: char limit |
| P6 optional sections | note present 5/5; thanks line 1/5 | Note is observed; ask if ever skipped |
| P7 length tiers | one band | Unknown |
| P8 content-triggered | no links, code, tables | Unknown |
| P9 packaging | the note to the user IS packaging retained in capture; no code block, no alternatives | Observed note; Unknown whether alternatives/hooks are offered elsewhere |
| P10 defaults vs bans | no emoji/hashtags in LinkedIn genre = strong | Defaults, flagged strong |
| P11 generator env | zero dashes, zero questions could be global setting | Unknown |
| P12 voice protection | 01 note: "left out any detail... that wasn't in the brief" → no-invention rule is explicit | Conditional rule (L5); ask about over-polish |
