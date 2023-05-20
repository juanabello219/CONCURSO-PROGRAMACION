#Programación de reportes
datos_usuarios = [{
    "1065875449":{
        "nombre":"Didier Fernando",
        "apellido":"Guerrero Sumalave", 
        "direccion":"Carrera 37 número 2 Norte 29", 
        "telefono":"3208777146", 
        "tarjetas_a_cargo":[
            [
                890123,0,True
            ],
            [
                123890,10000,False
            ]
        ]
    } 
}]

import module_reportes
from clear_screen import system_clear_function

#Menu para realizar las consultas
def menu_reportes(datos_usuarios:list):
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
        print("6.    Salir de los reportes                  ")
        print("                                             ")
        print("============================================ ")
        opcion = int(input("Ingrese la opción que deseas utilizar: "))
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            return 
        else:
            print("La opción no es valida, intentelo de nuevo.")
            continue