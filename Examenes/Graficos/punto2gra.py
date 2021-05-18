import matplotlib.pyplot as plt
pieLabels = ['Medellín', 'Cali', 'Bogotá', 'Barcelona','París']
sizes = [2.56,2.22,7.18,1.62,2.16]
pieExplode = [0.2,0,0,0,0]

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*15.74,2)
        pieLabels[i] += indicador+str(porcentaje) +'Millones de habitantes'


etiquetarElementosPorcentuales(sizes,pieLabels,' -- ')

plt.pie (sizes,labels=pieLabels,
        explode=pieExplode,
        shadow= True,
        counterclock = True,
        startangle= 45)
#....................#
plt.title('''Mis 5 ciudades favoritas del mundo
                 + En millones de habitantes''')
plt.savefig('Examentorta.png')
#...................#
plt.show()