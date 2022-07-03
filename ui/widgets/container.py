from ui.widgets.widget import Widget
from ui.widgets.button import Button

import pygame

class Container(Widget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.widgets = []

        self.x = 0
        self.y = 0
        self.placed = False

        self.organization_type = None
    
    def addWidget(self, widget):
        self.widgets.append(widget)

    def place(self, x, y, type):
        self.x = x
        self.y = y
        self.placed = True
        self.organization_type = type
        self.updateRelativePositions()

    def placeAtBottom(self, widget : Widget):
        widget.y = self.getHeight()

        self.widgets.append(widget)

    def getHeight(self):
        if self.organization_type == Widget.AUTO_BOTTOM:
            h = 0
            widget : Widget
            for widget in self.widgets:
                h += widget.getTotalHeight()
            return h
        else:
            return 0
        
    def updateRelativePositions(self):
        """Tells all the widgets what their positions are compared to the container or to the screen"""
        
        # Auto positions
        if self.organization_type == Widget.AUTO_BOTTOM:
            y_offset = 0
            widget : Widget
            for widget in self.widgets:
                widget.y = y_offset
                widget.position_type = self.organization_type
                y_offset += widget.getTotalHeight()
        
        elif self.organization_type == Widget.AUTO_RIGHT:
            x_offset = 0
            widget : Widget
            for widget in self.widgets:
                widget.x = x_offset
                x_offset += widget.getTotalWidth()
        
        # Abssolute positions
        elif self.organization_type == Widget.ABSOLUTE_POSITION:
            widget : Widget
            for widget in self.widgets:
                widget.x = widget.absolute_position[0] + self.x
                widget.y = widget.absolute_position[1] + self.y
                widget.position_type = self.organization_type

        # Fixed positions
        elif self.organization_type == Widget.ABSOLUTE_POSITION:
            widget : Widget
            for widget in self.widgets:
                widget.x = widget.fixed_position[0]
                widget.y = widget.fixed_position[1]
                widget.position_type = self.organization_type
        
        else:
            raise BaseException("Unknown organization type "+self.organization_type)
                

        
    def getWidth(self):
        if self.organization_type == Widget.AUTO_BOTTOM:
            w = 0
            widget : Widget
            for widget in self.widgets:
                w = max(w, widget.getTotalWidth())
            return w
        return 0
    
    def draw(self, surface):

        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.getWidth(), self.getHeight()), width=1)

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

class VsisibleContainer(Container):
    def __init__(self,  border_color=(200, 200, 200, 255), back_color=(50, 50, 50, 255), border_width=1, border_radius=0, foreground_color=(120, 120, 120, 255)):
        super().__init__()
        self.back_color = back_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.foreground_color = foreground_color
        self.border_color = border_color
    
    def draw(self, surface):
        if not self.placed:
            raise BaseException("couldn't draw this container because it has not been placed")

        # calculate container width and height
        # draw the rectangle

        for widget in self.widgets:
            if not widget.placed:
                raise BaseException("couldn't draw this widget because it has not been placed "+str(widget))
            widget.draw(surface)

