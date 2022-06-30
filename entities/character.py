
from physics.simulation.GravityBody import * 
from animation.animationManager import *

from simulation import *    


class Character:
    def __init__(self,body_parameters: tuple):
        self.collider = GravityBody(body_parameters[0], body_parameters[1], body_parameters[2], body_parameters[3])
        self.animation_manager =  AnimationManager()
    
    