
from physics.simulation.gravityBody import * 
from animation.animationManager import *

class Character:
    def __init__(self,body_parameters: tuple):
        self.collider = GravityBody(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
        self.JUMP_FORCE = -500
        self.is_willing_to_jump = False
        self.is_willing_to_stop_jumping = False
        self.gravity_scale = 1

        self.start_timer = False
        self.jump_timer = 0.4 # 0.5s of jumping max
        self.timer = self.jump_timer
    
    def tryToJump(self):
        self.is_willing_to_jump = True
    
    def releaseJump(self):
        self.is_willing_to_stop_jumping = True
    
    def update(self, deltaTime):
        """Update the character's Y position using the jump and gravity features"""

        if self.start_timer:
            self.timer -= deltaTime
            if self.timer <= 0:
                self.is_willing_to_stop_jumping = True

        self.collider.addGravity()

        if self.is_willing_to_jump and self.collider.y >= HEIGHT-GROUND_MARGIN:
            self.collider.gravity_scale = 0
            self.start_timer = True
            self.collider.addForce(self.JUMP_FORCE)


        if self.collider.y >= HEIGHT-GROUND_MARGIN and self.is_willing_to_jump == False:
            self.collider.y = HEIGHT-GROUND_MARGIN
            self.collider.resetVelocity()
        
        if self.is_willing_to_stop_jumping:
            self.collider.gravity_scale = self.gravity_scale
            self.is_willing_to_stop_jumping = False
            self.timer = self.jump_timer
            self.start_timer = False


        self.collider.y += self.collider.getMotion(deltaTime)

        self.is_willing_to_jump = False
