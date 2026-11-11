import os
import re
import csv
import shutil
from pathlib import Path
from zipfile import ZipFile
import requests
from bs4 import BeautifulSoup

print("=== PROGRAM AUTOMATION SYSTEMS: UTS PROJECT (ALL-IN-ONE) ===")

# ==========================================
# 1. MATERI: PATHLIB & FILE MANAGEMENT
# ==========================================
try:
    current_dir = Path.cwd()
    data_dir = current_dir / "data"
    output_dir = current_dir / "output"
    backup_dir = current_dir / "backup"

    # Membuat folder secara otomatis menggunakan Pathlib
    data_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    backup_dir.mkdir(exist_ok=True)
    print("[INFO] (Chapter 10) Struktur folder proyek berhasil disiapkan secara otomatis.")
except Exception as e:
    print(f"[ERROR] Gagal membuat direktori: {e}")

# ==========================================
# 2. MATERI: WEB SCRAPING (REQUESTS & BS4)
# ==========================================
url = "https://www.gutenberg.org/browse/scores/top"
print(f"[INFO] (Chapter 13) Mengakses target web: {url}")

try:
    # Exception handling untuk koneksi web
    response = requests.get(url, timeout=10)
    response.raise_for_status() # Cek apakah sukses (status code 200)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    book_elements = soup.select('ol li a') 
    print(f"[INFO] Berhasil menemukan {len(book_elements)} data mentah dari web.")

    processed_data = []
    raw_texts = []
    
    # ==========================================
    # 3. MATERI: REGULAR EXPRESSIONS (REGEX) & STRING PROCESSING
    # ==========================================
    # Pola regex untuk mendeteksi karakter huruf/kata yang valid pada judul
    title_pattern = re.compile(r'^[A-Za-z0-9\s,\-\:\.\!\?]+$')

    counter = 1
    for tag in book_elements[:25]: # Batasi 25 data teratas agar rapi
        raw_title = tag.text.strip()
        
        if raw_title:
            # Penerapan Regular Expressions untuk menyaring/membersihkan teks judul
            # Memastikan teks sesuai format standar atau membersihkan karakter aneh
            clean_match = title_pattern.search(raw_title)
            
            if clean_match:
                clean_title = clean_match.group()
            else:
                # Jika ada karakter khusus di luar regex, bersihkan secara manual
                clean_title = re.sub(r'[^\w\s,\-\:\.]', '', raw_title)

            kategori = "Classic Literature"
            status = "Free / Public Domain"
            
            # Menyimpan data yang sudah diproses
            processed_data.append([clean_title, kategori, status])
            raw_texts.append(f"No. {counter} | Judul: {clean_title} | Kategori: {kategori}\n")
            counter += 1

    # Simpan data mentah ke folder data/
    raw_file_path = data_dir / "raw_data.txt"
    with open(raw_file_path, "w", encoding="utf-8") as raw_file:
        raw_file.writelines(raw_texts)
    print(f"[INFO] (Chapter 9/10) Data mentah disimpan ke: {raw_file_path}")

    # ==========================================
    # 4. MATERI: CSV FILE HANDLING (WRITING DATA)
    # ==========================================
    output_csv_path = output_dir / "hasil_scraping.csv"
    with open(output_csv_path, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.writer(csv_file, delimiter=';') # Pemisah titik koma agar rapi di Excel
        writer.writerow(["Judul Buku", "Kategori", "Status Lisensi"])
        writer.writerows(processed_data)
    print(f"[INFO] (Chapter 10/12) Data terstruktur berhasil disimpan ke CSV: {output_csv_path}")

    # Membuat file laporan teks ringkas
    report_path = output_dir / "laporan.txt"
    with open(report_path, "w", encoding="utf-8") as rep:
        rep.write("=== LAPORAN AUTOMATION SYSTEMS UTS ===\n")
        rep.write(f"Total Buku Berhasil Diproses: {len(processed_data)} data.\n")
        rep.write("Status: Sukses diekstrak menggunakan BeautifulSoup & Regex.\n")

    # ==========================================
    # 5. MATERI: ZIPFILE ARCHIVING & BACKUP
    # ==========================================
    backup_zip_path = backup_dir / "backup_data.zip"
    print(f"[INFO] (Chapter 11) Membuat arsip backup ZIP di: {backup_zip_path}")
    
    with ZipFile(backup_zip_path, 'w') as backup_zip:
        for file_path in output_dir.iterdir():
            if file_path.is_file():
                backup_zip.write(file_path, arcname=file_path.name)
                
    print("[SUCCESS] Seluruh rangkaian otomatisasi program selesai dengan sempurna!")

except requests.exceptions.RequestException as e:
    print(f"[ERROR] Terjadi kesalahan jaringan saat mengakses web: {e}")
except Exception as e:
    print(f"[ERROR] Terjadi kesalahan tak terduga pada program: {e}")