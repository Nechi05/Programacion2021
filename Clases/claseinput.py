#..........Constantes........#
MENSAJE_BIENVENIDA = "Bienvenido"
PREGUNTA_NOMBRE = "Cómo te llamas? : "
PREGUNTA_EDAD = "Cuantos años tienes? : "
PREGUNTA_ESTATURA = "Cuanto Mides? : "
PREGUNTA_IMC = "Quieres conocer tu Indice de masa corporal? : "
MENSAJE_SALUDO = " Un gusto conocerte"

#......Entrada al código......#
print(MENSAJE_BIENVENIDA)
nombre = input(PREGUNTA_NOMBRE)
print(MENSAJE_SALUDO,nombre)
edad = int(input(PREGUNTA_EDAD))
estatura = float(input(PREGUNTA_ESTATURA))
imc = input(PREGUNTA_IMC)