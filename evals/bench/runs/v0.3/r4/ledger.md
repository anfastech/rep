# Ledger (train N=5: 01 story-failure, 02 data/process, 03 experiment/contrarian, 04 how-to list, 05 announcement)

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| F1 | Line 1 is a first-person claim starting with "I" (action or result, usually with a number) | 5/5 | observed | Open with an "I ..." sentence stating what you did or found |
| F2 | Hook length (line 1) | 8 to 16 words, N=5 | range | About 8 to 18 words |
| F3 | Optional 1-line hook follow-up before the bridge (the reveal/second fact) | 2/5 (03, 05) | tendency | Optionally a short second hook line (a surprising number or the key detail) |
| F4 | Bridge line "Here's <what happened / what we did / why I did it / the N-step playbook I use / where we are>:" ending in colon | 5/5 | observed | Always a "Here's ...:" bridge line right after the hook |
| F5 | Bridge wording matches type: story "what happened", process "what we did", experiment "why I did it", list "the N-step playbook I use", announcement "where we are" | 5/5 one per type | conditional | Pick bridge wording by brief type |
| F6 | Context/setup 1-2 lines after bridge; "Most ..." common-belief opener | 3/5 (02,03,04) | tendency | Usually set up with what most people think/do |
| F7 | Body shape: story = short single-sentence lines chronological (01,03); results/process/announcement = "→ " arrow list 4-6 items (02,05); how-to = numbered "1/" steps, each a bold-less title line + 1-2 sentence explanation line (04) | 5/5 split by type | conditional (menu) | Template menu by brief type |
| F8 | Arrow list length | 4 to 6 items, N=2 | range | About 3 to 7 arrows |
| F9 | Numbered steps | 4 steps, N=1; count announced in bridge | range | 3 to 5 steps; count in bridge |
| F10 | Lesson/reframe: two short lines, contrast "X isn't/wasn't the problem. Y is/was." or "X is just ... The Y is what ..." | 5/5 (some form) | observed | One reframe/lesson pair before the CTA |
| F11 | Aphoristic closer / directive line before CTA ("One site down is a bad day...", "Don't trim... Cancel them all...") | 2/5 (01, 03) | tendency | Optional |
| F12 | "No X. No Y. Just Z." triple | 2/5 (02 inside list, 04), max 1 | capped | At most 1 per post |
| F13 | Resource line: "I <wrote up / put ... into / turned this into> <the resource>." | 5/5 | observed | Always offer a resource tied to the post |
| F14 | CTA fixed string: Comment "<WORD>" and I'll send you the link. | 5/5 | observed (fixed string) | Verbatim |
| F15 | Keyword is one ALL-CAPS common noun unrelated to topic (PRETZEL, OTTER, TEAPOT, MANGO, CACTUS) | 5/5 | observed | Random unrelated concrete noun, all caps, in double quotes |
| F16 | "PS - " line (hyphen with spaces), 2 sentences, speaks to reader (you) with a nudge or reframe; 05 splits readers into two groups | 5/5 | observed | Always end post with "PS - ..." 2 sentences |
| F17 | Footer: "---" then "Hook formula used: <Formula name> — for A/B tracking. Strip before publishing." | 5/5 | observed (fixed string) | Verbatim, formula name from a library |
| F18 | Formula names: "Confession / Gap Reveal", "Results-First / Before-After Transformation", "DON'T Do X — Do Y Instead", "Effort Proof + Free Resource", "Breaking News + Speed Flex" — Title Case, joined with " / " or " + " | 5 distinct names | unknown (library) | Name the formula; full library unknown |
| F19 | One sentence or two per line; blank line between every line | 5/5 | observed (format) | Every line its own paragraph |
| F20 | Total words | 135 to 164 incl. footer, N=5 | range | About 120 to 190 words |
| F21 | Nonblank lines | 17 to 19, N=5 | range | About 15 to 22 |
| F22 | Sentence length mean 6 to 10 words | N=5 | range | Short sentences |
| F23 | Questions, exclamations, emojis, hashtags | 0/5 each | absent | Default none |
| F24 | Contractions | 4 to 7 per post | tendency | Use contractions |
| F25 | Em dashes in post body | 0/5 (only in footer) | absent | Default none in body (P11: may be generator setting) |
| F26 | Markdown bold/headers | 0/5 | absent | Plain text |
| F27 | Voice: first person I/we, past tense for story, present for lesson; plain words, grade-school level | 5/5 | default | |
| F28 | Numbers as digits (12, 3,000, 41%, 22, 4/) | 5/5 | default | Digits for numbers |
| F29 | "So I ..." decision line in story | 2/5 (01, 03 — both story/experiment) | conditional | In stories, a "So I ..." pivot line |
| F30 | Owning-the-mistake line ("my call") | 1/5, failure brief | conditional (weak) | If failure, own it |

## Pattern walk (references/patterns.md)
- P1 AI-tells: contrast reveal 5/5 (F10), triple "No X. No Y. Just Z." 2/5, reveal bridge "Here's ...:" 5/5, aphorism 2/5, engagement bait (comment keyword) 5/5. The source does NOT ban these; they are part of its form. Commenting on post itself: 0/5.
- P2 caps: triple max 1; arrow list max 1 per post; contrast pairs 1-3 per post (uncapped evidence). Sentences per line max 2 (except PS, 2).
- P3 menu: yes — 3 body shapes (story, arrow, numbered) plus hook-formula library.
- P4 voice file: unknown — ask.
- P5 platform units: LinkedIn-like; "see more" cut likely around line 2-3 (bridge sits at line 2-3). Characters unmeasured as rule. Unknown.
- P6 optional sections: resource/CTA might be optional if no resource exists; 5/5 present → "usually"? Fixed string 5/5 so kept observed, with question.
- P7 length tiers: all in one band; unknown.
- P8 content-triggered: no links, code, tables seen. Unknown.
- P9 packaging: footer meta-line is packaging ("Strip before publishing") — captured. Other packaging unknown.
- P10 defaults: no hashtags/emojis are defaults.
- P11 generator: body em-dash absence and "PS -" hyphen may come from settings.
- P12 voice protection: unknown.
