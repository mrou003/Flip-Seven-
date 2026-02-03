import random
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap, QFont

class GameEngine(QObject):
    doublon = Signal()

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.packet = []
        self.hand = []
        distribution = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        for value, count in enumerate(distribution):
            self.packet.extend([value] * count)

        random.shuffle(self.packet)
        self.index = 0

    def draw_card(self):
        if self.index >= len(self.packet):
            return None

        value = self.packet[self.index]
        self.index += 1

        if value in self.hand:
            self.doublon.emit()
            return None

        self.hand.append(value)
        return value

class Simulation(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Simulation")
        self.setStyleSheet("""
            QWidget#Simulation {
                background-color: rgb(188, 210, 238);
            }
        """)

        self.game = GameEngine()
        self.game.doublon.connect(self.on_doublon)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.piles = DisplayPiles()
        self.hand = HandWidget()
        self.buttons = ButtonWidget()

        layout.addWidget(self.piles)
        layout.addWidget(self.hand)
        layout.addWidget(self.buttons)

        self.buttons.pullClicked.connect(self.draw_card)

    def draw_card(self):
        value = self.game.draw_card()
        if value is None:
            return

        self.piles.show_card(value)
        self.hand.add_card(value)

    def on_doublon(self):
        self.hand.clear()
        self.piles.reset()
        self.game.reset()


# =========================
# AFFICHAGE DES PILES
# =========================

class DisplayPiles(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)

        self.left = CardLabel("back_card", 200, 300)
        self.right = CardLabel("back_card", 200, 300)

        self.layout.addWidget(self.left)
        self.layout.addWidget(self.right)

    def show_card(self, value):
        self.left.set_card(value)

    def reset(self):
        self.left.set_card("back_card")



class HandWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignLeft)

    def add_card(self, value):
        self.layout.addWidget(CardLabel(value, 50, 70))

    def clear(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()



class ButtonWidget(QWidget):
    pullClicked = Signal()

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout(self)

        pull = GameButton("Tirer une carte")
        stop = GameButton("Arrêter")

        layout.addWidget(pull)
        layout.addWidget(stop)

        pull.clicked.connect(self.pullClicked.emit)
        stop.clicked.connect(self.on_stop)

    def on_stop(self):
        print("Arrêt du tour")


class GameButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFont(QFont("AppleGothic", 18))
        self.setStyleSheet("""
            QPushButton {
                background-color: rgb(188, 210, 238);
                border-radius: 6px;
                padding: 10px;
                font-weight: bold;
            }
        """)


class CardLabel(QLabel):
    def __init__(self, value, w, h):
        super().__init__()
        self.setFixedSize(w, h)
        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.set_card(value)

    def set_card(self, value):
        pixmap = QPixmap(f"image/{value}.png")
        if pixmap.isNull():
            self.setText("Image\nmanquante")
            return

        self.setPixmap(
            pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )
