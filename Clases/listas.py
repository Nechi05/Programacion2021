nombres = []
print (type(nombres))
print (nombres)
nombres = ['Julio','Samuel','Aleja','Felipe']
print (nombres)
print (nombres [2])
nombres.append ('Ricardo')
print (nombres)
print (nombres [2])
edades = [17,25,19,20,21,18,23,24,29]
estatura = [1.84,1.67,1.70,1.78]
#al ultimo
print (edades[-2])

print (edades[0:2])
print (edades[:3])
print (edades[2:])
print (edades[:])
edades.sort ()
print (edades)
edades.sort (reverse=True)
print (edades)
mayor = max (edades)
print (mayor)
menor = min(edades)
print (menor)
#como contamos cuantos elementos hay
largoListaEdades = len (edades)
print (largoListaEdades)
#como sumamos elementos?
sumaEdades = sum (edades)
print (sumaEdades)
#como calculo el promedio?
promedioEdades = sumaEdades / largoListaEdades
print (promedioEdades)
#eliminar elementos de la lista
edades.pop (2)
print (edades)

#ciclo for y las listas
largoListaEdades = len (edades)
for indice in range (largoListaEdades):
    print (edades[indice])