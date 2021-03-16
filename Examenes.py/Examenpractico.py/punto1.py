listaPesos = [20000,30000,4000,2500,1000,7600]
PreguntaMoneda = '''
    C - Mostrar original en Pesos Colombianos
    D - Mostrar en Dolares 
    E - Mostrar en Euros
'''
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento*0.00023,2)
    listaEuros.append (conversor)

ListaDolares = []
for elemento in listaPesos:
    conversor = round (elemento*0.00028,2)
    ListaDolares.append (conversor)

opcionMoneda = input (PreguntaMoneda)
if (opcionMoneda == 'C'):
    print ('Mostrando lista original')
print (listaPesos)
elif (opcionMoneda == 'D'):
    print ('Mostrando la lista en dolares' )
    print (ListaDolares)
elif (opcionMoneda == 'E'):
    print ('Mostrando la lista en euros')
    print (listaEuros)
else:
    print ('Valor ingresado no válido')
