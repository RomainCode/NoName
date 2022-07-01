from __future__ import annotations

from utils import utils
import math
import pygame
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from physics.collisions.rectangle2D import Rectangle2D

class Circle2D:
    """Simple circle that can handle collision detection"""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isCollisionWithRect(self, rect : Rectangle2D) -> bool:
        cx = self.x
        cy = self.y
        rx = rect.x
        ry = rect.y
        rw = rect.w
        rh = rect.h
        radius = self.r
        
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

    def isCollisionWithCircle(self, circle : Circle2D) -> bool:
        if utils.magnitude(self.x, self.y, circle.x, circle.y) < self.r+circle.r:
            return True
        return False

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), self.r, width=1)

    def update(self, deltaTime):
        pass