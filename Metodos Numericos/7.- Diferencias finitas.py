import numpy as np
import math
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt

############################ PROGRESIVA ##################################

def diferencia_progresiva(f, x, h):
    return (f(x + h) - f(x)) / h

def segunda_derivada_progresiva(f, x, h):
    return (f(x + 2*h) - 2 * f(x + h) + f(x)) / h**2

def tercera_derivada_progresiva(f, x, h):
    return (f(x + 3*h) - 3 * f(x + 2*h) + 3 * f(x + h) - f(x)) / h**3

def cuarta_derivada_progresiva(f, x, h):
    return (f(x + 4*h) - 4 * f(x + 3*h) + 6 * f(x + 2*h) - 4 * f(x + h) + f(x)) / h**4

############################ REGRESIVA ##################################

def diferencia_regresiva(f, x, h):
    return (f(x) - f(x - h)) / h

def segunda_derivada_regresiva(f, x, h):
    return (f(x) - 2 * f(x - h) + f(x - 2*h)) / h**2

def tercera_derivada_regresiva(f, x, h):
    return (f(x) - 3 * f(x - h) + 3 * f(x - 2*h) - f(x - 3*h)) / h**3

def cuarta_derivada_regresiva(f, x, h):
    return (f(x) - 4 * f(x - h) + 6 * f(x - 2*h) - 4 * f(x - 3*h) + f(x - 4*h)) / h**4

############################ CENTRADA ##################################

def diferencia_centrada(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def segunda_derivada_centrada(f, x, h):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

def tercera_derivada_centrada(f, x, h):
    return (f(x + 2*h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2*h)) / (2 * h**3)

def cuarta_derivada_centrada(f, x, h):
    return (f(x + 2*h) - 4 * f(x + h) + 6 * f(x) - 4 * f(x - h) + f(x - 2*h)) / h**4


f = lambda x: x-math.e**-x
x = float(input("Dame el valor de x: "))
h = float(input("Dame el valor de h: "))

############################ PRIMERA DERIVADA ###########################
df_progresiva = diferencia_progresiva(f, x, h)
df_regresiva = diferencia_regresiva(f, x, h)
df_centrada = diferencia_centrada(f, x, h)
############################ SEGUNDA DERIVADA ###########################
d2fp = segunda_derivada_progresiva(f, x, h)
d2fr = segunda_derivada_regresiva(f, x, h)
d2fc = segunda_derivada_centrada(f, x, h)
############################ TERCERA DERIVADA ###########################
d3fp = tercera_derivada_progresiva(f, x, h)
d3fr = tercera_derivada_regresiva(f, x, h)
d3fc = tercera_derivada_centrada(f, x, h)
############################ CUARTA DERIVADA ############################
d4fp = cuarta_derivada_progresiva(f, x, h)
d4fr = cuarta_derivada_regresiva(f, x, h)
d4fc = cuarta_derivada_centrada(f, x, h)

headers = ["Tipo", "Primera derivada", "Segunda derivada", "Tercera derivada", "Cuarta derivada"]

filas = [
    {"Tipo": "Progresiva", "Primera Derivada": df_progresiva, "Segunda Derivada": d2fp, "Tercera Derivada": d3fp, "Cuarta Derivada": d4fp},
    {"Tipo": "Regresiva", "Primera Derivada": df_regresiva, "Segunda Derivada": d2fr, "Tercera Derivada": d3fr, "Cuarta Derivada": d4fr},
    {"Tipo": "Centrada", "Primera Derivada": df_centrada, "Segunda Derivada": d2fc, "Tercera Derivada": d3fc, "Cuarta Derivada": d4fc}
]

tabla = [[row["Tipo"], row["Primera Derivada"], row["Segunda Derivada"], row["Tercera Derivada"], row["Cuarta Derivada"]] for row in filas]

print(tabulate(tabla, headers=headers))

x_values = np.linspace(x - 10*h, x + 10*h, 400)

y_values = [f(val) for val in x_values]

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label='Función f(x)')

y_prime_values = [(f(val + h) - f(val - h)) / (2 * h) for val in x_values]
plt.plot(x_values, y_prime_values, label='Primera derivada f\'(x)', linestyle='--')

y_double_prime_values = [segunda_derivada_centrada(f, val, h) for val in x_values]
plt.plot(x_values, y_double_prime_values, label='Segunda derivada f\'\'(x)', linestyle='--')

y_triple_prime_values = [tercera_derivada_centrada(f, val, h) for val in x_values]
plt.plot(x_values, y_triple_prime_values, label='Tercera derivada f\'\'\'(x)', linestyle='--')

y_quad_prime_values = [cuarta_derivada_centrada(f, val, h) for val in x_values]
plt.plot(x_values, y_quad_prime_values, label='Cuarta derivada f\'\'\'\'(x)', linestyle='--')

plt.title('Gráfico de la función y sus derivadas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

df = pd.DataFrame(tabla)
df.to_csv("Funciones finitas.csv", index = False)