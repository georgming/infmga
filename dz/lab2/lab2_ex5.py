#Ex5
import turtle as tl
a = 50
x = 25
for j in range(10):
    tl.penup()
    tl.goto(tl.xcor() - x, tl.ycor() - x)
    tl.pendown()
    for i in range(4):
        tl.fd(a)
        tl.lt(90)
    a += x * 2
tl.mainloop()