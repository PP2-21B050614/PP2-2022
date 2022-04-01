import pygame
import os 

pygame.init()
pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode((500, 500))
done = True
musics = list(os.listdir('LAB7/Music'))
BLACK = (0, 0, 0)
pygame.mixer.music.load('LAB7/Music/'+musics[0])
pygame.mixer.music.play()
image = pygame.transform.scale(pygame.image.load('LAB7/M.jpg'),(200, 200))

pygame.display.set_caption("Music")
k=0

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RSHIFT:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                if k == 0:
                    k = len(musics)-1
                    pygame.mixer.music.load('LAB7/Music/'+musics[k])
                    pygame.mixer.music.play()
                else:
                    k -= 1
                    pygame.mixer.music.load('LAB7/Music/'+musics[k])
                    pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                if k == len(musics)-1:
                    k = 0
                    pygame.mixer.music.load('LAB7/Music/'+musics[k])
                    pygame.mixer.music.play()
                else:
                    k += 1
                    pygame.mixer.music.load('LAB7/Music/'+musics[k])
                    pygame.mixer.music.play()

    screen.fill(BLACK)
    screen.blit(image,(150,150))
    pygame.time.delay(10)
    
    pygame.display.flip()