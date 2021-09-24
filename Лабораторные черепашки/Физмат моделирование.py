import turtle as t

t.speed(1)
x = -500

y = 0
t.penup()
t.goto(x, y)
t.pendown()
Vy = 80
Vy0 = 80
Vx = 10
x0 = 0
ay = -10
dt = 0.001
while Vy0 >= 0:
    while y >= 0:
        x0 = x
        t.goto(x, y)
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt
        dt += 0.001

    if y <= 0:
        Vy = Vy0 / 1.41
        Vy0 = Vy
        y = 0
        t.goto(x0, 0)
