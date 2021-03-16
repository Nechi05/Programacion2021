#......Preguntas......#
PreguntaNumero = ''' Ingrese una de estas opciones para: 
    1. Convertir las temperaturas en °C a K o °F
    2. Conocer el estado en que se encuentra el paciente 
    3. Conocer la temperatura más alta y más baja
    4. Salir
'''
PreguntaTemperatura = ''' 
    C. Mostrar temperatura Original
    F. Mostrar temperatura en grados Fahrenheit
    K. Mostrar temperatura en grados Kelvin
'''
PreguntaGradoTemp = 'Ingrese una temperatura en °C : '
#............Mensajes..........#
MensajeBienvenida = "Buen día, te doy la bienvenida a NeoNatalChild"
MensajeOpcionC = 'La conversión no es necesaria'
MensajeOpcionF = 'Mostrando temperatura en °F'
MensajeOpcionK = 'Mostrando temperatura en K'
MensajeDespedida = "Feliz día, hasta pronto"

MensajeMayor = 'La temperatura máxima es ...'
MensajeMenor = 'La temperatura mínima es ...'
MensajeSaliendo = 'Saliendo del programa'
#..........Error...........#
MensajeNoValido = 'Opción ingresada no válida'

Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#...Entrada al código...#
print (MensajeBienvenida)
#.......ConversionPuntoUno.............#
TemperaturaFahrenheit = []
for elemento in Temperatura_Corporal:
    conversor = round (elemento*1.8+32)
    TemperaturaFahrenheit.append (conversor)
TemperaturaKelvin = []
for elemento in Temperatura_Corporal:
    conversor = round (elemento+273.15)
    TemperaturaKelvin.append (conversor)

opcionEscogida = int(input(PreguntaNumero))
while (opcionEscogida !=5):
#....OpcionUno.....#
    if (opcionEscogida == 1):
        OpcionTemperatura = input (PreguntaTemperatura)
        if (OpcionTemperatura == 'C'):
            print (MensajeOpcionC)
            print (Temperatura_Corporal)
        elif (OpcionTemperatura == 'F'):
            print (MensajeOpcionF)
            print (TemperaturaFahrenheit)
        elif (OpcionTemperatura == 'K'):
            print (MensajeOpcionK)
            print (TemperaturaKelvin)
        else:
            print (MensajeNoValido)
#......OpcionDos.......#
    elif (opcionEscogida == 2):
        valorIngresado = float (input(PreguntaGradoTemp))
        Temperatura_Corporal.append (valorIngresado)
        if (valorIngresado < 36):
            print ('El paciente presenta Hipotermia')
        elif (valorIngresado >= 37.6):
            print ('El paciente presenta Fiebre')
        elif (valorIngresado >= 36 and valorIngresado < 37.6):
            print ('El paciente presenta temperatura normal')
#......OpcionTres.......#
    elif (opcionEscogida == 3):
        print (MensajeMayor, max (Temperatura_Corporal))
        print (MensajeMenor, min (Temperatura_Corporal))
#......OpcionCuatro......#
    elif (opcionEscogida == 4):
        print (MensajeSaliendo)
    else:
        print (MensajeNoValido)
    opcionEscogida = int(input(PreguntaNumero))
print (MensajeDespedida)