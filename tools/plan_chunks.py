#!/usr/bin/env python3
"""Print a GitHub Actions matrix of frame-exact render chunks for a project: [{"i":0,"t0":..,"t1":..},...]"""
import json, pathlib, sys
proj, n = pathlib.Path(sys.argv[1]), int(sys.argv[2])
dur = json.loads((proj / "audio" / "timing.json").read_text())["total_duration"]
fps = 30; frames = round(dur * fps); n = max(1, min(n, frames // 300 or 1))
b = [frames * i // n for i in range(n + 1)]
print(json.dumps([{"i": i, "t0": round(b[i] / fps, 6), "t1": round(b[i + 1] / fps, 6)} for i in range(n)]))
