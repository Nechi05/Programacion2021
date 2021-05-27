# Se sabe que un Dólar son 0.82 euros, indique a un usuario que ingrese su
# dinero en dólares y su nombre, luego muestre en pantalla el nombre del usuario y cuanto
# dinero tiene en euros (recuerde validar que todos los datos ingresados por el usuario sean
# del formato correcto).

listaDolares = []
preguntaNombre = '¿Cómo es tu nombre?: '
preguntaDolares = 'Ingresa tu dinero en dolares: '

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        nombre = input('ingrese su Nombre :')
        assert (nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('ingresaste un dato no válido')
valorIngresado = float (input(preguntaDolares))
listaDolares.append(valorIngresado)
print (f'{nombre}, Este es tu dinero en dolares' ,listaDolares)

listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento*0.82,2)
    listaEuros.append (conversor)
    print ('Y este es tu dinero en euros',listaEuros)

