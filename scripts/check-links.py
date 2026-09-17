#!/usr/bin/env python3
"""
scripts/check-links.py
Audits all active internal links across the ITSENJA web development repository to guarantee 0 broken links.
"""

import os
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ActiveLinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_code = False
        self.code_tags = {'textarea', 'pre', 'code', 'script'}

    def handle_starttag(self, tag, attrs):
        if tag in self.code_tags:
            self.in_code = True
            return

        if not self.in_code:
            for attr, val in attrs:
                if attr in ('href', 'src') and val:
                    self.links.append((tag, attr, val))

    def handle_endtag(self, tag):
        if tag in self.code_tags:
            self.in_code = False

def check_internal_links():
    html_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        if any(x in root for x in ['.git', 'node_modules', 'backups', 'tes']):
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))

    print(f"🔍 Memeriksa link pada {len(html_files)} file HTML aktif...")
    broken_links = []
    total_links_checked = 0

    for file_path in html_files:
        rel_html = os.path.relpath(file_path, BASE_DIR)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        parser = ActiveLinkExtractor()
        try:
            parser.feed(content)
        except Exception:
            pass

        for tag, attr, link in parser.links:
            # Ignore external, anchor, mailto, tel, javascript, template strings
            if not link or link.startswith('#') or link.startswith('http://') or link.startswith('https://') or \
               link.startswith('mailto:') or link.startswith('tel:') or link.startswith('javascript:') or \
               link.startswith('data:') or '${' in link or link == '...':
                continue

            total_links_checked += 1
            clean_link = link.split('?')[0].split('#')[0]
            if not clean_link:
                continue

            # Handle absolute root paths (e.g. /favicon.svg)
            if clean_link.startswith('/'):
                target_path = os.path.normpath(os.path.join(BASE_DIR, clean_link.lstrip('/')))
            else:
                target_path = os.path.normpath(os.path.join(os.path.dirname(file_path), clean_link))

            # Directory check
            if os.path.isdir(target_path):
                index_target = os.path.join(target_path, 'index.html')
                if not os.path.exists(index_target):
                    broken_links.append((rel_html, link, target_path))
            elif not os.path.exists(target_path):
                broken_links.append((rel_html, link, target_path))

    print(f"📊 Total internal link diperiksa: {total_links_checked}")
    if broken_links:
        print(f"❌ Ditemukan {len(broken_links)} broken link:")
        for source, link, target in broken_links:
            print(f"  • Sumber: {source} -> Link: '{link}' (Target tidak ada: {target})")
        return False
    else:
        print("✅ SEMUA internal link valid! (0 broken links)")
        return True

if __name__ == '__main__':
    check_internal_links()
