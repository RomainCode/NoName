from ui.widgets.widget import Widget
from ui.widgets.button import Button

class Container:
    
    def __init__(self):
        self.widgets = []

        self.x = 0
        self.y = 0
        self.placed = False
    
    def place(self, x, y):
        self.x = x
        self.y = y
        self.placed = True
    
    def autoPosition(self):
        pass

    def placeAtBottom(self, widget : Widget, margin=2):
        y_buffer = 0
        w : Widget
        for w in self.widgets:
            if w.position_type != Widget.ABSOLUTE_POSITION:
                y_buffer += w.h + 2+2
            else:
                raise BaseException("Can't position differents position's types in the same container")
        
        widget.y = y_buffer

        self.widgets.append(widget)

    
    def draw(self, surface):

        if not self.placed:
            raise BaseException("couldn't draw this container because it has not been placed")

        for widget in self.widgets:
            if not widget.placed:
                raise BaseException("couldn't draw this widget because it has not been placed "+str(widget))
            widget.draw(surface)
    
    def update(self, deltaTime, is_left_click=False):
        if not self.placed:
            raise BaseException("couldn't update this container because it has not been placed")
        
        for widget in self.widgets:
            if not widget.placed:
                raise BaseException("couldn't update this widget because it has not been placed "+str(widget))
            if widget.__class__ == Button:
                widget : Button
                widget.update(deltaTime, self.x, self.y, is_left_click)