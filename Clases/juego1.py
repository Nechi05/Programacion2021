#......MENSAJES......#
MENSAJE_SALUDO = 'Bienvenido a este programa, Come on'
PREGUNTA_NUMERO = '''
            En este juego debes asertar un numero entero
            que va   
            del 1 - 10
            lo puedes intentar las veces que quieras
            SUERTE, ingresa tu número

'''
PREGUNTA_FALLIDA = 'Aaaaah! Fallaste, ingresa otro número '
MENSAJE_GANASTE = 'Felicidades, ganaste!'
MENSAJE_PERDISTE = 'Perdiste! vuelve a intentarlo,'
#...Entrada al código...#
numeroOculto = 7
vidas = 5
print (MENSAJE_SALUDO)
numeroIngresado = int(input(PREGUNTA_NUMERO))
if (numeroIngresado != numeroOculto):
    vidas-=1
while (numeroOculto != numeroIngresado and vidas >0) :
    numeroIngresado = int(input(PREGUNTA_FALLIDA))
    vidas-=1
if (vidas >=0 and numeroOculto == numeroIngresado):
    print (MENSAJE_GANASTE)
    print (vidas)
else:
    print(MENSAJE_PERDISTE, "el número era el ", numeroOculto)