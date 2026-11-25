# sesion 4
# consultar cadena de texto

# producto = "monitor"
# print(producto [0]) # m
# print(producto [1]) # o
# print(producto [2]) # n
# print(producto [3]) # i
# print(producto [4]) # t
# print(producto [5]) # o
# print(producto [6]) #r

# f strings construir mensajes con variables

# print(f"El producto es: {producto}")

# posiciones positivas y negativas
# print(producto[6]) # r
# print(producto[-1]) # r
# print(producto[0])

# extraer partes de una cadena de texto
# print(producto[0:3]) # mon
# print(producto[2:5]) # ito 
# print(producto[3:]) # itor

# longitud de una cadena de texto
# producto = "memoria ram 16gb"
# longitud = len(producto)
# print("La longitud de la cadena de texto es: ", len(producto))

# metodos de cadenas de texto
# convertir a mayusculas

# producto = "memoria ram 16gb"
# print(producto.upper()) # MEMORIA RAM 16GB

# convertir a minusculas
# print(producto.lower()) # memoria ram 16gb

# capitalizar la primera letra de la cadena de texto
# print(producto.capitalize()) # Memoria ram 16gb

# reemplazar una palabra por otra
# print(producto.replace("a", "e")) 

# agregar una letra al final de la cadena de texto
# print(producto + "s")

# eliminar espacios en blanco al inicio y al final de la cadena de texto
# print(producto.strip())

# limpiar base de datos
# nombre = "   Richard Rodriguez   "
# print(f"nombre del cliente es: {nombre.strip()}")

# ejercicio

# nombre = ["   MARIA GOMEZ   ", "   juan perez   ", "   ANA LOPEZ   "]

# consultar primer nombre
# print(nombre[0].strip().capitalize()) # Maria gomez

# limpia el primer nombre
# nombre[0] = nombre[0].strip()

# convierte a formato titulo
# print(nombre[0].strip().title()) 
# print(nombre[1].strip().title())
# print(nombre[2].strip().title())

# listas

# listas = ["monitor",
#            "teclado",
#              "mouse",
#               "pendrive"]

# print(listas)

# operaciones básicas con listas
# listas.append("impresora")
# print(listas)

# agregar un elemento en una posición específica
# listas.insert(0, "disco duro")
# print(listas)

# eliminar un elemento de la lista
# listas.remove("pendrive")
# print(listas)

# eliminar un elemento de la lista
# del listas[2]
# print(listas) 

# ordenar una lista
# listas.sort() 
# print(listas)

# ordenar una lista en reversa
# listas.sort(reverse=True)
# print(listas)

# unir dos listas
# listas2 = ["teclado inalambrico", "mouse inalambrico", "pendrive externo"]
# listas3 = listas + listas2
# print(listas3)

# convertir cadena de texto a lista
# cadena = "monitor, teclado, mouse, pendrive"
# lista4 = cadena.split(", ")
# print(lista4)

# contar elementos de una lista
# print(len(lista4))

# ejercicio 2

# crear una lista
# listas = ["Saco", "Camiseta", "Pantalon", "Zapatos", "Gorra"]
# print(listas)
# consulta un elemento de la lista
# print(listas[3])
# modifica un elemento de la lista
# listas[3] = "Botas"
# print(listas)
# agregar un elemento a la lista
# listas.append("Reloj")
# print(listas)
# elimina un elemento de la lista
# listas.remove("Gorra")
# print(listas)

#duplas

ubicaciones-geograficas = ("Latitud", "Longitud", "Altitud")    
print(ubicaciones-geograficas)

cordinantes = (12.0464, -77.0428, 16.40909)
print(cordinantes)

estadistica-media = (10, 20, 30, 40, 50)
print(estadistica-media)

datos-personales = ("cedula", "nombre", "apellido", "edad")
print(datos-personales)

