cedula = "1098621411"
nombre = "juan andres"
apellido = "abello contreras"
direccion = "gamarra cesar"
telefono = "3157700754"

usuario= {}
cod_tarjeta=123789
saldo =0
estado=True

usuario[cedula]={"nombre":nombre,"apellido":apellido,"direccion":direccion,"telefono":telefono,"tarjetas":[]}
valor=usuario[cedula]
valor["tarjetas"]=[cod_tarjeta,saldo,estado]

print(usuario)