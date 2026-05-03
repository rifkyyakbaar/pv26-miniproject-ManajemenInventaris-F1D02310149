# PV26 Mini Project - Inventaris

Aplikasi manajemen inventaris menggunakan PySide6, SQLite, dan QSS eksternal.

## Fitur

- Input barang dengan 5 field: Kode Barang, Nama Barang, Kategori, Jumlah, Harga
- Tampilan data dengan `QTableWidget`
- Simpan data ke SQLite secara persisten
- Dialog terpisah untuk tambah / edit barang
- Menu `Tentang` menampilkan nama aplikasi, deskripsi, nama mahasiswa, dan NIM
- Styling menggunakan `style.qss`
- Fitur Tambahan (Reset Database): Menu khusus untuk mengosongkan seluruh isi tabel di database secara instan guna mempermudah proses pengujian aplikasi.

## Instalasi

1. Buka Terminal di VS Code (Ctrl + ` atau View > Terminal).
2. Buat Virtual Environment: `python -m venv venv`
3. Aktifkan Virtual Environment: `venv\Scripts\activate` (Windows) atau `source venv/bin/activate` (Linux/Mac)
4. Install PySide6: `pip install PySide6`
5. Jalankan aplikasi: `python main.py`

## Catatan

- File database akan dibuat otomatis saat aplikasi pertama dijalankan

## Teknologi

- PySide6
- SQLite
- QSS eksternal
- Separation of Concerns (UI, database, logika)
