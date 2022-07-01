from animation.animation import Animation
from physics.collisions.circle2D import Circle2D

import pygame

class Coin:

    SPEED = 120

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
        pygame.draw.circle(surface, (255, 0, 0), (self.collider.x, self.collider.y), self.collider.r, width=1)
        surface.blit(self.animation.getCurrentImage(), (self.collider.x-self.collider.r, self.collider.y-self.collider.r))
    
    def synchronize(self, last_time, current_pointer):
        self.animation.last_time = last_time
        self.animation.pointer = current_pointer
    
    def move(self, deltaTime):
        self.collider.x -= deltaTime*Coin.SPEED


