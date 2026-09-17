#!/usr/bin/env python3
"""
scripts/check-indexing.py
Audits SEO, Indexing, Meta Tags, Canonical URLs, and Schema.org Structured Data.
"""

import os
import re
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def audit_indexing():
    print("🚀 Memulai Audit Indexing & Technical SEO...")
    issues = []

    # 1. Check sitemap.xml
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        issues.append("❌ sitemap.xml tidak ditemukan!")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            urls = root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
            print(f"  ✓ sitemap.xml valid dengan {len(urls)} URL terdaftar.")
        except Exception as e:
            issues.append(f"❌ sitemap.xml tidak valid XML: {e}")

    # 2. Check robots.txt
    robots_path = os.path.join(BASE_DIR, 'robots.txt')
    if not os.path.exists(robots_path):
        issues.append("❌ robots.txt tidak ditemukan!")
    else:
        with open(robots_path, 'r', encoding='utf-8') as f:
            robots_content = f.read()
        if 'Sitemap:' in robots_content and 'User-agent:' in robots_content:
            print("  ✓ robots.txt valid dan merujuk ke sitemap.xml.")
        else:
            issues.append("⚠️ robots.txt tidak memuat deklarasi Sitemap atau User-agent!")

    # 3. Check index.html SEO & Metadata
    index_path = os.path.join(BASE_DIR, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    checks = [
        ('Canonical URL', r'<link\s+rel=["\']canonical["\']'),
        ('Meta Robots', r'<meta\s+name=["\']robots["\']'),
        ('Google Search Console', r'<meta\s+name=["\']google-site-verification["\']'),
        ('Favicon Vector (SVG)', r'<link\s+rel=["\']icon["\']\s+type=["\']image/svg\+xml["\']'),
        ('Favicon Fallback (ICO)', r'<link\s+rel=["\']alternate icon["\']'),
        ('Apple Touch Icon', r'<link\s+rel=["\']apple-touch-icon["\']'),
        ('Open Graph Title', r'<meta\s+property=["\']og:title["\']'),
        ('Organization Schema', r'"@type":\s*"EducationalOrganization"'),
        ('BreadcrumbList Schema', r'"@type":\s*"BreadcrumbList"'),
        ('Course Schema', r'"@type":\s*"Course"'),
        ('Floating WhatsApp Tracker', r'data-track="whatsapp"'),
        ('CTA Click Tracker', r'data-track="cta"'),
        ('Anti-Spam Honeypot Trap', r'name="website_url_trap"')
    ]

    for name, pattern in checks:
        if re.search(pattern, html, re.IGNORECASE):
            print(f"  ✓ {name}: Terdeteksi & Terpasang.")
        else:
            issues.append(f"❌ {name}: TIDAK ditemukan pada index.html!")

    print("\n--- HASIL AUDIT INDEXING ---")
    if issues:
        for err in issues:
            print(err)
        return False
    else:
        print("✅ 100% AUDIT INDEXING & TECHNICAL SEO LULUS SEMPURNA!")
        return True

if __name__ == '__main__':
    audit_indexing()
