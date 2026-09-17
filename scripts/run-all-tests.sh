#!/usr/bin/env bash
set -e

echo "=================================================="
echo "🛡️  ITSENJA WEB DEV — FULL SAFETYNET & E2E SUITE"
echo "=================================================="
echo ""

echo "▶ 1. Audit Internal Links & Assets..."
python3 scripts/check-links.py
echo ""

echo "▶ 2. Audit Indexing & Technical SEO..."
python3 scripts/check-indexing.py
echo ""

echo "▶ 3. Menjalankan Unit & Structural Safetynet Tests..."
pytest tests/test_unit_safetynet.py -v
echo ""

echo "▶ 4. Menjalankan End-to-End (E2E) Browser Tests (Selenium Headless Chrome)..."
pytest tests/test_e2e_safetynet.py -v
echo ""

echo "=================================================="
echo "✅ SEMUA TEST SUITE SAFETYNET & E2E LULUS 100%!"
echo "=================================================="
