#Lab2_Ex13
import turtle as tl
def arc(x, k):
    d = 100
    for _ in range(k * d // 360):
        tl.fd(x)
        tl.lt(360 / d)

def draw(x, y, b, a, color):
    tl.goto(x, y)
    tl.pendown()
    tl.color(color)
    tl.begin_fill()
    arc(b, a)
    tl.end_fill()
    tl.penup()

draw(0, 0, 10, 360, 'yellow')
draw(100, 150, 2, 360, 'blue')
draw(-100, 150, 2, 360, 'blue')
tl.pensize(5)
tl.rt(90)
draw(0, 180, 70, 4, 'black')
draw(-80, 100, 5, 179, 'red')

tl.mainloop()