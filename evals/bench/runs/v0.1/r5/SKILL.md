---
name: x-post-packager
description: Use when turning a brief (story, opinion, tips, data, announcement) into a ready-to-publish X (Twitter) post or thread package with character counts, hashtag, image specs and posting notes.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  final-draft: drafts/v3.md (leak-scrubbed)
  method: reverse-engineer-skill v0.1
---

# X post packager

Input: a brief with a topic, facts, numbers, a takeaway, and optional link or visual asset. Output: a markdown posting package for X: format line, post copy in code blocks with exact character counts, hashtag line, optional reply, optional image specs, notes.

## Template

Thread:

~~~~
**Format:** Thread (N posts)[ + chart image]

**Thread structure:**

**1/N** (X chars)
```
1/N <hook>
```

**2/N** (X chars)
```
2/N <body>
```

...

**N/N** (X chars, including hashtag)
```
N/N <takeaway>. <open question>? #Hashtag
```

**Hashtags:** #Hashtag (final post only)

[**Image specs (attach to 1/N):**
- <1200×675, 16:9>, <PNG|JPG>, <under 5MB>
- <what the image shows>]

**Notes:** <why the post is shaped this way>. <engagement tactic>.
~~~~

Single post:

~~~~
**Format:** <Single post | Single promotional post + link in reply>

**Post text** (X chars[, including hashtag])
```
<copy>
```

[**Reply (<when to post it; note that the link lives here because X cuts reach roughly in half for posts with links>)** (X chars; URL counts as 23)
```
<label>: [<link> URL]
```]

**Hashtags:** <#Hashtag | None. <reason>>

[**Image specs (attach to main post):** ...]

**Notes:** ...
~~~~

## Rules

1. Start with `**Format:** <format>`. [observed 5/5]
2. Choose a thread when the brief has a sequence: a story with cause and lesson, a list of tips, a data walk-through. Choose a single post for one opinion or one announcement. [conditional 5/5: 01,02,04 thread; 03,05 single]
3. Threads: 4 to 5 posts usually; 3 to 7 allowed. Header `**Thread structure:**`; each post gets `**k/N** (X chars)` then a code block whose text starts with `k/N `. [range 4 to 5, N=3; observed 3/3]
4. Keep every post short: about 50 to 130 characters, far under 280. One idea per post. [range 56 to 107 chars, N=14]
5. Give exact character counts, including the `k/N ` prefix. Add ", including hashtag" when the post holds the hashtag. URLs count as 23. [observed 5/5]
6. Hook (first post or first line): a blunt result, stat, or contrarian claim, with a number where the brief has one. First sentence 3 to 10 words. No setup, no "thread", no 🧵. When the brief's core is a stat, the hook's first token is the stat itself ("41% of ..."). [observed 5/5; stat-first conditional 1/1 data brief]
7. For a list brief, the hook names the count ("4 moves that still work") and each later post is one standalone tactic: instruction sentence, then a short justification. [conditional 1/5: list brief 04]
8. For a story brief: stake/result, what we did, what broke, the lesson. Put the full damage in post 1. If the brief admits fault, do it once, in two or three words at the end of the hook ("My fault."); do not repeat it later. [conditional 1/5: 01]
9. Final post (or end of single post): the takeaway as a direct instruction, then an open question to the reader, then the hashtag. In a story thread the lesson gets its own post and the last post is the question alone ("Have you ever ...? How did it go?"). Promotional posts skip the question. [conditional 4/5: all non-promo; story split 1/1]
10. Voice: first person as the account owner, "we/our" for the company, "I/my" for personal acts. Short declaratives and fragments ("No new features." "Not a bluff."). Use contractions (shouldn't, couldn't, can't, what's). [observed 5/5; contractions 4/5]
11. Numbers as digits, including percentages and counts ("9 hires so far." may open a sentence). Spell out "one" as a plain word ("pilot at one site") and, sometimes, a small number opening the hook ("Two of our 12..."). Keep the brief's own phrasing for fractions ("dropped by a third"). [observed 5/5; spelled-out tendency 1/5]
12. No emojis, no exclamation marks, no em dashes, no markdown inside post copy. [absent 0/5]
13. Hashtags: at most one, CamelCase, broad topic or place (#Operations, #CustomerSupport, #Lisbon), at the very end of the final post. Always write a `**Hashtags:**` line: "#Tag (final post only)" for threads; "None." plus a one-line reason when you skip it (e.g. a clean contrarian take). [observed 5/5; none 1/5 opinion post]
14. Links never go in the main post. Put them in a reply section whose label says to post it right after the main post and why (roughly half the reach lost to the link penalty); use a bracket placeholder when the URL is unknown. [conditional 1/1 link briefs]
15. Add `**Image specs (attach to ...):**` when the brief has data that charts well (PNG bar chart, highlight the key number) or a real-world visual (JPG photo, "Real people, no stock imagery."). Always 1200×675 (16:9), under 5MB. Format line adds " + chart image" for charts. [conditional 2/5: data 02, announcement 05]
16. End with `**Notes:**` (2 to 3 sentences): name the content-mix bucket (value post 70% bucket, interaction post 20% bucket, promo post 10% bucket), why the shape works, and one engagement tactic (answer the first replies inside half an hour; pin your own reply; space promos between value posts). Notes may be dropped when image specs already close the package. [tendency 4/5; bucket named 3/5]
17. Single opinion post: claim, proof, question as three lines separated by blank lines. Single promotional post: one paragraph of short factual sentences (what, count so far, what's next), no line breaks, no CTA sentence or hype ("Come join us", "just"); the reply line is the only CTA. Hashtag at the end. [conditional 2/2: opinion 03, promo 05]
18. Image specs bullets: size/format line, a line describing the image with the key number highlighted, and optionally a line starting "Optional" for a second panel (e.g. before/after). [conditional 2/5]

## Example

**Format:** Thread (4 posts)

**Thread structure:**

**1/4** (63 chars)
```
1/4 We cut our cloud bill 38% without touching a single server.
```

**2/4** (81 chars)
```
2/4 We tagged every resource by team. Half the spend had no owner anyone knew of.
```

**3/4** (71 chars)
```
3/4 We deleted the orphans. Nothing broke. Not one ticket in six weeks.
```

**4/4** (93 chars, including hashtag)
```
4/4 Tag before you optimize. What share of your bill could you name an owner for? #CloudCosts
```

**Hashtags:** #CloudCosts (final post only)

**Notes:** Value post, the 70% bucket. Answer the first replies inside half an hour.

## Unknowns

- Banned words or phrases.
- Persona/backstory of the account and its audience.
- The exact content-mix framework beyond the 70/20/10 bucket names.
- Behavior for other platforms (LinkedIn, Threads) or very long briefs.
- Whether hashtags are ever more than one, and the full rule for skipping them.
- Posting-time or scheduling advice.
