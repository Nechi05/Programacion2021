#Un consultorio de neurología desea tener un archivo para el manejo de
# los clientes, se pide que desarrolle un programa que en su primera ejecución cree el archivo
# llamado pacientes.txt. Luego en cada ejecución se preguntará por el nombre del paciente, una
# descripción de la enfermedad y el precio de la consulta (se deben almacenar estos datos
# nuevos en el archivo pacientes.txt).

import sys
nombre = input ('Ingrese el nombre del paciente: ')
enfermedadEntrada = input ('¿Qué enfermedad tiene este paciente?: ')
precio = input('Ingrese el precio de la consulta: ')

nombreArchivo = "Pacientes.txt"
try:
    archivo = open (nombreArchivo)
    print ('1')
except FileNotFoundError:
    archivo = open (nombreArchivo, 'w',encoding='UTF-8')
    descripcion = 'Información pacientes'
    print ('2')
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo,'a')
linea = "\nnombre:" + nombre + " enfermedad: " + enfermedadEntrada + " precio: "+ str(precio)
archivo.writelines(linea)
archivo.close()

#leer
with open (nombreArchivo,'r') as reader:
    for line in reader:
        print(line)



