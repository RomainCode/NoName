import pygame
from utils.utils import *

class Rectangle2D:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        


    def colliseWithRect(self, rectB : Rectangle2D.Rectangle2D) -> bool:
        return isCollisionRect(self.x, self.y, rectB.x, rectB.y, self.w, self.h, rectB.w, rectB.h)
        
    

    def debugDraw(self, surface : pygame.Surface):
        pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.w, self.h))