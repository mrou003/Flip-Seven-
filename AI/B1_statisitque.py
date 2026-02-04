import random
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
)
from PySide6.QtGui import QPixmap, QFont

class B1_stat(QObject):
    Action = Signal(object)
    
    def __init__(self):
        super().__init__()
        self.packet = []
        self.distribution = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.hand = []
    
    def getCard(self,card):
        self.updatePacket(card)
        
    
    def getHand(self,hand):
        self.hand = hand
        self.calculateProba()
        
        
    
    def setAction(self,proba):
        
        if proba <=30:
            self.Action.emit("Pull")
        else:
            self.Action.emit("Stop")
         
       
    
    def updatePacket(self, card):
        
        self.distribution[card] -=1
        self.showupdated_distribution()
    
    
    

        
    
    def showupdated_distribution(self):
        self.packet = []
        for value, count in enumerate(self.distribution):
            self.packet.extend([value] * count)
            
    def calculateProba(self):
        if len(self.distribution)!=0 : 
            print(self.hand)
            sumProba = 0
            
            
            
            for i in self.hand:
                num = self.distribution[i]
                
                den = 0
                den = sum(self.distribution)
                sumProba+=num/den
            
            self.setAction(sumProba*100)
            
            
            
    
        
        
        
    