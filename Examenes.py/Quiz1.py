#............Perfil Lipidico............#
#......Constantes......#
MENSAJE_BIENVENIDA = "Hola, a continuación vamos a averiguar el estado en el que están tus niveles de triglicéridos y de homocisteína"
VALOR_TRI = "Cual es el nivel de trigliceridos en sangre del paciente en mg/dL? : "
VALOR_HOMO = "Cual es el nivel de homocisteína en sangre del paciente en µmol/L? : "
MENSAJE_OPTIMO_TRI = "El nivel de trigliceridos en sangre es óptimo"
MENSAJE_OPTIMO_HOMO = "El nivel de homocisteína en sangre es óptimo"
MENSAJE_LIMIOPTIMO_TRI = "El nivel de trigliceridos en sangre está al límite del rango que se considera saludable"
MENSAJE_LIMIOPTIMO_HOMO = "El nivel de homocisteína en sangre está al límite del rango que se considera saludable"
MENSAJE_ALTO_TRI = "El nivel de trigliceridos en sangre es alto, ¡CUIDADO!"
MENSAJE_ALTO_HOMO = "El nivel de homocisteína en sangre es alto, ¡CUIDADO!"
MENSAJE_MUYALTO_TRI = "El nivel de trigliceridos en sangre es MUY ALTO, ¡RIESGOSO!"
MENSAJE_MUYALTO_HOMO = "El nivel de homocisteína en sangre es MUY ALTO, ¡RIESGOSO!"
MENSAJE_DESPEDIDA = "Espero haber sido de ayuda, hasta pronto."

#......Entrada al código......#
print(MENSAJE_BIENVENIDA)
trigliceridos = int(input(VALOR_TRI))
homocisteína = int(input(VALOR_HOMO))
isoptimotri = trigliceridos < 150 
isptimohomo = homocisteína >= 2 and homocisteína < 15
islimioptimotri = trigliceridos >= 150 and trigliceridos < 199
islimioptimohomo = homocisteína >= 15  and homocisteína < 30
isaltotri = trigliceridos >=200 and trigliceridos < 499
isaltohomo = homocisteína >=30 and homocisteína < 100
ismuyaltotri = trigliceridos > 500
ismuyaltohomo = homocisteína > 100

resultado = ""
#Trigliceridos
if(isoptimotri) :
    resultado = (MENSAJE_OPTIMO_TRI)
elif(islimioptimotri) : 
    resultado = (MENSAJE_LIMIOPTIMO_TRI)
elif(isaltotri) : 
    resultado = (MENSAJE_ALTO_TRI)
else :
    resultado = (MENSAJE_MUYALTO_TRI)
print(resultado)
#Homocisteína
if(isptimohomo) :
    resultado = (MENSAJE_OPTIMO_HOMO)
elif(islimioptimohomo) : 
    resultado = (MENSAJE_LIMIOPTIMO_HOMO)
elif(isaltohomo) : 
    resultado = (MENSAJE_ALTO_HOMO)
else :
    resultado = (MENSAJE_MUYALTO_HOMO)
print(resultado)

print(MENSAJE_DESPEDIDA)