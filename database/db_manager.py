"""
Modul database untuk mengelola operasi SQLite.
Menyediakan class DatabaseManager untuk CRUD data inventaris.
"""
import sqlite3

class DatabaseManager:
    """Mengelola operasi SQLite untuk Inventaris Barang."""
    
    def __init__(self, db_name='data_inventaris.db'):
        """Inisialisasi database dan buat tabel jika belum ada."""
        self.db_name = db_name
        self.create_table()
    
    def get_connection(self):
        """Buat koneksi ke database SQLite."""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def create_table(self):
        """Buat tabel barang jika belum ada."""
        with self.get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS barang (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    kode_barang TEXT NOT NULL UNIQUE,
                    nama_barang TEXT NOT NULL,
                    kategori TEXT NOT NULL,
                    jumlah INTEGER NOT NULL,
                    harga INTEGER NOT NULL
                )
            ''')
            
    def tambah_barang(self, kode, nama, kategori, jumlah, harga):
        """Tambah data barang baru ke database."""
        with self.get_connection() as conn:
            conn.execute('INSERT INTO barang (kode_barang, nama_barang, kategori, jumlah, harga) VALUES (?, ?, ?, ?, ?)',
                         (kode, nama, kategori, jumlah, harga))
            
    def ambil_semua(self):
        """Ambil semua data barang dari database."""
        with self.get_connection() as conn:
            return conn.execute('SELECT * FROM barang ORDER BY nama_barang').fetchall()
            
    def update_barang(self, id_barang, kode, nama, kategori, jumlah, harga):
        """Update data barang berdasarkan ID."""
        with self.get_connection() as conn:
            conn.execute('UPDATE barang SET kode_barang=?, nama_barang=?, kategori=?, jumlah=?, harga=? WHERE id=?',
                         (kode, nama, kategori, jumlah, harga, id_barang))
            
    def hapus_barang(self, id_barang):
        """Hapus data barang berdasarkan ID."""
        with self.get_connection() as conn:
            conn.execute('DELETE FROM barang WHERE id = ?', (id_barang,))
    
    def reset_database(self):
        """Hapus seluruh data dan reset penomoran ID mulai ulang dari 1."""
        with self.get_connection() as conn:
            conn.execute('DELETE FROM barang')
            conn.execute("DELETE FROM sqlite_sequence WHERE name='barang'")

    
    def cari_barang(self, keyword):
        """Cari barang berdasarkan keyword (kode atau nama)."""
        with self.get_connection() as conn:
            query = '''
                SELECT * FROM barang 
                WHERE kode_barang LIKE ? OR nama_barang LIKE ? 
                ORDER BY nama_barang
            '''
            pattern = f"%{keyword}%"
            return conn.execute(query, (pattern, pattern)).fetchall()