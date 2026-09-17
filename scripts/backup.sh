#!/usr/bin/env bash
# scripts/backup.sh
# Creates an automated, timestamped, compressed backup archive of the entire web portal.

set -e

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKUP_DIR="${BASE_DIR}/backups"
TIMESTAMP="$(date +'%Y%m%d_%H%M%S')"
BACKUP_NAME="backup_itsenja_webdev_${TIMESTAMP}.tar.gz"
ARCHIVE_PATH="${BACKUP_DIR}/${BACKUP_NAME}"
CHECKSUM_PATH="${BACKUP_DIR}/${BACKUP_NAME}.sha256"

mkdir -p "${BACKUP_DIR}"

echo "=================================================="
echo "📦 Memulai Pencadangan (Backup) Portal ITSENJA..."
echo "Direktori Proyek : ${BASE_DIR}"
echo "Target Arsip     : ${ARCHIVE_PATH}"
echo "=================================================="

tar --exclude='.git' \
    --exclude='node_modules' \
    --exclude='backups' \
    --exclude='*.tar.gz' \
    --exclude='*.zip' \
    --exclude='__pycache__' \
    --exclude='.DS_Store' \
    -czf "${ARCHIVE_PATH}" -C "${BASE_DIR}" .

# Hitung checksum SHA-256 untuk integritas data
sha256sum "${ARCHIVE_PATH}" | awk '{print $1}' > "${CHECKSUM_PATH}"

FILE_SIZE="$(du -h "${ARCHIVE_PATH}" | cut -f1)"
CHECKSUM_VAL="$(cat "${CHECKSUM_PATH}")"

echo "✅ Backup Berhasil Dibuat!"
echo "• Nama File : ${BACKUP_NAME}"
echo "• Ukuran    : ${FILE_SIZE}"
echo "• SHA-256   : ${CHECKSUM_VAL}"
echo "• Lokasi    : ${ARCHIVE_PATH}"
echo "=================================================="
