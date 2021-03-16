Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
PreguntaGradoTemp = 'Ingrese una temperatura en °C'

valorIngresado = float (input(PreguntaGradoTemp))
Temperatura_Corporal.append (valorIngresado)
print (Temperatura_Corporal)

#.......Estado de la temperatura.......#
EstadoTemperatura = []
for elemento in Temperatura_Corporal:
    EstadoTemperatura = ''
    if (elemento < 36):
        EstadoTemperatura = 'Hipotermia'
    elif (elemento >= 37.6):
        EstadoTemperatura = 'Fiebre'
    elif (elemento >= 36 and elemento <37.6):
        EstadoTemperatura = 'temperatura normal'
    Temperatura_Corporal.append (EstadoTemperatura)
