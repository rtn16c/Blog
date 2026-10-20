"""
Generates sitemap.xml by scanning all HTML files in the repo.
Priority rules:
  1.0  - index.html (root)
  0.8  - top-level pages and section index pages (e.g. mainframe/index.html)
  0.6  - posts and other sub-pages
Excludes: post-template.html, anything inside .github/
"""

import os
from datetime import date

BASE_URL = "https://return16.com"
OUTPUT = "sitemap.xml"

EXCLUDE_FILES = {"post-template.html"}
EXCLUDE_DIRS  = {".github", ".git"}


def get_priority(rel_path: str) -> str:
    parts = rel_path.strip("/").split("/")
    if rel_path == "index.html":
        return "1.0"
    # section index pages e.g. mainframe/index.html
    if len(parts) == 2 and parts[-1] == "index.html":
        return "0.8"
    # top-level pages e.g. about.html
    if len(parts) == 1:
        return "0.8"
    # everything deeper (posts, flashcards, etc.)
    return "0.6"


def get_changefreq(priority: str) -> str:
    return "weekly" if priority in ("1.0", "0.8") else "monthly"


def url_for(rel_path: str) -> str:
    # Turn index.html into trailing slash for clean URLs
    if rel_path.endswith("/index.html"):
        rel_path = rel_path[: -len("index.html")]
    elif rel_path == "index.html":
        return BASE_URL + "/"
    return BASE_URL + "/" + rel_path


def collect_html_files(root: str):
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune excluded directories in-place
        dirnames[:] = [
            d for d in dirnames if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        for filename in filenames:
            if not filename.endswith(".html"):
                continue
            if filename in EXCLUDE_FILES:
                continue
            abs_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(abs_path, root).replace("\\", "/")
            entries.append(rel_path)
    entries.sort()
    return entries


def build_sitemap(files):
    today = date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        "",
    ]
    for rel_path in files:
        priority   = get_priority(rel_path)
        changefreq = get_changefreq(priority)
        loc        = url_for(rel_path)
        lines += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{today}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
            "",
        ]
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = collect_html_files(repo_root)
    xml = build_sitemap(files)
    output_path = os.path.join(repo_root, OUTPUT)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote {len(files)} URLs to {OUTPUT}")
    for f in files:
        print(f"  {f}")
