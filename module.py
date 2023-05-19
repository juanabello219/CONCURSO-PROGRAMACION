from os import system 
system("clear")
import random

tarjetas={}
def menu():
    print("================================")
    print("***Bienvenidos al menu principal")
    print("================================")
    print("                                ")
    print("1.    recarga de tarjeta        ")
    print("2.    comprar tarjeta           ")
    print("3.    recarga por codigo        ")
    print("4.            salir             ")
    print("                                ")
    print("================================")
    opcion = int(input("ingrese la opcion que deseas: "))
    if (opcion>4):
        print("error, la opcion ingresada no se encuentra dentro el menu")
    if (opcion==1):
        print("opcion se encuentra en desarrollo")
    elif (opcion==2):
        compra_tarjetas()
    elif (opcion ==3):
        print("opcion se encuentra en desarrollo")
    elif(opcion==4):
        print("saliendo del sistema...")
        exit()
    else:
        print("ocurrio un error")


def compra_tarjetas():
        cedula = input("por favor ingrese su cedula: ")
        nombre = input("por favor ingrese su nombre:  ")
        direccion = input("por favor ingrese su direccion: ")
        telefono = input("por favor ingrese su numero de telefono: ")
        valor_tarjeta= 0
        opcion = input("deseas recargar tu tarjeta (si/no):")
        if opcion == "si":
            recarga=int(input("ingresa el valor de la recarga: "))
            valor_tarjeta = recarga
        elif opcion == "no":
            print("saliendo del sistema... ")
            quit()
        for _ in range(1,6):
            cod_tarjeta= random.randrange(1000000,9000000)
            if cod_tarjeta in tarjetas:
                cod_tarjeta= random.randrange(1000000,9000000)
        tarjetas["cedula"]=cedula
        tarjetas["nombre"]=nombre
        tarjetas["direccion"]=direccion
        tarjetas["telefono"]=telefono
        tarjetas["cod_tarjeta"]=cod_tarjeta
        tarjetas["saldo_tarjeta"]= valor_tarjeta
        print(tarjetas)


