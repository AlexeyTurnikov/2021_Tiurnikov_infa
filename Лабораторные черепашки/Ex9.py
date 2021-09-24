import turtle as t
import numpy as np
import math


def paint(n, length):
    angle = (180 * (n - 2) / n)

    outangle = 180 - angle
    t.left(outangle + angle / 2)
    for _ in range(0, n, 1):
        t.forward(length)
        t.left(outangle)
    t.right(outangle / 2 + 90)
    return angle


line = 30
for schet in range(3, 14, 1):
    paint(schet, line)
    R = abs(line / (2 * np.sin(math.radians(360 / (2 * schet)))))
    t.penup()
    t.goto(R, 0)
    t.pendown()
    line += 20
