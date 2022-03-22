from random import randrange as rnd, choice, shuffle
from tkinter import *
import itertools, time, copy
import time

nr = 4
nc = 4
np = 4

m = 25

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

class Cell():
    def __init__(self):
        self.n = 0
        self.bomb = 0
        self.mode = 'closed'

class Layer():
    def __init__(self):
        self.n = 0

    def change(self, k):
        if self.n + k >= 0 and self.n + k <= np - 1:
            self.n += k

layer = Layer()

def new_game():
    layer.n = 0

    global a
    a = [[[Cell() for c in range(nc)] for r in range(nr)] for p in range(np)]
    bomb_count = 5
    while bomb_count > 0:
        r = rnd(nr)
        c = rnd(nc)
        p = rnd(np)
        if not a[r][c][p].bomb:
            a[r][c][p].bomb = 1
            bomb_count -= 1

    for r in range(nr):
        for c in range(nc):
            for p in range(np):
                k = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        for dp in [-1, 0, 1]:
                            rr = r + dr
                            cc = c + dc
                            pp = p + dp
                            if rr in range(nr) and cc in range(nc) and pp in range(np):
                                if a[rr][cc][pp].bomb:
                                    k += 1
                a[r][c][p].n = k
    paint()
    canv.create_text(m * (nr + 3), nc * m + 30, font=("Purisa", 12), text='layer:' + str(layer.n))



def paint():
    canv.delete(ALL)

    for r in range(nr):
        for c in range(nc):
            x = m + c * m
            y = m + r * m
            p = layer.n
            if a[r][c][p].mode == 'opened':
                if not a[r][c][p].bomb:
                    canv.create_rectangle(x, y, x + m, y + m, fill='white')
                    if a[r][c][p].n > 0:
                        canv.create_text(x + m // 2, y + m // 2, text=a[r][c][p].n)
                else:
                    canv.create_rectangle(x, y, x + m, y + m, fill='red')
                    canv.create_rectangle(m * (nr + 2), m * (nc + 1) + 20, m * (nr + 2) + 100, m * (nc + 1) + 50, fill='red')
                    canv.create_text((m * (nr + 2) + m * (nr + 2) + 100) // 2,
                                     (m * (nc + 1) + 20 + m * (nc + 1) + 50) // 2, font=("Purisa", 12), text='game over')
            elif a[r][c][p].mode == 'closed':
                canv.create_rectangle(x, y, x + m, y + m, fill='gray')
            elif a[r][c][p].mode == 'flag':
                canv.create_rectangle(x, y, x + m, y + m, fill='yellow')
                canv.create_text(x + m // 2, y + m // 2, text='*')


def cell_change(r, c, p, button):

    if a[r][c][p].mode == 'closed':
        if button == 1:
            time.sleep(0.001)
            a[r][c][p].mode = 'opened'
            if a[r][c][p].n == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        for dp in [-1, 0, 1]:
                            rr = r + dr
                            cc = c + dc
                            pp = p + dp
                            if rr in range(nr) and cc in range(nc) and pp in range(np):
                                paint()
                                canv.update()
                                cell_change(rr, cc, pp, 1)
        elif button == 3:
            a[r][c][p].mode = 'flag'
    elif a[r][c][p].mode == 'flag' and button == 3:
        a[r][c][p].mode = 'closed'


def click(event):
    p = layer.n
    r = (event.y - m) // m
    c = (event.x - m) // m
    if r in range(nr) and c in range(nc):
        cell_change(r, c, p, event.num)
    paint()
    canv.create_text(m * (nr + 3), nc * m + 30, font=("Purisa", 12), text='layer:' + str(layer.n))


new_game()


def task_up(event):
    layer.change(1)
    paint()
    canv.create_text(m * (nr + 3), nc * m + 30, font=("Purisa", 12), text='layer:' + str(layer.n))

button_up = Button(canv, width = 5, height = 1, font=("Purisa", 12), text = 'up')
button_up.focus()
button_up.place(x = (nr + 2)*m, y = m)
button_up.bind('<Button-1>', task_up)


def task_down(event):
    layer.change(-1)
    paint()
    canv.create_text(m * (nr + 3), nc * m + 30, font=("Purisa", 12), text='layer:' + str(layer.n))

button_down = Button(canv, width = 5, height = 1, font=("Purisa", 12), text = 'down')
button_down.focus()
button_down.place(x = (nr + 2)*m, y = m + 50)
button_down.bind('<Button-1>', task_down)


def task_newgame(event):
    new_game()

button_newgame = Button(canv, width = 10, height = 2, font=("Purisa", 15), text = 'new game')
button_newgame.focus()
button_newgame.place(x = (nr + 4)*m + 80, y = m)
button_newgame.bind('<Button-1>', task_newgame)


canv.bind('<1>', click)
canv.bind('<3>', click)
mainloop()