import os
import csv

#Validar existencia del archivo

def validar_existencia():
    if os.path.isfile("usuarios.txt"):
        if os.path.isfile("recargas.txt"):
            if os.path.isfile("tarjetas.txt"):
                return True
    else:
        return False

def crear_archivo_usuarios():
    fielnames = ["cedula","nombre","apellido","direccion", "telefono", "tarjeta1", "saldo1", "estado1", "tarjeta2", "saldo2", "estado2", "tarjeta3", "saldo3", "estado3"]
    try:
        with open("usuarios.txt", "w", encoding="UTF-8", newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=fielnames, quotechar='"')
            csv_writer.writeheader()
    except FileNotFoundError:
        print("Error en la configuración")

def crear_archivo_recargas():
    fieldnames2 = ["codigo_tarjeta", "valor_recarga", "fecha_recarga"]
    try:
        with open("recargas.txt", "w", encoding="UTF-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames2, quotechar='"')
            csv_writer.writeheader()
    except FileNotFoundError:
        print("Error en la configuración")

def crear_archivo_tarjetas():
    fieldnames2 = ["cedula_usuario", "nombre_usuario", "codigo_tarjeta"]
    try:
        with open("tarjetas.txt", "w", encoding="UTF-8") as f:
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames2, quotechar='"')
            csv_writer.writeheader()
    except FileNotFoundError:
        print("Error en la configuración")


def leer_archivo_usuarios():
    pass

def leer_archivo_recargas():
    pass

def leer_archivo_tarjetas():
    pass
