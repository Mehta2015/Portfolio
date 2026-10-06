#!/usr/bin/env python3
"""Check every external link in index.html. Run on your own computer: python3 check-links.py
Needs Python 3.8+ and nothing else. Anything not marked OK needs a look."""
import re, urllib.request, urllib.error, html, concurrent.futures as cf

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
src = open("index.html", encoding="utf-8").read()
links = sorted({html.unescape(u) for u in re.findall(r'href="(https?://[^"]+)"', src)})
skip = ("fonts.googleapis", "fonts.gstatic", "keyurmehta.in")

def check(url):
    if any(s in url for s in skip):
        return url, "SKIP", ""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read(200000).decode("utf-8", "ignore")
            final = r.geturl()
            # Google Play and the App Store sometimes return 200 with a "not found" page
            if "play.google.com" in url and ("We're sorry, the requested URL was not found" in body or "id=" not in final):
                return url, "GONE", "Play Store says the app isn't available"
            if "apps.apple.com" in url and ("This app is currently not available" in body or "/app/" not in final):
                return url, "GONE", "App Store listing unavailable in this region or removed"
            return url, "OK", str(r.status)
    except urllib.error.HTTPError as e:
        return url, "GONE" if e.code in (404, 410) else "CHECK", f"HTTP {e.code}"
    except Exception as e:
        return url, "CHECK", type(e).__name__

with cf.ThreadPoolExecutor(8) as ex:
    results = list(ex.map(check, links))

bad = [r for r in results if r[1] not in ("OK", "SKIP")]
for url, status, note in results:
    if status != "SKIP":
        print(f"{status:5}  {url}  {note}")
print(f"\n{len(results)} links checked, {len(bad)} need attention.")
