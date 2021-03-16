Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

PreguntaTemperatura = ''' 
    C. Mostrar temperatura Original
    F. Mostrar temperatura en grados Fahrenheit
    K. Mostrar temperatura en grados Kelvin
'''

MensajeOpcionC = 'La conversión no es necesaria'
MensajeOpcionF = 'Mostrando temperatura en °F'
MensajeOpcionK = 'Mostrando temperatura en K'
MensajeNoValido = 'Opción ingresada no válida'

TemperaturaFahrenheit = []
for elemento in Temperatura_Corporal:
    conversor = round (elemento*1.8+32)
    TemperaturaFahrenheit.append (conversor)

TemperaturaKelvin = []
for elemento in Temperatura_Corporal:
    conversor = round (elemento+273.15)
    TemperaturaKelvin.append (conversor)

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

