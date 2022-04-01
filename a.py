import pygame
import os
f = os.listdir('LAB7/Music')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
text=font.render(f[0],True,RED)

pygame.init()
size=x, y=(1000,400)
screen=pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(BLACK)

k=0
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    k+=1
    screen.blit(text,(0,0))
    screen.blit(f[k],(0,k*20))     
    clock.tick(60)
    pygame.display.flip()

pygame.quit()