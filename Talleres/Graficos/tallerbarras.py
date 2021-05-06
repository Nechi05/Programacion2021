import matplotlib.pyplot as plt

meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
ingresos = [908526,998526,908526,908526,1108526,968526,978526,1408526,959526,999526,908526,1500526]

plt.bar (meses,ingresos,width=0.8, color='c')
plt.title('Ingresos de un trabajador colombiano promedio en 2020')
plt.xlabel ('Mes')
plt.ylabel('Ingresos')
plt.savefig('TallerGraficoBarras.png')

plt.show()