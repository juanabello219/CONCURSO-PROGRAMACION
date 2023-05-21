def search_user(datos_usuarios, cedula):
    for row in datos_usuarios:
        #print(row)
        valor = list(row.keys())
        print(valor)
        if valor[0] == cedula:
            return True
        else:
            print("El usuario no esta registrado en el sistema.")
            return False