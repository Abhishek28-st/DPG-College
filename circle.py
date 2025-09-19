def midpoint_circle(r):
    x = 0 
    y = r
    r = 10
    p = 1 - r
    points = [] 
    while x <= y:
        points.append((x, y))
        points.append((y, x))
        points.append((x, -y))
        points.append((y, -x))
        points.append((-x, y))
        points.append((-y, x))
        points.append((-x, -y))
        points.append((-y, -x))
        if p < 0:
            p += 2 * x + 1
        else:
            p += 2 * (x - y) + 1
            y -= 1
        x += 1
    return points
print(midpoint_circle(10))