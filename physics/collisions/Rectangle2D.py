from __future__ import annotations

import pygame
from utils.utils import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from physics.collisions.circle2D import Circle2D

class Rectangle2D:
    """Simple rectangle that has the ability to detect collisions"""
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h      

    def isCollisionWithRect(self, rectB) -> bool:
        return isCollisionRect(self.x, self.y, rectB.x, rectB.y, self.w, self.h, rectB.w, rectB.h)
        

    def isCollisionWithCircle(self, circle : Circle2D) -> bool:
        cx = circle.x
        cy = circle.y
        rx = self.x
        ry = self.y
        rw = self.w
        rh = self.h
        radius = circle.r
        
        testX = cx
        testY = cy

        if (cx < rx):        testX = rx
        elif (cx > rx+rw): testX = rx+rw
        if (cy < ry):        testY = ry
        elif (cy > ry+rh): testY = ry+rh

        distX = cx-testX
        distY = cy-testY
        distance = math.sqrt( (distX*distX) + (distY*distY) )

        if (distance <= radius):
            return True
        return False
    

    def debugDraw(self, surface : pygame.Surface):
        pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.w, self.h))