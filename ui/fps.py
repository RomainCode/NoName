import pygame
from utils.utils import createFont

font = createFont(size=20)


def drawFps(clock: pygame.time.Clock, pos: list[list] or tuple[tuple], surface: pygame.Surface):
    """return fps, and draw it to surface as white text"""
    fps = str(int(clock.get_fps()))  # getting fps value
    img = font.render(f"fps: {fps}", True, [255, 255, 255])
    surface.blit(img, pos)

