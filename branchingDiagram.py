import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r_values = np.linspace(2.5, 4.0, 10000)  # Valores de r
iterations = 1000                        # Iteraciones totales
last = 100                               # Iteraciones que se grafican (para evitar transitorios)

# Inicializar el valor inicial
x = 1e-5 * np.ones_like(r_values)

# Iterar el mapa logístico
for i in range(iterations):
    x = r_values * x * (1 - x)
    if i >= (iterations - last):
        plt.plot(r_values, x, ',k', alpha=0.25)

plt.title("Diagrama de Bifurcación del Mapa Logístico")
plt.xlabel('r')
plt.ylabel('x')
plt.grid(True)
plt.show()
