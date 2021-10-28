#lab4_ex2 'Боевое задание'
import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

ZERO = (0, 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (147, 172, 167)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
GREEN = (26, 102, 42)

FPS = 30
sc = pygame.display.set_mode((800, 600))
sc.fill(PINK)

def SPIN_ELLIPSE(A, COLOUR, a, b, x, y, f):
    X = pygame.Surface((a, b), pygame.SRCALPHA)
    X.fill(ZERO)
    ellipse(X, COLOUR, (0, 0, a, b))
    X = rotate(X, f)
    A.blit(X, (x, y))

def SPIN_RECT(A, COLOUR, a, b, x, y, f):
    X = pygame.Surface((a, b), pygame.SRCALPHA)
    X.fill(COLOUR)
    X = rotate(X, f)
    A.blit(X, (x, y))

def VETKA(A, a, b, x, y, f):
    X = pygame.Surface((a / 2.5, b / 2.5), pygame.SRCALPHA)
    X.fill(ZERO)
    ellipse(X, GREEN, (0, 0, a, b), 2)
    X = rotate(X, f)
    A.blit(X, (x, y))

def C(x, a):
    a1 = 100
    x = a * x / a1
    return(x)

def BAMBUK(x, y, a ,b):
    BAMBUK = pygame.Surface((C(100, a), C(100, b)), pygame.SRCALPHA)
    BAMBUK.fill(ZERO)

    rect(BAMBUK, GREEN, (C(50 - 9 / 5, a), C(100 - 27, b), C(9, a), C(27, b)))
    rect(BAMBUK, GREEN, (C(50 - 9 / 5, a), C(43, b), C(9, a), C(27, b)))
    SPIN_RECT(BAMBUK, GREEN, C(6, a), C(20, b), C(50, a), C(20, b), -20)
    SPIN_RECT(BAMBUK, GREEN, C(5, a), C(20, b), C(58, a), C(1, b), -30)

    VETKA(BAMBUK, C(50, a), C(20, b), C(58, a), C(55, b), -20)
    VETKA(BAMBUK, C(90, a), C(20, b), C(55, a), C(35, b), 10)
    VETKA(BAMBUK, C(90, a), C(20, b), C(15, a), C(25, b), -40)
    VETKA(BAMBUK, C(50, a), C(20, b), C(26, a), C(55, b), -30)

    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(20, a), C(34, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(25, a), C(36, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(30, a), C(38, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(35, a), C(40, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(40, a), C(42, b), -100)

    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(35, a), C(65, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(30, a), C(65, b), -100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(25, a), C(65, b), -100)


    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(65, a), C(45, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(70, a), C(42, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(75, a), C(41, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(80, a), C(40, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(85, a), C(39, b), 100)

    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(75, a), C(65, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(70, a), C(65, b), 100)
    SPIN_ELLIPSE(BAMBUK, GREEN, C(13, a), C(3, b), C(65, a), C(65, b), 100)

    sc.blit(BAMBUK, (x, y))

def PANDA(x, y, a):
    PANDA = pygame.Surface((C(100, a), C(100, a)), pygame.SRCALPHA)
    PANDA.fill(ZERO)

    # LEG_2
    polygon(PANDA, BLACK, ([C(30 + 5, a), C(30, a)],
                           [C(25 + 5, a), C(35, a)],
                           [C(18 + 5, a), C(65, a)],
                           [C(25 + 5, a), C(70, a)],
                           [C(30 + 5, a), C(65, a)]))
    SPIN_ELLIPSE(PANDA, BLACK, C(30, a), C(10, a), C(18, a), C(35.5, a), 65)

    #HEAD
    SPIN_ELLIPSE(PANDA, WHITE, C(60, a), C(30, a), C(30, a), C(30, a), 0)
    SPIN_ELLIPSE(PANDA, WHITE,      C(13, a),    C(33, a),   C(25, a),   C(21, a),  0)
    SPIN_ELLIPSE(PANDA, WHITE,      C(13, a),    C(33, a),   C(27, a),   C(33, a),  -65)
    SPIN_ELLIPSE(PANDA, WHITE,      C(10, a),    C(25, a),   C(27, a),   C(14, a),  -75)
    SPIN_ELLIPSE(PANDA, WHITE,      C(10, a),    C(25, a),   C(45, a),   C(15, a),  25)
    SPIN_ELLIPSE(PANDA, WHITE,      C(20, a),    C(20, a),   C(30, a),   C(20, a),  25)

    ellipse(PANDA, BLACK, (C(38, a),    C(35, a),   C(10, a),   C(10, a)))
    ellipse(PANDA, BLACK, (C(25, a), C(33, a), C(7, a), C(10, a)))
    ellipse(PANDA, BLACK, (C(27, a), C(48, a), C(8, a), C(6, a)))

    #LEG_1
    polygon(PANDA, BLACK, ([C(60, a), C(30, a)],
                           [C(60, a), C(60, a)],
                           [C(49, a), C(75, a)],
                           [C(46, a), C(78, a)],
                           [C(39, a), C(69, a)]))
    ellipse(PANDA, BLACK, (C(35, a), C(67, a), C(14, a), C(13, a)))

    #LEG_3
    SPIN_ELLIPSE(PANDA, BLACK, C(35, a), C(12, a), C(56, a), C(42, a), 55)

    #EARS
    SPIN_ELLIPSE(PANDA, BLACK, C(18, a), C(8, a), C(22, a), C(10, a), 40)
    SPIN_ELLIPSE(PANDA, BLACK, C(18, a), C(8, a), C(48, a), C(15, a), -70)


    sc.blit(PANDA, (x, y))

BAMBUK(300, 0, 250, 250)
BAMBUK(180, 100, 170, 200)
BAMBUK(600, 0, 200, 250)
BAMBUK(0, 0, 250, 250)

PANDA(150, 380, 180)
PANDA(230, 200, 400)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()