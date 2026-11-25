#RETO
flota = [
    {"codigo": "V-101", "km": 320},
    {"codigo": "V-102", "km": 780},
    {"codigo": "V-103", "km": 1250},
    {"codigo": "V-104", "km": 1680},
    {"codigo": "V-105", "km": 450},
    {"codigo": "V-106", "km": 920},
    {"codigo": "V-107", "km": 1420},
    {"codigo": "V-108", "km": 1850},
    {"codigo": "V-109", "km": 610},
    {"codigo": "V-110", "km": 1100},
    {"codigo": "V-111", "km": 250},
    {"codigo": "V-112", "km": 1550},
]

#contadores
uso_reciente = 0
seguimiento = 0
programar_revision = 0
prioridad_alta = 0
fuera_de_rango = 0

#kilometraje
km_total = 0

print("MANTENIMIENTO")

#registros
for vehiculo in flota:
    codigo = vehiculo["codigo"]
    km = vehiculo["km"]

#acumular kilómetros
    km_total += km

#intervalos
    if 0 <= km <= 499:
        categoria = "Uso reciente"
        uso_reciente += 1
    elif 500 <= km <= 999:
        categoria = "Seguimiento"
        seguimiento += 1
    elif 1000 <= km <= 1499:
        categoria = "Programar revisión"
        programar_revision += 1
    elif 1500 <= km <= 1999:
        categoria = "Prioridad alta"
        prioridad_alta += 1
    else:
        categoria = "Fuera de rango (2000 km o más)"
        fuera_de_rango += 1

    print(f"Vehículo: {codigo} | Km: {km} km | Categoría: {categoria}")

#promedio
cantidad_vehiculos = len(flota)
promedio_km = km_total / cantidad_vehiculos

#reporte
print("FRECUENCIAS Y KILOMETRAJE")
print(f"0 a 499 km (Uso reciente):        {uso_reciente} vehículos")
print(f"500 a 999 km (Seguimiento):       {seguimiento} vehículos")
print(f"1.000 a 1.499 km (Programar rev.):{programar_revision} vehículos")
print(f"1.500 a 1.999 km (Prioridad alta):{prioridad_alta} vehículos")
if fuera_de_rango > 0:
    print(f"Otros rangos:                     {fuera_de_rango} vehículos")
print(f"Total de vehículos evaluados:     {cantidad_vehiculos}")
print(f"Kilometraje acumulado total:      {km_total} km")
print(f"Promedio de km por vehículo:      {promedio_km:.2f} km")

#while
print("CONSULTA INDIVIDUAL DE VEHICULOS")

continuar = "s"

while continuar == "s":
    codigo_buscado = input("\nIngrese el código del vehículo (ej. V-103): ").strip().upper()
    encontrado = False

    for vehiculo in flota:
        if vehiculo["codigo"] == codigo_buscado:
            encontrado = True
            km = vehiculo["km"]

            if 0 <= km <= 499:
                categoria = "Uso reciente"
            elif 500 <= km <= 999:
                categoria = "Seguimiento"
            elif 1000 <= km <= 1499:
                categoria = "Programar revisión"
            elif 1500 <= km <= 1999:
                categoria = "Prioridad alta"
            else:
                categoria = "Fuera de rango (2000 km o más)"

            print(f"-> Código: {vehiculo['codigo']}")
            print(f"-> Kilometraje desde último mantenimiento: {km} km")
            print(f"-> Estado / Categoría: {categoria}")
            break

    if not encontrado:
        print(f"-> No se encontró ningún vehículo con el código '{codigo_buscado}'.")

    continuar = input("\n¿Desea realizar otra consulta? (s/n): ").strip().lower()

print("Consulta finalizada")