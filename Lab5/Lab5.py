import pygame
from random import randint

pygame.init()

Width = 1100
Height = 700
screen = pygame.display.set_mode((Width, Height))
finished = False
score = 29
time = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

family = pygame.sprite.Group()  # Семья смешариков
family_massive = []  # Массив с данными смешариков
family_must_back = []  # Массив с номерами убитых смешариков
nanny_group = pygame.sprite.Group()  # Группа ЖЕЛЕЗНОЙ НЯНИ
SMESHARIKI = ["Kopatych.png", "Sovynja.png", "Nyusha.png", "Losyash.png", "Ezhik.png", "Barash.png", "Pin.png",
              "Krosh.png",
              "Karkarych.png"]
SMESHARIKI_SURF = []


def background(background_number):
    """
    Функция, рисующая задний фон.
    :param background_number: 1 - заставка смешариков. 2 - ангар Пина. 3 - ЖЕЛЕЗНАЯ НЯНЯ. 4 - смешарики с тортом.
    """
    surface = pygame.image.load("clear.png")
    if background_number == 1:
        surface = pygame.image.load("fon.png")
    if background_number == 2:
        surface = pygame.image.load("Svalka.png")
    if background_number == 3:
        surface = pygame.image.load("Ironwoman.png")
    if background_number == 4:
        surface = pygame.image.load("Pobeda.png")
    screen.blit(surface, (0, 0))


def text(count, condition):
    """
    Выводит на экран текущий счет и текст при проигрыше.
    :param count: Текущий счет
    :param condition: 0 - игра идет. 1 - победа. -1 - проигрыш
    """
    if condition == 0:
        font = pygame.font.SysFont('Arial', 80)
        words = font.render("Счёт: " + str(count), True, (0, 0, 0))
        place = words.get_rect(center=(125, 75))
        screen.blit(words, place)
    if condition == -1:
        font = pygame.font.SysFont('Arial', 80)
        words1 = font.render("ЖЕЛЕЗНАЯ НЯНЯ", True, (0, 0, 0))
        words2 = font.render("обыграла вас", True, (0, 0, 0))
        place1 = words1.get_rect(center=(550, 550))
        place2 = words2.get_rect(center=(550, 650))
        screen.blit(words1, place1)
        screen.blit(words2, place2)
    if condition == 1:
        font = pygame.font.SysFont('Arial', 80)
        words1 = font.render("Вы обыграли", True, (0, 0, 0))
        words2 = font.render("ЖЕЛЕЗНУЮ НЯНЮ", True, (0, 0, 0))
        place1 = words1.get_rect(center=(550, 550))
        place2 = words2.get_rect(center=(550, 650))
        screen.blit(words1, place1)
        screen.blit(words2, place2)


def click(nanny_come=False):
    """
    Проверяет попал ли игрок по смешарику и удаляет смешарика в случае попадания.
    Если игрок попадает по смешарику, то ему добавляется 2 балла.
    Если игрок попадает по ЖЕЛЕЗНОЙ НЯНЕ, то ему снимается балл
    :param nanny_come: Появилась ли уже ЖЕЛЕЗНАЯ НЯНЯ?
    """
    for event in pygame.event.get():
        global score
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = event.pos
            for ball in family_massive:
                if abs(x_mouse - (ball.rect.x + 75)) <= 75 and abs(y_mouse - (ball.rect.y + 75)) <= 75:
                    ball.kill()
                    family_massive.remove(ball)
                    family_must_back.append(ball.number)
                    score += 2
            if nanny_come is True and abs(x_mouse - (nanny.rect.x + 75)) <= 100 and abs(
                    y_mouse - (nanny.rect.y + 75)) <= 100:
                score -= 1


def back():
    """
    Возвращает по одному убитому смешарику обратно на экран каждые 45 итераций.
    """
    if len(family_must_back) > 0 and time % 25 == 0:
        family_massive.append(
            Ball(randint(100, Width), randint(100, Height), SMESHARIKI_SURF[family_must_back[0]], family))
        family_must_back.remove(family_must_back[0])


class Ball(pygame.sprite.Sprite):
    """
    Класс создающий смешариков
    """

    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        number = 0
        self.image = surf
        for photo in SMESHARIKI_SURF:
            if surf != photo:
                number += 1
            if surf == photo:
                self.number = number
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed = randint(1, 20)
        self.leftrightmovement = randint(0, 1)
        self.updownmovement = randint(0, 1)
        self.i = 0

    def update(self):
        """
        Функция, отвечающая за определение направления движения смешарика и скорость его движения
        """
        if self.i % 7 == 0:
            if self.rect.x <= 10 or self.rect.x >= Width - 160:
                self.leftrightmovement += 1
            if self.rect.y <= 10 or self.rect.y >= Height - 160:
                self.updownmovement += 1
        if self.leftrightmovement % 2 == 0:
            self.rect.x += self.speed
        if self.leftrightmovement % 2 == 1:
            self.rect.x -= self.speed
        if self.updownmovement % 2 == 0:
            self.rect.y += self.speed
        if self.updownmovement % 2 == 1:
            self.rect.y -= self.speed
        self.i += 1


class Nanny(pygame.sprite.Sprite):
    """
    Класс, отвечающий за создание ЖЕЛЕЗНОЙ НЯНИ.
    """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Nyanya.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 15
        self.leftrightmovement = 0
        self.updownmovement = 0

    def movement(self):
        if self.rect.x <= 150 or self.rect.x >= Width - 100:
            self.leftrightmovement += 1
        if self.rect.y <= 150 or self.rect.y >= Height - 100:
            self.updownmovement += 1
        if self.leftrightmovement % 2 == 0:
            self.rect.x += self.speed
        if self.leftrightmovement % 2 == 1:
            self.rect.x -= self.speed
        if self.updownmovement % 2 == 0:
            self.rect.y += self.speed
        if self.updownmovement % 2 == 1:
            self.rect.y -= self.speed

    def update(self):
        """
        Функция, отвечающая за определение направления движения ЖЕЛЕЗНОЙ НЯНИ, скорость движения, выбор цели.
        """
        if self.rect.x <= 10 or self.rect.x >= Width - 160:
            self.leftrightmovement += 1
        if self.rect.y <= 10 or self.rect.y >= Height - 160:
            self.updownmovement += 1

        if len(family_massive) > 0:
            sacrifice = family_massive[0]
            if self.rect.x - sacrifice.rect.x < 0:
                self.rect.x += self.speed
            if self.rect.x - sacrifice.rect.x > 0:
                self.rect.x -= self.speed
            if self.rect.y - sacrifice.rect.y < 0:
                self.rect.y += self.speed
            if self.rect.y - sacrifice.rect.y > 0:
                self.rect.y -= self.speed
        else:
            if self.rect.x <= 150 or self.rect.x >= Width - 100:
                self.leftrightmovement += 1
            if self.rect.y <= 150 or self.rect.y >= Height - 100:
                self.updownmovement += 1
            if self.leftrightmovement % 2 == 0:
                self.rect.x += self.speed
            if self.leftrightmovement % 2 == 1:
                self.rect.x -= self.speed
            if self.updownmovement % 2 == 0:
                self.rect.y += self.speed
            if self.updownmovement % 2 == 1:
                self.rect.y -= self.speed


def murder():
    """
    Функция, отвечающая на вопрос: "Догнала ли ЖЕЛЕЗНАЯ НЯНЯ цель или нет?"
    Если ЖЕЛЕЗНАЯ НЯНЯ догоняет цель, то у игрока снимается 1 балл.
    """
    if len(family_massive) > 0:
        sacrifice = family_massive[0]
        if abs(nanny.rect.x - sacrifice.rect.x) < 75 and abs(nanny.rect.x - sacrifice.rect.x) < 75:
            sacrifice.kill()
            family_massive.remove(sacrifice)
            family_must_back.append(sacrifice.number)
            global score
            score -= 1


for i in range(len(SMESHARIKI)):
    SMESHARIKI_SURF.append(pygame.image.load(SMESHARIKI[i]))
    family_massive.append(Ball(randint(100, Width), randint(100, Height), SMESHARIKI_SURF[i], family))

nanny = Nanny(550, 400)
nanny.add(nanny_group)

while score < 20:  # начало игры
    background(1)
    time += 1
    family.draw(screen)
    family.update()
    text(score, 0)
    pygame.time.delay(20)
    click(False)
    back()
    pygame.display.update()
    for something in pygame.event.get():
        if something.type == pygame.QUIT:
            pygame.quit()

while 0 < score < 30:  # Появление ЖЕЛЕЗНОЙ НЯНИ
    background(2)
    time += 1
    family.draw(screen)
    family.update()

    nanny_group.draw(screen)
    nanny_group.update()
    murder()

    text(score, 0)
    click(True)
    back()
    pygame.time.delay(20)
    pygame.display.update()
    for something in pygame.event.get():
        if something.type == pygame.QUIT:
            pygame.quit()

time = 0

if score <= 0:
    while not finished:  # Проигрыш
        time += 1
        background(3)
        text(score, -1)
        pygame.display.update()
        if time % 5000 == 0:
            finished = True
        for something in pygame.event.get():
            if something.type == pygame.QUIT:
                finished = True

if score >= 30:
    while not finished:  # Победа
        time += 1
        background(4)
        text(score, 1)
        pygame.display.update()
        if time % 500 == 0:
            finished = True
        for something in pygame.event.get():
            if something.type == pygame.QUIT:
                finished = True
pygame.quit()
