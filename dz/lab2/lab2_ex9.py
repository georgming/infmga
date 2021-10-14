#Lab2_Ex9
import turtle as tl
import numpy as np

def polygon(n, l):
    for _ in range(n):
        tl.fd(l)
        tl.lt(360 / n)
    tl.rt(90 * (i + 2) / i)

a = 10
d = 10
for i in range(3, 100):
    tl.lt(90 * (i + 2) / i)
    polygon(i, a)
    tl.penup()
    tl.fd(d)
    tl.pendown()
    a = ((a / (2 * np.sin(np.pi / i))) + d) * 2 * np.sin(np.pi / (i + 1))
tl.mainloop()