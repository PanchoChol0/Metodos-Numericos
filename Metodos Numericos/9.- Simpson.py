import numpy as np
import matplotlib.pyplot as plt
import math

# Definir la función
def f(x):
    return x + math.cos(x)

# Pedir al usuario los valores de a y b
a = float(input("Inserte el valor de a: "))
b = float(input("Inserte el valor de b: "))

# Calcular la integral con la regla de Simpson 1/3
h_13 = (b - a) / 2
I_13 = (1/3) * h_13 * (f(a) + 4 * f((a + b) / 2) + f(b))
print("\nREGLA DE SIMPSON 1/3")
print("La raíz es: ",I_13)

# Calcular la integral con la regla de Simpson 3/8
h_38 = (b - a) / 3
I_38 = (3/8) * h_38 * (f(a) + 3 * f(a + h_38) + 3 * f(a + 2 * h_38) + f(b))
print("\nREGLA DE SIMPSON 3/8")
print("La raíz es: ",I_38)

# Crear puntos para la gráfica
x_values = np.linspace(a, b, 100)
y_values = [f(x) for x in x_values]

# Graficar la función
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label='Función f(x)')

# Graficar las áreas aproximadas por las reglas de Simpson
x_simpson_13 = [a, (a + b) / 2, b]
y_simpson_13 = [f(x) for x in x_simpson_13]
plt.fill_between(x_simpson_13, y_simpson_13, step='mid', alpha=0.4, label='Simpson 1/3')

x_simpson_38 = [a, a + h_38, a + 2 * h_38, b]
y_simpson_38 = [f(x) for x in x_simpson_38]
plt.fill_between(x_simpson_38, y_simpson_38, step='mid', alpha=0.4, color='orange', label='Simpson 3/8')

# Añadir título y leyenda al gráfico
plt.title('Gráfico de la función y las áreas aproximadas por Simpson 1/3 y 3/8')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()