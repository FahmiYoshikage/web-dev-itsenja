# Sprint 05: Git, GitHub & Modern Deployment Workflow
**ITSENJA Web Development Bootcamp**

Modul pembelajaran komprehensif Version Control System (VCS), arsitektur Git, Conventional Commits, strategi branching & pull request kolaboratif di GitHub, resolusi merge conflict, hingga deployment website otomatis ke GitHub Pages dan Vercel.

---

## 📂 Struktur Modul Sprint 05

```
Sprint-05/
├── index.html                  # Slide presentasi teori interaktif fullscreen (20 Slide + Simulator)
├── praktikum.html              # Slide workshop praktikum interaktif hands-on (12 Slide + Lab Live)
├── slide.html                  # Alias / backup slide presentasi
├── README.md                   # Dokumentasi kurikulum & panduan modul
└── latihan-git/                # Template proyek praktikum mandiri
    ├── index.html              # Starter website portofolio modern
    ├── style.css               # Desain responsif & dark mode tokens
    ├── app.js                  # Interaktivitas JavaScript & event logic
    └── .gitignore              # Standar aturan ignore file sensitif/cache
```

---

## 🎯 Pokok Bahasan & Silabus Materi

1. **Konsep Dasar Version Control System (VCS)**
   - Perbedaan pengelolaan kode manual vs Snapshot-based VCS.
   - Manfaat time-travel, audit jejak baris kode, dan kolaborasi tanpa tumpang tindih.

2. **Arsitektur 3 Wilayah Git (The Three Stages)**
   - Working Directory, Staging Area (Index), dan Git Local Repository.
   - Siklus 4 status file: Untracked, Unmodified, Modified, dan Staged.

3. **Setup & Konfigurasi Esensial**
   - Penyiapan identitas global (`user.name`, `user.email`).
   - Konfigurasi default branch `main`.
   - Setup autentikasi GitHub (SSH Key & Personal Access Token).

4. **Siklus Fundamental: Init, Status, Add, Commit**
   - Anatomi folder `.git/`.
   - Perbedaan `git add <file>` vs `git add .`.
   - Filosofi Atomic Commit & Standar Industri **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, `chore:`).

5. **Inspeksi Jejak Riwayat & Perubahan**
   - Navigasi riwayat dengan `git log`, `--oneline`, `--graph`.
   - Pemeriksaan baris perubahan dengan `git diff` dan `git diff --staged`.

6. **Manajemen File Sensitif (.gitignore Best Practices)**
   - Mencegah kebocoran `.env`, credentials, dan folder berat `node_modules/`.
   - Cara melepaskan file yang terlanjur ter-track (`git rm --cached`).

7. **Time Travel & Pembatalan Aman**
   - Mengembalikan file yang belum di-stage (`git restore`).
   - Mengeluarkan file dari staging (`git restore --staged`).
   - Menambal commit terakhir (`git commit --amend`).
   - Pembatalan publik aman (`git revert`) vs manipulasi riwayat (`git reset --soft/mixed/hard`).

8. **Strategi Percabangan (Branching Workflow)**
   - Mengapa dilarang coding langsung di branch `main`.
   - Pola Feature Branching: `feature/*`, `bugfix/*`, `hotfix/*`.
   - Perintah `git branch`, `git checkout -b`, `git switch -c`.

9. **Penggabungan Cabang & Resolusi Merge Conflict**
   - Fast-Forward vs 3-Way Merge Commit.
   - Anatomi penanda konflik (`<<<<<<< HEAD`, `=======`, `>>>>>>>`).
   - Langkah sistematis menyelesaikan konflik tanpa merusak kode rekan tim.

10. **Git Stash**
    - Menyimpan perubahan yang belum siap di-commit untuk beralih konteks darurat.

11. **Kolaborasi Remote di GitHub**
    - Menghubungkan lokal ke remote (`git remote add origin`).
    - Sinkronisasi via `git push -u origin main` dan `git pull`.
    - Alur kerja tim: Forking, Branching, Pull Request (PR), dan Inline Code Review.

12. **Deployment Workflow (Go Live!)**
    - Deployment statis instan via GitHub Pages.
    - Continuous Deployment otomatis via Vercel / Netlify setiap `git push`.

---

## 💻 Cara Mengakses

- **Akses Langsung di Browser:** Buka file [index.html](index.html) pada browser.
- **Akses via Docker Hub Platform:** Kunjungi [http://localhost:8080/Sprint-05/](http://localhost:8080/Sprint-05/).
- **Navigasi Keyboard:** Gunakan tombol panah `[←]` dan `[→]` atau `[Spasi]` untuk berpindah slide.
