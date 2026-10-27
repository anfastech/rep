---
name: content-repurposing
description: Use when given one piece of source content (a post, story, insight, how-to, opinion, or announcement) and asked to repurpose it into a multi-platform pack for Twitter/X, LinkedIn, Instagram, Facebook, and TikTok, with posting and testing advice.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  rounds: 3 drafts, 2 train replays, 1 held-out replay
  method: reverse-engineer-skill v0.1
---

# Content Repurposing Pack

Input: one source piece (its facts, numbers, story, lessons) plus any author context
(role, company size, field). Output: one Markdown document with a source summary,
five platform versions, and analytics advice. Every number and fact must match the
source in every section. Add no new facts, numbers, names, or events. Reflection,
framing, and general reasoning in the author's voice are expected and fill out the length.

## Template

```
# Content Repurposing: <Source Headline in Title Case>

## Source Summary
**Original Format**: <type of source, e.g. "Data insight post", "How-to list", "Contrarian opinion post", "Company announcement", "Customer win story">
**Key Message**: <one sentence with the core facts and numbers, often "<what happened>; <what to do>">
**Target Audience**: <3 to 5 role groups, comma separated, last joined with "and">

---

## Twitter/X Thread (10 tweets)

**Tweet 1/10** (Hook)
<hook sentence>

<1 to 3 short punch or stat lines>

<promise line, e.g. "Here's what broke and how we fixed it."> 🧵

**Tweet 2/10**
<...>

... through **Tweet 10/10**

<closing recap>

<question to readers>

<reply CTA> 👇

#<CamelCase> #<CamelCase> #<CamelCase>

---

## LinkedIn Post

<one-line hook> <emoji>

<short paragraphs telling the story>

Key takeaways:
• <takeaway. one-line reason.>
• <...>
• <...>

<1 to 2 reflective paragraphs>

<question to readers>

**Hashtags**: #<CamelCase> x5

---

## Instagram Caption

<hook line> <1 to 2 emojis>

<1 to 2 short context lines>

<emoji> <list line>
<emoji> <list line>
<emoji> <list line>

<1 to 2 short paragraphs, may end with an emoji>

<save + comment/share/tag CTA> 👇

.
.
.
#<lowercase> x18 to 19 on one line

**Visual Suggestion**: <N>-slide carousel. Slide 1: <...>. Slide 2: <...>. ... For Stories: a <poll/quiz/slider/"This or That"/link> sticker <...>.

---

## Facebook Post

<opening line, often a question> <optional emoji>

<2 to 3 sentences with the core facts>

<one-line takeaway>

<question to readers>. <Tell us below / Share it in the comments> 👇

#<OneCamelCaseTag>

---

## TikTok Script (if applicable)

**Hook (0-3 sec)**: "<spoken hook>"
**Main Content (3-45 sec)**: "<spoken body, 50 to 80 words>"
**CTA (45-60 sec)**: "<follow/save/comment/tag ask>"

**On-Screen Text Ideas**:
- "<short overlay>"
- "<...>"
- "<...>"
- "<...>"

**Audio Suggestion**: Trending <style> sound <...>; <optional second clause>.

**Hashtags**: #FYP #<lowercase> #<lowercase> #<lowercase> #<lowercase>

---

## Analytics Recommendations
- Best posting times: LinkedIn, <...>. Twitter/X, <...>. Instagram, <...>. Facebook, <...>. TikTok, <...>.
- Engagement tactics: On LinkedIn, <...>. On Twitter/X, <...>. On Instagram, <...>. On Facebook, <...>.
- A/B testing ideas: Test <hook A> against <hook B>. Test <visual A> against <visual B>. Test <a third variable>.
```

## Rules

Each rule ends with its evidence tag.

### Whole document
1. Use the template's headers, labels, and order exactly, including "(10 tweets)", "(if applicable)", "(Hook)", and a `---` line between every section. [observed 5/5]
2. Always fill the TikTok section, even though its header says "(if applicable)". [observed 5/5]
3. Repeat the same facts and numbers across all platforms. Each platform retells the whole story at its own length; none says "see thread". [observed 5/5]
4. Never use em dashes or en dashes. Use commas, periods, colons, or semicolons. Write ranges with "to" ("8 to 10 AM", "Slides 2 to 5"). The only hyphenated ranges are the TikTok time labels. [absent 0/5, genre often uses dashes]
5. Numbers as digits ("3 screens", "22 meetings", "41%"), except a spelled number in a hook is fine for rhythm. [observed 5/5]
6. Plain words, short sentences (average about 10 to 14 words), contractions used. Short punchy fragments are welcome ("Not the oven. Not the flour."). [range observed 10.1 to 14.3 mean words, N=5]
7. Voice: first person. Use "I" when the author did it, "we" when the team or company did it. Speak to the reader as "you" in lessons and CTAs. [observed 5/5]
8. No exclamation marks, except in celebratory content (an announcement, or praise for a teammate's win). Even then, use about 3 to 4 in the whole pack, only in Instagram, Facebook, and TikTok (for example, a greeting line), and none in the thread, LinkedIn, or Analytics. [conditional 1/5 train: announcement, 4 marks total; held-out success story had 1 in Facebook]
9. Total length about 1,100 to 1,450 words. [range observed 1190 to 1337, N=5]
10. If author context is given (role, company size, field), mention it naturally once or twice (for example, a TikTok CTA "Follow for more <field> lessons") and include the author's home-field tag in the LinkedIn and Instagram hashtag sets even when the topic is adjacent. [observed 5/5]

### Title
10b. The H1 headline is the source's own headline in title case: capitalize main words, keep short articles and prepositions lowercase ("at", "to", "of", "in", "a", "for"). About 6 to 14 words. [observed 5/5, range 8 to 11]

### Source Summary
11. "Original Format" names the source type in a short phrase. "Key Message" is one sentence carrying the main numbers. "Target Audience" lists 3 to 5 role groups. [observed 5/5]

### Twitter/X thread
12. Exactly 10 tweets. Each tweet is 2 to 4 short paragraphs split by blank lines, usually 25 to 45 words (a one-beat tweet may be shorter), under 280 characters. Whole thread about 290 to 380 words. [range observed 14 to 43 words per tweet, mean 33; thread 286 to 377, N=5]
13. Tweet 1: a hook sentence (bold claim, confession, stat, or news), then 1 to 3 short stat or punch lines, then a promise line ending in 🧵. [observed 5/5]
14. Tweets 2 to 9 move one beat each: setup, what happened, the cost or result, why it matters, then the lessons. Write them as a person talking, not a slide deck. Vary openers: a plain statement, a rhetorical question ("Why does that matter?", "Sounds fine, right?"), an expectation line for stories ("I expected pushback."), or a framing line ending in a colon. Use colon framing lines in at most 2 to 3 tweets, only before a list or a reveal. Include 1 to 3 rhetorical questions across tweets 2 to 9. [observed 5/5; questions in thread 1 to 4 per output]
14b. For a story, data, or opinion source, include the assumption or expectation beat ("We assumed ...", "I thought ...", "I expected ...") before the reveal, and one tweet on the hidden or real cost. [tendency 3/5: story, data, opinion]
15. If the source has discrete lessons or tactics, give each its own tweet opening "<Noun> N:" plus a one-line title. Pick the noun the source uses: "Lesson", "Tactic", "Change", and so on, then 1 to 2 explaining lines. [conditional 2/5: lesson or tactic lists; held-out 2/2 also used it ("Lesson", "Change"), label widened after the held-out test]
16. If the source contains a repeatable method, tweet 9 is "Try it yourself:" or "How to try this yourself:" with 4 numbered steps and a one-line close. If it is a how-to list, tweet 9 is a recap with one emoji per tactic. [conditional 3/5: method or how-to]
17. Tweet 10: a one-line recap of the key numbers in fragments ("30 loaves. 4 loaves. One change."), a question to readers, a reply or share CTA ending in 👇, then exactly 3 CamelCase hashtags. No hashtags in tweets 1 to 9. [observed 5/5 for CTA and tags; recap of numbers 4/5]
18. Emojis in the thread: 🧵 in tweet 1, 👇 in tweet 10. Use emoji list bullets only in a how-to recap or an announcement's list of roles or news; other lists use "•" or numbers. At most one other accent emoji (📉, 🙌, a flag). [tendency 5/5; emoji lists 2/5: how-to, announcement]

### LinkedIn
19. First line is a one-line hook, usually ending in one emoji (👇, 📊, 🃏, a flag). [tendency 4/5]
20. Body paragraphs are mostly 2 to 4 sentences of plain storytelling, with 1 to 2 one-line pivots between them ("Then the numbers came in.", "That's where it went wrong."). Do not break every sentence onto its own line. Give the story its context: why the old way existed, what the author assumed, what changed. [observed 5/5]
21. Include "Key takeaways:" followed by 3 to 4 "•" bullets, each a short claim and one supporting sentence. For an announcement use "Why this matters:" with 3 "•" bullets ("For customers, ...", "For new hires, ..."). [conditional 4/5 takeaways, 1/5 announcement]
22. For a how-to list, present the steps first as keycap-emoji paragraphs (1️⃣ 2️⃣ 3️⃣ 4️⃣), then the takeaways bullets. [conditional 1/5: how-to]
23. After the bullets, 1 to 2 reflective paragraphs on what changed or what the author believes now. End with a question to readers. [observed 5/5]
24. Close with "**Hashtags**: " and exactly 5 CamelCase hashtags. [observed 5/5]
25. Length about 230 to 290 words including the hashtag line. Under 230 is too thin. [range observed 240 to 269, N=5]

### Instagram
26. First line: a punchy hook with 1 to 2 emojis (can be a number triplet like "12 sites. 1 day. 2 down."). [observed 5/5]
27. Include one block of 3 to 4 lines that each start with an emoji (stats or steps), no bullets. [observed 5/5]
28. 1 to 2 more short paragraphs; one may end with 💡, 🔑, 🙌 or similar. Then a CTA asking to save and to comment, share, or tag, ending in 👇. For an announcement or hiring, "link in bio" may be in the CTA. [observed 5/5]
28b. Instagram length about 190 to 230 words including the hashtag line and Visual Suggestion. Under 190 is too thin: add a 2 to 3 sentence reflective paragraph after the emoji list. [range observed 198 to 218, N=5]
29. Then three lines each holding only ".", then one line of 18 to 19 lowercase hashtags mixing topic, niche, and broad business tags. [observed 5/5, range 18 to 19]
30. After the hashtags: "**Visual Suggestion**: <3 to 6>-slide carousel." Describe each slide in one clause ("Slide 1: ...", "Slides 2 to 5: ..."), then "For Stories: a <sticker type> sticker ..." with a question. [observed 5/5, range 3 to 6 slides]

### Facebook
31. 50 to 80 words in 3 to 4 short paragraphs. Friendly and plain. Usually opens with a question ("Ever ...?", "What would happen if ...?"). [range observed 54 to 77; question opener tendency 3/5]
32. End with a question to readers plus "Tell us below", "Share it below" or "in the comments", usually with 👇. Then exactly 1 CamelCase hashtag. [observed 5/5; 👇 4/5]

### TikTok
33. Three bold timed lines, each a quoted spoken line: Hook (0-3 sec), Main Content (3-45 sec) of about 50 to 80 words in short spoken sentences, CTA (45-60 sec) asking to follow, save, comment, or tag. [observed 5/5, main range 55 to 70]
34. "**On-Screen Text Ideas**:" with 4 to 5 quoted overlay bullets that track the story's beats and numbers. [observed 5/5]
35. "**Audio Suggestion**: Trending <format> sound/voiceover ..." naming a mood shift at the reveal or lessons. [observed 5/5]
36. "**Hashtags**: #FYP" plus 4 lowercase tags. [observed 5/5]

### Analytics Recommendations
37. Exactly 3 bullets with the labels "Best posting times:", "Engagement tactics:", "A/B testing ideas:". [observed 5/5]
38. Posting times in the order LinkedIn, Twitter/X, Instagram, Facebook, TikTok. Defaults: LinkedIn, Tuesday to Thursday, 8 to 10 AM; Twitter/X, weekdays 9 AM to 12 PM; Instagram, weekdays 11 AM to 1 PM; Facebook, weekdays 1 to 3 PM; TikTok, 6 to 9 PM. Adjust or add a clause when the brief gives a reason (two time zones, quarter end, Monday calendar planning). [observed 5/5 order; defaults 3/5 verbatim, 2/5 adjusted]
39. Engagement tactics: one sentence per platform, "On LinkedIn, ... On Twitter/X, ... On Instagram, ... On Facebook, ...". Name concrete moves (reply in the first hour, pin the thread, poll or quiz sticker, quote-tweet a strong tweet later). An announcement may lead with an extra team move. [observed 5/5]
40. A/B testing ideas: 3 sentences, each "Test <A> against <B>." The first tests two hooks drawn from the pack, quoted. [observed 5/5]
41. The Analytics section has no emojis and no exclamation marks, even when quoting a hook. [absent 0/5]

## Example (partial, new topic)

Brief: a bakery owner moved to preorders only for weekend bread. Waste fell from 30 loaves a week to 4.

```
**Tweet 1/10** (Hook)
We used to throw away 30 loaves every weekend.

Now it's 4.

One change did it. Here's what we switched and why it worked. 🧵
```

```
**Facebook Post** body:
Ever baked more than you could sell?

We switched our weekend bread to preorders only. Waste dropped from 30 loaves a week to 4.

Bake to the order, not to the guess.

What's one change that cut waste in your business? Tell us below 👇

#SmallBusiness
```

## Unknowns

What the source skill may contain that the outputs cannot show. Do not act on these as rules.

- Whether the author persona (role, company, field) lives in the skill or in each brief. All 7 outputs may share one author.
- When the TikTok section is skipped or marked not applicable. All outputs fill it.
- Banned words or phrases. None can be inferred from 5 outputs.
- Behavior for sources that are very long, non-business, or have no numbers.
- Whether a different thread length is ever allowed. All show 10 tweets.
- Hashtag source lists (fixed bank or free choice).
