import pygame
from ball import Ball

pygame.init()
#scr
scr = pygame.display.set_mode((700,700))
pygame.display.set_caption("Game by Adiya")
clock = pygame.time.Clock()

speed = 20
cent_x = 350
cent_y = 350
ball = Ball(cent_x, cent_y, 700, 700)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball.move_left()
    if keys[pygame.K_RIGHT]:
        ball.move_right()
    if keys[pygame.K_UP]:
        ball.move_up()
    if keys[pygame.K_DOWN]:
        ball.move_down()
    if keys[pygame.K_q]:
        running = False

    scr.fill((255,255,255))
    pygame.draw.circle(scr, (255,0,0), (ball.x, ball.y), ball.rad)
 
    pygame.display.update()
    clock.tick(60)

pygame.quit()
