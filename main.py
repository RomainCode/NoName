# externals libs
from doctest import master
import pygame
import time
import config
from pygame.locals import *

# our libs
from game.game import Game
from physics.simulation.gravityBody import * 
from world.world import World
from entities.character import Character
from entities.staticEnemy import StaticEnemy
from animation.animation import Animation
from ui.fps import drawFps

screen = config.screen

game = Game()
character = Character((50,400,config.PLAYER_WIDTH,config.PLAYER_HEIGHT))
world = World(character)
anim = Animation()
static_enemy = StaticEnemy((500, 300, 50, 50), True, True, animation_model=anim, max_hp=120)
static_list = [static_enemy]



# temp ui
from gameLogic.main import Element, TabContainer

tab_container = TabContainer()
tab_container.dumbGenerate(amount=20)
tab_container.x = 0


t1 = time.time()
deltaTime = 0

while not game.isNeedToClose:


    # Input collector
    left_clicked = False
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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click
                left_clicked = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: tab_container.scroll_offset = min(tab_container.scroll_offset + 15, 0)
            if event.button == 5: tab_container.scroll_offset = max(tab_container.scroll_offset - 15, - tab_container.max_height+tab_container.h)
        
    # deltaTime calculation
    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    # graphic update

    screen.fill((100, 100, 100))

    
    world.update(deltaTime)
    world.draw(screen)
    character.update(deltaTime)
    drawFps(config.clock, (0,0), screen)
    
    character.collider.debugDraw(screen)

    tab_container.draw(screen)
    tab_container.update(deltaTime, is_clicked=left_clicked)

    for enemy in list(static_list):    
        enemy.update(deltaTime)
        enemy.draw(screen)

        if enemy.collider.isCollisionWithRect(character.collider):
            enemy.onKilled(score=world.main_score)
            static_list.remove(enemy)


    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()