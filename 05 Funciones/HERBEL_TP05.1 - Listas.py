# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
#Creo una lista que inicia en 4 y va sumando de a 4 hasta llegar al 100 inclusive
lista = list(range(4,101,4))
print(lista) #Muestro la lista completa


# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
# Creo una lista con cinco elementos
mi_lista = ['playa', 'mar', 'sol', 'arena', 'viento']
print(mi_lista[-2]) #Muestro el penultimo usando la indexación negativa, buscando desde el último hacia el inicio


# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

#Creo una lista vacía
lista_vacía = []
lista_vacía.append('perro') #Agrego tres palabras
lista_vacía.append('gato')
lista_vacía.append('pajaro')
print(lista_vacía) #Imprimo por pantalla la lista actualizada


# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

#Creo la lista 'animales' con cuatro elementos
animales = ['perro', 'gato', 'conejo', 'pez']
animales[1] = 'loro' #Cambio el segundo valor, (índice 1) por 'loro'
animales[-1] = 'oso' #Cambio el último valor (índice -1) por 'oso'
print(animales) #Imprimo la lista actualizada


# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

#El programa crea la lista con esos 5 valores y luego remueve el valor mas grande. Finalmente imprime la lista actualizada sin el número mayor


# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

#Creo una lista con números del 1 al 30, avanzando de 5 en 5
una_lista = list(range(10,31,5))
print(una_lista[0:2]) #Imprimo los dos primeros valores de la lista usando slicing


# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

#Creo una lista llamada 'autos' con cuatro elementos
autos = ['sedan', 'polo', 'suran', 'gol']
autos [1] = 'nivus' #Cambio el índice 1 ('polo') por 'nivus'
autos [2] = 'taos' #Cambio el índice 2 ('suran') por 'taos'
print(autos) #(opcional) Imprimo la lista actualizada para verificar


# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

#Creo la lista vacía 'dobles'
dobles = []
dobles.append(2*5) #Agrego el doble de 5
dobles.append(2*10) #Agrego el doble de 10
dobles.append(2*15) #Agrego el doble de 15
print(dobles) #Imprimo la lista resultante


# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# Dada la lista 'compras', cuyos elementos representan productos comprados por diferentes clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append('jugo') #Agrego 'jugo' a la lista del tercer cliente

compras[1][1] = 'tallarines' #Reemplazo ´fideos´ por tallarines en la lista del segundo cliente (índice 1)

compras[0].remove('pan') #Elimino 'pan' de la lista del primer cliente (índice 0)

print(compras) #Imprimo la lista resultante


# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

#Creo la lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada) #Imprimo la lista resultante