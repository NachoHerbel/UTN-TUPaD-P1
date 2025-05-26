# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# Defino la función
def contar_bloques(n):
    if n == 1:          # Establezco el caso base cuando llego al último nivel con un solo bloque
        return 1
    return n + contar_bloques(n - 1)    # Sumo la cantidad de bloques del primer nivel y llamo recursivamente al siguiente nivel con un bloque menos

# Verificación de la función
print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))