import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 50)

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)


def game_loop():

    snake_pos = [100, 60]
    snake_body = [[100, 60], [80, 60], [60, 60]]

    direction = 'RIGHT'
    change_to = direction

    # FOOD (position + value + timer)
    food_pos = [
        random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
        random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
    ]

    food_value = random.choice([1, 2, 5])
    food_spawn_time = pygame.time.get_ticks()
    food_lifetime = 4000  # 4 seconds

    score = 0
    level = 1
    speed = 10

    while True:

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to

        # MOVE SNAKE HEAD
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        snake_body.insert(0, list(snake_pos))

        # TIME (for food disappearing)
        current_time = pygame.time.get_ticks()

        # FOOD TIMER EXPIRE → respawn
        if current_time - food_spawn_time > food_lifetime:
            food_pos = [
                random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
            ]
            food_value = random.choice([1, 2, 5])
            food_spawn_time = current_time

        # EAT FOOD
        if snake_pos == food_pos:
            score += food_value

            if score % 3 == 0:
                level += 1
                speed += 2

            food_pos = [
                random.randrange(1, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
            ]
            food_value = random.choice([1, 2, 5])
            food_spawn_time = current_time

        else:
            snake_body.pop()

        # WALL COLLISION
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            return score

        # SELF COLLISION
        for block in snake_body[1:]:
            if snake_pos == block:
                return score

        # DRAW
        screen.fill(BLACK)

        # snake
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN,
                             pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # food
        pygame.draw.rect(screen, RED,
                         pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # UI
        score_surface = font.render(f'Score: {score}  Level: {level}', True, WHITE)
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        clock.tick(speed)


# MAIN LOOP
playing = True

while playing:
    result = game_loop()

    if result == "QUIT":
        playing = False

pygame.quit()
