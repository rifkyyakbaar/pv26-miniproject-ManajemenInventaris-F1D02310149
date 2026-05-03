style_content = """/* Main Window Background */
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #667eea, stop:1 #764ba2);
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Menu Bar */
QMenuBar {
    background-color: #2d3748;
    color: white;
    padding: 6px;
}

QMenuBar::item:selected {
    background-color: #4a5568;
}

QMenu {
    background-color: #f7fafc;
    color: #2d3748;
}

QMenu::item:selected {
    background-color: #667eea;
    color: white;
}

/* Table Widget */
QTableWidget {
    background: white;
    gridline-color: #cbd5e0;
    font-size: 13px;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    selection-background-color: #667eea;
    alternate-background-color: #f7fafc;
}

QTableWidget::item:selected {
    background-color: #667eea;
    color: white;
    font-weight: bold;
}

QHeaderView::section {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #667eea, stop:1 #764ba2);
    color: white;
    padding: 12px;
    border: none;
    font-weight: bold;
    font-size: 13px;
}

/* Buttons */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #667eea, stop:1 #764ba2);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: bold;
    font-size: 13px;
    min-height: 40px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #5568d3, stop:1 #6b4399);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #4a4a8a, stop:1 #5a3a8f);
}

/* Labels */
QLabel {
    font-size: 13px;
    color: #2d3748;
    font-weight: 500;
}

/* Input Fields */
QLineEdit {
    border: 2px solid #cbd5e0;
    border-radius: 6px;
    padding: 10px;
    background-color: white;
    color: #2d3748;
    font-size: 13px;
    selection-background-color: #667eea;
}

QLineEdit:focus {
    border: 2px solid #667eea;
    background-color: #f7fafc;
}

/* Combo Box */
QComboBox {
    border: 2px solid #cbd5e0;
    border-radius: 6px;
    padding: 10px;
    background-color: white;
    color: #2d3748;
    font-size: 13px;
}

QComboBox:focus {
    border: 2px solid #667eea;
    background-color: #f7fafc;
}

QComboBox::drop-down {
    border: none;
    width: 30px;
    background: white;
}

QComboBox QAbstractItemView {
    border: 1px solid #cbd5e0;
    selection-background-color: #667eea;
    padding: 4px;
}

/* Message Box */
QMessageBox {
    background-color: #f7fafc;
}

QMessageBox QLabel {
    color: #2d3748;
}

/* Dialog */
QDialog {
    background-color: #f7fafc;
}
"""

with open("style.qss", "w") as f:
    f.write(style_content)

print("Style file updated successfully!")
