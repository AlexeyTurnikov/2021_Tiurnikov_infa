import turtle as t


def right():
    t.right(90)
    t.forward(50)
    t.left(90)


def left():
    t.left(90)
    t.forward(50)
    t.right(90)


def down():
    t.right(180)
    t.forward(50)
    t.right(180)


def up():
    t.forward(50)


def rightcornerdown():
    t.left(45)
    t.backward((50 ** 2 + 50 ** 2) ** 0.5)
    t.right(45)


def rightcornerup():
    t.right(45)
    t.forward((50 ** 2 + 50 ** 2) ** 0.5)
    t.left(45)


def leftcornerdown():
    t.right(45)
    t.backward((50 ** 2 + 50 ** 2) ** 0.5)
    t.left(45)


def baza():
    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.pendown()


def zero():
    right()
    left()
    down()
    down()
    right()
    up()
    up()
    down()
    down()
    baza()


def one():
    t.penup()
    down()
    t.pendown()
    rightcornerup()
    down()
    down()
    baza()


def two():
    right()
    down()
    leftcornerdown()
    right()
    baza()


def three():
    right()
    down()
    left()
    right()
    down()
    left()
    right()
    baza()


def four():
    down()
    right()
    up()
    down()
    down()
    t.penup()
    baza()


def five():
    right()
    left()
    down()
    right()
    down()
    left()
    right()
    baza()


def six():
    t.penup()
    right()
    t.pendown()
    leftcornerdown()
    right()
    left()
    down()
    right()
    up()
    down()
    baza()


def seven():
    right()
    leftcornerdown()
    down()
    t.penup()
    right()
    t.pendown()
    baza()


def eight():
    right()
    down()
    left()
    up()
    down()
    down()
    right()
    up()
    down()
    baza()


def nine():
    down()
    right()
    up()
    left()
    right()
    down()
    leftcornerdown()
    t.penup()
    right()
    t.pendown()
    baza()


def printos(a):
    for i in a:
        if i == 'right':
            right()
        if i == 'left':
            left()
        if i == 'down':
            down()
        if i == 'up':
            up()
        if i == 'rightcornerdown':
            rightcornerdown()
        if i == 'rightcornerup':
            rightcornerup()
        if i == 'leftcornerdown':
            leftcornerdown()
        if i == 'baza':
            baza()
        if i == 't.penup':
            t.penup()
        if i == 't.pendown':
            t.pendown()


zeros = ('right', 'left', 'down', 'down', 'right', 'up', 'up', 'down', 'down', 'baza')
ones = ('t.penup', 'down', 't.pendown', 'rightcornerup', 'down', 'down', 'baza')
twos = ('right', 'down', 'leftcornerdown', 'right', 'baza')
threes = ('right', 'down', 'left', 'right', 'down', 'left', 'right', 'baza')
fours = ('down', 'right', 'up', 'down', 'down', 't.penup', 'baza')
fives = ('right', 'left', 'down', 'right', 'down', 'left', 'right', 'baza')
sixs = (
    't.penup', 'right', 't.pendown', 'leftcornerdown', 'right', 'left', 'down', 'right', 'up',
    'down',
    'baza')
sevens = ('right', 'leftcornerdown', 'down', 't.penup', 'right', 't.pendown', 'baza')
eights = ('right', 'down', 'left', 'up', 'down', 'down', 'right', 'up', 'down', 'baza')
nines = (
    'down', 'right', 'up', 'left', 'right', 'down', 'leftcornerdown',
    't.penup', 'right', 't.pendown',
    'baza')
t.speed(10)
t.left(90)
Numberfile = []
with open("Почтовые числа.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        Numberfile.append(line.rstrip())
Numberfile = tuple(Numberfile)
# printos(Numberfile)
printos(ones)
printos(fours)
printos(ones)
printos(sevens)
printos(zeros)
printos(zeros)
