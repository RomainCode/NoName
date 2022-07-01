import pygame

"""Contain all the infos needed by the game, static lib"""

# color RGB + white,black
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BASE_SPEED = 120

PLAYER_WIDTH = 55
PLAYER_HEIGHT = 100

current_speed = BASE_SPEED

# pygame conf
pygame.init()
pygame.font.init()
pygame.mixer.init()
WIDTH, HEIGHT = 1280, 720
FPS = 144
SYS_FONT = "Comic Sans MS"
##FLAVICON = pygame.image.load("./assets/favicon.ico")
clock = pygame.time.Clock()
caption = "No Name Game yet"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption )
##pygame.display.set_icon(FLAVICON)

"""# different font size
H0 = pygame.font.SysFont(SYS_FONT, 55)
H1 = pygame.font.SysFont(SYS_FONT, 32)
H2 = pygame.font.SysFont(SYS_FONT, 24)
H3 = pygame.font.SysFont(SYS_FONT, 18)
H4 = pygame.font.SysFont(SYS_FONT, 16)
H5 = pygame.font.SysFont(SYS_FONT, 13)
H6 = pygame.font.SysFont(SYS_FONT, 10)"""

Keys = {"jump":"space"}


GROUND_MARGIN = 200

### CONVENTIONS D'ECRITURE ###
# variables contantes -> MA_VARIABLE
# variable classique -> ma_variable
# fonction -> maFonction
# clase -> MaClasse

# faire mini docu en début de fonctions, spécifier au max les types des params/return