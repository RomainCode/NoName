
from physics.simulation.gravityBody import * 
from animation.animationManager import *

class Character:
    def __init__(self,body_parameters: tuple):
        self.collider = GravityBody(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
        self.jump_power = 0
        self.JUMP_FORCE = -400
        self.is_willing_to_jump = False
        self.is_willing_to_stop_jumping = False
        self.gravity_scale = 1

        self.start_timer = False
        self.jump_timer = 0.5 # 0.5s of jumping max
        self.timer = self.jump_timer
    
    def tryToJump(self):
        self.is_willing_to_jump = True
    
    def releaseJump(self):
        self.is_willing_to_stop_jumping = True

    def addForce(self, f):
        self.collider.velocityY += f
    
    def addGravity(self):
        self.addForce(self.gravity_scale*GravityBody.GRAVITY)
    
    def calculateMovement(self, deltaTime):
        return self.collider.velocityY * deltaTime
    
    def update(self, deltaTime):

        if self.start_timer:
            self.timer -= deltaTime
            if self.timer <= 0:
                self.is_willing_to_stop_jumping = True

        self.addGravity()

        if self.is_willing_to_jump and self.collider.y >= HEIGHT-GROUND_MARGIN:
            self.gravity_scale = 0
            self.start_timer = True
            self.addForce(self.JUMP_FORCE)


        if self.collider.y >= HEIGHT-GROUND_MARGIN and self.is_willing_to_jump == False:
            self.collider.y = HEIGHT-GROUND_MARGIN
            self.collider.velocityY = 0
        
        if self.is_willing_to_stop_jumping:
            self.gravity_scale = 1
            self.is_willing_to_stop_jumping = False
            self.timer = self.jump_timer
            self.start_timer = False


        self.collider.y += self.calculateMovement(deltaTime)

        self.is_willing_to_jump = False
