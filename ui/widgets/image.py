from __future__ import annotations

from ui.widgets.widget import Widget
import config
from utils import utils

import pygame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.widgets.container import Container

class Image(Widget):

    def __init__(self, container : Container, image : pygame.Surface = None, background_color=(0, 0, 0, 0), border_width=0, border_radius=0, border_color=(0, 0, 0, 0)):
        super().__init__(container)
        self.image = image
        self.background_color = background_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.border_color = border_color
    

    def place(self, position=(0, 0)):
        self.w, self.h = self.calculateRawDimensions()
        self.placed = True
        self.container.addWidget(self)

    def calculateRawDimensions(self) -> tuple:
        return self.image.get_width(), self.image.get_height()
    
    def draw(self, surface, x_off, y_off):
        
        if self.position_type == Widget.AUTO_BOTTOM or self.position_type == Widget.AUTO_RIGHT:
            x = self.x + x_off + self.left_margin
            y = self.y + y_off + self.top_margin
        elif self.position_type == Widget.ABSOLUTE_POSITION:
            x = self.x
            y = self.y
        elif self.position_type == Widget.FIXED_POSITION:
            x = self.x
            y = self.y
        elif self.position_type == None:
            raise BaseException("Can't position an undefined position type widget")

        # draw the background
        if self.background_color[3] != 0:
            pygame.draw.rect(surface, self.background_color, (x, y, self.w, self.h), border_radius=self.border_radius)

        # draw the image
        surface.blit(self.image, (x+self.left_padding, y+self.top_padding))

        # draw the border
        if self.border_width != 0:
            pygame.draw.rect(surface, self.border_color, (x, y, self.w, self.h), width=self.border_width, border_radius=self.border_radius)

