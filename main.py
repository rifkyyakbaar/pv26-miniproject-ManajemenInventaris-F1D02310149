"""
Main entry point untuk Aplikasi Manajemen Inventaris.
Menggunakan PySide6 untuk GUI dan SQLite untuk penyimpanan data.
"""
import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    try:
        with open("style.qss", "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())
    except FileNotFoundError:
        pass

    window = MainWindow()
    window.show()

    sys.exit(app.exec())