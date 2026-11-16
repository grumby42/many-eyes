"""Stage the Many Eyes GitHub Pages site: copies each built volume and writes index.html + README.md.
Usage: python3 site.py <out_dir> <utc_stamp>
"""
import json, pathlib, re, shutil, sys, html

OUT = pathlib.Path(sys.argv[1]); STAMP = sys.argv[2]
SRC = pathlib.Path("/home/claude")
VOLS = [("I", "many-eyes.html", "Diaries Across History"), ("II", "many-eyes-volume-2.html", "Diaries Across History, continued"),
        ("III", "many-eyes-volume-3.html", "Edges of the Map"), ("IV", "many-eyes-volume-4.html", "The Notebook"),
        ("V", "many-eyes-volume-5.html", "The Studio"), ("VI", "many-eyes-volume-6.html", "The Room"),
        ("VII", "many-eyes-volume-7.html", "Getting There"), ("VIII", "many-eyes-volume-8.html", "The Same Sky"), ("IX", "many-eyes-volume-9.html", "The Ward"), ("X", "many-eyes-volume-10.html", "The Return Gaze"), ("XI", "many-eyes-volume-11.html", "The Courtroom"), ("XIII", "many-eyes-volume-13.html", "Signals"), ("XIV", "many-eyes-volume-14.html", "The Assay"), ("XV", "many-eyes-volume-15.html", "Hidden Worlds")]
OUT.mkdir(parents=True, exist_ok=True)
cards, rows = [], []
for num, fn, name in VOLS:
    p = SRC / fn
    if not p.exists():
        cards.append(f'<li class="vol soon"><span class="num">{num}</span><div><h2>{html.escape(name)}</h2><p class="sub">In preparation.</p></div></li>')
        continue
    s = p.read_text(encoding="utf-8")
    d = json.loads(re.search(r'<script id="book-data" type="application/json">(.*?)</script>', s, re.S).group(1))
    build = re.search(r'BUILD = "([^"]+)"', s).group(1)
    m = d.get("meta") or {}
    title = m["volume"].split("·")[-1].strip() if "·" in (m.get("volume") or "") else name
    sub = m.get("sub") or "Real diaries, letters and dated records from many vantage points, laid side by side."
    chs = d["chapters"]
    eyes = sum(len(c["eyes"]) for c in chs); ents = sum(len(c["entries"]) for c in chs)
    toc = " · ".join(html.escape(c.get("short_title") or c["title"]) for c in chs)
    shutil.copy2(p, OUT / fn)
    mb = p.stat().st_size / 1e6
    cards.append(f'''<li class="vol"><span class="num">{num}</span><div>
<h2><a href="{fn}">{html.escape(title)}</a></h2><p class="sub">{html.escape(sub)}</p>
<p class="toc">{toc}</p>
<p class="meta">{len(chs)} chapters · {eyes} eyes · {ents} dated entries · {mb:.1f} MB · build <code>{build}</code></p></div></li>''')
    rows.append(f"| {num} | [{title}]({fn}) | {len(chs)} | {eyes} | {ents} | `{build}` |")

comp = SRC / "many-eyes-companion.html"
compcard = ""
if comp.exists():
    shutil.copy2(comp, OUT / comp.name)
    compcard = f'''<li class="vol"><span class="num">∞</span><div><h2><a href="{comp.name}">The Long Chains · Companion</a></h2><p class="sub">The whole series as one web: chains of linked events across centuries and volumes, a chain explorer, every chapter on one timeline, dates shared between chapters, on this day, and an index of every eye.</p><p class="meta">Open it alongside the volumes; its links open each volume at the right chapter.</p></div></li>'''
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Many Eyes</title><meta name="description" content="A synoptic reader of history: real diaries, letters and dated records from many vantage points, laid side by side.">
<style>
:root{{--bg:#f5efe4;--card:#fbf7ef;--ink:#2a2420;--ink2:#5a5048;--ink3:#8a7d70;--rule:#e2d6c3;--acc:#9a6a2a}}
@media (prefers-color-scheme:dark){{:root{{--bg:#1c1915;--card:#25211c;--ink:#ece4d6;--ink2:#c3b8a6;--ink3:#93887a;--rule:#3a342c;--acc:#d7a65e}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Georgia,"Iowan Old Style",serif}}
main{{max-width:880px;margin:0 auto;padding:48px 16px 64px}}
.kicker{{font:600 12px/1 system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--acc)}}
h1{{font-size:clamp(40px,8vw,64px);margin:.2em 0 .1em;letter-spacing:-.01em}}
.lede{{color:var(--ink2);font-size:19px;max-width:40em}}
ol{{list-style:none;padding:0;margin:40px 0 0}}
.vol{{display:grid;grid-template-columns:56px 1fr;gap:16px;padding:22px 0;border-top:1px solid var(--rule)}}
.num{{font-size:30px;color:var(--acc);line-height:1.1}}
h2{{margin:0 0 4px;font-size:24px}}h2 a{{color:inherit;text-decoration:none;border-bottom:1px solid var(--rule)}}h2 a:hover{{border-color:var(--acc)}}
.sub{{margin:0 0 6px;color:var(--ink2)}}.toc{{margin:0 0 6px;font-size:15px;color:var(--ink2)}}
.meta{{margin:0;font:13px/1.5 system-ui,sans-serif;color:var(--ink3)}}code{{font-size:12px}}
.soon h2{{color:var(--ink3)}}
.note{{margin-top:40px;padding-top:18px;border-top:1px solid var(--rule);font:14px/1.6 system-ui,sans-serif;color:var(--ink3)}}
</style></head><body><main>
<p class="kicker">A synoptic reader</p><h1>Many Eyes</h1>
<p class="lede">Each chapter takes one event and lays real diaries, letters, notebooks, minutes and dated records from many people side by side on a shared timeline: who saw what, where, and on which day. Every volume is a single offline HTML file; open it in any browser, or save it for reading without a connection.</p>
<ol>{compcard}{"".join(cards)}</ol>
<p class="note">All sources are real. Entries are digests in the editors' words; short quotations appear only from English texts published before 1929, world-famous phrases and official United States records. Images are public domain. Contested questions are presented as positions with their evidence, not verdicts. Compiled by Ted Gransbury with Claude. Text licensed CC BY 4.0; code MIT. Site generated {STAMP}.</p>
</main></body></html>'''
(OUT / "index.html").write_text(page, encoding="utf-8")
readme = f"""# Many Eyes

A synoptic reader of history. Each chapter takes one event and lays real, authentic diaries, letters, notebooks, minutes and dated records from many vantage points side by side on a shared timeline, with maps, convergences (days several witnesses recorded), ties between witnesses, threads between chapters and volumes, and public-domain images.

Each volume is one self-contained offline HTML file. Read online via GitHub Pages, or download a file and open it in any browser.

| Vol | Title | Chapters | Eyes | Entries | Build |
|---|---|---|---|---|---|
{chr(10).join(rows)}

**Sourcing rules.** All sources are real. Entries are digests; quotations are short and limited to English texts published before 1929, world-famous phrases and official US records. Memoirs written later, forgeries and legends are flagged. Contested questions are given as positions with evidence. Each volume was checked by independent fact-check passes before publication.

Compiled by Ted Gransbury with Claude. Generated {STAMP}.

**Licence.** Book text: CC BY 4.0 (see `LICENSE-CONTENT.md`). Build scripts: MIT (see `LICENSE`). Quotations and images are public domain or short quotations for commentary, and keep their own status.
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")
(OUT / ".nojekyll").write_text("")
print("staged", len(rows), "volumes in", OUT)
