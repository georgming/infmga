#lab4_ex2 'Боевое задание'
import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 600))
sc.fill((255, 255, 255))

ZERO = (0, 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (147, 172, 167)
BLACK = (0, 0, 0)
GRONGE = (145, 124, 111)
BRONGE = (108, 93, 83)
CHAKU = (172, 157, 147)
FACI = (227, 219, 219)
GREY = (204, 204, 204)
ORANGE = (253, 106, 2)

def S(X_0, COLOUR, x, y, A, f):
    X = pygame.Surface((X_0[0], X_0[1]), pygame.SRCALPHA)
    X.fill(ZERO)
    ellipse(X, COLOUR, (0, 0, X_0[0], X_0[1]))
    X = rotate(X, f)
    A.blit(X, (x, y))

def MAN(x, y, k):
    #4:5
    a = 400 / k
    b = 500 / k

    MAN = pygame.Surface((a, b), pygame.SRCALPHA)
    MAN.fill(ZERO)

    MAN_HAND_1 = [a / 2, b / 8]
    MAN_HAND_2 = [a / 2, b / 8]
    ellipse(MAN, (GRONGE), (a / 2 - MAN_HAND_1[0] / 2 - a / 8, b / 2.1, MAN_HAND_1[0], MAN_HAND_1[1]))
    ellipse(MAN, (GRONGE), (a / 2 - MAN_HAND_2[0] / 2 + a / 8, b / 2.1, MAN_HAND_2[0], MAN_HAND_2[1]))

    MAN_LEG_1_1 = [a / 6, b / 3]
    MAN_LEG_1_2 = [a / 6, b / 13]
    MAN_LEG_2_1 = [a / 6, b / 3]
    MAN_LEG_2_2 = [a / 6, b / 13]
    ellipse(MAN, (GRONGE), (a / 2 - MAN_LEG_1_1[0] / 2 - a / 9, b / 1.6, MAN_LEG_1_1[0], MAN_LEG_1_1[1]))
    ellipse(MAN, (GRONGE), (a / 2 - MAN_LEG_1_2[0] / 2 - a / 6.7, b / 1.12, MAN_LEG_1_2[0], MAN_LEG_1_2[1]))
    ellipse(MAN, (GRONGE), (a / 2 - MAN_LEG_2_1[0] / 2 + a / 9, b / 1.6, MAN_LEG_2_1[0], MAN_LEG_2_1[1]))
    ellipse(MAN, (GRONGE), (a / 2 - MAN_LEG_2_2[0] / 2 + a / 6.7, b / 1.12, MAN_LEG_2_2[0], MAN_LEG_2_2[1]))

    MAN_HEAD_A1 = [a / 1.7, b / 3]
    ellipse(MAN, (GREY), (a / 2 - MAN_HEAD_A1[0] / 2, b / 7, MAN_HEAD_A1[0], MAN_HEAD_A1[1]))
    ellipse(MAN, (BRONGE), (a / 2 - MAN_HEAD_A1[0] / 2, b / 7, MAN_HEAD_A1[0], MAN_HEAD_A1[1]), 1)

    MAN_BODY_A = [a / 2.1, b / 2]
    MAN_BODY = pygame.Surface((MAN_BODY_A[0], MAN_BODY_A[1]), pygame.SRCALPHA)
    MAN_BODY.fill(ZERO)
    ellipse(MAN_BODY, GRONGE, (0, 0, MAN_BODY_A[0], 2 * MAN_BODY_A[1]))
    MAN.blit(MAN_BODY, (a / 2 - MAN_BODY_A[0]/2, b / 3.2))

    MAN_HEAD_A2 = [a / 2.2, b / 4]
    MAN_HEAD_A3 = [a / 3, b / 5]
    ellipse(MAN, (CHAKU), (a / 2 - MAN_HEAD_A2[0] / 2,    b / 5,     MAN_HEAD_A2[0], MAN_HEAD_A2[1]))
    ellipse(MAN, (FACI),   (a / 2 - MAN_HEAD_A3[0] / 2,    b / 4.4,     MAN_HEAD_A3[0], MAN_HEAD_A3[1]))

    rect(MAN, BRONGE, (a / 2 - a / 2.1 / 2, b / 1.4, a / 2.1, b / 10))
    rect(MAN, BRONGE, (a / 2 - a / 7.1 / 2, b / 2.2, a / 7.1, b / 3.9))
    line(MAN, BLACK, [a / 6, b / 2 - b / 3], [a / 6, b / 2 + b / 2.2])

    line(MAN, BLACK, [a / 2 - a / 30, b / 3],   [a / 2 - a / 25 - a / 15, b / 2 - b / 5])
    line(MAN, BLACK, [a / 2 + a / 30, b / 3],   [a / 2 + a / 25 + a / 15, b / 2 - b / 5])
    arc(MAN, BLACK,  (a / 2 - a / 8 / 2,    b / 2.7,    a / 8,    b / 20), 0, 3.14)

    sc.blit(MAN, (x, y))

def FISH(x, y, a, b, A):
    FISH = pygame.Surface((a, b), pygame.SRCALPHA)
    FISH.fill(ZERO)

    FISH_LEG_0 = [a / 2.5, b / 5.8]
    S(FISH_LEG_0, ORANGE, a / 5.5, b / 15, FISH, 25)
    S(FISH_LEG_0, ORANGE, a / 6, b / 3, FISH, -25)
    S(FISH_LEG_0, ORANGE, a / 1.7, b / 14.7, FISH, 25)
    S(FISH_LEG_0, ORANGE, a / 1.7, b / 3.3, FISH, -25)

    FISH_BODY_0 = [a / 1.5, b / 3.5]
    ellipse(FISH, GREEN, (a / 10, b / 3.5, FISH_BODY_0[0], FISH_BODY_0[1]))

    circle(FISH, BLACK, (a / 5, b / 2.3), b / 15)

    FISH = rotate(FISH, -25)
    A.blit(FISH, (x, y))

def CAT(x, y, k):
    #2:1
    a = 200 / k
    b = 100 / k

    CAT = pygame.Surface((a, b), pygame.SRCALPHA)
    CAT.fill(ZERO)

    CAT_LEG_0 = [a / 3, b / 8.5]
    S(CAT_LEG_0, GREY, a / 1.6, b / 2, CAT, -25)
    S(CAT_LEG_0, GREY, a / 1.8, b / 1.8, CAT, -30)
    S(CAT_LEG_0, GREY, a / 25, b / 1.75, CAT, 0)
    S(CAT_LEG_0, GREY, a / 10, b / 1.6, CAT, 15)

    CAT_BODY = [a / 2.1, b / 4]
    ellipse(CAT, GREY, (a/4, b/2, CAT_BODY[0], CAT_BODY[1]))

    CAT_EAR_0 = [a / 12, b / 5]
    CAT_EAR = pygame.Surface((CAT_EAR_0[0], CAT_EAR_0[1]), pygame.SRCALPHA)
    CAT_EAR.fill(ZERO)
    polygon(CAT_EAR, GREY, [[0,                    CAT_EAR_0[1]],
                             [CAT_EAR_0[0],         CAT_EAR_0[1]],
                             [CAT_EAR_0[0] / 2,     0]])
    CAT_EAR_1 = rotate(CAT_EAR, 10)
    CAT_EAR_2 = rotate(CAT_EAR, -5)
    CAT.blit(CAT_EAR_1, (a / 4, b / 5))
    CAT.blit(CAT_EAR_2, (a / 2.95, b / 4.6))

    FISH(a / 10, b / 3, a / 3, b / 3, CAT)

    CAT_TEETH_0 = [a / 30, b / 15]
    CAT_TEETH = pygame.Surface((CAT_TEETH_0[0], CAT_TEETH_0[1]), pygame.SRCALPHA)
    CAT_TEETH.fill(ZERO)
    polygon(CAT_TEETH, WHITE, [[0, 0],
                             [CAT_TEETH_0[0], 0],
                             [CAT_TEETH_0[0] / 2, CAT_TEETH_0[1]]])
    CAT_TEETH_1 = rotate(CAT_TEETH, -5)
    CAT_TEETH_2 = rotate(CAT_TEETH, -5)
    CAT.blit(CAT_TEETH_1, (a / 3.75, b / 1.92))
    CAT.blit(CAT_TEETH_2, (a / 3.25, b / 1.82))

    CAT_HEAD = [a / 5.8, b / 3.8]
    ellipse(CAT, GREY, (a / 4, b / 3, CAT_HEAD[0], CAT_HEAD[1]))

    circle(CAT, BLACK, (a / 3.4, b / 1.95), b / 60)

    CAT_TAIL_0 = [a / 2.2, b / 9]
    CAT_TAIL = pygame.Surface((CAT_TAIL_0[0], CAT_TAIL_0[1]), pygame.SRCALPHA)
    CAT_TAIL.fill(ZERO)
    ellipse(CAT_TAIL, GREY, (0, 0, CAT_TAIL_0[0], CAT_TAIL_0[1]))
    CAT_TAIL = rotate(CAT_TAIL, 25)
    CAT.blit(CAT_TAIL, (a / 1.8, b / 3.8))

    CAT_EYE = [a / 18, b / 12]
    CAT_PUPIL = [a / 50, b / 20]
    ellipse(CAT, WHITE, (a / 3.8, b / 2.6, CAT_EYE[0], CAT_EYE[1]))
    ellipse(CAT, WHITE, (a / 3, b / 2.4, CAT_EYE[0], CAT_EYE[1]))
    ellipse(CAT, BLACK, (a / 3.4, b / 2.55, CAT_PUPIL[0], CAT_PUPIL[1]))
    ellipse(CAT, BLACK, (a / 2.75, b / 2.35, CAT_PUPIL[0], CAT_PUPIL[1]))

    sc.blit(CAT, (x, y))

def IGLU(x, y, k):
    #2:1
    a = 200 / k
    b = 100 / k

    IGLU = pygame.Surface((a + 1, b + 1), pygame.SRCALPHA)
    IGLU.fill(ZERO)

    IGLU_BODY_0 = [a, b]
    IGLU_BODY = pygame.Surface((IGLU_BODY_0[0], IGLU_BODY_0[1]), pygame.SRCALPHA)
    IGLU_BODY.fill(ZERO)
    ellipse(IGLU_BODY, GREY, (0, 0, IGLU_BODY_0[0], 2 * IGLU_BODY_0[1]))
    ellipse(IGLU_BODY, BLACK, (0, 0, IGLU_BODY_0[0], 2 * IGLU_BODY_0[1]), 5)
    IGLU.blit(IGLU_BODY, (0, 0))

    for i in range(1, 5):
        line(IGLU, BLACK,   [i * a / 5, b], [i * a / 5, b - b / 4])

    for i in range(5):
        line(IGLU, BLACK,   [i * a / 5 + a / 10, b - b / 4], [i * a / 5 + a / 10, b - 2 * b / 4])

    for i in range(4):
        line(IGLU, BLACK,   [i * a / 5 + 2 * a / 10, b - 2 * b / 4], [i * a / 5 + 2 * a / 10, b - 3 * b / 4])

    line(IGLU, BLACK, [a / 2,           b / 4],     [a / 2,         0])
    line(IGLU, BLACK, [3 * a / 10,      b / 4],     [3 * a / 10,    b / 9])
    line(IGLU, BLACK, [7 * a / 10,      b / 4],     [7 * a / 10,    b / 9])
    #Горизонтальные линии. Записаны снизу вверх
    line(IGLU, BLACK, [0, 4 * b / 4], [a, 4 * b / 4])
    line(IGLU, BLACK, [a / 35, 3 * b / 4], [a - a / 35, 3 * b / 4])
    line(IGLU, BLACK, [a / 13, 2 * b / 4], [a - a / 13, 2 * b / 4])
    line(IGLU, BLACK, [a / 5.5, 1 * b / 4], [a - a / 5.5, 1 * b / 4])

    sc.blit(IGLU, (x, y))

rect(sc, GREY, (0, 0, 600, 200))
IGLU(20, 140, 0.65)
CAT(50, 400, 0.7)
MAN(350, 100, 1.7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()