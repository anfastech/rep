# Ledger (train N=5: 01 reel-story, 02 carousel-data, 03 image-experiment, 04 carousel-list, 05 photo-announcement)

## Packaging and skeleton

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Deliverable = fenced caption block, then (optional) alt-text line, then fenced status card | 5/5 | observed | Output exactly: caption in a ``` block, alt text line, ``` status card |
| Caption: every paragraph is one physical line, blank line between paragraphs | 5/5 | observed | One line per paragraph, blank line between |
| Last caption line = hashtags only, nothing after | 5/5 | observed | Hashtag line closes the caption |
| Hashtag count | 3 in all 5; card prints `hashtags:   3` | observed (count of source range unknown) | Exactly 3 hashtags; whether source allows 3-5 unknown |
| Hashtag form: lowercase, run-together, 1 niche + 1-2 broader | 5/5 | observed / default | lowercase, no camelCase |
| Hashtags anywhere else in caption | 0/5 | absent | none |
| Body paragraphs (excl. hashtag line) | 4 to 7 (01:5, 02:6, 03:6, 04:7, 05:4) | range | about 3 to 8 |
| Caption words (incl. hashtags) | 71 to 135 | range | roughly 60 to 160 |
| Caption characters | 426 to 811 | range | well under platform max; under ~900 |
| Line 1 length in chars | 75 to 111, card always "of 125" | observed (limit) + range | Line 1 must fit in 125 characters |
| Sentences per paragraph | max 3 (02 line 3, 04 items) | capped | at most 3 |
| Words per sentence | short; mean 9.8-19 incl. card | default | short plain sentences |

## Hook / job

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Card `job:` field with letter + explanation | 5/5 | observed | Always state the job |
| Job B "<format>, line one is the hook" | 4/4 non-reel (carousel x2, single image, single photo) | observed for still posts | Still posts: line one is the hook, job B |
| Job A "the reel carries the hook (<who> on camera, "<words>" in the first two seconds)"; caption line 1 = the ask | 1/5 (reel only) | unknown (seen once) | Unknown: does every reel get job A? What triggers A? |
| Hook carries a concrete number or count | 4/4 job-B hooks (41%, 22/4, "four levers", "15 more") + reel hook "3,000" | tendency (strong) | Usually put the most concrete number in the hook |
| Hook = 1-2 sentences | 5/5 | range | 1 to 2 sentences |
| Hook types | stat (02), confession/experiment (03), question+claim (04), announcement (05), CTA-first (01) | varies | No fixed hook type |

## Role skeleton (P14)

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Story shape: hook → context/problem → what we did → result → reader takeaway → ask → hashtags | 02, 03 fully; 01 same order after CTA line (no separate takeaway line, change stated as "Now every...") | menu entry (3/5) | Story/result template |
| List shape: hook → "Most ... advice assumes" context → numbered items "N. Imperative. explanation." → ask → hashtags | 04 only | unknown (seen once) | fold into general; numbered list allowed |
| Announcement shape: news hook → progress fact → who we are → ask merged with reader targeting ("If you've been looking for ...") | 05 only | unknown (seen once) | fold into general |
| Reader-takeaway line opening "If you..." / "Before you..." | 02, 03 (05 "If you've been looking" = ask line) | tendency 3/5 | Usually a second-person takeaway near the end |
| Context line opening "Most ..." (generalisation) | 03, 04 | tendency 2/5 | sometimes |

## Ask (CTA)

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Exactly one ask; card prints "ask: one, <ask>" | 5/5 | observed | One ask only |
| Ask kinds: comment keyword (01), save (02, 04), answer question in comments (03), link in bio (05) | varied | conditional on goal (save x2 for reference/how-to value) | Pick the ask from the goal |
| Ask position: own line just above hashtags | 02, 03, 04 | tendency 3/5 | Usually |
| Ask merged into last body line | 05 (link in bio) | seen once | — |
| Ask as line 1 | 01 (reel, job A) | seen once | Unknown |
| Comment-keyword ask: keyword in caps, "Comment WORD and I'll send you <thing>"; card adds "(say WORD out loud in the video too)" | 01 | seen once | Unknown |
| Save ask phrasing "Save this ..." + occasion | 02, 04 | conditional 2/2 save asks | "Save this for/before <moment>." |
| Links in caption | 0/5; card "first comment: none, no link" 4/5; 05 "none, the link lives in the bio, not the caption" | observed | No links in caption; point to bio |

## Search keywords

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| Two 2-word search phrases woven into caption, reported with line numbers | 5/5 | observed | Two plain-language search phrases |
| Line numbers count from caption line 1 including blank lines | 5/5 | observed | |
| One phrase in line 1 | 02, 03 | tendency 2/5 | |
| Phrase repeated twice | 02, 03 | tendency | |
| Phrases are plain descriptive nouns, not hashtags | 5/5 | observed | |

## Alt text

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| "Alt text (cover slide): ..." for carousels | 02, 04 | conditional 2/2 carousel | |
| "Alt text: ..." for single image/photo | 03, 05 | conditional 2/2 single | |
| No alt text for reel | 01 | seen once | Unknown |
| Alt text 1-2 plain descriptive sentences, describes what is shown (incl. numbers/text on slide) | 4/4 | observed | |

## Card

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| First line `CAPTION READY` | 5/5 | observed fixed | |
| Field order job, visible, ask, hashtags, search, first comment, linter | 5/5 | observed | |
| Values aligned at column 13 (except "first comment:") | 5/5 | observed | |
| `visible:    N of 125 characters used before the cut` where N = chars of caption line 1 | 5/5 (verified by count) | observed | |
| `linter:     READY, checked by hand against caption.py's rules` | 5/5 fixed | observed | implies a linter script exists; unknown rules |

## Voice and mechanics

| Feature | Seen | Class | Rule text |
|---|---|---|---|
| First-person company voice (we/our), I for the poster, you for reader | 5/5 | default | |
| Contractions | 5/5 (1-5) | default | |
| Emojis | 0/5 | absent | default none |
| Exclamation marks | 0/5 | absent | default none |
| Em/en dashes | 0/5 (card uses " - ") | absent | default; may be generator setting (P11) |
| Bold/markdown in caption | 0/5 | absent | (Instagram has no markdown) |
| "not X, it's Y" contrast | 01 ("held up. What failed was"), 02 ("weren't ... They were"), 04 ("not a bluff", "not discounts") | capped max 3 (04), others ≤1 | not banned; at most 1-2 |
| Rule-of-three triples | 0 clear in captions | absent | default avoid |
| Reveal bridges ("Here's the thing") | 0/5 | absent | Unknown if banned |
| Neat closing aphorism | 0/5 (captions end on ask + hashtags) | absent | Unknown if banned |
| Numbers as digits for stats | 5/5 (some small numbers spelled: Two, Nine, three, four) | default | |
| Jargon/hype words | 0/5 | absent | plain words |
