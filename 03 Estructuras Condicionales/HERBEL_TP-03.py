# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = float(input("Por favor, ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Por favor, ingrese un número: "))

if (num % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12:
    print("Usted es Niño/a")

elif edad >= 12 and edad < 18:
    print("Usted es Adolescente")

elif edad >= 18 and edad < 30:
    print("Usted es Adulto/a joven")

else: 
    print("Usted es un Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

contrasenia = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")

else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente: 
## from statistics import mode, median, mean 
## mi_lista = [1,2,5,5,3] 
## mean(mi_lista) 
# En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html.  La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
# Definir la lista numeros_aleatorios de la siguiente forma: 
## import random 
## numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria. 

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print(f"Esta es una lista de 50 números seleccionados al azar: {numeros_aleatorios}")

from statistics import mode, median, mean
moda = (mode(numeros_aleatorios))
mediana = (median(numeros_aleatorios))
media = (mean(numeros_aleatorios))

if media > mediana > moda:
    print("La lista tiene sesgo positivo")

elif media < mediana < moda:
    print("La lista tiene sesgo negativo")

else:
    print("La lista no tiene sesgo")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

palabra = input("Por favor, ingrese una palabra: ")

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

if palabra[-1] in (vocales):
    print(f"{palabra}!")

else:
    print(palabra)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor ingrese su nombre: ")

print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n"
      "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n"
      "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = input("Por favor seleccione una opción (1, 2 o 3): ")

if opcion.isdigit():
    opcion = int(opcion)

    if opcion == 1:
        print(nombre.upper())

    elif opcion == 2:
        print(nombre.lower())

    elif opcion ==3:
        print(nombre.title())

    else:
        print("Opción inválida. Debe ingresar 1, 2 o 3.")

else:
    print("Entrada inválida. Debe ingresar un número.")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = input("Por favor, ingrese la magnitud (Ritcher): ")

try: 
    magnitud = float(magnitud)

    if magnitud < 0:
        print("Entrada inválida. La magnitud no puede ser un número negativo")       

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    
    elif magnitud < 4:
        print("Leve (ligeramente perceptible)")
    
    elif magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    
    elif magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")

    elif magnitud < 7:
        print("Muy fuerte (puede causar daños significativos)")
    
    else:
        print("Extremo (puede causar graves daños a gran escala)")

except ValueError:
    print("Entrada inválida. Debe ingresar un número.")


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

meses_dias = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

mes = int(input("Por favor, indique el mes del año (1-12): "))

if mes not in meses_dias:
    print("Error: El mes debe estar entre 1 y 12.")
    exit()

dia = int(input(f"Por favor, indique el día del mes (1-{meses_dias[mes]}): "))

if dia < 1 or dia > meses_dias[mes]:
    print(f"Error: Día inválido. Hasta {meses_dias[mes]} días en el mes {mes}.")
    exit()

hemisferio = input("Por favor, indique en qué hemisferio se encuentra (N/S): ")
hemisferio = hemisferio.upper()

nombres_hemisferios = {"N":"NORTE", "S":"SUR"}

if hemisferio not in nombres_hemisferios:
    print("Error, debe ingresar 'N' para hemisferio norte o 'S' para hemisferio sur.")
    exit()

else:
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    else:
        if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:
            estacion = "Primavera"

print(f"En el hemisferio {nombres_hemisferios[hemisferio]}, el dia {dia}/{mes} corresponde a la estacion {estacion}.")
