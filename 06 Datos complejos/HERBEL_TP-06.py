# 1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# Defino el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añado las frutas
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

# Imprimo el diccionario
print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

#Actualizo precios
precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

# Imprimo el diccionario
print(precios_frutas)


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# Imprimo solo las keys
print(precios_frutas.keys())


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# Crear un diccionario vacío
contactos = {}

# Utilizo un range para repetir el código 5 veces
for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número del contacto: ")
    contactos[nombre] = numero  # Guardamos el número asociado al nombre

# Solicito el nombre del contacto para buscarlo en el diccionario
consulta = input("Por favor, ingrese el nombre del contacto que quiere buscar: ")

if consulta in contactos:   # Busca si el nombre está guardado
    print("El número es: ", contactos[consulta])
else:
    print("El contacto no existe.")


# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicito al usuario que ingrese una frase
frase = input("Por favor, ingrese una frase: ")

# Separo la frase en palabras
palabras = frase.split()

# Creo el set de palabras unicas
palabras_unicas = set(palabras)

# Creo un diccionario vacío para ir llenandolo
conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1    # Si ya está, sumamos 1
    else:
        conteo[palabra] = 1     # Si no está, empezamos en 1

# Imprimimos los resultados por pantalla
print("Palabras únicas: ", palabras_unicas)
print("Conteo de palabras:")
for palabra, cantidad in conteo.items(): 
    print(f"{palabra}: {cantidad}")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

# Creo el diccionario vacío
alumnos = {}

# Solicito el nombre de los 3 alumnos y sus notas
for i in range (3):
    nombre = input(f"Por favor ingrese el nombre del alumno {i + 1}: ")
    
    print("Ingresá las 3 notas del alumno separadas por espacio (ej: 7 8 9): ")
    notas_input = input()

    notas = tuple(map(int, notas_input.split()))    # Convierte el string a lista de enteros y luego a tupla

    alumnos[nombre] = notas

# Calcular y mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")


# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Defino un set para quienes aprobaron el primer parcial
parcial_1 = {101, 102, 103, 104}

# Defino un set para quienes aprobaron el segundo parcial
parcial_2 = {101, 103, 105, 106}

# Muestro quienes aprobaron ambos parciales
ambos = parcial_1 & parcial_2   # Busco la intersección de ambos conjuntos
print(f"Quienes aprobaron ambos parciales son: {ambos}")

# Muestro quienes aprobaron solo uno
solo_uno = parcial_1 ^ parcial_2    # Busco la diferencia entre los conjuntos
print(f"Quienes aprobaron un parcial son: {solo_uno}")

# Muestro quienes aprobaron al menos uno
al_menos_uno = parcial_1 | parcial_2    # Busco la unión entre los conjuntos
print(f"Quienes aprobaron al menos un parcial son: {al_menos_uno}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Creo un diccionario vacío
stock = {
    "manzanas": 10,
    "bananas" : 5,
    "naranjas" : 8
}

# Solicito al usuario que ingrese un producto
producto = input("Por favor, ingrese un producto: ").lower()

# Reviso si el producto existe y en tal caso, actualizo el stock
if producto in stock:
    print(f"Hay {stock[producto]} kilos de {producto}.")

    agregar = int(input("¿Cuántas kilos quiere agregar?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
# Si el producto no está en el stock, lo agrego y cargo su stock
else:
    print(f"{producto} no está en el stock.")

    nuevo_stock = int(input(f"¿Cuántas kilos de {producto} quiere agregar?: "))
    stock[producto] = nuevo_stock
    print(f"{producto} fue agregado al stock con {nuevo_stock} kilos.")


# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# agenda = {
#     ("lunes", "10:00"): "Reunión",
#     ("martes", "15:00"): "Clase inglés",
# }
# Permití consultar qué actividad hay en cierto día y hora.

# Creo la agenda con claves como tuplas (día, hora)
agenda = {
    ("lunes", "19:00") : "Arq. y S.O.",
    ("miercoles", "19:00") : "Programación",
    ("jueves", "21:00") : "Org. Empresarial",
    ("viernes", "20:00") : "Matemáticas",
}

# Pido datos al usuario
dia = input("Ingre el día: ").lower()
hora = input("Ingre la hora (HH:MM): ")

# Creo la tupla de búsqueda
consulta = (dia, hora)

# Consulto la agenda
if consulta in agenda:
    print(f"Tenés: {agenda[consulta]}")
else:
    print("No hay ninguna actividad programada en ese día y hora.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:
# original = {"Argentina": "Buenos Aires"}
# invertido = {"Buenos Aires": "Argentina"}

# Creo el primer diccionario
original = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín"
}

# Creo el diccionario invertido
invertido = {}

# Recorro el original e invierto los los keys / values
for pais, capital in original.items():
    invertido[capital] = pais

# Muestro el resultado
print("Diccionario original:\n", original)
print("\nDiccionario invertido:\n", invertido)