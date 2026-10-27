"""Measure the form of a set of text outputs, compare two sets, or check a skill for leaked content.

  python3 style_stats.py profile DIR             features per file + set invariants
  python3 style_stats.py compare ORIG_DIR NEW_DIR  flag NEW features outside ORIG's observed range
  python3 style_stats.py leak SKILL.md ORIG_DIR  shared 6-word runs between a skill and the originals

Reads every *.txt and *.md file in a directory. Standard library only.
"""
import re
import sys
from pathlib import Path

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CONTRACTION = re.compile(r"\b\w+'(s|t|re|ve|ll|d|m)\b", re.I)


def load(d):
    return {p.name: p.read_text() for p in sorted(Path(d).iterdir()) if p.suffix in (".txt", ".md")}


def sentences(text):
    flat = " ".join(l.strip() for l in text.splitlines() if l.strip())
    return [s for s in re.split(r"(?<=[.?!])\s+", flat) if s.strip()]


def line_shape(line):
    """First token of a line, digits collapsed, so '1/ You need' -> '#/'."""
    tok = line.split()[0] if line.split() else ""
    return re.sub(r"\d+", "#", tok)


def features(text):
    lines = text.strip("\n").splitlines()
    body = [l for l in lines if l.strip()]
    sents = sentences(text)
    slen = [len(s.split()) for s in sents] or [0]
    return {
        "words": len(text.split()),
        "lines": len(lines),
        "nonblank_lines": len(body),
        "sentences": len(sents),
        "max_sentence_words": max(slen),
        "mean_sentence_words": round(sum(slen) / len(slen), 1),
        "first_line_words": len(body[0].split()) if body else 0,
        "questions": text.count("?"),
        "exclaims": text.count("!"),
        "emojis": len(EMOJI.findall(text)),
        "hashtags": len(re.findall(r"#\w", text)),
        "contractions": len(CONTRACTION.findall(text)),
        "hyphens": len(re.findall(r"\w-\w", text)),
        "dashes": len(re.findall("[–—]|--", text)),
        "digits": len(re.findall(r"\d+", text)),
        "we_our": len(re.findall(r"\b(we|our|us)\b", text, re.I)),
        "you_your": len(re.findall(r"\b(you|your)\b", text, re.I)),
        "i_my": len(re.findall(r"\b(I|my|me)\b", text)),
    }


def profile(d):
    files = load(d)
    feats = {n: features(t) for n, t in files.items()}
    keys = list(next(iter(feats.values())))
    print(f"N={len(files)}  " + "  ".join(files))
    print(f"{'feature':22} {'min':>6} {'max':>6} {'mean':>6}  per-file")
    for k in keys:
        vals = [f[k] for f in feats.values()]
        print(f"{k:22} {min(vals):>6} {max(vals):>6} {sum(vals) / len(vals):>6.1f}  {vals}")
    shapes = {n: [line_shape(l) for l in t.splitlines() if l.strip()] for n, t in files.items()}
    print("\nline shapes (first token per non-blank line):")
    for n, s in shapes.items():
        print(f"  {n}: {' | '.join(s)}")
    line_sets = [set(l.strip() for l in t.splitlines() if l.strip()) for t in files.values()]
    fixed = set.intersection(*line_sets)
    print(f"\nlines identical in all {len(files)} files: {sorted(fixed) or 'none'}")
    return feats


def compare(orig_dir, new_dir):
    o = {n: features(t) for n, t in load(orig_dir).items()}
    n = {k: features(t) for k, t in load(new_dir).items()}
    print(f"ORIG N={len(o)}  NEW N={len(n)}")
    print(f"{'feature':22} {'orig range':>12} {'new range':>12}  flag")
    flagged = 0
    for k in next(iter(o.values())):
        ov = [f[k] for f in o.values()]
        nv = [f[k] for f in n.values()]
        outside = [v for v in nv if v < min(ov) or v > max(ov)]
        flag = f"OUTSIDE x{len(outside)}" if outside else ""
        flagged += bool(outside)
        print(f"{k:22} {f'{min(ov)}-{max(ov)}':>12} {f'{min(nv)}-{max(nv)}':>12}  {flag}")
    print(f"\n{flagged} features outside the original range. A flag is a lead to inspect, not a verdict:"
          " a small original set under-samples the true range.")


def leak(skill_path, orig_dir, n=6):
    def grams(t):
        w = re.findall(r"[\w$']+", t.lower())
        return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}

    skill = grams(Path(skill_path).read_text())
    hits = 0
    for name, text in load(orig_dir).items():
        shared = sorted(skill & grams(text))
        hits += len(shared)
        for g in shared:
            print(f"{name}: {g}")
    print(f"\n{hits} shared {n}-word runs. Fixed lines that repeat in every original (sign-offs, CTAs) are"
          " expected; anything else is copied content.")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["help"]
    {"profile": profile, "compare": compare, "leak": leak}.get(cmd, lambda *_: print(__doc__))(*args)
