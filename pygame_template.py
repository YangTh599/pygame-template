import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from time import sleep as slp

pygame.init()
pygame.display.set_caption("Pygame Window Caption is up here") # Window Caption

#CONSTANTS

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (20,140,25)
FPS = 60

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

#Pygame Window
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Draw Function to update graphics
def draw(window):
    
    window.fill(WHITE) # 15
    pygame.display.update()

def main(window): # MAIN FUNCTION
    clock = pygame.time.Clock()

    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # QUIT
                run = False
                break
        
        draw(window) # UPDATES SCREEN


    pygame.quit()
    quit()

if __name__ == "__main__": 
    main(window)

