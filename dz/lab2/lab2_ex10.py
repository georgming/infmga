#Lab2_Ex10
import turtle as tl
def circle(x):
    d = 100
    for _ in range(d):
        tl.fd(x)
        tl.lt(360 / d)
n = 6
for i in range(n):
    circle(5)
    tl.lt(360 / n)
tl.mainloop()
