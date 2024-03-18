import cmath
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

def f(x):
    return (x / 2)**2 - x

def muller_method(f, x0, x1, x2, max_iter):
    results = [["Iteración", "x3", "f(x3)", "Error Relativo", "Error Porcentual"]]
    for i in range(3,max_iter+1):
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0)) / h0
        d1 = (f(x2) - f(x1)) / h1
        a = (d1 - d0) / (h1 + h0)
        b = d1 + h1 * a
        c = f(x2)
        sr = cmath.sqrt(b**2 - 4 * c * a)
        denom = b + sr if abs(b - sr) < abs(b + sr) else b - sr
        numer = -2 * c / denom
        x3 = x2 + numer
        eR = abs(numer) / abs(x3)
        eRp = eR * 100
        results.append([i, x3, f(x3), eR, eRp])
        x0, x1, x2 = x1, x2, x3
    return results, x3

x0 = float(input("Inserte el valor de x0: "))
x1 = float(input("Inserte el valor de x1: "))
x2 = float(input("Inserte el valor de x2: "))
max_iter = int(input("Número máximo de iteraciones: "))

tabla = [["i", "x3", "f(x3)", "eR", "eRp"]]
table, x3 = muller_method(f, x0, x1, x2, max_iter)
print(tabulate(table))

print(f"La raíz es: {x3}")
print(f"El error relativo porcentual es: {table[-1][-1]}%")

df = pd.DataFrame(table[1:], columns=table[0])
df.to_csv('Muller.csv', index=False)

x_val = np.linspace(float(x3.real) - 5, float(x3.real) + 5, 400)
y_val = np.vectorize(lambda x: f(x).real)(x_val)

plt.plot(x_val, y_val, label="f(x)")
plt.scatter(x3.real, f(x3).real, color='turquoise', label='Raíz encontrada')

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Gráfica de f(x)")
plt.grid(True)

plt.legend()
plt.show()
