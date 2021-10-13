#Lab2_Ex12
import turtle as tl
def arc(x, k):
    d = 100
    for _ in range(k * d // 360):
        tl.fd(x)
        tl.lt(360 / d)
tl.lt(90)
for i in range(5):
    arc(2, 180)
    arc(0.5, 180)
tl.mainloop()