"""Extract a compact cross-series dataset from the seven built volumes, and compute the Long Chains."""
import json, re, pathlib, collections, itertools

VOLS = [("1", "I", "many-eyes.html"), ("2", "II", "many-eyes-volume-2.html"), ("3", "III", "many-eyes-volume-3.html"),
        ("4", "IV", "many-eyes-volume-4.html"), ("5", "V", "many-eyes-volume-5.html"), ("6", "VI", "many-eyes-volume-6.html"),
        ("7", "VII", "many-eyes-volume-7.html"), ("8", "VIII", "many-eyes-volume-8.html"), ("9", "IX", "many-eyes-volume-9.html"), ("10", "X", "many-eyes-volume-10.html"), ("11", "XI", "many-eyes-volume-11.html"), ("13", "XIII", "many-eyes-volume-13.html"), ("14", "XIV", "many-eyes-volume-14.html"), ("15", "XV", "many-eyes-volume-15.html")]
SRC = pathlib.Path("/home/claude")

def year_of(iso):
    m = re.match(r"^(-?\d{1,4})", str(iso or ""))
    return int(m.group(1)) if m else None

def load():
    vols, chapters, eyes, entries, edges = [], [], [], [], []
    for vn, roman, fn in VOLS:
        if not (SRC / fn).exists(): continue
        s = (SRC / fn).read_text(encoding="utf-8")
        d = json.loads(re.search(r'<script id="book-data" type="application/json">(.*?)</script>', s, re.S).group(1))
        build = re.search(r'BUILD = "([^"]+)"', s).group(1)
        m = d.get("meta") or {}
        vtitle = m["volume"].split("·")[-1].strip() if "·" in (m.get("volume") or "") else {"1": "Diaries Across History", "2": "Diaries Across History, continued", "3": "Edges of the Map"}.get(vn, "")
        vols.append({"v": vn, "r": roman, "f": fn, "t": vtitle, "b": build})
        for ci, ch in enumerate(d["chapters"]):
            key = f"v{vn}:{ch['id']}"
            yrs = [y for y in (year_of(e.get("date_iso")) for e in ch["entries"]) if y is not None]
            chapters.append({"k": key, "v": vn, "n": ci + 1, "id": ch["id"], "t": ch.get("short_title") or ch["title"],
                             "T": ch["title"], "s": ch.get("span", ""), "y0": min(yrs) if yrs else None, "y1": max(yrs) if yrs else None,
                             "ne": len(ch["eyes"]), "nn": len(ch["entries"])})
            names = {}
            for e in ch["eyes"]:
                names[e["id"]] = e.get("short") or e["name"]
                eyes.append({"k": key, "id": e["id"], "n": e["name"], "l": e.get("life", ""), "w": (e.get("where") or "")[:80],
                             "r": (e.get("role") or e.get("side") or "")[:110], "p": e.get("pron", "")})
            for e in ch["entries"]:
                entries.append({"k": key, "d": e.get("date_iso", ""), "dd": e.get("date_display", ""), "e": names.get(e.get("eye"), e.get("eye", "")),
                                "ei": e.get("eye", ""), "p": (e.get("place") or "")[:60], "h": (e.get("headline") or "")[:160],
                                "a": 1 if e.get("confidence") == "approx" else 0})
            for t in ch.get("threads_out", []) or []:
                to = (t.get("to") or "").strip()
                if not to: continue
                tk = to if re.match(r"^v\d+:", to) else f"v{vn}:{to}"
                edges.append({"a": key, "b": tk, "note": t.get("note", "")})
    ck = {c["k"] for c in chapters}
    edges = [e for e in edges if e["b"] in ck and e["a"] != e["b"]]
    return vols, chapters, eyes, entries, edges

def chains(chapters, edges, top=14):
    yr = {c["k"]: (c["y0"] if c["y0"] is not None else 0) for c in chapters}
    adj = collections.defaultdict(dict)
    for e in edges:
        a, b = e["a"], e["b"]
        if yr[a] < yr[b]: adj[a].setdefault(b, e["note"])
        elif yr[b] < yr[a]: adj[b].setdefault(a, e["note"])
    memo = {}
    def best(n):  # longest strictly-later path from n
        if n in memo: return memo[n]
        bp = [n]
        for m in sorted(adj[n], key=lambda x: yr[x]):
            p = [n] + best(m)
            if len(p) > len(bp) or (len(p) == len(bp) and yr[p[-1]] > yr[bp[-1]]): bp = p
        memo[n] = bp
        return bp
    vol = {c["k"]: c["v"] for c in chapters}
    grand = best(min(memo or {c["k"]: 0 for c in chapters}, key=lambda k: yr[k]) if False else max((c["k"] for c in chapters), key=lambda k: len(best(k))))
    cands = []
    for c in chapters:
        n = c["k"]
        for m in adj[n]:
            for m2 in [None] + list(adj[m]):
                p = [n, m] + (best(m2) if m2 else best(m)[1:])
                p = p[:9]
                if len(p) >= 4: cands.append(p)
    uniq = {tuple(p): p for p in cands}
    cands = sorted(uniq.values(), key=lambda p: (-(len(set(vol[k] for k in p)) + len(p)), yr[p[0]]))
    out, used = [], []
    for p in cands:
        sp = set(p)
        if any(len(sp & u) > 2 for u in used): continue
        used.append(sp)
        hops = [{"k": p[0], "note": ""}] + [{"k": p[i + 1], "note": adj[p[i]].get(p[i + 1], "")} for i in range(len(p) - 1)]
        out.append(hops)
        if len(out) >= top: break
    g = [{"k": grand[0], "note": ""}] + [{"k": grand[i + 1], "note": adj[grand[i]].get(grand[i + 1], "")} for i in range(len(grand) - 1)]
    return g, out

def same_days(entries, chapters):
    vol = {c["k"]: c["v"] for c in chapters}
    by = collections.defaultdict(list)
    for i, e in enumerate(entries):
        if re.match(r"^-?\d{4}-\d{2}-\d{2}$", e["d"]) and not e["a"]: by[e["d"]].append(i)
    rows = []
    for d, idx in by.items():
        ks = {entries[i]["k"] for i in idx}
        vs = {vol[k] for k in ks}
        if len(ks) >= 2: rows.append({"d": d, "i": idx, "nc": len(ks), "nv": len(vs)})
    rows.sort(key=lambda r: (-r["nv"], -r["nc"], r["d"]))
    return rows

if __name__ == "__main__":
    vols, chapters, eyes, entries, edges = load()
    grand, ch = chains(chapters, edges)
    sd = same_days(entries, chapters)
    print(len(vols), len(chapters), len(eyes), len(entries), len(edges), "chains", [len(c) for c in ch], "multi-chapter days", len(sd), "multi-volume", sum(1 for r in sd if r["nv"] > 1))
    print("grand", len(grand))
    for c in ch: print(len(c), " > ".join(h["k"] for h in c))
