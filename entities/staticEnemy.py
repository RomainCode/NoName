
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.mainScore import MainScore

from physics.collisions.rectangle2D import Rectangle2D
from animation.animation import Animation
from gameLogic.gain import * 
import config


class HPComp:
    def __init__(self, max_hp : int):
        self.max_hp = max_hp
        self.hp = self.max_hp

    def draw(self, surface):
        pass

class GainWhenKilledComp:
    def __init__(self, gain : dict):
        # gain : {'item_id', amount}
        # ex : 
        self.gain = gain

    def onKilled(self, score : MainScore):
        flag = extractGain(self.gain, score)
        if flag == config.ERROR_FLAG:
            raise Exception("An error has occurred while extrating the gain in GainWhenKilledComp->__onKilled")


class StaticEnemy:

    SPEED = config.BASE_SPEED

    def __init__(self, entity_rect_collider : tuple, has_hp : bool, has_gain : bool, animation_model : Animation, max_hp=100, gain={"GOLD": 395}):
        if has_hp:
            self.hp_component = HPComp(max_hp)
        else:
            self.hp_component = None
        
        if has_gain:
            self.gain_component = GainWhenKilledComp(gain)
        else:
            self.gain_component = None

        self.collider = Rectangle2D(entity_rect_collider[0], entity_rect_collider[1], entity_rect_collider[2], entity_rect_collider[3])
        
        self.animation = animation_model.copy() # only one animation for the beginning
        self.animation.synchronize(animation_model)
        self.animation.pause()


    def update(self, deltaTime):
        self.animation.update(deltaTime)
        self.moveLeft(deltaTime)

    def moveLeft(self, deltaTime):
        self.collider.x -= deltaTime * StaticEnemy.SPEED

    def draw(self, surface):
        self.collider.debugDraw(surface)
    
    def onKilled(self, score=None):
        if self.gain_component != None:
            self.gain_component.onKilled(score)
