import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((700, 600))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()
class Snake:
    def __init__(self, x ,y):
        self.size=1
        self.elements=[[x,y]]
        self.radius=10
        self.dx=5
        self.dy=0
        self.is_add=False
        self.speed=30
    
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,RED,element,self.radius)
    
    def add(self):
        self.size+=1
        self.elements.append([0,0])
        self.is_add=False
        if self.size % 4==0:
            self.speed+=5

    def move(self):
        if self.is_add:
            self.add()

        for i in range(self.size-1,0,-1):
            self.elements[i][0]=self.elements[i-1][0]
            self.elements[i][1]=self.elements[i-1][1]
        self.elements[0][0]+=self.dx
        self.elements[0][1]+=self.dy
    
    def eat(self, foodx, foody):
        x=self.elements[0][0]
        y=self.elements[0][1]
        if foodx <= x <= foodx + 20 and  foody <= y <= foody + 20:
            return True
        return False

class Food:
    def __init__(self):
        self.x=randint(0,685)
        self.y=randint(0,585)
    def gen(self):
        self.x=randint(0,685)
        self.y=randint(0,585)
        if [self.x,self.y] in snake.elements:
            self.x=randint(0,685)
            self.y=randint(0,585)
            
    def draw(self):
        pygame.draw.rect(screen,GREEN,(self.x, self.y, 15,15))

snake=Snake(100,100)
food=Food()
running=True

FPS=30
font_small = pygame.font.SysFont("Verdana", 20)
m=5

while running:
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if event.key==pygame.K_SPACE:
                snake.is_add=True
            if event.key==pygame.K_RIGHT and snake.dx!=-m:
                snake.dx=m
                snake.dy=0
            if event.key==pygame.K_LEFT and snake.dx!=m:
                snake.dx=-m
                snake.dy=0
            if event.key==pygame.K_DOWN and snake.dy!=-m: 
                snake.dx=0
                snake.dy=m
            if event.key==pygame.K_UP and snake.dy!=m:
                snake.dx=0
                snake.dy=-m
    if snake.elements[0][1]+20>600:
        running=False
    if snake.elements[0][1]<20:
        running=False
    if snake.elements[0][0]+20>700:
        running=False
    if snake.elements[0][0]<20:
        running=False
    if snake.eat(food.x,food.y):
        snake.is_add=True
        food.gen()

    snake.move()
    screen.fill(BLACK)
    sc = font_small.render('Score: ' + str(snake.size), True, WHITE)
    screen.blit(sc, (600, 15))
    lv = snake.size // 4 + 1
    lvls = font_small.render(f'Lvl: {lv}', True, WHITE)
    screen.blit(lvls, (600, 35))
    snake.draw()
    food.draw()
    pygame.display.flip()
pygame.quit()