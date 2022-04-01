import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()

pygame.init()
size=x, y=(400,400)
screen=pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(BLACK)
r=25
x=25
y=25
#pygame.draw.rect(screen, (WHITE), (70, 30, 100, 100), 4)
#image = pygame.image.load('ball.png')
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            y-=10
        if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
            y+=10
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            x+=10
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            x-=10
    if y+25>400:
        y=375
    if y<25:
        y=25
    if x+25>400:
        x=375
    if x<25:
        x=25
    clock.tick(60)
    screen.fill(BLACK)
    pygame.draw.circle(screen,RED,(x,y),25)
    pygame.display.flip()

pygame.quit()