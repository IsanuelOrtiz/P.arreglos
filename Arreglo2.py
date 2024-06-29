import operator
import functools
Numeros = [15, 83, 29, 374, 7, 58, 923, 32]

# Ordenar la lista
Numeros_ordenados = sorted(Numeros)

# Encontrar el segundo menor y el segundo mayor
segundo_menor = Numeros_ordenados[1]
segundo_mayor = Numeros_ordenados[-2]

# Calcular el mínimo, máximo y la suma de todos los números
Resultado = functools.reduce(operator.mul,Numeros)

print(f"El segundo número más bajo es {segundo_menor} y el segundo número más alto es {segundo_mayor}")
print("El resultado de multiplicar todos los elementos de la lista es:", Resultado)
