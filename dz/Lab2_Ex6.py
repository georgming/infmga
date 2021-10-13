#Ex5
import turtle as tl
n = 12
for _ in range(n):
    tl.lt(360 / n)
    tl.fd(100)
    tl.stamp()
    tl.bk(100)
tl.mainloop()