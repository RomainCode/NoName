import pygame
import time
import os

# types : Ponctual, Timed
# states : Playing, Paused, Stopped


class Animation:

    ## Enum
    PLAYING = 0
    STOPPED = 1
    PAUSED = 2
    PONCTUAL = 3
    TIMED = 4
    ##

    def __init__(self):
        self.images = []
        self.pointer = 0
        self.last_time = 0
        self.time_btw_frames = 500
        self.type = Animation.TIMED
        self.state = Animation.PLAYING

    def setInterval(self, t : int):
        self.time_btw_frames = t
    
    def setState(self, state : int):
        self.state = state
    
    def setType(self, type : int):
        self.type = type

    def pause(self):
        self.state = Animation.PAUSED
    
    def resume(self):
        if self.state == Animation.PAUSED:
            self.state = Animation.PLAYING
    
    def replay(self):
        self.pointer = 0
        self.state = Animation.PLAYING
    
    def resetFlag(self):
        if self.type == Animation.PONCTUAL:
            self.state = Animation.STOPPED
    
    def updateTimedAnimation(self, deltaTime):
        if time.time() > self.last_time + self.time_btw_frames:
            self.setToNextFrame()
            self.last_time = time.time()

    def updatePonctualAnimation(self, deltaTime):
        pass

    def update(self, deltaTime):
        if self.state == Animation.PLAYING:
            if self.type == Animation.TIMED:
                self.updateTimedAnimation()
            else:
                pass # updat ponctual anim

    def getCurrentImage(self):
        if len(self.images) == 0:
            raise ValueError("No images stored in this animation, can't get an image")
        if self.pointer > len(self.images)+1 or self.pointer < 0:
            raise ValueError("Image pointer out of reach")
        return self.images[self.pointer]
    
    def setToNextFrame(self) -> None:
        if self.pointer + 1 > len(self.images):
            self.resetFlag()
            if self.type == Animation.PONCTUAL:
                return
        self.pointer = (self.pointer + 1) % len(self.images)
        


    def getAllImagesInFolder(self,path : str) -> list:
        """
        return for all images in directory with all path as a list
        ex list:['./assets/slime/Slime1.png', './assets/slime/Slime2.png']

        """
        result = []
        a = next(os.walk(path), (None, None, []))[2]  # [] if no file is found
        for image in a:
            result.append(path+image)
        
        print(result)
        return result
    

    def adImageByPath(self, path : str):
        img = pygame.image.load(path)
        self.images.append(img)
        
