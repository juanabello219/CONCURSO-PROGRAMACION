from os import system 
from clear_screen import system_clear_function
from datetime import datetime
import random
import reportes
from module_reportes import search_user

#Datos de prueba para que veas como se va a organizar la estructura.
datos_usuarios = [{
    "1065875449":{
        "nombre":"Didier Fernando",
        "apellido":"Guerrero Sumalave", 
        "direccion":"Carrera 37 número 2 Norte 29", 
        "telefono":"3208777146", 
        "tarjetas":[
            [
                890123,0,"Activa"
            ],
            [
                123890,10000,"Activa"
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

def recargas_tarjetas(datos_usuarios):
    cedula = input("Ingrese el numero de su cedula: ")
    for row in datos_usuarios:
        #print(row)
        valor = list(row.keys())
        #print(valor)
        if valor[0] == cedula:
            datos_usuario=row[cedula]
            print(f"{datos_usuario['nombre']} {datos_usuario['apellido']}")
            tarjetas=datos_usuario["tarjetas"]
            print("="*90)
            print("                       DATOS DE LAS TARJETAS                       ")
            gap = ' '*3
            encabezado = f"{'Codigo':^6s}{gap}{'Saldo':^10s}{gap}{'Estado':^10}"
            print("="*32)
            print(encabezado)
            print("-"*32)
            for i in tarjetas:
                rec = f"{i[0]:<6d}{gap}{i[1]:10d}{gap}{i[2]:>10s}"
                print(rec)
            cod_recarga=int(input("Ingrese el codigo de la tarjeta a recargar: "))
            for i in tarjetas:
                if i[0]==cod_recarga and i[2]=="Inactiva":
                    print("Esta tarjeta esta inactiva, no se puede recargar")
                    return
                elif i[0]==cod_recarga and i[2]=="Activa":
                    pos=tarjetas.index(i)
                    cop_recarga=int(input("Ingrese el valor a recargar: "))
                    tarjetas.pop(pos)
                    print(tarjetas)
                    temp=[i[0],i[1]+cop_recarga,"Activa"]
                    tarjetas.append(temp)
                    datos_usuario["tarjetas"]=tarjetas
                    print(datos_usuario)
                    print(datos_usuarios)
                    return 

def inactivar_tarjetas(datos_usuarios):
    cedula = input("Ingrese el numero de su cedula: ")
    for row in datos_usuarios:
        #print(row)
        #valor = list(row.keys())
        valor = row.get(cedula)
        if valor != None:
            datos_usuario=row[cedula]
            print(f"{datos_usuario['nombre']} {datos_usuario['apellido']}")
            tarjetas=datos_usuario["tarjetas"]
            print("="*90)
            print("                       DATOS DE LAS TARJETAS                       ")
            gap = ' '*3
            encabezado = f"{'Codigo':^6s}{gap}{'Saldo':^10s}{gap}{'Estado':^10}"
            print("="*90)
            print(encabezado)
            print("-"*90)
            for i in tarjetas:
                rec = f"{i[0]:<6d}{gap}{i[1]:10d}{gap}{i[2]:>10s}"
                print(rec)
            cod_tarjeta=int(input("Ingrese el codigo de la tarjeta a desactivar: "))
            for i in tarjetas:
                if cod_tarjeta ==i[0]:
                    pos=tarjetas.index(i)
                    confirmacion=input("Confirma inactivación de tarjeta [si/no]: ").lower()
                    if confirmacion=="si":
                        tarjetas.pop(pos)
                        #print(tarjetas)
                        temp=[i[0],i[1],"Inactiva"]
                        tarjetas.append(temp)
                        datos_usuario["tarjetas"]=tarjetas
                        #print(datos_usuario)
                        #print(datos_usuarios)
                        
        else:
            print("Este usuario no esta registrado en el sistema.")

#Juan toca mejorar esto pensando en la estructura que deje como base arriba.
def compra_tarjetas():
    usuario={}
    cedula = input("Ingrese su numero de cedula: ")
    valor = search_user(datos_usuarios, cedula)
    if valor:
        print("El usuario ya se encuentra registrado, buscalo en los reportes.")
    else:
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
                estado = "Activa"
                usuario[cedula]={"nombre":nombre,"apellido":apellido,"direccion":direccion,"telefono":telefono,"tarjetas":[]}
                valor=usuario[cedula]
                x = [codigo, valor_tarjeta, estado]
                valor["tarjetas"]=[x]
                datos_usuarios.append(usuario)
                return f"El proceso fue exitoso"

def search_user(datos_usuarios, cedula):
    for row in datos_usuarios:
        #print(row)
        valor = list(row.keys())
        #print(valor)
        if valor[0] == cedula:
            return True
        else:
            continue
    return False


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
        print("5.    Inactivación de tarjeta                ")
        print("6.    Salir del sistema                      ")
        print("                                             ")
        print("============================================ ")
        opcion = int(input("Ingrese la opción que deseas utilizar: "))
        if (opcion>6):
            system_clear_function()
            print("La opción no se encuentra, intentalo de nuevo.")
            continue
        if (opcion==1):
            recargas_tarjetas(datos_usuarios)
        elif (opcion==2):
            valor=compra_tarjetas()
            print(valor)
           #print(datos_usuarios)
        elif (opcion ==3):
            pass
        elif(opcion==4):
            reportes.menu_reportes(datos_usuarios)
        elif (opcion==5):
            inactivar_tarjetas(datos_usuarios)
        else:
            print("Ocurrio un error, Intentalo de nuevo.")
            continue