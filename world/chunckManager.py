from world.chunck import Chunk


class ChunckManager:
    def __init__(self):
        self.chuncks = {}

    def add_chunck(self):
        chunck = Chunk()
        self.chuncks[chunck.id] = chunck