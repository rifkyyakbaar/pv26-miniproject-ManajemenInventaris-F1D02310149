"""
Modul UI untuk dialog tambah/edit barang.
Menyediakan DialogForm dengan form input dan validasi data.
"""
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from logic.validator import Validator

class DialogForm(QDialog):
    """Dialog untuk input data barang (tambah/edit)."""
    
    def __init__(self, parent=None, item_id=None, kode="", nama="", kategori="", jumlah=0, harga=0):
        """Inisialisasi dialog dengan data barang (jika edit)."""
        super().__init__(parent)
        self.item_id = item_id
        self.init_ui(kode, nama, kategori, jumlah, harga)

    def init_ui(self, kode, nama, kategori, jumlah, harga):
        """Buat layout dan komponen form input."""
        self.setWindowTitle("Tambah / Ubah Barang")
        self.setModal(True)
        self.setGeometry(100, 100, 500, 450)

        layout = QVBoxLayout()

        self.kode_edit = QLineEdit(kode)
        self.nama_edit = QLineEdit(nama)
        
        self.kategori_combo = QComboBox()
        self.kategori_combo.addItems(["Alat", "Bahan", "Elektronik", "Furniture", "Lainnya"])
        if kategori and kategori in ["Alat", "Bahan", "Elektronik", "Furniture", "Lainnya"]:
            self.kategori_combo.setCurrentText(kategori)
        
        self.jumlah_edit = QLineEdit(str(jumlah))
        self.harga_edit = QLineEdit(str(harga))

        layout.addWidget(QLabel("Kode Barang:"))
        layout.addWidget(self.kode_edit)
        layout.addWidget(QLabel("Nama Barang:"))
        layout.addWidget(self.nama_edit)
        layout.addWidget(QLabel("Kategori:"))
        layout.addWidget(self.kategori_combo)
        layout.addWidget(QLabel("Jumlah:"))
        layout.addWidget(self.jumlah_edit)
        layout.addWidget(QLabel("Harga (Rp):"))
        layout.addWidget(self.harga_edit)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Simpan")
        save_button.clicked.connect(self.save)
        cancel_button = QPushButton("Batal")
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def save(self):
        """Validasi input sebelum menyimpan."""
        kode = self.kode_edit.text()
        nama = self.nama_edit.text()
        kategori = self.kategori_combo.currentText()
        jumlah = self.jumlah_edit.text()
        harga = self.harga_edit.text()

        valid_kode, msg_kode = Validator.validate_code(kode)
        valid_nama, msg_nama = Validator.validate_name(nama)
        valid_kategori, msg_kategori = Validator.validate_category(kategori)
        valid_jumlah, msg_jumlah = Validator.validate_quantity(jumlah)
        valid_harga, msg_harga = Validator.validate_price(harga)

        if not valid_kode:
            QMessageBox.warning(self, "Input Tidak Valid", msg_kode)
            return
        if not valid_nama:
            QMessageBox.warning(self, "Input Tidak Valid", msg_nama)
            return
        if not valid_kategori:
            QMessageBox.warning(self, "Input Tidak Valid", msg_kategori)
            return
        if not valid_jumlah:
            QMessageBox.warning(self, "Input Tidak Valid", msg_jumlah)
            return
        if not valid_harga:
            QMessageBox.warning(self, "Input Tidak Valid", msg_harga)
            return

        self.accept()

    def get_data(self):
        """Ambil data dari form input sebagai tuple."""
        return (
            self.kode_edit.text(),
            self.nama_edit.text(),
            self.kategori_combo.currentText(),
            int(self.jumlah_edit.text()),
            int(self.harga_edit.text()),
        )