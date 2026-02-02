import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
)
from PySide6.QtGui import QFontDatabase, QFont
import random
class ButtonPull(QPushButton):
    def __init__(self,text):
        super().__init__()
        self.adjustSize()
        self.clicked.connect(self.on_button_press)
        self.setText("Tirez une cartes")
        
        font = QFont("AppleGothic", 20)  # 20 est la taille
        self.setFont(font)
        
        self.setStyleSheet("""
    QPushButton {
        background-color: rgb(188, 210, 238);
        border-radius: 5px;
        color: black;
        font-weight: bold;   
        
        
    }
""")


    def on_button_press(self):
        print("Bouton pressé !")
        

        
         
         
        

class MainWindow(QWidget):
    def __init__(self, intx, inty):
        super().__init__()
        self.resize(intx, inty)
        
        self.layout = QVBoxLayout(self)
        self.mainWidget = QWidget()
        self.button = ButtonPull("Tirez une carte")
        self.layout.addWidget(self.mainWidget)
        self.layout.addWidget(self.button)
        

    def bgColor(self):
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(87, 97, 112);
            }`
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    fen = MainWindow(600, 600)
    fen.bgColor()
    fen.show()

    sys.exit(app.exec())


