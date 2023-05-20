from os import system 
from clear_screen import system_clear_function
from datetime import datetime
import random


#Datos de prueba para que veas como se va a organizar la estructura.
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
},{
    "1098621411":{
        "nombre":"Juan Andres",
        "apellido":"Abello Contreras", 
        "direccion":"Gamarra Cesar", 
        "telefono":"3157700754", 
        "tarjetas_a_cargo":[
            [
                665100,0,True
            ],
            [
                432600,20000,False
            ]
        ]
    } 
}]

#Datos de las recargas
recargas = [
    {
    10001:{
            "codigo_tarjeta": 890123,
            "cedula_usuario": "1065875449",
            "valor_recarga":20000,
            "fecha":"2023-05-19 20:32:00.556641"
        }
    },
    {
    10002:{
            "codigo_tarjeta": 890123,
            "cedula_usuario": "1065875449",
            "valor_recarga":5000,
            "fecha":"2023-05-19 20:40:00.556641"
        }
    },
    {
        10003:{
            "codigo_tarjeta": 665100,
            "cedula_usuario": "1098621411",
            "valor_recarga":10000,
            "fecha":"2023-05-19 21:27:00.556641"
        }
    }
]

#Menu de opciones
def menu():
    while (True):
        print("============================================ ")
        print("*****SYSTEM E-CARD AGUACHICA****             ")
        print("============================================ ")
        print("                                             ")
        print("1.    Recarga de tarjetas                    ")
        print("2.    Comprar tarjeta                        ")
        print("3.    Registro de usuarios                   ")
        print("4.    Reportes generales                     ")
        print("5.    Activación/inactivación de tarjeta     ")
        print("6.    Salir del sistema                      ")
        print("                                             ")
        print("============================================ ")
        opcion = int(input("Ingrese la opción que deseas utilizar: "))
        if (opcion>4):
            system_clear_function()
            print("La opción no se encuentra, intentalo de nuevo.")
            continue
        if (opcion==1):
            pass
        elif (opcion==2):
            compra_tarjetas()
            pass
        elif (opcion ==3):
            pass
        elif(opcion==4):
            print("Saliendo del sistema...")
            exit()
        else:
            print("Ocurrio un error, Intentalo de nuevo.")
            continue

#Juan toca mejorar esto pensando en la estructura que deje como base arriba.
def compra_tarjetas():
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
},{
    "1098621411":{
        "nombre":"Juan Andres",
        "apellido":"Abello Contreras", 
        "direccion":"Gamarra Cesar", 
        "telefono":"3157700754", 
        "tarjetas_a_cargo":[
            [
                665100,0,True
            ],
            [
                432600,20000,False
            ]
        ]
    } 
}]
    while(True):
        cedula=int(input("ingrese el numero de cedula "))
        if cedula in datos_usuarios:
            print("datos encontrados")
        else:
            datos_usuarios=[{cedula}]
            nombre = input("ingrese su nombre completo:")
            apellido = input("ingrese su apellido: ")