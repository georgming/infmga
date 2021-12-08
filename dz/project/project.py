import pygame
from pygame.draw import *
from random import randint
pygame.init()

screen_lenght = 1000
screen_width = 600
FPS = 60
screen = pygame.display.set_mode((screen_lenght, screen_width))

class ball:
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
    COLOR = 0
    x_0 = 0
    y_0 = 0
    r_0 = 0

    def __init__(self, color, x, y, r, dx, dy):
        self.COLOR = self.COLORS[color]
        self.x_0 = x
        self.y_0 = y
        self.r_0 = r
        self.dv = [0, 0]
        self.dv[0] = dx
        self.dv[1] = dy
        self.click_number = 0
    def draw(self):
        circle(screen, self.COLOR, (self.x_0, self.y_0), self.r_0)
        self.x_0 += self.dv[0]
        self.y_0 += self.dv[1]
        if self.x_0 >= screen_lenght - self.r_0 or self.x_0 <= self.r_0:
            self.dv[0] *= -1
        if self.y_0 >= screen_width - self.r_0 or self.y_0 <= self.r_0:
            self.dv[1] *= -1
score = 0
level_number = 0

font = pygame.font.Font(None, 50)
text = font.render("Score: ", True, (255, 255, 255))
text2 = font.render(str(score), True, (255, 255, 255))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
ball_1 = ball(randint(0, 5), randint(150, screen_lenght - 150), randint(100, screen_width - 100), 50, 5, 5)
ball_2 = ball(randint(0, 5), randint(150, screen_lenght - 150), randint(100, screen_width - 100), 50, 10, 10)
ball_3 = ball(randint(0, 5), randint(150, screen_lenght - 150), randint(100, screen_width - 100), 40, 5, 5)
ball_4 = ball(randint(0, 5), randint(150, screen_lenght - 150), randint(100, screen_width - 100), 20, 5, 5)
ball_5 = ball(randint(0, 5), randint(150, screen_lenght - 150), randint(100, screen_width - 100), 10, 5, 5)
balls = (ball_1, ball_2, ball_3, ball_4, ball_5)
def click(event):
    click_x_y = event.pos
    global score, level_number, sublevel_number
    for i in range(len(balls)):
        if (balls[i].x_0 - balls[i].r_0 < click_x_y[0] < balls[i].x_0 + balls[i].r_0) and (balls[i].y_0 - balls[i].r_0 < click_x_y[1] < balls[i].y_0 + balls[i].r_0):
            score += 1
            level_number += 1
            balls[i].click_number += 1
    print(score)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    if level_number == 0:
        balls[0].draw()
    if 1 <= level_number <= 2:
        if balls[1].click_number == 0 and balls[2].click_number ==0:
            balls[1].draw()
            balls[2].draw()
        if balls[1].click_number == 1 and balls[2].click_number ==0:
            balls[2].draw()
        if balls[1].click_number == 0 and balls[2].click_number ==1:
            balls[1].draw()

    text = font.render("Score: ", True, (255, 255, 255))
    text2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, [20, 10])
    screen.blit(text2, [135, 10])
    pygame.display.update()
    screen.fill((0, 0, 0))
pygame.quit()