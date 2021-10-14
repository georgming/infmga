#lab4_ex1 "злой смайлик"
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
#лицо
circle(screen, (0,0,0), (200,200), 101)
circle(screen, (255,206,180), (200,200), 100)
#глаза
circle(screen, (0,0,0), (250,190), 21)
circle(screen, (0,0,0), (150,190), 21)
circle(screen, (255,255,255), (250,190), 20)
circle(screen, (255,255,255), (150,190), 20)
circle(screen, (0,0,0), (250,190), 3)
circle(screen, (0,0,0), (150,190), 5)
#рот и брови
rect(screen, (255, 0, 0), (150, 250, 100, 10))
line(screen,(0, 0, 0),[220,180],[280,150],10)
line(screen,(0, 0, 0),[120,130],[180, 180],20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
