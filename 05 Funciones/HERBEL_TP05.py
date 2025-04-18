# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Defino la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# //// PROGRAMA PRINCIPAL ////
imprimir_hola_mundo() # Llamamos a la funcion para mostrar el mensaje


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Defino la función
def saludar_usuario(nombre):
    return f"Hola {nombre.title()}!" # Devuelve el saludo con la primer letra en mayúscula

# //// PROGRAMA PRINCIPAL ////
# Solicitamos al usuario el nombre
nombre = input("Por favor, ingrese su nombre: ")
print(saludar_usuario(nombre)) # Llamamos a la funcion para mostrar el mensaje


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Defino la función
def informacion_personal(nombre, apellido, edad, residencia):
    print (f"Soy {nombre.title()} {apellido.title()}, tengo {edad} años y vivo en {residencia.title()}") 

# //// PROGRAMA PRINCIPAL ////
# Solicitamos al usuario sus datos
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = int(input("Por favor, ingrese su edad: "))
residencia = input("Por favor, ingrese su lugar de residencia: ")
# Llamamos a la funcion para mostrar el mensaje con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Importo el valor de pi desde el módulo math
from math import pi

# Defino una función que calcula el área de un círculo
def calcular_area_circulo(r):
    return pi * r ** 2    # Fórmula del área: π * r²

# Defino una función que calcula el perímetro de un círculo
def calcular_perimetro_circulo(r):
    return 2 * pi * r     # Fórmula del perímetro: 2 * π * r

# //// PROGRAMA PRINCIPAL ////
# Solicitamos al usuario que ingrese el radio del círculo y lo convertimos a float
radio = float(input("Por favor, ingrese el radio: "))

# Validamos que la cantidad ingresada sea mayor a cero
if radio <= 0:
    print("ERROR. El radio debe ser un número positivo mayor a cero.")

else:
    # Llamamos a ambas funciones para mostrar el área y perímetro del circulo redondeando en dos decimales    
    print("Área:", round(calcular_area_circulo(radio),2),"| Perímetro:", round(calcular_perimetro_circulo(radio),2))


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

# Defino la función
def segundos_a_horas(segundos):
    return segundos / 3600 # 1 hora tiene 3600 segundos

# //// PROGRAMA PRINCIPAL ////
# Solicitamos al usuario una cantidad de segundos
seg = int(input("Por favor, ingrese los segundos: "))

# Validamos que la cantidad ingresada no sea negativa
if seg < 0:
    print("ERROR. La cantidad se segundos no puede ser negativa.")
else: 
    # Si es válida, convertimos los segundos a horas redondeando en dos decimales
    print("Los segundos ingresados equivalen a", round(segundos_a_horas(seg),2), "horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Defino la funcion que imprime la tabla del número recibido
def tabla_multiplicar(numero):
    for i in range (1,11): # Recorro del 1 al 10
        print(f"{numero} * {i:2} = {numero * i:3}") # Imprimo la tabla completa del numero recibido, de 1 a 10 en cada línea formateando para que los mismos se muestren alineados

# //// PROGRAMA PRINCIPAL ////
num1 = int(input("Por favor, ingrese el número: ")) # Pido al usuario un número 
print(f"\nLa tabla de multiplicar de {num1} es:")
tabla_multiplicar(num1) # Llamo a la función


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Defino la función
def operaciones_basicas(a, b):
# Hago las operaciones
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "ERROR. No se puede dividir por cero (0)"
    return (suma, resta, multiplicacion, division) # Devuelvo los resultados como una tupla

# //// PROGRAMA PRINCIPAL ////
num1 = float(input("Por favor, ingrese el primer número: "))
num2 = float(input("Por favor, ingrese el segundo número: "))

# Llamo a la función con los números ingresados por el usuario y guardo el resultado (como tupla de 4 elementos) en la variable 'resultado'
resultado = operaciones_basicas(num1, num2)

print("\nResultados de las operaciones:")
# Muestro los resultados accediendo a los elementos de la tupla
print(f"SUMA: {num1} + {num2} = {resultado[0]}")
print(f"RESTA: {num1} - {num2} = {resultado[1]}")
print(f"MULTIPLICACIÓN: {num1} x {num2} = {resultado[2]}")
print(f"DIVISIÓN: {num1} / {num2} = {resultado[3]}")


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# Defino la función
def calcular_imc(peso, altura): # Fórmula del IMC = peso / altura²
    return peso / (altura ** 2)

# //// PROGRAMA PRINCIPAL ////
# Le pido al usuario los datos para calcular el IMC
kilos = float(input("Por favor ingrese su peso (kg): "))
metros = float(input("Por favor ingrese su altura (m): "))

# Validamos que la cantidad ingresada no sea cero
if kilos <= 0 or metros <=0:
    print("ERROR. El peso y/o la altura no pueden ser 0")

else:
    # Imprimo el IMC redondeando a 2 decimales
    print("Su IMC es de:", round(calcular_imc(kilos, metros),2))


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Defino la función
def celsius_a_fahrenheit(celsius):   
    return ((9 / 5) * celsius) + 32 # Fórmula para convertir a Temperatura Fahrenheit = 9/5 x Temperatura en Celsius + 32

# //// PROGRAMA PRINCIPAL ////
# Le pido al usuario los grados C° para convertir a F°
grados = float(input("Por favor, ingrese la temperatura (C°): "))

# Imprimo los grados convertidos redondeando a dos decimales
print(f"{grados}, C° equivale a {round(celsius_a_fahrenheit(grados),)} F°")


# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Defino la función
def calcular_promedio(a, b, c):
    return (a + b + c) / 3      # Promedio las 3 notas

# //// PROGRAMA PRINCIPAL ////
# Pido al usuario que ingrese sus tres notas
nota1 = float(input("Por favor, ingrese su primer nota: "))
nota2 = float(input("Por favor, ingrese su segunda nota: "))
nota3 = float(input("Por favor, ingrese su tercer nota: "))

# Imprimo por pantalla el promedio redondeando a 2 decimales
print("Su promedio es:", round(calcular_promedio(nota1, nota2, nota3),2))