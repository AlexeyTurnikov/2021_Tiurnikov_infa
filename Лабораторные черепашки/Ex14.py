import turtle as t


def star(n, length):
    for _ in range(n):
        t.forward(length)
        angle = 180 - 180 / n
        t.right(angle)


n = int(input())
star(n, 50)
