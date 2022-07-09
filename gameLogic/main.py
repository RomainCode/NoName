from xml.dom.minidom import Element
import pygame
import config
from utils import utils

class MenueContainer:
    pass

class TabContainer:

    # Constants
    MAX_ELEMENTS_VISIBLES = 6
    MARGIN_BTW_ELEMENTS = 4


    def __init__(self) -> None:
        self.elements = []

        # Scrolling behaviour
        self.scroll_offset = 0
        
        # Rect
        self.x = 0
        self.y = 0
        self.w = 250
        self.h = 450

        self.max_height = self.getElementsHeight()
    
    def dumbGenerate(self, amount : int =5) -> None:
        """Temporary element generator for LEVEL elements"""
        self.elements = []
        img = pygame.transform.scale(pygame.image.load("assets/images/slime/blurping/Slime1.png"), (50, 50))
        for i in range(amount):
            el = Element()
            el.image = img
            el.y = 200 + 55*i
            el.type = Element.LEVEL
            self.elements.append(el)



    def draw(self, surface) -> None:

        surf = pygame.Surface((self.w, self.h))

        x_pointer = 0
        y_pointer = 0 + self.scroll_offset
        el : Element
        for el in self.elements:
            # set the element to his next logical location (at the bottom of the previous one)
            el.x = x_pointer
            el.y = y_pointer
            el.draw(surf, real_x_off=self.x, real_y_off=self.y)
            y_pointer += el.height + TabContainer.MARGIN_BTW_ELEMENTS # add his height for the next element to be well placed
    
        surface.blit(surf, (0, 0))
    
    def update(self, deltaTime, is_clicked=False) -> None:
        self.max_height = self.getElementsHeight() # update the sum of all the element's heighs + their margins

        if self.isHovering():
            for el in self.elements:
                if utils.isPointInRect(self.x, self.y, self.w, self.h, el.x, el.y): # update the element only if it's visible
                    el.update(deltaTime, is_clicked=is_clicked)

    def isHovering(self, x_off=0, y_off=0) -> bool:
        """Check if the mouse is colliding with the element rect"""
        mouse_pos = pygame.mouse.get_pos()
        if utils.isPointInRect(self.x, self.y, self.w, self.h, mouse_pos[0], mouse_pos[1]):
            return True
        else:
            return False
    
    def getElementsHeight(self) -> int:
        h = 0
        for el in self.elements:
            h += el.height + TabContainer.MARGIN_BTW_ELEMENTS
        return h

        
            

class Element:

    # Constants
    LEVEL = 0
    UPGRADE = 0
    QUEST = 0

    def __init__(self,):
        # Rect
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        self.type = Element.LEVEL

        self.image = None

        self.background_color = (50, 50, 50, 255)
        self.color = (255, 255, 255)

        self.button = Button()

    def getAlignVertically(self, height) -> int:
        """Return the y position of a vertically aligned position (compared to the current height of the element)"""
        return (self.height - height)/2 + self.y
    
    def draw(self, surface, infos={"current_lvl":"129", "name":"Hyper Sword", "gain":"6", "amount":"5", "cost":"2.73 B"}, real_x_off=0, real_y_off=0):

        # LEVEL draw structure
        #    [1]        [2]         [3]          [4]
        # | image | | lvl. XX | | next gain | | button |
        # |       | |  name   | |           | |        |
        
        if self.type == Element.LEVEL:

            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height), width=1)

            x_pointer = self.x
            self.width = 0
            self.height = 0

            # draw the background
            pygame.draw.rect(surface, self.background_color, (x_pointer, self.y, self.width, self.height))

            # draw the image
            surface.blit(self.image, (x_pointer, self.y))
            pygame.draw.rect(surface, (50, 50, 50), (x_pointer, self.y, self.image.get_width(), self.image.get_height()), width=2)
            x_pointer += self.image.get_width()
            self.width += self.image.get_width()
            self.height = max(self.height, self.image.get_height())

            # Draw [2]
            text = config.H2.render("Lvl. "+infos["current_lvl"], True, (255, 255, 255), (75, 75, 75))
            surface.blit(text, (x_pointer+5, self.getAlignVertically(text.get_height())))
            lvl_width = text.get_width()

            name = config.H3.render(infos["name"], True, (200, 200, 200), (75, 75, 75))
            surface.blit(name, (x_pointer+5, self.getAlignVertically(text.get_height())+name.get_height()+2))
            name_width = name.get_width()
            self.width += max(lvl_width, name_width)
            x_pointer += max(lvl_width, name_width)

            # Draw [3]
            text = config.H2.render("+ "+infos["gain"], True, (255, 255, 255), (75, 75, 75))
            surface.blit(text, (x_pointer+5, self.getAlignVertically(text.get_height())))
            x_pointer += 5 + text.get_width()
            self.width += text.get_width() + 5

            x_pointer += 20

            # Draw [4]
            pygame.draw.rect(surface, (50, 255, 50), (x_pointer, self.y, self.height, self.height), border_radius=3)
            text = config.H2.render(infos["cost"], True, (255, 255, 255))
            #text = textOutline(config.H2, infos["cost"], (240, 240, 240), (75, 75, 75), 3)
            surface.blit(text, (x_pointer+5, self.getAlignVertically(text.get_height())))
            
            #x_pointer += real_x_off
            
            self.button.x = x_pointer
            self.button.y = self.y
            self.button.w = self.height
            self.button.h = self.height

            self.width += self.height

            self.button.draw(surface)

    def update(self, deltaTime, is_clicked=False):
        self.button.update(is_clicked)


class Button:

    def __init__(self) -> None:
        # Rect
        self.x = 0
        self. y = 0
        self.w = 0
        self.h = 0

        self.on_click_fn = lambda : print(str(self))
        self.on_hover_fn = None
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), (self.x, self.y, self.w, self.h), width=1)
    
    def update(self, is_clicked=False):
        if self.isHovering():

            if self.on_hover_fn != None:
                self.on_hover_fn()

            if is_clicked and self.on_click_fn != None:
                self.on_click_fn()


    def isHovering(self, x_off=0, y_off=0) -> bool:
        """Check if the mouse is colliding with the button rect"""
        mouse_pos = pygame.mouse.get_pos()
        if utils.isPointInRect(self.x, self.y, self.w, self.h, mouse_pos[0], mouse_pos[1]):
            return True
        else:
            return False
    


def textHollow(font, message, fontcolor, force) -> pygame.Surface:
	notcolor = [c ^ 0xFF for c in fontcolor]
	base = font.render(message, 0, fontcolor, notcolor)
	size = base.get_width() + force, base.get_height() + force
	img = pygame.Surface(size, 16)
	img.fill(notcolor)
	base.set_colorkey(0)
	img.blit(base, (0, 0))
	img.blit(base, (force, 0))
	img.blit(base, (0, force))
	img.blit(base, (force, force))
	base.set_colorkey(0)
	base.set_palette_at(1, notcolor)
	img.blit(base, (1, 1))
	img.set_colorkey(notcolor)
	return img


def textOutline(font, message, fontcolor, outlinecolor, force) -> pygame.Surface:
	base = font.render(message, 0, fontcolor)
	outline = textHollow(font, message, outlinecolor, force)
	img = pygame.Surface(outline.get_size(), 16)
	img.blit(base, (1, 1))
	img.blit(outline, (0, 0))
	img.set_colorkey(0)
	return img
