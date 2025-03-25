# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar = input("Por favor, ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

from math import pi
r = float(input("Por favor, ingrese el radio del círculo: "))
print (f"El perímetro del círculo es: {round(2*r*pi,2)}")
print (f"El área del círculo es: {round(pi*(r**2),2)}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seg = int(input("Por favor, ingrese la cantidad de segundos: "))

print (f"Eso equivale a {round(seg/3600,2)} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.  

n = int(input("Por favor, ingrese un número: "))

print (f"{n} x 0 = {n * 0}")
print (f"{n} x 1 = {n * 1}")
print (f"{n} x 2 = {n * 2}")
print (f"{n} x 3 = {n * 3}")
print (f"{n} x 4 = {n * 4}")
print (f"{n} x 5 = {n * 5}")
print (f"{n} x 6 = {n * 6}")
print (f"{n} x 7 = {n * 7}")
print (f"{n} x 8 = {n * 8}")
print (f"{n} x 9 = {n * 9}")
print (f"{n} x 10 = {n * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num1 = float(input("Por favor, ingrese el primer número distinto de 0: "))
num2 = float(input("Por favor, ingrese el segundo número distinto de 0: "))
#suma
print (f"La suma de {num1} y {num2} es: {num1 + num2}")
#division
print (f"La división de {num1} y {num2} es: {num1 / num2}")
#multiplicacion
print (f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
#resta
print (f"La resta de {num1} y {num2} es: {num1 - num2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

peso = float(input("Por favor, ingrese su peso (kg): "))
altura = float(input("Por favor, ingrese su altura (m): "))

print (f"Su Índice de Masa Corporal (IMC) es de: {round((peso / (altura **2)),2)}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

cel = float(input("Por favor, ingrese la temperatura en Celsius (C°): "))

print (f"Su equivalente en Fahrenheit (F°) es de {round(((9/5) * cel +32),2)}")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input ("Por favor, ingrese el primer número: "))
num2 = float(input ("Por favor, ingrese el segundo número: "))
num3 = float(input ("Por favor, ingrese el tercer número: "))

print (f"El promedio de dichos números es: {round(((num1 + num2 +num3)/3),2)}")