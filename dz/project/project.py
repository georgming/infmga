import pygame
from pygame.draw import *
from random import randint
pygame.init()

screen_lenght = 500
screen_width = 500

FPS = 60
screen = pygame.display.set_mode((screen_lenght, screen_width))

font = pygame.font.Font(None, 50)
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
    ty = 0
    start = 100
    a = 1

    def __init__(self, color, x, y, r, dx, dy):
        self.COLOR = self.COLORS[color]
        self.x_0 = x
        self.y_0 = y
        self.r_0 = r
        self.dv = [0, 0]
        self.dv[0] = dx
        self.dv[1] = dy
        self.start = self.y_0
        self.isClicked = False

    def draw(self, mode):
        if mode == 0:
            if self.isClicked == False:
                circle(screen, self.COLOR, (self.x_0, self.y_0), self.r_0)
                if 0 <= self.y_0 <= 8 * screen_width / 9:
                    self.x_0 += self.a * self.dv[0]
                    self.ty += abs(self.dv[0])
                    self.y_0 = self.start - self.dv[1] * self.ty + ((self.ty) ** 2) / 500
                    if 115 * screen_lenght / 120 <= self.x_0 or self.x_0 <= self.r_0:
                        self.a = -self.a
                else:
                    self.ty = 0
                    self.start = 8 * screen_width / 9
                    self.y_0 = self.start - self.dv[1] * self.ty + ((self.ty) ** 2) / 500
                    if self.dv[1] == 0:
                        self.dv[1] = 2.4
                    self.dv[1] = self.dv[1] / 1.2

        if mode == 1:
            if self.isClicked == False:
                circle(screen, self.COLOR, (self.x_0, self.y_0), self.r_0)
                self.x_0 += self.dv[0]
                self.y_0 += self.dv[1]
                if self.x_0 >= screen_lenght - 1 - self.r_0 or self.x_0 <= self.r_0:
                    self.dv[0] *= -1
                if self.y_0 >= screen_width - 1 - self.r_0 or self.y_0 <= self.r_0:
                    self.dv[1] *= -1

score = 0
draw_mode = 1
level = 0

pygame.display.update()
clock = pygame.time.Clock()
finished = False
ball_1 = ball(randint(0, 5), randint(200, screen_lenght - 200), randint(100, screen_width), 50, 5, 5)

balls = [ball_1]
def click(event):
    click_x_y = event.pos
    global score, level, balls, ball_1
    for i in range(len(balls)):
        if (balls[i].x_0 - balls[i].r_0 < click_x_y[0] < balls[i].x_0 + balls[i].r_0) and (
                balls[i].y_0 - balls[i].r_0 < click_x_y[1] < balls[i].y_0 + balls[i].r_0) and (
                balls[i].isClicked == False):
            if score >= 19:
                balls[i].r_0 = balls[i].r_0 - 10
                score += 1
                if balls[i] == 10:
                    del balls[i]
            else:
                balls[i].isClicked = True
                del balls[i]
                score += 1
                break

    if score == 1 and balls == []:
        level += 1
        d_l = 10 * screen_lenght // 12
        d_w = 8 * screen_width // 9
        ball_1 = ball(randint(0, 5), randint(screen_lenght - d_l, d_l), randint(200, d_w), 50, 10, 10)
        ball_2 = ball(randint(0, 5), randint(screen_lenght - d_l, d_l), randint(200, d_w), 40, 5, 5)
        balls = [ball_1, ball_2]
    if score == 3 and balls == []:
        level += 1
        d_l = 10 * screen_lenght // 12
        d_w = 8 * screen_width // 9
        ball_1 = ball(randint(0, 5), randint(screen_lenght - d_l, d_l), randint(200, d_w), 30, 5, 5)
        ball_2 = ball(randint(0, 5), randint(screen_lenght - d_l, d_l), randint(200, d_w), 20, 5, 5)
        ball_3 = ball(randint(0, 5), randint(screen_lenght - d_l, d_l), randint(200, d_w), 10, 5, 5)
        balls = [ball_1, ball_2, ball_3]
    if score == 6 and balls == []:
        level += 1
        ball_1 = ball(randint(0, 5), randint(200, screen_lenght - 200), randint(200, screen_width - 100), 40, 0, 20)
        ball_2 = ball(randint(0, 5), randint(200, screen_lenght - 200), randint(200, screen_width - 100), 40, 20, 0)
        ball_3 = ball(randint(0, 5), randint(200, screen_lenght - 200), randint(200, screen_width - 100), 40, 20, 20)
        balls = [ball_1, ball_2, ball_3]
    if score == 9 and balls == []:
        level += 1
        d_l = screen_lenght // 12
        d_w = screen_width // 12
        ball_1 = ball(randint(0, 5), 1 * d_l, 1 * d_w, 30, 7, 0)
        ball_2 = ball(randint(0, 5), 2 * d_l, 2 * d_w, 30, 7, 0)
        ball_3 = ball(randint(0, 5), 3 * d_l, 3 * d_w, 30, 7, 0)
        ball_4 = ball(randint(0, 5), 4 * d_l, 4 * d_w, 30, 7, 0)
        ball_5 = ball(randint(0, 5), 5 * d_l, 5 * d_w, 30, 7, 0)
        ball_6 = ball(randint(0, 5), 7 * d_l, 5 * d_w, 30, -7, 0)
        ball_7 = ball(randint(0, 5), 8 * d_l, 4 * d_w, 30, -7, 0)
        ball_8 = ball(randint(0, 5), 9 * d_l, 3 * d_w, 30, -7, 0)
        ball_9 = ball(randint(0, 5), 10 * d_l, 2 * d_w, 30, -7, 0)
        ball_10 = ball(randint(0, 5), 11 * d_l, 1 * d_w, 30, -7, 0)
        balls = [ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, ball_7, ball_8, ball_9, ball_10]
    if score == 19 and balls == []:
        level += 1
        ball_1 = ball(randint(0, 5), randint(200, screen_lenght - 200), randint(200, screen_width - 100), 100, 5, 5)
        balls = [ball_1,]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    if score == 9:
        draw_mode = 0
    if score == 19:
        draw_mode = 1
    for j in range(len(balls)):
        balls[j].draw(draw_mode)

    text = font.render("Score: ", True, (255, 255, 255))
    text2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(text, [20, 20])
    screen.blit(text2, [140, 20])

    text = font.render("Level: ", True, (255, 255, 255))

    if 29 <= score:
        win = font.render('You WIN!', True, (255, 255, 255))
        screen.blit(win, [screen_lenght / 4, screen_width / 2])

    level_txt = font.render(str(level), True, (255, 255, 255))
    screen.blit(text, [screen_lenght / 30, screen_width / 10])
    screen.blit(level_txt, [screen_lenght / 4, screen_width / 10])


    pygame.display.update()
    screen.fill((0, 0, 0))
pygame.quit()