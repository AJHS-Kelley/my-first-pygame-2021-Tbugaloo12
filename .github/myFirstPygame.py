# My First Pygame, Terrell Fuller, 11/30/21, 1:31PM, v0.4

import pygame, says
from pygame.locals import*

# Initialize Pygame
pygame.init()

# Setup the Window to draw on.
windowSurface=pygame.display.set_mode((500, 400),0,32)
pygame.display.set_caption( 'My First PyGame')


# Setup color values
BLACK = (0,0,0)
WHITE = (255, 255, 255
RED= (255, 0, 0)
GREEN= (0, 255, 0)
BLUE= (0, 0, 255)
TASTYORANGE= (255, 165, 0)

# Setup the fonts .
basicfont = pygame.font.SysFont(None, 48)

# Setup the text .
text = basicFont.render('Hello, world', True, WHITE, BLUE)
textRect = text.get_rec()
textRect.centrarx = windowSurface.get_rect().centerx
textRect.centrary = windowSurface.get_rect().centery

