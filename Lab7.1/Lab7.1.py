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
points = 0
time_text = 0
old_bullet = 0
bullet = 0
balls = []


def text(time):
    """
    Функция, отвечающая за текущий счет и уведомление об уничтожении цели.
    :param time: текущее время существования уведомления об уничтожении цели.
    :return: time: текущее время существования уведомления об уничтожении цели, увеличенное на 1.
    """
    font1 = pygame.font.SysFont('Arial', 80)
    words1 = font1.render(str(points), True, (0, 0, 0))
    place1 = words1.get_rect(center=(75, 100))
    screen.blit(words1, place1)
    if 0 < time < 50:
        time += 1
        font2 = pygame.font.SysFont('Arial', 32)
        words2 = font2.render("Вы уничтожили цель за " + str(old_bullet) + " выстрелов.", True, (0, 0, 0))
        place2 = words2.get_rect(center=(400, 200))
        screen.blit(words2, place2)

    else:
        time = 0

    return time


class Ball:
    def __init__(self, screen_ball: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen_ball
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

            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:

            return True
        else:
            return False


class Gun:
    """
    Класс, отвечающий за пушку.
    """
    def __init__(self, screen_gun):
        self.screen = screen_gun
        self.f2_power = 25
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.width = 20
        self.height = 5
        self.growth = 0

    def fire2_start(self):
        """
        Подготовка к выстрелу
        """
        self.f2_on = 1

    def fire2_end(self, event_gun, extraballs, extrabullet):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        return: extraballs - измененный массив с мячами, которые вылетели из пушки.
                extrabullet - количество выстрелов на данный момент.
        """

        extrabullet += 1
        new_ball = Ball(screen)
        new_ball.r += 5
        self.an = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        extraballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 25
        return extraballs, extrabullet

    def targetting(self, event_target):
        """
        Прицеливание. Зависит от положения мыши.
        """

        if event_target.pos[0] == 20:
            self.an = math.atan(event_target.pos[1] - 450)
        else:
            self.an = math.atan((event_target.pos[1] - 450) / (event_target.pos[0] - 20))

        if self.f2_on:
            self.color = RED

        else:
            self.color = GREY

    def draw(self):
        """
        Функция, отвечающая за правильную прорисовку пушки, ее поворот в зависимости от курсора
        Максимальные размеры пушки (100,13)
        """
        if gun.growth == 1 and self.width < 100 and self.height < 13:
            self.width += 1
            self.height += 0.1
        elif gun.growth == 1:
            self.width = 100
            self.height = 13
        if gun.growth == 0:
            self.width = 20
            self.height = 5
        gun_screen = pygame.Surface((self.width, 2 * self.height))
        gun_screen.set_colorkey(BLACK)
        pygame.draw.rect(gun_screen, self.color, (0, int(self.height / 2), self.width, self.height))

        rotated_gun_screen = pygame.transform.rotate(gun_screen, 180 - self.an * 57.7)
        new_rect = rotated_gun_screen.get_rect(center=gun_screen.get_rect(topleft=(20, 450)).center)
        screen.blit(rotated_gun_screen, new_rect.topleft)

    def power_up(self):
        """
        Функция, отвечающая за силу выстрела в зависимости от продолжительности нажатия.
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    """
    Класс, отвечающий за цели и их поведение.
    """
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = 500
        self.y = 500
        self.r = 10
        self.speed = random.randint(1, 5)
        self.leftrightmovement = random.randint(0, 1)
        self.updownmovement = random.randint(0, 1)
        self.i = 0
        self.color = RED
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(550, 700)
        self.y = random.randint(300, 475)
        self.r = random.randint(10, 50)
        self.color = random.choice(GAME_COLORS)

    def move(self):
        """
        Функция, отвечающая за движение цели.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        if self.i % 15 == 0:
            if self.x <= 400 or self.x >= WIDTH - 50:
                self.leftrightmovement += 1
            if self.y <= 50 or self.y >= HEIGHT - 120:
                self.updownmovement += 1
        if self.leftrightmovement % 2 == 0:
            self.x += self.speed
        if self.leftrightmovement % 2 == 1:
            self.x -= self.speed
        if self.updownmovement % 2 == 0:
            self.y += self.speed
        if self.updownmovement % 2 == 1:
            self.y -= self.speed
        self.i += 1


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
target1.new_target()
target2.new_target()

finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.move()
    target2.move()
    time_text = text(time_text)
    for ball in balls:
        ball.draw()
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
            gun.growth = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            balls, bullet = gun.fire2_end(event, balls, bullet)
            gun.growth = 0
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for ball in balls:
        ball.move()
        if ball.hittest(target1) or ball.hittest(target2):
            time_text = 1
            old_bullet = bullet
            bullet = 0
            points += 1
            if ball.hittest(target1):
                target1.new_target()
                target1.live = 0
            if ball.hittest(target2):
                target2.new_target()
                target2.live = 0

    gun.power_up()

pygame.quit()
