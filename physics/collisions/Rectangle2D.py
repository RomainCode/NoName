from __future__ import annotations

import pygame
from utils.utils import *

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from physics.collisions.circle2D import Circle2D

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
        

    def isCollisionWithCircle(self, circle : Circle2D):
        
        rleft = self.x
        rtop = self.y
        width = self.w
        height = self.h
        center_x = circle.x
        center_y = circle.y
        radius = circle.r

        # complete boundbox of the rectangle
        rright, rbottom = rleft + width/2, rtop + height/2

        # bounding box of the circle
        cleft, ctop     = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if math.hypot(x-center_x, y-center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected
    

    def debugDraw(self, surface : pygame.Surface):
        pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.w, self.h))