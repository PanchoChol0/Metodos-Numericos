import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate
def f(x):
  return (math.sin(x - 3)) / (x - 1/2)
  
a=float(input('Teclea el valor de a: '))
b=float(input('Teclea el valor de b: '))

it=int(input('Teclea el numero de iteraciones: '))

if(f(a)*f(b)<0):
  print("hay raiz")
  tabla=[["i","a", "b", "m", "f(a)", "f(b)", "f(m)","Er","Erp"]]
  mAnt = 0
  xval = np.linspace(a, b, 1000)
  yval = np.vectorize(f)(xval)
  valm = []
  valeR = []

  for i in range(1,it):
    m = b - (f(b)*(b-a)) / (f(b) - f(a))
    eR = abs(m - mAnt) / m
    eRp = abs(eR * 100)
    tabla.append([i,a,b,m,f(a),f(b),f(m),abs(eR),abs(eRp)])

    valm.append(m)
    valeR.append(eRp)

    mAnt = m

    if(f(a)*f(m)>0):
      a = m
    else:
      b = m

  print(tabulate(tabla))
  print(f"La raiz encontrada es: {m}")

  
  plt.plot(xval, yval, label = 'f(x)')

  plt.scatter(valm, np.vectorize(f)(valm), color = 'blue', label = 'Raices encontradas')

  plt.figure()
  plt.plot(range(1, it), valeR, label = 'Error Relativo Porcentual')

  plt.xlabel('Iteracion')
  plt.ylabel('Error Realtivo Porcentual')
  plt.title('Error en el Metodo de Falsa Posicion')
  plt.grid(True)
  plt.legend()
  plt.show()  

  df = pd.DataFrame(tabla)
  df.to_csv('Regla_falsa.csv', index=False)

else:
  print("no hay raiz") 