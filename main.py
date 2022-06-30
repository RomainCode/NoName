# externals libs
import pygame
import time
import config
from pygame.locals import *

# our libs
from game.game import Game
from physics.simulation.gravityBody import * 
from entities.coin import Coin

# temp import
from physics.collisions.rectangle2D import Rectangle2D
from entities.character import Character

game = Game()
screen = config.screen

# temp variables test
collider = GravityBody(10,10,20,50)


character = Character((50,10,20,50))
coin = Coin(28, 220, 25)

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
            if event.key == pygame.K_SPACE or pygame.mouse.get_pressed()[0]:
                character.tryToJump()
                 

    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    # Fill the background with white
    screen.fill((100, 100, 100))

    character.collider.debugDraw(screen)
    coin.update(deltaTime)
    coin.draw(screen)
    character.update(deltaTime)

    if coin.collider.isCollisionWithRect(character.collider):
        print("collision")

    #character.collider.update(deltaTime)
    #character.collider.y += character.collider.velocityY
    #character.collider.velocityY = 0


    config.clock.tick(config.FPS)
    # Flip the display
    pygame.display.flip()


pygame.quit()