import random
import pygame
import time

import config
from animation.animation import Animation as animation
import csv




def load_tileset(filename, width, height) -> list:
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tileset = []
    for tile_x in range(0, image_width//width):
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            tileset.append(image.subsurface(rect))
    return tileset

def strip_from_sheet(sheet, start, size):
    frames = []
    img_width = sheet.get_width()
    img_height = sheet.get_height()
    columns = img_width // size[0]
    rows = img_height // size[1]
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pygame.Rect(location, size)))
    return frames

def resize_tileset(tileset, width, height) -> list:
    new_tileset = []
    for image in tileset:
        new_img = pygame.transform.scale(image, (width, height))
        new_tileset.append(new_img)
    return new_tileset


class Chunck:

    SPEED = config.BASE_SPEED

    TileSet = strip_from_sheet(pygame.image.load("./assets/images/tileset.png"), (0, 0), (16, 16))
    TileSet = resize_tileset(TileSet, 64, 64)

    def __init__(self, img_size: int, mapset_csv_path: str, offsetX = 0):
        anim = animation()
        self.id = int(time.time() / 500 + random.randint(1, 100))
        self.img_size = img_size
        self.map = list(csv.reader(open(mapset_csv_path)))
        
        self.offsetX = offsetX
        self.passed_right = False
        self.passed_left  = False
        self.generate()


    def generate(self):

        variations ={"grass": ["0", "1","3"], "dirt":["2"]}

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "0": # => grass
                    self.map[y][x] = random.choice(variations["grass"])
                    
                if self.map[y][x] == "2": # => dirt
                    self.map[y][x] = random.choice(variations["dirt"])

       

    def draw(self, surface: pygame.Surface):
        y = 0
        for row in self.map:
            x = 0
            for tile in row:
                if tile != "-1":
                    surface.blit(Chunck.TileSet[int(tile)], (x * self.img_size + self.offsetX, y * self.img_size+config.HEIGHT-config.GROUND_MARGIN+config.PLAYER_HEIGHT))
                x += 1
            y += 1
    
    def update(self, deltaTime):
        self.offsetX = self.offsetX - deltaTime*Chunck.SPEED
        if self.offsetX <= -len(self.map[0])*self.img_size + config.WIDTH: # when out of chunck from right side 
            self.passed_right = True
        if self.offsetX <= -len(self.map[0])*self.img_size: # when out of chunck from the left side
            self.passed_left = True
    


