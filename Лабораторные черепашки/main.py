import turtle as t

def paint(n, length):
    angle = (180 * (n - 2) / n)
    outangle = 180 - angle
    t.left(outangle + angle / 2)
    for _ in range(0, n, 1):
        t.forward(length)
        t.left(outangle)
    t.right(angle)

t.speed(1)
paint(5,50)