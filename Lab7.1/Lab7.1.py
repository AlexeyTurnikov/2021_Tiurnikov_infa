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
DARKGREY = (20, 20, 20)
DARKGREEN = (40, 70, 45)
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
    words2 = font2.render(str(points), True, (0, 0, 0))
    place2 = words2.get_rect(center=(100, 132))
    screen.blit(words2, place2)


def win_or_lose_text(winlose):
    """
    Функция, отвечающая за текст при победе или проигрыше
    Если winlose == 1, то победа
    Если winlose == 0, то проигрыш
    """
    if winlose == 0:
        phrase = "Вы проиграли"
    else:
        phrase = "Вы выиграли"
    font = pygame.font.SysFont('Arial', 32)
    words = font.render(phrase, True, (0, 0, 0))
    place = words.get_rect(center=(WIDTH / 2, HEIGHT / 2))
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
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
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

    def __init__(self, x=20, y=530):
        self.screen = screen
        self.f2_power = 75
        self.f2_on = 0
        self.angle = 1
        self.width = 100
        self.height = 100
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
        new_ball = Ball(screen, int(self.x + self.width / 2), int(self.y + self.height / 2), 30)
        new_ball.r += 10
        self.angle = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.angle)
        new_ball.vy = - self.f2_power * math.sin(self.angle)
        extraballs.append(new_ball)
        self.f2_on = 0
        self.f2_power = 75
        return extraballs, extrabullet

    def targeting(self, event_target):
        """
        Прицеливание. Зависит от положения мыши.
        """

        if event_target.pos[0] == self.x + self.width / 2:
            self.angle = math.atan(event_target.pos[1] - (self.y + self.height / 2))
        else:
            self.angle = math.atan(
                (event_target.pos[1] - (self.y + self.height / 2)) / (event_target.pos[0] - (self.x + self.width / 2)))

    def _base_gun_tower(self, tower_screen):
        pygame.draw.circle(tower_screen, DARKGREEN, (int(self.width / 2), int(self.height / 2)),
                           int((self.height + self.width) / 10))
        pygame.draw.rect(tower_screen, DARKGREEN, (
            int(self.width / 2 - (self.height + self.width) / 10), int(self.height / 2),
            int(2 * (self.height + self.width) / 10),
            int((self.width + self.height) / 10)))

    def _gun_tower(self, tower_screen):
        pygame.draw.rect(tower_screen, GREY, (int(self.width / 2), 0, int(self.width / 10), int(self.height / 2)))
        pygame.draw.rect(tower_screen, GREY,
                         (int(self.width / 2) - int(self.width / 10), 0, int(self.width / 10), int(self.height / 2)))
        pygame.draw.polygon(tower_screen, DARKGREY,
                            [(int(self.width / 2 - 2 * self.width / 10), 0), (int(self.width / 2 - self.width / 10), 0),
                             (int(self.width / 2 - self.width / 10), int(self.height / 10))])
        pygame.draw.polygon(tower_screen, DARKGREY,
                            [(int(self.width / 2 + 2 * self.width / 10), 0), (int(self.width / 2 + self.width / 10), 0),
                             (int(self.width / 2 + self.width / 10), int(self.height / 10))])
        self._base_gun_tower(tower_screen)

    def draw(self):
        """
        Функция, отвечающая за правильную прорисовку пушки, ее поворот в зависимости от курсора
        Максимальные размеры пушки (200,200)
        """
        if self.growth == 1 and self.width < 200 and self.height < 200:
            self.width += 1
            self.height += 1
        elif self.growth == 1:
            self.width = 200
            self.height = 200
        if self.growth == 0:
            self.width = 100
            self.height = 100
        gun_screen = pygame.Surface((self.width, self.height))
        gun_screen.set_colorkey(BLACK)
        self._gun_tower(gun_screen)
        if self.angle <= 0:
            rotated_gun_screen = pygame.transform.rotate(gun_screen, 270 - self.angle * 57.3)
        else:
            rotated_gun_screen = pygame.transform.rotate(gun_screen, 90 - self.angle * 57.3)
        new_rect = rotated_gun_screen.get_rect(center=gun_screen.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_gun_screen, new_rect.topleft)

    def power_up(self):
        """
        Функция, отвечающая за силу выстрела в зависимости от продолжительности нажатия.

        """
        if self.f2_on:
            if self.f2_power < 150:
                self.f2_power += 1

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
    def __init__(self, x=20, y=475):
        super().__init__(x, y)
        self.f2_power = 50

    # anti-air-gun = aag
    def _gun_tower(self, tower_screen):
        pygame.draw.rect(tower_screen, GREY,
                         (int(self.width / 2) + int(self.width / 15), 0, int(self.width / 10), int(self.height / 2)))
        pygame.draw.rect(tower_screen, GREY,
                         (int(self.width / 2) - int(self.width / 15) - int(self.width / 10), 0, int(self.width / 10),
                          int(self.height / 2)))
        self._base_gun_tower(tower_screen)

    def fire2_end(self, event_gun, extraballs, extrabullet):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        return: extraballs - измененный массив с мячами, которые вылетели из пушки.
                extrabullet - количество залпов на данный момент.
        """

        extrabullet += 1
        for i in range(10):
            new_ball = Ball(screen, self.x + int(self.width / 2) + random.randint(-2, 2),
                            self.y + int(self.height / 3) + random.randint(-10, 10), 5)
            self.angle = math.atan2((event_gun.pos[1] - new_ball.y), (event_gun.pos[0] - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.angle) * random.randint(1, 3)
            new_ball.vy = - self.f2_power * math.sin(self.angle) * random.randint(1, 3)
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

    def move(self, minx, maxx, miny, maxy, timer):
        """
        Функция, отвечающая за движение цели.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        if self.i % timer == 0:
            if self.x <= minx or self.x >= maxx:
                self.leftrightmovement += 1
            if self.y <= miny or self.y >= maxy:
                self.updownmovement += 1
        if self.leftrightmovement % 2 == 0:
            self.x += self.speed
        else:
            self.x -= self.speed
        if self.updownmovement % 2 == 0:
            self.y += self.speed
        else:
            self.y -= self.speed
        self.i += 1


class Bomb(Target):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image_bomb = pygame.image.load("bomb.png")
        self.rect_bomb = self.image_bomb.get_rect(center=(self.x, self.y))

    def movement(self):
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
        self.r = 0
        self.image_minion = pygame.image.load("minion.jpg")
        self.rect_minion = self.image_minion.get_rect(center=(self.x, self.y))
        self.image_minion.set_colorkey(WHITE)

    def move(self, minx, maxx, miny, maxy, timer):
        super().move(minx, maxx, miny, maxy, timer)
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
finished = False

for amount_of_targets in range(15):
    target = Target()
    targets.append(target)

while not finished:
    screen.fill(WHITE)
    text()
    tank.draw()
    minion.move(25, WIDTH - 125, 45, 55, 1)
    for bomber in bombs:
        bomber.movement()
    for ball in balls:
        ball.draw()
    for target in targets:
        target.move(100, WIDTH - 50, 50, HEIGHT - 120, 15)
    pygame.display.update()
    clock.tick(FPS)
    if points <= 0 or points >= 50:
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
            tank.targeting(event)

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
            win_or_lose_text(0)
        if points >= 50:
            win_or_lose_text(1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
