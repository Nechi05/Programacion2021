texto = 'Hola, espero estés bien'
lista = [1,2,3,4]
lista.sort()
print (lista)
lista.pop(2)
for elemento in lista:
    print (elemento)
    for i in range (len(lista)):
        print (lista[i])

for letra in texto:
    print (letra)

#Separar cada palabra
palabras = texto.split (' ')
print (palabras)
#--Preguntar el tipo--
print (type(palabras))
#Eliminar una letra en especifico
eliminarE= texto.split('e')
datos = 'nombre;apellido;edad'
print (datos.split(';'))
print (eliminarE)
#Unir algo que ya se separó
uniendo = 'i'.join(eliminarE)
print (uniendo)
info = ' '.join(datos.split(';'))
print (info)

#codigoASCI
listaNombres = ['Juan','Laura','Katherine','Mario','daniel',]
print (max(listaNombres))
#comparar strings según el tamaño
print (max(listaNombres, key=len))


respuesta = input('Ingrese Si o No: ')
print (respuesta.upper())
if respuesta.upper() == 'SI':
    print ('Hola, Bienvenido al programa')
else:
    print ('chao!!')

nombre = input ('Ingrese su nombre: ')
print (nombre.capitalize())
print (type(nombre))

#minuscula y la primera mayuscula
correo = 'ESPERO ESTES BIEN'
print (correo.casefold().capitalize())

#que algo quede en el centro
saludo = 'Hola como estas? '
nombre = 'Maria'
print (saludo.center(50))
print (nombre.center(50))

#saber si lo que ingreso el usuario está bien
numeroId = '198765'
print (numeroId.isnumeric())

#todo parrafo debería terminar en punto
parrafo = 'hola jabhsbjaghsd hagagdsajadgsd hgdshgfsghfgvf.'
print (parrafo.endswith('.'))