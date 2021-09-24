from random import randint
import turtle as t


def pole():
    t.penup()
    t.shape = 'circle'
    t.shapesize(1)
    t.width(5)
    t.goto(-220, 220)
    t.pendown()
    t.goto(-220, -220)
    t.goto(220, -220)
    t.goto(220, 220)
    t.goto(-220, 220)


number_of_turtles = 20
steps_of_time_number = 100
pole()
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.5)
    unit.speed(0)
    unit.penup()
    unit.goto(randint(-200, 200), randint(-200, 200))

for i in range(steps_of_time_number):
    for unit in pool:
        unit.speed(0)
        unit.forward(5)
        unit.left(randint(0, 180))
