import pygame
from player import MusicPlayer 

pygame.init()
pygame.mixer.init()

scr = pygame.display.set_mode((400,400))
icon = pygame.image.load('spotify.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Music by Adiya")
clock = pygame.time.Clock()

player=MusicPlayer()
font = pygame.font.SysFont("Arial", 36)
text_surface = font.render('Hello World', True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scr.fill((0,186,225))
    scr.blit(text_surface, (100,100))
    pygame.draw.line(scr, (225,225,225), (0,40), (400,40), 3) 
    pygame.display.update()
    clock.tick(60)

pygame.quit()