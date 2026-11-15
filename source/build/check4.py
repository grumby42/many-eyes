import sys, asyncio
from playwright.async_api import async_playwright
async def main(path, outdir):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w, scheme in ((1280, "light"), (390, "dark")):
            pg = await b.new_page(viewport={"width": w, "height": 900}, color_scheme=scheme)
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append("console:" + m.text) if m.type == "error" else None)
            await pg.goto("file://" + path); await pg.wait_for_timeout(900)
            r = await pg.evaluate("""() => ({sections: document.querySelectorAll('section.chapter').length,
              entries: document.querySelectorAll('.entry').length, ledgers: document.querySelectorAll('table.ledger').length,
              ledgerRows: document.querySelectorAll('table.ledger tbody tr').length,
              undef: (document.body.innerText.match(/undefined|NaN|\\[object/g)||[]).length,
              overflow: document.documentElement.scrollWidth - innerWidth,
              maps: document.querySelectorAll('section.chapter svg .mapdot').length,
              imgs: document.querySelectorAll('img').length, broken: [...document.querySelectorAll('img')].filter(i=>i.complete&&!i.naturalWidth).length})""")
            print(w, scheme, r, "errors:", errs or "none")
            await pg.evaluate("document.documentElement.style.scrollBehavior='auto'")
            for cid in [x for x in (await pg.evaluate("[...document.querySelectorAll('section.chapter')].slice(0,2).map(s=>s.id)"))]:
                await pg.evaluate(f"document.getElementById('{cid}').scrollIntoView()"); await pg.wait_for_timeout(500)
                await pg.screenshot(path=f"{outdir}/{w}-{cid}.png")
            await pg.evaluate("(document.querySelector('table.ledger')||document.body).scrollIntoView()"); await pg.wait_for_timeout(400)
            await pg.screenshot(path=f"{outdir}/{w}-ledger.png")
            await pg.close()
        await b.close()
asyncio.run(main(sys.argv[1], sys.argv[2]))
