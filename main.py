def f1(x, y):
    return 2*x**2 + 3*x*y - y**2
def f2(x, y):
    return x**2 - 4*x*y + 5*y**2
def f(x, y):
    return f1(x, y) + f2(x, y)

def contrainst1(x, y):
    return 2*(x+y)-100
def contrainst2(x, y):
    return x*y-600
def contrainst3(x, y):
    return y-(x**2)/50-2

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X, Y)')
ax.set_title('Graphique de la fonction f')

plt.show()
