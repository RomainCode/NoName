from ui.widgets.widget import Widget
from ui.widgets.widget import ButtonComp, BorderComp
from ui.widgets.button import Button

import pygame

class Container(Widget):

    DRAW_DEBUG_RECTS = False
    
    def __init__(self, parent=None, position_type=Widget.AUTO_RIGHT):
        super().__init__(parent)
        self.widgets = []
        self.position_type = position_type
    
    def addWidget(self, widget):
        if widget not in self.widgets:
            self.widgets.append(widget)

    
    def link(self, x, y):
        self.setPosition(x, y)
        if self.container is not None:
            self.container.addWidget(self)
            if self.position_type == Widget.AUTO_BOTTOM:
                self.y = self.container.getHeight()
                self.x = 0
            elif self.position_type == Widget.AUTO_RIGHT:
                self.x = self.container.getWidth()
                self.y = 0
            else:
                raise BaseException("Unknown organization type "+str(self.position_type))
        self.setDimensions()
    
    def setDimensions(self, fixed=None):
        if fixed == None:
            self.w, self.h = self.getWidth(), self.getHeight()
        else:
            self.w, self.h = fixed
    
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        self.placed = True
        self.calculateEachChildPositions()


    def copyAndAssign(self, x=0, y=0, parent=None):
        new_container = Container(parent=parent)
        for widget in self.widgets:
            new_container.addWidget(widget)
        new_container.position_type = self.position_type
        new_container.calculateEachChildPositions()
        return new_container


    def getHeight(self):
        if self.position_type == Widget.AUTO_BOTTOM:
            h = 0
            widget : Widget
            for widget in self.widgets:
                h += widget.getTotalHeight()
            return h
        elif self.position_type == Widget.AUTO_RIGHT:
            h = 0
            widget : Widget
            for widget in self.widgets:
                h = max(h, widget.getTotalHeight())
            return h
        else:
            raise NotImplemented("Can't calculate this container height")
        
    def getWidth(self):
        if self.position_type == Widget.AUTO_BOTTOM:
            w = 0
            widget : Widget
            for widget in self.widgets:
                w = max(w, widget.getTotalWidth())
            return w

        elif self.position_type == Widget.AUTO_RIGHT:
            w = 0
            widget : Widget
            for widget in self.widgets:
                w += widget.getTotalWidth()
            return w
        else:
            raise NotImplemented("Can't calculate this container width")
        
    def calculateEachChildPositions(self):
        """Tells all the widgets what their positions are compared to the container or to the screen"""
        
        # Auto positions
        if self.position_type == Widget.AUTO_BOTTOM:
            y_offset = 0
            widget : Widget
            for widget in self.widgets:
                widget.y = y_offset
                widget.x = 0
                if widget.__class__ != Container:
                    widget.position_type = self.position_type
                y_offset += widget.getTotalHeight()
        
        elif self.position_type == Widget.AUTO_RIGHT:
            x_offset = 0
            widget : Widget
            for widget in self.widgets:
                if widget.__class__ != Container:
                    widget.position_type = self.position_type
                widget.x = x_offset
                widget.y = 0
                x_offset += widget.getTotalWidth()
        
        # Abssolute positions
        elif self.position_type == Widget.ABSOLUTE_POSITION:
            widget : Widget
            for widget in self.widgets:
                widget.x = widget.absolute_position[0] + self.x
                widget.y = widget.absolute_position[1] + self.y
                if widget.__class__ != Container:
                    widget.position_type = self.position_type

        # Fixed positions
        elif self.position_type == Widget.ABSOLUTE_POSITION:
            widget : Widget
            for widget in self.widgets:
                widget.x = widget.fixed_position[0]
                widget.y = widget.fixed_position[1]
                if widget.__class__ != Container:
                    widget.position_type = self.position_type
        
        else:
            raise BaseException("Unknown organization type "+str(self.position_type))
                
    
    def draw(self, surface, x_off=0, y_off=0):

        if Container.DRAW_DEBUG_RECTS == True:
            pygame.draw.rect(surface, (255, 0, 0), (self.x+x_off+self.left_margin, self.y+y_off+self.top_margin, self.w, self.h), width=1)

        if not self.placed:
            raise BaseException("couldn't draw this container because it has not been placed")

        for widget in self.widgets:
            if not widget.placed:
                raise BaseException("couldn't draw this widget because it has not been placed "+str(widget))

            widget.draw(surface, x_off+self.x+self.left_margin+self.left_padding, y_off+self.y+self.top_margin+self.top_padding)
    
        for component in self.components:
            if component.__class__ == BorderComp:
                component.draw(surface, self, x_off+self.x+self.left_margin, y_off+self.y+self.top_margin)

    def update(self, deltaTime, is_left_click=False, x_off=0, y_off=0):

        for component in self.components:
            if component.__class__ == ButtonComp:
                component.update(self.isHovering(x_off, y_off), is_left_click)
        
        if not self.placed:
            raise BaseException("couldn't update this container because it has not been placed")
        
        for widget in self.widgets:
            if not widget.placed:
                raise BaseException("couldn't update this widget because it has not been placed "+str(widget))
            if widget.__class__ == Button:
                widget : Button
                widget.update(deltaTime, x_off=x_off+self.x, y_off=y_off+self.y, left_clicked=is_left_click)
            if widget.__class__ == Container:
                widget.update(deltaTime, x_off=x_off+self.x, y_off=y_off+self.y, is_left_click=is_left_click)