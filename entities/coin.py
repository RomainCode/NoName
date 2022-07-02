from animation.animation import Animation
from physics.collisions.circle2D import Circle2D
import config

import pygame

class Coin:

    SPEED = config.BASE_SPEED

    def __init__(self, x, y, r=20):
        self.animation = Animation()
        size = (2*r, 2*r)
        ids = [1, 2, 3, 4, 5, 6]
        for id_ in ids:
            self.animation.adImageByPath(f"assets/images/coin/floating_coin{id_}.png", size=size)
        self.animation.setInterval(0.2)
        self.collider = Circle2D(x, y, r)

    def update(self, deltaTime):
        self.animation.update(deltaTime)
        self.move(deltaTime)

    def draw(self, surface):
        surface.blit(self.animation.getCurrentImage(), (self.collider.x-self.collider.r, self.collider.y-self.collider.r))
    
    def move(self, deltaTime): # move to the left the coin
        self.collider.x -= deltaTime*Coin.SPEED


