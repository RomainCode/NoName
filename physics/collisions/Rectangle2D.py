import pygame
from utils.utils import *

class Rectangle2D:
    def __init__(self, x, y, w, h, gravity=None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if gravity is not None:
            self.gravity = gravity        


    def isCollisionWithRect(self, rectB) -> bool:
        return isCollisionRect(self.x, self.y, rectB.x, rectB.y, self.w, self.h, rectB.w, rectB.h)
        
    

    def debugDraw(self, surface : pygame.Surface):
        pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.w, self.h))