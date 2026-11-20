#!/usr/bin/env python3
"""Make a labelled contact sheet of every downloaded photo, for review."""
import json, pathlib, sys
from PIL import Image, ImageDraw
proj = pathlib.Path(sys.argv[1]); spec = json.loads((proj / "photos.json").read_text())
tiles = []
for p in spec["photos"]:
    f = proj / "assets" / "photos" / (p.get("file") or "")
    if not p.get("file") or not f.exists(): continue
    im = Image.open(f).convert("RGB"); im.thumbnail((480, 360))
    t = Image.new("RGB", (480, 400), (20, 20, 20)); t.paste(im, ((480 - im.width) // 2, 0))
    ImageDraw.Draw(t).text((8, 368), f"{p['id']}  {p.get('commons', '')[5:60]}", fill=(230, 230, 230)); tiles.append(t)
if tiles:
    cols = 3; rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 480, rows * 400), (10, 10, 10))
    for i, t in enumerate(tiles): sheet.paste(t, ((i % cols) * 480, (i // cols) * 400))
    sheet.save(proj / "out" / "photos_sheet.jpg", quality=85)
