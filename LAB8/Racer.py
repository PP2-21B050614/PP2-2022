import pygame
import random
pygame.init() 
clock = pygame.time.Clock()
FPS=60
screen = pygame.display.set_mode((400,600))
directory = "LAB8/PNG/"
bg = pygame.image.load(directory + "street.png")
redc = pygame.image.load(directory + "rcar.png")
coinpng = pygame.image.load(directory + "coin.png")
bluec = pygame.image.load(directory + "bcar.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        s