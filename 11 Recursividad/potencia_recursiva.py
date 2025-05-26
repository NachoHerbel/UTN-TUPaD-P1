# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1)

# Defino una función recursiva que calcule la potencia de un número elevado a un exponente segun fórmula
def potencia_recur(n,m):
    if m == 0:          # Establezco los casos base para exponentes 0 y 1
        return 1
    elif m == 1:
        return n
    else:
        return n * potencia_recur(n,m-1)

# Esta cláusula verifica si el script está siendo ejecutado directamente (en vez de importado como módulo).
if __name__ == "__main__":
    # Programa principal
    print(potencia_recur(2,5))