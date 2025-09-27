import matplotlib.pyplot as plt

def midpoint_circle(r):
    x = 0
    y = r
    p = 1 - r
    points = []

    while x <= y:
        points.append(( x,  y))
        points.append(( y,  x))
        points.append(( x, -y))
        points.append(( y, -x))
        points.append((-x,  y))
        points.append((-y,  x))
        points.append((-x, -y))
        points.append((-y, -x))

        if p < 0:
            p = p + 2*x + 1
        else:
            p = p + 2*(x - y) + 1
            y -= 1
        x += 1

    points = list(set(points))
    return points


r = 10
points = midpoint_circle(r)

xs = [p[0] for p in points]
ys = [p[1] for p in points]

plt.figure(figsize=(6, 6))
plt.scatter(xs, ys, s=30, color="blue")  # draw points
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Midpoint Circle Algorithm (r = {r})')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.savefig("circle.png", bbox_inches="tight")
plt.show()