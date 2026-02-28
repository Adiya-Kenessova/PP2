import math

# input
r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

# distance between A and B
AB = math.hypot(x2 - x1, y2 - y1)

# function to compute distance from point (0,0) to segment AB
def dist_to_segment(x1, y1, x2, y2):
    # vector from A to B
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(x1, y1)  # A==B
    # projection factor t
    t = max(0, min(1, -(x1*dx + y1*dy)/(dx*dx + dy*dy)))
    # closest point on segment
    cx = x1 + t*dx
    cy = y1 + t*dy
    return math.hypot(cx, cy)

# check distance from center to segment
dist = dist_to_segment(x1, y1, x2, y2)

if dist >= r:
    # straight line is fine
    print("{:.10f}".format(AB))
else:
    # distances from center to points
    OA = math.hypot(x1, y1)
    OB = math.hypot(x2, y2)

    # tangent lengths
    t1 = math.sqrt(OA**2 - r**2)
    t2 = math.sqrt(OB**2 - r**2)

    # angles of points
    ang1 = math.atan2(y1, x1)
    ang2 = math.atan2(y2, x2)

    delta = abs(ang1 - ang2)
    delta = min(delta, 2*math.pi - delta)

    # angles for tangent points
    a1 = math.acos(r / OA)
    a2 = math.acos(r / OB)

    # arc along circle
    arc = r * (delta - a1 - a2)

    ans = t1 + t2 + arc
    print("{:.10f}".format(ans))