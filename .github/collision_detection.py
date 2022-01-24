# PyGame Collision Detection Practice, Terrell Fuller, January 24, 2022, 12:01, v0.3

import pygame, sys, random
from pygame.locals import *

# Setup Pygame
pygame.init()
mainClock = pygame.time.Clock()

# Setup the Pygame Window
WINDOWWITH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDHEIGHT), 0, 32)
pygame.display.set_caption('Collision Detection 2022')

# Setup colors.
BLACK = (0,0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

