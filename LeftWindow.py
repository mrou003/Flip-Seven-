import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QListView
)
from PySide6.QtGui import QFont
from PySide6.QtCore import QStringListModel


class leftWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.listPlugin = ListPlugin()
        layout.addWidget(self.listPlugin)


class ListPlugin(QListView):
    def __init__(self):
        super().__init__()

        self.setFont(QFont("AppleGothic", 20))

        self.model = QStringListModel()
        self.model.setStringList([
            "Simulation Game",
            "Simulation Game"
        ])
        self.setModel(self.model)

    
        self.setStyleSheet("""
            QListView {
                background-color: rgb(87, 97, 112);
                border: none;
                color: black;
                font-weight: bold;
            }

            QListView::item {
                padding: 10px;
            }

            QListView::item:hover {
                background-color: rgba(76, 105, 149, 0.39)  ;
            }

            QListView::item:selected {
                background-color: rgba(52, 74, 108, 0.16);
                color : rgb(61, 76, 143);
            }
        """)
        self.clicked.connect(self.on_list_clicked)

    def on_list_clicked(self, index):
        print("working :", self.model.data(index))
        self.clearFocus()
