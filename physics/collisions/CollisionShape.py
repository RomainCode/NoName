import pygame
import utils.utils as utils

class Rectangle2D:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        


    def colliseWithRect(self, rectB : Rectangle2D) -> bool:
        return utils.isCollisionRect(self.x, self.y, rectB.x, rectB.y, self.w, self.h, rectB.w, rectB.h)
        
    

    def debugDraw(self, surface):
        rect = pygame.Rect((self.x,self.y),(self.w,self.h))
        pygame.draw.rect(surface=surface,color=(255,255,255), rect=rect)