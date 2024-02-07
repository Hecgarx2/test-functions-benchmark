import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la Michalewicz function
def eggholder(x, y):
    a = np.sqrt(np.fabs(y + x/2 + 47))
    b = np.sqrt(np.fabs(x - (y+47)))
    return -(y+47) * np.sin(a)- y * np.sin(b)

# Generar datos para graficar
x = np.linspace(-512, 512, 50)
y = np.linspace(-512, 512, 50)
X, Y = np.meshgrid(x, y)
Z = eggholder(X, Y)

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