import sys
nombre = input('ingrese su nombre : ')
edad = int(input('ingrese su edad : '))
estatura = float (input('ingrese su estatura : '))

nombreArchivo = 'estudiantes.txt'
try:
    archivo = open (nombreArchivo)
    print('1')
except FileNotFoundError:
    archivo = open (nombreArchivo,'w',encoding='UTF-8')
    description = 'Archivo de datos de estudiantes'
    archivo.writelines(description)
    sys.exit(1)

archivo = open (nombreArchivo,'a')
linea = '\nnombre: ' + nombre + ' edad: '+ str(edad) + ' estatura: ' + str(estatura)
archivo.writelines(linea)
archivo.close()

#leer
with open (nombreArchivo) as reader:
    for linea in reader:
        print (linea)