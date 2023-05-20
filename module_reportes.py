from clear_screen import system_clear_function
from string import Template

#Funciones para manejar los reportes

#Consultas por usuario
def search_user(data_users):
    cedula = input("Ingrese la cedula a consultar: ")
    for row in data_users:
        valor = list(row.keys())
        #print(valor)
        if valor[0] == cedula:
            system_clear_function()
            #print("El usuario esta registrado en el sistema.")
            print("***********INFORMACIÓN DEL USUARIO*************")
            #print(f"CEDULA""\t\t\tNOMBRE""\t\t\tAPELLIDO""\t\t\tDIRECCION""\t\t\tTELEFONO")
            print(Template("$cedula $nombre $apellido $direccion $telefono").substitute(cedula = "Cedula", nombre=" Nombres", apellido="Apellidos", direccion="Dirección", telefono="Telefono"))
            datos_usuario=row[cedula]
            print("")
            #print(Template("$cedula\t$nombre\t$apellido\t$direccion\t$telefono").substitute(cedula=cedula, nombre=datos_usuario["nombre"],apellido=datos_usuario['apellido'], direccion=datos_usuario['direccion'], telefono=datos_usuario['telefono']))
            print(f"{cedula}{datos_usuario['nombre']:10}{datos_usuario['apellido']:10}{datos_usuario['direccion']:10}{datos_usuario['telefono']:10}")
            print("")
            print(f"TARJETAS A CARGO")
            cards = datos_usuario["tarjetas_a_cargo"]
            print(Template("$codigo"     "$saldo"     "$estado").substitute(codigo = "Codigo", saldo="Saldo", estado="Estado"))
            for i in cards:
                print(Template("$codigo"     "$saldo"     "$estado").substitute(codigo = i[0], saldo=i[1], estado=i[2]))      
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

#Revisar formatos de salida con cadenas para mejor la salida.
# lista = [{"cedula":"1065875449","nombre":"Didier Guerrero","direccion":"calle 5 N 10-12","telefono":"3208777146"},
#          {"cedula":"18925019","nombre":"Juan Abello","direccion":"calle 5 N 10-12","telefono":"3208777146"},
#          {"cedula":"9150234","nombre":"Lorena Beltran Castro","direccion":"calle 5 N 10-12","telefono":"3208777146"},
#          {"cedula":"1001890234","nombre":"Nicolas Bohorquez","direccion":"calle 5 N 10-12","telefono":"3208777146"},
#          ]

# gap = ' '*3
# encabezado = f"{'Cedula':^10s}{gap}{'Nombre':^25s}{gap}{'Dirección':^15s}{gap}{'Telefono':^10s}"

# print("="*70)
# print(encabezado)
# print("-"*70)


# for i in lista: 
#     #print(i)
#     #print(f"{i['cedula']}")
#     rec = f"{i['cedula']:>10s}{gap}{i['nombre']:25s}{gap}{i['direccion']:15}{gap}{i['telefono']:10}"
#     print(rec)