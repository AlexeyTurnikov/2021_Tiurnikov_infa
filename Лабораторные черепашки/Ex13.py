import turtle as t


def circle(length):
    t.speed(100)
    for _ in range(72):
        t.left(5)
        t.forward(length)


def glaz(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.color('brown')
    circle(2)
    t.end_fill()


def nos(x, y):
    t.penup()
    t.goto(x, y)
    t.color('black')
    t.width(20)
    t.pendown()
    t.goto(x, y - 20)


def mouse(length):
    t.right(90)
    t.color('red')
    t.width(20)
    t.speed(100)
    for _ in range(36):
        t.left(5)
        t.forward(length)


t.begin_fill()
t.color('yellow')
circle(10)
t.end_fill()
glaz(-50, 150)
glaz(50, 150)
nos(0, 100)
t.penup()
t.goto(-80, 100)
t.pendown()
mouse(7)
