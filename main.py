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
from ui.widgets.widget import ButtonComp, BorderComp
from ui.widgets.image import Image
from ui.widgets.text import Text


menue_container = Container(position_type=Widget.AUTO_BOTTOM)

container = Container(position_type=Widget.AUTO_RIGHT, parent=menue_container)
image_surface = pygame.transform.scale(pygame.image.load("assets/images/slime/blurping/Slime1.png"), (50, 50))
img = Image(container, image_surface, background_color=(50, 50, 50, 20), border_width=3, border_radius=3, border_color=(25, 25, 25))
img.link()

## text container
text_container = Container(parent=container, position_type=Widget.AUTO_BOTTOM)

level_text = Text(text_container, "Lvl. XXX", config.H2)
name_text = Text(text_container, "Slime", config.H4, (200, 200, 200, 255))

text_container.link(0, 0)
text_container.setMargins(10, 10, 0, 0)

next_upgrade_container = Container(container, position_type=Widget.AUTO_BOTTOM)
text_2 = Text(next_upgrade_container, "+ 6", font=config.H4)
text_3 = Text(next_upgrade_container, "PPS", font=config.H4)
next_upgrade_container.link(0, 0)


## btn
buy_comtainer = Container(parent=container, position_type=Widget.AUTO_BOTTOM)
buy_text = Text(buy_comtainer, "Buy 1", config.H3)
price = Text(buy_comtainer, "1.24 M", config.H3)

btn_comp = ButtonComp()
btn_comp.on_click_fn = lambda : print("Clicked !")
buy_comtainer.addComponent(btn_comp)

border = BorderComp(3, 5, (200, 100, 100))
buy_comtainer.addComponent(border)

buy_comtainer.setMargins(10, 10, 10, 10)
buy_comtainer.setPaddings(5, 5, 5, 5)
buy_comtainer.link(0, 0)


container.setMargins(10, 10, 10,)
container.link(150, 300)


container_bis = container.copyAndAssign(parent=menue_container)
container_bis.setMargins(10, 10, 10,)
container_bis.link(0, 0)

menue_container.link(300, 100)


img.setAlignment(Widget.VIERTICAL_ALIGN)
text_container.setAlignment(Widget.VIERTICAL_ALIGN)
next_upgrade_container.setAlignment(Widget.VIERTICAL_ALIGN)
buy_comtainer.setAlignment(Widget.VIERTICAL_ALIGN)

########## How to code with widgets ##########

### Diferents objects all coming from a Widget class
## Widget class
# contain the rectangle of the object, margins, paddins, position_type, alignement...

### How to implement a Text with his container
# container = Container(parent=None) -> initialize the Container
# 
# text = Text(container, text="Coucou") -> initialize the Text object and point it to the container
# text.place() -> set the x and y of the widget, adds it to the container widgets list
# 
# container.link(10, 20)


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
    menue_container.update(deltaTime, is_left_click=left_clicked)
    drawFps(config.clock, (0,0), screen)
    menue_container.draw(screen)
    


    for enemy in list(static_list):    
        enemy.update(deltaTime)
        enemy.draw(screen)

        if enemy.collider.isCollisionWithRect(character.collider):
            enemy.onKilled(score=world.main_score)
            static_list.remove(enemy)


    config.clock.tick(config.FPS)
    pygame.display.flip()


pygame.quit()