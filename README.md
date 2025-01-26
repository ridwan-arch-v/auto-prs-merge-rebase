# Git PR & Tag Tools

Alat ini adalah skrip Python yang mempermudah pengelolaan git repository dengan membuat branch, melakukan commit, membuat tag, membuat Pull Request (PR), melakukan merge PR otomatis, serta melakukan rebase pada branch utama (`main`) setelah merge. Skrip ini memanfaatkan GitHub CLI (`gh`) dan alat-alat Git untuk mengotomatiskan tugas-tugas git yang biasa dilakukan dalam alur kerja pengembangan perangkat lunak.

## Fitur Utama

- **Membuat Branch**: Membuat dan beralih ke branch baru.
- **Commit Otomatis**: Melakukan commit ke branch dengan pesan yang diberikan.
- **Tagging Otomatis**: Membuat tag baru dan memberi pesan commit untuk tag tersebut.
- **Push Branch dan Tag**: Mendorong branch dan tag yang baru dibuat ke GitHub.
- **Buat Pull Request**: Secara otomatis membuat Pull Request (PR) dari branch baru ke branch utama (`main`).
- **Auto-Merge PR**: Setelah PR dibuat, skrip akan mencoba untuk menggabungkan PR secara otomatis.
- **Auto-Rebase**: Setelah menggabungkan PR, skrip akan melakukan rebase pada branch `main` untuk memastikan branch tersebut selalu terkini dengan perubahan terbaru.

## Persyaratan

Untuk menjalankan skrip ini, Anda harus memastikan beberapa alat dan konfigurasi berikut sudah terpasang:

- **Python 3.x**: Pastikan Anda telah menginstal Python 3.6 atau lebih baru.
- **Git**: Pastikan Git sudah terinstal dan dapat diakses dari terminal/command prompt.
- **GitHub CLI (`gh`)**: GitHub CLI digunakan untuk berinteraksi dengan GitHub dan membuat Pull Request serta melakukan merge secara otomatis.
  - [Instalasi GitHub CLI](https://cli.github.com/)
- **Autentikasi GitHub CLI**: Anda perlu melakukan login menggunakan GitHub CLI untuk berinteraksi dengan GitHub.
  ```bash
  gh auth login
  ```

## Cara Menggunakan

Ikuti langkah-langkah berikut untuk menggunakan alat ini:

1. **Clone Repository**:
   - Clone repository Anda atau buat repository baru di GitHub.
   - Pastikan Anda sudah berada di dalam direktori kerja proyek.

2. **Install GitHub CLI**:
   - Jika belum menginstal GitHub CLI, Anda bisa mengunduh dan menginstalnya dari [sini](https://cli.github.com/).
   - Login ke akun GitHub Anda menggunakan perintah berikut:
     ```bash
     gh auth login
     ```

3. **Jalankan Skrip Python**:
   - Setelah GitHub CLI terinstal dan sudah login, jalankan skrip Python dengan perintah:
     ```bash
     python main.py
     ```

4. **Masukkan Input**:
   - Skrip ini akan meminta beberapa input dari Anda di terminal:
     - **Nama Branch**: Nama branch baru yang akan dibuat.
     - **Pesan Commit**: Pesan untuk commit pertama Anda di branch tersebut.
     - **Nama Tag**: Nama tag yang akan dibuat.
     - **Pesan Commit untuk Tag**: Pesan untuk commit tag tersebut.

5. **Proses Otomatis**:
   - Skrip ini akan otomatis menjalankan serangkaian perintah git, yaitu:
     - Membuat dan berpindah ke branch baru.
     - Melakukan commit dan tag.
     - Mem-push branch dan tag ke GitHub.
     - Membuat Pull Request (PR) ke branch utama (`main`).
     - Menggabungkan PR secara otomatis menggunakan `--merge`.
     - Melakukan rebase pada branch `main` agar selalu up-to-date dengan perubahan terbaru.

6. **Cek Hasilnya**:
   - Setelah menjalankan skrip, Anda bisa melihat hasilnya di GitHub:
     - Pull Request yang dibuat akan muncul di repository GitHub Anda.
     - Branch dan tag yang baru dibuat akan terdaftar di GitHub.

## Contoh Output

Berikut adalah contoh alur proses yang terjadi saat menjalankan skrip:

```bash
Masukkan nama branch: test/1.0.7
Masukkan pesan commit: test vol 7
Masukkan nama tag: 1.0.7
Masukkan pesan commit untuk tag: 07
Switched to a new branch 'test/1.0.7'
Commit berhasil dengan pesan: test vol 7
Tag 1.0.7 telah dibuat.
Branch test/1.0.7 dan tag 1.0.7 telah dipush ke GitHub.
Pull Request telah dibuat dari test/1.0.7 ke main.
PR test/1.0.7 berhasil digabungkan ke main.
Perubahan terbaru dari branch main berhasil di-fetch.
Branch main berhasil di-rebase dengan perubahan terbaru dari GitHub.
```

## Troubleshooting

Jika Anda menemui masalah, pastikan bahwa:

- Anda telah terautentikasi dengan GitHub CLI menggunakan `gh auth login`.
- Anda menjalankan perintah di dalam direktori proyek yang merupakan git repository yang valid (ada `.git` folder di dalamnya).
- Pastikan Git dan GitHub CLI sudah terinstal dengan benar dan dapat diakses di terminal.

Jika ada error atau kesalahan lainnya, Anda bisa melihat log output yang disediakan oleh skrip di terminal untuk informasi lebih lanjut.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, Anda bisa melakukan fork, membuat perubahan, dan mengajukan Pull Request. Semua kontribusi akan sangat dihargai!

## Lisensi

Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

**Catatan:** Pastikan Anda menggunakan alat ini dengan hati-hati di proyek yang sudah ada, terutama saat melakukan merge otomatis dan rebase. Sebaiknya diuji terlebih dahulu di repository testing atau branch terpisah sebelum diterapkan ke proyek utama.
