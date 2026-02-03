import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
)
from PySide6.QtGui import QFont, QPixmap
from MainWidgetFolder.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = MainWindow(800, 800)
    fen.show()
    sys.exit(app.exec())
