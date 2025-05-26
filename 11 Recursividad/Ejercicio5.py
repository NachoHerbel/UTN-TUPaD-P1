# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Defino la funcion es_palindromo(palabra)
def es_palindromo(palabra):
    if len(palabra) <= 1:           # Establezco el caso base donde la palabra tiene 1 o 0 letras, considerándola palíndromo
        return True
    if palabra[0] != palabra[-1]:   # Si los caracteres son diferentes, la palabra no es palíndromo
        return False
    return es_palindromo(palabra[1:-1]) # Comparo el primer caracter con el último recursivamente

# Verificación de la función
print(es_palindromo("radar"))
