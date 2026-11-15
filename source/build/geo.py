"""Map + data-figure generators for Many Eyes (pure Python, offline)."""
import json, math, csv, pathlib
from shapely.geometry import Polygon, MultiPolygon, box, LineString
from shapely.ops import unary_union

GEO = pathlib.Path("/tmp/claude-0/-home-claude/fa284f55-6839-573e-8ba4-d29a7355a349/scratchpad/geo")
_LAND = {}


def _decode(topo, name):
    sc, tr = topo["transform"]["scale"], topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
        arcs.append(pts)

    def ring(idx):
        out = []
        for i in idx:
            seg = arcs[i] if i >= 0 else arcs[~i][::-1]
            out.extend(seg if not out else seg[1:])
        return out

    polys = []
    obj = topo["objects"][name]
    geoms = obj["geometries"] if obj["type"] == "GeometryCollection" else [obj]
    for g in geoms:
        parts = g["arcs"] if g["type"] == "MultiPolygon" else [g["arcs"]] if g["type"] == "Polygon" else []
        for p in parts:
            rings = [ring(r) for r in p]
            if len(rings[0]) >= 4:
                try:
                    polys.extend(_fix_antimeridian(rings[0], [r for r in rings[1:] if len(r) >= 4]))
                except Exception:
                    pass
    return polys


def _unwrap(r):
    out = [r[0]]; off = 0.0
    for (a1, b1), (a2, b2) in zip(r, r[1:]):
        d = a2 - a1
        if d > 180: off -= 360
        elif d < -180: off += 360
        out.append((a2 + off, b2))
    return out, off


def _fix_antimeridian(ext, holes):
    """Rings that jump across +-180 are unwrapped, closed round the pole if they circle it, and split back into [-180, 180]."""
    jumps = any(abs(b[0] - a[0]) > 180 for a, b in zip(ext, ext[1:]))
    if not jumps:
        poly = Polygon(ext, holes)
        return [poly if poly.is_valid else poly.buffer(0)]
    u, off = _unwrap(ext)
    if abs(off) > 1:  # circles a pole
        pole = -90 if sum(b for _, b in u) / len(u) < 0 else 90
        u = u[:-1] + [(u[-2][0], pole), (u[0][0], pole), u[0]] if False else u + [(u[-1][0], pole), (u[0][0], pole), u[0]]
    poly = Polygon(u)
    if not poly.is_valid: poly = poly.buffer(0)
    for h in holes:
        hu, _ = _unwrap(h)
        try: poly = poly.difference(Polygon(hu))
        except Exception: pass
    from shapely.affinity import translate
    parts = []
    for k in (-1, 0, 1):
        piece = poly.intersection(box(-180 + 360 * k, -90, 180 + 360 * k, 90))
        if piece.is_empty: continue
        piece = translate(piece, xoff=-360 * k)
        for q in (piece.geoms if hasattr(piece, "geoms") else [piece]):
            if q.geom_type == "Polygon" and not q.is_empty: parts.append(q)
    return parts


def land(res):
    if res not in _LAND:
        topo = json.loads((GEO / "dl" / "package" / f"land-{res}.json").read_text())
        _LAND[res] = _decode(topo, "land")
    return _LAND[res]


def eye_hue(i):
    return round((i * 137.508 + 12) % 360)


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def locator_svg(points, W=820, H=520, title=""):
    """points: list of dicts {name, short, idx, lat, lon, label, waypoints:[{lat,lon,label}]}"""
    pts = [p for p in points if p.get("lat") is not None]
    if not pts:
        return ""
    lats = [p["lat"] for p in pts] + [w["lat"] for p in pts for w in p.get("waypoints", [])]
    lons = [p["lon"] for p in pts] + [w["lon"] for p in pts for w in p.get("waypoints", [])]
    lat0, lat1, lon0, lon1 = min(lats), max(lats), min(lons), max(lons)
    # minimum span and padding
    span = max(lat1 - lat0, (lon1 - lon0) * math.cos(math.radians((lat0 + lat1) / 2)), 3.0)
    pad = span * 0.18 + 0.6
    lat0 -= pad; lat1 += pad
    kx = math.cos(math.radians((lat0 + lat1) / 2))
    lon_pad = pad / max(kx, .2)
    lon0 -= lon_pad; lon1 += lon_pad
    # fit aspect W:H
    w_deg = (lon1 - lon0) * kx; h_deg = lat1 - lat0
    target = W / H
    if w_deg / h_deg < target:
        extra = (h_deg * target - w_deg) / kx / 2; lon0 -= extra; lon1 += extra
    else:
        extra = (w_deg / target - h_deg) / 2; lat0 -= extra; lat1 += extra
    lat0, lat1 = max(lat0, -75), min(lat1, 82)
    lon0, lon1 = max(lon0, -180), min(lon1, 180)
    sx = W / ((lon1 - lon0) * kx); sy = H / (lat1 - lat0)
    s = min(sx, sy)
    ox = (W - (lon1 - lon0) * kx * s) / 2; oy = (H - (lat1 - lat0) * s) / 2
    P = lambda lon, lat: (ox + (lon - lon0) * kx * s, oy + (lat1 - lat) * s)
    span_deg = max(lat1 - lat0, (lon1 - lon0) * kx)
    res = "10m" if span_deg < 9 else "50m" if span_deg < 45 else "110m"
    clip = box(max(lon0 - 1, -179.99), max(lat0 - 1, -89), min(lon1 + 1, 179.99), min(lat1 + 1, 89))
    tol = span_deg / 900
    paths, coast = [], []
    def lines_of(geom):
        if geom.is_empty: return []
        if geom.geom_type == "LineString": return [geom]
        if hasattr(geom, "geoms"): return [x for gg in geom.geoms for x in lines_of(gg)]
        return []
    for poly in land(res):
        if not poly.intersects(clip):
            continue
        g = poly.intersection(clip).simplify(tol, preserve_topology=True)
        for pp in (g.geoms if hasattr(g, "geoms") else [g]):
            if pp.geom_type != "Polygon" or pp.is_empty:
                continue
            for rg in [pp.exterior] + list(pp.interiors):
                c = list(rg.coords)
                if len(c) < 3: continue
                pc = [P(*q) for q in c]; xs_ = [q[0] for q in pc]; ys_ = [q[1] for q in pc]
                if max(xs_) - min(xs_) > W * 0.4 and max(ys_) - min(ys_) < 6: continue
                paths.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in (P(*q) for q in c)) + "Z")
        # coastline strokes: the real shore only, never the clip edge
        inner = box(clip.bounds[0] + 0.02, clip.bounds[1] + 0.02, clip.bounds[2] - 0.02, clip.bounds[3] - 0.02)
        for sub in (poly.geoms if hasattr(poly, "geoms") else [poly]):
          if sub.geom_type != "Polygon": continue
          for rg in [sub.exterior] + list(sub.interiors):
            for ln in lines_of(rg.intersection(inner)):
                ln = ln.simplify(tol)
                c = list(ln.coords)
                pc = [P(*q) for q in c]
                if len(c) >= 2 and max(q[0] for q in pc) - min(q[0] for q in pc) > W * 0.4 and max(q[1] for q in pc) - min(q[1] for q in pc) < 6: continue
                if len(c) >= 2:
                    coast.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in (P(*q) for q in c)))
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title or "Map of where each diarist stood")}" class="locmap">',
           f'<rect width="{W}" height="{H}" fill="var(--sea)"/>']
    # graticule
    step = 1 if span_deg < 8 else 5 if span_deg < 40 else 15
    g = []
    for la in range(int(math.floor(lat0 / step)) * step, int(lat1) + step, step):
        if lat0 < la < lat1:
            x0, y = P(lon0, la); x1, _ = P(lon1, la); g.append(f"M{x0:.0f} {y:.1f}H{x1:.0f}")
    for lo in range(int(math.floor(lon0 / step)) * step, int(lon1) + step, step):
        if lon0 < lo < lon1:
            x, y0 = P(lo, lat1); _, y1 = P(lo, lat0); g.append(f"M{x:.1f} {y0:.0f}V{y1:.0f}")
    out.append(f'<path d="{"".join(g)}" stroke="var(--rule)" stroke-width=".6" fill="none" opacity=".7"/>')
    out.append(f'<path d="{"".join(paths)}" fill="var(--land)" stroke="none" fill-rule="evenodd"/>')
    out.append(f'<path d="{"".join(coast)}" fill="none" stroke="var(--ink3)" stroke-width=".7" stroke-linejoin="round"/>')
    return _overlay(out, pts, P, W, H, wrap=True)


def _overlay(out, pts, P, W, H, wrap=True, note=""):
    # routes
    for p in pts:
        wps = p.get("waypoints") or []
        if wps:
            seq = [P(w["lon"], w["lat"]) for w in wps]
            parts_ = []
            for k, (x, y) in enumerate(seq):
                jump = wrap and k > 0 and abs(wps[k]["lon"] - wps[k - 1]["lon"]) > 180
                parts_.append(("M" if (k == 0 or jump) else "L") + f"{x:.1f} {y:.1f}")
            d = "".join(parts_)
            out.append(f'<path d="{d}" fill="none" stroke="hsl({eye_hue(p["idx"])} var(--eyeS) var(--eyeL))" stroke-width="2" stroke-dasharray="5 4" opacity=".75"/>')
            for (x, y), w in zip(seq, wps):
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="hsl({eye_hue(p["idx"])} var(--eyeS) var(--eyeL))" opacity=".8"><title>{esc(p["name"])} — {esc(w.get("label",""))}</title></circle>')
    # cluster main points by place
    clusters = []
    for p in pts:
        x, y = P(p["lon"], p["lat"])
        for cl in clusters:
            if abs(cl[0][0] - x) < 30 and abs(cl[0][1] - y) < 30:
                cl.append((x, y, p)); break
        else:
            clusters.append([(x, y, p)])
    clusters = {i: c for i, c in enumerate(clusters)}
    labels = []
    for key, items in clusters.items():
        cx = sum(i[0] for i in items) / len(items); cy = sum(i[1] for i in items) / len(items)
        n = len(items)
        for k, (x, y, p) in enumerate(items):
            if n > 1:
                a = 2 * math.pi * k / n - math.pi / 2; r = 7 + 1.4 * n
                x, y = cx + math.cos(a) * r, cy + math.sin(a) * r
            out.append(f'<g class="mapdot" data-eye="{esc(p["id"])}" style="cursor:pointer"><title>{esc(p["name"])} — {esc(p.get("label",""))}</title>'
                       f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="hsl({eye_hue(p["idx"])} var(--eyeS) var(--eyeL))" stroke="var(--card)" stroke-width="1.8"/></g>')
        seen = []
        for it in items:
            lb = it[2].get("label", "").split(",")[0].strip()
            if lb and lb not in seen: seen.append(lb)
        place = " · ".join(seen[:3]) + (" …" if len(seen) > 3 else "")
        names = ", ".join(i[2]["short"] for i in items)
        labels.append((cx, cy + (7 + 1.4 * n if n > 1 else 0), place, names))
    # place labels (simple collision nudging)
    used = []
    for cx, cy, place, names in sorted(labels, key=lambda t: t[1]):
        ly = cy + 18
        shown = names[:70] + ("…" if len(names) > 70 else "")
        half = max(len(place) * 3.6, len(shown) * 2.9) + 8
        lx = min(max(cx, half), W - half)
        if ly > H - 30: ly = cy - 30
        for _ in range(12):
            if all(abs(ly - uy) > 26 or abs(lx - ux) > 150 for ux, uy in used): break
            ly += 14
        used.append((lx, ly))
        out.append(f'<text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-size="12" font-weight="700" fill="var(--ink)" paint-order="stroke" stroke="var(--sea)" stroke-width="3.5">{esc(place)}</text>')
        out.append(f'<text x="{lx:.0f}" y="{ly + 12:.0f}" text-anchor="middle" font-size="10.5" fill="var(--ink2)" paint-order="stroke" stroke="var(--sea)" stroke-width="3">{esc(names[:70] + ("…" if len(names) > 70 else ""))}</text>')
    if note:
        out.append(f'<text x="8" y="{H-8}" font-size="10" fill="var(--ink2)" paint-order="stroke" stroke="var(--sea)" stroke-width="3">{esc(note)}</text>')
    out.append(f'<text x="{W-8}" y="{H-8 - (14 if note else 0)}" text-anchor="end" font-size="9.5" fill="var(--ink3)">Coastlines: Natural Earth (public domain). Positions approximate; dashed lines trace journeys.</text>')
    out.append("</svg>")
    return "".join(out)


def polar_svg(points, pole, W=820, H=560, title=""):
    """Azimuthal equidistant map centred on a pole. pole = 'N' or 'S'."""
    sgn = 1 if pole == "N" else -1
    colat = lambda lat: 90 - sgn * lat
    def proj(lon, lat):
        r = colat(lat); a = math.radians(lon)
        return (r * math.sin(a), (r * math.cos(a)) if pole == "N" else (-r * math.cos(a)))
    pts_all = [p for p in points if p.get("lat") is not None]
    LIM = 62  # colatitude shown at most
    inside = [p for p in pts_all if colat(p["lat"]) <= LIM]
    off = [p for p in pts_all if colat(p["lat"]) > LIM]
    pts = []
    for p in inside:
        q = dict(p); q["waypoints"] = [w for w in (p.get("waypoints") or []) if colat(w["lat"]) <= LIM]
        pts.append(q)
    xy = [proj(p["lon"], p["lat"]) for p in pts] + [proj(w["lon"], w["lat"]) for p in pts for w in p["waypoints"]]
    xy.append((0.0, 0.0))  # always include the pole
    x0, x1 = min(x for x, _ in xy), max(x for x, _ in xy); y0, y1 = min(y for _, y in xy), max(y for _, y in xy)
    span = max(x1 - x0, y1 - y0, 12.0); pad = span * 0.14 + 2
    x0 -= pad; x1 += pad; y0 -= pad; y1 += pad
    if (x1 - x0) / (y1 - y0) < W / H:
        e = ((y1 - y0) * W / H - (x1 - x0)) / 2; x0 -= e; x1 += e
    else:
        e = ((x1 - x0) * H / W - (y1 - y0)) / 2; y0 -= e; y1 += e
    s_ = W / (x1 - x0)
    P = lambda lon, lat: ((proj(lon, lat)[0] - x0) * s_, (y1 - proj(lon, lat)[1]) * s_)
    rmax = max(math.hypot(x, y) for x in (x0, x1) for y in (y0, y1))
    latlim = sgn * (90 - min(rmax + 2, 89))
    band = box(-180, latlim, 180, 90) if pole == "N" else box(-180, -90, 180, latlim)
    view = box(0, 0, W, H)
    res = "50m" if span < 40 else "110m"
    paths, coast, projected = [], [], []
    from shapely.geometry import Polygon as _Poly, LineString as _LS
    for poly in land(res):
        if not poly.intersects(band): continue
        g0 = poly.intersection(band)
        for pp in (g0.geoms if hasattr(g0, "geoms") else [g0]):
            if pp.geom_type != "Polygon" or pp.is_empty: continue
            try:
                def _dens(cs):
                    out_ = [cs[0]]
                    for (a1, b1), (a2, b2) in zip(cs, cs[1:]):
                        if abs(a2 - a1) <= 180:
                            k = int(max(abs(a2 - a1), abs(b2 - b1)) // 1.0)
                            for j in range(1, k):
                                t = j / k; out_.append((a1 + (a2 - a1) * t, b1 + (b2 - b1) * t))
                        out_.append((a2, b2))
                    return out_
                ext = [P(*q) for q in _dens(list(pp.exterior.coords))]
                holes = [[P(*q) for q in _dens(list(r.coords))] for r in pp.interiors]
                pg = _Poly(ext, [h for h in holes if len(h) >= 4]).buffer(0)
                pg = pg.intersection(view)
                if not pg.is_empty: projected.append(pg)
            except Exception:
                continue
            # coastline: original rings, skip seams on the antimeridian and the band edge
            for rg in [pp.exterior] + list(pp.interiors):
                c = list(rg.coords); seg = []
                for (lo1, la1), (lo2, la2) in zip(c, c[1:]):
                    seam = (abs(lo1) > 179.9 and abs(lo2) > 179.9) or abs(lo2 - lo1) > 15 or (abs(la1 - latlim) < 1e-6 and abs(la2 - latlim) < 1e-6)
                    if seam:
                        if len(seg) > 1: coast.append(seg)
                        seg = []
                    else:
                        if not seg: seg = [P(lo1, la1)]
                        seg.append(P(lo2, la2))
                if len(seg) > 1: coast.append(seg)
    if projected:
        merged = unary_union(projected).simplify(0.6)
        for q in (merged.geoms if hasattr(merged, "geoms") else [merged]):
            if q.geom_type != "Polygon" or q.is_empty: continue
            for rg in [q.exterior] + list(q.interiors):
                paths.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in rg.coords) + "Z")
    cpaths = []
    for seg in coast:
        ln = _LS(seg).intersection(view)
        for l in (ln.geoms if hasattr(ln, "geoms") else [ln]):
            if l.geom_type == "LineString" and not l.is_empty:
                cpaths.append("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in l.simplify(0.6).coords))
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title or "Polar map of where each diarist stood")}" class="locmap">',
           f'<rect width="{W}" height="{H}" fill="var(--sea)"/>']
    cx, cy = P(0, sgn * 90)
    g = []
    stepl = 5 if rmax < 25 else 10
    for k in range(stepl, int(rmax) + stepl, stepl):
        g.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{k * s_:.1f}" fill="none"/>')
    for lo in range(-180, 180, 30):
        ex, ey = P(lo, sgn * (90 - rmax - 5))
        g.append(f'<path d="M{cx:.1f} {cy:.1f}L{ex:.1f} {ey:.1f}" fill="none"/>')
    out.append(f'<g stroke="var(--rule)" stroke-width=".6" opacity=".7">{"".join(g)}</g>')
    out.append(f'<path d="{"".join(paths)}" fill="var(--land)" stroke="none" fill-rule="evenodd"/>')
    out.append(f'<path d="{"".join(cpaths)}" fill="none" stroke="var(--ink3)" stroke-width=".7" stroke-linejoin="round"/>')
    out.append(f'<g><circle cx="{cx:.1f}" cy="{cy:.1f}" r="4" fill="none" stroke="var(--accent)" stroke-width="1.6"/><path d="M{cx-7:.1f} {cy:.1f}h14M{cx:.1f} {cy-7:.1f}v14" stroke="var(--accent)" stroke-width="1.2"/>'
               f'<text x="{cx + 9:.1f}" y="{cy - 8:.1f}" font-size="11" font-weight="700" fill="var(--accent)" paint-order="stroke" stroke="var(--sea)" stroke-width="3">{"North" if pole == "N" else "South"} Pole</text></g>')
    note = ""
    if off:
        names = []
        for p in off:
            lb = (p.get("label") or "").split(",")[0]
            names.append(f'{p["short"]} ({lb})' if lb else p["short"])
        note = "Beyond this map: " + "; ".join(names)
        if len(note) > 140: note = note[:138] + "…"
    return _overlay(out, pts, P, W, H, wrap=False, note=note)


def _read(name):
    with open(GEO / "dl" / f"{name}.csv", newline="") as f:
        return list(csv.DictReader(f))


def minard_svg():
    troops, cities, temp = _read("Minard.troops"), _read("Minard.cities"), _read("Minard.temp")
    W, H = 900, 520
    lon0, lon1, lat0, lat1 = 23.5, 38.2, 53.8, 55.95
    P = lambda lon, lat: (30 + (float(lon) - lon0) / (lon1 - lon0) * (W - 60), 30 + (lat1 - float(lat)) / (lat1 - lat0) * 280)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Redrawing of Minard\'s 1869 map of the 1812 campaign" class="figsvg">',
           f'<rect width="{W}" height="{H}" fill="var(--sea)"/>']
    maxs = max(int(t["survivors"]) for t in troops)
    # draw segments per group in order: retreat underneath advance? draw advance first then retreat
    for direction, col in (("A", "#d9b98a"), ("R", "var(--ink)")):
        for grp in sorted(set(t["group"] for t in troops)):
            seq = [t for t in troops if t["group"] == grp]
            for a, b in zip(seq, seq[1:]):
                if a["direction"] != direction: continue
                (x0, y0), (x1, y1) = P(a["long"], a["lat"]), P(b["long"], b["lat"])
                w = max(1.2, int(a["survivors"]) / maxs * 46)
                out.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{col}" stroke-width="{w:.1f}" stroke-linecap="round"><title>{"Advancing" if direction=="A" else "Retreating"}: {int(a["survivors"]):,} men</title></line>')
    for c in cities:
        x, y = P(c["long"], c["lat"])
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="var(--accent)"/><text x="{x+4:.1f}" y="{y-5:.1f}" font-size="11" fill="var(--ink)" paint-order="stroke" stroke="var(--sea)" stroke-width="3">{esc(c["city"])}</text>')
    # labels for size
    for t in troops:
        if t["group"] == "1" and t["long"] in ("24", "37.6") and t["direction"] == "A":
            x, y = P(t["long"], t["lat"])
            out.append(f'<text x="{x:.0f}" y="{y-28:.0f}" font-size="11" font-weight="700" fill="var(--ink2)" text-anchor="middle">{int(t["survivors"]):,} men</text>')
    # temperature chart
    ty0 = 360
    out.append(f'<text x="30" y="{ty0-12}" font-size="11.5" font-weight="700" fill="var(--ink2)">Temperature on the retreat (Réaumur; ×1.25 = °C)</text>')
    tp = [(P(t["long"], lat1)[0], ty0 + 10 + (-float(t["temp"])) * 4.2, t) for t in temp]
    for v in (0, -10, -20, -30):
        y = ty0 + 10 + (-v) * 4.2
        out.append(f'<line x1="30" x2="{W-30}" y1="{y:.0f}" y2="{y:.0f}" stroke="var(--rule)"/><text x="{W-28}" y="{y+4:.0f}" font-size="10" fill="var(--ink3)">{v}°</text>')
    out.append('<polyline fill="none" stroke="var(--accent2)" stroke-width="2" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y, _ in tp) + '"/>')
    for x, y, t in tp:
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="var(--accent2)"/><text x="{x:.1f}" y="{y+16:.1f}" font-size="10" text-anchor="middle" fill="var(--ink2)">{esc(t["temp"])}° {esc(t["date"] if t["date"] != "NA" else "")}</text>')
        tx, _ = P(t["long"], lat1)
        out.append(f'<line x1="{tx:.1f}" x2="{tx:.1f}" y1="300" y2="{y:.1f}" stroke="var(--rule)" stroke-dasharray="2 3"/>')
    out.append(f'<text x="{W-8}" y="{H-8}" text-anchor="end" font-size="9.5" fill="var(--ink3)">Redrawn for this book from Minard\'s data (HistData package). Tan = advance, dark = retreat; width = men surviving.</text></svg>')
    return "".join(out)


def snow_svg():
    deaths, pumps, streets = _read("Snow.deaths"), _read("Snow.pumps"), _read("Snow.streets")
    xs = [float(s["x"]) for s in streets]; ys = [float(s["y"]) for s in streets]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    W = 760; H = int(W * (y1 - y0) / (x1 - x0))
    P = lambda x, y: (10 + (float(x) - x0) / (x1 - x0) * (W - 20), 10 + (y1 - float(y)) / (y1 - y0) * (H - 20))
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Redrawing of John Snow\'s 1854 cholera map of Soho" class="figsvg">',
           f'<rect width="{W}" height="{H}" fill="var(--sea)"/>']
    segs = {}
    for s in streets:
        segs.setdefault(s["street"], []).append(P(s["x"], s["y"]))
    d = "".join("M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in pts) for pts in segs.values())
    out.append(f'<path d="{d}" stroke="var(--ink3)" stroke-width="1.4" fill="none" stroke-linecap="round"/>')
    for r in deaths:
        x, y = P(r["x"], r["y"])
        out.append(f'<rect x="{x-1.6:.1f}" y="{y-1.6:.1f}" width="3.2" height="3.2" fill="var(--accent)"/>')
    for p in pumps:
        x, y = P(p["x"], p["y"])
        broad = "Broad" in p["label"]
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7 if broad else 4.5}" fill="{"var(--accent2)" if broad else "var(--card)"}" stroke="var(--accent2)" stroke-width="2"><title>Pump: {esc(p["label"])}</title></circle>')
        if broad:
            out.append(f'<text x="{x+10:.1f}" y="{y-8:.1f}" font-size="12" font-weight="700" fill="var(--ink)" paint-order="stroke" stroke="var(--sea)" stroke-width="3.5">Broad Street pump</text>')
    out.append(f'<text x="{W-8}" y="{H-8}" text-anchor="end" font-size="9.5" fill="var(--ink3)">Redrawn from Snow\'s 1854 data (HistData package): {len(deaths)} deaths (red), {len(pumps)} pumps (blue rings).</text></svg>')
    return "".join(out)


if __name__ == "__main__":
    demo = [{"id": "a", "name": "Pepys", "short": "Pepys", "idx": 0, "lat": 51.51, "lon": -0.08, "label": "London"},
            {"id": "b", "name": "Evelyn", "short": "Evelyn", "idx": 1, "lat": 51.48, "lon": -0.03, "label": "Deptford"},
            {"id": "c", "name": "Mompesson", "short": "Mompesson", "idx": 2, "lat": 53.29, "lon": -1.72, "label": "Eyam"},
            {"id": "d", "name": "Van de Velde", "short": "Van de Velde", "idx": 3, "lat": 53.36, "lon": 5.22, "label": "Terschelling",
             "waypoints": [{"lat": 52.37, "lon": 4.9, "label": "Amsterdam"}, {"lat": 53.36, "lon": 5.22, "label": "Vlie"}]}]
    out = GEO / "test.html"
    out.write_text("<style>:root{--sea:#ece3d1;--land:#f8f2e6;--rule:#d8ccb6;--ink:#2b2420;--ink2:#5b4f45;--ink3:#857565;--card:#fff;--eyeS:52%;--eyeL:40%;--accent:#8a2f1d;--accent2:#2f5d62}svg{width:800px;display:block;margin:10px}</style>"
                   + locator_svg(demo) + minard_svg() + snow_svg())
    print("ok", out)
