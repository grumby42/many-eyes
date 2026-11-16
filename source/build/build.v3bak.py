#!/usr/bin/env python3
"""Assemble Many Eyes: read ch-*.json, validate + normalise, inject into template."""
import json, re, sys, datetime, pathlib, base64, io
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import geo

SP = pathlib.Path("/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad")
import os
VOL = os.environ.get("VOL", "1")
V1ORDER = ["heian", "thirty-years", "london-1666", "french-rev", "russia-1812", "us-civil-war",
         "ww1", "russia-1917", "nanjing-1937", "ww2-europe", "japan-1945", "long-threads"]
V2ORDER = ["merer", "babylon-331", "vesuvius-79", "black-death", "constantinople-1453", "first-contact", "imjin-war",
           "ming-qing", "vienna-1683", "lisbon-1755", "tambora-1816", "opium-war", "irish-famine", "black-ships",
           "delhi-1857", "krakatoa-1883", "spain-1936", "moscow-1937", "partition-1947", "apollo-11", "wall-1989"]
ORDER = V2ORDER if VOL == "2" else V1ORDER
ROOT = SP / "vol2" if VOL == "2" else SP
out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SP / "build" / "many-eyes.html"
stamp = sys.argv[2] if len(sys.argv) > 2 else datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
dt = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")
build = ("EYES2-" if VOL == "2" else "EYES-") + dt.strftime("%Y%m%d-%H%MZ")

SHORT = {"Murasaki Shikibu": "Murasaki", "Sei Shōnagon": "Sei Shōnagon"}
SHORTS = json.loads((SP / "build" / "shorts.json").read_text(encoding="utf-8"))
FIXES, FIXLOG = [], []
for fp in sorted(((SP / "build") if VOL == "1" else ROOT).glob("manual-fixes.json")) + sorted(ROOT.glob("audit-*.json")):
    FIXES += json.loads(fp.read_text(encoding="utf-8"))
COORDS = json.loads((ROOT / "coords.json").read_text(encoding="utf-8")) if (ROOT / "coords.json").exists() else {}
PATCHES = {}
for fp in sorted(ROOT.glob("patch-*.json")):
    try:
        pj = json.loads(fp.read_text(encoding="utf-8")); PATCHES.setdefault(pj["chapter"], []).append(pj)
    except Exception as ex:
        print("BAD PATCH", fp, ex)
AUDIT2 = []
for fp in sorted(ROOT.glob("audit2-*.json")):
    AUDIT2 += json.loads(fp.read_text(encoding="utf-8"))
for cid_, plist in PATCHES.items():
    for pj in plist:
        dels2 = {}
        for fx in AUDIT2:
            if fx.get("patch") != cid_ or not fx.get("fix"): continue
            kind, _, key = str(fx.get("where", "")).partition(":")
            f = fx["fix"]
            try:
                if kind == "add_eyes":
                    for e in pj.get("add_eyes", []):
                        if e.get("id") == key: e.update(f)
                else:
                    arr = pj.get(kind, []); i = int(key)
                    if f.get("delete"): dels2.setdefault(kind, set()).add(i)
                    elif kind == "updates": arr[i].setdefault("fix", {}).update(f)
                    else: arr[i].update(f)
                FIXLOG.append(f"{cid_} audit2 {fx['where']} applied")
            except Exception as ex:
                FIXLOG.append(f"{cid_} audit2 {fx.get('where')} FAILED {ex}")
        for kind, idx in dels2.items():
            pj[kind] = [x for i, x in enumerate(pj.get(kind, [])) if i not in idx]
MANIFEST = json.loads((ROOT / "images" / "manifest.json").read_text(encoding="utf-8")) if (ROOT / "images" / "manifest.json").exists() else []
REJECT = set(json.loads((ROOT / "images" / "reject.json").read_text())) if (ROOT / "images" / "reject.json").exists() else set()

def embed_image(path):
    from PIL import Image
    im = Image.open(path); im = im.convert("RGB")
    im.thumbnail((1000, 1000))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']
EXTERNAL = {}
if VOL == "2":
    for i, cid0 in enumerate(V1ORDER):
        fp = SP / f"ch-{cid0}.json"
        if fp.exists():
            EXTERNAL["v1:" + cid0] = {"volume": "Volume I", "num": ROMAN[i + 1], "title": json.loads(fp.read_text(encoding="utf-8")).get("title", cid0)}
OUTLINE_TITLE_OF = {"merer": "The Pyramid Logbook", "black-death": "The Great Mortality", "constantinople-1453": "The Last Days of Constantinople",
    "imjin-war": "The Imjin War", "vienna-1683": "Vienna Besieged", "lisbon-1755": "The Morning the Earth Moved",
    "tambora-1816": "The Year Without a Summer", "krakatoa-1883": "The Sound Heard Round the World",
    "babylon-331": "Written in the Stars", "first-contact": "First Contact", "ming-qing": "The Mandate Changes Hands",
    "opium-war": "Opium and Gunboats", "irish-famine": "The Great Hunger", "black-ships": "The Black Ships", "delhi-1857": "Delhi, 1857",
    "vesuvius-79": "Ash at Misenum", "spain-1936": "Spain Divided", "moscow-1937": "Moscow, 1937", "partition-1947": "The Sixth River",
    "apollo-11": "One Small Step", "wall-1989": "The Wall Opens"}
if VOL == "2":
    META = {"html_title": "Many Eyes, Volume II — Diaries Across History", "kicker": "A synoptic reader", "volume": "Volume II",
        "sub": "From a pyramid logbook to the night the Wall opened: forty-five centuries of the same days, written down by people on every side of them",
        "preface": "Volume II follows the method of the first book further back in time and across more of the world. It opens with the oldest dated diary we have, a boat inspector's logbook from the reign of Khufu, and Babylonian astronomers recording the night sky over Alexander's battles. It then runs through plague, siege, first contact between continents, the fall of a dynasty, invasion, three natural catastrophes recorded on several continents at once, the nineteenth century's collisions of empire (the Opium War, the Irish Famine, Perry's black ships in Edo Bay and the uprising of 1857), and finally the twentieth century: Spain divided, the Moscow purges, the Partition of India, the first landing on the Moon and the year the Wall came down. The modern chapters quote almost nothing, because their diaries are still in copyright; they are told in digests, with the famous public phrases as the only exceptions. As before, every chapter lays the records of people inside one stretch of history on a single timeline, and where two or more of them wrote about the same day the timeline places their entries side by side and marks the row in gold. Threads at the end of each chapter point back into Volume I where the stories connect.",
        "outline_title": "Still to come"}
else:
    META = {"html_title": "Many Eyes — Diaries Across History", "kicker": "A synoptic reader", "volume": "",
        "sub": "The same days of history, written down by the people who lived them — across courts, armies, cities and continents",
        "preface": "Every chapter takes one stretch of history and lays the private records of the people inside it on a single timeline: court ladies and the regent they served; a mercenary and the burgher whose city he burned; a bookseller, a king and an American diplomat on the same July days in Paris; a missionary, her Chinese colleague, a German Nazi Party member and a Japanese general inside the same captured city. Where two or more of them wrote about the same day, the timeline places their entries side by side and marks the row in gold.",
        "outline_title": "Volume II — contents"}

_VOICE = [
    (r"\bNOT RE-VERIFIED in this session\b", "Not re-checked for this edition"),
    (r"\bnot re-verified this session\b", "not re-checked for this edition"),
    (r"\s*\((read|fetched|seen) this session\)", ""),
    (r"\b(could not|couldn't) be (opened|consulted|reached|confirmed|checked) in this session\b", r"could not be \2 for this edition"),
    (r"\bwas not (confirmed|consulted|examined|checked) (in )?this session\b", r"was not \1 for this edition"),
    (r"\bwere not (confirmed|consulted|examined|checked) (in )?this session\b", r"were not \1 for this edition"),
    (r"\bwas reachable this session\b", "was reachable for this edition"),
    (r"\bin this (session|pass)\b", "for this edition"),
    (r"\bthis session\b", "this edition"),
    (r"\bI could not consult\b", "this edition could not consult"),
    (r"\bI could not (see|open|check|confirm|verify)\b", r"this edition could not \1"),
    (r"\bI could verify\b", "this edition could verify"),
    (r"\bI did not (see|verify|check|confirm|consult)\b", r"this edition did not \1"),
    (r"\bThe online text I could reach\b", "The online text available"),
    (r"\bI could reach\b", "available"),
]
def neutral_voice(txt):
    for a, c in _VOICE:
        txt = re.sub(a, c, txt)
    # capitalise sentence starts that now begin with 'this edition'
    txt = re.sub(r"(^|[.;:]\s+)this edition", lambda m: m.group(1) + "This edition", txt)
    return txt
def scrub(o, key=""):
    if isinstance(o, dict):
        return {k: (v if k in ("quote", "url", "embed", "svg", "map_svg") else scrub(v, k)) for k, v in o.items()}
    if isinstance(o, list):
        return [scrub(v, key) for v in o]
    if isinstance(o, str) and key not in ("quote", "url"):
        return neutral_voice(o)
    return o
log = []
chapters = []
for cid in ORDER:
    p = pathlib.Path(os.environ.get("CHDIR", str(ROOT))) / f"ch-{cid}.json"
    if not p.exists():
        log.append(f"MISSING chapter {cid}")
        continue
    ch = json.loads(p.read_text(encoding="utf-8"))
    ch["id"] = cid
    # ---- apply audit + manual fixes (indices refer to the raw file) ----
    dels = set()
    for fx in FIXES:
        if fx.get("chapter") != cid or not fx.get("fix"):
            continue
        kind, _, key = str(fx.get("where", "")).partition(":")
        f = fx["fix"]
        try:
            if kind == "entry":
                i = int(key)
                if f.get("delete"): dels.add(i)
                else: ch["entries"][i].update({k: v for k, v in f.items() if k != "delete"})
            elif kind == "eye":
                for e in ch["eyes"]:
                    if e.get("id") == key:
                        tr = f.get("text_replace")
                        if tr:
                            hit = False
                            for fld in ("bio", "role", "authenticity", "where", "life", "vantage_label"):
                                if tr["old"] in str(e.get(fld, "")): e[fld] = e[fld].replace(tr["old"], tr["new"]); hit = True
                            if not hit: raise ValueError("eye text_replace old not found")
                        e.update({k: v for k, v in f.items() if k != "text_replace"})
            elif kind == "intro":
                i = int(key); v = f.get("text") or f.get("intro") or f.get("paragraph")
                if v: ch["intro"][i] = v
                tr = f.get("text_replace")
                if tr:
                    if tr["old"] not in ch["intro"][i]: raise ValueError("text_replace old not found")
                    ch["intro"][i] = ch["intro"][i].replace(tr["old"], tr["new"])
            elif kind == "threads_out":
                tr = f.get("text_replace")
                if tr:
                    t0 = ch["threads_out"][int(key)]
                    if tr["old"] not in t0.get("note", ""): raise ValueError("text_replace old not found")
                    t0["note"] = t0["note"].replace(tr["old"], tr["new"])
                else:
                    ch["threads_out"][int(key)].update(f)
            elif kind in ("calendar_note", "vantage_key", "subtitle", "title"):
                tr = f.get("text_replace")
                if tr:
                    if tr["old"] not in ch.get(kind, ""): raise ValueError("text_replace old not found")
                    ch[kind] = ch[kind].replace(tr["old"], tr["new"])
                else:
                    ch[kind] = f.get("text", f.get(kind, ch.get(kind)))
            elif kind in ("convergence", "image"):
                arr = ch["convergences" if kind == "convergence" else "images"]; i = int(key)
                if f.get("delete"): arr[i] = None
                else: arr[i].update(f)
            else:
                continue
            FIXLOG.append(f"{cid} {fx['where']} [{fx.get('severity')}] applied")
        except Exception as ex:
            FIXLOG.append(f"{cid} {fx.get('where')} FAILED {ex}")
    for pj in PATCHES.get(cid, []):
        for up in pj.get("updates", []):
            kind, _, key = str(up.get("where", "")).partition(":")
            try:
                if kind == "entry": ch["entries"][int(key)].update(up.get("fix") or {})
                elif kind == "eye":
                    for e in ch["eyes"]:
                        if e.get("id") == key: e.update(up.get("fix") or {})
                elif kind == "convergence": ch["convergences"][int(key)].update(up.get("fix") or {})
                FIXLOG.append(f"{cid} patch-update {up.get('where')} applied")
            except Exception as ex:
                FIXLOG.append(f"{cid} patch-update {up.get('where')} FAILED {ex}")
    ch["entries"] = [e for i, e in enumerate(ch["entries"]) if i not in dels]
    known = {e.get("id") for e in ch["eyes"]}
    for pj in PATCHES.get(cid, []):
        for e in pj.get("add_eyes", []):
            if e.get("id") in known: continue
            ch["eyes"].append(e); known.add(e.get("id"))
            if e.get("lat") is not None: COORDS.setdefault(f"{cid}:{e['id']}", {"lat": e["lat"], "lon": e["lon"], "label": e.get("where", "")[:40]})
        ch["entries"] += pj.get("add_entries", [])
        ch.setdefault("convergences", []).extend(pj.get("add_convergences", []))
        ch.setdefault("ties", []).extend(pj.get("add_ties", []))
        ch.setdefault("images", []).extend(pj.get("add_images", []))
        ch.setdefault("further", []).extend(pj.get("add_further", []))
    for k in ("convergences", "images"):
        ch[k] = [x for x in ch.get(k, []) if x]
    eyes = ch.get("eyes", [])
    ids = set()
    for e in eyes:
        e["id"] = re.sub(r"[^a-z0-9-]+", "-", str(e.get("id", "")).lower()).strip("-") or "eye"
        if e["id"] in ids:
            e["id"] += "-2"
        ids.add(e["id"])
        try:
            e["vantage"] = max(0, min(4, int(e.get("vantage", 2))))
        except Exception:
            e["vantage"] = 2
        e["sources"] = [s for s in e.get("sources", []) if isinstance(s, dict)]
        nm = str(e.get("name", ""))
        if e.get("lat") is not None and f"{cid}:{e['id']}" not in COORDS:
            try: COORDS[f"{cid}:{e['id']}"] = {"lat": float(e["lat"]), "lon": float(e["lon"]), "label": (e.get("coord_label") or e.get("where") or "")[:40], "waypoints": e.get("waypoints") or []}
            except Exception: pass
        if f"{cid}:{e['id']}" in SHORTS: e["short"] = SHORTS[f"{cid}:{e['id']}"]
        if not e.get("short"):
            base = re.sub(r"\s*\(.*?\)", "", nm).split(",")[0].strip() or nm
            if nm in SHORT: e["short"] = SHORT[nm]
            elif base in SHORT: e["short"] = SHORT[base]
            elif " no " in base and len(base) > 15: e["short"] = base.split(" no ")[-1]
            elif len(base) <= 12: e["short"] = base
            elif len(nm) <= 15: e["short"] = nm
            else: e["short"] = base.split()[-1]
    # remap entry eye ids with the same slugging
    def slug(x):
        return re.sub(r"[^a-z0-9-]+", "-", str(x).lower()).strip("-")
    good = []
    for en in ch.get("entries", []):
        en["eye"] = slug(en.get("eye", ""))
        if en["eye"] not in ids:
            log.append(f"{cid}: entry eye '{en['eye']}' not in eyes -> dropped ({en.get('headline')})")
            continue
        if not re.match(r"^-?\d{1,4}(-\d{2}){0,2}", str(en.get("date_iso", ""))):
            log.append(f"{cid}: bad date_iso {en.get('date_iso')!r} -> dropped")
            continue
        q = (en.get("quote") or "").strip().strip('"“”')
        if q and len(q.split()) > 12:
            log.append(f"{cid}: quote over 12 words removed ({en['eye']} {en['date_iso']})")
            q = ""
        en["quote"] = q
        en.setdefault("precision", "day")
        good.append(en)
    ch["entries"] = good
    for c in ch.get("convergences", []):
        c["eyes"] = [slug(x) for x in c.get("eyes", []) if slug(x) in ids]
    ch["ties"] = [t for t in ch.get("ties", []) if slug(t.get("a")) in ids and slug(t.get("b")) in ids]
    for t in ch["ties"]:
        t["a"], t["b"] = slug(t["a"]), slug(t["b"])
    ch["threads_out"] = [t for t in ch.get("threads_out", []) if (t.get("to") in ORDER or t.get("to") in EXTERNAL) and t.get("to") != cid]
    # ---- map of where they stood ----
    pts = []
    for i, e in enumerate(ch["eyes"]):
        c = COORDS.get(f"{cid}:{e['id']}")
        if c: pts.append({"id": e["id"], "name": e["name"], "short": e.get("short", e["name"]), "idx": i, "lat": c["lat"], "lon": c["lon"], "label": c.get("label", ""), "waypoints": c.get("waypoints", [])})
    missing = [e["id"] for e in ch["eyes"] if f"{cid}:{e['id']}" not in COORDS]
    if missing: log.append(f"{cid}: no coords for {missing}")
    ch["map_svg"] = geo.locator_svg(pts, title=f"Map of where the diarists of {ch.get('title','')} stood") if pts else ""
    # ---- data figures ----
    ch["figures"] = []
    if cid == "russia-1812":
        ch["figures"].append({"svg": geo.minard_svg(), "title": "Minard's march, redrawn from his data",
            "caption": "Charles Joseph Minard's 1869 chart of the campaign is often called the best statistical graphic ever drawn. This is a fresh drawing from the numbers he used: the tan band is the army going east, the dark band the army coming back, each as wide as the number of men still alive, with the cold of the retreat plotted beneath. The diarists in this chapter are inside those bands."})
    if cid == "long-threads":
        ch["figures"].append({"svg": geo.snow_svg(), "title": "John Snow's Soho, 1854, redrawn from his data",
            "caption": "Snow marked every cholera death around Broad Street and every public pump. The deaths cluster on one pump. A fresh drawing from the coordinates digitised from his map; his dated letter of 1854 is one of the eyes in this chapter."})
    # ---- embedded public-domain images ----
    for m in MANIFEST:
        if m.get("chapter") != cid or m.get("file") in REJECT: continue
        fpth = ROOT / "images" / "raw" / pathlib.Path(m["file"]).name
        if not fpth.exists(): continue
        try:
            ch["images"].insert(0, {"embed": embed_image(fpth), "title": m.get("title", ""), "caption": m.get("caption", ""),
                "date": m.get("date", ""), "credit": " · ".join(x for x in [m.get("creator", ""), ("original: " + m["original_holder"]) if m.get("original_holder") else "", "public domain"] if x),
                "url": ""})
        except Exception as ex:
            log.append(f"{cid}: image {m.get('file')} failed {ex}")
    ch = scrub(ch)
    chapters.append(ch)
    log.append(f"{cid}: {len(eyes)} eyes, {len(good)} entries, {len(ch.get('convergences', []))} convergences, {len(ch.get('images', []))} plates")

V2 = json.loads((SP / "build" / "volume2.json").read_text(encoding="utf-8")) if (SP / "build" / "volume2.json").exists() else None
if VOL == "2" and V2:
    done_titles = {c.get("outline_title", "") for c in chapters} | {OUTLINE_TITLE_OF.get(c["id"], "") for c in chapters}
    V2 = json.loads(json.dumps(V2))
    for pt in V2["parts"]:
        pt["chapters"] = [c for c in pt["chapters"] if c["title"] not in done_titles]
    V2["parts"] = [pt for pt in V2["parts"] if pt["chapters"]]
    V2["subtitle"] = "The rest of the proposed table of contents, to be researched in later batches"
    V2["intro"] = ["These chapters from the Volume II outline are still to come. The names under each are leads chosen because the records are known to exist; none of it has been verified yet, and every date and claim will be checked the way the chapters in this book were."]
    if not V2["parts"]:
        V2 = None
data = json.dumps({"chapters": chapters, "volume2": V2, "meta": META, "external": EXTERNAL}, ensure_ascii=False)
data = data.replace("</", "<\\/").replace("<!--", "<\\!--")
tpl = (SP / "build" / "template.html").read_text(encoding="utf-8")
html = tpl.replace("__TITLE__", META["html_title"]).replace("__DATA__", data).replace("__BUILD__", build).replace("__STAMP__", stamp)
out_path.write_text(html, encoding="utf-8")
print("\n".join(log)); print(f"fixes applied: {sum(1 for x in FIXLOG if 'applied' in x)}, failed: {[x for x in FIXLOG if 'FAILED' in x]}")
print(f"wrote {out_path} ({len(html)//1024} KB) build={build} stamp={stamp}")
