import random
import pygame
from animation.animation import animation
class Chunck:
    def __init__(self):
        self.background = None
        self.path = "./assets/pictures/grass/"
        anim = animation()
        self.grounds_files =  anim.getAllImagesInFolder(self.path)

        self.grounds = {}
        for val in self.grounds_files:
            pygame.transform.scale(val,(126,126))
            self.grounds[val] = self.path + val

        self.ground_lenght = random.randint(50,200)
        self.tiles = []
        self.id = time.time()+self.random.randint(1,100)

        print("chunck id: " + str(self.id))

    @property
    def set_ground(self):
        for i in range(self.ground_lenght):
            grass = random.choice(self.grounds)
            self.tiles.append(pygame.image.load(self.grounds[grass]))
        return self.tiles

    def draw(self,x,y,win):
        all_tiles = self.set_ground()
        i = 0
        for tile in all_tiles:
            i += 126
            win.blit(tile,(x+i,y))
        


