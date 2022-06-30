# externals libs
import pygame
import time
import config
from pygame.locals import *

# our libs
from game.game import Game
from physics.simulation.gravityBody import * 

# temp import
from physics.collisions.Rectangle2D import Rectangle2D
from entities.character import Character

game = Game()
screen = config.screen

# temp variables test
collider = GravityBody(10,10,20,50)


character = Character((50,10,20,50))

# un joueur
# -> un collider
# -> un système d'animation
# object sith gravity <- collider


t1 = time.time()
deltaTime = 0

while not game.isNeedToClose:

    jump = False

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.isNeedToClose = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.tryToJump()
                

    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    # Fill the background with white
    screen.fill((50, 50, 50))

    character.collider.debugDraw(screen)
    character.update(deltaTime)
    #character.collider.update(deltaTime)
    #character.collider.y += character.collider.velocityY
    #character.collider.velocityY = 0


    config.clock.tick(config.FPS)
    # Flip the display
    pygame.display.flip()


pygame.quit()