"""Score posts against the hidden skill's 12 rules.

Usage: python3 check_rules.py <post.txt>[:failure] ...
Append ':failure' when the brief was a failure/mistake topic (R9 must fire).
"""
import re
import sys

BANNED = ["leverage", "synergy", "game-changer", "unlock", "journey"]
PS = "P.S. I write about this every Tuesday in The Margin."
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def words(s):
    return len(s.split())


def check(text, failure):
    lines = text.strip("\n").split("\n")
    body = [l for l in lines if l.strip()]
    lessons = [l for l in body if re.match(r"^[123]/ ", l)]
    sentences = [s for s in re.split(r"[.?!]\s", " ".join(body)) if s.strip()]
    cost = [l for l in body if l.startswith("Cost of this lesson:")]
    r = {}
    r["R1 hook"] = words(lines[0]) <= 12 and lines[0].endswith(".") and "?" not in lines[0]
    r["R2 blank"] = len(lines) > 1 and lines[1].strip() == ""
    r["R3 Last"] = len(lines) > 2 and lines[2].startswith("Last ")
    r["R4 3 lessons"] = (
        [l[:2] for l in lessons] == ["1/", "2/", "3/"] and all(words(l) <= 21 for l in lessons)
    )
    r["R5 no we/our"] = not re.search(r"\b(we|our)\b", text, re.I)
    r["R6 sent<=15"] = all(words(s) <= 15 for s in sentences if not s.startswith(("1/", "2/", "3/")))
    r["R7 no emoji/#/md"] = not (EMOJI.search(text) or "#" in text or "**" in text)
    r["R8 banned"] = not any(b in text.lower() for b in BANNED)
    r["R9 cost cond"] = (len(cost) == 1) == failure
    r["R10 What's?"] = len(body) > 1 and body[-2].startswith("What's") and body[-2].endswith("?")
    r["R11 P.S."] = body[-1].strip() == PS
    r["R12 80-120w"] = 80 <= words(text) <= 120
    return r


if __name__ == "__main__":
    total = passed = 0
    for arg in sys.argv[1:]:
        path, _, flag = arg.partition(":")
        res = check(open(path).read(), flag == "failure")
        fails = [k for k, v in res.items() if not v]
        total += len(res)
        passed += len(res) - len(fails)
        print(f"{path.split('/')[-1]}: {len(res) - len(fails)}/12  fails={fails}")
    print(f"TOTAL {passed}/{total}")
