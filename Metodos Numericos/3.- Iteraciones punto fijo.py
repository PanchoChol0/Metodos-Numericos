import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

def f(x):
  return math.sin(x)
def g(x):
  return math.sin(x)+x

x = float(input("Inserta el valor de x: "))
it=int(input("Iteraciones: "))
xAnt = 0
tabla = [["i","x","f(x)","g(x)","ER","ERP"]]

valeR = []

for i in range(1,it):
  eR = abs((x - xAnt)/ x)
  eRp = abs(eR * 100)
  tabla.append([i,x,f(x),g(x),eR,eRp])
  xAnt = x
  x = g(x)

  valeR.append(eRp)

print(tabulate(tabla))
print(f"La raiz mas cercana es: {x}")
print(f"Con un error de: {eRp}%")

xVal = np.linspace(x, 100)
yVal = np.vectorize(f)(xVal)

plt.plot(xVal, yVal, label="f(x)")

plt.scatter(x, np.vectorize(f)(x), color = 'blue', label = 'Raices encontradas')

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Gráfico de f(x)")

plt.grid(True)
plt.legend()
plt.show()

df = pd.DataFrame(tabla)
df.to_csv('Punto_fijo.csv',index=False)

