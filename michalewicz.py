import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la Michalewicz function
def michalewicz(x, y):
    return -1 * ( (np.sin(X) * np.sin((1 * X**2) / np.pi)**20) + 
           (np.sin(Y) * np.sin((2 * Y**2) / np.pi)**20) )

# Generar datos para graficar
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
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