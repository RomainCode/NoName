import math
import pygame

number_abbreviations = ["K", "M", "B", "t", "q", "Q", "s", "S", "o", "n", "d", "U", "D", "T", "Qt", "Qd", "Sd", "St", "O", "N", "v", "c"]
Font=pygame.font.SysFont('timesnewroman',  30)

font = pygame.font.Font("./assets/fonts/upheavtt.ttf", 28)

class MainScore():
    def __init__(self):
        self.current_gold = 4544512

    def getStr(self):
            amount = self.current_gold
            amount_str = str(int(amount))

            if len(amount_str) >= 3:
                power_of_10 = len(amount_str)
                power_unit = (power_of_10 - 4) // 3

                if power_unit+1 > len(number_abbreviations):
                    raise ValueError("Numbr out of range of the abbreviations !")

                return str(round(amount / 10**(power_unit*3+3), 2)) + number_abbreviations[power_unit]
            else:
                return amount_str
    
    def draw(self, surface):
        img = font.render(self.getStr(), True, (250, 250, 250))
        surface.blit(img, (100, 100))
