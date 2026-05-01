import pygame
from tools import *
from datetime import datetime

pygame.init()
w, h = 1200, 600
menu_h = 90

icon = pygame.image.load("assets/paint.png")
pygame.display.set_icon(icon)

scr = pygame.display.set_mode((w,h))
pygame.display.set_caption("Paint by Adiya")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 18)

canvas = pygame.Surface((w, h - menu_h))
canvas.fill((0,0,0))

#state
color = (0,0,0)
brush_size = 5
mode = "brush"
drawing = False
start_p = None
last_p = None
preview = None

#text
text_mode = False
text_input = ""
text_p = (0,0)
cursor_visible = True
cursor_timer = 0

#buttons
btn_brush  = pygame.Rect(10, 10, 80, 30)
btn_line   = pygame.Rect(100, 10, 80, 30)
btn_rect   = pygame.Rect(190, 10, 80, 30)
btn_circle = pygame.Rect(280, 10, 80, 30)
btn_fill   = pygame.Rect(370, 10, 80, 30)
btn_text   = pygame.Rect(460, 10, 80, 30)
btn_square = pygame.Rect(10, 50, 80, 30)
btn_tri    = pygame.Rect(100, 50, 80, 30)
btn_etri   = pygame.Rect(190, 50, 80, 30)
btn_rhomb  = pygame.Rect(280, 50, 80, 30)

btn_s = pygame.Rect(900, 20, 40, 40)
btn_m = pygame.Rect(950, 20, 40, 40)
btn_l = pygame.Rect(1000, 20, 40, 40)

color_buttons = [
    (pygame.Rect(550, 10, 30, 30), (255, 0, 0)),
    (pygame.Rect(590, 10, 30, 30), (0, 255, 0)),
    (pygame.Rect(630, 10, 30, 30), (0, 0, 255)),
    (pygame.Rect(670, 10, 30, 30), (0, 0, 0)),
    (pygame.Rect(710, 10, 30, 30), (255, 255, 255)),
]

#maps (SHORT LOGIC)
key_map = {
    pygame.K_b:"brush", pygame.K_l:"line", pygame.K_r:"rect",
    pygame.K_c:"circle", pygame.K_s:"square", pygame.K_t:"triangle",
    pygame.K_y:"etriangle", pygame.K_h:"rhombus",
    pygame.K_f:"fill", pygame.K_x:"text", pygame.K_e:"eraser"
}

size_map = {pygame.K_1:2, pygame.K_2:5, pygame.K_3:10}

draw_map = {
    "line": drawLine,
    "rect": drawRect,
    "circle": drawCircle,
    "square": drawSquare,
    "triangle": drawRightTriangle,
    "etriangle": drawEquilateralTriangle,
    "rhombus": drawRhombus
}

running = True
while running:
    mouse = pygame.mouse.get_pos()
    canvas_pos = (mouse[0], mouse[1] - menu_h)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key in key_map:
                mode = key_map[event.key]

            if event.key in size_map:
                brush_size = size_map[event.key]

            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            if text_mode:
                if event.key == pygame.K_RETURN:
                    txt = font.render(text_input, True, color)
                    canvas.blit(txt, text_p)
                    text_mode = False

                elif event.key == pygame.K_ESCAPE:
                    text_mode = False

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse[1] <= menu_h:

                if btn_brush.collidepoint(mouse): mode = "brush"
                elif btn_line.collidepoint(mouse): mode = "line"
                elif btn_rect.collidepoint(mouse): mode = "rect"
                elif btn_circle.collidepoint(mouse): mode = "circle"
                elif btn_fill.collidepoint(mouse): mode = "fill"
                elif btn_text.collidepoint(mouse): mode = "text"
                elif btn_square.collidepoint(mouse): mode = "square"
                elif btn_tri.collidepoint(mouse): mode = "triangle"
                elif btn_etri.collidepoint(mouse): mode = "etriangle"
                elif btn_rhomb.collidepoint(mouse): mode = "rhombus"

                elif btn_s.collidepoint(mouse): brush_size = 2
                elif btn_m.collidepoint(mouse): brush_size = 5
                elif btn_l.collidepoint(mouse): brush_size = 10

                for rect, col in color_buttons:
                    if rect.collidepoint(mouse):
                        color = col

            if mouse[1] > menu_h:

                if mode == "fill":
                    flood_fill(canvas, canvas_pos[0], canvas_pos[1], color)

                elif mode == "text":
                    text_mode = True
                    text_input = ""
                    text_p = canvas_pos

                else:
                    drawing = True
                    start_p = canvas_pos
                    last_p = canvas_pos

        if event.type == pygame.MOUSEBUTTONUP:

            if drawing and mode in draw_map:
                draw_map[mode](canvas, color, start_p, canvas_pos, brush_size)

            drawing = False
            preview = None

        if event.type == pygame.MOUSEMOTION:

            if drawing:
                if mode == "brush":
                    brush(canvas, color, last_p, canvas_pos, brush_size)

                elif mode == "eraser":
                    brush(canvas, (255,255,255), last_p, canvas_pos, brush_size)

                elif mode in draw_map:
                    preview = (start_p, canvas_pos)

                last_p = canvas_pos

    #DRAW
    scr.fill((0,0,0))
    pygame.draw.rect(scr, (120,120,120), (0, 0, w, menu_h))

    buttons = [
        (btn_brush,"Brush"), (btn_line,"Line"),
        (btn_rect,"Rect"), (btn_circle,"Circle"),
        (btn_fill,"Fill"), (btn_text,"Text"),
        (btn_square,"Square"), (btn_tri,"Tri"),
        (btn_etri,"ETri"), (btn_rhomb,"Rhomb")
    ]

    for rect,label in buttons:
        pygame.draw.rect(scr,(180,180,180),rect)
        scr.blit(font.render(label,True,(0,0,0)),(rect.x+5,rect.y+5))

    pygame.draw.rect(scr,(200,200,200),btn_s)
    pygame.draw.rect(scr,(200,200,200),btn_m)
    pygame.draw.rect(scr,(200,200,200),btn_l)

    scr.blit(font.render("S",True,(0,0,0)),(910,25))
    scr.blit(font.render("M",True,(0,0,0)),(960,25))
    scr.blit(font.render("L",True,(0,0,0)),(1010,25))

    for rect,col in color_buttons:
        pygame.draw.rect(scr,col,rect)
        pygame.draw.rect(scr,(0,0,0),rect,2)
        if col == color:
            pygame.draw.rect(scr,(255,255,0),rect,3)

    if preview and mode in draw_map:
        temp = canvas.copy()
        draw_map[mode](temp, color, preview[0], preview[1], brush_size)
        scr.blit(temp,(0,menu_h))
    else:
        scr.blit(canvas,(0,menu_h))

    if text_mode:
        preview_text = font.render(text_input,True,color)
        text_rect = preview_text.get_rect()
        text_rect.topleft = (text_p[0], text_p[1] + menu_h)

        pygame.draw.rect(scr,(255,255,255),text_rect)
        scr.blit(preview_text,text_rect)

        if cursor_visible:
            pygame.draw.line(scr,color,
                             (text_rect.right+2,text_rect.top),
                             (text_rect.right+2,text_rect.bottom),2)

    cursor_timer += clock.get_time()
    if cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = 0

    pygame.display.flip()
    clock.tick(60)

pygame.quit()