from random import randint, random
import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))

done = True
x = 25
y = 25
clock = pygame.time.Clock()
a=randint(0,697)
b=randint(0,697)
r=25
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 10
    if pressed[pygame.K_DOWN]:
        y += 10
    if pressed[pygame.K_RIGHT]:
        x += 10
    if pressed[pygame.K_LEFT]:
        x -= 10
    if x + r > 700:
        x = 700-r
    if x < r:
        x = r
    if y + r > 700:
        y = 700-r
    if y < r:
        y = r
    
    screen.fill((255, 255, 255))
    if (((a-x)**2)+((b-y)**2))**0.5<10+r:
        a=randint(0,697)
        b=randint(0,697)
        r=r+10
    d=2
    pygame.draw.line(screen, (0, 0, 0), (x,y),(x+100,y),10)
    pygame.draw.circle(screen, (255, 0, 0), [a,b], 10)
    
    pygame.display.flip()
    clock.tick(60)