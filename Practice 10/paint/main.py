import pygame

def drawCircle(surf, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    rad = int(((x1 - x2)**2 + (y1 - y2)**2)**0.5)

    pygame.draw.circle(surf, color, start, rad, width)

def drawRect(scr, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    w, h = abs(x1 - x2), abs(y1 - y2)
  
    pygame.draw.rect(scr, color, (min(x1, x2), min(y1, y2), w, h), width)

def brush(scr, color, start, end, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(abs(dx), abs(dy))

    for i in range(steps):
        x = int(start[0] + i * dx / steps)
        y = int(start[1] + i * dy / steps)
        pygame.draw.circle(scr, color, (x, y), radius)


pygame.init()
W, H = 900, 600
MENU_HEIGHT = 100
scr = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint from me")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 15)
canvas = pygame.Surface((W, H - MENU_HEIGHT)) #size of drawing area
canvas.fill((0, 0, 0))

#cur condition
history = [canvas.copy()]
radius = 5
color = (0, 0, 255)
mode = 'brush'
drawing = False
start_pos = None
last_pos = None

#buttons
btn_brush = pygame.Rect(10, 10, 80, 80)
btn_rect = pygame.Rect(100, 10, 80, 80)
btn_circle = pygame.Rect(190, 10, 80, 80)
btn_eraser = pygame.Rect(280, 10, 80, 80)
btn_small = pygame.Rect(600, 20, 40, 40)
btn_medium = pygame.Rect(645, 20, 40, 40)
btn_big = pygame.Rect(690, 20, 40, 40)

colors = [
    (pygame.Rect(470, 10, 40, 40), (255, 0, 0)),# Red
    (pygame.Rect(515, 10, 40, 40), (0, 255, 0)),# Green
    (pygame.Rect(470, 55, 40, 40), (0, 0, 255)), # Blue
    (pygame.Rect(515, 55, 40, 40), (255, 255, 255))# White
]


running = True
while running:
    pos = pygame.mouse.get_pos()
    canvas_pos = (pos[0], pos[1] - MENU_HEIGHT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #key types
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                mode = 'brush'
            if event.key == pygame.K_e:
                mode = 'eraser'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_r:
                mode = 'rect'
            if event.key == pygame.K_q:
                running = False

        #down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pos[1] > MENU_HEIGHT:
                drawing = True
                last_pos = canvas_pos
                start_pos = canvas_pos

            if btn_brush.collidepoint(pos):
                mode = "brush"
            elif btn_rect.collidepoint(pos):
                mode = "rect"
            elif btn_circle.collidepoint(pos):
                mode = "circle"
            elif btn_eraser.collidepoint(pos):
                mode = "eraser"

            if btn_small.collidepoint(pos):
                radius = 3
            elif btn_medium.collidepoint(pos):
                radius = 10
            elif btn_big.collidepoint(pos):
                radius = 20

            for r, c in colors:
                if r.collidepoint(pos):
                    color = c

        #up
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                if mode == "rect":
                    drawRect(canvas, color, start_pos, canvas_pos, radius)
                elif mode == "circle":
                    drawCircle(canvas, color, start_pos, canvas_pos, radius)

            drawing = False

        #mouse move
        if event.type == pygame.MOUSEMOTION and drawing and last_pos:
            if mode == "brush":
                brush(canvas, color, last_pos, canvas_pos, radius)
            elif mode == "eraser":
                brush(canvas, (0, 0, 0), last_pos, canvas_pos, radius)

            last_pos = canvas_pos

    scr.fill((30, 30, 30))
    scr.blit(canvas, (0, MENU_HEIGHT))

    pygame.draw.rect(scr, (50, 50, 50), (0, 0, W, MENU_HEIGHT))

#controllers
    pygame.draw.rect(scr, (180, 180, 180), btn_brush)
    pygame.draw.rect(scr, (180, 180, 180), btn_rect)
    pygame.draw.rect(scr, (180, 180, 180), btn_circle)
    pygame.draw.rect(scr, (180, 180, 180), btn_eraser)
    scr.blit(font.render("Brush", True, (0,0,0)), (30, 35))
    scr.blit(font.render("Rect", True, (0,0,0)), (120, 35))
    scr.blit(font.render("Circle", True, (0,0,0)), (210, 35))
    scr.blit(font.render("Eraser", True, (0,0,0)), (300, 35))


    pygame.draw.rect(scr, (200, 200, 200), btn_small)
    pygame.draw.rect(scr, (200, 200, 200), btn_medium)
    pygame.draw.rect(scr, (200, 200, 200), btn_big)
    scr.blit(font.render("S", True, (0,0,0)), (610, 20))
    scr.blit(font.render("M", True, (0,0,0)), (655, 20))
    scr.blit(font.render("L", True, (0,0,0)), (700, 20))

    

    for r, c in colors:
        pygame.draw.rect(scr, c, r)

    pygame.display.flip()
    clock.tick(60)

