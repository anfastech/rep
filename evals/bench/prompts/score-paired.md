You are scoring a skill-reconstruction benchmark. Be strict and literal. Two recovered skills, X and Y, were made blind from the same outputs. Score both against the same ground truth in one pass so the grading is consistent.

Inputs:
- REAL skill (ground truth): every file in {BENCH}/hidden/{ID}/
- RECOVERED X: {BENCH}/blind/{ID}/X.md
- RECOVERED Y: {BENCH}/blind/{ID}/Y.md
- The 7 outputs the real skill produced: {BENCH}/outputs/{ID}/ (train/, heldout/)
Do not read anything else.

Steps:
1. From the REAL skill, list every atomic rule that shapes the final deliverable. Skip pure workflow (asking the user questions, publishing, API setup, scraping, telemetry). Each: id (G1...), short text, type (structure, length, voice, mechanics, word-list, persona, conditional, format, cta, other).
2. For each G rule mark visible: yes | partly | no (would a careful reader of the 7 outputs see evidence of it?). Then mark X and Y each: full | partial | unknown-listed | none.
3. List every rule-like item in X and in Y (R1...), with section: rules | defaults | template | unknowns-skip. Template skeletons count once as one item. Items under Unknowns are not scored here (section unknowns-skip, label n/a). Label each other item: grounded (matches a G rule) | incidental (true of these outputs, not required by the real skill) | wrong (contradicts the real skill).
4. Write {BENCH}/scores/{ID}-paired.json:
   {"id","g_rules":[{"id","text","type","visible","X","Y"}],
    "X":{"r_items":[{"id","text","section","label"}]}, "Y":{...}}
   Do not compute summary numbers; a script will.
5. Reply with one line: done, G count, X item count, Y item count.
