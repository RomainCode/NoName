import random
import pygame
import time

import config
from animation.animation import Animation as animation
import csv




def load_tileset(filename: str, width: int, height: int) -> list:
    """load tile sheet from a given file"""
    image = pygame.image.load(filename).convert()
    image_width, image_height = image.get_size()
    tileset = []
    for tile_x in range(0, image_width//width):
        for tile_y in range(0, image_height//height):
            rect = (tile_x*width, tile_y*height, width, height)
            tileset.append(image.subsurface(rect))
    return tileset

def strip_from_sheet(sheet: pygame.Surface, start: int, size: int) -> list:
    """from imported sheet it cut all image with a given size"""

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

def resize_tileset(tileset: list[pygame.Surface], width: int, height: int) -> list:
    """Resize all tiles from a tileset list"""

    new_tileset = []
    for image in tileset:
        new_img = pygame.transform.scale(image, (width, height))
        new_tileset.append(new_img)
    return new_tileset


class Chunck:
    """It's the object that represents the moving scenery
       ex: Chunck(64,"world/map_set/__fantasy__0_1.csv")
    """
    
    SPEED = config.BASE_SPEED

    TileSet = strip_from_sheet(pygame.image.load("./assets/images/tileset.png"), (0, 0), (16, 16))
    TileSet = resize_tileset(TileSet, 64, 64)

    def __init__(self, img_size: int, mapset_csv_path: str, offsetX = 0, offsetY=5):
       
        anim = animation()
        self.id = int(time.time() / 500 + random.randint(1, 100))
        self.img_size = img_size
        self.map = list(csv.reader(open(mapset_csv_path)))
        
        self.offsetX = offsetX
        self.passed_right = False
        self.passed_left  = False
        self.generate()
        self.offsetY= offsetY

    def generate(self) -> list[list]:
        """this function manage textures variations, it need a csv in order to work"""
        # dirt 5 == ore
        # dirt 2 == basic dirt
        
        final_dirt = []
        final_grass = []
        dirt = [["2" for i in range(92)],["5" for i in range(8)]]
        grass = [["0" for i in range(33)],["1" for i in range(33)],["3" for i in range(33)]]
        for dirts in dirt:
            final_dirt.extend(dirts)
        for grasses in grass:
            final_grass.extend(grasses)
        variations ={"grass": final_grass, "dirt": final_dirt}

        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == "0": # => grass
                    self.map[y][x] = random.choice(variations["grass"])
                    
                if self.map[y][x] == "2": # => dirt
                    self.map[y][x] = random.choice(variations["dirt"])

       

    def draw(self, surface: pygame.Surface):
        """draw all tiles"""
        y = 0
        for row in self.map:
            x = 0
            for tile in row:
                if tile != "-1":
                    surface.blit(Chunck.TileSet[int(tile)], (x * self.img_size + self.offsetX, y * self.img_size+config.HEIGHT-config.GROUND_MARGIN-self.offsetY+ config.PLAYER_HEIGHT))
                x += 1
            y += 1
    
    def update(self, deltaTime):
        """update positions of each tiles"""
        self.offsetX = self.offsetX - deltaTime*Chunck.SPEED
        if self.offsetX <= -len(self.map[0])*self.img_size + config.WIDTH: # when out of chunck from right side 
            self.passed_right = True
        if self.offsetX <= -len(self.map[0])*self.img_size: # when out of chunck from the left side
            self.passed_left = True
    


