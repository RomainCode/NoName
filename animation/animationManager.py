from animation.animation import Animation

class AnimationManager:
    def __init__(self):
        self.current_animation_name = ""
        self.current_animation : Animation = None
        self.animation_map = {}
    
    def getCurrentImage(self):
        if self.current_animation != None:
            return self.current_animation.getCurrentImage()
        else:
            raise ValueError("No animation selected, can't get an image")
    
    def update(self, deltaTime):
        if self.current_animation != None:
            self.current_animation.update(deltaTime)

    def addAnimation(self, key : str, animation : Animation):
        self.animation_map[key] = animation
    
    def removeAnimation(self, key : str):
        self.animation_map.remove(key)
    
    def getAnimation(self, key : str) -> Animation:
        return self.animation_map[key]
    
    def setToCurrentAnimation(self, key : str):
        self.current_animation = self.animation_map[key]
        self.current_animation_name = key
    
    def play(self):
        if self.current_animation != None:
            self.current_animation.play()
        else:
            raise ValueError("No animation selected")

    def play(self, key : str):
        self.setToCurrentAnimation(key)
        self.current_animation.play()
    
    def pause(self):
        if self.current_animation != None:
            self.current_animation.pause()
        else:
            raise ValueError("No animation selected")
    
    def pause(self, key : str):
        self.setToCurrentAnimation(key)
        self.current_animation.pause()
    
    def resume(self):
        if self.current_animation != None:
            self.current_animation.resume()
        else:
            raise ValueError("No animation selected")
    
    def resume(self, key : str):
        self.setToCurrentAnimation(key)
        self.current_animation.resume()
