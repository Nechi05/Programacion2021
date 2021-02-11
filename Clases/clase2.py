# estos son booleans, variables de valor falso y verdadero
pruebaV = True
pruebaF = False
print(pruebaV)
print(pruebaF)
edad = 20
estatura = 1.84
peso = 76
NOMBRE = "Abraham Iriarte Naranjo"
ismayorEdad = edad >= 18
print("#"*15, "hola", "#"*15)
print(ismayorEdad)
print("#"*15, "bajo la estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print(isMayorEstatura)
# calculando si el peso es diferente de 76
print("#"*15, "peso diferente de 76", "#"*15)
ispesoDiferente = peso != 76
print(ispesoDiferente)
# vamos a ver si un apellido está en el nombre completp
apellido = "Iriarte"
isApellido = apellido in NOMBRE
print("#"*15, "está apellido en el nombre?", "#"*15)
print (isApellido)
