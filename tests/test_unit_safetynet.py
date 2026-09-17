import os
import re
import json
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALL_CRITICAL_FILES = [
    "index.html",
    "404.html",
    "sitemap.xml",
    "robots.txt",
    "Sprint-01/slide.html",
    "Sprint-01/index.html",
    "Sprint-02/slide.html",
    "Sprint-02/index.html",
    "Sprint-03/index.html",
    "Sprint-03/slide.html",
    "Sprint-04/index.html",
    "Sprint-04/slide.html",
    "Sprint-05/index.html",
    "Sprint-05/slide.html",
    "Sprint-05/praktikum.html",
    "Sprint-05/latihan-git/index.html",
]

SLIDE_DECKS = [
    "Sprint-01/slide.html",
    "Sprint-02/slide.html",
    "Sprint-03/index.html",
    "Sprint-03/slide.html",
    "Sprint-04/index.html",
    "Sprint-04/slide.html",
    "Sprint-05/index.html",
    "Sprint-05/slide.html",
    "Sprint-05/praktikum.html",
]


def test_critical_files_exist():
    """Ensure all required project and curriculum files are present on disk."""
    for rel_path in ALL_CRITICAL_FILES:
        full_path = os.path.join(PROJECT_ROOT, rel_path)
        assert os.path.exists(full_path), f"Critical file missing: {rel_path}"
        assert os.path.getsize(full_path) > 0, f"Critical file is empty: {rel_path}"


def test_html_syntax_and_doctypes():
    """Ensure every HTML file has DOCTYPE, proper lang attribute, charset, and viewport."""
    html_files = [f for f in ALL_CRITICAL_FILES if f.endswith(".html")]
    for rel_path in html_files:
        full_path = os.path.join(PROJECT_ROOT, rel_path)
        with open(full_path, "r", encoding="utf-8") as fp:
            content = fp.read()

        assert "<!doctype html" in content.lower() or "<!DOCTYPE html" in content, (
            f"Missing DOCTYPE in {rel_path}"
        )

        soup = BeautifulSoup(content, "html.parser")
        html_tag = soup.find("html")
        assert html_tag is not None, f"Missing <html> tag in {rel_path}"
        assert html_tag.get("lang") in ["id", "en"], (
            f"Invalid or missing lang in {rel_path}: {html_tag.get('lang')}"
        )

        meta_charset = soup.find("meta", charset=True)
        assert meta_charset is not None and meta_charset["charset"].lower() == "utf-8", (
            f"Missing UTF-8 charset in {rel_path}"
        )

        meta_viewport = soup.find("meta", attrs={"name": "viewport"})
        assert meta_viewport is not None and "width=device-width" in meta_viewport.get("content", ""), (
            f"Missing responsive viewport meta in {rel_path}"
        )

        assert soup.title is not None and len(soup.title.text.strip()) > 5, (
            f"Missing or too short title in {rel_path}"
        )


def test_slide_deck_design_system_consistency():
    """
    Ensure every interactive slide deck adheres to the standardized design system:
    - Google Fonts: Plus Jakarta Sans & Fira Code
    - Font Awesome 6 Icons
    - Bottom .navigation-bar with Hub link, Prev/Next buttons, and Progress bar
    - Each slide has .header-bar, .badge-tag, and .slide-counter
    """
    for rel_path in SLIDE_DECKS:
        full_path = os.path.join(PROJECT_ROOT, rel_path)
        with open(full_path, "r", encoding="utf-8") as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")

        # 1. Fonts check
        font_links = [l["href"] for l in soup.find_all("link", rel="stylesheet") if "fonts.googleapis.com" in l.get("href", "")]
        assert len(font_links) > 0, f"Missing Google Fonts link in {rel_path}"
        assert any("Plus+Jakarta+Sans" in l or "Plus Jakarta Sans" in l for l in font_links), (
            f"Missing Plus Jakarta Sans font in {rel_path}"
        )
        assert any("Fira+Code" in l or "Fira Code" in l for l in font_links), (
            f"Missing Fira Code font in {rel_path}"
        )

        # 2. Font Awesome check
        fa_links = [l for l in soup.find_all("link", rel="stylesheet") if "font-awesome" in l.get("href", "")]
        assert len(fa_links) > 0, f"Missing Font Awesome in {rel_path}"

        # 3. Bottom Navigation Bar check
        nav_bar = soup.find(class_="navigation-bar")
        assert nav_bar is not None, f"Missing .navigation-bar in {rel_path}"

        nav_hub = nav_bar.find(class_="nav-hub-link")
        assert nav_hub is not None, f"Missing .nav-hub-link in {rel_path} navigation bar"
        assert "Pusat Belajar" in nav_hub.text, f".nav-hub-link text invalid in {rel_path}"

        prev_btn = nav_bar.find(id="prev-btn")
        next_btn = nav_bar.find(id="next-btn")
        assert prev_btn is not None and next_btn is not None, (
            f"Missing #prev-btn or #next-btn in {rel_path}"
        )

        progress_bar = nav_bar.find(id="progress-bar")
        assert progress_bar is not None, f"Missing #progress-bar in {rel_path}"

        # 4. Slide content & header bar check
        slides = soup.find_all("section", class_="slide")
        assert len(slides) >= 10, f"Expected at least 10 slides in {rel_path}, found {len(slides)}"

        active_slides = [s for s in slides if "active" in s.get("class", [])]
        assert len(active_slides) == 1, (
            f"Expected exactly 1 initial active slide in {rel_path}, found {len(active_slides)}"
        )

        for idx, slide in enumerate(slides, start=1):
            header_bar = slide.find(class_="header-bar")
            assert header_bar is not None, (
                f"Slide {idx} in {rel_path} is missing .header-bar"
            )
            badge_tag = header_bar.find(class_="badge-tag")
            assert badge_tag is not None, (
                f"Slide {idx} in {rel_path} is missing .badge-tag in .header-bar"
            )
            slide_counter = header_bar.find(class_="slide-counter")
            assert slide_counter is not None, (
                f"Slide {idx} in {rel_path} is missing .slide-counter in .header-bar"
            )


def test_favicons_across_all_pages():
    """Ensure all primary pages include SVG, ICO fallback, and Apple touch icon."""
    pages = [
        "index.html",
        "404.html",
        "Sprint-01/slide.html",
        "Sprint-01/index.html",
        "Sprint-02/slide.html",
        "Sprint-02/index.html",
        "Sprint-03/index.html",
        "Sprint-03/slide.html",
        "Sprint-04/index.html",
        "Sprint-04/slide.html",
        "Sprint-05/index.html",
        "Sprint-05/slide.html",
        "Sprint-05/praktikum.html",
        "Sprint-05/latihan-git/index.html",
    ]
    for rel_path in pages:
        full_path = os.path.join(PROJECT_ROOT, rel_path)
        with open(full_path, "r", encoding="utf-8") as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")

        icons = soup.find_all("link", rel=lambda r: r and "icon" in r)
        assert len(icons) >= 2, (
            f"Insufficient favicon tags in {rel_path}. Found: {len(icons)}"
        )

        svg_icon = soup.find("link", rel="icon", type="image/svg+xml")
        assert svg_icon is not None, f"Missing SVG favicon in {rel_path}"


def test_sitemap_xml_integrity():
    """Ensure sitemap.xml is valid, uses schema 0.9, and covers all sprint pages."""
    sitemap_path = os.path.join(PROJECT_ROOT, "sitemap.xml")
    assert os.path.exists(sitemap_path), "sitemap.xml does not exist"

    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Namespace handling
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = root.findall("sm:url", ns)
    assert len(urls) >= 11, f"Expected at least 11 registered URLs in sitemap, found {len(urls)}"

    locs = [u.find("sm:loc", ns).text for u in urls if u.find("sm:loc", ns) is not None]
    
    expected_endpoints = [
        "https://itsenja.com/",
        "https://itsenja.com/Sprint-01/slide.html",
        "https://itsenja.com/Sprint-02/slide.html",
        "https://itsenja.com/Sprint-03/",
        "https://itsenja.com/Sprint-04/",
        "https://itsenja.com/Sprint-05/",
        "https://itsenja.com/Sprint-05/praktikum.html",
        "https://itsenja.com/404.html",
    ]

    for expected in expected_endpoints:
        assert any(expected == loc or expected in loc for loc in locs), (
            f"Endpoint {expected} missing in sitemap.xml"
        )


def test_robots_txt_spec():
    """Ensure robots.txt has proper User-agent, Allow, and Sitemap directives."""
    robots_path = os.path.join(PROJECT_ROOT, "robots.txt")
    with open(robots_path, "r", encoding="utf-8") as fp:
        content = fp.read()

    assert "User-agent: *" in content, "Missing User-agent: * in robots.txt"
    assert "Allow: /" in content, "Missing Allow: / in robots.txt"
    assert "Sitemap: https://itsenja.com/sitemap.xml" in content, (
        "Missing or incorrect Sitemap directive in robots.txt"
    )


def test_structured_data_schemas():
    """Ensure index.html contains valid Organization, BreadcrumbList, and Course schemas."""
    index_path = os.path.join(PROJECT_ROOT, "index.html")
    with open(index_path, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")

    scripts = soup.find_all("script", type="application/ld+json")
    assert len(scripts) >= 1, f"Expected at least 1 JSON-LD script, found {len(scripts)}"

    schema_types = set()
    for s in scripts:
        try:
            data = json.loads(s.string)
            if "@graph" in data:
                for item in data["@graph"]:
                    schema_types.add(item.get("@type"))
                    if item.get("@type") == "ItemList":
                        for sub in item.get("itemListElement", []):
                            schema_types.add(sub.get("@type"))
            else:
                schema_types.add(data.get("@type"))
        except json.JSONDecodeError as err:
            pytest.fail(f"Invalid JSON-LD schema syntax: {err}")

    assert any(t in schema_types for t in ["EducationalOrganization", "Organization"]), (
        "Organization schema missing in index.html"
    )
    assert "BreadcrumbList" in schema_types, "BreadcrumbList schema missing in index.html"
    assert "Course" in schema_types, "Course schema missing in index.html"


def test_antispam_honeypot_spec():
    """Ensure contact form contains the anti-spam honeypot input."""
    index_path = os.path.join(PROJECT_ROOT, "index.html")
    with open(index_path, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")

    hp_input = soup.find("input", attrs={"name": "website_url_trap"}) or soup.find(id="hp_website")
    assert hp_input is not None, "Honeypot input ('website_url_trap' / 'hp_website') missing in contact form"
    
    parent = hp_input.find_parent(class_=re.compile(r"honeypot|antispam|hp-field|hp-trap"))
    assert parent is not None, "Honeypot input must be wrapped in a hidden container (e.g. .hp-trap)"
    assert parent.get("aria-hidden") == "true" or "display: none" in parent.get("style", ""), (
        "Honeypot container must have aria-hidden='true' or hidden styling"
    )


def test_cta_and_wa_tracking_attributes():
    """Ensure CTA tracking attributes and WhatsApp tracking are configured in index.html."""
    index_path = os.path.join(PROJECT_ROOT, "index.html")
    with open(index_path, "r", encoding="utf-8") as fp:
        soup = BeautifulSoup(fp.read(), "html.parser")

    wa_btn = soup.find(attrs={"data-track": "whatsapp"})
    assert wa_btn is not None, "Floating WhatsApp button missing data-track='whatsapp'"

    cta_elements = soup.find_all(attrs={"data-track": "cta"})
    assert len(cta_elements) >= 5, (
        f"Expected at least 5 CTA tracked buttons, found {len(cta_elements)}"
    )

    # All CTA buttons must have data-cta-name
    for cta in cta_elements:
        assert cta.get("data-cta-name"), f"CTA element missing data-cta-name: {cta}"


def test_zero_broken_internal_links():
    """Check every local link and asset in all HTML files to ensure 0 broken links."""
    html_files = [f for f in ALL_CRITICAL_FILES if f.endswith(".html")]

    for rel_path in html_files:
        full_path = os.path.join(PROJECT_ROOT, rel_path)
        base_dir = os.path.dirname(full_path)

        with open(full_path, "r", encoding="utf-8") as fp:
            soup = BeautifulSoup(fp.read(), "html.parser")

        # Check all <a href="...">
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith(("#", "javascript:", "mailto:", "tel:", "http://", "https://")):
                continue

            clean_href = href.split("#")[0].split("?")[0]
            if not clean_href:
                continue

            if clean_href.startswith("/"):
                target = os.path.join(PROJECT_ROOT, clean_href.lstrip("/"))
            else:
                target = os.path.join(base_dir, clean_href)

            target = unquote(target)
            if os.path.isdir(target):
                index_target = os.path.join(target, "index.html")
                assert os.path.exists(index_target), (
                    f"Broken link in {rel_path}: {href} -> missing index.html in directory"
                )
            else:
                assert os.path.exists(target), (
                    f"Broken link in {rel_path}: href '{href}' points to missing file '{target}'"
                )

        # Check all <img src="..."> and <script src="...">
        for tag in soup.find_all(["img", "script"], src=True):
            src = tag["src"].strip()
            if not src or src.startswith(("http://", "https://", "data:")):
                continue

            clean_src = src.split("#")[0].split("?")[0]
            if not clean_src:
                continue

            if clean_src.startswith("/"):
                target = os.path.join(PROJECT_ROOT, clean_src.lstrip("/"))
            else:
                target = os.path.join(base_dir, clean_src)

            target = unquote(target)
            assert os.path.exists(target), (
                f"Broken asset in {rel_path}: src '{src}' points to missing file '{target}'"
            )
