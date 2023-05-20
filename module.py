from os import system 
from clear_screen import system_clear_function
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
}]

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
            #compra_tarjetas()
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
    # cedula = input("por favor ingrese su cedula: ")
    # nombre = input("por favor ingrese su nombre:  ")
    # direccion = input("por favor ingrese su direccion: ")
    # telefono = input("por favor ingrese su numero de telefono: ")
    # valor_tarjeta= 0
    # opcion = input("deseas recargar tu tarjeta (si/no):")
    # if opcion == "si":
    #     recarga=int(input("ingresa el valor de la recarga: "))
    #     valor_tarjeta = recarga
    # elif opcion == "no":
    #     print("saliendo del sistema... ")
    #     quit()
    # for _ in range(1,6):
    #     cod_tarjeta= random.randrange(1000000,9000000)
    #     if cod_tarjeta in tarjetas:
    #         cod_tarjeta= random.randrange(1000000,9000000)
    #         tarjetas["cedula"]=cedula
    #         tarjetas["nombre"]=nombre
    #         tarjetas["direccion"]=direccion
    #         tarjetas["telefono"]=telefono
    #         tarjetas["cod_tarjeta"]=cod_tarjeta
    #         tarjetas["saldo_tarjeta"]= valor_tarjeta
    #         print(tarjetas)
    pass