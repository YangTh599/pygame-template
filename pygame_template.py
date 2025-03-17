import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    pygame.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,box):
    #BACKGROUND
    window.fill(WHITE) # 15
    

    #FOREGROUND
    box.draw_textbox()

    pygame.display.update()

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    box = boxes.Text_box(window, 200,200,200,50,"WEEEEEEEE",text_color=BLACK, rotation = 50)
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events()
        

        
        draw(window,box) # UPDATES SCREEN

    pygame.quit()
    sys.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

