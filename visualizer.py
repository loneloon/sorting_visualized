import os
import datetime
import random
import copy
import sys

# prompt silencer

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
os.environ['SDL_VIDEO_self.winDOW_POS'] = "%d,%d" % (650, 200)

import pygame


class Visualizer:
    def __init__(self, width, height, max_value, step_delay=None):
        pygame.init()
        
        self.scr_width = width
        self.scr_height = height

        self.max_value = max_value

        self.step_delay = step_delay if step_delay is not None else 0

        self.win = pygame.display.set_mode((self.scr_width, self.scr_height))
        
        pygame.display.set_caption("Sorting Visualizer")

        self.isFullscreen = True
        if self.isFullscreen:
            pygame.display.toggle_fullscreen()
    
    def update_image(self, arr, selected):
    
        pygame.time.delay(self.step_delay)
        self.display_refresh(arr, selected)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
    
    
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

    def display_refresh(self, arr, selected):
        self.win.fill((0, 0, 0))

        for idx, i in enumerate(arr):
            if idx == selected:
                pygame.draw.rect(self.win, (255, 0, 0),
                                 ((self.scr_width / len(arr)) * idx, self.scr_height - i * (self.scr_height*0.8) / self.max_value, self.scr_width / len(arr), i * (self.scr_height*0.8) / self.max_value))
            else:
                pygame.draw.rect(self.win, (255, 255, 255), ((self.scr_width/len(arr))*idx, self.scr_height - i*(self.scr_height*0.8)/self.max_value, self.scr_width/len(arr), i*(self.scr_height*0.8)/self.max_value))

        pygame.display.update()

    @staticmethod
    def animation_loop(sorting_function, input_arr):
        sorting_function(input_arr)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

#  Place the update method of a Visualizer object in the end of the iteration cycle of a sorting function
#  first arg - current array, second - idx of a pointer
