---
name: linkedin-post-draft
description: Use when asked to write a single LinkedIn post for a named person's profile from a brief (story, data point, opinion, how-to, or announcement), producing a draft with hooks, an edit note, a claims check and open gaps.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.1
---

# LinkedIn Post Draft (ghostwritten, fact-safe)

Input: a brief naming the author (person, role, company), what happened or what they think, any numbers, the intent (lesson, data insight, opinion, how-to, announcement), and any link. Output: one plain-text draft package in the exact layout below. Nothing is posted.

## Template

Blank lines exactly as shown. Text in `<>` is a placeholder. Everything else is verbatim.

```
<Title> · content/drafts/<YYYY-MM-DD>-<slug>.md
Single post · LinkedIn · <Name>'s profile (first person<, speaking for the company>) · voice provisional

Hook (used below):
<hook>

Alternative hooks:
1. <alt hook>
2. <alt hook>

Post:

<hook, repeated word for word>

<block>

<block>
...
<close: one reader action>

#<tag> #<tag> <#tag>

First comment: <none (no link in this post). | <label>: <URL or [PROOF NEEDED: ...]>>

Edit note
- One argument: <the single argument, one sentence; "Every paragraph serves it." optional>
- Fakes: <what is the author's own from the brief; what was left as slots; any added line flagged for the author's yes>
- Skeptic: <only if there is an obvious objection; say whether the post answers it>
- Intent and CTA: <intent> post; <what the close asks and why it fits>
- Swap test: <passes / weak, and which specifics make it the author's>
- Readability: <where the key facts land, e.g. inside the first ~140 characters, before "see more"; paragraph shape; ends on the action>
- AI-tell check: removed <n> <tell> ("<quote>"), <n> <tell> ("<quote>"). No banned words. No dashes.
- Voice: provisional. No voice card or past posts for <First name>. Offer: paste 5 to 10 of <their> LinkedIn posts and I'll build <their> voice card.

Claims and facts: <Title>   (sign-off: <scope>)
- Kept: <fact>; <fact>; <fact>. <One attribution sentence.>
- Softened: <phrase and why, or none>
- Cut: <phrase, why, how to restore, or none>
- Sourced: <source, or "none needed; no world facts.">
- Disclaimers added: none.
- Person yes needed: <Name>.

Open gaps
- PERSON YES NEEDED (<Name>)
- <every [STORY NEEDED: ...], [NAME: ...], [PROOF NEEDED: ...] slot, in the order it appears>

Nothing is published. You edit and post. If you want the social pieces in a two-week posting calendar, ask for it next.
```

## Rules

Evidence tags: [observed N/N], [conditional k/N: brief property], [tendency k/N], [range observed a to b, N=n], [absent 0/N].

### Header
1. Line 1: a short title, then ` · `, then the draft path `content/drafts/<run date>-<kebab slug>.md`. The title is 3 to 6 words, no verb phrase padding. When the brief has data numbers (counts, percentages, results), lead with them ("<number> <thing>, <number> <result>"); a how-to, lesson or announcement may instead name the lesson or topic plainly. [observed 5/5; range observed 4 to 6 words, N=5; number-led 2/5]
2. Line 2 is the format line. Add ", speaking for the company" inside the parentheses when the post announces company news. [observed 5/5; conditional 1/5: company announcement]
3. Write "voice provisional" when no voice card or past posts were given. [observed 5/5; behaviour with a voice card is unknown]

### Hooks
4. The hook is 2 or 3 short sentences, about 15 to 35 words. It lands the brief's key number(s) or the core claim inside the first ~140 characters. Plain statement of what happened or what the author holds; no question, no colon reveal. [observed 5/5; range observed 17 to 29 words, N=5]
5. Hook types: the result or the failure stated flat ("We did X. Y happened."), or the reader's problem plus a promise (name the hard situation, then promise the list and its count) for how-to posts. [observed 5/5]
6. Exactly 2 alternative hooks, each 1 or 2 sentences, about 12 to 25 words, each a different angle: lead with the consequence number, the author owning the call, the contrarian claim, or one concrete item from the list. Use only facts in the brief. If an alt hook adds anything not in the brief, flag it in Claims (Cut) and Open gaps as [PROOF NEEDED]. [observed 5/5; range 14 to 23 words]

### Post body
7. The body opens with the hook word for word. [observed 5/5]
8. Body length about 130 to 220 words in 6 to 10 blocks, each 1 to 3 sentences, one blank line between. Mix short and longer lines: most sentences 6 to 20 words, plus at least one longer, flowing sentence of 20 to 30 words that walks through a cause or a process. Do not chop every thought into fragments. The hook and slot text count toward the body length. [range observed 163 to 180 words, 7 to 8 blocks, N=5]
9. Never invent detail the brief does not give: reasons, feelings, what broke, names, examples, outcomes. Put a bracket slot where that detail belongs: `[STORY NEEDED: <what is needed, in <Name>'s words>, e.g. <hint>]` for story, `[NAME: <the specific name, rule or fact>]` for a specific item, `[PROOF NEEDED: <what to confirm>]` for a URL or unverified claim. A slot may sit alone as a block or end a sentence. Expect 3 to 7 slots. Every added sentence that states a fact, an outcome, or a stance the brief did not give must be a slot or be flagged in Fakes. [observed 5/5; range 3 to 6]
10. Any intent may add one or two short lines of plain reasoning that follow from the brief (why a move works, why a habit forms). If the line reads as the author's stance, flag it in Fakes and Softened for the author to keep or cut. [observed flagged 2/5; unflagged general reasoning 3/5]
11. Structure by intent:
    - Lesson or failure: what happened, the author owns the call, slot for why and what broke, the cost restated in human terms, the lesson stated in one plain sentence, why it works, what changes next. [conditional 1/5]
    - Data insight: the number, restate it in plain terms (a fraction or "out of" phrasing), what was done, the result, what the author takes from it. [conditional 1/5]
    - Opinion: the view stated as the author's own, a one-line reason, the evidence, a short concession to the other side, the point. [conditional 1/5]
    - How-to: a numbered list of the parallel moves, each as `N. <Move as a short imperative>.` then the explanation on the next line, no blank line inside an item. Then one line on why they work, then a story slot. Use a numbered list only for parallel items. [conditional 1/5]
    - Announcement: what is new and the numbers in the first two sentences, why it matters, slots for why and who, what the author's own role is, then the ask. Company = "we"; the author's own role = "I". [conditional 1/5]
12. The close is one reader action, not a recap. Default form: "If you're/your <situation>, <do this>." A how-to list closes "Save this for your next <occasion>." A hiring post closes with where to apply and an offer to message directly. [observed 5/5 action close; "If" form 4/5]
13. Then 2 or 3 hashtags on one line: lowercase, single words (a proper noun keeps its capital). Usually one is the author's own field (for example their department or industry). [observed 5/5; range 2 to 3; field tag 5/5]
14. Links never go in the body. If there is a link, `First comment: <label>: <URL>`; if the URL is not given, use `[PROOF NEEDED: <what URL>]` there. Otherwise `First comment: none (no link in this post).` [conditional 1/5 link; 4/5 none]

### Mechanics
15. No emojis, no exclamation marks, no em dashes, en dashes, or double hyphens. [absent 0/5 each]
16. Use contractions (I'm, we're, didn't, that's). [observed 5/5, 8 to 18 per output]
17. Write the brief's data as numerals, even at the start of a sentence. Small counts used as plain words in prose ("four moves", "Two sites", "Three screens") may be spelled out. The Edit note and Claims use numerals. [tendency: numerals 5/5 for data; spelled small counts 3/5]
18. First person. "I" for the author's own calls and views, "we/our" for the team or company. [observed 5/5]
19. Plain words, short sentences, no hype: no "thrilled to announce", "exciting new chapter", "journey", "Here's the kicker", rhetorical-question openers, colon reveals ("The result? 4.", "The lesson is plain: ..."), and at most one "not X, it's Y" shape. Do not state world facts (market behaviour, statistics) without a source opened in this run. [observed: these are named as removed in 5/5 AI-tell bullets]

### Edit note
20. The Edit note is terse: each bullet 1 to 3 short sentences, about 160 to 200 words for the whole note. Refer to the author by first name here and in the body slots. Bullets in this order, each starting with its label: One argument, Fakes, Intent and CTA, Swap test, Readability, AI-tell check, Voice. One argument, Fakes, Intent and CTA, AI-tell check and Voice always appear. [observed 5/5 for those five]
21. Add "Skeptic" when the post has an obvious objection; say how the author's own number answers it, or that the answer is not in yet and which slot holds it. Place it after Fakes or after Swap test. [conditional 2/5: lesson and opinion posts]
22. Swap test: "passes" when the post holds the author's own numbers or story (name them); "weak until the story slot is filled" when the advice is general. Omit it for an announcement (including a hiring announcement). [conditional 4/5]
23. Readability: say where the key numbers land (inside the first ~100 or ~140 characters, before "see more"), note list use if any, and "Ends on the action." Usually present. [tendency 4/5]
24. AI-tell check: draft once, then cut the tells listed in rule 19 and any opinion or world fact the brief did not give. Name 2 or 3 things you removed, each as `<count> <tell> ("<quoted phrase>")`, then "No banned words." and/or "No dashes." [observed 5/5]
25. Voice bullet always ends with the offer to build a voice card from 5 to 10 past posts. [observed 5/5]

### Claims and facts
26. Header: `Claims and facts: <Title>` then three spaces, then `(sign-off: <scope>)`. Scope is "scoped sign-off this run, from the brief" when the post uses the author's or the company's own facts (events, numbers, announcements); "product facts only; no brand claims in this post" when the post has no company facts (pure advice). [observed 5/5; conditional 4/5 vs 1/5]
27. Six bullets in fixed order: Kept, Softened, Cut, Sourced, Disclaimers added, Person yes needed. Use "none" or "none needed; no world facts." when empty. A fact the brief gives but marks as not public goes under Softened or Cut with a note that it is held back until the author confirms. Derived numbers (18 from 22 minus 4, a restated percentage) are noted as arithmetic. Anything cut says how to restore it. Kept lists the facts separated by semicolons, then one closing attribution ("All are <first name>'s own account from the brief." or "as <first name>'s advice"), not a tag after every item. The whole Claims section is about 80 to 115 words. [observed 5/5]

### Open gaps and close
28. Open gaps: first `PERSON YES NEEDED (<Name>)` with the full name; optionally add ": the post is in <their> voice and tells <their> story." Do not list added lines here; they live in Fakes. Then one bullet per slot, shortened: body slots in order, then the first-comment slot, then any alt-hook [PROOF NEEDED]. [observed 5/5]
29. The last line is always: "Nothing is published. You edit and post. If you want the social pieces in a two-week posting calendar, ask for it next." [observed 5/5, fixed string]

## Example (new topic)

```
Missed appointments down by half · content/drafts/2026-03-04-reminder-texts-no-shows.md
Single post · LinkedIn · Dana Okafor's profile (first person) · voice provisional

Hook (used below):
Our dental clinic lost 30 appointments a week to no-shows. We added one text the day before, and that number fell to 14.

Alternative hooks:
1. 14 no-shows a week, down from 30. The fix was a single reminder text.
2. I ignored our no-show numbers for two years. One text the day before cut them in half.

Post:

Our dental clinic lost 30 appointments a week to no-shows. We added one text the day before, and that number fell to 14.

[STORY NEEDED: what a no-show cost the clinic, in Dana's words]

The text is short. It names the time, the dentist and a way to move the slot. [NAME: the exact wording Dana's team uses]

What surprised me is how many people weren't skipping. They'd forgotten. A reminder gave them a way to tell us early.

[STORY NEEDED: what the front desk does with the freed slots]

If your diary has gaps you can't explain, send one reminder the day before and count for a month.

#healthcare #operations
...
```

## Unknowns

The outputs cannot show these. Do not act on them as rules.

- The banned word list behind "No banned words."
- The full AI-tell list beyond the tells named above.
- How the output changes when a voice card or past posts exist (the "voice provisional" line and Voice bullet likely change).
- Other sign-off scopes, and when "Disclaimers added" is not "none" (health, finance, legal claims?).
- Formats other than "Single post · LinkedIn" (threads, carousels, other platforms) and what the two-week calendar step produces.
- Whether the draft file at content/drafts/ is actually written, and where the voice card and brand facts live.
- Whether the title must be a headline number or just follows the brief.
- Intents beyond the five above (personal reflection, praise of a team member) and their closes; a held-out reflection post closed with a question inviting replies.
- Consent handling when another person appears in the story (a held-out output added a second PERSON YES NEEDED line for them).
- The full set of sign-off scopes (a held-out personal story used a third variant).
