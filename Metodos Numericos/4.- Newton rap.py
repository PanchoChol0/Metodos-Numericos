import math
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import pandas as pd

def f(x):
    return (x/4)**2 - 6

def f_p(x):
    return 1/8 * x

x = float(input("Introduce el valor de xi: "))
it = int(input("Introduce las iteraciones: "))
xAnt = 0
tabla = [["i","xi","f(xi)","f'(xi)","ER","ERP"]]                                                               
valeR = []

for i in range(1,it):
    eR = abs((x - xAnt) / x)
    eRp = abs(eR * 100)
    xim = x - (f(x)) / f_p(x) 
    tabla.append([i,x,f(x),f_p(x),eR,eRp])
    xAnt = x
    x = xim

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

plt.figure()
plt.plot(range(1,it),valeR, label = 'Error Relativo Porcentual')

plt.xlabel('Iteracion')
plt.ylabel('Error Relativo Porcentual')
plt.title('Error en el Metodo de Newton')

plt.grid(True)
plt.legend()
plt.show()

df = pd.DataFrame(tabla)
df.to_csv('NewtonR.csv',index=False)




