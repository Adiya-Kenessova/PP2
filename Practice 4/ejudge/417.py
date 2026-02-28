import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
b = 2*(dx*x1 + dy*y1)
c = x1*x1 + y1*y1 - R*R

disc = b*b - 4*a*c

if disc < 0:  # no intersection
    # check if both points inside
    if x1*x1 + y1*y1 <= R*R and x2*x2 + y2*y2 <= R*R:
        ans = math.hypot(dx, dy)
    else:
        ans = 0.0
else:
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc)/(2*a)
    t2 = (-b + sqrt_disc)/(2*a)
    t_in = max(0, min(t1, t2))
    t_out = min(1, max(t1, t2))
    if t_out < t_in:
        ans = 0.0
    else:
        ans = math.hypot(dx, dy) * (t_out - t_in)

print(f"{ans:.10f}")