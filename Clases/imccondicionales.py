#......Constantes......#
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en mts? : "
MENSAJE_BIENVENIDA = "Hola buen día? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es de..."
MENSAJE_RESULTADO = "El resultado de la prueba de obesidad es..."
MENSAJE_BAJO_PESO = "Estas bajitico de peso pa, a comer"
MENSAJE_ADECUADO = "Estás dentro de tu peso ideal"
MENSAJE_SOBREPESO = "Ten cuidado, estas en sobre peso"
MENSAJE_OBESO = "Cuidado! estás obeso, tu salud corre riesgo"

#......Entrada al código......#
print(MENSAJE_BIENVENIDA)
peso = float(input(PREGUNTA_PESO))
estatura = float(input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isAdecuado = imc >= 18.5 and imc < 25
isSobrepeso = imc >= 25 and imc < 30
resultado = ""
if(isBajoPeso):
    resultado = (MENSAJE_BAJO_PESO)
elif(isAdecuado):
    resultado(MENSAJE_ADECUADO)
elif(isSobrepeso):
    resultado(MENSAJE_SOBREPESO)
else:
    resultado(MENSAJE_OBESO)
print(MENSAJE_DESPEDIDA, imc)
print(resultado)
