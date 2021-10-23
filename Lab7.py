import math
import random
import pygame

FPS = 30
g = 10
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 0
        self.t = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        if HEIGHT - 100 >= self.y >= 100:
            self.y -= self.vy * self.t - (g / 2) * self.t ** 2
            self.vy -= g * self.t
            self.t += 0.05
            self.live += 1
        elif self.y > HEIGHT - 100 and abs(self.vy) > 7:
            self.y = HEIGHT - 101
            self.vy = -self.vy / 1.41
            self.t = 0.3
        elif self.y < 100 and abs(self.vy) > 7:
            self.y = 101
            self.vy = -self.vy / 1.41
            self.t = 0.3
        if abs(self.vy) < 7 and self.live > 15:
            self.vy = 0

        if WIDTH - 10 >= self.x >= 10:
            self.x += self.vx * self.t
        elif self.x > WIDTH - 10:
            self.x = WIDTH - 15
            self.vx = -self.vx / 2
        elif self.x < 10:
            self.x = 15
            self.vx = -self.vx / 2

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        if self.live >= 75:
            self.r = 0

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 25
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.width = 20
        self.height = 5

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 25


    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] == 20:
                self.an = math.atan(event.pos[1] - 450)
            else:
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 20))

        if self.f2_on:
            self.color = RED
            self.width += 1
            self.height += 0.1
        else:
            self.color = GREY
            self.width = 20
            self.height = 5

    def draw(self):
        gun_screen = pygame.Surface((self.width, 2*self.height))
        gun_screen.set_colorkey(BLACK)
        pygame.draw.rect(gun_screen, self.color, (0, int(self.height/2), self.width, self.height))

        rotated_gun_screen = pygame.transform.rotate(gun_screen, 180 - self.an * 57.7)
        new_rect = rotated_gun_screen.get_rect(center=gun_screen.get_rect(topleft=(20, 450)).center)
        screen.blit(rotated_gun_screen, new_rect.topleft)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 500
        self.y = 500
        self.r = 10
        self.color = RED
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(550, 700)
        self.y = random.randint(300, 475)
        self.r = random.randint(10, 50)
        self.color = random.choice(GAME_COLORS)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for ball in balls:
        ball.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for ball in balls:
        ball.move()
        if ball.hittest(target):
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()
