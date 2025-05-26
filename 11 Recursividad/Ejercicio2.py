# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Solicito al usuario que ingrese un número para calcular la serie Fibonacci
pos_user = int(input("Por favor, ingrese una posición de la serie Fibonacci: "))

# Importo la función del cálculo del valor de la serie Fibonacci
from serie_fibonacci import fibonacci_recursivo

# Muestro por pantalla la serie completa de Fibonacci hasta la posición que especificó el usuario
print("La serie de Fibonacci hasta la posicion indicada es:")
for i in range(pos_user + 1):
    print(f"Posición {i}: {fibonacci_recursivo(i)}")