import turtle as t


def circle(length):
    t.speed(100)
    for _ in range(360):
        t.left(1)
        t.forward(length)
    t.left(180)
    for _ in range(360):
        t.left(1)
        t.forward(length)


t.speed(100)
t.left(90)
n = 4
for line in range(1, n + 1):
    circle(1 + line / 10)
