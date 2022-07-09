import random

from world.chunck import Chunck
from config import *
import os
import re
import csv


class ChunckManager:
    """Stores chunks and auto generation/deletion when needed
       to change biome use ChunckManager.current_biome = "BIOME"
    """
    FANTASY = "fantasy"

    def __init__(self):
        self.chuncks = []
        self.unload_chuncks = []
        self.maps_path = "./world/map sets/"
        self.maps = self.get_allmaps()
        self.csv = {}
        for map_ in self.maps:
         self.csv[map_] = list(csv.reader(open(map_)))

      
        self.biomes = {}
        self.map_biome()
        self.current_biome = "fantasy"
        self.add_chunck()

    def add_chunck(self, offsetX=0):
        """this function create a chunck"""
        rdm = random.choice(self.biomes[self.current_biome])
        
        chunck = Chunck(64, rdm[0] , offsetX, offsetY=10*64)
        self.chuncks.append(chunck)

    def update_chuncks(self, deltaTime):
        """update chuncks positions"""
        for chunck in self.chuncks:
            chunck.update(deltaTime)

    def back(self): 
        """ handle the suppression of a past chunk and the generation of a new one, preserves continuity in the tiles"""
        for chunck in self.chuncks:
            if chunck.passed_left:
                self.chuncks.remove(chunck)
            elif chunck.passed_right:
                if chunck not in self.unload_chuncks:
                    self.add_chunck(offsetX=WIDTH)
                    self.chuncks[-1].offsetX = WIDTH
                    self.chuncks[-2].offsetX = -len(self.chuncks[-2].map[0]) * self.chuncks[-2].img_size + WIDTH
                    self.unload_chuncks.clear()
                    self.unload_chuncks.append(chunck)  # pourquoi sotcker les chuncks unload ?

   

    def get_allmaps(self) -> list:
        """ return a list with all path of maps"""

        result = []
        maps_list = next(os.walk(self.maps_path), (None, None, []))[2]  # [] if no file is found
        for maps in maps_list:
            if maps[-4:len(maps)] == ".csv":
                result.append(self.maps_path + maps)

        return result

    def map_biome(self) -> dict:
        """this function permit to make distinction between all maps, and put them in a dictionnary"""
        for maps in self.maps:
            args = maps.split("__")
            if args[1] not in self.biomes:
                self.biomes[args[1]] = [[maps, args[2]]]
            else:
                self.biomes[args[1]].append([maps,args[2]])
                
    def update(self, deltaTime):
        """handle add/deleting chunks
           update the inner chuncks
        """
        self.back()
        self.update_chuncks(deltaTime)

    def draw(self, screen):
        """draw the map
        """
        for chunck in self.chuncks:
            chunck.draw(screen)
