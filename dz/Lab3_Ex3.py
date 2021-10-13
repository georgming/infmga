import turtle as tl
from random import *
tl.speed(10)
for _ in range(1000):
    tl.fd(randint(1, 50))
    tl.rt(randint(0, 359))
tl.mainloop()