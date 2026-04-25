import pygame
import sys
import random
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

background = pygame.image.load("images/AnimatedStreet.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 36)


class Player:
    def __init__(self):
        self.image = pygame.image.load("images/car.png")
        self.image = pygame.transform.scale(self.image, (100, 120))

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5, 0)

    def draw(self):
        screen.blit(self.image, self.rect)


class Enemy:
    def __init__(self):
        self.image = pygame.image.load("images/Enemy.png")
        self.image = pygame.transform.scale(self.image, (40, 90))

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height   # spawn above screen

    def move(self):
        self.rect.move_ip(0, 6)

        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self):
        screen.blit(self.image, self.rect)


class Coin:
    def __init__(self):
        self.base_image = pygame.image.load("images/Coin.png")
        self.spawn()

    def spawn(self):
        # weight = value
        self.value = random.choice([1, 2, 5])

        # size depends on value (THIS is the "task requirement")
        if self.value == 1:
            self.size = 25
        elif self.value == 2:
            self.size = 40
        else:
            self.size = 55

        self.image = pygame.transform.scale(self.base_image, (self.size, self.size))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.move_ip(0, 5)

        if self.rect.top > HEIGHT:
            self.spawn()

    def draw(self):
        screen.blit(self.image, self.rect)


player = Player()
enemy = Enemy()
coin = Coin()

score = 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player.update()
    enemy.move()
    coin.move()

    # COLLISION
    if player.rect.colliderect(enemy.rect):
        pygame.quit()
        sys.exit()

    if player.rect.colliderect(coin.rect):
        score += 1
        coin.spawn()

    # DRAW
    screen.blit(background, (0, 0))

    player.draw()
    enemy.draw()
    coin.draw()

    text = font.render(f"Coins: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)
