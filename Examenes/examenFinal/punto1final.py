# Solicite a un usuario que ingrese sus 8 alimentos favoritos y sus precios
# luego realice un gráfico de barras con la información ingresada (recuerde poner título al
# gráfico y a sus ejes también recuerde guardar el resultado en un archivo png)

import matplotlib.pyplot as plt
def agregarElementos (preguntaFoods, preguntaPrecios):
    listaFoods = []
    listaPrecios = []
    for i in range (8):
        print (f'ingresando alimento {i+1} de 8')
        listaFoods.append (input(preguntaFoods))
        listaPrecios.append (float(input(preguntaPrecios)))
    return listaFoods, listaPrecios

#........Mensajes.......#
preguntaFoods = 'Ingresa tu alimento favorito: '
preguntaPrecios = 'Ingresa el precio del alimento: '
listaFoods, listaPrecios = agregarElementos(preguntaFoods,preguntaPrecios)
print(listaFoods,listaPrecios)
plt.bar (listaFoods, listaPrecios)
plt.title('Mis 8 alimentos favoritos')
plt.xlabel('Nombres')
plt.ylabel('Precios')
plt.savefig('alimentosFav.png')
plt.show()