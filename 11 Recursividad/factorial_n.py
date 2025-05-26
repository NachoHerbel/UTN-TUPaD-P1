# Crea una función recursiva que calcule el factorial de un número.

# Defino una función que calcule el factorial de un número
def factorial_n(num):
    if num == 0:        # Establezco el caso base
        return  1
    else:
        return num * factorial_n(num-1)

# Esta cláusula verifica si el script está siendo ejecutado directamente (en vez de importado como módulo).
if __name__=="__main__":
    # Programa principal
    print (factorial_n(5))