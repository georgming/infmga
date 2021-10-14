#Пострение графиков
#Задание 2
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5.01, 0.01)
plt.minorticks_on()
plt.grid()
plt.grid(which='minor')
y1 = x**2 - x - 6
plt.plot(x, y1, x, x - x)
plt.show()

#x = -2
#x = 3