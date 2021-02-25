#......Mensajes......#
SALUDAR = 'Bienvenido, te apoyaré en tu ahorro'
MENSAJE_AHORRO = 'LLEVAS AHORRADO ...'
PREGUNTA_VALOR_PC = 'Cuanto vale el pc que quieres? '
PREGUNTA_CUANTO_TIENE = 'Cuanto tienes ahorrado? '

#...Entrada al código...#
print(SALUDAR)
valor = float (input(PREGUNTA_VALOR_PC))
ahorrado = float (input(PREGUNTA_CUANTO_TIENE))

while (valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "Aún te faltan ...", valor - ahorrado)
    ahorrado = ahorrado + 1000 
print (valor == ahorrado)