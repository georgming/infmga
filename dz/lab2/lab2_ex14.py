#Lab2_Ex14
import  turtle as tl

def star(n):
    for _ in range(n):
        tl.lt(180 - 180 / n)
        tl.fd(200)
star(5)
#star(11)
tl.mainloop()