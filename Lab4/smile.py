import pygame.draw as d
import pygame as pg

pg.init()

FPS = 30
screen = pg.display.set_mode((1000, 800))
d.rect(screen, (255, 255, 255), (0, 0, 1000, 1000))
d.circle(screen, (255, 255, 115), (500, 500), 300)
d.circle(screen, (0, 0, 0), (500, 500), 300, 5)
d.circle(screen, (255, 0, 0), (350, 430), 70)
d.circle(screen, (255, 0, 0), (650, 460), 50)
d.circle(screen, (0, 0, 0), (350, 430), 30)
d.circle(screen, (0, 0, 0), (650, 460), 20)
d.line(screen, (0, 0, 0), (400, 650), (650, 650), 80)
d.line(screen, (0, 0, 0), (150, 200), (500, 400), 50)
d.line(screen, (0, 0, 0), (850, 250), (550, 450), 40)
pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
