import pygame
import pygame.draw as draw
import random
from random import randint

pygame.init()
n = 10
playtime = 1000 - 1
score = 0

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
screen = pygame.display.set_mode((1100, 800))
clock = pygame.time.Clock()
finished = False


def new_ball():
    """
    Функция, создающая шарик в случайном месте, со случайным радиусом, со случайным цветом из массива цветов.
    :return: x-координата нового шарика, y-координата нового шарика, радиус нового шарика, цвет нового шарика
    """
    x_new = randint(100, 700)
    y_new = randint(100, 500)
    r_new = randint(30, 50)
    color_new = COLORS[randint(0, 5)]
    ball_surface = pygame.Surface((100, 100))
    ball_surface.set_colorkey(BLACK)
    draw.circle(ball_surface, color_new, (50, 50), r_new)
    screen.blit(ball_surface, (x_new, y_new))
    return x_new, y_new, r_new, color_new


def ball(x_ball, y_ball, r_ball, color_ball):
    """
    Функция, рисующая шарик по заданным координатам, радиусу и цвету
    :param x_ball: координата x для шарика
    :param y_ball: координата y для шарика
    :param r_ball: радиус шарика
    :param color_ball: цвет шарика
    """
    ball_surface = pygame.Surface((100, 100))
    ball_surface.set_colorkey(BLACK)
    draw.circle(ball_surface, color_ball, (50, 50), r_ball)
    screen.blit(ball_surface, (x_ball, y_ball))


def movement(number, velocity):
    """
    Функция, отвечающая за определение направления движения шарика и скорость его движения
    :param number: Порядковый номер шарика
    :param velocity: Максимальная скорость шарика
    """
    if leftrightmovement[number] % 2 == 0:
        x[number] += random.uniform(3*velocity/4,velocity)
    if leftrightmovement[number] % 2 == 1:
        x[number] -= random.uniform(3*velocity/4,velocity)
    if updownmovement[number] % 2 == 0:
        y[number] += random.uniform(3*velocity/4,velocity)
    if updownmovement[number] % 2 == 1:
        y[number] -= random.uniform(3*velocity/4,velocity)
    if x[number] >= 1050 or x[number] <= 50:
        leftrightmovement[number] += 1
    if y[number] >= 750 or y[number] <= 50:
        updownmovement[number] += 1


def click():
    """
    Функция, отвечающая на вопрос: "Попал ли игрок по шарику?".
    :return: Количество набранных очков
    """
    count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = event.pos
            for number in range(0, n):
                if (x_mouse - x[number]) ** 2 + (y_mouse - y[number]) ** 2 <= (2 * r[number]) ** 2:
                    ball(x[number], y[number], r[number], WHITE)
                    r[number] = 0
                    count += 1
                    pygame.display.update()
    return count


x = []
y = []
r = []
old_r = []
color = []
time = []
leftrightmovement = []
updownmovement = []

screen.fill(WHITE)

for i in range(0, n):
    x.append(0)
    y.append(0)
    r.append(0)
    color.append(0)
    leftrightmovement.append(randint(-1, 1))
    updownmovement.append(randint(-1, 1))
    time.append(randint(0, 300))
    x[i], y[i], r[i], color[i] = new_ball()
    old_r.append(r[i])

pygame.display.update()

while not finished:
    for i in range(0, n):
        time[i] += 1
        score += click()
        ball(x[i], y[i], r[i], WHITE)
        movement(i, 7)

        if time[i] % 600 == 0:
            r[i] = old_r[i]
        if time[i] % 250 == 0:
            r[i] = 0

        ball(x[i], y[i], r[i], color[i])
        pygame.display.update()

    if time[0] == playtime:
        finished = True
        print("Поздравляем! Количество попаданий: " + str(score))

pygame.quit()
