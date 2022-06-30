from game.game import Game
import pygame
import config

# temp import
from physics.collisions.Rectangle2D import Rectangle2D

game = Game()
screen = config.screen

# temp variables test
rectangle = Rectangle2D(10, 10, 20, 50)


while not game.isNeedToClose:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.isNeedToClose = True

    # Fill the background with white
    screen.fill((50, 50, 50))

    rectangle.debugDraw(screen)


    config.clock.tick(config.FPS)
    # Flip the display
    pygame.display.flip()


pygame.quit()