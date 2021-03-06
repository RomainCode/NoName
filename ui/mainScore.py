import math
import pygame
from utils.utils import createFont

number_abbreviations = ["K", "M", "B", "t", "q", "Q", "s", "S", "o", "n", "d", "U", "D", "T", "Qt", "Qd", "Sd", "St", "O", "N", "v", "c"]


font1 =createFont(size=28)
font2 = createFont(size=18)

class MainScore():
    """Stores and display the main scores informations"""
    def __init__(self):
        self.current_gold = 0
        self.current_PPS = 40.3
        self.super_star = 0

    def getStr(self, i : int):
            amount = i
            amount_str = str(int(amount))

            if len(amount_str) > 3:
                power_of_10 = len(amount_str)
                power_unit = (power_of_10 - 4) // 3

                if power_unit+1 > len(number_abbreviations):
                    raise ValueError("Numbr out of range of the abbreviations !")

                return str(round(amount / 10**(power_unit*3+3), 2)) + number_abbreviations[power_unit]
            else:
                return amount_str

    def draw(self, surface):
        img = font1.render(self.getStr(self.current_gold), True, (250, 250, 250))
        surface.blit(img, (100, 100))
        img = font2.render(self.getStr(self.current_PPS)+" PPS", True, (250, 250, 250))
        surface.blit(img, (100, 125))
    
    def triggerGoldCoin(self):
        self.current_gold += 1

    def addGold(self, amount):
        self.current_gold += amount
        self.gainGoldFlag(amount)
    
    def addPPS(self, amount):
        self.current_PPS += amount
        self.gainPPSFlag(amount)
    
    def gainGoldFlag(self, amoount):
        pass # handle gain gold effect

    def gainPPSFlag(self, amoount):
        pass # handle gain gold effect
    
    def update(self, deltaTime):
        self.current_gold += self.current_PPS * deltaTime
