from world.chunck import Chunck
from config import *
import os
import re

class ChunckManager:
    """Stores chunks and auto generation/deletion when needed"""
    FANTASY = "fantasy"
    def __init__(self):
        self.chuncks = []
        self.unload_chuncks = []
        self.add_chunck()
        self.maps_path = "./world/map sets/"
        self.maps = self.get_allmaps()
        self.maps_biomes = {}        
        self.map_biome()
    


    def add_chunck(self, offsetX = 0):
        chunck = Chunck(64,"./world/map sets/__fantasy__1.csv", offsetX)
        self.chuncks.append(chunck)

    def update_chuncks(self, deltaTime):
        for chunck in self.chuncks:
            chunck.update(deltaTime) 

    def back(self): # handle the suppression of a past chunk and the generation of a new one, preserves continuity in the tiles
        for chunck in self.chuncks:
            if chunck.passed_left:
                self.chuncks.remove(chunck)
            elif chunck.passed_right:
                if chunck not in self.unload_chuncks:
                    self.add_chunck(offsetX=WIDTH)
                    self.chuncks[-1].offsetX = WIDTH
                    self.chuncks[-2].offsetX = -len(self.chuncks[-2].map[0])*self.chuncks[-2].img_size + WIDTH
                    self.unload_chuncks.clear()
                    self.unload_chuncks.append(chunck) # pourquoi sotcker les chuncks unload ?

    
    def switch_chunck(self):
        pass
    
    def get_allmaps(self):
        result = []
        maps_list = next(os.walk(self.maps_path), (None, None, []))[2]  # [] if no file is found
        for maps in maps_list:
            if maps[-4:len(maps)] == ".csv":
             result.append(self.maps_path+maps)
    
        return result
    
    def map_biome(self):
        for maps in self.maps:

             #pattern = re.compile(r"__[a-zA-Z]+__", re.IGNORECASE)
             #m = pattern.match(maps, pattern)
             #print(m)
             pass
        
            
    def update(self, deltaTime):
        # handle add/deleting chunks
        self.back()
        # update the inner chuncks
        self.update_chuncks(deltaTime)


    def draw(self, screen):
        for chunck in self.chuncks:
            chunck.draw(screen)
    