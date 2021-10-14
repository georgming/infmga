import turtle as tl
tl.speed(10)
tl.goto(500, 0), tl.goto(-500, 0)
Vx = 5
Vy = 60
ay = -10
dt = 0.01

x = -500
y = 0
for i in range(1000):
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    if y + y + Vy * dt + ay * dt ** 2 / 2 <= 0:
        Vy *= -1
    tl.goto(x, y)

tl.mainloop()