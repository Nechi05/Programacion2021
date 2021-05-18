#----------Restar dos números -----------#
def restar (a = 0, b = 0):
    resta = a - b
    return resta
#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0):
    multiplica = a * b
    return multiplica
#----------dividir dos números -----------#
def dividir (a = 0, b = 1):
    dividi = a / b
    return dividi

#------------ Funciones dependientes de otras-------#
def calcular (operacion, numeroA, numeroB):
    print (operacion(numeroA,numeroB))


print(restar(83,87))
print(multiplicar(83,87))
print(dividir(83,87))
print(dividir()) 

calcular (multiplicar,63,67)