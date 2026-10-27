---
name: target
description: Use when writing a short first-person LinkedIn-style post from a brief (a story, result, experiment, playbook, or announcement) that ends with a comment-for-the-link lead magnet, a PS line, and a hook-formula tracking footer.
metadata:
  reconstructed-from: 7 outputs (5 train, 2 held out); rules 2, 8, 12 amended after the held-out test (amendments not re-tested)
  method: reverse-engineer-skill v0.1
---

# First-person lead-magnet post

Input: a brief with what the author did or learned, any numbers, the lesson,
and a free resource to offer. Output: one plain-text post plus a tracking footer.

## Template

Every line is its own block with one blank line between lines. Exceptions: the "→ " list is one tight block (no blank lines inside it), and the footer's "---" sits directly above the "Hook formula used" line.

```
I <did / do the thing>. <optional second sentence with the result or twist>
<optional: short twist line as its own block>
Here's <what happened | what we did | why I did it | the N-step playbook I use | where we are>:
<context line 1: the before-state, or the common belief>
<context line 2>
<BODY: story lines OR "→ " list OR "1/ " steps — see rules 6-8>
<reframe line 1: what it is NOT>
<reframe line 2: what it really is>
<optional punchline or directive line>
I <wrote up | put | turned this into> <the resource>.
Comment "<WORD>" and I'll send you the link.
PS - <sentence to "you" about the stakes>. <second sentence that sharpens it>.

---
Hook formula used: <Formula Name> — for A/B tracking. Strip before publishing.
```

## Rules

1. One sentence (occasionally two very short ones) per line, blank line between every line. [observed 5/5]
2. Line 1 usually starts with "I" and states what the author did or what changed for them (the action, not the final result), in plain past or present tense. If the brief credits someone else (a team member did the thing), open with that person instead ("A <role> on my team <did X>."). A second sentence on the same line, or a short second line, may give the surprising number or twist. [observed 5/5 train; held-out 1/2 opened with a credited team member, so: conditional]
3. If the brief has a headline number, put it in the hook. [tendency 3/5: the 2 without had no headline number]
4. Hook first line is short: about 6 to 17 words, including any second sentence on that line. A twist or detail may sit on its own second line. [range observed 8 to 16, N=5; second line 2/5]
5. Next comes a bridge line "Here's ...:" ending in a colon, matched to the post type: "Here's what happened:" (story), "Here's what we did:" (process), "Here's why I did it:" (experiment), "Here's the N-step playbook I use:" (playbook), "Here's where we are:" (announcement). [observed 5/5]
6. Then 2 short context lines: the before-state, or a common belief followed by a short correction. [observed 5/5]
7. If the brief is a story or experiment, tell the body as 6 to 10 one-sentence lines in order: action, what went wrong or what happened, the numbers. If it is a failure, the author owns the decision plainly. [conditional 2/5: story/experiment briefs]
8. If the brief is a set of steps taken or facts (process, results, announcement), use a list of 4 to 6 lines each starting "→ ", written as consecutive lines with NO blank lines between them and NO period at the end of single-phrase items. Process items are full "We <verb>..." or "I <verb>..." clauses; announcement items can be noun phrases with numbers. An item may carry a second short sentence ("<change>. <proof>."), in which case it keeps its periods. One item may be "No X. No Y. Just Z." (that one keeps its periods). [conditional 2/5: process/announcement briefs]
9. If the brief is a playbook of N tactics, write each as "1/ <Tactic as imperative>." on its own line, followed by one explanation line of 1 to 2 very short sentences (about 6 to 15 words total). [conditional 1/5: playbook brief]
10. After the body, a two-line reframe that names the real cause or meaning: first line says what the obvious cause or thing is not (or is "just"), second line says what it really is. [tendency 4/5]
11. Optionally one more punchline line: a two-sentence small-vs-big contrast, a "Don't X. Do Y." directive, a forward-looking line, or "No X. No Y. Just Z." [tendency 3/5 + 1/5]
12. Resource line: one sentence starting "I wrote up", "I wrote down", "I put", "I shared", or "I turned this into", naming a concrete free resource tied to the lesson (checklist, template, sheet, note, list). [observed 5/5]
13. CTA line exactly: `Comment "<WORD>" and I'll send you the link.` WORD is one random concrete noun in ALL CAPS that has nothing to do with the topic (a food, an animal, a household object). [observed 5/5]
14. Then `PS - ` (capital PS, no periods, space-hyphen-space) and two sentences addressed to "you": restate the stakes or set a small challenge. [observed 5/5]
15. Then a blank line, `---`, and on the very next line (no blank) exactly: `Hook formula used: <Formula Name> — for A/B tracking. Strip before publishing.` [observed 5/5]
16. Formula Name is a short Title Case label for the hook type used, often two labels joined with " / " or " + " (a hook type plus a modifier, e.g. a "results first" or "confession" style label plus a "proof", "reveal", "transformation" or "permission" style label). Pick the label that honestly describes the hook you wrote. If the hook is a contrarian "don't do X, do Y" hook, the body also carries a matching "Don't X. Do Y." line. [observed 7/7 format (5 train + 2 held-out, all 7 names distinct); library unknown]
17. No questions, no exclamation marks, no emojis, no hashtags, no em dashes in the post body (the footer's dash is fine). The "→ " arrow is the only symbol. [absent 0/5]
18. Voice: first person (I, we, our), plain short words, contractions, digits for numbers, average sentence about 6 to 11 words. Calm, matter-of-fact; no hype words. [observed 5/5; range]
19. Length: keep it tight, about 110 to 160 words before the footer and about 13 to 18 non-blank lines before the footer. Do not pad: go straight from the body (or list) to the reframe, with at most one extra line between. [range observed about 120 to 148 words before footer, 135 to 164 incl. footer, N=5]

## Example

(New topic, not from any source.)

```
I stopped sending our weekly status email. Nobody noticed for 6 weeks.

Here's why I did it:

The email took me 2 hours every Friday.

I assumed people read it.

So I just stopped sending it.

No warning. No replacement.

Week 1, no replies.

Week 3, still nothing.

Week 6, one person asked where it went.

They wanted one number from it.

The email wasn't useful.

The one number was.

Don't write the report. Find the number people actually use.

I wrote up the 3-line update I send now.

Comment "WALRUS" and I'll send you the link.

PS - Every team has one task like this. Stop it for a month and see who asks.

---
Hook formula used: Quiet Experiment + Contrarian Rule — for A/B tracking. Strip before publishing.
```

## Unknowns

- The full hook-formula library and how the skill picks one (only 5 names seen).
- How the CTA keyword is chosen (random list, or something else).
- Any banned word list, persona backstory, or audience definition.
- Behavior when the brief has no resource to offer (every output offered one).
- Whether a word or line limit is stated in the source.
- Platform target (looks like LinkedIn; never stated).
