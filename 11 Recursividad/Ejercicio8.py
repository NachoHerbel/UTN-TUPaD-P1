# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

# Defino la función
def contar_digito(numero, digito):
    if numero == 0:     # Caso base cuando el número es 0 ya no hay dígitos que contar
        return 0
    else:
        ultimo_digito = numero % 10     # Tomo el último dígito del número
        if ultimo_digito == digito:     # Llamo recursivamente con el número sin el último dígito, sumando apariciones si corresponde
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Verificación de la función
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))
