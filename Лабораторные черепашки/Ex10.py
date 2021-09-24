import turtle as t


def circle():
    for _ in range(360):
        t.left(1)
        t.forward(1)
    t.left(180)
    for _ in range(360):
        t.left(1)
        t.forward(1)


t.speed(0)
n = 3
for _ in range(1, n + 1):
    circle()
    angle = 360 / n
    t.left(angle)
