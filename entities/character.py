
from physics.simulation.gravityBody import * 
from animation.animationManager import *

class Character:
    def __init__(self,body_parameters: tuple):
        self.collider = GravityBody(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
        self.jump_power = 0
        self.JUMP_FORCE = -600
        self.is_willing_to_jump = False
    
    def tryToJump(self):
        self.is_willing_to_jump = True

     
    
    def update(self, deltaTime):
        self.collider.velocityY = self.collider.velocityY + GravityBody.GRAVITY

        if self.is_willing_to_jump and self.collider.y >= HEIGHT-GROUND_MARGIN:
            self.collider.velocityY = self.JUMP_FORCE


        if self.collider.y >= HEIGHT-GROUND_MARGIN and self.is_willing_to_jump == False:
            self.collider.velocityY = 0

        self.collider.y += self.collider.velocityY*deltaTime

        self.is_willing_to_jump = False



        
        