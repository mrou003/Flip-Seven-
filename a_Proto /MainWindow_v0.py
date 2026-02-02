import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
)
from PySide6.QtGui import QFont, QPixmap



class MainWindow(QWidget):
    def __init__(self, intx, inty):
        super().__init__()
        self.resize(intx, inty)
        lowerlayout = QHBoxLayout()
        lowerWidget = QWidget()

        layout = QVBoxLayout(self)
        self.label = QLabel()
        pixmap = QPixmap("12.png")
        self.label_back = QLabel()
        pixmap_back = QPixmap("back_card.png")

        
        self.upperLayout = QHBoxLayout(self)
        self.leftWidget = QWidget()
        self.rightWidget = QWidget()
        pixmab_back_card = pixmap_back.scaled(
                300,
                400,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
       
        pixmap_card = pixmap.scaled(
                300,
                400,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        self.label_back.setPixmap(pixmab_back_card)
        self.label_back.setScaledContents(True)
        self.label.setPixmap(pixmap_card)
        self.label.setScaledContents(True)
        self.button_pull = ButtonPull("Tirez une carte")
        self.button_stop = ButtonPull("Arretez de tirer")
        self.upperLayout.addWidget(self.leftWidget)
       
        self.upperLayout.addWidget(self.label)
        
        self.upperLayout.addWidget(self.label_back)
        upperWidget = QWidget()
        upperWidget.setLayout(self.upperLayout)

        layout.addWidget(upperWidget)
        lowerlayout.addWidget(self.button_pull)
        lowerlayout.addWidget(self.button_stop)
        lowerWidget.setLayout(lowerlayout)
        layout.addWidget(lowerWidget)

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(87, 97, 112);
            }
        """)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = MainWindow(600, 600)
    fen.show()
    sys.exit(app.exec())
