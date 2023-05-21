#Programación de reportes
# #datos_usuarios = [{
#     "1065875449":{
#         "nombre":"Didier Fernando",
#         "apellido":"Guerrero Sumalave", 
#         "direccion":"Cra 37 # 2N29", 
#         "telefono":"3208777146", 
#         "tarjetas_a_cargo":[
#             [
#                 890123,0,True
#             ],
#             [
#                 123890,10000,False
#             ]
#         ]
#     } 
# },
#                 {
#     "1065875448":{
#         "nombre":"Didier Fernando",
#         "apellido":"Guerrero Sumalave", 
#         "direccion":"Cra 37 # 2N29", 
#         "telefono":"3208777146", 
#         "tarjetas_a_cargo":[
#             [
#                 890123,0,True
#             ],
#             [
#                 123890,10000,False
#             ]
#         ]
#     } 
# }
#                 ]

# #Datos de las recargas
# recargas = [
#     {
#     10001:{
#             "codigo_tarjeta": 890123,
#             "cedula_usuario": "1065875449",
#             "valor_recarga":20000,
#             "fecha":"2023-05-19 20:32:00.556641"
#         }
#     },
#     {
#     10002:{
#             "codigo_tarjeta": 890123,
#             "cedula_usuario": "1065875449",
#             "valor_recarga":5000,
#             "fecha":"2023-05-19 20:40:00.556641"
#         }
#     }
# ]

import module_reportes
from clear_screen import system_clear_function
import module
#from module import datos_usuarios

#Menu para realizar las consultas
def menu_reportes(datos_usuarios):
    while (True):
        print("============================================ ")
        print("*****SYSTEM E-CARD AGUACHICA****             ")
        print("============================================ ")
        print("                                             ")
        print("1.    Consultar datos por usuario            ")
        print("2.    Consultar datos por tarjeta            ")
        print("3.    Consultar tarjetas activas             ")
        print("4.    Consultar tarjetas inactivas           ")
        print("5.    Consultar recargas por fecha           ")
        print("6.    Consultar registro por compra")
        print("7.    Salir de los reportes                  ")
        print("                                             ")
        print("============================================ ")
        opcion = int(input("Ingrese la opción que deseas utilizar: "))
        if opcion == 1:
            print(datos_usuarios)
            module_reportes.search_user(datos_usuarios)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            module.crear_csv() 
        elif opcion == 7:
            return
        else:
            print("La opción no es valida, intentelo de nuevo.")
            continue