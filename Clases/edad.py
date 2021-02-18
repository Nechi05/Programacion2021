#......Entradas......#
MENSAJE_BIENVENIDA = "Bienvenido al código, averiguaremos si eres mayor de edad"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad, puedes seguir"
MENSAJE_MENOR_EDAD = "Eres menor de edad, no puedes seguir"
PREGUNTA_EDAD = "Cuantos años tienes? : "

#......Entrada al código......#
print(MENSAJE_BIENVENIDA)
edad = int(input(PREGUNTA_EDAD))
ismayor = edad > 18
if(ismayor):
    print(MENSAJE_MAYOR_EDAD)
else:
    print(MENSAJE_MENOR_EDAD)