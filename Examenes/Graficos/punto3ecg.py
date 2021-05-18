import pandas as pd
import matplotlib.pyplot as plt

ecgDatos = pd.read_csv('ecgExamen.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print (ecgDatos.keys ())

muestras = list(ecgDatos['muestra'].values())
print (muestras)

valor = list(ecgDatos['valor'].values())
print (valor)

plt.plot(muestras, valor)
plt.title('Electrogardiograma')
plt.savefig('EcgExamen.png')
plt.show()
