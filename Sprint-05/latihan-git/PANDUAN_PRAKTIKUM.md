# Panduan Praktikum Mandiri: Git, GitHub & Modern Deployment Workflow
**ITSENJA Web Development Bootcamp — Sprint 05**

Selamat datang di modul praktikum hands-on Git! Melalui panduan ini, kamu akan mempraktikkan seluruh materi Sprint 05 dari inisialisasi repositori lokal hingga website kamu dapat diakses secara publik di internet melalui GitHub Pages / Vercel.

---

## 🎯 Target Pembelajaran
1. Mengonfigurasi identitas Git global di komputer lokal.
2. Menginisialisasi repositori Git dan memahami siklus 3-Stage (Working Directory -> Staging Area -> Local Repo).
3. Mengaplikasikan format pesan commit standar **Conventional Commits**.
4. Melindungi kredensial rahasia dengan `.gitignore`.
5. Menerapkan **Feature Branching Strategy** (membuat branch, commit fitur terisolasi, dan merge).
6. Mengunggah repositori ke **GitHub** (Remote Repository).
7. Melakukan deployment gratis ke internet via **GitHub Pages** atau **Vercel**.

---

## 📋 Langkah Demi Langkah (Step-by-Step Lab)

### Tahap 1: Setup Identitas Git
Buka terminal (Git Bash, Terminal macOS/Linux, atau PowerShell) dan jalankan:
```bash
git config --global user.name "Nama Lengkap Kamu"
git config --global user.email "email.kamu@example.com"
git config --global init.defaultBranch main
```
Periksa hasil konfigurasi:
```bash
git config --list
```

---

### Tahap 2: Inisialisasi Repositori Lokal
Masuk ke folder proyek latihan ini (`Sprint-05/latihan-git`):
```bash
cd Sprint-05/latihan-git
git init
```
Periksa status direktori:
```bash
git status
```
*File `index.html`, `style.css`, `app.js`, dan `.gitignore` akan berstatus warna merah (Untracked Files).*

---

### Tahap 3: Staging & Initial Commit (Conventional Commits)
Masukkan semua file ke Staging Area:
```bash
git add .
git status
```
*Semua file sekarang berubah menjadi hijau (Changes to be committed).*

Buat commit pertama dengan standar Conventional Commits:
```bash
git commit -m "feat: initialize responsive web portfolio starter"
```

Cek riwayat commit:
```bash
git log --oneline
```

---

### Tahap 4: Mengembangkan Fitur dengan Branching
Jangan pernah melakukan perubahan fitur eksperimen langsung di branch `main`. Buat branch baru untuk menambahkan kartu proyek Sprint 03:

```bash
git switch -c feature/add-sprint03-card
```

Buka file `index.html` dan tambahkan kartu baru di dalam `#projectsList`:
```html
<article class="project-card">
  <div class="project-header">
    <span class="project-sprint">Sprint 03</span>
    <span class="project-badge">JavaScript DOM</span>
  </div>
  <h3>Interaktivitas Web & Event Handling</h3>
  <p>Manipulasi elemen DOM secara dinamis, event listeners klik mouse, kalkulator interaktif, dan validasi form.</p>
</article>
```

Simpan file, lalu periksa perbedaannya:
```bash
git diff
git add index.html
git commit -m "feat(projects): add sprint 03 javascript dom project card"
```

---

### Tahap 5: Menggabungkan Branch ke Main (Merge)
Pindah kembali ke branch utama:
```bash
git switch main
```
Gabungkan perubahan dari branch fitur:
```bash
git merge feature/add-sprint03-card
```
*Git akan melakukan Fast-Forward Merge karena tidak ada commit lain di branch main.*

Hapus branch fitur lokal yang sudah selesai:
```bash
git branch -d feature/add-sprint03-card
```

---

### Tahap 6: Menghubungkan ke GitHub Remote
1. Buka [GitHub](https://github.com) dan login ke akunmu.
2. Buat repositori baru bernama `web-portfolio-bootcamp` (biarkan kosong, **jangan centang** Initialize with README).
3. Hubungkan repositori lokal ke GitHub:
```bash
git remote add origin https://github.com/USERNAME_KAMU/web-portfolio-bootcamp.git
git branch -M main
git push -u origin main
```
*Refresh halaman GitHub-mu, seluruh kode dan riwayat commit sudah tersimpan aman di cloud!*

---

### Tahap 7: Deployment Gratis ke Internet

#### Opsi A: Menggunakan GitHub Pages (Hanya 1 Menit)
1. Di halaman repositori GitHub-mu, klik tab **Settings** (ikon gerigi di atas).
2. Di menu sidebar kiri, pilih menu **Pages**.
3. Di bagian **Build and deployment > Source**, pilih `Deploy from a branch`.
4. Di bagian **Branch**, pilih `main` dan folder `/ (root)`, lalu klik tombol **Save**.
5. Tunggu sekitar 1–2 menit, refresh halaman. GitHub akan memberikan link publik websitemu:
   `https://USERNAME_KAMU.github.io/web-portfolio-bootcamp/`

#### Opsi B: Menggunakan Vercel (Auto Continuous Deployment)
1. Kunjungi [vercel.com](https://vercel.com) dan login dengan akun GitHub.
2. Klik tombol **Add New... > Project**.
3. Pilih repositori `web-portfolio-bootcamp` dan klik **Import**.
4. Biarkan konfigurasi default, lalu klik **Deploy**.
5. Websitemu langsung live dengan sertifikat SSL gratis! Setiap kali kamu menjalankan `git push`, Vercel akan otomatis meng-update website dalam hitungan detik.

---

## 🏆 Checklist Penyelesaian Praktikum
- [ ] Berhasil mengonfigurasi `user.name` dan `user.email` di Git.
- [ ] Memahami status file melalui `git status` dan membaca riwayat via `git log`.
- [ ] Menulis pesan commit dengan format `feat:`, `fix:`, atau `docs:`.
- [ ] Berhasil membuat branch terpisah dan melakukan merge ke `main`.
- [ ] Repositori ter-push ke GitHub tanpa file-file terlarang (`.env`, `node_modules`).
- [ ] Website berhasil diakses secara publik melalui internet!
