import turtle as t

x = 0
y = 0

t.goto(x, y)
length = 50
for o in range(1, 11, 1):
    t.pendown()
    t.forward(length / 2)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length / 2)
    t.penup()
    t.goto(0, x - 10)
    x = x - 10
    length += 20
