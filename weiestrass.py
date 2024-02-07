import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir la función de Weierstrass en dos dimensiones
def weierstrass_2d(x, y, a, b, terms):
    result = 0
    for n in range(terms):
        for m in range(terms):
            result += a**(n+m) * np.cos(b**n * np.pi * x) * np.cos(b**m * np.pi * y)
    return result

# Generar datos para graficar
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = weierstrass_2d(X, Y, a=0.5, b=0.5, terms=50)  # Ajusta los parámetros "a" y "b" según tus necesidades

# Graficar la función
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configuraciones adicionales
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Función de Weierstrass en 3D')

plt.show()