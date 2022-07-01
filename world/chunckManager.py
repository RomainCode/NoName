from world.chunck import Chunck
from config import *

class ChunckManager:
    """Stores chunks and auto generation/deletion when needed"""
    def __init__(self):
        self.chuncks = []
        self.unload_chuncks = []
        self.add_chunck()

    
    def update(self, deltaTime):
        # handle add/deleting chunks
        self.back()
        # update the inner chuncks
        self.update_chuncks(deltaTime)

    def draw(self, screen):
        for chunck in self.chuncks:
            chunck.draw(screen)
    

    def add_chunck(self, offsetX = 0):
        chunck = Chunck(64, "./world/map sets/map_test.csv", offsetX)
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
                    self.unload_chuncks.append(chunck) # pourquoi sotcker les chuncks unloadé ?

 
