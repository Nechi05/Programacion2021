#......Constantes......#
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en mts? : "
MENSAJE_BIENVENIDA = "Hola cómo estás? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es de..."
MENSAJE_RESULTADO = "El resultado de la prueba de obesidad es..."
#......Entrada al código......#
print(MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print(MENSAJE_DESPEDIDA, IMC)
isObeso = IMC>= 30
print(MENSAJE_RESULTADO,isObeso)
