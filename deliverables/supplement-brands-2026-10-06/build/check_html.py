"""Render-check the presentation with headless Chromium (Playwright)."""
import os, sys, glob
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
HTML = "file://" + os.path.join(os.path.dirname(HERE), "supplement-brands-2026-10-06.html")
SHOTS = os.path.join(HERE, "_shots"); os.makedirs(SHOTS, exist_ok=True)
exe = glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")[0]
sizes = [("laptop", 1440, 900), ("projector", 1024, 768), ("phone", 390, 844)]
problems = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=exe)
    for name, w, h in sizes:
        pg = b.new_page(viewport={"width": w, "height": h})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else (problems.append("external request " + r.request.url), r.abort()))
        pg.goto(HTML); pg.wait_for_timeout(300)
        n = pg.evaluate("document.querySelectorAll('.slide').length")
        for i in range(n):
            pg.evaluate(f"go({i})"); pg.wait_for_timeout(320)
            info = pg.evaluate("""() => {const s=document.querySelector('.slide.active');
              return {sh:s.scrollHeight, ch:s.clientHeight, docw:document.documentElement.scrollWidth, vw:innerWidth,
                      empty:[...s.querySelectorAll('.chart')].filter(c=>!c.querySelector('svg rect,svg circle')).length}}""")
            if info["docw"] > info["vw"] + 1: problems.append(f"{name} slide {i+1}: horizontal overflow {info['docw']}>{info['vw']}")
            if info["empty"]: problems.append(f"{name} slide {i+1}: empty chart")
            if name != "phone" and info["sh"] > info["ch"] + 4: problems.append(f"{name} slide {i+1}: needs vertical scroll ({info['sh']} > {info['ch']})")
            pg.screenshot(path=os.path.join(SHOTS, f"{name}-{i+1:02d}.png"))
        if errs: problems.append(f"{name}: JS errors {errs}")
        pg.close()
    # interaction checks on laptop
    pg = b.new_page(viewport={"width": 1440, "height": 900}); pg.goto(HTML + "#1")
    pg.keyboard.press("ArrowRight"); assert pg.evaluate("cur") == 1, "arrow key"
    pg.click("#next"); assert pg.evaluate("cur") == 2, "next button"
    pg.click("#prev"); assert pg.evaluate("cur") == 1, "back button"
    pg.click("#menuBtn"); pg.click("#menu button:nth-child(6)"); assert pg.evaluate("cur") == 5, "menu"
    pg.evaluate("go(1)"); pg.click("#s2 .kf >> nth=0"); assert pg.get_attribute("#s2 .kf >> nth=0", "aria-expanded") == "true", "expand"
    pg.evaluate("go(2)"); pg.click("#scTabs button[data-k='1']"); pg.wait_for_timeout(100)
    pg.hover("#scView svg g[data-tip] >> nth=2"); pg.wait_for_timeout(100)
    assert pg.is_visible("#tip"), "hover tip"; pg.screenshot(path=os.path.join(SHOTS, "x-hover.png"))
    pg.evaluate("go(5)"); pg.click("#s6 .ms >> nth=3"); txt = pg.inner_text("#tlDetail"); assert "Whole Foods" in txt or "2021" in txt, txt
    pg.click("#tlTabs button[data-k='vg']"); pg.wait_for_timeout(100); pg.screenshot(path=os.path.join(SHOTS, "x-timeline-vg.png"))
    pg.evaluate("go(7)"); pg.click("#chg th.colsel >> nth=6"); dim = pg.evaluate("document.querySelectorAll('#chg tr.dim').length"); assert dim == 4, dim
    pg.click("#chg tbody tr >> nth=3"); assert "Sephora" in pg.inner_text("#seqView")
    pg.screenshot(path=os.path.join(SHOTS, "x-channels.png"))
    pg.evaluate("go(8)"); pg.click("#s9 [data-p='W2']"); assert "class actions" in pg.inner_text("#sdDetail")
    pg.click("#sdTabs button[data-k='matrix']"); pg.wait_for_timeout(100); pg.screenshot(path=os.path.join(SHOTS, "x-matrix.png"))
    b.close()
print("\n".join(problems) if problems else "no problems found")
