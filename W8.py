# Write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.0, 4.0, 100)
g = x **2
h = x **3

plt.plot(x, g, 'g', label='raised to the power of two')
plt.xlabel('x')
plt.plot(x, h, 'r', label='raised to the power of three')
plt.ylabel('y')
plt.title('Squared X Cubed')
plt.legend()
plt.show()
