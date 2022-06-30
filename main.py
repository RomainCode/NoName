from game.game import Game
import pygame
import config

game = Game()

while not game.isNeedToClose:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.isNeedToClose = True

    # Fill the background with white
    config.screen.fill((255, 255, 255))


    config.clock.tick()
    # Flip the display
    pygame.display.flip()


pygame.quit()