"""Validate generated HTML links, anchors, images and the expected lab pages.

Run after `python -m mkdocs build --strict`. Uses only Python's standard library.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.images = path, set(), [], []
        self.h1_count = 0
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.h1_count += 1
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)


root = Path(sys.argv[1] if len(sys.argv) > 1 else "site").resolve()
pages = {path.resolve(): Page(path) for path in root.rglob("*.html")}
errors = []
checked_links = checked_images = 0
expected = ["index.html"] + [f"tasks/{name}/index.html" for name in (
    "01-access-the-lab", "02-control-hub", "03-configure-ai-receptionist",
    "04-intent-based-routing", "05-webex-app", "06-verify-ai-receptionist",
)]
for name in expected:
    if root / name not in pages:
        errors.append(f"Missing page: {name}")
    elif pages[root / name].h1_count != 1:
        errors.append(f"{name}: expected exactly one page title (h1)")
for path, page in pages.items():
    # 404 navigation may use absolute production URLs and is checked by MkDocs.
    if path.name == "404.html":
        continue
    for url in page.links + [img.get("src", "") for img in page.images]:
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc:
            continue
        if not parsed.path:
            target = path
        elif parsed.path.startswith("/"):
            # Theme-generated absolute URLs can include the project Pages prefix.
            parts = unquote(parsed.path).lstrip("/")
            target = root / parts
            if not target.exists() and "/" in parts:
                target = root / parts.split("/", 1)[1]
        else:
            target = (path.parent / unquote(parsed.path)).resolve()
        if target.is_dir():
            target /= "index.html"
        if not target.exists():
            errors.append(f"{path.relative_to(root)}: missing {url}")
        elif parsed.fragment and target in pages:
            anchor = unquote(parsed.fragment)
            if anchor not in pages[target].ids:
                errors.append(f"{path.relative_to(root)}: missing anchor {url}")
        checked_links += 1
    for img in page.images:
        if not img.get("alt", "").strip():
            errors.append(f"{path.relative_to(root)}: image has no alt text: {img.get('src')}")
        checked_images += 1
if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print(f"PASS: {len(expected)} lab pages; {checked_links} local links/anchors; {checked_images} image references.")
