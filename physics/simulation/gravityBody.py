from physics.collisions.rectangle2D import Rectangle2D
from config import HEIGHT
from config import GROUND_MARGIN




class GravityBody(Rectangle2D):
    """Rectangle that has the ability to handle Y forces and gravity"""
    GRAVITY = 9.8 # (m/s)
    CORRECTING_FACTOR = 1.3 # to make it more suitable in a game

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h) # extends Rectangle2D
        self.velocityY = 0
        self.wheight = 90
        self.deltaTime =0
        self.gravity_scale = 1
    
    def addForce(self, f : float):
        self.velocityY += f

    def getMotion(self, deltaTime) -> float:
        return self.velocityY * deltaTime   
    
    def addGravity(self):
        self.velocityY += GravityBody.GRAVITY*self.gravity_scale
    
    def resetVelocity(self):
        self.velocityY = 0
            
    def draw(self, surface):
        self.drawDebug(surface)
    
    def __str__(self) -> str:
        return f"GravityObject x={self.x}, y={self.y}, w={self.w}, h={self.h}, velocityY={self.velocityY}, weight={self.weight}"