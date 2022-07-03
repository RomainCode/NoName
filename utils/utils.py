import math
from config import SYS_FONT, WHITE
import pygame

def isCollisionRect(x1, y1, x2, y2, w1, h1, w2, h2) -> bool:
    if x1 < x2+w2 and x1+w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2:
        return True
    return False


def magnitude(x1, y1, x2, y2): # lenght of a vector
    return math.sqrt((x1+x2)**2 + (y1+y2)**2)

def isPointInRect(xr, yr, wr, hr, x, y) -> bool:
    x1, y1, w, h = xr, yr, wr, hr
    x2, y2 = x1+w, y1+h
    if (x1 < x and x < x2):
        if (y1 < y and y < y2):
            return True
    return False

def createFont(text=None, color: tuple[int, int, int] = WHITE, font: str = SYS_FONT, size: int = 28,
               background=None) -> pygame.font.Font or list[pygame.font.Font.render]:
    """simple font function that return a rendered text or a font """
    font = pygame.font.Font(font, size)
    if text is not None:
        text = font.render(text, True, color, background)
        width = text.get_width()
        height = text.get_height()
        color_key = text.getcolorkey()
        list_ = []
        list_.extend([text, width, height, color_key])
        return list_
    else:
        return font