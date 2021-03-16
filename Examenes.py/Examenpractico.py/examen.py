PreguntaNumero = '''Ingrese alguna de estas opciones
    1. Hacer conversión de pesos a dolares o euros
    2. Agreugue un valor a la lista de pesos
    3. Mostrar valor más alto, más bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
'''

listaPesos = [20000,30000,4000,2500,1000,7600]
opcionEscogida = int(input(PreguntaNumero))
while (opcionEscogida !=5):
    if (opcionEscogida == 1):
        print ('Escogiste 1')
    elif (opcionEscogida == 2):
        print ('Escogiste 2')
    elif (opcionEscogida == 3):
        print ('Escogiste 3')
    elif (opcionEscogida == 4):
        print ('Escogiste 4')
    else:
        print ('Respuesta no valida')
    opcionEscogida = int(input(PreguntaNumero))

print ('Feliz día')

