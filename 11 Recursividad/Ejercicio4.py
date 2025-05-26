# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

# Solicito al usuario que ingrese un número para transformar en binario
dec_bin = int(input("Por favor, ingrese un número decimal para transformar a binario: "))

# Importo la función para transformar decimal a binario
from decimal_a_biario import decimal_a_binario

# Muestro por pantalla el resultado 
print(f"El número {dec_bin} en binario es: {decimal_a_binario(dec_bin)}")