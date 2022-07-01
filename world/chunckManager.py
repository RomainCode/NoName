from world.chunck import Chunck
from config import *

class ChunckManager:
    def __init__(self):
        self.chuncks = []
        self.unload_chuncks = []
        self.add_chunck()


    def back(self):
        for chunck in self.chuncks:
            if chunck.passed_left:
                self.chuncks.remove(chunck)
                print(self.chuncks)
            elif chunck.passed_right:
                if chunck not in self.unload_chuncks:
                    self.add_chunck(offsetX=WIDTH)
                    self.chuncks[-1].offsetX = WIDTH
                    self.chuncks[-2].offsetX = -len(self.chuncks[-2].map[0])*self.chuncks[-2].img_size + WIDTH


                    self.unload_chuncks.append(chunck)
              
    def add_chunck(self, offsetX = 0):
        chunck = Chunck(64, "./world/map sets/map_test.csv", offsetX)
        self.chuncks.append(chunck)

    def update_chuncks(self, deltaTime):
        for chunck in self.chuncks:
            chunck.update(deltaTime) 

    def draw_chuncks(self, screen):
        for chunck in self.chuncks:
            chunck.draw(screen)

 
