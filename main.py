# externals libs
import pygame
import time
import config
from pygame.locals import *

# our libs
from game.game import Game
from physics.simulation.gravityBody import * 
from entities.coin import Coin
from world.world import World
from world.chunck import Chunck
from world.chunckManager import ChunckManager
from ui.mainScore import MainScore

# temp import
from physics.collisions.rectangle2D import Rectangle2D
from entities.character import Character

game = Game()
screen = config.screen

# temp variables test
collider = GravityBody(10,10,20,50)


character = Character((50,10,20,50))
world = World(character)
main_score = MainScore()

chunck_manager = ChunckManager()
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
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                character.releaseJump()

    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    # Fill the background with white
    screen.fill((100, 100, 100))

    character.collider.debugDraw(screen)
    world.update(deltaTime)
    world.draw(screen)
    character.update(deltaTime)
    chunck_manager.back()
    chunck_manager.update_chuncks(deltaTime)
    chunck_manager.draw_chuncks(screen)
    main_score.draw(screen)

    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()