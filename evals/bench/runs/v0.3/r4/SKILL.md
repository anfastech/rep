---
name: target
description: Use when writing a short first-person LinkedIn-style post that ends by offering a resource in exchange for a comment keyword, with a hook-formula tracking footer.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# Lead-magnet post writer (target)

Input: a brief (what the author did, found or announced; facts and numbers; the takeaway; a resource they can share). Output: one plain-text social post with a comment-keyword CTA, then a tracking footer naming the hook formula.

## Step 1: pick a hook formula

Name it in the footer. Names are Title Case and usually join two ideas with " / " or " + ". Seen:
- Confession / Gap Reveal: a mistake you made and what it exposed.
- Results-First / Before-After Transformation: lead with the result number.
- A contrarian "stop doing X, do Y" formula: a contrarian move you tested. (Its exact name is withheld by the leak check; name it in the same style.)
- Effort Proof + Free Resource: a skill you use, packaged as steps.
- Breaking News + Speed Flex: a fresh milestone or announcement.
Other formulas likely exist. If none fits, name one in the same style.

## Step 2: pick the body shape

| Shape | Trigger | Bridge line | Body |
|---|---|---|---|
| Story | something happened: a mistake, a bold experiment | "Here's what happened:" or "Here's why I did it:" | 6 to 10 short chronological lines, one beat each; usually a "So I ..." decision line |
| Arrow list | a process already done, results, or announcement facts | "Here's what we did:" or "Here's where we are:" | 1 to 2 context lines, then 4 to 6 "→ " lines |
| Playbook | how-to, tactics | "Here's the N-step playbook I use:" | 2 context lines (a "Most people think ..." line, then the correction), then N steps |

## Template

I <did / found / launched ...> <number or concrete fact>.

[Optional, about 2 posts in 5: one short second line that lands the surprising result or the key detail on its own, e.g. a result number or a place.]

Here's <bridge>:

<1 to 2 context lines; often starts "Most ...">

<body per shape>

<reframe line 1: vary the form. "X isn't/wasn't the (real) problem." | "X is just ..." | "Most X don't ...">

<reframe line 2: the real cause or point. "Y is/was." | "Y is what makes it ..." | "They just ... because ...">

[Optional punchline: one aphorism, or "Don't X. Do Y.", or one "No X. No Y. Just Z." line]

I <wrote up | put ... into | turned this into> <resource>.

Comment "<KEYWORD>" and I'll send you the link.

PS - <2 sentences to the reader>

---
Hook formula used: <Formula Name> — for A/B tracking. Strip before publishing.

## Rules

1. Line 1 begins "I", first person, states what you did or found, usually with a number. [observed 5/5]
2. The "Here's ...:" bridge comes right after the hook (line 2, or 3 if there is a second hook line), worded by shape. [observed 5/5; conditional by type]
3. Every line is one or two sentences, with a blank line between lines. Exception: arrow lines and nothing else sit on consecutive lines with no blank line between them. [observed 5/5]
4. Arrow lines start "→ " and are short fragments or sentences without a closing period. [observed 2/2]
5. Playbook steps: "1/ <imperative step>." on its own line, blank line, then a 1 to 2 sentence explanation line. Put the step count in the bridge. [observed 1/1]
6. A two-line reframe comes after the body and before the resource line. Vary its form; the "X wasn't the problem. Y was." form appears in only about 2 of 5 posts. [observed 5/5; form tendency 2/5]
7. Resource line, then exactly: Comment "<KEYWORD>" and I'll send you the link. [observed 5/5]
8. KEYWORD is one ALL-CAPS everyday concrete noun unrelated to the topic (food, animal, object). [observed 5/5]
9. Then "PS - " (space, hyphen, space) and 2 sentences to the reader: a blunt observation about their situation, or a split between two kinds of readers. Not a how-to tip. [observed 5/5]
10. Blank line, "---", then the footer line verbatim with the formula name. [observed 5/5]
11. At most one "No X. No Y. Just Z." line; use it in about half of posts at most. [capped max 1; 2/5]

## Defaults

- About 135 to 170 words counting everything, footer included; 16 to 20 non-blank lines. [range 135-164, 17-19, N=5]
- Short sentences, about 6 to 10 words on average; plain words; contractions; digits for numbers. [5/5]
- No questions, exclamation marks, emojis, hashtags, bold or headers, and no em dashes in the post body. [absent 0/5]

## Example (new topic)

I cut our restaurant menu from 40 dishes to 12.

Here's what happened:

Our kitchen was always behind on Friday nights.

We blamed the cooks. We hired two more.

It got worse.

So I pulled six months of orders.

28 dishes sold fewer than 5 plates a week.

We dropped all 28. Prep time fell by half.

The cooks were never the problem.

The menu was.

I wrote up the sales sheet we used to pick the 12.

Comment "LADDER" and I'll send you the link.

PS - Every dish on your menu costs you prep, stock and space. Most of them aren't paying rent.

---
Hook formula used: Mistake Reveal + Hidden Cost — for A/B tracking. Strip before publishing.

## Unknowns

Questions the outputs cannot answer. Do not act on these as rules.

- Must the hook always start with "I"? The held-out set has a third-person opener ("A junior analyst on my team ..."). See report.md, Untested changes.
- What is the full hook formula library, and how is a formula chosen (by goal, by post type, rotated for A/B tests)?
- Is the style fixed, or set by a per-user voice file (tone, CTA wording, keyword style, banned words)?
- Is the resource + comment-keyword CTA always required, or skipped when there is no resource?
- Are there length tiers (short/standard/long)? All outputs sit in one band of about 135 to 165 words.
- Are em dashes, questions, emojis and hashtags banned, or just absent? These may come from the generator's own settings.
- Rules for content the sample does not cover: links, images, tagging people, hashtags, multi-post threads.
- How is the deliverable handed over: one draft, or several variants per formula for the A/B test?
- Is the keyword meant to be random, or chosen from a list?
