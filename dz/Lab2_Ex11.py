#Lab2_Ex11
import turtle as tl
def circle(x, j):
    d = 50
    for _ in range(d):
        tl.fd(x)
        tl.lt(360 * j / d)
tl.lt(90)
a = 5
for i in range(10):
    circle(a, 1)
    circle(a, -1)
    a += 1
tl.mainloop()