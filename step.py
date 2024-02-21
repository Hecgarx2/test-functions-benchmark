import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la step function
def step(x, y):
    return ((np.floor(x + 0.5))**2) + ((np.floor(y + 0.5))**2)

# Generar datos para graficar
x = np.linspace(-5.12, 5.12, 50)
y = np.linspace(-5.12, 5.12, 50)  
X, Y = np.meshgrid(x, y)
Z = step(X, Y)

# Graficar la función
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configuraciones adicionales
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Step Function')

plt.show()