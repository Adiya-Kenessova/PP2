x1, y1 = map(float, input().split())    #finds the intersection of the line connecting two points with the x-axis
x2, y2 = map(float, input().split())

x = (x1*y2 + x2*y1) / (y1+y2)
y = 0.0


print(f"{x:.10f} {y:.10f}")
