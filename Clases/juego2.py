
import random
#......MENSAJES......#
MENSAJE_SALUDO = 'Bienvenido a este programa, Come on'
PREGUNTA_NUMERO = '''
            En este juego debes asertar un numero entero
            que va   
            del 1 - 10
            lo puedes intentar las veces 
            que quieras hasta que se te acaben las vidas
            SUERTE, ingresa tu número

'''
PREGUNTA_DIFICULTAD = '''
    1- Fácil
    2- Moderado
    3- Difícil
'''
PREGUNTA_FALLIDA = 'Aaaaah! Fallaste, ingresa otro número '
MENSAJE_GANASTE = 'Felicidades, ganaste!'
MENSAJE_PERDISTE = 'Perdiste! vuelve a intentarlo,'
#...Entrada al código...#
numeroOculto = random.randint(1,10)
vidas = None
dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ('Ingrese una opción válida')
    dificultad = int(input(PREGUNTA_DIFICULTAD))

if (dificultad ==1):
    print ('Modo fácil activado')
    vidas = 5
elif (dificultad ==2):
    print ('Modo moderado activado')
    vidas = 3
else :
    print ('Modo difícil activado, con cuidado!')
    vidas = 1

numeroIngresado = int (input(PREGUNTA_NUMERO))
while (numeroIngresado != numeroOculto and vidas > 1):
    vidas -=1
    print (f'te quedan {vidas} vidas')
    numeroIngresado = int(input(PREGUNTA_FALLIDA))

if (vidas >= 0 and numeroIngresado == numeroOculto):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE, 'el numero era el', numeroOculto)