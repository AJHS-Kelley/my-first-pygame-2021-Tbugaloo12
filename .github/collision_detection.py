# PyGame Collision Detection Practice, Terrell Fuller, January 24, 2022, 12:04, v0.6

from pickle import FALSE
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

# Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint)(0, WINDOWWIDTH - FOODSIZE),random.radiant(0, WINDOWWIEGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = FALSE
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Run the game loop.

while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == Quit:
            pygame.quit()
            sys.exit()
         if event.type == KEYDOWN:
             # Change the keyboard variables
              if event.key == K_LEFT or event. key == K_a:
                   moveRight = False
                   moveLeft =True
              if event.key == K_RIGHT or event.key == K_d: 
                  moveLeft = False
                  moveRight = True 
              if event.key == K_UP or event.key == K_w:
                  moveDown = False
                  moveUp = True
              if event.key == K_DOWN or event.key == K_s:
                  moveUp = False 
                  moveDown = True 
                          