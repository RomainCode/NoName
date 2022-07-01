from __future__ import annotations

from utils import utils
import math
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from physics.collisions.rectangle2D import Rectangle2D

class Circle2D:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isCollisionWithRect(self, rect : Rectangle2D):
        
        rleft = rect.x
        rtop = rect.y
        width = rect.w
        height = rect.h
        center_x = self.x
        center_y = self.y
        radius = self.r

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

    def isCollisionWithCircle(self, circle):
        if utils.magnitude(self.x, self.y, circle.x, circle.y) < self.r+circle.r:
            return True
        return False

    def draw(self, surface):
        pass

    def update(self, deltaTime):
        pass