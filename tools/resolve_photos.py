#!/usr/bin/env python3
"""Fill in a Commons file for every photos.json entry that has a "query" but no "commons" yet.

Picks the first search hit whose licence is free (public domain, CC0, CC BY, CC BY-SA), that is a
raster image and at least --min-width pixels wide. Writes the choice back into photos.json so the
next run (and fetch_commons.py get) uses the same file. Review the contact sheet afterwards.

  python3 tools/resolve_photos.py --project episodes/E001-ships-over-land
"""
import argparse, json, pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "engine" / "scripts"))
import fetch_commons as fc
import re
# titles that are almost never period material for a history channel
BAD = re.compile(r"parade|festival|reenact|cosplay|costume|selfie|carnival|fancy dress", re.I)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--min-width", type=int, default=1000)
    a = ap.parse_args()
    proj = pathlib.Path(a.project)
    spec = json.loads((proj / "photos.json").read_text())
    used = {p.get("commons") for p in spec["photos"] if p.get("commons")}
    missing = 0
    for p in spec["photos"]:
        if p.get("commons") and not p.get("url"):
            # verify a guessed file name; fall back to the queries if Commons does not have it
            r = fc.api(action="query", titles=p["commons"], **fc.IIPROP)
            pg = ((r.get("query") or {}).get("pages") or [{}])[0]
            if pg.get("missing") is not None or "imageinfo" not in pg:
                print(f"{p['id']}: {p['commons']} not on Commons, searching instead")
                used.discard(p.pop("commons"))
            else:
                continue
        if p.get("commons") or p.get("url") or not p.get("query"):
            continue
        queries = p["query"] if isinstance(p["query"], list) else [p["query"]]
        pages = []
        for q in queries:
            r = fc.api(action="query", generator="search", gsrsearch=q, gsrnamespace=6, gsrlimit=20, **fc.IIPROP)
            pages += sorted((r.get("query") or {}).get("pages", []), key=lambda x: x.get("index", 0))
        pick = None
        for pg in pages:
            d = fc.info(pg)
            if d["title"] in used or not fc.FREE.search(d["license"] or ""):
                continue
            if "image/jpeg" not in (d["mime"] or "") and "image/png" not in (d["mime"] or ""):
                continue
            if (d["w"] or 0) < a.min_width:
                continue
            if BAD.search(d["title"]):
                continue
            pick = d; break
        if not pick:
            print(f"{p['id']}: no free image found for {p['query']!r}"); missing += 1; continue
        p["commons"] = pick["title"]; used.add(pick["title"])
        print(f"{p['id']}: {pick['title']}  [{pick['license']}]  {pick['w']}x{pick['h']}")
        time.sleep(0.5)
    (proj / "photos.json").write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    if missing:
        sys.exit(f"{missing} photo(s) unresolved: change their query or set 'commons' by hand")

if __name__ == "__main__":
    main()
