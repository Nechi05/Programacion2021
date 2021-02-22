#.......CONSTANTES......#
PREGUNTA_NUMERO_A = "Ingrese Numero A : "
PREGUNTA_NUMERO_B = "Ingrese Numero B : "
MENSAJE_BIENVENIDA = "Hola, bienvenido"
PREGUNTA_MAYOR = "El numero A es mayor al numero B? "
PREGUNTA_MENOR = "El numero A es menor al numero B? "
PREGUNTA_IGUAL = "Estos dos numeros son iguales? "

#......ENTRADA AL CÓDIGO......#
print(MENSAJE_BIENVENIDA)
numeroA = int(input(PREGUNTA_NUMERO_A))
numeroB = int(input(PREGUNTA_NUMERO_B))
ismayor = numeroA > numeroB
print(PREGUNTA_MAYOR, ismayor)
ismenor = numeroA < numeroB
print(PREGUNTA_MENOR, ismenor)
isigual = numeroA == numeroB
print(PREGUNTA_IGUAL, isigual)
sumar = numeroA + numeroB
print("La suma de estos dos numeros es", sumar)
restar = numeroA - numeroB
print("la resta de estos dos numeros es", restar)
multiplicar = numeroA * numeroB
print("la multiplicación entre A y B es", multiplicar)
dividir = numeroA / numeroB
print("la division entre A y B dió como resultado", dividir)