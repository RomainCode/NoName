from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.widgets.container import Container

import pygame

from utils import utils

class Widget:

    FIXED_POSITION = 0 # to the screen
    ABSOLUTE_POSITION = 1 # to the container
    AUTO_BOTTOM = 2 # auto in the container
    AUTO_RIGHT = 3 # auto in the container

    VERTICAL_FILLING = 4 # playing with the padding top/bottom
    HORIZONTAL_FILLING = 5 # playing with the padding left/right
    
    VIERTICAL_ALIGN = 6 # playing width the margin top/bottom
    HORIZONTAL_ALIGN = 7 # playing with the margin top/bottom

    NULL = 8

    def __init__(self, container : Container):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.position_type = None
        self.container = None
        self.placed = False
        self.warn = True
        self.container : Container = container
        self.components = []

        # optionals
        self.absolute_position = [0, 0]
        self.fixed_position = [0, 0]

        # padding
        self.left_padding = 0
        self.right_padding = 0
        self.top_padding = 0
        self.bottom_padding = 0

        # margin
        self.left_margin = 0
        self.right_margin = 0
        self.top_margin = 0
        self.bottom_margin = 0

    def addComponent(self, component):
        self.components.append(component)
    
    def setAlignment(self, alignment):
        if self.container != None:
            if alignment == Widget.VIERTICAL_ALIGN:
                self.top_margin = (self.container.getHeight()-self.h)/2
                self.bottom_margin = self.top_margin
            elif alignment == Widget.VERTICAL_FILLING:
                self.top_padding = (self.container.getHeight()-self.h)/2
                self.bottom_padding = self.top_padding
                self.top_margin = 0
                self.bottom_margin = 0
            elif alignment == Widget.HORIZONTAL_ALIGN:
                self.left_margin = (self.container.getWidth()-self.w)/2
                self.right_margin = self.left_margin
        else:
            print("This widget does not have a parent container, can't align it")
    
    def getTotalWidth(self):
        return self.w + self.left_margin + self.right_margin + self.left_padding + self.right_padding
    
    def getTotalHeight(self):
        return self.h + self.top_margin + self.bottom_margin + self.top_padding + self.bottom_padding

    def setMargins(self, left=0, right=0, top=0, bottom=0):
        if self.warn:
            if self.placed and self.position_type == Widget.AUTO_BOTTOM:
                print("Warning : Errors may occurs when resizing a widgets that is already placed in a container")
        self.left_margin = left
        self.right_margin = right
        self.top_margin = top
        self.bottom_margin = bottom
    
    def setPaddings(self, left=0, right=0, top=0, bottom=0):
        self.left_padding = left
        self.right_padding = right
        self.top_padding = top
        self.bottom_padding = bottom
    
    def __str__(self):
        return f"coords : (x={self.x}, y={self.y}), margins : (left={self.left_margin}, right={self.right_margin}, top={self.top_margin}, bottom={self.bottom_margin})"

    def isHovering(self, x_off=0, y_off=0) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        if self.position_type == Widget.AUTO_BOTTOM or self.position_type == Widget.AUTO_RIGHT:
            x = self.x + x_off + self.left_margin
            y = self.y + y_off + self.top_margin
        
        if self.position_type == Widget.ABSOLUTE_POSITION or self.position_type == Widget.FIXED_POSITION:
            raise NotImplemented("ABSOLUTE_POSITION and FIXED_POSITION are not yet totally implemented. Please use AUTO_BOTTOM or AUTO_RIGHT")

        if utils.isPointInRect(x, y, self.w+self.left_padding+self.right_padding, self.h+self.top_padding+self.bottom_padding, mouse_pos[0], mouse_pos[1]):
            return True
        else:
            return False



class ButtonComp:

    def __init__(self):
        self.on_click_fn = None
        self.on_hover_fn = None
        self.on_hover_off = None

    def update(self, is_collision, is_clicked):
        if is_collision:
            if self.on_hover_fn != None:
                self.on_hover_fn()
            if is_clicked:
                if self.on_click_fn != None:
                    self.on_click_fn()

class BorderComp:
    def __init__(self, border_width, border_radius, border_color):
        self.border_radius = border_radius
        self.border_width = border_width
        self.border_color = border_color
    
    def draw(self, surface, widget : Widget, x, y):
        pygame.draw.rect(surface, self.border_color, (x, y, widget.w+widget.right_margin, widget.h+widget.bottom_margin), self.border_width, self.border_radius)

