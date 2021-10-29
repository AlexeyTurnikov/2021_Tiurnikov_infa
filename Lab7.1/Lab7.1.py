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
points = 15
old_bullet = 0
bullet = 0
balls = []
targets = []
bombs = []
quit_game = 0

def text():
    """
    Функция, отвечающая за текущий счет и уведомление об уничтожении цели.
    """
    font1 = pygame.font.SysFont('Arial', 16)
    font2 = pygame.font.SysFont('Arial', 32)
    words1 = font1.render("Оставшиеся снаряды: ", True, (0, 0, 0))
    place1 = words1.get_rect(center=(100, 100))
    screen.blit(words1, place1)
    words2 = font2.render(str(points), True, (0,0,0))
    place2 = words2.get_rect(center=(100,132))
    screen.blit(words2,place2)

def lose_text():
    font = pygame.font.SysFont('Arial', 32)
    words = font.render("Вы проиграли", True, (0, 0, 0))
    place = words.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(words, place)

def win_text():
    font = pygame.font.SysFont('Arial', 32)
    words = font.render("Вы выиграли", True, (0, 0, 0))
    place = words.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(words, place)

class Ball:
    def __init__(self, screen_ball: pygame.Surface, x=40, y=450, live_time=75):
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
        self.live_time = live_time + random.randint(-3, 3)

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
        if self.live >= self.live_time:
            self.r = 0
            self.x = 1000
            self.y = 1000

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

    def __init__(self, x=20, y=500):
        self.screen = screen
        self.f2_power = 75
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.width = 40
        self.height = 10
        self.growth = 0
        self.x = x
        self.y = y
        self.left = 0
        self.right = 0

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
        new_ball = Ball(screen, self.x, self.y)
        new_ball.r += 10
        self.an = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        extraballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 75
        return extraballs, extrabullet

    def targetting(self, event_target):
        """
        Прицеливание. Зависит от положения мыши.
        """

        if event_target.pos[0] == self.x:
            self.an = math.atan(event_target.pos[1] - self.y)
        else:
            self.an = math.atan((event_target.pos[1] - self.y) / (event_target.pos[0] - self.x))

        if self.f2_on:
            self.color = RED

        else:
            self.color = GREY

    def draw(self):
        """
        Функция, отвечающая за правильную прорисовку пушки, ее поворот в зависимости от курсора
        Максимальные размеры пушки (100,13)
        """
        if self.growth == 1 and self.width < 100 and self.height < 16:
            self.width += 1
            self.height += 0.1
        elif self.growth == 1:
            self.width = 100
            self.height = 16
        if self.growth == 0:
            self.width = 40
            self.height = 10
        gun_screen = pygame.Surface((self.width, 2 * self.height))
        gun_screen.set_colorkey(BLACK)
        pygame.draw.rect(gun_screen, self.color, (0, int(self.height / 2), self.width, self.height))
        pygame.draw.circle(gun_screen, GREEN, (self.width - 10, self.height), self.width/3 + 2)
        rotated_gun_screen = pygame.transform.rotate(gun_screen, 180 - self.an * 57.7)
        new_rect = rotated_gun_screen.get_rect(center=gun_screen.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_gun_screen, new_rect.topleft)

    def power_up(self):
        """
        Функция, отвечающая за силу выстрела в зависимости от продолжительности нажатия.

        """
        if self.f2_on:
            if self.f2_power < 150:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self, event_move):
        if event_move.type == pygame.KEYDOWN:
            if event_move.key == pygame.K_LEFT:
                self.left = 1
            if event_move.key == pygame.K_RIGHT:
                self.right = 1
        if event_move.type == pygame.KEYUP:
            if event_move.key == pygame.K_LEFT:
                self.left = 0
            if event_move.key == pygame.K_RIGHT:
                self.right = 0
        if self.left == 1:
            self.x -= 1
        if self.right == 1:
            self.x += 1


class AntiAirGun(Gun):
    def __init__(self, x=20, y=500):
        super().__init__(x, y)
        self.f2_power = 50

    # anti-air-gun = aag
    def draw(self):

        aag_screen = pygame.Surface((self.width, 2 * self.height))
        aag_screen.set_colorkey(BLACK)
        pygame.draw.rect(aag_screen, self.color, (0, int(self.height / 2), self.width, self.height))
        pygame.draw.circle(aag_screen, GREEN, (self.width - 10, self.height), 12)
        rotated_aag_screen = pygame.transform.rotate(aag_screen, 180 - self.an * 57.7)
        new_rect = rotated_aag_screen.get_rect(center=aag_screen.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_aag_screen, new_rect.topleft)

    def fire2_end(self, event_gun, extraballs, extrabullet):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        return: extraballs - измененный массив с мячами, которые вылетели из пушки.
                extrabullet - количество залпов на данный момент.
        """

        extrabullet += 1
        for i in range(10):
            new_ball = Ball(screen, self.x + random.randint(-2, 2), self.y + random.randint(-10, 10), 5)
            self.an = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an) * random.randint(1, 3)
            new_ball.vy = - self.f2_power * math.sin(self.an) * random.randint(1, 3)
            extraballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 50
        return extraballs, extrabullet


class Target:
    """
    Класс, отвечающий за цели и их поведение.
    """

    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = random.randint(300, 700)
        self.y = random.randint(100, 475)
        self.r = random.randint(5, 50)
        self.color = random.choice(GAME_COLORS)
        self.speed = random.randint(1, 10)
        self.leftrightmovement = random.randint(0, 1)
        self.updownmovement = random.randint(0, 1)
        self.i = 0

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
            if self.x <= 100 or self.x >= WIDTH - 50:
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


class Bomb(Target):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image_bomb = pygame.image.load("bomb.png")
        self.rect_bomb = self.image_bomb.get_rect(center=(self.x, self.y))

    def move(self):
        self.y += self.speed
        screen.blit(self.image_bomb, (self.x, self.y))

    def boom(self):
        self.live = 0
        bomb_ball = Ball(screen, self.x, self.y, 3)
        bomb_ball.r += 70
        bomb_ball.color = BLACK
        balls.append(bomb_ball)
        self.x += 1000


class Minion(Target):
    def __init__(self, x=random.randint(100, 700), y=50):
        super().__init__()
        self.x = x
        self.y = y
        self.image_minion = pygame.image.load("minion.jpg")
        self.rect_minion = self.image_minion.get_rect(center=(self.x, self.y))
        self.image_minion.set_colorkey(WHITE)

    def move(self):
        if self.i % 15 == 0:
            if self.x <= 25 or self.x >= WIDTH - 125:
                self.leftrightmovement += 1
        if self.leftrightmovement % 2 == 0:
            self.x += self.speed
        if self.leftrightmovement % 2 == 1:
            self.x -= self.speed
        self.i += 1
        screen.blit(self.image_minion, (self.x, self.y))

    def spawn(self):
        bomb = Bomb(self.x, self.y + 10)
        bombs.append(bomb)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.time.set_timer(pygame.USEREVENT, 10)
pygame.time.set_timer(pygame.USEREVENT + 1, 5000)
clock = pygame.time.Clock()
tank = AntiAirGun()
minion = Minion()
for amount_of_targets in range(15):
    target = Target()
    targets.append(target)

finished = False

while not finished:
    screen.fill(WHITE)
    text()
    tank.draw()
    minion.move()
    for bomber in bombs:
        bomber.move()
    for ball in balls:
        ball.draw()
    for target in targets:
        target.move()
    pygame.display.update()
    clock.tick(FPS)
    if points <= 0:
        finished = True
    for event in pygame.event.get():
        tank.move(event)
        if event.type == pygame.USEREVENT + 1:
            minion.spawn()
        if event.type == pygame.QUIT:
            finished = True
            quit_game = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if isinstance(tank, Gun) and not isinstance(tank, AntiAirGun):
                    tank = AntiAirGun(tank.x, tank.y)
                else:
                    tank = Gun(tank.x, tank.y)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tank.fire2_start()
            tank.growth = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            balls, bullet = tank.fire2_end(event, balls, bullet)
            points -= 2
            tank.growth = 0
        elif event.type == pygame.MOUSEMOTION:
            tank.targetting(event)

    for ball in balls:
        ball.move()
        for target in targets:
            if ball.hittest(target):
                old_bullet = bullet
                bullet = 0
                points += 1
                target.new_target()
                target.live = 0
        for bomber in bombs:
            if ball.hittest(bomber):
                old_bullet = bullet
                bullet = 0
                points += 10
                bomber.boom()
    tank.power_up()
finished = False
if quit_game != 1:
    screen.fill(WHITE)
    while not finished:
        if points <= 0:
            lose_text()
        if points >= 50:
            win_text()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
