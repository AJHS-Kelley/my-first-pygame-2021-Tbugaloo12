# PyGame Collision Detection Practice, Terrell Fuller, January 24, 2022, 11:46, v0.2

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