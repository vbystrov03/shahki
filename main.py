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
place_s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#записываем в список имя пешки
def place(x, y):
    if x == 50 and y == 50:
        place_s[0] = 1



#поле
for x in range(8):
    pygame.draw.line(sc, WHITE, [100*x, 0], [100*x, 799], 1)
for x in range(8):
    pygame.draw.line(sc, WHITE, [0, 100*x], [799, 100*x], 1)


class Peshka(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.circleData = [color, (x, y), 50]

    def draw(self):
        pygame.draw.circle(sc, self.circleData[0], self.circleData[1], self.circleData[2])

    def update(self):
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pg.draw.circle(
                    sc, RED, i.pos, 20)

        """self.rect = self.image.get_rect(center=(x, y))"""

        """self.rect = self.rect(x,y)"""


#первый ряд
Peshka1 = Peshka(150, 50, BLACK)





while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(sc, RED, event.pos, 20)
    Peshka1.draw()


    pygame.display.update()

