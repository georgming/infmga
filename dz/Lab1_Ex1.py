#Пострение графиков
#Задание 1
import numpy as np
x = [1, 10, 1000]
for i in range(3):
    y = (np.exp(1 / (np.sin(x[i]) + 1)) / (5/4 + 1/x[i]**15)) / (1 + x[i]**2)
    print(y)