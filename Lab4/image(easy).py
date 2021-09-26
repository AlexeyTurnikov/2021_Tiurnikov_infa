import pygame.draw as d
import pygame as pg


def text1():
    font = pg.font.SysFont('Arial', 24)
    slova = font.render("Бобик живет тут", True, (0, 0, 0))
    place = slova.get_rect(center=(650, 560))
    screen.blit(slova, place)


def runmeat(x1, y1):
    d.ellipse(screen, (255, 50, 50), (x1, y1, 80, 50))
    d.ellipse(screen, (0, 0, 0), (x1, y1, 80, 50), 1)


def house():
    d.rect(screen, colourhouse, (550, 530, 200, 180))
    d.rect(screen, black, (550, 530, 200, 180), 2)
    d.circle(screen, colourdoor, (650, 630), 30)
    d.circle(screen, black, (650, 630), 30, 2)
    d.rect(screen, colourdoor, (620, 630, 60, 80))
    d.line(screen, black, (620, 630), (620, 710), 2)
    d.line(screen, black, (680, 630), (680, 710), 2)
    d.line(screen, colourhouse, (750, 620), (790, 590), 180)
    d.line(screen, black, (750, 530), (790, 500), 5)
    d.line(screen, black, (750, 710), (790, 680), 2)
    d.line(screen, black, (790, 680), (790, 500), 2)
    d.polygon(screen, colourroof, ((550, 530), (750, 530), (650, 430)))
    d.polygon(screen, colourroof, ((750, 530), (790, 500), (650, 430)))
    d.line(screen, black, (550, 530), (650, 430), 2)
    d.line(screen, black, (750, 530), (650, 430), 2)
    d.line(screen, black, (790, 500), (650, 430), 2)
    text1()
    funnymorda(690, 580, 0.6)


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
    house()


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
    d.ellipse(screen, (255, 255, 255), (xfm + 20 * scale, yfm + 15 * scale, 12 * scale, 6 * scale))
    d.circle(screen, black, (xfm + 20 * scale + 6 * scale, yfm + 15 * scale + 3 * scale), 3 * scale - 0.5)
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


pg.init()
pg.font.init()
brown = (150, 100, 50)
brown1 = (120, 80, 40)
black = (0, 0, 0)
colourroof = (100, 60, 10)
colourhouse = (150, 50, 50)
colourdoor = (200, 100, 50)
screen = pg.display.set_mode((800, 800))
FPS = 30
x = 101
y = 550
povorot = 0
beg = 0
n = 0
xmeat = 100
ymeat = 700

fon()
antisobaka(250, 650, 1)
funnysobaka(350, 550, 1.5)
runmeat(325, 700)
pg.display.update()

clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
