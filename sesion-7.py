# #sesion 7
# #ciclo for

# guias = ["G001", "G002", "G003", "G004", "G004"]

# for memoria in guias:
#     print("Revisando envío:", memoria)

#     #for+range

#     for consecutivo in range(2):
#         print("revisando envio:", guias [consecutivo])

# for consecutivo in range(2, 5):
#         print("revisando envio:", guias [consecutivo])

# #contadores

# contador = 0

# for guia in guias:
#      contador += 1
#      print("Revisando", guia)
# print("Total:", contador)

# #acumulador de km

# distancias = [15, 22, 10, 18]

# distancia_total = 0
# for distancia in distancias:
#      distancia_total += distancia

# print("Distancia total:", distancia_total)

#ciclo whilw
# #intentos de entrega

# envios = [
#      {"estado": "entregrado"},
#      {"estado": "en ruta"},
#      {"estado": "devuelto"},
#      {"estado": "entregado"},
#      {"estado": "devuelto"},
#      {"estado": "devuelto"},
# ]

# entregados = 0
# en_ruta = 0
# devueltos = 0

# for envio in envios:
#      if envios["estado"] =="entregado":
#           entregados += 1

#     elif envios["estado"] =="en ruta":
#             en ruta +=1

# else:
#     devueltos +=1

# #MOSTRAR RESULTADOS
# # print(RESUMEN DE ENVIOS)
# # print("Entregados:", "entregados")
# # print("En ruta:", "en ruta")
# # print("En ruta:", "en ruta")
# # print("Devueltos:", "devueltos")

# #while
# # intentos de entregas

# guia = "G001"
# intentos = 0
# entregado = False
# while intentos < 3 and entregado == False:
#        intentos += 1
#        entregado = True

#        print("guia", guia)
#        print("intentos de entrega", intentos)

# resultado = input("se entrego el paquete?(s/n):   ").lower()

# if resultado == "s":
#     entregado = True
# else:
#     entregado = False

# if entregado:
#     print("envio entregado")

# else:
#     print("envio devuelto")

# frecuencia de entregas en tiempo

tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0

for tiempo in tiempos:
    if 1 <= tiempo <=3:
        grupo_1_3 +=1
    elif 4 <= tiempo <=6:
        grupo_4_6 +=1
    elif 7 <= tiempo <=9:
        grupo_7_9 +=1
    elif 10 <= tiempo <=12:
        grupo_10_12 +=1

print ("REPORTE DE TIEMPOS DE ENTREGA")
print ("de 1 a 3 días:", grupo_1_3, "entregas")
print ("de 4 a 6 días:", grupo_4_6, "entregas")
print ("de 7 a 9 días:", grupo_7_9, "entregas")
print ("de 10 a 12 días:", grupo_10_12, "entregas")