import pygame
import sys
from racer import Player, Enemy, Coin, Hazard, PowerUp
from ui import UI
from persistence import save_score, load_leaderboard

pygame.init()

FPS = 70
clock = pygame.time.Clock()

w, h = 400, 600
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption("Racer Game")

font = pygame.font.SysFont(None, 28)

lanes = [w // 6, w // 2, w * 5 // 6]

player_name = input("Enter your name: ")

ui = UI(w, h)

state = "menu"
score = 0
distance = 0
coins_collected = 0

player = Player(lanes)
enemies = [Enemy(lanes) for _ in range(2)]
coin = Coin(lanes)
hazards = [Hazard(lanes) for _ in range(2)]
powerups = [PowerUp(lanes) for _ in range(1)]


def reset_game():
    global player, enemies, coin, hazards, powerups, score, distance, coins_collected

    player = Player(lanes)
    enemies = [Enemy(lanes) for _ in range(2)]
    coin = Coin(lanes)
    hazards = [Hazard(lanes) for _ in range(2)]
    powerups = [PowerUp(lanes) for _ in range(1)]

    score = 0
    distance = 0
    coins_collected = 0


def draw_road():
    scr.fill((30, 30, 30))
    pygame.draw.rect(scr, (175, 175, 175), (0, 0, w, h))
    pygame.draw.line(scr, (255, 255, 255), (w // 3, 0), (w // 3, h), 5)
    pygame.draw.line(scr, (255, 255, 255), (w * 2 // 3, 0), (w * 2 // 3, h), 5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # MENU CLICK
        if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            action = ui.handle_menu_click(event.pos)

            if action == "play":
                reset_game()
                state = "play"

            elif action == "leaders":
                state = "leaders"

            elif action == "quit":
                pygame.quit()
                sys.exit()

        if state == "leaders" and event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 500:
                state = "menu"

        # GAMEOVER EXIT
        if state == "gameover" and event.type == pygame.MOUSEBUTTONDOWN:
            state = "menu"

    # MENU
    if state == "menu":
        scr.fill((0, 0, 0))
        ui.draw_menu(scr)

    # PLAY
    elif state == "play":

        player.update()
        distance += 1

        speed = 6 + score // 5

        if player.nitro_timer > 0:
            speed += 5
            player.nitro_timer -= 1

        for enemy in enemies:
            enemy.move(speed)

        for hazard in hazards:
            hazard.move()

        coin.move()

        for p in powerups:
            p.move()

        # COLLISIONS
        for enemy in enemies:
            if player.rect.colliderect(enemy.rect):
                if player.shield:
                    player.shield = False
                    enemy.reset()
                else:
                    save_score(player_name, score, distance, coins_collected)
                    state = "gameover"

        if player.rect.colliderect(coin.rect):
            score += coin.value
            coins_collected += coin.value
            coin.spawn()

        for hazard in hazards:
            if player.rect.colliderect(hazard.rect):
                hazard.reset()

        if player.power_timer > 0:
            player.power_timer -= 1
        else:
            player.active_powerup = None

        for p in powerups:
            if player.rect.colliderect(p.rect):

                player.active_powerup = p.type
                player.power_timer = 180

                if p.type == "nitro":
                    player.nitro_timer = 180

                elif p.type == "shield":
                    player.shield = True

                elif p.type == "repair":
                    for hazard in hazards:
                        hazard.reset()

                p.reset()

        # DRAW
        draw_road()

        player.draw(scr)
        coin.draw(scr)

        for enemy in enemies:
            enemy.draw(scr)

        for hazard in hazards:
            hazard.draw(scr)

        for p in powerups:
            p.draw(scr)

        scr.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (10, 10))

    # GAME OVER
    elif state == "gameover":
        scr.fill((0, 0, 0))
        ui.draw_game_over(scr, score)

    # LEADERBOARD
    elif state == "leaders":
        scr.fill((0, 0, 0))

        try:
            board = load_leaderboard()
        except:
            board = []

        title = font.render("LEADERBOARD", True, (255, 255, 255))
        scr.blit(title, (120, 30))

        if len(board) == 0:
            msg = font.render("No data yet", True, (255, 0, 0))
            scr.blit(msg, (140, 250))
        else:
            y = 80
            for i, entry in enumerate(board[:10]):
                name = entry.get("name", "???")
                score_val = entry.get("score", 0)

                text = font.render(
                    f"{i+1}. {name} - {score_val}",
                    True,
                    (255, 255, 255)
                )
                scr.blit(text, (80, y))
                y += 30

        hint = font.render("Click anywhere to return", True, (180, 180, 180))
        scr.blit(hint, (80, 520))

    pygame.display.update()
    clock.tick(FPS)