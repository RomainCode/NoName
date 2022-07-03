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
from entities.staticEnemy import StaticEnemy
from animation.animation import Animation

screen = config.screen

game = Game()
character = Character((50,400,config.PLAYER_WIDTH,config.PLAYER_HEIGHT))
world = World(character)
anim = Animation()
static_enemy = StaticEnemy((500, 300, 50, 50), True, True, animation_model=anim, max_hp=120)
static_list = [static_enemy]



# temp ui
from ui.widgets.container import Container
from ui.widgets.button import Button
from ui.widgets.widget import Widget

container = Container()
container.place(50, 50)

btn = Button(container, text="Hello World !", border_color=config.BLUE, foreground_color=config.WHITE, border_radius=3, border_width=3)
btn.place(Widget.AUTO_POSITION)
btn.attachCommand(Button.ON_CLICK_EVENT, lambda : print("Hello World"))

btn2 = Button(container, text="Button test 2 !", border_color=config.RED, foreground_color=config.WHITE)
btn2.place(Widget.AUTO_POSITION)

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
        
    # deltaTime calculation
    t2 = time.time()
    deltaTime = t2 - t1
    t1 = t2

    screen.fill((100, 100, 100))


    character.collider.debugDraw(screen)
    world.update(deltaTime)
    world.draw(screen)
    character.update(deltaTime)

    container.update(deltaTime, is_left_click=left_clicked)

    container.draw(screen)


    for enemy in list(static_list):    
        enemy.update(deltaTime)
        enemy.draw(screen)

        if enemy.collider.isCollisionWithRect(character.collider):
            enemy.onKilled(score=world.main_score)
            static_list.remove(enemy)


    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()