import pygame

W, H = 800, 800

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)

game_over = False
speed = 10

sc = pygame.display.set_mode((W, H))
sc.fill(GREY)
pygame.display.set_caption("Shahki by vbystrov")
place_s = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# записываем в список имя пешки
def place(x, y):
    global place_s
    if x == 50 and y == 50:
        place_s[0] = 1
    elif x == 150 and y == 50:
        place_s[1] = 1
    elif x == 250 and y == 50:
        place_s[2] = 1
    elif x == 350 and y == 50:
        place_s[3] = 1
    elif x == 40 and y == 50:
        place_s[0] = 1
    elif x == 550 and y == 50:
        place_s[1] = 1
    elif x == 650 and y == 50:
        place_s[2] = 1
    elif x == 750 and y == 50:
        place_s[3] = 1


# нужно создать функцию, которая создает классы пешки из списка
def pr_place():
    for i in range(len(place_s)):
        if i == 1:
            None


# поле
for x in range(8):
    pygame.draw.line(sc, WHITE, [100 * x, 0], [100 * x, 799], 1)
for x in range(8):
    pygame.draw.line(sc, WHITE, [0, 100 * x], [799, 100 * x], 1)


class Peshka(pygame.sprite.Sprite):
    def __init__(self, x, y, color, name):
        pygame.sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.name = name
        self.color = color

    def draw(self):
        pygame.draw.circle(sc, self.color, (self.startX, self.startY), 50)

    def update(self):
        global place_s
        if self.startX == 50 and self.startY == 50:
            place_s[0] = self.name
        elif self.startX == 150 and self.startY == 50:
            place_s[1] = self.name
        elif self.startX == 250 and self.startY == 50:
            place_s[2] = self.name

        """self.rect = self.image.get_rect(center=(x, y))"""

        """self.rect = self.rect(x,y)"""


Peshka1 = Peshka(50, 50, BLACK, 'Peshka1')
# первый ряд

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and (
                    (event.pos[0] >= 0 and event.pos[0] <= 100) and ((event.pos[1] >= 0 and event.pos[1] <= 100))):
                pygame.draw.circle(sc, RED, event.pos, 20)
                del Peshka1
                Peshka1 = Peshka(150, 50, BLACK, 'Peshka1')
                print(event.pos)

    Peshka1.draw()
    Peshka1.update()
    print(place_s)
    pygame.display.update()
