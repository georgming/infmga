import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 200
a = 1200
b = 600
screen = pygame.display.set_mode((a, b))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN]
N = 10

BALLS = [0] * N
for i in range(N):
    BALLS[i] = [0] * 4


for i in range(N):
    r = randint(30, 60)
    x = randint(50, 900)
    y = randint(50, 500)
    color = COLORS[randint(0, 3)]
    BALLS[i][0] = x
    BALLS[i][1] = y
    BALLS[i][2] = r
    BALLS[i][3] = color
    circle(screen, color, (x, y), r)

def click(event):
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
A = []
n = 0

D = [0] * N
for i in range(N):
    D[i] = [1, 1]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(N):
                A = pygame.mouse.get_pos()
                x1 = A[0]
                y1 = A[1]
                if ((x1-BALLS[i][0])**2 + (y1-BALLS[i][1])**2)**0.5 <= BALLS[i][2]:
                    print(')))')
                    n += 1
                else:
                    print('(((')
    for i in range(N):
        BALLS[i][0] += D[i][0]
        BALLS[i][1] += D[i][1]

        circle(screen, BALLS[i][3], (BALLS[i][0], BALLS[i][1]), BALLS[i][2])
        if BALLS[i][0] >= a - BALLS[i][2] or BALLS[i][0] < BALLS[i][2]:
            D[i][0] *= -1
        if BALLS[i][1] >= b - BALLS[i][2] or BALLS[i][1] < BALLS[i][2]:
            D[i][1] *= -1
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
print('Количество очков:', n)