import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, scr, font):
        pygame.draw.rect(scr, GRAY, self.rect)
        txt = font.render(self.text, True, BLACK)
        scr.blit(txt, (self.rect.x + 20, self.rect.y + 10))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


class UI:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.font = pygame.font.SysFont(None, 32)
        self.title_font = pygame.font.SysFont(None, 50)

        self.play_btn = Button(120, 180, 160, 50, "PLAY")
        self.leaders_btn = Button(120, 250, 160, 50, "LEADERS")
        self.quit_btn = Button(120, 320, 160, 50, "QUIT")

    def draw_menu(self, scr):
        scr.fill((30, 30, 30))

        title = self.title_font.render("RACER", True, WHITE)
        scr.blit(title, (self.w//2 - title.get_width()//2, 80))

        self.play_btn.draw(scr, self.font)
        self.leaders_btn.draw(scr, self.font)
        self.quit_btn.draw(scr, self.font)

    def handle_menu_click(self, pos):
        if self.play_btn.clicked(pos):
            return "play"
        if self.leaders_btn.clicked(pos):
            return "leaders"
        if self.quit_btn.clicked(pos):
            return "quit"
        return "menu"

    def draw_game_over(self, scr, score):
        scr.fill((0, 0, 0))
        txt = self.font.render(f"Game Over! Score: {score}", True, WHITE)
        scr.blit(txt, (80, 250))

        retry = self.font.render("Click to return", True, WHITE)
        scr.blit(retry, (90, 320))