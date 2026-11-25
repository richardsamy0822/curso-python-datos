# # sesion 3
# # tipo de datos

# # enteros (int)

# edad = 25
# cantidad = 0
# temperatura = -50

# #flotantes (float)
# precio = 10.5
# pi = 3.1416
# peso = 25.2 
# print(edad, cantidad, temperatura, precio, pi, peso)

# #booleanos (bool)
# requiere_inscripcion = True
# esta_lluvioso = False
# print(requiere_inscripcion, esta_lluvioso)

# #type() -> nos permite conocer el tipo de dato de una variable

# print(type(edad))
# print(type(precio))
# print(type(requiere_inscripcion))
# print(type(pi))

# #que pasa si no convierto el tipo de dato

# print(edad + requiere_inscripcion)

# cantidad = 10

# print = (cantidad * 3)

# #registro de ventas

# producto = input("Ingrese el nombre del producto: ")
# cantidad = int(input("Ingrese la cantidad vendida: "))
# precio = float(input("Ingrese el precio del producto: "))

# total = cantidad * precio
# print("producto: ", producto)
# print("total: ", total)
      
#ejercicio clase 3
actividad = str(input("Ingrese la actividad : "))
cupos = int(input("Ingrese la cantidad de cupos: "))
duracion_horas = float(input("Duración de la actividad: "))
requiere_inscripcion = bool(input("Requiere inscripción (True/False): "))

print("actividad: ", actividad)
print("cupos: ", cupos)
print("duracion_horas: ", duracion_horas)
print("requiere_inscripcion: ", requiere_inscripcion)

#funcion type

print(type(actividad))
print(type(cupos))
print(type(duracion_horas))
print(type(requiere_inscripcion))
