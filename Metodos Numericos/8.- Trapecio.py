import numpy as np
import cmath

def f(x):
    return x + cmath.cos(x)

def metodo_trapecio(f, a, b, n):
    h = (b - a) / n
    suma = (f(a) + f(b)) / 2
    for i in range(1, n):
        suma += f(a + i * h)
    return suma * h

a = float(input("Ingrese el límite inferior del intervalo de integración (a): "))
b = float(input("Ingrese el límite superior del intervalo de integración (b): "))
n = int(input("Ingrese el número de trapecios (n): "))

integral_aproximada = metodo_trapecio(f, a, b, n)

print(f"La integral aproximada de f(x) en el intervalo [{a}, {b}] usando {n} trapecios es: {integral_aproximada}")