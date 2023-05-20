from clear_screen import system_clear_function


#Funciones para manejar los reportes

#Consultas por usuario
def search_user(data_users):
    cedula = input("Ingrese la cedula a consultar: ")
    for row in data_users:
        valor = list(row.keys())
        #print(valor)
        if valor[0] == cedula:
            system_clear_function()
            print("El usuario esta registrado en el sistema.")
            print("\t INFORMACIÓN DEL USUARIO ")
            print(f"CEDULA""\t\t\tNOMBRE""\t\t\tAPELLIDO""\t\t\tDIRECCION""\t\t\tTELEFONO")
            datos_usuario=row[cedula]
            print("")
            print(f"{cedula} \t{datos_usuario['nombre']}\t{datos_usuario['apellido']}\t{datos_usuario['direccion']}\t{datos_usuario['telefono']}")
            print("")
            print(f"TARJETAS A CARGO")
            cards = datos_usuario["tarjetas_a_cargo"]
            print(f"CODIGO      SALDO       ESTADO")
            for i in cards:
                print(f"{i[0]}      {i[1]}      {i[2]}")
            print("")
            return True
        else:
            print("El usuario no esta registrado en el sistema.")
            return False

#Consultas por tarjeta
def search_card(data):
    pass

#Consultas por tarjetas activas
def search_cards_actives(data):
    pass

#Consultas por tarjetas inactivas
def search_cards_inactives(data):
    pass

#Consultas por fechas
def search_reload_date(data):
    pass
