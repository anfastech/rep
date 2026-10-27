"""Measure layout gaps between an original video beat and a replay, frame by frame.

Usage: python3 frame_diff.py ORIGINAL OFFSET REPLAY   (OFFSET: where the replayed beat starts in ORIGINAL, seconds)

Features are crude colour masks. A match is a diagnostic: always compare the clips by eye too.
"""
import subprocess
import sys

from PIL import Image

W, H = 360, 640
TIMES = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]


def grab(path, t):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", path, "-frames:v", "1",
                          "-vf", f"scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    return Image.frombytes("RGB", (W, H), raw)


def features(img):
    px = img.load()
    gold, skin, cap, sat_rows = [], [], [], {}
    lum = 0
    for y in range(H):
        for x in range(W):
            r, g, b = px[x, y]
            lum += 0.299 * r + 0.587 * g + 0.114 * b
            if r > 190 and g > 140 and b < 110 and r - b > 110:
                gold.append(y)
            if r > 150 and 100 < g < 210 and 80 < b < 190 and r - b > 30 and r > g > b and abs(r - g) < 70:
                skin.append((x, y))
            if y < H * 0.4 and r > 200 and g > 200 and b > 200:
                cap.append((x, y))
            mx, mn = max(r, g, b), min(r, g, b)
            if mx > 150 and mx - mn > 110:
                sat_rows[y] = sat_rows.get(y, 0) + 1
    f = {"luma": lum / (W * H)}
    f["gold_pct"] = 100 * len(gold) / (W * H)
    f["gold_y"] = sum(gold) / len(gold) / H if gold else 0
    f["skin_pct"] = 100 * len(skin) / (W * H)
    f["skin_bottom"] = max(y for _, y in skin) / H if skin else 0
    if cap:
        ys = sorted(y for _, y in cap)
        f["cap_y"] = ys[0] / H
        f["cap_h"] = (ys[-1] - ys[0]) / H
        f["cap_w"] = (max(x for x, _ in cap) - min(x for x, _ in cap)) / W
    else:
        f["cap_y"] = f["cap_h"] = f["cap_w"] = 0
    f["pixrow_y"] = max(sat_rows, key=sat_rows.get) / H if sat_rows else 0
    return f


def main():
    orig, off, new = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    rows = [(t, features(grab(orig, off + t)), features(grab(new, t))) for t in TIMES]
    keys = list(rows[0][1])
    print(f"{'feature':<12}" + "".join(f"{t:>14}" for t in TIMES) + f"{'mean |diff|':>13}")
    for k in keys:
        cells, diffs = "", []
        for _, a, b in rows:
            cells += f"{a[k]:>7.2f}/{b[k]:<6.2f}"
            diffs.append(abs(a[k] - b[k]))
        print(f"{k:<12}{cells}{sum(diffs) / len(diffs):>13.3f}")
    print("cells: original/ours. y values are fractions of frame height.")


if __name__ == "__main__":
    main()
