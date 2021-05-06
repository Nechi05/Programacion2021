import matplotlib.pyplot as plt
pieLabels = ['Medellín', 'Cali', 'Bogotá', 'Pasto','Pereira']
sizes = [40,25,15,10,10]
pieExplode = [0,0,0.2,0,0]

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100,2)
        pieLabels[i] += indicador+str(porcentaje) +'Millones de habitantes'


etiquetarElementosPorcentuales(sizes,pieLabels,' -- ')

plt.pie (sizes,labels=pieLabels,
        explode=pieExplode,
        shadow= True,
        counterclock = True,
        startangle= 45)
#....................#
plt.title('''Las 5 ciudades mas importantes de Colombia
                 + En millones de habitantes''')
plt.savefig('tallertorta.png')
#...................#
plt.show()