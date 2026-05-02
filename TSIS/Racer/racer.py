import pygame
import random

WIDTH = 400
HEIGHT = 600


class Player:
    def __init__(self, lanes):
        self.image = pygame.image.load("assets/car.png")
        self.image = pygame.transform.scale(self.image, (100, 120))

        self.lanes = lanes
        self.lane_index = 1

        self.rect = self.image.get_rect()
        self.rect.centerx = self.lanes[self.lane_index]
        self.rect.bottom = HEIGHT - 10

        # powerups
        self.shield = False
        self.nitro_timer = 0
        self.active_powerup = None
        self.power_timer = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if hasattr(self, 'move_cooldown') and self.move_cooldown > 0:
            self.move_cooldown -= 1
            return

        if keys[pygame.K_LEFT] and self.lane_index > 0:
            self.lane_index -= 1
            self.rect.centerx = self.lanes[self.lane_index]
            self.move_cooldown = 15

        if keys[pygame.K_RIGHT]  and self.lane_index < len(self.lanes) - 1:
            self.lane_index += 1
            self.rect.centerx = self.lanes[self.lane_index]
            self.move_cooldown = 15

    def draw(self, scr):
        scr.blit(self.image, self.rect)


class Enemy:
    def __init__(self, lanes):
        self.lanes = lanes

        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (45, 80))

        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.centerx = random.choice(self.lanes)
        self.rect.y = random.randint(-700, -100)

    def move(self, speed):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self, scr):
        scr.blit(self.image, self.rect)


class Coin:
    def __init__(self, lanes):
        self.base = pygame.image.load("assets/coin.png")
        self.image = pygame.transform.scale(self.base, (35, 35))
        self.lanes = lanes
        self.spawn()

    def spawn(self):
        self.value = random.choice([1, 2, 5])
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(self.lanes)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.spawn()

    def draw(self, scr):
        scr.blit(self.image, self.rect)


class Hazard:
    def __init__(self, lanes):
        self.lanes = lanes

        self.oil = pygame.transform.scale(
            pygame.image.load("assets/oil.png"), (60, 60)
        )
        self.banana = pygame.transform.scale(
            pygame.image.load("assets/banana.png"), (50, 50)
        )

        self.reset()

    def reset(self):
        self.type = random.choice(["oil", "banana"])
        self.image = self.oil if self.type == "oil" else self.banana

        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(self.lanes)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.y += 6
        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self, scr):
        scr.blit(self.image, self.rect)


class PowerUp:
    def __init__(self, lanes):
        self.lanes = lanes

        self.images = {
            "nitro": pygame.transform.scale(
                pygame.image.load("assets/nitro.png"), (40, 40)
            ),
            "shield": pygame.transform.scale(
                pygame.image.load("assets/shield.png"), (40, 40)
            ),
            "repair": pygame.transform.scale(
                pygame.image.load("assets/repair.png"), (40, 40)
            )
        }

        self.type = None
        self.image = None
        self.rect = None
        self.reset()

    def reset(self):
        self.type = random.choice(["nitro", "shield", "repair"])
        self.image = self.images[self.type]

        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(self.lanes)
        self.rect.y = -self.rect.height

    def move(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.reset()

    def draw(self, scr):
        scr.blit(self.image, self.rect)