import turtle as t

deltadlina = 5
length = 10
t.forward(length / 2)
t.left(90)
t.forward(length)
t.left(90)
t.forward(length)
t.left(90)
t.forward(length + deltadlina)
t.left(90)
length += 2 * deltadlina
for i in range(10):
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length + deltadlina)
    t.left(90)
    t.forward(length + deltadlina)
    length += 2 * deltadlina
    t.left(90)
