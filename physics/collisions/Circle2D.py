from utils import utils

class Circle2D:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isCollisionWithRect(self, rect):
        Xn = max(rect.x, min(self.x, rect.w))
        Yn = max(rect.y, min(self.y, rect.h))
        Dx = Xn - self.x
        Dy = Yn - self.y
        return (Dx**2 + Dy**2) <= self.r**2

    def isCollisionWithCircle(self, circle):
        if utils.magnitude(self.x, self.y, circle.x, circle.y) < self.r+circle.r:
            return True
        return False

    def draw(self, surface):
        pass

    def update(self, deltaTime):
        pass