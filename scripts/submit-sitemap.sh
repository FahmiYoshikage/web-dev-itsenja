#!/usr/bin/env bash
# scripts/submit-sitemap.sh
# Ping Search Engines (Google, Bing) to notify updated sitemap.xml

DOMAIN="${1:-https://itsenja.com}"
SITEMAP_URL="${DOMAIN}/sitemap.xml"

echo "=================================================="
echo "🚀 ITSENJA Search Engine Sitemap Submission"
echo "=================================================="
echo "Target Sitemap URL: ${SITEMAP_URL}"
echo ""

# 1. Google Search Console Ping
echo "📡 Pinging Google Search Console..."
GOOGLE_PING="https://www.google.com/ping?sitemap=${SITEMAP_URL}"
curl -s -o /dev/null -w "HTTP Status Google: %{http_code}\n" "${GOOGLE_PING}" || echo "Note: Ping request finished."

# 2. Bing Webmaster Ping
echo "📡 Pinging Bing Webmaster Tools..."
BING_PING="https://www.bing.com/ping?sitemap=${SITEMAP_URL}"
curl -s -o /dev/null -w "HTTP Status Bing: %{http_code}\n" "${BING_PING}" || echo "Note: Ping request finished."

echo ""
echo "✅ Petunjuk Submit Manual Google Search Console:"
echo "1. Buka https://search.google.com/search-console"
echo "2. Pilih properti domain web kamu."
echo "3. Klik menu 'Sitemaps' di sidebar kiri."
echo "4. Masukkan 'sitemap.xml' pada kolom Tambahkan Peta Situs baru, lalu klik Kirim."
echo "5. Status sitemap akan berubah menjadi 'Berhasil' dalam beberapa menit."
echo "=================================================="
