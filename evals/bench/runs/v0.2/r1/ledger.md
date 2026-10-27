# Ledger (train N=5: failure story, data insight, contrarian, how-to list, announcement)

| # | Feature | Seen | Class | Rule text |
|---|---|---|---|---|
| F1 | Deliverable order: header (2 lines), Hook, Alternative hooks, Post, hashtags, First comment, Edit note, Claims and facts, Open gaps, closing line | 5/5 | observed | Always output these blocks in this order |
| F2 | Header line 1: `<working title> · content/drafts/<run date>-<slug>.md` | 5/5 | observed | Title, middle dot, draft path with date-slug |
| F3 | Header line 2: `Single post · LinkedIn · <Name>'s profile (first person) · voice provisional` | 5/5 | observed (values brief-driven) | Format · platform · account (person) · voice status |
| F4 | "(first person, speaking for the company)" | 1/5, company announcement | conditional | If the post speaks for the company, say so in line 2 |
| F5 | `Hook (used below):` then hook, repeated verbatim as first paragraph of Post | 5/5 | observed | Hook block, reused verbatim |
| F6 | Hook 2 to 3 sentences, 17 to 29 words, 89 to 141 chars, the key number(s) inside it | 5/5 | range | 2 to 3 short sentences, under ~140 chars to clear "see more" |
| F7 | `Alternative hooks:` exactly 2, numbered `1.` `2.` | 5/5 | observed (count could be config) | Two alternatives, different angle each |
| F8 | `Post:` then body 163 to 180 words, 7 to 8 paragraphs, 1 to 3 sentences each | 5/5 | range | ~140 to 220 words, short paragraphs |
| F9 | Placeholder slots `[STORY NEEDED: ...]`, `[NAME: ...]`, `[PROOF NEEDED: ...]` instead of invented detail; 3 to 6 slots in body | 5/5 | observed (slot count range) | Never invent; leave typed slot with "e.g." hint |
| F10 | Body has 0 questions, 0 exclamation, 0 emoji, 0 dashes | 5/5 | default (P10/P11) | Defaults; dashes and AI tells explicitly checked in Edit note |
| F11 | Numbered list in body | 1/5, how-to list brief | conditional | Numbered list only for parallel items (Edit note says so) |
| F12 | Last paragraph is a reader action, "If you ..." 4/5; "Save this for ..." on list | 5/5 action; opener tendency 4/5 | observed + conditional | End on action matched to intent, not recap |
| F13 | Hashtags: one line after body, 2 to 3, lowercase topic tags, proper noun capitalised | 5/5 | range | 2 to 3 hashtags on own line |
| F14 | `First comment: none (no link in this post).` | 4/5; 5/5 when no link | conditional | Links go in first comment, never body |
| F15 | First comment holds link (as PROOF NEEDED slot if URL missing) | 1/5, brief has a link/CTA | conditional | |
| F16 | `Edit note` bullets: One argument, Fakes, Intent and CTA, Swap test, Skeptic, Readability, AI-tell check, Voice | One argument/Fakes/Intent/AI-tell/Voice 5/5; Swap 4/5; Readability 4/5; Skeptic 2/5 | observed + tendency | Checklist; skip a check only when it has nothing to say |
| F17 | Swap test absent on announcement | 1/5 | conditional (weak) | |
| F18 | Skeptic bullet present on lesson/opinion briefs (01, 03) | 2/5 | tendency | Include when a claim invites pushback |
| F19 | AI-tell check reports counts removed: colon reveal, rhetorical-question opener, "not X, it's Y", "Here's the kicker", invented feelings, hype phrases ("thrilled to announce", "exciting new chapter", "journey"), unsourced world facts; plus "No banned words. No dashes." | 5/5 | observed | Report "removed N <tell>" per tell; banned list exists |
| F20 | "not X, it's Y" kept at most once | 1/5 mention | capped max 1 | |
| F21 | Voice bullet: provisional when no voice card or past posts; offer "paste 5 to 10 of <Name>'s LinkedIn posts and I'll build her voice card" | 5/5 | observed (voice file, P4) | |
| F22 | `Claims and facts: <title>   (sign-off: <scope>)` then Kept, Softened, Cut, Sourced, Disclaimers added, Person yes needed | 5/5 | observed | Fixed 6-row claims ledger |
| F23 | World facts need a source opened this run; else cut and note how to restore | 1/5 triggered (04) | conditional | |
| F24 | Opinions or stances not in the brief are flagged for the person's yes | 2/5 (03, 05) | conditional | |
| F25 | `Open gaps`: first "PERSON YES NEEDED (<Name>)", then every slot in post order, plus alt-hook PROOF items | 5/5 | observed | |
| F26 | Closing line `Nothing is published. You edit and post. If you want the social pieces in a two-week posting calendar, ask for it next.` | 5/5 | observed fixed string | |
| F27 | Voice: first person "I" for own story, "we" for company; contractions used (8 to 18); plain, concrete; mean sentence 12 to 17 words | 5/5 | default | |
| F28 | Hook types: blunt outcome with numbers (01,02,03,05) or reader problem (04) | 5/5 | tendency | |
| F29 | Banned words list | "No banned words" 3/5 | unknown | List not visible |
| F30 | Other formats (thread, calendar, multi-platform "social pieces") | "Single post" label 5/5 | unknown (P3/P7) | Menu not observable |
