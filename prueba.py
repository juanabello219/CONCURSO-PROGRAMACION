def search_user(data_users):
    cedula = input("Ingrese la cedula a consultar: ")
    for row in data_users:
        valor = list(row.keys())
        #print(valor)
        if valor[0] == cedula:
            print("="*90)
            print("                       DATOS DEL USUARIO                       ")
            gap = ' '*3
            encabezado = f"{'Cedula':^10s}{gap}{'Nombres y apellidos':^35s}{gap}{'Dirección':^15}{gap}{'Telefono':^10s}"
            print("="*90)
            print(encabezado)
            print("-"*90)
            datos_usuario=row[cedula]
            #print(datos_usuario)
            rec = f"{cedula:>10s}{gap}{datos_usuario['nombre']:17s}{datos_usuario['apellido']:18s}{gap}{datos_usuario['direccion']:^15}{gap}{datos_usuario['telefono']:^10}"
            print(rec)
            # print(f"TARJETAS A CARGO")
            # cards = datos_usuario["tarjetas_a_cargo"]
            # print(Template("$codigo"     "$saldo"     "$estado").substitute(codigo = "Codigo", saldo="Saldo", estado="Estado"))
            # for i in cards:
            #     print(Template("$codigo"     "$saldo"     "$estado").substitute(codigo = i[0], saldo=i[1], estado=i[2]))      
            # print("")
            return True
        else:
            print("El usuario no esta registrado en el sistema.")
            return False