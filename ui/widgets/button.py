from __future__ import annotations

from ui.widgets.widget import Widget
import config
from utils import utils

import pygame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.widgets.container import Container

class Button(Widget):

    MARGIN = 2
    ON_CLICK_EVENT = 0
    ON_HOVER_EVENT = 1

    def __init__(self, container : Container, text="", onclick=None, font=config.H2, border_color=(200, 200, 200, 255), back_color=(50, 50, 50, 255), border_width=1, border_radius=0, foreground_color=(120, 120, 120, 255)):
        super().__init__()

        self.onclick_func = onclick
        self.onhover_func = None
        self.text = text
        self.font = font
        self.back_color = back_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.foreground_color = foreground_color
        self.border_color = border_color
        self.placed = False
        self.container = container
    
    def onClick(self):
        if self.onclick_func != None:
            self.onclick_func()
    
    def onHover(self):
        if self.onhover_func != None:
            self.onhover_func()
    
    def attachCommand(self, type : int, command : function):
        if type == Button.ON_CLICK_EVENT:
            self.onclick_func = command
        elif type == Button.ON_HOVER_EVENT:
            self.onhover_func = command
        else:
            print("couldn't attach the command to the type because the type is not recognized, check Button.ON_eventName events")
    
    def place(self, position_type, position=(0, 0)):
        self.position_type = position_type

        self.calculateDimensions()

        if self.position_type == Widget.ABSOLUTE_POSITION:
            self.x = position[0]
            self.y = position[1]
        elif self.position_type == Widget.AUTO_POSITION:
            self.position = self.container.placeAtBottom(self)
        self.placed = True
    
    def calculateDimensions(self):
        text = self.font.render(self.text, True, self.foreground_color, self.back_color)
        self.h = text.get_height() + self.MARGIN
        self.w = text.get_width() + self.MARGIN

    
    def draw(self, surface):
        text = self.font.render(self.text, True, self.foreground_color)

        x = self.x + self.container.x
        y = self.y + self.container.y
        
        # draw background
        pygame.draw.rect(surface, self.back_color, (x, y, self.w, self.h), border_radius=self.border_radius)

        # draw the border
        pygame.draw.rect(surface, self.border_color, (x, y, self.w, self.h), width=self.border_width, border_radius=self.border_radius)

        #draw the text
        surface.blit(text, (x, y))
    
    def update(self, deltaTime, x_offset, y_offset, left_clicked):
        mouse_pos = pygame.mouse.get_pos()
        x = self.x + x_offset
        y = self.y + y_offset

        if utils.isPointInRect(x, y, self.w, self.h, mouse_pos[0], mouse_pos[1]):
            self.onHover()
            if left_clicked:
                self.onClick()

