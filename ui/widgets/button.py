from __future__ import annotations

from ui.widgets.widget import Widget
from ui.widgets.widget import ButtonComp
import config
from utils import utils

import pygame, random

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ui.widgets.container import Container

class Button(Widget):


    ON_CLICK_EVENT = 0
    ON_HOVER_EVENT = 1

    def __init__(self, container : Container, text="", onclick=None, font=config.H2, border_color=(200, 200, 200, 255), back_color=(50, 50, 50, 255), border_width=1, border_radius=0, foreground_color=(120, 120, 120, 255)):
        super().__init__(container)

        self.text = text
        self.font = font
        self.back_color = back_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.foreground_color = foreground_color
        self.border_color = border_color
        self.placed = False

        self.button_comp = ButtonComp()
        self.button_comp.on_click_fn = onclick
        self.button_comp.on_hover_fn = onHoverBasic

        self.link()

    def onClick(self):
        if self.onclick_func != None:
            self.onclick_func()
    
    def onHover(self):
        if self.onhover_func != None:
            self.onhover_func()
    
    def attachCommand(self, type : int, command : function):
        if type == Button.ON_CLICK_EVENT:
           self.button_comp.on_click_fn = command
        elif type == Button.ON_HOVER_EVENT:
            self.button_comp.on_hover_fn = command
        else:
            print("couldn't attach the command to the type because the type is not recognized, check Button.ON_eventName events")
    
    def link(self):
        self.setDimensions()
        self.placed = True
        self.container.addWidget(self)
    
    def setDimensions(self, fixed=None):
        if fixed == None:
            self.w, self.h = self.calculateRawDimensions()
        else:
            self.w, self.h = self.fixed
    
    def calculateRawDimensions(self):
        text = self.font.render(self.text, True, self.foreground_color, self.back_color)
        return text.get_width(), text.get_height()

    
    def draw(self, surface, x_off, y_off):
        text = self.font.render(self.text, True, self.foreground_color)

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
        
        # draw background
        pygame.draw.rect(surface, self.back_color, (x, y, self.w+self.left_padding+self.right_padding, self.h+self.top_padding+self.bottom_padding), border_radius=self.border_radius)

        # draw the border
        pygame.draw.rect(surface, self.border_color, (x, y, self.w+self.left_padding+self.right_padding, self.h+self.top_padding+self.bottom_padding), width=self.border_width, border_radius=self.border_radius)

        #draw the text
        surface.blit(text, (x+self.left_padding, y+self.top_padding))
    
    def update(self, deltaTime, x_off=0, y_off=0, left_clicked=False):
        
        if self.isHovering(x_off, y_off):
            self.button_comp.update(is_collision=True, is_clicked=left_clicked)


def onHoverBasic():
    pass
    
def offHoverBasic():
    pass