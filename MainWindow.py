import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
)
from PySide6.QtGui import QFont, QPixmap
from LeftWindow import leftWindow

class MainWindow(QWidget):
    def __init__(self, intx, inty):
        super().__init__()

        self.resize(intx, inty)

        self.setObjectName("MainWindow")
        self.setStyleSheet("""
            QWidget#MainWindow {
                background-color: rgb(87, 97, 112);
            }
        """)

        self.upperMainWidget = QWidget()

        self.MainLayout = QHBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)

        self.leftWidget = leftWindow()
        self.leftWidget.setMaximumWidth(200)

        self.rightWidget = QWidget()
        self.rightWidget.setStyleSheet("""
            background-color: rgb(222, 233, 247);
        """)

        self.MainLayout.addWidget(self.leftWidget)
        self.MainLayout.addWidget(self.rightWidget)
        self.upperMainWidget.setLayout(self.MainLayout)

        self.LowerWidgetBox = QWidget()
        text = QLabel()
        text.setText("hello")
        
        testLayout = QVBoxLayout()
        testLayout.addWidget(text)
        self.LowerWidgetBox.setLayout(testLayout)
        
        
        
        
        self.LowerWidgetBox.setStyleSheet("""
            background-color: rgb(61, 76, 143);
        """)

        self.MainLayoutVBox = QVBoxLayout()
        self.MainLayoutVBox.setContentsMargins(0, 0, 0, 0)
        self.MainLayoutVBox.setSpacing(0)
        self.MainLayoutVBox.addWidget(self.upperMainWidget)
        self.MainLayoutVBox.addWidget(self.LowerWidgetBox)

        self.setLayout(self.MainLayoutVBox)

