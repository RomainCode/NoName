from physics.collisions.rectangle2D import *
from config import HEIGHT
from config import GROUND_MARGIN




class GravityBody(Rectangle2D):

    GRAVITY = 9.8 # (m/s)
    CORRECTING_FACTOR = 1.3

    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.velocityY = 0
        self.wheight = 60
        self.distance_ground = 0
        self.deltaTime =0
        self.gravity_scale = 1
    
    def update(self, deltaTime):
        #self.velocityY += self.velocityY * deltaTime
        self.velocityY += GravityBody.GRAVITY * deltaTime * self.wheight
        if self.y >= HEIGHT-GROUND_MARGIN:
            self.velocityY =0
            
        self.deltaTime = deltaTime
    
    def addForce(self, f):
        self.velocityY += f

    def getMotion(self, deltaTime):
        return self.velocityY * deltaTime   
    
    def addGravity(self):
        self.velocityY += GravityBody.GRAVITY*self.gravity_scale
    
    def resetVelocity(self):
        self.velocityY = 0
            
    def draw(self, surface):
        self.drawDebug(surface)
    
    def __str__(self) -> str:
        return f"GravityObject x={self.x}, y={self.y}, w={self.w}, h={self.h}, velocityY={self.velocityY}, weight={self.weight}"