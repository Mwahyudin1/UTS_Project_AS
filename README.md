# Automation Systems UTS Project: Online Book Catalog Scraper

Proyek otomatisasi sistem menggunakan Python untuk melakukan *web scraping* data buku digital dari Project Gutenberg, membersihkan data teks menggunakan *Regular Expressions*, menyimpannya ke dalam format CSV terstruktur, serta membuat arsip *backup* secara otomatis.

---

* **Nama:** Dean Pratama Saputra
* **Nim:** 312210114
* **Kelas:** I231E
* **Nama:** Mochamad Wahyudin Ardiansyah
* **Nim:** 312210148
* **Kelas:** I231E
* **Mata Kuliah:** Automation Systems
* **Dosen Pengampu:** Anggi Muhammad Rifa’i, M.Kom

---

## 📂 Struktur Folder Proyek
- `main.py` : Script utama program (All-in-One automation)
- `data/` : Menyimpan file data mentah (`raw_data.txt`)
- `output/` : Menyimpan file hasil akhir CSV (`hasil_scraping.csv`) dan laporan ringkas (`laporan.txt`)
- `backup/` : Menyimpan file arsip cadangan otomatis (`backup_data.zip`)
- `requirements.txt` : Daftar pustaka/library yang dibutuhkan

## 🛠️ Fitur & Penerapan Materi Kuliah
1. **Pathlib & File Management (Chapter 10):** Pembuatan direktori folder otomatis (`data`, `output`, `backup`).
2. **Web Scraping (Chapter 13):** Menggunakan `requests` dan `BeautifulSoup` untuk mengambil data dari web secara dinamis.
3. **Regular Expressions / Regex (Chapter 9):** Penyaringan dan pembersihan karakter teks judul buku.
4. **CSV Handling (Chapter 12):** Penyimpanan data terstruktur berformat CSV dengan pemisah titik koma (`;`).
5. **Exception Handling:** Mencegah terjadinya *crash* pada program saat terjadi gangguan koneksi atau file.
6. **ZipFile Archiving (Chapter 11):** Pengarsipan otomatis seluruh hasil kerja ke dalam format ZIP.

## 🚀 Cara Instalasi & Menjalankan Program
1. Pastikan Python sudah terinstal di komputer Anda.
2. Install *library* yang dibutuhkan melalui terminal dengan perintah:
   ```bash
   pip install -r requirements.txt
3. Menjalankan Program Utama
- Jalankan file script utama dengan mengetikkan perintah berikut di terminal:
  ```bash
  python main.py
4. Hasil Program Saat Perintah python main.py dieksekusi:
- Program akan berjalan secara otomatis dari proses pengambilan data web, pembersihan teks (Regex), hingga penyimpanan file.
- Folder `data/` akan berisi file teks mentah (`raw_data.txt`).
- Folder `output/` akan berisi file data bersih (`hasil_scraping.csv`) dan laporan ringkas (`laporan.txt`).
- Folder `backup/` akan otomatis menghasilkan file arsip (`backup_data.zip`).
- Jika seluruh rangkaian proses berjalan lancar tanpa kendala, terminal akan menampilkan pesan sukses:
  ```bash
  [SUCCESS] Seluruh rangkaian otomatisasi program selesai dengan sempurna!
