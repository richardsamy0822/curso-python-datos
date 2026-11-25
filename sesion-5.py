# # #sesion 5

# # #ejercicio 1

# # televisores = {
# #     "marca": "Samsung",
# #     "precio": 500000,
# #     "pulgadas": 65,
# #     "color": "negro",
# #     "resolucion": "4K"
# # }

# # print(televisores["marca"])
# # print(televisores["precio"])
# # print(televisores["pulgadas"])
# # print(televisores["color"])
# # print(televisores["resolucion"])

# # #consultar informacion get
# # #corchetes

# # print(televisores["precio"])
# # # print(televisores["disponible"])

# # #llaves

# # print(televisores.get("disponible"))
# # print(televisores.get("precio"))
# # print(televisores.get("pulgadas"))

# # #agregar informacion

# # televisores["disponible"] = False
# # print(televisores)

# # #modificar informacion
# # televisores["precio"]= 6000000
# # print(televisores)

# # #eliminar informacion 

# # del televisores["disponible"]
# # print(televisores)

# # #consultar grupos de datos

# # print(televisores.keys())
# # print(televisores.values())
# # print(televisores.items())

# # #coleccion de registros

# # electrodomesticos_de_cocina = [
# #     {
# #         "producto": "Microondas",
# #         "marca": "LG",
# #         "listros": 5,
# #         "color": "plata",
# #         "disponible": True
# # },
# # {
# #         "producto": "sanduchera",
# #         "marca": "oster",
# #         "listros": 5,
# #         "color": "negro",
# #         "disponible": True 
# # }
# # ]
# # print(electrodomesticos_de_cocina[0]["marca"])
# # print(electrodomesticos_de_cocina[1]["marca"])

# #ejercicio ejemplo vs code

# producto_1 = {"codigo": "P001", "nombre": "Cuaderno", "precio": 4500}
# producto_2 = {"codigo": "P002", "nombre": "Mouse", "precio": 35000}
# producto_3 = {"codigo": "P003", "nombre": "Teclado", "precio": 60000}

# inventario = [producto_1, producto_2, producto_3]

# print("Primer producto:", inventario[0]["nombre"])
# print("Precio del segundo:", inventario[1]["precio"])
# print("Tercer producto:", inventario[2]["nombre"], "-", inventario[2]["precio"])

# inventario[0]["precio"] = 5000
# print("Nuevo precio:", inventario[0]["precio"])
# print("Total de productos:", len(inventario))

# #conjuntos
# canales = {"Instagram", "Facebook", "TikTok"}

# print(canales)

# #agregar un canal
# canales.add("LinkedIn")

# print(canales)

# #comprobar si un elemento esta en el conjunto

# print("Instagram" in canales)

# print("youtube" in canales)

# #unir conjuntos

# campania_a = {"Instagram", "Facebook", "TikTok"}
# campania_b = {"LinkedIn", "Youtube", "TikTok"}

# campania_c = campania_a | campania_b
# print(campania_c)

# campania_d = campania_a & campania_b
# print(campania_d)


#diccionarios de productos
nevera_1 = {
    "codigo": "N-001",
    "marca": "Haceb",
    "tipo": "Doméstica",
    "costo_mantenimiento": 150000,
    "cantidad": 2,
    "jardin": "Jardin Infantil La Gaitana"
}

nevera_2 = {
    "codigo": "N-002",
    "marca": "Mabe",
    "tipo": "Industrial",
    "costo_mantenimiento": 350000,
    "cantidad": 1,
    "jardin": "Jardin Infantil El Portal"
}

nevera_3 = {
    "codigo": "N-003",
    "marca": "Whirlpool",
    "tipo": "Exhibidora",
    "costo_mantenimiento": 250000,
    "cantidad": 3,
    "jardin": "Jardin Infantil La Gaitana"
}

#Guardar los productos en una lista
inventario_neveras = [nevera_1, nevera_2, nevera_3]

#Consultar el nombre de un producto.
print("Marca de la primera nevera:", inventario_neveras[0]["marca"])
print("Ubicación de la segunda nevera:", inventario_neveras[1].get("jardin"))

#Modificar el precio o cantidad
inventario_neveras[1]["cantidad"] = 2
inventario_neveras[0]["costo_mantenimiento"] = 165000

print("Nueva cantidad en El Portal:", inventario_neveras[1]["cantidad"])
print("Nuevo costo de mantenimiento (N-001):", inventario_neveras[0]["costo_mantenimiento"])

#Crear un conjunto 
tipos_de_nevera = set()

tipos_de_nevera.add(inventario_neveras[0]["tipo"])
tipos_de_nevera.add(inventario_neveras[1]["tipo"])
tipos_de_nevera.add(inventario_neveras[2]["tipo"])

print("Tipos de neveras únicos en inventario:", tipos_de_nevera)