---
name: target
description: Use when turning a brief (story, data point, opinion, tips, announcement) into a ready-to-post X (Twitter) post or thread with posting notes.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# X post writer

Input: a brief with facts, numbers and a takeaway. Output: a markdown package: Format line, the post(s) in code blocks with character counts, Hashtags line, optional Image specs, Notes.

## Pick a shape

| Brief type | Shape | Hook | Ending | Bucket |
|---|---|---|---|---|
| Story / failure | Thread, 4-6 posts: hook (what happened + numbers + who's at fault) -> what we did -> what broke -> lesson -> question | confession with numbers | question + #Tag | value |
| Data finding | Thread, 3-5 posts: stat hook -> how we found it -> what we changed + result -> advice + question | the stat itself | question + #Tag | value; add chart image |
| Contrarian opinion | Single post, 3 short lines separated by blank lines: claim / proof with numbers / question | the claim | question, no hashtag | interaction (20%) |
| List / tips | Thread, 1 + one post per tip: question-hook + "<N> moves that still work" -> one tactic per post (tactic sentence + why) -> last tactic + question | question + promise | question + #Tag | value (70%) |
| Announcement / promo | Single post, one paragraph: news + numbers + what's next; link goes in reply | the news | #Tag, no question | promo (10%) |

## Template

~~~~
**Format:** <Thread (N posts) | Single post | Single promotional post>[ + chart image | + link in reply]

[thread]
**Thread structure:**

**1/N** (<chars> chars)
```
1/N <text>
```
... (last one: (<chars> chars, including hashtag))

[single]
**Post text** (<chars> chars[, including hashtag])
```
<text>
```

[if link]
**Reply (<when to post it>; <why the link is not in the post: X cuts reach of link posts by roughly half>)** (<chars> chars; URL counts as 23)
```
<label>: [<link> URL]
```

**Hashtags:** <#Tag (final post only) | #Tag | None. <one-sentence reason>>


[if data or photo]
**Image specs (attach to <1/N | the post>):**
- 1200×675 (16:9), <PNG | JPG>, under 5MB
- <what the image shows>
- <optional second panel>

**Notes:** <2-3 short sentences, about 15-35 words: why the shape works, its bucket (value 70% / interaction 20% / promo 10%), one posting tactic>
~~~~

## Rules
1. Format line first; Hashtags line always [observed 5/5].
2. Character count on every post [observed 5/5]. Posts short: thread posts about 50-140 chars, single 80-200 [range 56-130].
3. At most 1 hashtag (a broad topic in CamelCase, or the place for a location announcement), at the end of the last post [capped max 1].
4. Never say "thread" in the hook [source note].
5. The Hashtags line is bare: `#Tag (final post only)` for threads, `#Tag` for a single post. Only "None." takes a reason sentence [observed 5/5].
6. Image format is PNG for a chart, JPG for a photo; write only "PNG" or "JPG" [conditional 2/2].
7. Thread posts: 1 to 2 short sentences each (3 only when the last post adds the question); hook post under about 100 chars [range 56-106].
8. Promotional single post: one paragraph, news + numbers + what's next, no question, no call to action beyond the reply link [conditional 1/1].
9. Image specs when the brief has data to chart or real people to photograph [conditional 2/5]. Photos show the real team, never stock images.
10. Notes usually close the package [tendency 4/5]; may be skipped on a data thread with a chart. A promotional post always gets Notes, naming the promo bucket and reminding to space promos between value posts [conditional 1/1].

## Defaults
- First person (we/our; I for confessions and opinions). Digits for numbers. No emoji, no exclamation marks, no em dashes [absent 0/5].
- Short sentences; fragments fine. At most 3 sentences per post.
- At most 2 "not X" contrasts and 1 rule-of-three triple per output [capped, unconfirmed].
- End a non-promo thread or post with a question that invites replies [conditional 4/5].

## Example (new topic)

~~~~
**Format:** Thread (4 posts)

**Thread structure:**

**1/4** (65 chars)
```
1/4 Our bakery threw out 30% of its bread every night for a year.
```

**2/4** (81 chars)
```
2/4 We baked the same amount every day, no matter the weather or the day of week.
```

**3/4** (86 chars)
```
3/4 We started logging sales by weekday and rain. Waste fell to 8% in the first month.
```

**4/4** (92 chars, including hashtag)
```
4/4 Count what sells before you change what you bake. What does your log say? #SmallBusiness
```

**Hashtags:** #SmallBusiness (final post only)

**Notes:** A loss with a hard number opens strong, and the fix is easy to copy. Value post (70% bucket). Reply to the first comments fast.
~~~~

## Unknowns
- Is the 70/20/10 value/interaction/promo mix a fixed rule of the source, or a calendar the user supplies?
- Is there a per-user voice file (tone, banned words, preferred hashtags)?
- Are AI-tell devices (reveal bridges, closing aphorisms, "not X, it's Y") banned? None seen except one "Not a bluff." fragment.
- Are there length tiers (long threads 8+ posts, long-form posts for premium accounts)?
- What happens with video, polls, quote posts, or replies to others? Not seen.
- Are no-emoji / no-em-dash habits from the source or the generator's settings?
