"""
Modul UI untuk jendela utama aplikasi inventaris.
Menyediakan MainWindow dengan tabel data dan tombol aksi.
"""
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QMessageBox,
    QLabel,
    QMenuBar,
    QHeaderView,
    QLineEdit,
)
from PySide6.QtGui import QAction, QColor
from PySide6.QtCore import Qt
from database.db_manager import DatabaseManager
from ui.dialog_form import DialogForm

class MainWindow(QMainWindow):
    """Jendela utama aplikasi manajemen inventaris."""
    
    def __init__(self):
        """Inisialisasi jendela utama, koneksi database, dan UI."""
        super().__init__()
        self.db = DatabaseManager()
        self.setWindowTitle("Aplikasi Manajemen Inventaris")
        self.setGeometry(100, 100, 920, 650)
        self.init_ui()
        self.load_data()

    def init_ui(self):
        """Buat menu bar dan layout utama."""
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)

        tentang_menu = self.menu_bar.addMenu("Tentang")
        info_action = QAction("Tentang Aplikasi", self)
        info_action.triggered.connect(self.show_about_dialog)
        tentang_menu.addAction(info_action)

        database_menu = self.menu_bar.addMenu("Database")
        reset_action = QAction("Reset Data", self)
        reset_action.triggered.connect(self.reset_data)
        database_menu.addAction(reset_action)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        info_layout = QHBoxLayout()
        info_layout.addWidget(QLabel("<b>Aplikasi:</b> Manajemen Inventaris"))
        info_layout.addStretch()
        info_layout.addWidget(QLabel("<b>Nama:</b> Rifky Akbar Utomo Putra"))
        info_layout.addWidget(QLabel("<b>NIM:</b> F1D02310149"))
        layout.addLayout(info_layout)

        # Search bar
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Cari Barang:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Ketik kode atau nama barang...")
        self.search_input.textChanged.connect(self.filter_data)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Kode Barang",
            "Nama Barang",
            "Kategori",
            "Jumlah",
            "Harga",
        ])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        for col in range(1, 6):
            self.table.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.setColumnWidth(0, 40)
        self.table.horizontalHeader().setSectionsMovable(False)
        layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        add_button = QPushButton("Tambah Barang")
        add_button.clicked.connect(self.add_item)
        edit_button = QPushButton("Ubah Barang")
        edit_button.clicked.connect(self.edit_item)
        delete_button = QPushButton("Hapus Barang")
        delete_button.setObjectName("dangerButton")
        delete_button.clicked.connect(self.delete_item)

        button_layout.addWidget(add_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        layout.addLayout(button_layout)

        # Statistik dashboard
        stats_layout = QHBoxLayout()
        self.stats_label = QLabel()
        self.stats_label.setStyleSheet("color: #1976d2; font-weight: bold; font-size: 13px;")
        stats_layout.addWidget(self.stats_label)
        stats_layout.addStretch()
        layout.addLayout(stats_layout)

        central_widget.setLayout(layout)

    def load_data(self):
        """Muat data dari database ke tabel dengan highlight stok rendah."""
        items = self.db.ambil_semua()
        self.table.setRowCount(len(items))
        
        total_jenis = len(items)
        total_aset = 0
        
        for row, item in enumerate(items):
            jumlah = item["jumlah"]
            harga = item["harga"]
            total_aset += jumlah * harga
            
            self.table.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(item["kode_barang"]))
            self.table.setItem(row, 2, QTableWidgetItem(item["nama_barang"]))
            self.table.setItem(row, 3, QTableWidgetItem(item["kategori"]))
            
            qty_item = QTableWidgetItem(str(jumlah))
            harga_item = QTableWidgetItem(f"Rp {harga:,}")
            harga_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            
            self.table.setItem(row, 4, qty_item)
            self.table.setItem(row, 5, harga_item)
            
            # Highlight stok menipis (< 5)
            if jumlah < 5:
                color = QColor("#ffebee")  # Light red background
                for col in range(6):
                    item_widget = self.table.item(row, col)
                    item_widget.setBackground(color)
                    item_widget.setForeground(QColor("#c62828"))  # Dark red text
        
        # Update statistik
        self.update_stats(total_jenis, total_aset)

    def update_stats(self, total_jenis, total_aset):
        """Update label statistik dashboard."""
        stats_text = f"📊 Total Jenis Barang: {total_jenis} | 💰 Estimasi Nilai Aset: Rp {total_aset:,}"
        self.stats_label.setText(stats_text)

    def filter_data(self):
        """Filter tabel berdasarkan keyword pencarian."""
        keyword = self.search_input.text().strip()
        
        if not keyword:
            # Tampilkan semua data jika search kosong
            self.load_data()
            return
        
        # Cari data dari database
        items = self.db.cari_barang(keyword)
        self.table.setRowCount(len(items))
        
        total_jenis = len(items)
        total_aset = 0
        
        for row, item in enumerate(items):
            jumlah = item["jumlah"]
            harga = item["harga"]
            total_aset += jumlah * harga
            
            self.table.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(item["kode_barang"]))
            self.table.setItem(row, 2, QTableWidgetItem(item["nama_barang"]))
            self.table.setItem(row, 3, QTableWidgetItem(item["kategori"]))
            
            qty_item = QTableWidgetItem(str(jumlah))
            harga_item = QTableWidgetItem(f"Rp {harga:,}")
            harga_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            
            self.table.setItem(row, 4, qty_item)
            self.table.setItem(row, 5, harga_item)
            
            if jumlah < 5:
                color = QColor("#ffebee")
                for col in range(6):
                    item_widget = self.table.item(row, col)
                    item_widget.setBackground(color)
                    item_widget.setForeground(QColor("#c62828"))
        
        self.update_stats(total_jenis, total_aset)

    def add_item(self):
        """Buka dialog untuk menambah barang baru."""
        dialog = DialogForm(self)
        if dialog.exec():
            kode, nama, kategori, jumlah, harga = dialog.get_data()
            try:
                self.db.tambah_barang(kode, nama, kategori, jumlah, harga)
            except Exception as e:
                QMessageBox.warning(self, "Kesalahan", f"Tidak dapat menyimpan data: {e}")
            self.search_input.clear()
            self.load_data()

    def edit_item(self):
        """Buka dialog untuk mengedit barang yang dipilih."""
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih baris data terlebih dahulu.")
            return

        item_id = int(self.table.item(current_row, 0).text())
        kode = self.table.item(current_row, 1).text()
        nama = self.table.item(current_row, 2).text()
        kategori = self.table.item(current_row, 3).text()
        jumlah = int(self.table.item(current_row, 4).text())
        harga_text = self.table.item(current_row, 5).text().replace("Rp ", "").replace(",", "")
        harga = int(harga_text)

        dialog = DialogForm(self, item_id, kode, nama, kategori, jumlah, harga)
        if dialog.exec():
            kode, nama, kategori, jumlah, harga = dialog.get_data()
            self.db.update_barang(item_id, kode, nama, kategori, jumlah, harga)
            self.search_input.clear()
            self.load_data()

    def delete_item(self):
        """Hapus barang yang dipilih setelah konfirmasi."""
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih baris data terlebih dahulu.")
            return

        item_id = int(self.table.item(current_row, 0).text())
        reply = QMessageBox.question(
            self,
            "Konfirmasi Hapus",
            "Apakah Anda yakin ingin menghapus barang ini?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.db.hapus_barang(item_id)
            self.search_input.clear()
            self.load_data()

    def reset_data(self):
        """Reset seluruh data barang dan mulai ulang ID dari 1."""
        reply = QMessageBox.question(
            self,
            "Reset Database",
            "Reset database akan menghapus semua data dan memulai ID dari 1. Lanjutkan?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.db.reset_database()
            self.search_input.clear()
            self.load_data()

    def show_about_dialog(self):
        """Tampilkan dialog informasi tentang aplikasi."""
        QMessageBox.information(
            self,
            "Tentang Aplikasi",
            "Aplikasi Manajemen Inventaris\n"
            "- Teknologi: PySide6, SQLite, QSS eksternal\n"
            "- Fitur: CRUD, Search, Statistik, Highlight Stok Rendah\n"
            "- Nama: Rifky Akbar Utomo Putra\n"
            "- NIM: F1D02310149\n"
            "- Modul: Database, Logic, UI"
        )

