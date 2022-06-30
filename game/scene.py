import pygame


class Scene:

    def __init__(self):
        pass

    def handleEvents(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.isNeedToClose = True