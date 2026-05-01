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


def drawSquare(surf, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    side = max(abs(x2 - x1), abs(y2 - y1))

    x = x1 if x2 >= x1 else x1 - side
    y = y1 if y2 >= y1 else y1 - side

    pygame.draw.rect(surf, color, (x, y, side, side), width)


def drawRightTriangle(surf, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    points = [
        (x1, y1),
        (x1, y2),
        (x2, y2)
    ]
    pygame.draw.polygon(surf, color, points, width)


def drawEquilateralTriangle(surf, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    side = abs(x2 - x1)

    p1 = (x1, y1)
    p2 = (x1 + side, y1)
    p3 = (x1 + side // 2, y1 - int(side * 0.866))  # height formula

    pygame.draw.polygon(surf, color, [p1, p2, p3], width)


def drawRhombus(surf, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2

    points = [
        (cx, cy - dy),
        (cx + dx, cy),
        (cx, cy + dy),
        (cx - dx, cy)
    ]

    pygame.draw.polygon(surf, color, points, width) 


def brush(surf, color, start, end, size):
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))

    if steps == 0:
        pygame.draw.circle(surf, color, start, size)
        return

    for i in range(steps):
        x = int(start[0] + i * dx / steps)
        y = int(start[1] + i * dy / steps)
        pygame.draw.circle(surf, color, (x, y), size)


def drawLine(surf, color, start, end, width):
    pygame.draw.line(surf, color, start, end, width)


def flood_fill(surf, x, y, new_color):
    w, h = surf.get_size()
    target_color = surf.get_at((x, y))

    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        px, py = stack.pop()
        if px < 0 or px >= w or py < 0 or py >= h:
            continue

        if surf.get_at((px, py)) != target_color:
            continue

        surf.set_at((px, py), new_color)

        stack.append((px + 1, py))
        stack.append((px - 1, py))
        stack.append((px, py + 1))
        stack.append((px, py - 1))