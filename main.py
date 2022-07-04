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
from ui.widgets.container import Container
from ui.widgets.button import Button
from ui.widgets.widget import Widget
from ui.widgets.image import Image
from ui.widgets.text import Text

master_container = Container()
master_container.x = 100
master_container.y = 100

container = Container(parent=master_container)
btn = Button(container, text="Hello World !", border_color=config.BLUE, foreground_color=config.WHITE, border_radius=3, border_width=3)
btn.place()
btn.attachCommand(Button.ON_CLICK_EVENT, lambda : print("Hello World"))
btn2 = Button(container, text="Button test 2 !", border_color=config.RED, foreground_color=config.WHITE)
btn2.setMargins(5, 5, 10, 5)
btn2.setPaddings(5, 5, 5, 5)
btn2.place(Widget.AUTO_RIGHT)
container.place(150, 50, Widget.AUTO_BOTTOM)


container2 = Container(parent=master_container)
image_surface = pygame.transform.scale(pygame.image.load("assets/images/slime/blurping/Slime1.png"), (50, 50))
img = Image(container2, image_surface, background_color=(50, 50, 50, 20), border_width=3, border_radius=3)
img.setMargins(10, 10, 10, 10)
img.place()
text = Text(container2, text="Lv. XXX")
text.setMargins(10, 10, 10, 10)
text.place()
btn4 = Button(container2, text="Buy", border_color=config.GREEN, back_color=(175, 255, 75), foreground_color=(100, 100, 100), border_radius=3, border_width=3)
btn4.attachCommand(Button.ON_CLICK_EVENT, lambda : print("Stop"))
btn4.setPaddings(10, 10, 10, 10)
btn4.setMargins(10, 10, 10, 10)
btn4.place()
container2.place(150, 300, Widget.AUTO_RIGHT)

master_container.place(100, 100, Widget.AUTO_BOTTOM)

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

    # graphic update

    screen.fill((100, 100, 100))

    
    character.collider.debugDraw(screen)
    world.update(deltaTime)
    world.draw(screen)
    character.update(deltaTime)
    master_container.update(deltaTime, is_left_click=left_clicked)
    drawFps(config.clock, (0,0), screen)
    master_container.draw(screen)
    


    for enemy in list(static_list):    
        enemy.update(deltaTime)
        enemy.draw(screen)

        if enemy.collider.isCollisionWithRect(character.collider):
            enemy.onKilled(score=world.main_score)
            static_list.remove(enemy)


    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()