import pygame
from clock import MickeyClock

pygame.init()
scr = pygame.display.set_mode((600, 600))
pygame.display.set_caption("CLock by Adiya")
clock = pygame.time.Clock()
center = (300, 300)


bg = pygame.image.load("images/mickey.png").convert_alpha()
left = pygame.image.load("images/left.png").convert_alpha()
right = pygame.image.load("images/right.png").convert_alpha()

bg_rect = bg.get_rect()
bg_rect.center = center

mickey_clock = MickeyClock(center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sec_angle, min_angle = mickey_clock.get_angles()
    sec_img, sec_rect = mickey_clock.rotate(right, sec_angle)
    min_img, min_rect = mickey_clock.rotate(left, min_angle)

    scr.fill((255, 255, 255))
    scr.blit(bg, bg_rect)
    scr.blit(sec_img, sec_rect)
    scr.blit(min_img, min_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()