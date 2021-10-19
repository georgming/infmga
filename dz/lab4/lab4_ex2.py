#lab4_ex2 'Боевое задание'
import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 600))
sc.fill((255, 255, 255))

pi = math.pi
WHITE = (255, 255, 255)
GREEN = (147, 172, 167)
BLACK = (0, 0, 0)
GRONGE = (145, 124, 111)
BRONGE = (108, 93, 83)
CHAKU = (172, 157, 147)
FACI = (227, 219, 219)
GREY = (204, 204, 204)
ORANGE = (253, 106, 2)

#Вспомогательные функции
def spinel(A, f):
    B = []
    F = [[math.cos(f), -1 * math.sin(f)],
         [math.sin(f), math.cos(f)]]
    for i in range(len(A)):
        B.append([F[0][0] * A[i][0] + F[0][1] * A[i][1],
                  F[1][0] * A[i][0] + F[1][1] * A[i][1]])
    return(B)

def chertila(a, b, j):
    RECT = []
    for i in range(-a, a + 1):
        RECT.append([i, - b * (1 - i**2 / a**2)**0.5 + b])
    if j == 1:
        for i in range(-a, a + 1):
            RECT.append([i, b * (1 - i**2 / a**2)**0.5 + b])
    return(RECT)

def corrector(A, x, y):
    for i in range(len(A)):
        A[i][0] += x
        A[i][1] += y
    return(A)

def ellie(COLOUR, A):
    ellipse(sc, COLOUR, (A[0], A[1], A[2], A[3]))

#Основные функции
def IGLU(x, y, a, b):
    #300, 300
    #rect(sc, BLACK, (x, y, a, b), 1)

    polygon(sc, GREY, corrector(chertila(a // 2, b // 2, -1), x + a // 2, y))
    arc(sc, BLACK, [x, y, a, b], 0, pi, 5)

    for i in range(1, 5):
        line(sc, BLACK, [x + i * b//5, y + b//2],
                        [x + i * b//5, y + b//2 - b//8])

    for i in range(5):
        line(sc, BLACK, [x + i * b//5 + b//10, y + b//2 - b//8],
                        [x + i * b//5 + b//10, y + b//2 - 2 * b//8])

    for i in range(4):
        line(sc, BLACK, [x + i * b//5 + 2 * b//10, y + b//2 - 2 * b//8],
                        [x + i * b//5 + 2 * b//10, y + b//2 - 3 * b//8])

    line(sc, BLACK, [x + 3 * b // 10, y + b // 2 - 3 * b // 8],
         [x + 3 * b // 10, y + b // 2 - 4 * b // 9])

    line(sc, BLACK, [x + b // 5 + 3 * b // 10, y + b // 2 - 3 * b // 8],
         [x + b // 5 + 3 * b // 10, y + b // 2 - 4 * b // 8])

    line(sc, BLACK, [x + 2 * b // 5 + 3 * b // 10, y + b // 2 - 3 * b // 8],
         [x + 2 * b // 5 + 3 * b // 10, y + b // 2 - 4 * b // 9])

    line(sc, BLACK, [x, y + b//2],
                    [x + a, y + b//2])

    line(sc, BLACK, [x + a//30, y + b // 2 - b // 8],
                    [x + a//1.03, y + b // 2 - b // 8])

    line(sc, BLACK, [x + a//11.8, y + b // 2 - 2 * b // 8],
                    [x + a//1.08, y + b // 2 - 2 * b // 8])

    line(sc, BLACK, [x + a//5.2, y + b // 2 - 3 * b // 8],
                    [x + a//1.2, y + b // 2 - 3 * b // 8])

def FISH(x, y, a, b):

    #rect(sc, BLACK, (x, y, a, b), 1)
    #150, 200

    #FISH_LEG_<
    polygon(sc, ORANGE, corrector(spinel(chertila(a // 6, b // 25, 1), pi / 10),
                                  x + a // 1.3,
                                  y + b // 1.9))

    polygon(sc, ORANGE, corrector(spinel(chertila(a // 6, b // 25, 1), -pi / 1.5),
                                  x + a // 1.6,
                                  y + b // 1.5))

    #FISH_LEG_/
    polygon(sc, ORANGE, corrector(spinel(chertila(a // 6, b // 25, 1), pi / 9),
                                  x + a // 1.8,
                                  y + b // 3.5))

    #FISH_LEG_\
    polygon(sc, ORANGE, corrector(spinel(chertila(a // 6, b // 25, 1), pi / 2.7),
                                  x + a // 2.7,
                                  y + b // 2.2))

    #FISH_BODY
    polygon(sc, GREEN, corrector(spinel(chertila(a//3, b//12, 1), pi/4),
                                 x + a//2,
                                 y + b//3))

    circle(sc, BLACK, [x + a//4, y + b//3.8], a//30)

def CAT(x, y, a, b):

    #rect(sc, BLACK, (x, y, a, b), 1)

    CAT_BODY = [x + a // 4, y + b // 2.5, a // 2.3, b // 5]
    ellipse(sc, GREY, CAT_BODY)

    LEG = [a // 10, b // 23]

    CAT_LEG_1_1 = [x + a // 5.3, y + b // 2.2, 0]
    polygon(sc, GREY, corrector(spinel(chertila(LEG[0], LEG[1], 1), CAT_LEG_1_1[2]),
                                CAT_LEG_1_1[0],
                                CAT_LEG_1_1[1]))

    CAT_LEG_1_2 = [x + a // 4.2, y + b // 1.8, -pi / 10]
    polygon(sc, GREY, corrector(spinel(chertila(LEG[0], LEG[1], 1), CAT_LEG_1_2[2]),
                                CAT_LEG_1_2[0],
                                CAT_LEG_1_2[1]))

    CAT_LEG_2_1 = [x + a // 1.4, y + b // 2, pi / 10]
    polygon(sc, GREY, corrector(spinel(chertila(LEG[0], LEG[1], 1), CAT_LEG_2_1[2]),
                                CAT_LEG_2_1[0],
                                CAT_LEG_2_1[1]))

    CAT_LEG_2_2 = [x + a // 1.5, y + b // 1.7, pi / 4.8]
    polygon(sc, GREY, corrector(spinel(chertila(LEG[0], LEG[1], 1), CAT_LEG_2_2[2]),
                                CAT_LEG_2_2[0],
                                CAT_LEG_2_2[1]))

    FISH(x + a // 5.1, y + b // 4.4, 150 * a // 140 // 5, 200 * b // 70 // 5)

    CAT_TEETH = [[x + a // 3.03 - a // 20 - a // 60,    y + b // 3 + b // 22],
                 [x + a // 3.03 - a // 20 + a // 50,    y + b // 3 + b // 22],
                 [x + a // 3.03 - a // 20,              y + b // 3 + b // 22 + b // 15]]
    polygon(sc, WHITE, CAT_TEETH)
    polygon(sc, WHITE, corrector(CAT_TEETH, a // 40, b // 40))

    CAT_HEAD= [x + a//4, y + b//5, a//6, b//4]
    ellie(GREY, CAT_HEAD)

    CAT_TAIL = [x + a//1.35, y + b//2.5, pi / 1.2]
    polygon(sc, GREY, corrector(spinel(chertila(a//5, b//17, 1), CAT_TAIL[2]),
                                CAT_TAIL[0],
                                CAT_TAIL[1]))

    CAT_EYE_1 = [x + a//3.7, y + b//3.7, a//20, b//15]
    ellie(WHITE, CAT_EYE_1)

    CAT_PUPIL_1 = [x + a // 3.3, y + b // 3.69, a // 60, b // 20]
    ellie(BLACK, CAT_PUPIL_1)

    CAT_EYE_1 = [x + a // 3.1, y + b // 3.1, a // 20, b // 15]
    ellie(WHITE, CAT_EYE_1)

    CAT_PUPIL_2 = [x + a // 2.8, y + b // 3.05, a // 60, b // 20]
    ellie(BLACK, CAT_PUPIL_2)

    CAT_NOSE = [[x + a // 2.95 - a//23 - a//100,    y + b // 3.05 + b//22],
                [x + a // 2.95 - a//23 + a//100,    y + b // 3.05 + b//22],
                [x + a // 2.95 - a//23,             y + b // 3.05 + b//22 + b//60]]
    polygon(sc, BLACK, CAT_NOSE)

    CAT_EAR = [[x + a // 2.95 - a//28 - a//50,     y + b // 4.8 + b//22],
               [x + a // 2.95 - a//28 + a//30,     y + b // 4.8 + b//22],
               [x + a // 2.95 - a//28,              y + b // 4.8 + b//22 - b//10]]
    polygon(sc, GREY, CAT_EAR)
    polygon(sc, GREY, corrector(CAT_EAR, a//15, 0))

def HUMAN(x, y, a, b):

    #rect(sc, BLACK, (x, y, a, b), 1)

    #MAN_HANDS
    polygon(sc, GRONGE, corrector(spinel(chertila(a // 16, b // 8, 1), pi / 2),
                                x + a // 2.1,
                                y + b // 1.85))

    polygon(sc, GRONGE, corrector(spinel(chertila(a // 16, b // 8, 1), -pi / 2.5),
                                x + a // 1.9,
                                y + b // 1.95))

    line(sc, BLACK, [x + a//6.5,    y + b//4],
                    [x + a//6.5,    y + b//1.2])

    LEG_1_1_n = [x + a // 2 + a // 30,      y + b // 2 + b // 6, a // 8, b // 6]
    ellie(GRONGE, LEG_1_1_n)

    LEG_1_2_n = [x + a // 2 + a // 15,      y + b // 2 + b // 3.55, a // 5.5, b // 14]
    ellie(GRONGE, LEG_1_2_n)

    LEG_2_1_n = [x + a // 3.5 + a // 30,    y + b // 2 + b // 6, a // 8, b // 6]
    ellie(GRONGE, LEG_2_1_n)

    LEG_2_2_n = [x + a // 5.5 + a // 19,    y + b // 2 + b // 3.55, a // 5.5, b // 14]
    ellie(GRONGE, LEG_2_2_n)

    #MAN_BODY
    polygon(sc, GRONGE, corrector(chertila(int(a // 4), b // 3, -1),
                                x + a // 2,
                                y + b // 2.5))

    rect(sc, BRONGE, (x + a // 2.3,      y + b // 2,     a // 11,    b // 4.75))
    rect(sc, BRONGE, (x + a // 4,        y + b // 1.4,   a // 2,     b // 25))

    #MAN_HEAD
    A = [x + a//2 - a//2//2,            y + b//4,       a//2,       b//4]
    ellie(GREY, A)

    A = [x + a // 2 - a // 2.7 // 2,    y + b // 3.6,   a // 2.7,   b // 5]
    ellie(CHAKU, A)

    A = [x + a // 2 - a // 3.7 // 2,    y + b // 3.4,   a // 3.7,   b // 6]
    ellie(FACI, A)

    #MAN_FACE
    MAN_EYE_1_n = [a//2 - a//18,     b//2 - b//8,    a//2.2 - a//18,     b//2.1 - b//8]
    line(sc, BLACK, [x + MAN_EYE_1_n[0],     y + MAN_EYE_1_n[1]],     [x + MAN_EYE_1_n[2],     y + MAN_EYE_1_n[3]], 2)

    MAN_EYE_2_n = [a // 2 + a // 35, b // 2 - b // 8, a // 2.2 + a // 6.9, b // 2.1 - b // 8]
    line(sc, BLACK, [x + MAN_EYE_2_n[0],     y + MAN_EYE_2_n[1]],     [x + MAN_EYE_2_n[2],     y + MAN_EYE_2_n[3]], 2)

    MOUTH_n = [a//2.3, b//2.5]
    arc(sc, BLACK, (x + MOUTH_n[0],     y + MOUTH_n[1],     a//10,  b//20), 0, pi)

rect(sc, GREY, (0, 0, 600, 150))
IGLU(25, 150, 300, 300)
CAT(0, 400, 3 * 140, 3 * 70)
HUMAN(325, 25, 300, 465)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()