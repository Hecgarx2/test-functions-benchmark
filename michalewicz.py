import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la Michalewicz function
def michalewicz(x, y):
    a = np.sin(x) * np.sin((1 * x**2) / np.pi)**20
    b = np.sin(y) * np.sin((2 * y**2) / np.pi)**20
    return -1 * (a + b)

# Generar datos para graficar
x = np.linspace(0, np.pi, 50)
y = np.linspace(0, np.pi, 50)
X, Y = np.meshgrid(x, y)
Z = michalewicz(X, Y)

# Graficar la función
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configuraciones adicionales
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Michalewicz Function')

plt.show()