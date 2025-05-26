# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# Defino la función para sumar los dígitos de un número
def suma_digitos(n):
    if n < 10:          # Caso base, si el número tiene un sólo dígito, se devuelve ese número
        return n
    else:
        return (n % 10) + suma_digitos(n // 10) # Sumo el último dígito y llamo recursivamente con la división entera
    

# Verificación de la función
print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))