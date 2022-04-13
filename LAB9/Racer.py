import pygame
import sys
import random

pygame.init() 
clock = pygame.time.Clock()

FPS = 60
weight = 400 
height = 600 
step = 5
start_speed = 8
speed = start_speed
screen = pygame.display.set_mode((weight,height)) 

directory = "files/"
bg = pygame.image.load(directory + "street.png")
redc = pygame.image.load(directory + "rcar.png")
coinpng = pygame.image.load(directory + "coin.png")
coin2png = pygame.image.load(directory + "coin1.png")
bluec = pygame.image.load(directory + "bcar.png")

font = pygame.font.SysFont("comics", 50) 

class enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = redc 
        self.rect = self.image.get_rect() 

    def update(self): 
        self.rect.move_ip(0,speed) 
        if self.rect.top > height: 
            self.top = 0
            self.rect.center = (random.randint(30,350),0) 

    def draw(self,surface): 
        surface.blit(self.image,self.rect) 

class coin(pygame.sprite.Sprite): 
    def __init__(self, png, speed): 
        super().__init__() 
        self.image = png 
        self.image = pygame.transform.scale(self.image, (40, 40)) 
        self.rect = self.image.get_rect() 
        self.counter = 0 
        self.speed = speed

    def update(self): 
        self.rect.move_ip(0,self.speed) 
        if self.rect.bottom > height: 
            self.top = 0 
            self.rect.center = (random.randint(30,350),0)
             
    def draw(self):
        screen.blit(self.image ,self.rect) 
 
    def collide(self) : 
        self.top = 0
        self.rect.center = (random.randint(30,350), 0) 
    

class player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = bluec 
        self.rect = self.image.get_rect() 
        self.rect.center = (150,520) 
    def update(self): 
        pressed = pygame.key.get_pressed() 
        if self.rect.left > 0: 
            if pressed[pygame.K_LEFT]: 
                self.rect.move_ip(-step,0) 
        if self.rect.right < weight: 
            if pressed[pygame.K_RIGHT]: 
                self.rect.move_ip(step,0) 
    def draw(self,surface): 
        surface.blit(self.image,self.rect)

all_sprite = pygame.sprite.Group()
 
p1 = player() 
e1 = enemy() 
c1 = coin(coinpng, 8)
c2 = coin(coin2png, 1) 


all_sprite.add(e1) 
all_sprite.add(c1) 
all_sprite.add(c2)
all_sprite.add(p1)
 
enemies = pygame.sprite.Group() 
coins = pygame.sprite.Group() 
enemies.add(e1) 
coins.add(c1)
coins.add(c2) 

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
     
    score = font.render(str(c1.counter + c2.counter), True, (0, 255, 255)) 

    speed = start_speed + (c1.counter + c2.counter)//15

    p1.update() 
    e1.update() 
    c1.update()
    c2.update()

    if pygame.sprite.spritecollideany(p1,enemies): 
        pygame.quit() 
        sys.exit() 
 
    if pygame.sprite.collide_circle(p1, c1): 
        c1.collide() 
        c1.counter += 1 
    if pygame.sprite.collide_circle(p1, c2): 
        c2.collide() 
        c2.counter += 3
    
 
    if pygame.sprite.spritecollideany(c1, enemies): 
       c1.collide() 
         
    screen.blit(bg,(0,0)) 
    screen.blit(score,(weight-score.get_width()-10,0)) 
 
    p1.draw(screen) 
    e1.draw(screen) 
    c1.draw() 
    c2.draw()
     
    pygame.display.update() 
    clock.tick(FPS)