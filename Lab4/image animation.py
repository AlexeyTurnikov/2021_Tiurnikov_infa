import pygame.draw as d
import pygame as pg
import random
import time

red = (255, 50, 50)
brown = (150, 100, 50)
dark_brown = (120, 80, 40)
black = (0, 0, 0)

FPS = 30
x = 101
y = 550
x_meat = 100
y_meat = 700


def text(st):
    """
    writes string from the text on the screen
    :param st: number of string where 1 = "Бобик - физтех,"; 2 = "Бобик хочет кушать"; 3 = "Помогите ему найти мясо"; 4 = "Ураааа Бобик добыл еды"
    :return: one string from the dictionary of strings written in the animation
    """
    font = pg.font.SysFont('Arial', 72)
    texts = ["Бобик - физтех,", "Бобик хочет кушать", "Помогите ему найти мясо", "Ураааа Бобик добыл еды"]
    coord_y = [75, 190, 290, 75]
    words = font.render(texts[st - 1], True, (0, 0, 0))
    place = words.get_rect(center=(400, coord_y[st - 1]))
    screen.blit(words, place)


def meat(x, y):
    """
    draws meat
    :param x: horizontal coordinate of meat
    :param y: vertical coordinate of meat
    :return: a drawing of meat
    """
    d.ellipse(screen, red, (x, y, 80, 50))
    d.ellipse(screen, black, (x, y, 80, 50), 1)


def background():
    """
    draws the background
    :return: the drawing of a background
    """
    x_fence = 0
    d.rect(screen, (50, 150, 200), (0, 0, 800, 150))
    d.rect(screen, (200, 150, 0), (0, 150, 800, 600))
    for stick in range(21):
        d.line(screen, (0, 0, 0), (x_fence, 150), (x_fence, 600), 1)
        x_fence += 39
    d.line(screen, (0, 0, 0), (0, 600), (800, 600), 10)
    d.line(screen, (0, 0, 0), (0, 150), (800, 150), 5)
    d.rect(screen, (0, 200, 100), (0, 600, 800, 800))


def face(x, y, scale, happy=0):
    """
    draws the dog's face
    :param x: horizontal coordinate of the face
    :param y: vertical coordinate of the face
    :param scale: scale
    :param happy: if the face doesn't express happiness = 0, else = 1
    :return: the drawing of the dog's face
    """
    # base
    d.circle(screen, brown, (x, y + 15), 15 * scale)
    d.circle(screen, black, (x, y + 15), 15 * scale, 1)
    d.circle(screen, brown, (x + 70 * scale, y + 15), 15 * scale)
    d.circle(screen, black, (x + 70 * scale, y + 15), 15 * scale, 1)
    d.rect(screen, brown, (x, y, 70 * scale, 70 * scale))
    d.rect(screen, black, (x, y, 70 * scale, 70 * scale), 1)
    # eyes
    d.ellipse(screen, (255, 255, 255), (x + 20, y + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (x + 20 + 6 * scale, y + 15 * scale + 3 * scale), 3 * scale - 0.5)
    d.ellipse(screen, (255, 255, 255), (x + 20 * scale + 30 * scale, y + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (x + 20 * scale + 30 * scale + 6 * scale, y + 15 * scale + 3 * scale), 3 * scale - 0.5)
    # nose
    d.ellipse(screen, black, (x + 25 * scale, y + 30 * scale, 20 * scale, 10 * scale))
    # mouth
    if happy == 0:
        d.arc(screen, black, (x + 5 * scale, y + 55 * scale, 60 * scale, 40 * scale), 3.14 / 4, 3.14 * 3 / 4, 1)
        d.polygon(screen, (255, 255, 255), [[x + 15 * scale, y + 60 * scale], [x + 19 * scale, y + 57 * scale],
                                            [x + 17 * scale, y + 50 * scale]])
        d.polygon(screen, (255, 255, 255), [[x + 54 * scale, y + 60 * scale], [x + 50 * scale, y + 57 * scale],
                                            [x + 52 * scale, y + 50 * scale]])
    else:
        d.arc(screen, black, (x + 5 * scale, y + 43 * scale, 60 * scale, 20 * scale), -3.14 * 5 / 6, -3.14 / 6, 4)
        d.polygon(screen, (255, 255, 255), [[x + 15 * scale, y + 60 * scale], [x + 19 * scale, y + 57 * scale],
                                            [x + 17 * scale, y + 50 * scale]])
        d.polygon(screen, (255, 255, 255), [[x + 54 * scale, y + 60 * scale], [x + 50 * scale, y + 57 * scale],
                                            [x + 52 * scale, y + 50 * scale]])


def body(x, y, scale, orient=1):
    """
    draws dog's body
    :param x: horizontal coordinate of the body
    :param y: vertical coordinate of the body
    :param scale: scale
    :param orient: orientation of the body; 1 = left, else = right
    :return: the dog's body
    """
    if orient == 1:
        # base
        d.ellipse(screen, dark_brown, (x, y, 180 * scale, 70 * scale))
        d.ellipse(screen, black, (x, y, 180 * scale, 70 * scale), 1)
        # tail
        d.ellipse(screen, dark_brown, (x + 170 * scale, y + 25 * scale, 30 * scale, 20 * scale))
        d.ellipse(screen, black, (x + 170 * scale, y + 25 * scale, 30 * scale, 20 * scale), 1)
    else:
        # reversed base
        d.ellipse(screen, dark_brown, (x - 180 * scale, y, 180 * scale, 70 * scale))
        d.ellipse(screen, black, (x - 180 * scale, y, 180 * scale, 70 * scale), 1)
        # reversed tail
        d.ellipse(screen, dark_brown, (x - 195 * scale, y + 25 * scale, 30 * scale, 20 * scale))
        d.ellipse(screen, black, (x - 195 * scale, y + 25 * scale, 30 * scale, 20 * scale), 1)


def leg(x, y, scale, orient=1):
    """
    draws an oriented leg
    :param x: horizontal coordinate of the leg
    :param y: horizontal coordinate of the leg
    :param scale: scale
    :param orient: orientation of the leg: 1 = left, else = right
    :return: drawing of the dog's leg
    """
    if orient == 1:
        d.ellipse(screen, dark_brown, (x, y, 15 * scale, 40 * scale))
        d.ellipse(screen, black, (x, y, 15 * scale, 40 * scale), 1)
        d.ellipse(screen, dark_brown, (x - 15 * scale, y + 33 * scale, 25 * scale, 10 * scale))
        d.ellipse(screen, black, (x - 15 * scale, y + 33 * scale, 25 * scale, 10 * scale), 1)
    else:
        d.ellipse(screen, dark_brown, (x, y, 15 * scale, 40 * scale))
        d.ellipse(screen, black, (x, y, 15 * scale, 40 * scale), 1)
        d.ellipse(screen, dark_brown, (x + 7 * scale, y + 33 * scale, 25 * scale, 10 * scale))
        d.ellipse(screen, black, (x + 7 * scale, y + 33 * scale, 25 * scale, 10 * scale), 1)


def dog(x, y, scale, orient=1, happy=0, ):
    """
    draws a dog
    :param x: horizontal coordinate of the dog
    :param y: vertical coordinate of the dog
    :param scale: scale
    :param: orientation of the dog: 1 = left, anything else = right
    :return: the drawing of a dog
    """
    if orient == 1:
        leg(x + 70 * scale, y + 80 * scale, 1.7 * scale)
        leg(x + 180 * scale, y + 80 * scale, 1.7 * scale)
        body(x + 40 * scale, y + 37 * scale, scale)
    else:
        leg(x - 50 * scale, y + 80 * scale, 1.7 * scale, -1)
        leg(x - 155 * scale, y + 80 * scale, 1.7 * scale, -1)
        body(x + 20, y + 37 * scale, scale, -1)
    face(x, y, scale, happy)


pg.init()
pg.font.init()

screen = pg.display.set_mode((800, 800))

left_right = 0
up_down = 0
n = 0
for i in range(1200):
    background()
    meat(x_meat, y_meat)
    n += 1
    if n > 500:
        x_meat = random.randint(100, 700)
        y_meat = random.randint(630, 770)
        n = 0
    if left_right % 2 == 0:
        if up_down % 2 == 0:
            y += 0.5
        elif up_down % 2 == 1:
            y -= 0.5
        x += 3
        dog(x, y, 1, -1)
    elif left_right % 2 == 1:
        if up_down % 2 == 0:
            y += 0.5
        elif up_down % 2 == 1:
            y -= 0.5
        x -= 3
        dog(x, y, 1, 1, 0)
    if n % 50 == 0 and (x > 550 or x < 70):
        left_right += 1
        up_down += 1
    if y > 700 or y < 300:
        up_down += 1
    text(1)
    text(2)
    text(3)
    pg.display.update()
    time.sleep(0.01)

while True:
    background()
    if left_right % 2 == 1:
        dog(x, y, 1, 1, 1)
    if left_right % 2 == 0:
        dog(x, y, 1, -1, 1)
    meat(x, y + 75)
    text(4)
    pg.display.update()

clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
