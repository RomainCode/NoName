from world.chuncks import *
class ChunckManager:
    def __init__(self):
        self.chuncks = {}

    def add_chunck(self):
        chunck = Chunck()
        self.chuncks[chunck.id] = chunck