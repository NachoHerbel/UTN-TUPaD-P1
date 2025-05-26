# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.

# Defino la función que calcule la secuencia Fibonacci (serie matemática en la que cada número es la suma de los dos anteriores, comenzando con 0 y 1) teniendo en cuenta una posición dada.
def fibonacci_recursivo(posicion):
    if posicion == 0:       # Establezco los casos base para 0 y 1
        return 0
    elif posicion == 1:
        return 1
    else:
        # Teniendo en cuenta una posición dada sumo los números de las dos posiciones anteriores
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)

# Esta cláusula verifica si el script está siendo ejecutado directamente (en vez de importado como módulo).
if __name__=="__main__":
    # Programa principal
    print(fibonacci_recursivo(6))