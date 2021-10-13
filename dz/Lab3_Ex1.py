import turtle as tl
a = 30

def draw(X):
    M = [[0, 0],        [a, 0],                     #   0   1
         [0, -a],       [a, -a],                    #   2   3
         [0, -2 * a],   [a, -2 * a]]                #   4   5
    x0 = tl.xcor()
    y0 = tl.ycor()
    for i in range(len(X)):
        if X[i] >= 0:
            tl.goto(x0 + M[X[i]][0], y0 + M[X[i]][1])
        else:
            tl.up(), tl.goto(x0 + M[-1 * X[i]][0], y0 + M[-1 * X[i]][1]), tl.pd()

zero = [0, 4, 5, 1, 0, -1]
one = [-2, 1, 5, -1]
two = [0, 1, 3, 4, 5, -1]
three = [1, 2, 3, 4, -1]
four = [0, 2, 3, 5, 1]
five = [-4, 5, 3, 2, 0, 1]
six = [-2, 3, 5, 4, 2, -1]
seven = [0, 1, 2, 4, -1]
eight = [-3, 2, 0, 1, 3, 5, 4, 2, -1]
nine = [-4, 3, 1, 0, 2, 3, -1]

print('Введите комбинацию из цифр')
s = input()
A = []
D = [zero, one, two, three, four, five, six, seven, eight, nine]
W = [i for i in range(10)]

try:
    for i in s:
        if int(i) in W:
            A.append(D[int(i)])
except ValueError:
        print('Некорректные символы в строке')

for i in range(len(A)):
    draw(A[i])
    tl.penup(), tl.fd(10), tl.pendown()

tl.mainloop()