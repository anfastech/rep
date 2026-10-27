---
name: instagram-caption
description: Use when writing a paste-ready Instagram caption for a business account (carousel, single image, photo, reel) from a brief, with alt text and a status card.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out)
  method: reverse-engineer-skill v0.3
---

# Instagram caption

Input: a brief with the story or facts, the media type (carousel, single image/photo, reel), the goal, the audience. Output: a caption block, an alt-text line for still images, and a status card.

## Template

````
```
<line 1: the hook, fits in 125 characters>

<context: how it was before / what most people assume>

<what we did or what happened>

<result, short, with the number>

<reader takeaway: "If you ..." / "Before you ...">

<the one ask>

#tag1 #tag2 #tag3
```

Alt text<" (cover slide)" for carousels>: <what the image shows>

```
CAPTION READY
job:        B - <carousel cover | single image | single photo>, line one is the hook
visible:    <N> of 125 characters used before the cut
ask:        one, <the ask in a few words>
hashtags:   3
search:     "<phrase 1>" in line <x>, "<phrase 2>" in line <y>
first comment: none, no link
linter:     READY, checked by hand against caption.py's rules
```
````

Middle blocks are jobs, not a fixed count: drop or split them to fit the brief (4 to 7 body lines seen). A list post replaces "what we did / result" with numbered items; an announcement goes news → progress → who we are → ask.

## Rules

1. Output exactly three parts in order: caption in a ``` block, the alt-text line outside any block, the status card in a ``` block. [observed 5/5]
2. Every paragraph is one physical line; one blank line between paragraphs. [observed 5/5]
3. Line 1 must fit in 125 characters (the cut before "more"). On still posts line 1 is the hook. [observed 5/5; hook 4/4 still posts]
4. Exactly one ask, and the card says `ask:        one, ...`. [observed 5/5]
5. The caption ends with a line of exactly 3 lowercase run-together hashtags. Nothing after them, no hashtags elsewhere. [observed 5/5]
6. No links in the caption. A link goes in the bio, and the caption tells readers to find it there; the card then says `first comment: none, the link lives in the bio, not the caption`, otherwise `first comment: none, no link`. [observed 5/5; bio variant 1/1]
7. Work in two 2-word search phrases (plain words someone would type into search, not hashtags) and report them in the card by line number. Line numbers count from caption line 1 including blank lines, so text lines are 1, 3, 5... A phrase used twice: `in line <x> and line <y>`. [observed 5/5]
8. `visible:` = exact character count of caption line 1. [observed 5/5]
9. Alt text: carousel → `Alt text (cover slide): ...` describing the cover (its chart, title or listed items); single image or photo → `Alt text: ...`. One or two plain sentences. [conditional 2/2 carousel, 2/2 single image]
10. The card is verbatim in its fixed parts: `CAPTION READY`, field order, values aligned at column 13, the `hashtags:` and `linter:` lines. [observed 5/5]
11. Pick the ask from the goal [tendency, kinds seen]:
    - reference value (how-to, list, data) → `Save this <for/before the moment it will be useful>.` [2/2 save asks]
    - discussion → a direct question to the reader, then "Tell me in the comments."
    - hiring / sign-up → point to the link in the bio; this can close the last body line, addressed to the people the post is looking for
    - lead magnet → `Comment <KEYWORD> and I'll send you <thing>.`
12. At most 3 sentences per paragraph. [capped max 3]

## Defaults

1. Hook uses most of the 125 characters, often two sentences: the result or number, then the twist or context. Put the most concrete number from the brief in it. [range 75 to 111 chars, 4/5 at 105+]
2. The ask sits on its own line just above the hashtags, straight after the last body line, with no recap or summary line between them. [tendency 3/5]
3. Takeaway line speaks to the reader, opening "If you ..." or "Before you ...", never with a label like "Takeaway:". [tendency 2/5 + 1 merged with ask]
4. A context line often opens with a generalisation ("Most ..."). [tendency 2/5]
5. Numbered items: `<n>. <Imperative instruction>. <1 to 2 sentences on why it works.>` one per line. [seen 1/5]
6. Hashtags: one niche tag plus broader ones for the field. [5/5]
7. Voice: we/our for the company, I for the poster, you for the reader. Contractions. Short plain sentences. [5/5]
8. No emojis, no exclamation marks, no em or en dashes. [absent 0/5]
9. Digits for stats and counts. [5/5]
10. Caption roughly 70 to 140 words. [range 71 to 135]

## Example (new topic)

```
Our clinic cut missed appointments from 1 in 5 to 1 in 20. The fix was a text message two days out.

Most clinics send one reminder the morning of the visit. By then patients who can't make it have no time to cancel.

We moved our appointment reminder to 48 hours before and added a one-tap reschedule reply.

Missed appointments fell to 5% in three months.

If your schedule has gaps you can't fill, look at when the reminder lands before you look at who skipped.

Save this for your next front desk meeting.

#dentalpractice #patientexperience #healthcare
```

Alt text (cover slide): Line chart of missed appointments per month falling from 20% to 5%.

```
CAPTION READY
job:        B - carousel cover, line one is the hook
visible:    99 of 125 characters used before the cut
ask:        one, save the post
hashtags:   3
search:     "appointment reminder" in line 5, "missed appointments" in line 1 and line 7
first comment: none, no link
linter:     READY, checked by hand against caption.py's rules
```

## Unknowns

- Reels: one reel seen. Its card read `job:        A - the reel carries the hook (<who> on camera, "<hook words>" in the first two seconds)`, the caption opened with the ask, it had no alt text, and the keyword ask note told the presenter to speak the keyword in the video as well. Is that the rule for every reel, or only when the video opens on the hook? Are there other job letters?
- Are 3 hashtags fixed, or one value of a range (3 to 5)?
- What does caption.py check? Is there a banned-word list?
- When is a first comment used (the field always said "none")?
- Is the voice fixed or supplied by a per-brand voice file? Are length tiers available?
- Are "not X, it's Y" contrasts limited? Seen up to 3 in one caption, so not banned.
- Dash, emoji and exclamation absence may come from the generator's settings rather than the skill.
