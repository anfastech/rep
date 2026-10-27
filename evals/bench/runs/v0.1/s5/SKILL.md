---
name: newsletter-issue-writer
description: Use when writing one newsletter issue (Substack-style) for a named author from an issue brief, in that author's voice, with subject line options, preview text, image suggestions, a short Notes teaser, and the voice guide used.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out). Rules tagged [held-out] were added after the held-out test and are not yet replay-tested.
  method: reverse-engineer-skill v0.1
---

# Newsletter Issue Writer

Input: an issue brief (topic, story or news, facts, numbers, lesson, any CTA
or link) plus the author's name and role, and optionally transcripts or past
issues. Output: one plain-text package with six parts in a fixed order.

## Step 1: Voice guide

Build a voice guide for the author before writing. If transcripts or past
issues are supplied, derive it from them. If only briefs are supplied, infer it
from the briefs and the author's role, and say so in the Sources line. If a
guide for this author already exists, keep its Core, Vocabulary, and
Structural patterns sections. Refresh Signature moves (the example quote, and
one move fitted to this issue) and the first two Things that would sound wrong
(fitted to this issue's risk, e.g. hype for news, oversharing for a personal
piece). [observed 7/7; refresh scope from held-out]

## Step 2: Write the package

Output exactly this skeleton. Lines in `code` style below are fixed strings.
Two blank lines before every `====` banner.

```
SUBJECT LINE (chosen)
<subject line>

Alternatives
1. <alternative subject>
2. <alternative subject>

PREVIEW TEXT
<preview text>


==================== ISSUE ====================

# <subject line, verbatim>

*<preview text, or its first one or two sentences>*

<intro: 2 to 4 short paragraphs>

[Subscribe button]

## <body section>

<body>

## <body section>
...

[Button: <label>]        (only if the brief has a link or CTA)

[Share button]

* * *

<one-sentence takeaway>      (how-to briefs: the recap section comes first, see rule 8)

## <optional "try it" section>

## Your turn

<question + reply ask + small promise>

<forward line>

<Author first name>


==================== IMAGE SUGGESTIONS ====================

1. Placement: cover image.
   Purpose: <verb phrase: set / show / make / give ...>.
   Description: <one or two sentences, what to show and its style>.
   Alt text: "<one sentence ending with a period.>"

2. Placement: inline, <position> "<H2 name>".
   Purpose: <...>.
   Description: <...>.
   Alt text: "<...>"


==================== NOTES TEASER ====================

<one paragraph>


==================== VOICE GUIDE USED ====================

VOICE GUIDE: <Author full name>
Created: <today, YYYY-MM-DD>
Sources used: <what was supplied. If briefs only: "issue briefs only. No transcripts or past issues were supplied, so validate these markers against <his/her/their> published issues.">

## Core voice characteristics
- Register: <register>. Sounds like <concrete comparison>, not <contrast>.
- Avg sentence length: <range> words, <note on fragments>.
- Humor: <type and target>.
- Confidence: <how assertive; when they hedge>.

## Vocabulary
- Uses: <domain nouns>, plain verbs (<5 verbs>)
- Avoids: <cliches, hype words, and banned punctuation such as exclamation marks and em dashes>
- Technical level: <what the reader is assumed to know>

## Structural patterns
- Opens with: <hook habit>
- Closes with: <closing habit>, signed "<first name>"
- Paragraphs: <range> sentences
- <when prose, when lists>

## Signature moves
- <move, with a short quote from THIS issue as the example>
- <move>
- <move>
- <move, e.g. where metaphors come from>

## Things that would sound wrong
- <framing> ("<example>"): <why it breaks the voice>
- <framing> ("<example>"): <why>
- <framing> ("<example>"): <why>
```

## Rules

Subject and preview
1. One chosen subject plus exactly two numbered alternatives. Across the three, cover different angles: a concrete scene or claim, a number or detail, and the lesson or a "why/how" framing. The alternatives take the angles the chosen one does not. [observed 5/5; angle split tendency]
2. Subject is plain and specific, about 5 to 10 words, no question marks or colons for effect. [range observed 6 to 9, N=5]
3. Preview text is 1 to 3 short sentences, about 10 to 18 words. It names the tension or payoff the subject does not. [range observed 11 to 15, N=5]

Issue structure
4. H1 repeats the chosen subject verbatim. The italic line under it is the preview text (or its first sentences). [observed 5/5]
5. Intro is 2 to 4 short paragraphs, about 60 to 110 words, ending before `[Subscribe button]`. It contains exactly one bolded key fact or claim. [range observed 64 to 97, N=5]
6. The first sentence is a specific moment, a number, or the claim stated flat. No warm-up, no "In this issue". Match the opener to the brief: [conditional]
   - failure or story brief: a timestamped scene ("At <time> on <day>, ...") or "Last <season>, ..." [01, 02]
   - opinion or experiment brief: name the opinion outright, then the test you ran [03]
   - how-to brief: a plain fact about the author's position, then "It doesn't." style reversal and "Here are the N ..." [04]
   - news brief: say it is news, then state it plainly in one bolded line [05]
   - personal reflection: the situation with one bolded fact, then flag that this issue is more personal than usual and name what it covers [06, held-out]
   - credit or case story about someone else's work: the result first (what it does, the number), then who built it [07, held-out]
7. Body has 3 to 7 H2 sections before `## Your turn`. H2s are short sentence-case phrases, usually "What ...", "Why ...", "How ...", or "The ...". No puns. [range observed 4 to 6, N=5]
8. Section order follows the brief type: [conditional]
   - story, data, or experiment: context or setup, what happened or what was found, the real cause or surprise, what changed, the result or reflection [01, 02, 03]
   - N parallel items (tactics, changes the author made, habits kept): one H2 per item, numbered "1. <item>", after one or two unnumbered setup sections [04; 06 held-out]
   - how-to with N tactics: one H2 per tactic numbered "1. <tactic as an imperative>". Then `[Share button]`, `* * *`, and a "## Putting it together" section: one lead line, the tactics as a short numbered checklist, one line on what it takes, and the takeaway as the section's last line. Use `* * *` only once. [04]
   - announcement: why (reasons as bold lead-in paragraphs, not a list), what it took (lessons as bold lead-in paragraphs), who or what now, the ask (e.g. hiring), then a `[Button: <label>]` line [05]
9. When the brief has a downside or mistake, give it its own section and own it in first person ("What I got wrong", "The real mistake"). [tendency 2/5]
10. Bold one key line per section, the line a skimmer needs. Lists may use bold lead-in titles ("**Pilot first.** Then ..."). Total about 5 to 12 bold spans. [observed 5/5; range 6 to 10]
11. Numbered lists only for steps or ranked items; bullets for examples, quotes, or options. Lists have 3 to 5 items. [observed 5/5]
12. End matter, in this order: optional `[Button: ...]`, `[Share button]`, `* * *`, then a one-sentence takeaway starting "The thing to remember:" (a close variant is fine). Bold the core of the takeaway when it is the issue's main rule. [observed 5/5; wording 4/5]
13. If the brief is the author's own experiment or analysis method and the reader can rerun it, add a short section after the takeaway ("## Try it yourself" / "## Run your own version"): one lead line, a 3-step numbered list, one closing line. Skip it for case stories, news, and reflections. [conditional 2/7: 02, 03; absent in 07 held-out]
14. `## Your turn`: one direct question to the reader, then "Hit reply" (or "Reply with ..."), then a small promise (you read every reply, or you will collect answers for a future issue). For an announcement, it may open with "Two asks this week." [observed 5/5]
15. Then one forward line: "If this was useful, forward it to <the reader's colleague who faces this next>." For a hiring brief, ask readers to forward to a fitting candidate instead, and fold it into the second ask. [observed 4/5 + variant]
16. Sign off with the author's first name alone on its own line. [observed 5/5]
17. Issue length about 550 to 700 words; aim near 620. Short news issues may run a little shorter. [range observed 553 to 663, N=5]

Voice and mechanics
18. First person ("I" for decisions and mistakes, "we" for the team). Turn to the reader as "you" in lessons, advice, and general claims ("Your deadline is ...", "You don't need ..."), about 10 to 30 times per package. Own mistakes in active voice. [observed 5/5; you/your range 10 to 29]
19. Short sentences and fragments. Paragraphs 1 to 3 sentences, rarely 4. [range]
20. Use contractions. [observed 5/5]
21. Never use emojis, hashtags, exclamation marks, or em dashes, en dashes, or double hyphens. [absent 0/5]
22. Concrete numbers stated before the lesson. Plain verbs. Metaphors from the author's own field. [observed 5/5]
23. No inspirational framing or hype ("thrilled to share", "failure is a gift"). [observed 5/5]

Image suggestions
24. Usually two; give only the cover image when the issue has nothing worth a diagram or chart (a personal reflection). [two: 6/7; one: 06 held-out] #1 is always the cover image. #2 is inline, tied to a named H2; position is one of: start of, end of, or after that section. Each has Placement, Purpose, Description, Alt text, indented 3 spaces. Purpose is a short lowercase verb phrase ending in a period. Description starts lowercase ("a clean chart ..."), one or two sentences, about 15 to 35 words. Alt text is one plain sentence in double quotes, with the period inside. Whole block about 85 to 130 words. [observed 5/5; range 89 to 127]
25. Descriptions are simple and flat: a clean chart or diagram for data, a minimal object scene for a mood, no faces of strangers. For news about real people, ask for a real photo, not stock. [observed 5/5; real-photo conditional 1/5]

Notes teaser
26. One paragraph, about 35 to 55 words, aim near 45, first person, standing alone: the core story or claim, its key number, and the lesson. May end with a question to readers. [range observed 39 to 51, N=7; question tendency 2/7]

Voice guide
27. Print the full guide used, in the fixed headings shown. Four bullets in Core, three in Vocabulary, four in Structural patterns, four Signature moves, three Things that would sound wrong (each "<framing> (\"<example>\"): <why>"). Keep it compact: each bullet one line of about 5 to 20 words, the "why" a short clause ("would sound like X instead of Y", "breaks her habit of Z"). Whole guide about 230 to 300 words. [observed 5/5; range 266 to 268]
28. The issue must obey the guide's hard limits (the Avoids list, the sign-off, paragraph length). Signature moves are habits, not a checklist: an issue with no mistake in the brief need not show the ownership move. [observed 5/5]

## Example (new topic, partial)

Brief: a bakery owner switched flour suppliers to save money and lost a week of bread quality.

```
SUBJECT LINE (chosen)
The cheaper flour cost us a week of bread

Alternatives
1. 14% savings, 300 loaves we couldn't sell
2. Why I test suppliers on a Tuesday now

PREVIEW TEXT
The price was right. The protein content wasn't. Here's the test we run first.
```

Notes teaser: "We switched flour suppliers to save 14% and spent a week selling flat loaves. Same recipe, same ovens, different protein. Now every new supplier gets one slow Tuesday batch before they get our Saturday order."

## Unknowns

- Banned words beyond what the voice guide's Avoids line shows.
- How the voice guide changes when transcripts or past issues are supplied.
- Whether the source sets hard word limits for the issue, subject, or teaser.
- Behavior for brief types not seen (interview, roundup of links, sponsor section).
- Whether "Notes teaser" targets a specific platform feature and its length limit.
- Whether 2 alternatives is fixed. What decides 1 vs 2 images (seen once, on a personal piece).
- Whether "Your turn" ever carries more than one question, or the subscribe/share placeholders move for other platforms.
