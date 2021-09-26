import pygame.draw as d
import pygame as pg
import random
import time


def text1():
    font = pg.font.SysFont('Arial', 72)
    slova = font.render("Бобик - физтех,", True, (0, 0, 0))
    place = slova.get_rect(center=(400, 75))
    screen.blit(slova, place)


def text2():
    font = pg.font.SysFont('Arial', 72)
    text = font.render("Бобик хочет кушать", True, (0, 0, 0))
    place = text.get_rect(center=(400, 190))
    screen.blit(text, place)


def text3():
    font = pg.font.SysFont('Arial', 72)
    text = font.render("Помогите ему найти мясо", True, (0, 0, 0))
    place = text.get_rect(center=(400, 290))
    screen.blit(text, place)


def text4():
    font = pg.font.SysFont('Arial', 72)
    slova = font.render("Ураааа Бобик добыл еды", True, (0, 0, 0))
    place = slova.get_rect(center=(400, 75))
    screen.blit(slova, place)


def runmeat(x1, y1):
    d.ellipse(screen, (255, 50, 50), (x1, y1, 80, 50))
    d.ellipse(screen, (0, 0, 0), (x1, y1, 80, 50), 1)


def fon():
    xzabora = 0
    d.rect(screen, (50, 150, 200), (0, 0, 800, 150))
    d.rect(screen, (200, 150, 0), (0, 150, 800, 600))
    for kolvopalok in range(21):
        d.line(screen, (0, 0, 0), (xzabora, 150), (xzabora, 600), 1)
        xzabora += 39
    d.line(screen, (0, 0, 0), (0, 600), (800, 600), 10)
    d.line(screen, (0, 0, 0), (0, 150), (800, 150), 5)
    d.rect(screen, (0, 200, 100), (0, 600, 800, 800))


def morda(xm, ym, scale):
    # osnova
    d.circle(screen, brown, (xm, ym + 15), 15 * scale)
    d.circle(screen, black, (xm, ym + 15), 15 * scale, 1)
    d.circle(screen, brown, (xm + 70 * scale, ym + 15), 15 * scale)
    d.circle(screen, black, (xm + 70 * scale, ym + 15), 15 * scale, 1)
    d.rect(screen, brown, (xm, ym, 70 * scale, 70 * scale))
    d.rect(screen, black, (xm, ym, 70 * scale, 70 * scale), 1)
    # glaza
    d.ellipse(screen, (255, 255, 255), (xm + 20, ym + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (xm + 20 + 6 * scale, ym + 15 * scale + 3 * scale), 3 * scale - 0.5)
    d.ellipse(screen, (255, 255, 255), (xm + 20 * scale + 30 * scale, ym + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (xm + 20 * scale + 30 * scale + 6 * scale, ym + 15 * scale + 3 * scale),
             3 * scale - 0.5)
    # rot
    d.arc(screen, black, (xm + 5 * scale, ym + 55 * scale, 60 * scale, 40 * scale), 3.14 / 4, 3.14 * 3 / 4, 1)
    d.polygon(screen, (255, 255, 255),
              [[xm + 15 * scale, ym + 60 * scale], [xm + 19 * scale, ym + 57 * scale],
               [xm + 17 * scale, ym + 50 * scale]])
    d.polygon(screen, (255, 255, 255),
              [[xm + 54 * scale, ym + 60 * scale], [xm + 50 * scale, ym + 57 * scale],
               [xm + 52 * scale, ym + 50 * scale]])
    # nos
    d.ellipse(screen, black, (xm + 25 * scale, ym + 30 * scale, 20 * scale, 10 * scale))


def funnymorda(xfm, yfm, scale):
    # osnova
    d.circle(screen, brown, (xfm, yfm + 15), 15 * scale)
    d.circle(screen, black, (xfm, yfm + 15), 15 * scale, 1)
    d.circle(screen, brown, (xfm + 70 * scale, yfm + 15), 15 * scale)
    d.circle(screen, black, (xfm + 70 * scale, yfm + 15), 15 * scale, 1)
    d.rect(screen, brown, (xfm, yfm, 70 * scale, 70 * scale))
    d.rect(screen, black, (xfm, yfm, 70 * scale, 70 * scale), 1)
    # glaza
    d.ellipse(screen, (255, 255, 255), (xfm + 20, yfm + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (xfm + 20 + 6 * scale, yfm + 15 * scale + 3 * scale), 3 * scale - 0.5)
    d.ellipse(screen, (255, 255, 255), (xfm + 20 * scale + 30 * scale, yfm + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (xfm + 20 * scale + 30 * scale + 6 * scale, yfm + 15 * scale + 3 * scale), 3 * scale - 0.5)
    # rot
    d.arc(screen, black, (xfm + 5 * scale, yfm + 43 * scale, 60 * scale, 20 * scale), -3.14 * 5 / 6, -3.14 / 6, 4)
    d.polygon(screen, (255, 255, 255),
              [[xfm + 15 * scale, yfm + 60 * scale], [xfm + 19 * scale, yfm + 57 * scale],
               [xfm + 17 * scale, yfm + 50 * scale]])
    d.polygon(screen, (255, 255, 255),
              [[xfm + 54 * scale, yfm + 60 * scale], [xfm + 50 * scale, yfm + 57 * scale],
               [xfm + 52 * scale, yfm + 50 * scale]])
    # nos
    d.ellipse(screen, black, (xfm + 25 * scale, yfm + 30 * scale, 20 * scale, 10 * scale))


def telo(xt, yt, scale):
    # osnova
    d.ellipse(screen, brown1, (xt, yt, 180 * scale, 70 * scale))
    d.ellipse(screen, black, (xt, yt, 180 * scale, 70 * scale), 1)
    # xvost
    d.ellipse(screen, brown1, (xt + 170 * scale, yt + 25 * scale, 30 * scale, 20 * scale))
    d.ellipse(screen, black, (xt + 170 * scale, yt + 25 * scale, 30 * scale, 20 * scale), 1)


def antitelo(xat, yat, scale):
    # antiosnova
    d.ellipse(screen, brown1, (xat - 180 * scale, yat, 180 * scale, 70 * scale))
    d.ellipse(screen, black, (xat - 180 * scale, yat, 180 * scale, 70 * scale), 1)
    # antixvost
    d.ellipse(screen, brown1, (xat - 195 * scale, yat + 25 * scale, 30 * scale, 20 * scale))
    d.ellipse(screen, black, (xat - 195 * scale, yat + 25 * scale, 30 * scale, 20 * scale), 1)


def lapa(xl, yl, scale):
    d.ellipse(screen, brown1, (xl, yl, 15 * scale, 40 * scale))
    d.ellipse(screen, black, (xl, yl, 15 * scale, 40 * scale), 1)
    d.ellipse(screen, brown1, (xl - 15 * scale, yl + 33 * scale, 25 * scale, 10 * scale))
    d.ellipse(screen, black, (xl - 15 * scale, yl + 33 * scale, 25 * scale, 10 * scale), 1)


def antilapa(xal, yal, scale):
    d.ellipse(screen, brown1, (xal, yal, 15 * scale, 40 * scale))
    d.ellipse(screen, black, (xal, yal, 15 * scale, 40 * scale), 1)
    d.ellipse(screen, brown1, (xal + 7 * scale, yal + 33 * scale, 25 * scale, 10 * scale))
    d.ellipse(screen, black, (xal + 7 * scale, yal + 33 * scale, 25 * scale, 10 * scale), 1)


def sobaka(xs, ys, scale):
    lapa(xs + 70 * scale, ys + 80 * scale, 1.7 * scale)
    lapa(xs + 180 * scale, ys + 80 * scale, 1.7 * scale)
    telo(xs + 40 * scale, ys + 37 * scale, scale)
    morda(xs, ys, scale)


def funnysobaka(xfs, yfs, scale):
    lapa(xfs + 70 * scale, yfs + 80 * scale, 1.7 * scale)
    lapa(xfs + 180 * scale, yfs + 80 * scale, 1.7 * scale)
    telo(xfs + 40 * scale, yfs + 37 * scale, scale)
    funnymorda(xfs, yfs, scale)


def antisobaka(xas, yas, scale):
    antilapa(xas - 50 * scale, yas + 80 * scale, 1.7 * scale)
    antilapa(xas - 155 * scale, yas + 80 * scale, 1.7 * scale)
    antitelo(xas + 20, yas + 37 * scale, scale)
    morda(xas, yas, scale)


def funnyantisobaka(xfas, yfas, scale):
    antilapa(xfas - 50 * scale, yfas + 80 * scale, 1.7 * scale)
    antilapa(xfas - 155 * scale, yfas + 80 * scale, 1.7 * scale)
    antitelo(xfas + 20, yfas + 37 * scale, scale)
    funnymorda(xfas, yfas, scale)


pg.init()
pg.font.init()
brown = (150, 100, 50)
brown1 = (120, 80, 40)
black = (0, 0, 0)
screen = pg.display.set_mode((800, 800))
FPS = 30
x = 101
y = 550
povorot = 0
beg = 0
n = 0
xmeat = 100
ymeat = 700
for i in range(1200):
    fon()
    runmeat(xmeat, ymeat)
    n += 1
    if n > 500:
        xmeat = random.randint(100, 700)
        ymeat = random.randint(630, 770)
        n = 0
    if povorot % 2 == 0:
        if beg % 2 == 0:
            y += 0.5
        elif beg % 2 == 1:
            y -= 0.5
        x += random.randint(2, 5)
        antisobaka(x, y, 1)
    elif povorot % 2 == 1:
        if beg % 2 == 0:
            y += 0.5
        elif beg % 2 == 1:
            y -= 0.5
        x -= random.randint(2, 5)
        sobaka(x, y, 1)
    if n % 50 == 0 and (x > 550 or x < 70):
        povorot += 1
        beg += 1
    if y > 700 or y < 300:
        beg += 1
    text1()
    text2()
    text3()
    pg.display.update()
    time.sleep(0.01)
while True:
    fon()
    if povorot % 2 == 1:
        funnysobaka(x, y, 1)
    if povorot % 2 == 0:
        funnyantisobaka(x, y, 1)
    runmeat(x, y + 75)
    text4()
    pg.display.update()

clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
