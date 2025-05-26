# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general.

# Solicito al usuario que ingrese un número base y exponente para calcular su potencia según fórmula
base = int(input("Por favor, ingrese un número base: "))
exponente = int(input("Por favor, ingrese su exponente: "))

# Importo la función del cálculo de la potencia
from potencia_recursiva import potencia_recur

# Muestro por pantalla el resultado 
print(f"El número {base} ^ {exponente} es: {potencia_recur(base,exponente)}")