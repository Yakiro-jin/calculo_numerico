from math import *

def metodo_trapecio(f, a, b, n):

    h = (b - a) / n  # Ancho de cada trapecio
    suma = 0.5 * (f(a) + f(b))  # Suma de los extremos

    for i in range(1, n):
        suma += f(a + i * h)  # Suma de los puntos intermedios

    integral = h * suma
    return integral

f = lambda x: e**x - 3*x**2 

# Parámetros del método del trapecio
a = 0  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo
n = 1000  # Número de trapecios

# Calcular la integral usando el método del trapecio
resultado = metodo_trapecio(f, a, b, n)

print(f"Aproximación de la integral definida usando el método del trapecio: {resultado}")