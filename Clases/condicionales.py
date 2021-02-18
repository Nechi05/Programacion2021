#.......constantes.......#
MENSAJE_BIENVENIDA = "Hola, espero que estes bien"
MENSAJE_MAYOR = "El numero A es mayor que B"
MENSAJE_MENOR = "El numero A es menor que B"
MENSAJE_IGUAL = "A y B son iguales"
PREGUNTA_NUMERO_A = "Ingrese numero A : "
PREGUNTA_NUMERO_B = "Ingrese numero B : "

#......Entrada al código......#
print (MENSAJE_BIENVENIDA)
numeroA = int (input(PREGUNTA_NUMERO_A))
numeroB = int (input(PREGUNTA_NUMERO_B))
ismayor = numeroA > numeroB
ismenor = numeroA < numeroB

if (ismayor):
    print(MENSAJE_MAYOR)
elif (ismenor):
    print(MENSAJE_MENOR)
else:
    print(MENSAJE_IGUAL)