"""
Modul validasi untuk memvalidasi input data inventaris.
Menyediakan class Validator dengan method validasi untuk setiap field.
"""

class Validator:
    """Class untuk memvalidasi input data barang."""
    
    @staticmethod
    def validate_code(code):
        """Validasi kode barang: tidak kosong, minimal 3 karakter."""
        if not code or not code.strip():
            return False, "Kode barang harus diisi"
        if len(code.strip()) < 3:
            return False, "Kode barang minimal 3 karakter"
        return True, ""

    @staticmethod
    def validate_name(name):
        """Validasi nama barang: tidak kosong."""
        if not name or not name.strip():
            return False, "Nama barang harus diisi"
        return True, ""

    @staticmethod
    def validate_category(category):
        """Validasi kategori: tidak kosong."""
        if not category or not category.strip():
            return False, "Kategori harus diisi"
        return True, ""

    @staticmethod
    def validate_quantity(quantity):
        """Validasi jumlah: harus angka dan tidak negatif."""
        try:
            qty = int(quantity)
            if qty < 0:
                return False, "Jumlah tidak boleh negatif"
            return True, ""
        except ValueError:
            return False, "Jumlah harus berupa angka"

    @staticmethod
    def validate_price(price):
        """Validasi harga: harus angka dan tidak negatif."""
        try:
            prc = int(price)
            if prc < 0:
                return False, "Harga tidak boleh negatif"
            return True, ""
        except ValueError:
            return False, "Harga harus berupa angka"