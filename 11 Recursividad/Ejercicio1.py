# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

# Solicito al usuario que ingrese un número para calcular su factorial
num_user = int(input("Por favor, ingrese un número entero positivo para calcular su factorial: "))

# Importo la función del cálculo del factorial de un número "n"
from factorial_n import factorial_n

# Muestro por pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
print(f"Factoriales desde 1 hasta {num_user}:")
for i in range(1, num_user + 1):
    print(f"Factorial de {i}: {factorial_n(i)}")