import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import pandas as pd

def f(x):
    return (math.sin(x - 3)) / (x - 1/2)

x_o = float(input("Inserte el valor de xo: "))
x_i = float(input("Inserta el valor de xi: "))
it = int(input("Iteraciones: "))

tabla = [["i", "xo", "xi", "f(xo)", "f(xi)", "ER", "ERP"]]
xi_ant=0

for i in range(1, it+1):
    ER = abs((x_i - xi_ant) / x_i)
    ERP = ER * 100
    xi_ant=x_i
    tabla.append([i, x_o, x_i, f(x_o), f(x_i), ER, ERP]) 
    x_i=x_i-(f(x_i)*(x_i-x_o)) / (f(x_i)-f(x_o))
    x_o=xi_ant
    
print(tabulate(tabla))
print(f"La raiz es: {x_i}")
print(f"El error es: {ERP}%")

x_val = np.linspace(x_i, 100)
y_val = np.vectorize(f)(x_val)

plt.plot(x_val, y_val, label="f(x)")
plt.scatter(x_i, np.vectorize(f)(x_i), color='green', label='Raices encontradas')

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Gráfica de f(x)")

plt.grid(True)
plt.legend()
plt.show()

df = pd.DataFrame(tabla)
df.to_csv('Secante.csv',index = False)