import sys
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
)
from PySide6.QtGui import QFont, QPixmap
from P01_Simulation_Game.P01_simulationGame import Simulation

from .LeftWindow import leftWindow




class MainWindow(QWidget):
    def __init__(self, intx, inty):
        super().__init__()

        self.resize(intx, inty)

        

        self.upperMainWidget = QWidget()

        self.MainLayout = QHBoxLayout()
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setSpacing(0)

        self.leftWidget = leftWindow()
        self.leftWidget.setMaximumWidth(200)
        

        self.rightWidget = QWidget()
        self.rightLayout = QVBoxLayout(self.rightWidget)
        self.rightLayout.setContentsMargins(0, 0, 0, 0)
        self.rightLayout.setSpacing(0)
        

        self.MainLayout.addWidget(self.leftWidget)
        self.MainLayout.addWidget(self.rightWidget)
        self.upperMainWidget.setLayout(self.MainLayout)

        self.LowerWidgetBox = QWidget()
        
        self.text = QLabel()
        self.text.setFont(QFont("AppleGothic", 20))
        self.text.setAlignment(Qt.AlignRight)

        
        self.text.setStyleSheet("""
            QLabel{
                color: black;
            }
        """)
 
        
        
        testLayout = QVBoxLayout()
        testLayout.addWidget(self.text)
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
        self.leftWidget.pluginSelected.connect(self.on_plugin_selected)
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


    def on_plugin_selected(self, plugin_name):
        
        self.text.setText(plugin_name)
        self.clear_layout(self.rightLayout)

        if plugin_name == "Simulation":
            UI = Simulation()
            self.rightLayout.addWidget(UI)
        
        


        
    

