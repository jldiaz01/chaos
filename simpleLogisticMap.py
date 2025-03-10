import numpy as np
import matplotlib.pyplot as plt

# Parámetros
r = 3.7                # Prueba con valores entre 2.5 y 4.0
x0 = 0.5               # Condición inicial
n = 100                # Número de iteraciones

# Inicializar el arreglo
x = np.zeros(n)
x[0] = x0

# Iterar el mapa logístico
for i in range(1, n):
    x[i] = r * x[i-1] * (1 - x[i-1])

# Graficar la evolución
plt.figure(figsize=(10, 6))
plt.plot(range(n), x, 'bo-', markersize=4)
plt.title(f'Mapa Logístico: r = {r}, x₀ = {x0}')
plt.xlabel('Iteraciones')
plt.ylabel('x')
plt.grid(True)
plt.show()
