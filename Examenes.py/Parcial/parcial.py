#......Pacial 8/04/2021......#
#......Punto1.....#
def sumar (a=0,b =0):
    suma = a + b 
    return suma
def restar (a=0,b=0):
    resta = a - b 
    return resta
def multiplicar (a=0,b=0):
    multiplica = a*b
    return multiplica
def dividir (a=0,b=1):
    divide = a/b
    return divide
def potenciar (a=1,b=1):
    potencia = a**b
    return potencia
print (sumar(245,623))
print (restar(521,115))
print (multiplicar(12,7))
print (dividir(741,3))
print (potenciar(4,8))
#.....Punto2.....#
def mostarlista (listadeEntrada = []):
    for elemento in listadeEntrada:
        print (elemento)
    return None
def linedesign(cantidad = 10, simbolo = '#'):
    print(simbolo *cantidad)
    return None
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista3 = [9,10,11,12]
linedesign (3, '.......')
mostarlista (lista1)
linedesign(3,'...........')
mostarlista (lista2)
linedesign (3,'..........')
mostarlista (lista3)
#.....Punto3.....#
base = float(input('Asigne la base de su triangulo: '))
altura = float(input('Asigne la altura de su triangulo: '))
def areaTriangulo (b,h):
    area = (b*h)/2 
    return area
resultado = areaTriangulo (base,altura)
print (f'el area del triangulo es {resultado}')
#.....Punto4.....#
promedio = ()
maximo = ()
minimo = ()
listaEnteros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def mostrarlimites (listaEnteros):
    promedio = round (sum(listaEnteros)/len(listaEnteros))
    maximo = round (max (listaEnteros),2)
    minimo = round (min (listaEnteros),2)
print ('El promedio es', promedio)
print ('El maximo es', maximo)
print ('El minimo es', minimo)
#.....Profe no pude aquí, me sale
#......que no está definida la variable pero no supe como resolverlo
#...... y se acabó el tiempo, lo subiré...
#......Punto5......#
fibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144,...]