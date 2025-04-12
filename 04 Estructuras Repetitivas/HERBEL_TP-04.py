# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for x in range (0,101):
    print (x)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
num = int(input("Por favor, ingrese un número: "))

num = abs(num)

digito = 0

if num == 0:
    digito =1
else:
    while num > 0:
        num = num // 10
        digito += 1

print(f"El número tiene {digito} digito/s.")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
num_A = int(input("Por favor ingrese el primer número entero:"))
num_B = int(input("Por favor ingrese el segundo número entero:"))

if num_A > num_B:
    num_A, num_B = num_B, num_A

sumatoria = 0
for i in range (num_A + 1, num_B):
    sumatoria += i

print(f"La sumatoria de los números comprendidos entre {num_A} y {num_B} es: {sumatoria}")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
num = int(input("Por favor ingrese un número entero (0 para terminar): "))

sumatoria = 0

while num != 0:
    sumatoria = sumatoria + num
    num = int(input("Por favor, ingrese otro número entero (0 para terminar): "))

print("La sumatoria de los números ingresados es: ", sumatoria)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
import random
num_aleatorio = random.randint(0, 9)
intentos = 0

num_usuario = int(input("Por favor, ingrese un número entre 0 y 9: "))
intentos += 1

while num_usuario != num_aleatorio:
    print("Incorrecto, intente nuevamente.")
    num_usuario = int(input("Ingrese otro número entre 0 y 9: "))
    intentos += 1

print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for x in range (98,0,-2):
    print (x)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
num = int(input("Por favor, ingrese un número entero positivo: "))
sumatoria = 0

if num > 0:
    for i in range (0,num):
        sumatoria += i
    print(f"La sumatoria de los número comprendidos entre {num} y 0 es: {sumatoria}")
else:
    print("Por favor, ingrese un número entero positivo.")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont_pares = 0
cont_impares = 0
cont_positivos = 0
cont_negativos = 0

for i in range (100):
    num = int(input(f"Por favor, ingrese el número {i+1}: "))
    if num % 2 == 0:
        cont_pares = cont_pares + 1
    else:
        cont_impares = cont_impares + 1

    if num > 0:
        cont_positivos = cont_positivos + 1
    else:
        cont_negativos = cont_negativos + 1

print ("Los números pares son: ",cont_pares)
print ("Los números impares son: ",cont_impares)
print ("Los números positivos son: ",cont_positivos)
print ("Los números negativos son: ",cont_negativos)


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).
from statistics import mean

lista_usuario = []

for i in range (100):
    num = int(input(f"Por favor ingrese el número {i+1}: "))
    lista_usuario.append(num)

media = mean(lista_usuario)

print("La media de los números ingresados es", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
num = int(input("Por favor, ingrese un número entero: "))

numero_invertido = 0

while num > 0:
    ultimo_digito = num % 10
    numero_invertido = numero_invertido * 10 + ultimo_digito
    num = num // 10

print("El número invertido es", numero_invertido)