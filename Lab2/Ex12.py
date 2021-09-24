import turtle as t


def semicircle(length):
    t.speed(100)
    for _ in range(36):
        t.right(5)
        t.forward(length)


t.left(90)
for _ in range(1, 10):
    semicircle(5)
    semicircle(1)
