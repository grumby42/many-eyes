#!/usr/bin/env python3
"""Assemble Many Eyes: read ch-*.json, validate + normalise, inject into template."""
import json, re, sys, datetime, pathlib

SP = pathlib.Path("/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad")
ORDER = ["heian", "thirty-years", "london-1666", "french-rev", "russia-1812", "us-civil-war",
         "ww1", "russia-1917", "nanjing-1937", "ww2-europe", "japan-1945", "long-threads"]
out_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else SP / "build" / "many-eyes.html"
stamp = sys.argv[2] if len(sys.argv) > 2 else datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
dt = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ")
build = "EYES-" + dt.strftime("%Y%m%d-%H%MZ")

SHORT = {"Murasaki Shikibu": "Murasaki", "Sei Shōnagon": "Sei Shōnagon"}
SHORTS = json.loads((SP / "build" / "shorts.json").read_text(encoding="utf-8"))
FIXES, FIXLOG = [], []
for fp in sorted((SP / "build").glob("manual-fixes.json")) + sorted(SP.glob("audit-*.json")):
    FIXES += json.loads(fp.read_text(encoding="utf-8"))
log = []
chapters = []
for cid in ORDER:
    p = pathlib.Path(__import__("os").environ.get("CHDIR", str(SP))) / f"ch-{cid}.json"
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
                    if e.get("id") == key: e.update(f)
            elif kind == "intro":
                i = int(key); v = f.get("text") or f.get("intro") or f.get("paragraph")
                if v: ch["intro"][i] = v
                tr = f.get("text_replace")
                if tr:
                    if tr["old"] not in ch["intro"][i]: raise ValueError("text_replace old not found")
                    ch["intro"][i] = ch["intro"][i].replace(tr["old"], tr["new"])
            elif kind == "threads_out":
                ch["threads_out"][int(key)].update(f)
            elif kind in ("convergence", "image"):
                arr = ch["convergences" if kind == "convergence" else "images"]; i = int(key)
                if f.get("delete"): arr[i] = None
                else: arr[i].update(f)
            else:
                continue
            FIXLOG.append(f"{cid} {fx['where']} [{fx.get('severity')}] applied")
        except Exception as ex:
            FIXLOG.append(f"{cid} {fx.get('where')} FAILED {ex}")
    ch["entries"] = [e for i, e in enumerate(ch["entries"]) if i not in dels]
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
    ch["threads_out"] = [t for t in ch.get("threads_out", []) if t.get("to") in ORDER and t.get("to") != cid]
    chapters.append(ch)
    log.append(f"{cid}: {len(eyes)} eyes, {len(good)} entries, {len(ch.get('convergences', []))} convergences, {len(ch.get('images', []))} plates")

data = json.dumps({"chapters": chapters}, ensure_ascii=False)
data = data.replace("</", "<\\/").replace("<!--", "<\\!--")
tpl = (SP / "build" / "template.html").read_text(encoding="utf-8")
html = tpl.replace("__DATA__", data).replace("__BUILD__", build).replace("__STAMP__", stamp)
out_path.write_text(html, encoding="utf-8")
print("\n".join(log)); print(f"fixes applied: {sum(1 for x in FIXLOG if 'applied' in x)}, failed: {[x for x in FIXLOG if 'FAILED' in x]}")
print(f"wrote {out_path} ({len(html)//1024} KB) build={build} stamp={stamp}")
