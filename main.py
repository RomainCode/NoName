# externals libs
import pygame
import time
import config
from pygame.locals import *

# our libs
from game.game import Game
from physics.simulation.gravityBody import * 
from world.world import World
from entities.character import Character

screen = config.screen

game = Game()
character = Character((50,400,config.PLAYER_WIDTH,config.PLAYER_HEIGHT))
world = World(character)


t1 = time.time()
deltaTime = 0

while not game.isNeedToClose:


    # Input collector
    for event in pygame.event.get():

        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            game.isNeedToClose = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.mouse.get_pressed()[0]:
                character.tryToJump()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                character.releaseJump()
        
    # deltaTime calculation
    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    screen.fill((100, 100, 100))


    character.collider.debugDraw(screen)
    world.update(deltaTime)
    world.draw(screen)
    character.update(deltaTime)

    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()