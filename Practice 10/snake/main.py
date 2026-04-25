import pygame
import random

# --- Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 50)

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

def show_game_over(score):
    """ This function runs when you die. It returns True to restart, False to quit. """
    while True:
        screen.fill(BLACK)
        
        # 1. Draw Text
        msg = big_font.render(f"GAME OVER! Score: {score}", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - 150, 150))
        
        # 2. Define Button Rectangles
        btn_restart = pygame.Rect(WIDTH // 2 - 110, 300, 100, 50)
        btn_quit = pygame.Rect(WIDTH // 2 + 10, 300, 100, 50)
        
        # 3. Draw Buttons
        pygame.draw.rect(screen, GREEN, btn_restart)
        pygame.draw.rect(screen, RED, btn_quit)
        
        # 4. Draw Button Text
        restart_txt = font.render("Restart", True, WHITE)
        quit_txt = font.render("Quit", True, WHITE)
        screen.blit(restart_txt, (btn_restart.x + 15, btn_restart.y + 10))
        screen.blit(quit_txt, (btn_quit.x + 25, btn_quit.y + 10))
        
        pygame.display.flip()

        # 5. Handle Input for Game Over screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if btn_restart.collidepoint(mouse_pos):
                    return True  # User wants to restart
                if btn_quit.collidepoint(mouse_pos):
                    return False # User wants to quit

def game_loop():
    """ This is the actual game logic. """
    snake_pos = [100, 60]
    snake_body = [[100, 60], [80, 60], [60, 60]]
    direction = 'RIGHT'
    change_to = direction
    
    food_pos = [random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
    
    score = 0
    level = 1
    speed = 10
    
    while True:
        # --- Input ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT" # Tells the main code to stop everything
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN': change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP': change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT': change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT': change_to = 'RIGHT'

        direction = change_to

        # --- Move Snake ---
        if direction == 'UP': snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN': snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT': snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT': snake_pos[0] += BLOCK_SIZE

        snake_body.insert(0, list(snake_pos))

        # --- Food & Level Up ---
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 2
            food_pos = [random.randrange(1, (WIDTH//BLOCK_SIZE)) * BLOCK_SIZE,
                        random.randrange(1, (HEIGHT//BLOCK_SIZE)) * BLOCK_SIZE]
        else:
            snake_body.pop()

        # --- Collision Logic ---
        # Wall collision or hitting self
        if (snake_pos[0] < 0 or snake_pos[0] > WIDTH - BLOCK_SIZE or 
            snake_pos[1] < 0 or snake_pos[1] > HEIGHT - BLOCK_SIZE):
            return score # Game ends, return the score to main()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                return score # Game ends, return the score to main()

        # --- Drawing ---
        screen.fill(BLACK)
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
        score_surface = font.render(f'Score: {score}  Level: {level}', True, WHITE)
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        clock.tick(speed)

# --- The Main Program Control ---
playing = True
while playing:
    result = game_loop() # Start the game
    
    if result == "QUIT":
        playing = False
    else:
        # If the game ended naturally, show the Game Over screen
        wants_to_restart = show_game_over(result)
        if not wants_to_restart:
            playing = False

pygame.quit()