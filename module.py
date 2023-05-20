from os import system 
from clear_screen import system_clear_function
from datetime import datetime
import random
import reportes


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
    }
]

codigos_tarjetas = []

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
        print("5.   inactivación de tarjeta                 ")
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
            valor=compra_tarjetas()
            print(valor)
            print(datos_usuarios)
        elif (opcion ==3):
            pass
        elif(opcion==4):
            reportes.menu_reportes(datos_usuarios)
        else:
            print("Ocurrio un error, Intentalo de nuevo.")
            continue

#Juan toca mejorar esto pensando en la estructura que deje como base arriba.
def compra_tarjetas():
    usuario={}
    cedula = input("Ingrese su numero de cedula: ")
    nombre = input("ingrese su nombre completo: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()
    direccion = input("Ingrese su direccion: ").capitalize()
    telefono = input("Ingrese su numero de telefono: ")
    while (True):
        codigo=random.randrange(100000,999999)
        if codigo in codigos_tarjetas:
            continue
        else:
            codigos_tarjetas.append(codigo)
            valor_tarjeta = 0
            estado = True
            usuario[cedula]={"nombre":nombre,"apellido":apellido,"direccion":direccion,"telefono":telefono,"tarjetas":[]}
            valor=usuario[cedula]
            valor["tarjetas"]=[codigo,valor_tarjeta,estado]
            datos_usuarios.append(usuario)
            return f"el proceso fue exitoso"
