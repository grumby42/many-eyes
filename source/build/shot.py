import sys, asyncio
from playwright.async_api import async_playwright
async def main(path, out, width=1280, anchor=None):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": int(width), "height": 900})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append("console:" + m.text) if m.type == "error" else None)
        await pg.goto("file://" + path)
        await pg.wait_for_timeout(800)
        if anchor:
            await pg.evaluate(f"document.documentElement.style.scrollBehavior='auto';document.getElementById('{anchor}').scrollIntoView()")
            await pg.wait_for_timeout(1200)
        await pg.screenshot(path=out)
        print("errors:", errs or "none")
        print("sections:", await pg.evaluate("document.querySelectorAll('section.chapter').length"),
              "entries:", await pg.evaluate("document.querySelectorAll('.entry').length"))
        await b.close()
a = sys.argv[1:]
asyncio.run(main(a[0], a[1], a[2] if len(a) > 2 else 1280, a[3] if len(a) > 3 else None))
