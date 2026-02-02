import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
)
from PySide6.QtGui import QFont, QPixmap


class ButtonPull(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.clicked.connect(self.on_button_press)

        font = QFont("AppleGothic", 20)
        self.setFont(font)

        self.setStyleSheet("""
            QPushButton {
                background-color: rgb(188, 210, 238);
                border-radius: 5px;
                color: black;
                font-weight: bold;
                padding: 10px;
            }
        """)

    def on_button_press(self):
        print("Bouton pressé !")


class MainWindow(QWidget):
    def __init__(self, intx, inty):
        super().__init__()
        self.resize(intx, inty)

        layout = QVBoxLayout(self)
        self.label = QLabel()
        pixmap = QPixmap("12.png")

        
        self.upperLayout = QHBoxLayout(self)
        self.leftWidget = QWidget()
        self.rightWidget = QWidget()
       
        pixmap = pixmap.scaled(
                300,
                400,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.button = ButtonPull("Tirez une carte")
        self.upperLayout.addWidget(self.leftWidget)
       
        self.upperLayout.addWidget(self.label)
        self.upperLayout.addWidget(self.rightWidget)
        upperWidget = QWidget()
        upperWidget.setLayout(self.upperLayout)

        layout.addWidget(upperWidget)
        layout.addWidget(self.button)

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(87, 97, 112);
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = MainWindow(600, 600)
    fen.show()
    sys.exit(app.exec())
