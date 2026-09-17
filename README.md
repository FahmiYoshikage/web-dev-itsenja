# ITSENJA Web Development — Central Learning Hub & Interactive Slide Deck

Pusat materi pembelajaran, slide presentasi interaktif, live code playground, dan studi kasus proyek web development bootcamp **ITSENJA**.

Platform ini dapat dijalankan dengan mudah secara publik dan terisolasi menggunakan **Docker Compose**.

---

## Struktur Kurikulum & Modul Sprint

| Sprint | Topik Utama | Format & Akses | Status |
| :--- | :--- | :--- | :---: |
| **Sprint 01** | **Fundamental HTML5 & Semantic Web Structure**<br>• Anatomi dokumen HTML5, Heading Hierarchy, Teks<br>• Media Gambar, Hyperlink, Lists, Tabel Data, Form Input | [Slide Presentasi](Sprint-01/slide.html) · [Proyek Portofolio](Sprint-01/index.html) | Selesai |
| **Sprint 02** | **CSS3 & Modern Responsive Web Design**<br>• The Box Model, Tipografi Google Fonts, Warna HSL<br>• Modern Layout: Flexbox & CSS Grid, Media Queries | [Slide Presentasi](Sprint-02/slide.html) · [Proyek Portofolio](Sprint-02/index.html) | Selesai |
| **Sprint 03** | **JavaScript DOM & Web Interactivity**<br>• Variabel, Fungsi, Logika Pemrograman<br>• Event Handling, Manipulasi DOM (`querySelector`) | [Slide Presentasi](Sprint-03/index.html) | Selesai |
| **Sprint 04** | **Modern JS, Asynchronous & Fetch API**<br>• REST API, Status Code HTTP, JSON Data Parsing<br>• Promise Lifecycle, Async/Await, Error Handling & Live Search App | [Slide Presentasi](Sprint-04/index.html) | Selesai |
| **Sprint 05** | **Git, GitHub & Deployment Workflow**<br>• Arsitektur 3-Stage Git, Conventional Commits, Feature Branching<br>• Resolusi Merge Conflict, Pull Request di GitHub, Auto Deploy Pages/Vercel | [Slide Teori](Sprint-05/index.html) · [Praktikum Interaktif](Sprint-05/praktikum.html) | Aktif |
| **Sprint 06+** | **Backend Integration & Fullstack Basics** (Roadmap Selanjutnya) | Coming Soon | Roadmap |

---

## Menjalankan dengan Docker Compose (Sangat Mudah)

### 1. Jalankan Container
Pastikan Docker dan Docker Compose sudah terpasang di komputer/server kamu, lalu jalankan:

```bash
docker compose up -d
```

### 2. Akses Platform
Buka browser dan kunjungi:
- **Pusat Belajar (Central Hub):** [http://localhost:8080](http://localhost:8080)
- **Sprint 01 (HTML5):** [http://localhost:8080/Sprint-01/slide.html](http://localhost:8080/Sprint-01/slide.html)
- **Sprint 02 (CSS3):** [http://localhost:8080/Sprint-02/slide.html](http://localhost:8080/Sprint-02/slide.html)
- **Sprint 03 (JavaScript DOM):** [http://localhost:8080/Sprint-03/](http://localhost:8080/Sprint-03/)
- **Sprint 04 (Async & Fetch API):** [http://localhost:8080/Sprint-04/](http://localhost:8080/Sprint-04/)
- **Sprint 05 (Git & Deployment):** [http://localhost:8080/Sprint-05/](http://localhost:8080/Sprint-05/)

### 3. Mengubah Port (Opsional)
Jika ingin menggunakan port lain (misal port `3000` atau `80`), kamu bisa menjalankannya dengan variabel `PORT`:

```bash
PORT=3000 docker compose up -d
```

### 4. Menghentikan Container
```bash
docker compose down
```

---

## Fitur Utama Platform

- **Interactive Code Playground (HTML, CSS, JS):** Setiap slide dilengkapi dengan 3 tab editor yang dapat diubah dan dijalankan secara instan tanpa software tambahan.
- **Pencarian Topik Real-Time:** Filter materi di Pusat Belajar dengan kata kunci (misal: `flexbox`, `fetch`, `grid`, `table`).
- **Clean & Modern Aesthetic:** Bebas emoji berlebihan, menggunakan tipografi *Plus Jakarta Sans* dan *Fira Code*, layout fullscreen responsif.
- **Hot-Reload Development:** Volume mapping pada `docker-compose.yml` memastikan perubahan file HTML/CSS langsung ter-update tanpa perlu rebuild container.

---

## Tautan Evaluasi & Feedback

- **Kuis Pemahaman Materi (MCQ):** [https://s.id/MKb5O](https://s.id/MKb5O)
- **Survei Evaluasi Cara Mengajar Mentor:** [https://s.id/dqeBo](https://s.id/dqeBo)

---
© 2026 **ITSENJA Web Development** · Fahmi Ilham Bagaskara
