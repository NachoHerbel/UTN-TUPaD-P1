# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

# Defino la función que transforma un número decimal a binario
def decimal_a_binario(n):
    if n == 0:          # Establezco el caso base cuando el número es 0, devolviendo una cadena vacía
        return ""
    else:
        # Divido el número por 2 (n//2) y concateno el resto de la división (n % 2) al final del resultado
        return decimal_a_binario(n//2) + str(n % 2)


if __name__ == "__main__":
    print(decimal_a_binario(10))