"""Capture public, anonymous views of the actual published projects."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

targets = {
    "ritmo": ("https://meuritmo.net", ("meu ritmo",)),
    "mobile": ("https://meuritmo.net/app", ("meu ritmo", "android")),
    "imovance": ("https://imovel-em-dia-portfolio.vercel.app", ("imovance", "imóvel", "imovel")),
    "doc": ("https://portfolio-suite-jv.vercel.app/doc", ("doc intelligence",)),
    "flow": ("https://portfolio-suite-jv.vercel.app/flow", ("flowengine",)),
    "pulse": ("https://portfolio-suite-jv.vercel.app/pulse", ("pulse monitor",)),
    "freight": ("https://portfolio-suite-jv.vercel.app/freight", ("freight connect",)),
    "api": ("https://portfolio-suite-jv.vercel.app/api", ("api studio",)),
}
output = Path("screenshots")
output.mkdir(exist_ok=True)
results = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--disable-dev-shm-usage"])
    for name, (url, markers) in targets.items():
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1,
                                      locale="pt-BR", color_scheme="dark",
                                      reduced_motion="reduce", accept_downloads=False)
        page = context.new_page()
        try:
            response = page.goto(url, wait_until="domcontentloaded", timeout=45000)
            if not response or response.status >= 400:
                raise RuntimeError("HTTP error")
            page.wait_for_timeout(2200)
            body = page.locator("body").inner_text(timeout=10000).lower()
            title = page.title().lower()
            if not any(m in body or m in title for m in markers):
                raise RuntimeError("Project identity not found")
            if ("vercel authentication" in body or "deployment protection" in body or
                    "access denied" in body or len(body.strip()) < 80):
                raise RuntimeError("Blocked or incomplete page")
            page.screenshot(path=str(output / (name + ".jpg")), type="jpeg",
                            quality=80, animations="disabled", timeout=15000)
            results.append({"id": name, "url": url, "status": "captured", "title": page.title()})
        except Exception as error:
            results.append({"id": name, "url": url, "status": "unavailable", "reason": str(error)[:160]})
        finally:
            context.close()
    browser.close()
(output / "manifest.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(results, ensure_ascii=False))
if not any(r["status"] == "captured" for r in results):
    raise SystemExit("No screenshot could be captured")
