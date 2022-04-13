import pygame
import random

pygame.init()

#collars
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (150, 75, 0)
YELLOW = (255, 255, 102)
GRAY = (125, 125, 125)
LIGHT_BLUE = (0, 191, 255)
PINK = (255, 0, 128)
PURPLE = (128, 0, 128)
HUNTER_GREEN = (0, 100, 0)
ORANGE = (255, 165, 0)
L_GREEN = (48, 213, 200)
H_PURPLE = (66, 49, 137)

def main():
    screen = pygame.display.set_mode((800, 700))
    mode='random'
    draw_on=False
    last_pos=(0,0)
    color=ORANGE
    radius=1
    
    colors={
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'BLUE': (0, 0, 255),
        'GREEN': (0, 255, 0),
        'RED': (255, 0, 0),
        'BROWN': (150, 75, 0),
        'YELLOW': (255, 255, 102),
        'GRAY': (125, 125, 125),
        'LIGHT_BLUE': (0, 191, 255),
        'PINK': (255, 0, 128),
        'PURPLE':(128, 0, 128),
        'HUNTER_GREEN': (0, 100, 0),
        'ORANGE': (255, 165, 0),
        'L_GREEN': (48, 213, 200),
        'H_PURPLE': (66, 49, 137)
    }

    done=False
    while not done:
        pressed=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    radius += 1
                if event.key==pygame.K_DOWN:
                    radius -= -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                